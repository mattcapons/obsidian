from pathlib import Path
import math
import re
import sys

sys.path.insert(0, '/tmp/aapp-pdf-tools')
import pymupdf

COURSE = Path('/home/matteo/Documents/Obsidian/University/Advanced Algorithms and Parallel Programming')
DRAFTS = Path(__file__).parent
NAMES = ['AAPP Index', 'Course Introduction', 'Algorithm as recipes', 'Divide and Conquer', 'PRAM', 'ISPC', 'Randomized Algorithms']
texts = {name: (DRAFTS / (name + '.md')).read_text() for name in NAMES}
pdfs = {p.name: len(pymupdf.open(p)) for p in (COURSE / 'Slides').glob('*.pdf')}
headings = {name: set(re.findall(r'^#{1,6} (.+)$', txt, re.M)) for name, txt in texts.items()}
errors = []
for name, txt in texts.items():
    if not txt.startswith('---\n') or '\n---\n' not in txt[4:]:
        errors.append(f'{name}: missing properties')
    front = txt.split('---\n', 2)[1]
    if not re.fullmatch(r'(?:tags:\n(?:  - [a-z-]+\n)+)(?:lecture: "[0-9b]+"\nsource: "\[\[[^\n]+\]\]"\n)?', front):
        errors.append(f'{name}: unexpected frontmatter syntax')
    if txt.count('```') % 2 or txt.count('$$') % 2 or txt.count('$') % 2:
        errors.append(f'{name}: unbalanced math or code delimiters')
    if name != 'AAPP Index' and len(txt.split()) < 400:
        errors.append(f'{name}: insufficient content')
    for raw in re.findall(r'\[\[([^\]]+)\]\]', txt):
        target = raw.split('|')[0]
        base, _, section = target.partition('#')
        if base in texts:
            if section and section not in headings[base]:
                errors.append(f'{name}: missing heading {target}')
        elif base in pdfs:
            if section and (not re.fullmatch(r'page=\d+', section) or not 1 <= int(section[5:]) <= pdfs[base]):
                errors.append(f'{name}: invalid PDF page {target}')
        else:
            errors.append(f'{name}: unresolved link {target}')

# Check representative examples independently of their wording in the notes.
assert sum(1 / i for i in range(1, 5)) == 25 / 12
assert 2 ** -20 <= 1e-6 < 2 ** -19
a, b, c, d, e, f, g, h = 2, 3, 5, 7, 11, 13, 17, 19
p1, p2, p3, p4 = a*(f-h), (a+b)*h, (c+d)*e, d*(g-e)
p5, p6, p7 = (a+d)*(e+h), (b-d)*(g+h), (a-c)*(e+f)
assert [p5+p4-p2+p6, p1+p2, p3+p4, p5+p1-p3-p7] == [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]
for n in [1, 2, 4, 8, 16]:
    def recurrence(k):
        return 1 if k == 1 else 2 * recurrence(k // 2) + k
    assert recurrence(n) == n * (1 + int(math.log2(n)))
assert abs(1/(0.1+0.9/8) - 4.705882352941177) < 1e-12

if errors:
    raise SystemExit('\n'.join(errors))
print('Validated 7 notes: properties structure, links, PDF pages, delimiters, and representative calculations.')
for name, txt in texts.items():
    print(f'{name}: {len(txt.split())} words')

if '--install' in sys.argv:
    destinations = {name: COURSE / ('AAPP Index.md' if name == 'AAPP Index' else 'Notes/' + name + '.md') for name in NAMES}
    # Check every destination before writing; preserve any user-written content.
    for path in destinations.values():
        if path.exists() and path.read_text().strip():
            raise SystemExit(f'Existing nonempty note requires review: {path}')
    for name, path in destinations.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        (DRAFTS / (name + '.md')).replace(path)
    for name, path in destinations.items():
        assert path.read_text() == texts[name]
    print('Installed and verified all 7 notes in the course folder; staging copies moved to avoid duplicate Obsidian titles.')
