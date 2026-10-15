from pathlib import Path
import json,re,collections
out=Path('outputs/exam-bank'); groups=json.loads((out/'grouped.json').read_text()); sections=json.loads((out/'sections.json').read_text()); base=Path('Advanced Algorithms and Parallel Programming')
# Keep line structure for programs; join PDF wrapping for prose.
def format_text(t):
 lines=t.splitlines(); result=[]; prose=[]; code=[]
 def flush_prose():
  if prose:result.append(' '.join(' '.join(prose).split()));prose.clear()
 def flush_code():
  if code:
   result.append('```'+('text' if any('INCREMENT' in l for l in code) else 'c')+'\n'+'\n'.join(code)+'\n```');code.clear()
 for line in lines:
  s=line.strip()
  iscode=bool(re.match(r'(?:for\s*\(|#pragma|(?:a|b|c)\[|int MPI_|int source|int tag|gradient\.|INCREMENT\(|\d+\s+(?:i\s*=|while|A\[|i\s*=|if)|[{}])',s))
  if iscode:
   flush_prose();code.append(line)
  else:
   flush_code();prose.append(s)
 flush_code();flush_prose();return '\n\n'.join(result)
lines=['---','tags:','  - aapp','  - exam-practice','  - question-bank','status: unanswered','created: 2026-10-15','---','# AAPP — Past Exam Question Bank','','[[AAPP Index|Course index]]','','Questions collected from the supplied 2022–2025 exams, grouped by subject for revision and future reference answers. **No answers or newly generated questions are included.**','','> [!info] How to use this bank', '> Each entry has a stable question ID and an original exam/page reference. Answer with reasoning: the exams repeatedly state that an unsupported answer is invalid. Keep the ID when adding a future answer or requesting similar practice. Points in parentheses are the original marks where available.','','## Contents','']
for i,(name,_) in enumerate(sections):
 n=sum(g['q']['section']==i for g in groups)
 lines.append(f'- [[#{name}]] — {n} questions')
lines += ['','## Editorial conventions','','- Repeated questions with identical extracted wording are listed once with all their sources; distinct wording and technical variants are retained. Questions in the 2022 A/B papers are therefore combined only when their wording matches.','- Original exercise/subquestion labels, requirements, numerical values, and code are preserved. Blank answer lines, cover instructions, and challenge-based exemptions are omitted. A multi-part prompt without separate letter labels remains one entry.','- Page links use physical PDF pages. Embedded source pages retain task graphs, task weights, and cancellation timelines that plain text cannot capture. Some diagrams are shared by several entries.','- Source filenames identify exam sessions. Some PDFs contain copied footers with a different date; follow the linked source rather than treating a footer as a separate exam.','- Wording, claims to discuss, and apparent source errors are left as questions, not corrected into answers. In particular, check the bounds and increment in the September 2025 loop exactly as printed.','- Links to existing notes indicate related study material, not a guarantee that every question is already covered. Topics without a dedicated note remain included.','','> [!warning] Future answer pass','> Use the course notes and source PDFs to answer each ID when requested. Preserve assumptions and distinguish expected, worst-case, and amortized bounds. Where material is still missing, mark the answer as pending rather than inventing a course-specific explanation.','']
ids=[]; byfile=collections.defaultdict(list); visual_seen=set()
for si,(name,note) in enumerate(sections):
 lines += ['## '+name,'']
 lines += [('Related notes: '+note+'.') if note else '*No dedicated study note is currently available for this topic.*','']
 selected=[g for g in groups if g['q']['section']==si]
 for k,g in enumerate(selected,1):
  q=g['q'];id=f'AAPP-{si+1:02d}-{k:03d}';g['id']=id;ids.append(id)
  lines += ['### '+id,'',format_text(q['text']),'']
  if q['context']:lines+=['*Shared exercise context:* '+q['context'],'']
  for src in g['sources']:
   label=src['file'][11:-4]+' · Exercise '+src['ex']+src['sub']+f" · p. {src['page']}"
   lines += [f"Source: [[{src['file']}#page={src['page']}|{label}]]"]
   byfile[src['file']].append(id)
  lines += ['']
  if q.get('visual'):
   key=q['file'],q['page'];image=q['file'][11:-4]+f"-p{q['page']}.png"
   if key not in visual_seen:
    lines += [f'![[{image}|800]]','',f"*Original source page for the graph or diagram. [[{q['file']}#page={q['page']}|PDF page {q['page']}]].*",''];visual_seen.add(key)
   else:lines += [f'> [!example]- Shared graph or diagram',f'> ![[{image}|800]]','']
  lines += ['^'+id.lower(),'']
lines += ['## Source register','','46 distinct exam papers contribute 464 exercise/subquestion occurrences, represented above by '+str(len(ids))+' entries after exact-wording consolidation. All supplied exam papers are included; the register lets you reconstruct a particular session.','','| Exam paper | Question IDs |','|---|---|']
for f,xx in sorted(byfile.items()):
 refs=', '.join(f'[[#'+x+'|'+x+']]' for x in dict.fromkeys(xx))
 lines += ['| [['+f+'\\|'+f[11:-4]+']] | '+refs.replace('|','\\|')+' |']
lines+=['','### Duplicate PDF uploads','','The following pairs are byte-identical; each exam is represented once. The original files are unchanged.','','- [[Tema Esame 2024-02-16-2nd-1.pdf]] duplicates [[Tema Esame 2024-02-16-2nd.pdf]].','- [[Tema Esame 2024-06-26-1st-1.pdf]] duplicates [[Tema Esame 2024-06-26-1st.pdf]].','','### Files containing results rather than questions','','The following three PDFs contain marks/results tables and contribute no questions:','','- [[AAPP-2nd-midterm.pdf]]','- [[AAPP-Sep-10th.pdf]]','- [[elenco-AAPP-25-26.pdf]]','']
p=base/'Past Exam Question Bank.md';p.write_text('\n'.join(lines));(out/'grouped.json').write_text(json.dumps(groups,indent=2));print(p, 'entries',len(ids),'sources',len(byfile),'visual pages',len(visual_seen))
