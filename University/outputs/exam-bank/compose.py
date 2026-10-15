from pathlib import Path
import json,re,collections
out=Path('outputs/exam-bank'); qs=json.loads((out/'questions.json').read_text())
# Canonical source names for byte-identical duplicate uploads.
for q in qs: q['file']=q['file'].replace('2024-02-16-2nd-1','2024-02-16-2nd').replace('2024-06-26-1st-1','2024-06-26-1st')
sections=[('PRAM model and memory rules','[[PRAM]]'),('Parallel performance and scaling','[[PRAM]]'),('PRAM algorithms','[[PRAM]]'),('Divide and conquer and recurrences','[[Divide and Conquer]]'),('Randomized algorithm classes','[[Randomized Algorithms]]'),('Minimum cut','[[Minimum Cut]]'),('Sorting and partitioning','[[Sorting]]'),('Selection and order statistics',None),('Primality testing',None),('Dynamic programming and LCS',None),('BDDs and memoization',None),('Treaps',None),('Skip lists',None),('Disjoint sets',None),('Amortized analysis',None),('Online algorithms and competitive analysis',None),('Parallel design and architectures','[[Course Introduction]]'),('Dependences and loop parallelization',None),('Parallel patterns','[[PRAM]] (introductory patterns only)'),('Task graphs and OpenMP implementations',None),('OpenMP',None),('Pthreads and shared-memory synchronization',None),('MPI',None),('CUDA',None),('Halide and high-level synthesis',None)]
def classify(q):
 t=' '.join(q['text'].lower().split()); c=q['context'].lower(); first='-1st' in q['file']; old='2022' in q['file'] and '-2nd-' in q['file']; ex=q['ex']
 if first:
  if ex=='1' and not q['sub']: pass
  elif ex=='1':
   if any(w in t for w in ['amdahl','gustafson','scaling','speed','efficiency','𝑝𝐸','cost','“work”','"work"','work”','work done','work is','work c','“work','work”','work done','work”','work exceeds','work“']): return 1
   if any(w in t for w in ['prefix','matrix','sum algorithm']): return 2
   if 'work' in t and 'pram' in t: return 1
   return 0
  if q['file']=='Tema Esame 2023-01-17-1st.pdf' and ex=='2': return 7
  if 'treap' in t: return 11
  if re.search(r'skip[ -]?list',t): return 12
  if 'disjoint' in t: return 13
  if any(w in t for w in ['karger','min-cut','minimum cut']): return 5
  if 'primality' in t: return 8
  if any(w in t for w in ['bdd','memoization','computed table','unique table']): return 10
  if any(w in t for w in ['competitive','online','offline','on-line','off-line','move to front','move-to-front']): return 15
  if any(w in t for w in ['amortiz','amortis','potential','accounting','increment','multipop','dynamic table']): return 14
  if any(w in t for w in ['longest','lcs','dynamic programming']): return 9
  if any(w in t for w in ['select','ith smallest']): return 7
  if any(w in t for w in ['sort','partitioning','decision tree']): return 6
  if any(w in t for w in ['monte carlo','las vegas']): return 4
  if any(w in t for w in ['divide','master theorem','powering','strassen']): return 3
 else:
  if any(w in t for w in ['halide','high-level synthesis','register-transfer']): return 24
  if any(w in t for w in ['task graph','following structure','corresponding openmp','critical path','3 or 4 threads','optimize one task','calculate span']): return 19
  if old:
   if ex=='1': return 20
   if ex=='3': return 23 if '-a.pdf' in q['file'] else 22
   if ex=='4': return 21
  if 'mpi' in t or (ex=='4' and not any(w in t for w in ['pthread','pthreads','pthread','thread pool','joinable','condition variables','detached'])): return 22
  if any(w in t for w in ['pthread','pthreads','joinable','detached','joining','condition variables']): return 21
  if any(w in t for w in ['for (','for(','dependenc','dependency','dependence','doall','do-all','lexically','renaming']): return 17
  if ex=='2' or any(w in t for w in ['workpile','fork-join','map function','shared state','pipeline','map pattern']): return 18
  if ex=='3' and ('work' in t and 'graph' in t): return 19
  if ex=='3' or 'openmp' in t or 'omp ' in t: return 20
  return 16
 raise ValueError(q)
# Remove only exam administration; keep all technical content and code.
def clean(t):
 t=re.sub(r'This\s+question\s+can\s+be\s+skipped.*?(?:challenge\.|challenge\b)', '',t,flags=re.S|re.I)
 t=re.sub(r'\(You can skip this question if[^)]*\)', '',t,flags=re.I)
 t=re.sub(r'This question can be skipped in case of a passed challenge\.', '',t,flags=re.I)
 t=re.sub(r'\(You can skip this question if.*?\)', '',t,flags=re.S|re.I)
 for a,b in [('DOALLloop','DOALL loop'),('lexicallyforwarddependence','lexically forward dependence'),('separatinghyperplaneinarecurrenceparallelization','separating hyperplane in a recurrence parallelization'),('permutationscatter','permutation scatter'),('mergescatter','merge scatter'),('nelements','n elements')]: t=t.replace(a,b)
 return t.strip()
for q in qs:
 q['text']=clean(q['text']); q['section']=classify(q)
# Repair explicit cross-question context without supplying any answer.
for q in qs:
 if q['file']=='Tema Esame 2023-01-17-1st.pdf' and q['ex']=='2' and q['sub']=='C': q['text']='Context: Exercise 2A asks for the algorithm selecting the ith smallest of n elements (pseudocode and complexity).\n\n'+q['text']
 if q['ex']=='3' and q['file'] in ['Tema Esame 2025-01-24-2nd.pdf','Tema Esame 2025-07-04-2nd.pdf']:
  marker='Consider the following task graph'
  if marker in q['text']:
   q['text']=q['text'].split(marker)[0].strip()
  if q['sub'] in ['B','C']:
   q['section']=19
   q['context']='Consider the task graph on the source page.' + (' All tasks contain the same amount of work.' if '2025-07' in q['file'] else '')
 if q['file']=='Tema Esame 2024-07-24-2nd.pdf' and q['ex']=='3': q['section']=19
# Retain shared technical introductions, omit recurring instruction boilerplate.
for q in qs:
 if q['context'].lower().startswith('answer the'): q['context']=''
 key=q['file'],q['page']
 if q['section']==19 or 'following diagram' in q['text'].lower(): q['visual']=True
# Focused editorial classification after reviewing the extracted questions.
for q in qs:
 if q['n'] in [10,11,22,23,37,38,49,50,88,90]: q['section']=16
 if q['n']==151: q['section']=17
 if q['n']==335: q['section']=19
 if q['n']==369:
  q['section']=21
  q.pop('visual',None)
 if q['n']==354: q['section']=1
 if q['n']==212: q.pop('visual',None)
 if q['n']==421: q['text']=q['text'].replace('T1(n)=n3 and Tp(n)=n3/p', '$T_1(n)=n^3$ and $T_p(n)=n^3/p$')
# Exact textual repeats merge, substantive wording variants stay separate.
groups=collections.OrderedDict()
for q in qs:
 norm=re.sub(r'\s+',' ',q['text']).strip()
 key=(q['section'],norm,q['context'] if q.get('visual') else '', (q['file'],q['page']) if q.get('visual') else None)
 if key not in groups: groups[key]={'q':q,'sources':[]}
 groups[key]['sources'].append(q)
(out/'grouped.json').write_text(json.dumps(list(groups.values()),indent=2))
print('Occurrences',len(qs),'entries',len(groups))
for i,(name,_) in enumerate(sections):
 arr=[v for v in groups.values() if v['q']['section']==i]
 print(name,len(arr))
(out/'sections.json').write_text(json.dumps(sections))
