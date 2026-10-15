from pathlib import Path
import re,json
out=Path('outputs/exam-bank'); qs=[]; seen={}; dup=[]
for row in json.loads((out/'inventory.json').read_text()):
 name=row['file']
 if not name.startswith('Tema Esame'): continue
 if row['hash'] in seen: dup.append((name,seen[row['hash']])); continue
 seen[row['hash']]=name
 s=(out/(Path(name).stem+'.txt')).read_text()
 for pg,page in enumerate(s.split('\f'),1):
  ex=re.search(r'(?:Exercise|Questions)\s+(?:n\.\s*)?(\d)\s*\n',page)
  if not ex: continue
  body=page[ex.end():]
  body='\n'.join(l.rstrip() for l in body.splitlines() if l.strip() and not re.search(r'_{5}|Advanced Algorithms and Parallel Programming|Name & Surname',l))
  parts=list(re.finditer(r'^\s*([A-D])\.\s+',body,re.M))
  if parts:
   context=' '.join(body[:parts[0].start()].split())
   for i,m in enumerate(parts):
    t=body[m.end():parts[i+1].start() if i+1<len(parts) else len(body)].strip()
    qs.append(dict(file=name,page=pg,ex=ex[1],sub=m[1],text=t,context=context))
  else: qs.append(dict(file=name,page=pg,ex=ex[1],sub='',text=body.strip(),context=''))
for i,q in enumerate(qs): q['n']=i
(out/'questions.json').write_text(json.dumps(qs,indent=2))
(out/'duplicates.json').write_text(json.dumps(dup,indent=2))
print('Questions:',len(qs))
for q in qs:
 t=re.sub(r'This question can be skipped.*','', ' '.join(q['text'].split()))
 print(f"{q['n']} | {q['file'][11:-4]} {q['ex']}{q['sub']} | {t}")
