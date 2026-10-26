"""Create first-run navigation/workflow and verify the imported slide notes.

Never use this script to replace an existing course index or workflow.
"""
from pathlib import Path
from collections import defaultdict
import hashlib
import json
import re
import subprocess
import zipfile
import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT.parents[1]
OUT = ROOT / 'outputs'
STAMP = '2026-10-26'
entries = json.loads((OUT / 'source-map.json').read_text())
groups = defaultdict(list)
for e in entries:
    groups[e['group']].append(e)

def relative(path):
    return str(Path(path).relative_to(VAULT))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def wikilink(path, label=None, table=False):
    bar = r'\|' if table else '|'
    return '[[' + path + (bar + label if label else '') + ']]'

def create(path, text):
    if path.exists():
        raise RuntimeError(f'Read and preserve existing content instead of recreating: {path}')
    path.write_text(text)

archive = next((ROOT / 'Slides').rglob('Optional - to move deeper.zip'))
with zipfile.ZipFile(archive) as z:
    optional = [n for n in z.namelist() if n.lower().endswith('.pdf') and not n.startswith('__MACOSX/')]

index = ['---\ncourse: Embedded Systems\ntype: course-index\n---\n', '# Embedded Systems\n',
         'Original slides with selective English comments. The folders below mirror the two supplied topic folders. Each numbered section follows a physical PDF page, including repeated slides and article-printout footers.\n']
for group, decks in groups.items():
    index += [f'## {group}\n']
    for e in decks:
        index.append(f"- {wikilink(e['note'][:-3], Path(e['note']).stem)} — {e['pages']} pages.")
    index.append('')
index += ['## Workflow and additional reading\n',
          f"- {wikilink(relative(ROOT / 'Course Workflow'))} — source mapping, annotation conventions, source issues, and revision procedure.",
          f"- {wikilink(relative(archive), 'Optional — to move deeper')} — archive of 12 additional PDFs; retained as supplied, not processed into slide notes.\n"]
create(ROOT / 'Embedded Systems.md', '\n'.join(index))

comments = sum(len(e['annotation_pages']) for e in entries)
workflow = ['---\ncourse: Embedded Systems\ntype: course-workflow\n---\n', '# Course Workflow\n',
f'Last completed import: {STAMP}. Navigation: [[University/Embedded Systems/Embedded Systems|Embedded Systems]].\n',
'## Scope and organization\n',
'The first import found no existing course notes, course index, workflow, syllabus, or explicit exam exclusions in this course folder. Sixteen standalone PDFs in the two supplied topic folders were processed: 574 physical pages. The optional ZIP remains additional reading, as recorded below; no claim is made about whether that reading is examinable.\n',
'`Notes/` and `Attachments/` mirror the original topic folders in `Slides/`. Each PDF has its own note. Readable note filenames remove plus-sign separators where appropriate; the mapping below preserves the exact source and image-folder names. No expanded study-note format was replaced.\n',
'## Annotation and rendering conventions\n',
'- Slides remain the main material. Every page has one `## Slide N — title` section, one local PNG embed immediately below it, and a link to physical PDF page N. Title pages, repeated slides, references, and article footer pages are retained in order. Untitled article continuations have descriptive navigation headings. Differing printed slide numbers should be recorded separately when present.\n'
'- Comments are in English, in a `[!note] Comment` callout directly below the relevant page. Add only a specific missing explanation, small example, ambiguity, or evidenced correction; clear slides receive no commentary. Usually aim for 30–100 words when a comment is useful. Use LaTeX for mathematics, preserve lecturer terminology, and link to an existing explanation instead of repeating it.\n'
'- Keep exercise statements visible. Any added solution belongs in a separate collapsed `[!example]- Worked solution` callout. Do not require summaries, quizzes, or expanded textbook sections.\n'
'- Check the page and surrounding pages first. Consult primary external sources only where needed; cite them inside the relevant Comment. Apparent slide errors are explicitly qualified without changing the slide image. No lecturer remarks or exam requirements are inferred.\n'
'- PNGs were rendered locally with MuPDF (`mutool draw`), preserving the complete MediaBox and aspect ratio, with a 3200-pixel longest edge. Names are stable and zero-padded: `slide-001.png`, etc. No PDF-embed fallback was needed. MuPDF reported unavailable ICC support; the rendered examples were visually checked, but color-managed print fidelity is not certified. Original raster screenshot softness and content already clipped/covered in the PDFs remain visible.\n',
'## Source-to-note mapping\n',
'All paths in this table are relative to the course folder except the clickable vault links. Each image folder contains exactly the source page count, starting at `slide-001.png`.\n',
'| Source deck | Pages | Note | Image folder |',
'| --- | ---: | --- | --- |']
for e in entries:
    folder = str(Path(e['image_folder']).relative_to(ROOT.relative_to(VAULT)))
    workflow.append(f"| {wikilink(e['source'], e['group'] + '/' + Path(e['source']).name, True)} | {e['pages']} | {wikilink(e['note'][:-3], Path(e['note']).stem, True)} | `{folder}/` |")
workflow += ['', '## Verification and review record\n',
f'All 574 pages were inspected visually in ordered review sheets, with extracted text as an aid and full-resolution checks of dense code, diagrams, screenshots, and source limitations. There are {comments} Comment callouts across the 16 notes; the other pages stand on their own.\n',
'The machine audit checks PDF page counts, consecutive section order, exactly one matching PNG per section, matching source-page links, PNG decoding and dimensions, source-file hashes, all vault link targets and heading links, valid YAML properties, and inclusion in the course index. Detailed results are in [[University/Embedded Systems/outputs/verification.json|verification.json]].\n',
'[[University/Embedded Systems/outputs/source-map.json|source-map.json]] records each original PDF SHA-256, note path, image folder, page text hash, page image hash, heading, printed-number metadata, original generated section/comment hashes, and reviewed-page coverage. These fingerprints are the initial comparison baseline; user edits must always be read from the actual notes. Extracted text, structured text, ordered review sheets, and first-import helpers are retained under `outputs/`.\n',
'## Source issues and qualifications\n']
for e in entries:
    issue=e['outstanding_issues']
    if issue != 'None identified during page review.':
        workflow.append(f"- {wikilink(e['note'][:-3], Path(e['note']).stem)}: {issue}")
workflow += ['',
'Unreadable source regions remain unresolved: IDE page 20 has right-edge clipping; CAD walkthrough page 57 has an instruction partly covered by a screenshot; the boundary-scan article has a repeated cookie notice over top-of-page content on pages 2–9, including part of the page 6 diagram. These are source limitations, not missing rendered pages. Hidden wording was not invented. Historical products, software interfaces, licenses, prices, and feasibility estimates are retained as course material.\n',
'## Optional archive — not processed\n',
f'{wikilink(relative(archive), archive.name)} contains the following 12 PDFs. The archive was inspected by listing its contents, without extracting or annotating them. These optional references are outside the 16-note / 574-page completed import.\n']
workflow += [f'- {Path(name).name}' for name in optional]
workflow += ['', '## Continue on later runs\n',
'1. Read this workflow, the current index, every affected existing note, and the saved source map before editing. Preserve the user’s properties, comments, corrections, filenames, and any separate expanded notes. Check newly supplied syllabus or exam boundaries.\n'
'2. Inventory new standalone PDFs. Mirror their topic folder under `Notes/` and `Attachments/`, render the whole page, visually inspect every page, and use the same restrained annotation layout. Add finished notes to the index and mapping. Do not treat the optional archive as already processed.\n'
'3. For a revised PDF, save the previous source map and referenced images before rendering into a separate staging folder under `outputs/`. Compare the old and new page images and text, then inspect candidates visually. Match slide content across insertions, deletions, repetitions, and reordering; physical page numbers alone are insufficient.\n'
'4. Move a preserved comment only when its source slide is confidently matched. Flag comments whose slide changed or disappeared for review, retaining the old comment and source identity. Keep unmatched comments in a clearly marked review section rather than silently attaching them to another slide. Preserve user-written additions even when the generated baseline differs.\n'
'5. After review, update headings, page links, image mappings, and the saved fingerprints together. Repeat the coverage/link/image audit and record unresolved issues here. The import helpers are first-run utilities, not an automatic revision merger: `build_notes.py` skips existing notes, `prepare_slides.py` refuses to overwrite existing slide images, and `finish_course.py` refuses to replace an existing index/workflow.\n']
create(ROOT / 'Course Workflow.md', '\n'.join(workflow))

errors=[]
report={'date':STAMP,'decks':[],'errors':errors}
all_images=[]
index_text=(ROOT/'Embedded Systems.md').read_text()
for e in entries:
    source=VAULT/e['source']; note=VAULT/e['note']; body=note.read_text()
    props=yaml.safe_load(body.split('---\n',2)[1])
    if props['source'] != f"[[{e['source']}]]" or props['source_pages'] != e['pages']:
        errors.append(f'Properties disagree with source: {note}')
    info=subprocess.run(['pdfinfo',str(source)],capture_output=True,text=True,check=True).stdout
    pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1])
    if pages!=e['pages'] or sha(source)!=e['sha256']:
        errors.append(f'Source changed: {source}')
    sections=list(re.finditer(r'^## Slide (\d+) — (.+)$',body,re.M))
    if [int(s[1]) for s in sections]!=list(range(1,pages+1)):
        errors.append(f'Invalid section count/order: {note}')
    if e['note'][:-3] not in index_text:
        errors.append(f'Missing from index: {note}')
    actual_images=sorted((VAULT/e['image_folder']).glob('slide-*.png'))
    if len(actual_images)!=pages:
        errors.append(f'Invalid image count: {source}')
    for i,(s,p) in enumerate(zip(sections,e['page_data'])):
        n=i+1;section=body[s.start():sections[i+1].start() if i+1<len(sections) else len(body)]
        expected=f"![[{p['image']}]]"
        if not section.startswith(s[0]+'\n\n'+expected+'\n') or section.count('![[')!=1:
            errors.append(f'Invalid immediate embed: {note} page {n}')
        links=re.findall(r'^Source: \[\[([^\]]+)\]\]',section,re.M)
        if links != [f"{e['source']}#page={n}|PDF page {n}"]:
            errors.append(f'Invalid PDF page link: {note} page {n}')
        png=VAULT/p['image'];all_images.append(str(png))
        if png.name!=f'slide-{n:03}.png':errors.append(f'Invalid image name: {png}')
        with Image.open(png) as im:
            w,h=im.size;im.verify()
        if max(w,h)!=3200 or abs((w/h)/(p['width_pt']/p['height_pt'])-1)>0.002:
            errors.append(f'Invalid image size/aspect: {png}')
        p['heading']=s[0][3:]
        p['image_sha256']=sha(png)
        p['initial_section_sha256']=hashlib.sha256(section.encode()).hexdigest()
        callouts=re.findall(r'^> \[!note\] Comment\n(?:>.*\n?)+',section,re.M)
        p['initial_comment_sha256']=hashlib.sha256('\n'.join(callouts).encode()).hexdigest() if callouts else None
    if e['visually_reviewed_pages']!=list(range(1,pages+1)):
        errors.append(f'Incomplete visual review: {note}')
    e['initial_note_sha256']=sha(note)
    report['decks'].append({'source':e['source'],'note':e['note'],'pages':pages,'sections':len(sections),'images':len(actual_images),'comment_callouts':body.count('> [!note] Comment')})

if len(set(all_images))!=574:errors.append('Image paths are not unique across the 574 sections.')
checked_links=0
for note in list((ROOT/'Notes').rglob('*.md'))+[ROOT/'Embedded Systems.md',ROOT/'Course Workflow.md']:
    t=note.read_text()
    if t.startswith('---\n'):yaml.safe_load(t.split('---\n',2)[1])
    for raw in re.findall(r'\[\[([^\]\n]+)\]\]',t):
        target=raw.replace(r'\|','|').split('|',1)[0]
        path,_,anchor=target.partition('#')
        resolved=VAULT/path
        if not resolved.exists() and (VAULT/(path+'.md')).exists():resolved=VAULT/(path+'.md')
        if not resolved.exists():
            # Report file is produced at the end of this successful audit.
            if path != 'University/Embedded Systems/outputs/verification.json':
                errors.append(f'Unresolved vault link in {note.name}: {target}')
        elif anchor and not anchor.startswith('page='):
            headings=re.findall(r'^#{1,6} (.+)$',resolved.read_text(),re.M)
            if anchor not in headings:errors.append(f'Unresolved heading link in {note.name}: {target}')
        checked_links+=1

report.update({'notes':len(entries),'pdf_pages':sum(e['pages'] for e in entries),'unique_images':len(set(all_images)),'checked_vault_links':checked_links,'comment_callouts':sum(d['comment_callouts'] for d in report['decks']),'optional_archive_pdf_count_not_processed':len(optional),'png_longest_edge':3200,'render_box':'MediaBox','passed':not errors})
(OUT/'verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
if errors:
    print(json.dumps(report,indent=2,ensure_ascii=False))
    raise SystemExit('Verification failed; repair identified errors without recreating notes.')
(OUT/'source-map.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False))
print(json.dumps({k:v for k,v in report.items() if k!='decks'},indent=2))
