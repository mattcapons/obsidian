# Consolidate this checkout into one Obsidian vault

Use the repository folder as the vault: `/home/matteo/Documents/obsidian`.
`University` is a normal folder for course notes. Course links already use this layout.
The shared chat folder is `copilot/copilot-conversations`, and projects are in `copilot/projects`.

The preparation copies local chats, projects, settings, and missing plugins into the root vault.
It preserves the root's newer Copilot plugin and bundled skills. It also adjusts the copied
workspace's note paths and makes the root skill symlinks relative for portability.
It leaves the open University vault running so the current conversation can finish.

To complete the switch on this laptop:

1. Quit Obsidian completely after the current conversation has finished.
2. Run this command in a terminal:

   ```sh
   python3 /home/matteo/Documents/obsidian/outputs/vault-consolidation/consolidate.py --finish
   ```

3. Open Obsidian again. This checkout's registered vault will point to `/home/matteo/Documents/obsidian`.

The command refuses to retire the nested vault while Obsidian is running. After the app exits,
it refreshes the copies to include the final messages and settings, verifies that every local
chat is preserved, archives `University/.obsidian`, `University/copilot`, `University/.agents`,
and `University/.copilot`, and updates this checkout's vault registration. Unrelated vault
registrations are preserved.

Backups are local and excluded from Git in `outputs/vault-consolidation/.backup/`.
They include the previous settings and the retired nested folders. Copilot's settings file
remains excluded from Git because it can contain credentials.

On the other laptop, open the repository folder `obsidian` as the vault, rather than its
`University` subfolder. This preparation does not commit or push repository changes.
