from pathlib import Path
from collections import defaultdict
import re,json,hashlib,subprocess,yaml
from PIL import Image
root=Path('/home/matteo/Documents/obsidian');course=root/'University/Advanced Algorithms and Parallel Programming';out=root/'outputs/aapp-update-2026-10-26'
files=[p for p in root.rglob('*') if p.is_file() and not any(x.startswith('.') for x in p.relative_to(root).parts) and 'outputs' not in p.relative_to(root).parts]
byname=defaultdict(list)
for p in files:
 byname[p.name.casefold()].append(p)
 if p.suffix=='.md':byname[p.stem.casefold()].append(p)
notes=sorted(course.rglob('*.md'))+[root/'University/Study Note Prompts.md']
errors=[];refs=0;embeds=0;pdfrefs=0;tables=0;pages={};imagefiles=set();anchors=0
for p in files:
 if p.suffix.lower()=='.pdf' and course in p.parents:
  r=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True)
  m=re.search(r'^Pages:\s+(\d+)',r.stdout,re.M)
  if not m:errors.append(('pdfinfo',str(p),r.stderr))
  else:pages[p]=int(m[1])
def resolve(target,origin):
 target=target.replace('\\|','|')
 for q in [root/target,origin.parent/target]:
  for p in [q,q.with_suffix('.md') if not q.suffix else q]:
   if p.is_file():return p
 options=list(dict.fromkeys(byname.get(target.casefold(),[])))
 local=[p for p in options if course in p.parents]
 if len(local)==1:return local[0]
 if len(options)==1:return options[0]
 return None
for p in notes:
 s=p.read_text()
 try:
  if not s.startswith('---\n'):raise ValueError('missing frontmatter')
  fm=yaml.safe_load(s.split('---',2)[1]);assert isinstance(fm,dict)
 except Exception as e:errors.append(('yaml',p.name,str(e)))
 in_fence=False;lastcols=None
 for lineno,line in enumerate(s.splitlines(),1):
  if re.match(r'^\s*```',line):in_fence=not in_fence
  if not in_fence and line.startswith('|'):
   cols=len(re.split(r'(?<!\\)\|',line))-2;tables+=1
   if lastcols is not None and cols!=lastcols:errors.append(('table',p.name,lineno,cols,lastcols))
   lastcols=cols
  else:lastcols=None
 if in_fence:errors.append(('fence',p.name))
 # Fenced templates are literal examples, not Obsidian references.
 linktext=re.sub(r'(?ms)^```[^\n]*\n.*?^```\s*$', '', s)
 for m in re.finditer(r'(!?)\[\[([^\]]+)\]\]',linktext):
  refs+=1;target=m[2].replace('\\|','|').split('|')[0];base,sep,anchor=target.partition('#');q=resolve(base,p) if base else p
  if not q:errors.append(('link',p.name,target));continue
  if q.suffix=='.pdf' and anchor:
   pdfrefs+=1
   pm=re.fullmatch(r'page=(\d+)',anchor)
   if not pm or not(1<=int(pm[1])<=pages.get(q,0)):errors.append(('pdf page',p.name,target,pages.get(q)))
  elif q.suffix=='.md' and anchor:
   anchors+=1;txt=q.read_text()
   if anchor.startswith('^'):
    ok=bool(re.search(r'(?m)\^'+re.escape(anchor[1:])+r'\s*$',txt))
   else:
    heads=[re.sub(r'\s+#+\s*$','',h).strip() for h in re.findall(r'^#{1,6}\s+(.+)$',txt,re.M)]
    ok=anchor.casefold() in [h.casefold() for h in heads]
   if not ok:errors.append(('anchor',p.name,target))
  if m[1]=='!' and q.suffix.lower() in ['.png','.jpg','.jpeg','.webp','.svg']:
   embeds+=1;imagefiles.add(q)
for p in imagefiles:
 if p.suffix!='.svg':
  try:
   with Image.open(p) as im:im.load()
  except Exception as e:errors.append(('image',str(p),str(e)))
manifest=json.loads((out/'source-manifest.json').read_text())
for e in manifest:
 p=course/'Slides'/e['source']
 if hashlib.sha256(p.read_bytes()).hexdigest()!=e['sha256']:errors.append(('changed source',p.name))
workflow=(course/'Course Workflow.md').read_text()
for e in manifest:
 if e['sha256']+'  '+e['source'] not in workflow:errors.append(('unrecorded hash',e['source']))
for p in (out/'before').rglob('*.md.snapshot'):
 rel=p.relative_to(out/'before');orig=course/str(rel).removesuffix('.snapshot')
 if not orig.exists():errors.append(('removed original',str(orig)));continue
 old=p.read_text();new=orig.read_text()
 if old.split('---',2)[1]!=new.split('---',2)[1]:errors.append(('changed properties',orig.name))
 for embed in re.findall(r'!\[\[([^\]]+)\]\]',old):
  if '![[%s]]'%embed not in new:errors.append(('removed image',orig.name,embed))
beforebank=(out/'bank-before-study-links.md.snapshot').read_text();afterbank=(course/'Past Exam Question Bank.md').read_text()
getquestions=lambda t:re.findall(r'(?ms)^### (AAPP-\d+-\d+)\n(.*?)(?=^### AAPP-|^## |\Z)',t)
if getquestions(beforebank)!=getquestions(afterbank):errors.append(('question content changed after study-link snapshot',))
summary={'markdown_files':len(notes),'internal_references':refs,'heading_or_block_anchors':anchors,'pdf_page_references':pdfrefs,'image_embeds':embeds,'unique_embedded_images':len(imagefiles),'table_lines_checked':tables,'pdf_files_checked':len(pages),'slide_decks':len(manifest),'slide_pages':sum(e['pages'] for e in manifest),'bank_questions_preserved':len(getquestions(afterbank)),'errors':errors}
(out/'validation.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
