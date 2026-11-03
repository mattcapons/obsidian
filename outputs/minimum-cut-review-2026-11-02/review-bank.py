from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
out = Path('outputs/minimum-cut-review-2026-11-02')

feedback = {
1: r'''**Assessment: mostly correct basic Karger analysis; the Karger–Stein description and comparison are incomplete.** Your contraction idea, repetition order, and $O(n^4\log n)$ amplified bound match the course model. Three details matter: $2/[n(n-1)]$ is a lower bound on success, rather than necessarily its exact probability; contraction must preserve parallel-edge multiplicities and remove self-loops; and both Karger–Stein branches recurse using Karger–Stein, rather than simply finishing with one ordinary Karger path each.

**Suggested exam answer — Karger:** For a connected undirected unweighted graph with $n\ge2$ vertices, repeatedly choose a uniformly random remaining edge copy and merge its endpoints. Retain parallel edges, remove self-loops, and record which original vertices each supernode contains. After $n-2$ contractions, return the cut between the two supernodes. A chosen minimum cut survives whenever none of its edges is contracted; its survival probability is at least $p_0=2/[n(n-1)]$. Repeat from fresh copies of the original graph with independent random choices and retain the smallest returned cut. With $R$ runs, failure probability is at most $(1-p_0)^R\le e^{-p_0R}$. Thus your budget, written precisely as $R=\lceil c\,n(n-1)\ln n/2\rceil$, suffices for failure at most $n^{-c}$, for fixed $c>0$. At $O(n^2)$ time per run, total time is $O(n^4\log n)$.

**Suggested exam answer — Karger–Stein:** At a recursive call with $n>6$ supernodes, make two fresh copies and independently contract each to $t=\lceil1+n/\sqrt2\rceil$ supernodes. Recursively run Karger–Stein on both resulting multigraphs, and return the smaller lifted cut. For $n\le6$, find the minimum cut exactly by enumerating the nontrivial partitions. This branching is repeated at every recursive level. The threshold is a number of supernodes to leave, rather than a number of contractions to perform. It preserves a chosen minimum cut in a partial contraction with probability at least $1/2$, but the recursive call must still find that cut. One full recursive run has success probability $\Omega(1/\log n)$.

**Complexity comparison:** Under the lecture's quadratic contraction/copying model, one recursive run satisfies $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Exploring that recursion tree is one run. Repeating whole independent runs $O(\log^2 n)$ times gives inverse-polynomial failure probability and total $O(n^2\log^3 n)$ time.

| Algorithm | Time for one full run | Success guarantee per run | Total time for failure at most $n^{-c}$ |
|---|---|---|---|
| Karger | $O(n^2)$ | At least $2/[n(n-1)]$ | $O(n^4\log n)$ |
| Karger–Stein | $O(n^2\log n)$ | $\Omega(1/\log n)$ | $O(n^2\log^3 n)$ |

Karger–Stein improves the success-versus-time trade-off: its single recursive run costs more, but far fewer independent runs are needed. Both are Monte Carlo algorithms. For a fixed constant error target, the corresponding totals are $O(n^4)$ and $O(n^2\log^2 n)$; the extra logarithm in the table comes from requiring failure at most $n^{-c}$. The distinction between single-run and amplified bounds is also derived in [Vigoda's notes, §1.3.2](https://sites.cs.ucsb.edu/~vigoda/6550/Notes/Lec1.pdf#page=4).

**Base-case detail:** With the stated ceiling, $t=6$ when $n=6$. Use the exact base case $n\le6$ so recursion shrinks; the supplied slide's strict $n<6$ condition needs this correction.

**Study:** [[Minimum Cut#Contraction and the invariant]]; [[Minimum Cut#Repetition and running time]]; [[Minimum Cut#Stop early and branch]]; [[Minimum Cut#Partial survival and recursive success]]; [[Minimum Cut#Time for one run versus amplified time]]; [[lecture6-MinCut.pdf#page=16|slides 16–21]].''',

2: r'''**Assessment: correct classification and outcome distinction; the contraction algorithm is missing.** You correctly say that the output is a valid cut and may fail to be minimum. A limited run count alone does not establish Monte Carlo classification: the relevant combination is bounded runtime and possible error about optimality.

**Suggested exam answer:** Yes. On a connected undirected graph, Karger's algorithm repeatedly samples a uniformly random edge copy and contracts its endpoints until two supernodes remain. Preserve parallel-edge multiplicities, delete self-loops, and track original vertex memberships. The final partition defines a valid cut of the original graph, but an unlucky contraction can destroy the minimum cut being preserved. A basic run succeeds with probability at least $2/[n(n-1)]$ and takes $O(n^2)$ time in the course implementation model. Fresh independent repetitions improve reliability by keeping the smallest returned cut; $O(n^2\log n)$ runs suffice for inverse-polynomial failure, giving $O(n^4\log n)$ total time.

It is Monte Carlo because the runtime budget is bounded while the answer may be non-optimal. Verifying that the returned partition is a valid cut does not certify that it is minimum, so this check alone does not turn the algorithm into Las Vegas. Finite repetition gives a probability guarantee, rather than a universal zero-error guarantee.

**Study:** [[Minimum Cut#Contraction and the invariant]]; [[Minimum Cut#Success probability]]; [[Minimum Cut#Repetition and running time]]; [[Randomized Algorithms#Interpreting the error direction]]; [[lecture6-MinCut.pdf#page=9|slides 9–16]].''',
}

selected = set(__import__('json').loads((out / 'selected-questions.json').read_text()))
assert selected == {f'AAPP-06-{n:03d}' for n in feedback}
original = bank_path.read_bytes()
text = original.decode('utf-8')
snapshot = (out / 'Past Exam Question Bank.md.snapshot').read_text()
for number, body in feedback.items():
    qid = f'AAPP-06-{number:03d}'
    pattern = rf'(^### {qid}\n.*?)(?=^### |^## |\Z)'
    match = re.search(pattern, text, re.M | re.S)
    before = re.search(pattern, snapshot, re.M | re.S)
    assert match and before, qid
    assert match[1] == before[1], f'{qid} changed during review'
    assert '*Write your answer here.*' not in match[1], qid
    old = '> [!note]- Feedback\n> Not reviewed yet.'
    assert match[1].count(old) == 1, qid
    callout = '> [!note]- Feedback\n> **Reviewed: 2026-11-02.**\n>\n'
    callout += '\n'.join('> ' + line if line else '>' for line in body.splitlines())
    text = text[:match.start()] + match[1].replace(old, callout) + text[match.end():]

assert bank_path.read_bytes() == original, 'Note changed while preparing corrections'
bank_path.write_bytes(text.encode('utf-8'))
print('Added feedback to AAPP-06-001 and 002. Unanswered questions and all original attempts preserved.')
