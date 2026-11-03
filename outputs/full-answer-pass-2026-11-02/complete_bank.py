import json,re,hashlib
from pathlib import Path
from collections import Counter

vault=Path('/home/matteo/Documents/obsidian')
out=vault/'outputs/full-answer-pass-2026-11-02'
bank=vault/'University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md'
source=out/'Past Exam Question Bank.pre-merge.snapshot'
if not source.exists():source=out/'Past Exam Question Bank.md.snapshot'
snapshot=source.read_text()
questions=json.loads((out/'questions.json').read_text())
answers={}
for name in ['algorithms','patterns','systems','mpi-cuda']:
    part=json.loads((out/f'answers-{name}.json').read_text())
    assert not set(part)&set(answers)
    answers.update(part)
assert set(answers)=={q['id'] for q in questions} and len(answers)==552

# Additional subparts and concrete directives, retained with the main explanation.
answers['AAPP-10-009']='Dynamic programming saves repeated computation by retaining state results, so storage can determine feasibility: a polynomial-time table may still be too large, while memoizing an exponential state space does not make it small. Count the states, information per state and recursion stack, and retain only live dependencies where possible. LCS illustrates the tradeoff.\n\n'+answers['AAPP-10-009']
for key in [k for k in answers if k.startswith('AAPP-12-') and k not in ['AAPP-12-004','AAPP-12-008','AAPP-12-009','AAPP-12-010','AAPP-12-017']]:
    answers[key]='A treap is a binary search tree on keys and a min-heap on distinct random priorities.\n\n'+answers[key]
for n in (1,2):
    k=f'AAPP-14-{n:03d}'
    answers[k]=answers[k].replace('Study: Reference topic: disjoint-set forests; the supplied dedicated algorithm notes do not contain a full disjoint-set lecture.','Reference: [Princeton union-find implementation and bounds](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/UF.html).')
answers['AAPP-18-015']+='\n\nThe directly related parallel pattern is **Map**: apply the same independent operation to each element.'
answers['AAPP-18-017']+='\n\nFor a special removable flow chain, the prefix-sum recurrence `s[i]=s[i-1]+x[i]` can become a parallel scan when addition is associative in the chosen arithmetic. This preserves values under that assumption; it is an algorithmic reformulation rather than storage renaming.'
answers['AAPP-18-022']+='\n\nExample WAR: replace `y=x+1; x=f();` by `old=x;` followed by independent `y=old+1` and `x=f()`, if `f` has no conflicting side effects. Example WAW: replace independent overwritten results `x=f(); x=g();` by private `u=f(); v=g(); x=v;`, preserving the original final value.'
answers['AAPP-18-034']=answers['AAPP-18-034'].replace('Use a reduction for `sum`','Both phases update the same `total_sum`, so use a reduction for **both** phases (or one fused outer-row reduction)')+r'''

```c
#pragma omp parallel for reduction(+:total_sum)
for (int i=0; i<100; ++i) {
    for (int j=2; j<100; j+=2) {
        a[i][j] = f(a[i][j]) + b[i][j-2];
        total_sum += a[i][j];
    }
    for (int j=3; j<100; j+=2) {
        c[i][j] = f(a[i][j]) + b[i][j-2];
        total_sum += c[i][j];
    }
}
```
'''
answers['AAPP-18-036']+=r'''

```c
#pragma omp parallel
{
    #pragma omp for collapse(2) reduction(+:acc)
    for (int i=0; i<100; ++i)
        for (int j=1; j<100; j+=2) {
            a[i][j] += a[i][j-1];
            acc += a[i][j];
        }
    #pragma omp for collapse(2)
    for (int i=0; i<100; ++i)
        for (int j=2; j<100; j+=2)
            c[i][j] += f(a[i][j]) + b[i][j-2];
}
```
'''
answers['AAPP-18-037']=answers['AAPP-18-037'].replace('for `j=1..99`','across the two printed column ranges')+r'''

After explicitly removing the source's stray parenthesis and ensuring at least 200 columns in `a`:

```c
#pragma omp parallel
{
    #pragma omp for collapse(2) nowait
    for (int i=3; i<100; ++i)
        for (int j=1; j<100; ++j)
            a[i][2*j] = f(a[i-3][2*j-1]);
    #pragma omp for collapse(2)
    for (int i=0; i<100; ++i)
        for (int j=0; j<100; ++j)
            c[i][j] += a[i][2*j+1] + b[i][j];
}
```
'''
answers['AAPP-18-039']+=r'''

For example, parallelize columns while retaining each column's row chains, then use a reduction after the implicit barrier:

```c
#pragma omp parallel
{
    #pragma omp for
    for (int j=1; j<100; ++j)
        for (int i=2; i<100; ++i)
            x[i][j] = g(x[i-2][j], y[i][j-1]);
    #pragma omp for collapse(2) reduction(+:sum)
    for (int i=0; i<100; ++i)
        for (int j=1; j<100; ++j) {
            z[i][j] += x[i][j] * w[i][j];
            sum += z[i][j];
        }
}
```

Require pure/thread-safe `g` and defined integer arithmetic. This column decomposition is correct but can be strided in row-major storage.
'''
answers['AAPP-18-041']+=r'''

```c
#pragma omp parallel
{
    #pragma omp for
    for (int j=1; j<100; ++j)
        for (int i=4; i<100; ++i)
            x[i][j] = g(x[i-4][j], y[i][j-1]);
    #pragma omp for collapse(2)
    for (int i=0; i<100; ++i)
        for (int j=1; j<100; ++j)
            z[i][j-1] += x[i][j-1] * w[i][j-1];
}
/* sum retains its original zero value. */
```

For a concrete layout cost, assigning neighboring columns to different threads can make them update distinct elements on the same cache line (false sharing), while walking a column in row-major storage causes large strides. Neither alone changes the mathematical dependence; a `g` with `static int calls; ++calls;` would instead introduce a race.
'''
answers['AAPP-18-042']+=r'''

One direct wavefront implementation is:

```c
#pragma omp parallel
{
    for (int d=2; d<=n+m-2; ++d) {
        #pragma omp for
        for (int i=1; i<n; ++i) {
            int j=d-i;
            if (j>=1 && j<m)
                x[i][j]=x[i-1][j]+x[i][j-1]+y[i][j];
        } // implicit barrier before the next diagonal
    }
    #pragma omp for
    for (int i=0; i<100; ++i)
        for (int j=1; j<100; ++j)
            z[i][j]=z[i][j-1]-x[i][j-1]+w[i][j-1];
}
```

Assume `n,m>=100`, compatible dimensions and defined arithmetic, or adapt the second phase's fixed bounds to the actual domain. Wavefront cells are scattered in row-major storage; tiled dependent tasks improve locality and amortize barriers. A hypothetical `g` that increments shared state would require synchronization, but no such call is present in this source.
'''
answers['AAPP-19-028']+='\n\nMerge collision resolution belongs to **scatter**, where several inputs target one output. Ordinary gather has a unique owner per output; repeated indices only mean concurrent reads and require no merge of competing writes.'
answers['AAPP-23-048']=answers['AAPP-23-048'].replace('node62.htm','node59.htm')
for k in [k for k in answers if k.startswith('AAPP-23-')]:
    answers[k]=answers[k].replace('[MPI message envelope]('+ 'https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node60.htm)', '[MPI message envelope](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node58.htm)')
for n in (7,10):
    k=f'AAPP-22-{n:03d}'
    answers[k]=answers[k].replace('https://man7.org/linux/man-pages/man7/pthreads.7.html','https://man7.org/linux/man-pages/man3/pthread_cond_wait.3p.html').replace('Linux man-pages: POSIX threads overview','POSIX condition wait')
for n in (9,12,15,18):
    k=f'AAPP-22-{n:03d}'
    answers[k]=answers[k].replace('https://man7.org/linux/man-pages/man7/pthreads.7.html','https://man7.org/linux/man-pages/man3/pthread_barrier_wait.3p.html').replace('Linux man-pages: POSIX threads overview','POSIX barrier wait')
answers['AAPP-22-016']=answers['AAPP-22-016'].replace('https://man7.org/linux/man-pages/man7/pthreads.7.html','https://man7.org/linux/man-pages/man3/pthread_exit.3p.html').replace('Linux man-pages: POSIX threads overview','POSIX thread exit')

for k,v in answers.items():
    assert not any(ord(c)<32 and c not in '\n\t' for c in v),k
    assert v.count('```')%2==0,k
    text=re.sub(r'```.*?```','',v,flags=re.S)
    assert len(re.findall(r'(?<!\\)\$',text))%2==0,k
    assert len(v.split())>=25,k

matches=list(re.finditer(r'^### (AAPP-\d{2}-\d{3})\s*$',snapshot,re.M))
assert len(matches)==552
intro=snapshot[:matches[0].start()]
intro=intro.replace('Original prompts are preserved, with your attempts and review feedback beneath the questions you have worked on.','Original prompts are preserved, with your attempts, review feedback, and a collapsed **Model answer** for every question.')
intro=intro.replace('Unanswered questions should remain blank.','Your **My answer** space stays available for practice, even when a reference answer is provided below it.')
intro=intro.replace('## Editorial conventions','> [!tip] Reference answers added — 2026-11-02\n> Every one of the 552 entries has a collapsed **Model answer**, including previously unanswered or incomplete questions. Your original attempts and existing feedback are preserved. Try a question under **My answer** whenever useful, then expand the reference or request correction by its stable ID.\n>\n> Model answers state necessary assumptions, distinguish expected/worst-case/amortized costs, and flag defects in the printed source. Where the supplied notes do not identify a lecture-specific example, a standard example is explicitly labelled. Programming-model references use official OpenMP/MPI/CUDA/Halide documentation or the POSIX manual. Code is exam-style pseudocode or an illustrative snippet unless stated otherwise.\n\n## Editorial conventions')
intro=intro.replace('Do not fill in unanswered questions unless explicitly requested.','Reference answers are now explicitly requested for all questions. Continue preserving **My answer** as your practice space; future corrections should assess your attempt independently of the supplied model.')
parts=[intro]
original_blocks={}
for i,m in enumerate(matches):
    key=m.group(1)
    end=matches[i+1].start() if i+1<len(matches) else len(snapshot)
    original=snapshot[m.start():end]
    # A section heading between entries belongs outside the preceding answer callout.
    section=re.search(r'^## ',original,re.M)
    if section:
        body=original[:section.start()]
        following=original[section.start():]
    else:body=original;following=''
    callout='> [!success]- Model answer\n'+''.join(('> '+line+'\n') if line else '>\n' for line in answers[key].strip().splitlines())
    parts.append(body+callout+'\n'+following)
    original_blocks[key]=(body,following)
candidate=''.join(parts)
assert re.findall(r'^### (AAPP-\d{2}-\d{3})',candidate,re.M)==[q['id'] for q in questions]
assert len(re.findall(r'^> \[!success\]- Model answer$',candidate,re.M))==552
assert candidate.split('---',2)[:3][1]==snapshot.split('---',2)[:3][1]

# Remove inserted model blocks and compare each original question/attempt/feedback exactly.
for i,m in enumerate(list(re.finditer(r'^### (AAPP-\d{2}-\d{3})\s*$',candidate,re.M))):
    nexts=re.search(r'^### AAPP-',candidate[m.end():],re.M)
    end=m.end()+nexts.start() if nexts else len(candidate)
    block=candidate[m.start():end]
    start=block.index('> [!success]- Model answer\n')
    before=block[:start]
    after=block[start:]
    sec=re.search(r'^## ',after,re.M)
    following=after[sec.start():] if sec else ''
    oldbody,oldfollowing=original_blocks[m.group(1)]
    assert before==oldbody,(m.group(1),'original content changed')
    assert following==oldfollowing,(m.group(1),'section context changed')

# Validate all new wikilinks against actual note filenames and headings.
files=list(vault.rglob('*.md'))
by_stem={}
for f in files:
    if any(x.startswith('.') for x in f.relative_to(vault).parts):continue
    by_stem.setdefault(f.stem,[]).append(f)
link_issues=[]
for link in sorted(set(re.findall(r'\[\[([^\]]+)\]\]','\n'.join(answers.values())))):
    target=link.split('|')[0]
    title,_,heading=target.partition('#')
    if not title:continue
    choices=by_stem.get(title,[]) if not title.endswith('.pdf') else list(vault.rglob(title))
    if not choices:link_issues.append((link,'missing target'));continue
    if heading and not title.endswith('.pdf'):
        heads=[h.strip() for f in choices for h in re.findall(r'^#{1,6}\s+(.+)$',f.read_text(),re.M)]
        if heading not in heads:link_issues.append((link,'missing heading'))

(out/'answers-all.json').write_text(json.dumps(answers,ensure_ascii=False,indent=2)+'\n')
(out/'Past Exam Question Bank.completed.md').write_text(candidate)
report={'entries':552,'model_answers':552,'original_content_preserved':True,'word_count':sum(len(v.split()) for v in answers.values()),'section_counts':dict(sorted(Counter(q['section'] for q in questions).items())),'wikilink_issues':link_issues,'snapshot_sha256':hashlib.sha256(snapshot.encode()).hexdigest(),'candidate_sha256':hashlib.sha256(candidate.encode()).hexdigest()}
(out/'completion-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert not link_issues,'Fix new-link targets before applying.'
# Refuse to overwrite concurrent edits; allow idempotent re-runs of this same pass.
current=bank.read_text()
assert current in (snapshot,candidate),'The source note changed during generation; merge before writing.'
bank.write_text(candidate)
print('Applied complete reference answers to the vault note.')
