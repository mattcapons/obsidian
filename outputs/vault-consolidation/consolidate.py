#!/usr/bin/env python3
"""Prepare one root vault; retire the nested vault only after Obsidian exits."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
NESTED = ROOT / "University"
BACKUP = HERE / ".backup"
STATE = HERE / "state.json"
RETIRED = BACKUP / "retired" / "University"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def atomic_write(path, content, private=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".consolidate-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        if not private:
            os.chmod(name, path.stat().st_mode & 0o777 if path.exists() else 0o644)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def write_json(path, value, private=False):
    atomic_write(path, (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode(), private)


def backup_once(path):
    if not path.exists() and not path.is_symlink():
        return
    target = BACKUP / "before" / path.relative_to(ROOT)
    if target.exists() or target.is_symlink():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        target.symlink_to(os.readlink(path), target_is_directory=path.is_dir())
    elif path.is_dir():
        shutil.copytree(path, target, symlinks=True)
    else:
        shutil.copy2(path, target)


def copy_managed(source, target, state, content=None, replace=False):
    """Refresh our own copies; preserve independently edited destinations."""
    content = source.read_bytes() if content is None else content
    rel = str(target.relative_to(ROOT))
    wanted = hashlib.sha256(content).hexdigest()
    actual = digest(target)
    previous = state["copies"].get(rel)
    if actual == wanted:
        state["copies"][rel] = actual
        return
    if actual is not None and actual != previous and not (replace and previous is None):
        if source.is_relative_to(NESTED / "copilot/skills"):
            return  # Root has the newer bundled skills; the nested copy is backed up.
        alternate = target.with_name(target.stem + " (from University)" + target.suffix)
        if alternate.exists() and digest(alternate) != wanted:
            alternate = target.with_name(target.stem + " (from University " + wanted[:8] + ")" + target.suffix)
        target = alternate
        rel = str(target.relative_to(ROOT))
        state["conflicts"].append(rel)
    if target.exists():
        backup_once(target)
    atomic_write(target, content, private=target.name == "data.json")
    state["copies"][rel] = wanted


def remap_workspace(value):
    def path_for_root(path):
        if not isinstance(path, str) or not path or path.startswith(("University/", "copilot/", ".obsidian/")):
            return path
        if path.startswith(("/", "http:", "https:", "obsidian:")):
            return path
        return "University/" + path

    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if key == "file":
                result[key] = path_for_root(item)
            elif key == "lastOpenFiles" and isinstance(item, list):
                result[key] = [path_for_root(path) for path in item]
            else:
                result[key] = remap_workspace(item)
        return result
    if isinstance(value, list):
        return [remap_workspace(item) for item in value]
    return value


def prepare(state):
    BACKUP.mkdir(parents=True, exist_ok=True)
    os.chmod(BACKUP, 0o700)
    ignore = ROOT / ".gitignore"
    rules = ["outputs/vault-consolidation/.backup/", "outputs/vault-consolidation/state.json"]
    text = ignore.read_text()
    missing = [rule for rule in rules if rule not in text.splitlines()]
    if missing:
        backup_once(ignore)
        atomic_write(ignore, (text.rstrip() + "\n\n# Local vault-consolidation backups and state\n" + "\n".join(missing) + "\n").encode())
    for rel in [".obsidian", "University/.obsidian", "University/copilot", "University/.agents", "University/.copilot"]:
        backup_once(ROOT / rel)

    chats = NESTED / "copilot"
    if chats.is_dir():
        for source in sorted(chats.rglob("*")):
            if source.is_file():
                copy_managed(source, ROOT / "copilot" / source.relative_to(chats), state)

    config = NESTED / ".obsidian"
    if config.is_dir():
        for source in sorted(config.rglob("*")):
            if not source.is_file():
                continue
            rel = source.relative_to(config)
            target = ROOT / ".obsidian" / rel
            if rel.parts[0] == "ipynb-runtimes":
                continue  # Machine-local kernel ownership is not vault configuration.
            if str(rel) == "community-plugins.json":
                existing = json.loads(target.read_text()) if target.exists() else []
                incoming = json.loads(source.read_text())
                content = (json.dumps(list(dict.fromkeys(existing + incoming)), indent=2) + "\n").encode()
                copy_managed(source, target, state, content, replace=True)
            elif rel.name.startswith("workspace") and rel.suffix == ".json":
                content = (json.dumps(remap_workspace(json.loads(source.read_text())), indent=2, ensure_ascii=False) + "\n").encode()
                copy_managed(source, target, state, content, replace=True)
            elif str(rel) == "plugins/copilot/data.json":
                settings = json.loads(source.read_text())
                settings.update(copilotFolder="copilot", defaultSaveFolder="copilot/copilot-conversations", projectsFolder="copilot/projects")
                content = (json.dumps(settings, indent=2, ensure_ascii=False) + "\n").encode()
                copy_managed(source, target, state, content, replace=True)
            elif not target.exists() or str(target.relative_to(ROOT)) in state["copies"]:
                copy_managed(source, target, state)
            # Keep existing root plugin versions and root preferences on overlap.

    # Portable links work on either laptop regardless of its checkout path.
    skills = ROOT / ".agents/skills"
    if skills.is_dir():
        for link in sorted(skills.iterdir()):
            target = ROOT / "copilot/skills" / link.name
            if link.is_symlink() and target.is_dir():
                portable = os.path.relpath(target, link.parent)
                if os.readlink(link) != portable:
                    backup_once(link)
                    temporary = link.with_name(link.name + ".consolidation-tmp")
                    temporary.symlink_to(portable, target_is_directory=True)
                    temporary.replace(link)

    state["prepared_at"] = int(time.time())
    state["conflicts"] = sorted(set(state["conflicts"]))
    write_json(STATE, state, private=True)
    validate(state)


def validate(state):
    for source in (NESTED / "copilot/copilot-conversations").glob("*.md"):
        relative = source.relative_to(NESTED / "copilot")
        target = ROOT / "copilot" / relative
        if digest(source) != digest(target):
            variants = list(target.parent.glob(target.stem + " (from University*" + target.suffix))
            if not any(digest(source) == digest(variant) for variant in variants):
                raise RuntimeError("A source chat was not preserved: " + str(source))
    config = json.loads((ROOT / ".obsidian/plugins/copilot/data.json").read_text())
    if config["defaultSaveFolder"] != "copilot/copilot-conversations":
        raise RuntimeError("The consolidated chat save setting is incorrect.")
    for link in (ROOT / ".agents/skills").iterdir():
        if link.is_symlink() and not link.exists():
            raise RuntimeError("A skill link does not resolve: " + str(link))
    count = len(list((ROOT / "copilot/copilot-conversations").glob("*.md")))
    projects = len(list((ROOT / "copilot/projects").glob("*/project.md")))
    print("Consolidated root:", ROOT)
    print("Saved chat files:", count, "Projects:", projects)


def require_obsidian_closed():
    if not Path("/proc").is_dir():
        raise RuntimeError("This completion command requires this laptop's Linux /proc process check.")
    for proc in Path("/proc").iterdir():
        if not proc.name.isdigit():
            continue
        try:
            exe = Path(os.readlink(proc / "exe")).name.lower()
        except (OSError, PermissionError):
            continue
        if exe in {"obsidian", "obsidian-bin", "obsidian.exe"}:
            raise RuntimeError("Obsidian is still running. Quit Obsidian completely, then run this command from your terminal.")


def registry_path():
    candidates = []
    if os.environ.get("XDG_CONFIG_HOME"):
        candidates.append(Path(os.environ["XDG_CONFIG_HOME"]) / "obsidian/obsidian.json")
    candidates.extend([
        Path.home() / ".var/app/md.obsidian.Obsidian/config/obsidian/obsidian.json",
        Path.home() / ".config/obsidian/obsidian.json",
    ])
    for candidate in candidates:
        if candidate.is_file():
            data = json.loads(candidate.read_text())
            if any(Path(v.get("path", "")).resolve() in {ROOT, NESTED} for v in data.get("vaults", {}).values()):
                return candidate
    raise RuntimeError("No vault registration for this checkout was found; no nested folders were retired.")


def finish(state):
    require_obsidian_closed()
    registry = registry_path()
    prepare(state)  # Capture the final messages and settings saved on exit.
    data = json.loads(registry.read_text())
    matching = [key for key, value in data["vaults"].items() if Path(value.get("path", "")).resolve() in {ROOT, NESTED}]
    if not matching:
        raise RuntimeError("This checkout's vault registration changed; no nested folders were retired.")
    selected = next((key for key in matching if Path(data["vaults"][key]["path"]).resolve() == ROOT), matching[0])
    entry = dict(data["vaults"][selected])
    for key in matching:
        data["vaults"].pop(key)
    entry.update(path=str(ROOT), ts=int(time.time() * 1000), open=True)
    data["vaults"][selected] = entry
    registry_backup = BACKUP / "obsidian-registry-before.json"
    if not registry_backup.exists():
        atomic_write(registry_backup, registry.read_bytes(), private=True)

    destinations = []
    for name in [".obsidian", "copilot", ".agents", ".copilot"]:
        source = NESTED / name
        destination = RETIRED / name
        if source.exists():
            if destination.exists():
                raise RuntimeError("A retirement backup already exists: " + str(destination))
            destinations.append((source, destination))
    retired = []
    try:
        for source, destination in destinations:
            destination.parent.mkdir(parents=True, exist_ok=True)
            source.rename(destination)
            retired.append((source, destination))
        atomic_write(registry, (json.dumps(data, indent=2) + "\n").encode(), private=True)
    except BaseException:
        for source, destination in reversed(retired):
            destination.rename(source)
        raise
    state["finished_at"] = int(time.time())
    write_json(STATE, state, private=True)
    print("Finished. Open Obsidian; this checkout now uses only:", ROOT)
    print("The former nested setup is preserved in:", RETIRED)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--finish", action="store_true", help="Finish only after Obsidian has fully exited.")
    args = parser.parse_args()
    state = json.loads(STATE.read_text()) if STATE.exists() else {"copies": {}, "conflicts": []}
    if state.get("finished_at"):
        print("Already consolidated. Open this folder as your vault:", ROOT)
        return
    if args.finish:
        finish(state)
    else:
        prepare(state)
        print("Prepared. The current vault is untouched so this session can finish.")
        print("After quitting Obsidian, run: python3", str(Path(__file__).resolve()), "--finish")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError) as error:
        print("Stopped:", error, file=sys.stderr)
        sys.exit(1)
