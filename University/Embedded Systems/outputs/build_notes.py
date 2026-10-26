from pathlib import Path
import json
import re
import yaml
from editorial import COMMENTS, TITLES, DECK_TITLES, TOPICS, REVIEWED, ISSUES

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT.parents[1]
OUT = ROOT/'outputs'

def note_path(entry):
    return ROOT/'Notes'/entry['group']/(DECK_TITLES[entry['stem']]+'.md')

def build():
    entries = json.loads((OUT/'source-map.json').read_text())
    created=[]
    for e in entries:
        stem=e['stem']
        if REVIEWED.get(stem) != list(range(1,e['pages']+1)):
            continue
        target=note_path(e)
        if target.exists():
            # Never use this initial-creation helper to overwrite a user's note.
            continue
        target.parent.mkdir(parents=True,exist_ok=True)
        title=DECK_TITLES[stem]
        props={'course':'Embedded Systems','source':f"[[{e['source']}]]",'source_pages':e['pages'],'annotation_style':'slide-by-slide, concise English comments'}
        parts=['---\n'+yaml.safe_dump(props,sort_keys=False,allow_unicode=True,width=100000)+'---\n',f'# {title}\n',f"Original deck: [[{e['source']}|{Path(e['source']).name}]]\n",f"Topic: {TOPICS[stem]}\n",'[[University/Embedded Systems/Embedded Systems|Course index]]\n']
        for p in e['page_data']:
            n=p['page'];heading=TITLES.get(stem,{}).get(n,p['title'])
            heading=re.sub(r'\s+',' ',heading).replace('|','—').replace('#','').strip()
            parts.extend([f'## Slide {n} — {heading}\n',f"![[{p['image']}]]\n",f"Source: [[{e['source']}#page={n}|PDF page {n}]]\n"])
            if p['printed_number'] is not None and int(p['printed_number']) != n:
                parts.append(f"Printed slide number: {p['printed_number']}.\n")
            comment=COMMENTS.get(stem,{}).get(n)
            if comment:
                parts.append('> [!note] Comment\n'+'\n'.join('> '+line if line else '>' for line in comment.splitlines())+'\n')
        target.write_text('\n'.join(parts))
        e['note']=str(target.relative_to(VAULT))
        created.append(str(target.relative_to(ROOT)))
    # Update only generated source metadata; this does not modify existing notes.
    for e in entries:
        if e['stem'] in DECK_TITLES:
            e['note']=str(note_path(e).relative_to(VAULT))
            e['visually_reviewed_pages']=REVIEWED.get(e['stem'],[])
            e['annotation_pages']=sorted(COMMENTS.get(e['stem'],{}))
            e['outstanding_issues']=ISSUES.get(e['stem'],'None identified during page review.')
    (OUT/'source-map.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False))
    print(json.dumps({'created':created,'notes_total':sum(1 for e in entries if e.get('note') and (VAULT/e['note']).exists())},indent=2))

if __name__=='__main__':
    build()
