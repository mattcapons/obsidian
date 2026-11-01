from pathlib import Path
import itertools
import math
import re
import sys

COURSE = Path('/home/matteo/Documents/Obsidian/University/Advanced Algorithms and Parallel Programming')
NAMES = ['AAPP Index', 'Course Introduction', 'Algorithm as recipes', 'Divide and Conquer', 'PRAM', 'ISPC', 'Randomized Algorithms']
paths = {n: COURSE / ('AAPP Index.md' if n == 'AAPP Index' else 'Notes/' + n + '.md') for n in NAMES}
originals = {n: p.read_text() for n, p in paths.items()}
updates = originals.copy()

def replace(name, old, new):
    assert updates[name].count(old) == 1, f'Expected one match in {name}: {old[:70]}'
    updates[name] = updates[name].replace(old, new, 1)

def before(name, heading, text):
    replace(name, heading, text.strip() + '\n\n' + heading)

def after(name, anchor, text):
    replace(name, anchor, anchor + '\n\n' + text.strip())

before('Course Introduction', '## Teaching material', r'''
## Study priorities for the supplied decks

This checklist defines the scope of this note collection, based on the six PDFs currently supplied. It is a study guide, not confirmation that these PDFs cover the entire exam.

| Note | What to be able to do without looking |
|---|---|
| [[Algorithm as recipes]] | Trace sorting, distinguish bounds from input cases, derive and solve recurrences |
| [[Divide and Conquer]] | Identify recursive calls, verify Strassen's products, analyze tree-layout dimensions |
| [[PRAM]] | Check access legality, calculate time/work/cost, interpret scaling experiments |
| [[ISPC]] | Identify uniform/varying data, trace masks and local counts, explain gang versus task parallelism |
| [[Randomized Algorithms]] | State the probability space, use indicators, derive expected hires and sampling failure |

For a written answer, state the assumptions, explain the algorithm, justify correctness, and show the calculation. For an open question, connect the definition to one of the lecture examples. The technical notes now include **Exam practice** sections with original problems and worked solutions based on these topics.

External material in the notes supplies explanations for these same concepts. The broader syllabus announced in the introduction remains a roadmap until its decks or exercises are supplied. Dates and grading rules continue to come from the uploaded introduction rather than unrelated external courses.
''')

after('Algorithm as recipes', 'The first result follows by bounding the polynomial above and below by constant multiples of $n^3$ once $n$ is sufficiently large. The second follows because $2n^2/n^3=2/n\\to0$.', r'''
### Comparing growth rates

For positive $g(n)$, the ratio $f(n)/g(n)$ is often a useful first check:

- Ratio tending to zero establishes $f=o(g)$.
- Ratio tending to a finite positive constant establishes $f=\Theta(g)$.
- Ratio tending to infinity establishes $f=\omega(g)$.

The converse for $\Theta$ need not give a limit: a bounded positive oscillating ratio can still establish a tight bound. Also, changing the logarithm's base multiplies it by a constant, because $\log_b n=\log_a n/\log_a b$ for fixed $a,b>1$.

For example, $\log n=o(n^{1/2})$ and $n\log n=o(n^2)$. When proving a bound, state the constants and the threshold beyond which the inequality holds; do not only say “drop small terms.” This is supplementary reasoning for the notation in slides 11–13.
''')

after('Algorithm as recipes', 'Insertion sort uses constant auxiliary space and is stable with the strict comparison `>`: equal keys are not shifted past each other.', r'''
**Supplementary worked count:** an inversion is a pair $i<j$ with $A[i]>A[j]$. Each rightward shift removes one inversion, so the total number of shifts is the initial inversion count. In $[4,1,3,2]$, the inversions are $(4,1),(4,3),(4,2),(3,2)$: four shifts in total. The outer-loop overhead remains linear even when there are no inversions. This explains why nearly sorted inputs can be cheap.

The linear best case and quadratic worst case should always be attached to the stated input conditions. The underlying operation-count approach is also explained in [MIT's insertion-sort and merge-sort lecture](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/resources/lecture-1-administrivia-introduction-analysis-of-algorithms-insertion-sort-mergesort/index.html).
''')

old_sub = r'''**Supplementary substitution example:** for $T(n)=2T(n/2)+cn$, assume $T(n/2)\le K(n/2)\log_2(n/2)$. Then

$$
T(n)\le Kn(\log_2 n-1)+cn
\le Kn\log_2n
$$

when $K\ge c$. A suitable base-case adjustment completes the upper bound. The level-cost argument supplies the matching lower bound.'''
new_sub = r'''**Supplementary substitution proof:** take powers of two, $T(1)=d>0$, and $T(n)=2T(n/2)+cn$ with $c>0$. Prove $T(n)\le Kn\log_2n+Dn$ using $K\ge c$ and $D\ge d$.

The base case gives $T(1)=d\le D$. For the induction step,

$$
\begin{aligned}
T(n)&\le 2\left(K\frac n2\log_2\frac n2+D\frac n2\right)+cn\\
&=Kn\log_2n+Dn+(c-K)n\\
&\le Kn\log_2n+Dn.
\end{aligned}
$$

This makes the base-case constant explicit. For this exact recurrence, expanding levels gives $T(n)=dn+cn\log_2n$, supplying both the upper and lower bound. Hence $T(n)=\Theta(n\log n)$. For a nonrecursive term specified only as $\Theta(n)$, use constant upper and lower multiples of $n$ rather than asserting an exact equality.'''
replace('Algorithm as recipes', old_sub, new_sub)

after('Algorithm as recipes', 'In Cases 1 and 3, the difference must be polynomial. Merely being smaller or larger is insufficient. In Case 3, do not omit the regularity condition.', r'''
**Application checklist:** $a,b$ must be constants, and the nonrecursive cost must be eventually positive. Identify $a,b,f(n)$, compute $d=\log_ba$, and justify a case. If a condition fails, use a recursion tree or substitution. In standard balanced recurrences, floors and ceilings do not alter these asymptotic results. This is the form used in [MIT's Master theorem practice sheet](https://people.csail.mit.edu/thies/6.046-web/master.pdf).
''')

replace('Algorithm as recipes', '> Dijkstra requires nonnegative edge weights. For the lazy priority-queue implementation shown, skip a popped entry when its stored distance differs from the current `dist[u]`. Otherwise stale entries can repeat edge scans, so the usual efficient implementation analysis does not directly describe the fragment as printed. A heap implementation with decrease-key has the familiar $O((V+E)\\log V)$ bound; lazy heaps are commonly analyzed using $\\log E$ instead.', r'''> Dijkstra requires nonnegative edge weights. In the lazy priority-queue version, add `if (d != dist[u]) continue;` immediately after popping an entry. This avoids rescanning edges for obsolete distances. An indexed binary heap with decrease-key gives $O((V+E)\log V)$; the lazy heap can have $O(E)$ entries and is bounded by $O(V+(E+1)\log(E+2))$, including initialization. For simple graphs this is commonly expressed with a $\log V$ factor. The distinction and stale-entry check are explained in the [implementation's own documentation](https://cp-algorithms.com/graph/dijkstra_sparse.html#priority_queue).''')

before('Algorithm as recipes', '## Revision questions', r'''
## Exam practice

These are original practice questions based on the supplied deck, not past exam questions.

**1. Trace and count.** Sort $[4,1,3,2]$ by insertion sort. Count element shifts, then explain why the count is not the same as elapsed time.

> [!faq]- Worked solution
> The arrays after each insertion are $[1,4,3,2]$, $[1,3,4,2]$, and $[1,2,3,4]$. Shift counts are $1,1,2$, totaling $4$. Time also includes comparisons, key writes, loop control, and machine-dependent costs.

**2. Select a recurrence case.** Solve $T(n)=3T(n/2)+n^2$. Then explain why simply calling the nonrecursive term “larger” is insufficient.

> [!faq]- Worked solution
> The reference exponent is $d=\log_2 3\approx1.585$. The gap $2-d>0$ is polynomial. Regularity holds because $3(n/2)^2=(3/4)n^2$. Case 3 gives $\Theta(n^2)$. A positive polynomial gap and regularity are both required, rather than just a qualitative comparison.
''')

after('Divide and Conquer', 'Source: [[lecture3-DandC.pdf#page=2|Design paradigm]]. For recurrence tools, see [[Algorithm as recipes#Solving recurrences]].', r'''
### Turning the design into an exam answer

For correctness, use induction on input size: establish the base case, assume recursive calls solve smaller instances, then explain why combining those answers solves this instance. For complexity, count the calls actually made and charge the divide/combine work separately. A split into two pieces does not imply two recursive calls, and a block addition is not constant-time when blocks grow.

The supplied deck adapts these examples from [Demaine and Leiserson's MIT divide-and-conquer notes](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/9cdb6914be3e87215cb86f327ee4180b_lec3.pdf). Use only the matching examples here; that external lecture also contains material outside the supplied deck.
''')

before('Divide and Conquer', '### Complexity', r'''
### Numerical check of the seven products

**Supplementary worked example:** let

$$
A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad
B=\begin{pmatrix}5&6\\7&8\end{pmatrix}.
$$

Using the lecture's $P_i$ convention gives

$$
(P_1,P_2,P_3,P_4,P_5,P_6,P_7)=(-2,24,35,8,65,-30,-22).
$$

Consequently $r=65+8-24-30=19$, $s=-2+24=22$, $t=35+8=43$, and $u=65-2-35+22=50$:

$$
AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}.
$$

Checking by the ordinary row-column rule produces the same result. Product numbering differs across textbooks, so keep each set of product formulas together with its corresponding reconstruction formulas.
''')

before('Divide and Conquer', '## Revision questions', r'''
## Exam practice

These are original problems using the deck's algorithms and layouts.

**1. Explain duplicate recursion.** A power routine makes two independent calls to compute $a^{n/2}$, then multiplies their results. Compare it with computing that value once and storing it.

> [!faq]- Worked solution
> For even powers of two, duplicate calls give $T(n)=2T(n/2)+\Theta(1)=\Theta(n)$. Reusing a single result gives $T(n)=T(n/2)+\Theta(1)=\Theta(\log n)$. Both are correct, but their computation trees differ. Counting the mathematical expression's two factors as two necessary calls misses the opportunity to reuse a value.

**2. Analyze a layout rather than runtime.** An H-tree side length satisfies $L(n)=2L(n/4)+c$, with $L(1)=\ell_0>0$. Derive the side length and area for $n=4^k$.

> [!faq]- Worked solution
> Expansion gives $L(n)=2^k\ell_0+c(2^k-1)$. Since $2^k=\sqrt n$, the side is $\Theta(\sqrt n)$ and the square's area is $\Theta(n)$. The recurrence counts side length, so its answer must be squared to obtain area.
''')

after('PRAM', '**Supplementary interpretation:** $W/T_\\infty$ is its average parallelism. Reserving substantially more processors cannot remove the critical path.', r'''
**Supplementary connection to the simulation slides:** under ideal unit-cost operations and suitable scheduling, a computation of work $W$ and depth $D$ can run on CREW PRAM in $O(W/p+D)$ time. This is Brent's scheduling principle; it refines the idea of batching virtual processors. It supplies an explanation of the existing work/depth quantities, rather than a claim about actual machine timing. [Blelloch and Maggs, *Parallel Algorithms*, §25.2.4](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf).

For the tree sum, $W=\Theta(n)$ and $D=\Theta(\log n)$, giving the ideal bound $O(n/p+\log n)$. This describes a schedule for that computation. The chunk-and-tree algorithm below reorganizes the computation for the chosen $p$ and has its own $\log p$ reduction term.
''')

after('PRAM', 'It is cost-optimal while $p\\log p=O(n)$. Once the reduction overhead dominates local work, adding processors offers diminishing returns.', r'''
Using the optimal sequential sum as baseline, the chunk-and-tree model gives, up to constant factors,

$$
S_p=\Theta\left(\frac{n}{n/p+\log p}\right),\qquad
E_p^*=\Theta\left(\frac{n}{n+p\log p}\right).
$$

If $p\log p\ll n$, local work dominates and scaling is close to linear in this ideal model. If $p\log p\gg n$, the reduction term dominates and efficiency shrinks. Thus “work-efficient” and “efficient use of a particular allocation” answer different questions.
''')

after('PRAM', 'Source: [[lecture4-PRAM.pdf#page=23|Prefix-sum pattern]].', r'''
### Inclusive scan, exclusive scan, and compaction

**Supplementary clarification:** an inclusive sum includes the current element; an exclusive sum includes only earlier elements and starts with the additive identity $0$. A scan can use any associative operator; a general exclusive scan also needs an identity. Commutativity is not required when the original element order is preserved. [Blelloch, *Prefix Sums and Their Applications*, §§1.1–1.2](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf).

For $[3,1,4,2]$, the inclusive result is $[3,4,8,10]$ and the exclusive result is $[0,3,4,8]$.

**Worked compaction example:** let keep-flags be $[1,0,1,1,0]$. Their exclusive scan is $[0,1,1,2,3]$. Only kept elements write: input positions $0,2,3$ write to output positions $0,1,2$. These positions are distinct, so the output writes are exclusive; the preserved input order makes the compaction stable. The output length is the sum of the flags, $3$.

This explains a use of prefix sums already listed in the deck, without adding another sorting or graph algorithm.
''')

after('PRAM', 'With $s=0.1$ and $P=8$, it is $7.3$. This does not contradict Amdahl: the workload and definition of the measured serial fraction differ.', r'''
**Supplementary derivation from the lecture's formulas:** normalize the fixed-size sequential runtime to one. Amdahl's parallel runtime is the unchanged serial part $s$ plus $(1-s)/P$. For Gustafson, normalize the observed parallel runtime to one: the sequential machine would execute the same serial part $s$ and $P$ copies of the observed parallel part $1-s$.

Neither expression includes communication or scheduling overhead. An overhead term $h(P)$ in Amdahl's normalized runtime changes the prediction to $1/(s+(1-s)/P+h(P))$. This helps explain a measured plateau without changing the ideal law.
''')

before('PRAM', '## Revision questions', r'''
## Exam practice

These are original problems under explicit idealized assumptions.

**1. Work, time, and cost.** Sum 16 values on four processors. Count only additions: each processor first sums four local values, then four partial sums are reduced by a binary tree.

> [!faq]- Worked solution
> Local sums take three rounds, followed by two tree rounds: $T_4=5$. Work is $4\cdot3+3=15$ additions. Allocated cost is $4\cdot5=20$ processor-rounds. The sequential addition count is 15, so $S_4=3$ and $E_4^*=3/4$. Reads, initialization, and barriers are deliberately excluded from this small count. The idle slots during tree reduction explain $C_4>W$.

**2. Baseline trap.** Suppose $T^*=50$, $T_1=100$, $T_4=30$. Calculate speedup and both efficiency conventions.

> [!faq]- Worked solution
> $S_4=50/30=5/3$. Best-baseline efficiency is $E_4^*=50/(4\cdot30)=5/12$. The lecture's one-processor-implementation convention gives $E_4=100/(4\cdot30)=5/6$. The larger number does not remove the implementation's extra sequential work. Always state the baseline before interpreting the result.
''')

after('ISPC', '“Varying/private” describes per-instance values; it does not imply that all memory referenced by an instance is isolated. Instances can access shared array storage and can race if their writes collide.', r'''
### Masks and divergence

**Supplementary language clarification:** a gang shares a program counter, while an execution mask identifies the active instances. A varying conditional can run both branches under different masks; varying loops continue until all participating instances finish. [Official ISPC execution model](https://ispc.github.io/ispc.html#control-flow-within-a-gang).

For four lanes with inputs $[1,7,3,8]$ and condition `x > 5`, the true-branch mask is $[0,1,0,1]$. Only lanes 1 and 3 update their varying counters. A `uniform` counter would not represent four independent local counts.

In a Mandelbrot gang where iteration counts are $[2,2,2,100]$, the long-running pixel keeps the loop going after the other three lanes become inactive. The pixels are independent, but their different control paths can reduce SIMD utilization.
''')

after('ISPC', 'The condition can differ between instances. A mask selects which instances execute the increment. A varying branch should therefore be understood in terms of active instances rather than independent CPU threads.', r'''
**Why reduce after the loop?** Accumulate varying local totals during `foreach`, then call `reduce_add` once. Repeated cross-lane reductions inside the loop can spend more time communicating than vectorization saves. Favor contiguous lane accesses where the data permits. These principles are explained in the [ISPC performance guide](https://ispc.github.io/perfguide.html#implementing-reductions-efficiently).

In the row-major matrix example, neighboring column lanes read neighboring entries of $B$ at a fixed $k$, while sharing the row's $A$ value. This favorable lane access is different from the full cache behavior across all $k$ iterations; SIMD-friendly code can still have memory bottlenecks.
''')

after('ISPC', 'This is a teaching approximation, not a replacement for a numerical library. Large arguments, finite precision, and an insufficient truncation order affect accuracy. Validate against a reference before comparing performance.', r'''
**Supplementary numerical check:** for $x=1$ and exactly three terms, the corrected kernel should approximate $1-1/6+1/120=101/120\approx0.8416667$. For $x=0$, every term is zero; for $x=-1$, the result is the negative of the value at $1$. These checks expose indexing and sign errors without treating a timing result as evidence of correctness.
''')

before('ISPC', '## Takeaways', r'''
## Reduction order and numerical results

**Supplementary connection to the lecture examples:** real-number addition is associative, but floating-point addition can lose that property through rounding. A tree reduction may therefore differ from a sequential accumulation even when both implement the same mathematical sum. Compare floating-point outputs with a stated tolerance; exact integer counting remains exact when the integer range is sufficient. [Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic*](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

For instance, in double precision, $(10^{16}+(-10^{16}))+1$ is $1$, while $10^{16}+((-10^{16})+1)$ can be $0$. This is a rounding example, not an algebraic difference in the intended mathematical result.

For benchmark comparisons, use the same inputs, term count, output accuracy requirement, and comparable optimization settings. Check the answers first, separate warm-up from measured runs, and report repeated timings. The presence of SIMD or higher CPU utilization alone does not establish speedup.
''')

before('ISPC', '## Revision questions', r'''
## Exam practice

These are original traces of the language ideas covered by the slides.

**1. Trace a reduction.** Four instances have local counters $[2,1,3,4]$ after `foreach`. What does `reduce_add(counter)` return? What changes if it is called while only lanes 1 and 3 are active?

> [!faq]- Worked solution
> With all four active, it returns the uniform value $10$. With only lanes 1 and 3 active, the reduction includes their values only, giving $1+4=5$. A reduction inside a varying branch is not automatically a reduction over the whole gang. Place the final count reduction after the conditional and loop, as in the note's kernel.

**2. Separate the parallelism levels.** A gang has eight logical instances. A row-task matrix multiplication launches 100 tasks on a four-worker runtime. Does this create 800 OS threads?

> [!faq]- Worked solution
> No. A task executes a gang's SPMD work using SIMD execution; the runtime schedules tasks on four workers. The task count, logical instance count, hardware vector width, and worker count are different quantities. Multiple tasks must be scheduled on each worker over time.
''')

after('Randomized Algorithms', 'No independence assumption is required for this equality. Independence matters for other calculations, such as multiplying the probabilities of repeated sampling failures.', r'''
### Why dependence does not invalidate linearity

**Supplementary proof for a finite sample space:** write both variables on the same outcomes $\omega$:

$$
\mathbb E[X+Y]
=\sum_\omega (X(\omega)+Y(\omega))\Pr(\omega)
=\mathbb E[X]+\mathbb E[Y].
$$

This distributes a sum; it never replaces a joint probability with a product. For example, let $X$ indicate heads on one fair coin and let $Y=1-X$. They are dependent, but $\mathbb E[X+Y]=1=1/2+1/2$. Independence is needed for the general product rule $\mathbb E[XY]=\mathbb E[X]\mathbb E[Y]$, not for linearity. [Aspnes's Yale notes on random variables, §§3.2–3.3](https://www.cs.yale.edu/homes/aspnes/pinewiki/RandomVariables.html).
''')

after('Randomized Algorithms', 'For $n=4$, $H_4=1+1/2+1/3+1/4=25/12\\approx2.083$ expected hires. This can be fractional because it averages integer counts over many orders.', r'''
**Distinguish position from identity:** the probability $1/i$ concerns the applicant arriving at position $i$. An applicant of fixed quality rank has a different hiring probability. This derivation uses symmetry among the first $i$ arrival positions; it does not assign the same hiring probability to every applicant.

**Worked execution:** quality ranks $[3,1,4,2,5]$ produce hires at positions $1,3,5$. The indicators are $[1,0,1,0,1]$ and their sum is $3$. One run need not equal the expectation over random orders.
''')

after('Randomized Algorithms', 'The slides motivate this strategy but do not give a full permutation-generation algorithm; the pseudocode is an added explanation.', r'''
**Shuffle pitfall:** swapping each position with an independently chosen index from the entire array is not generally a uniform shuffle. For three elements, that scheme has $3^3=27$ equally likely index sequences but six possible permutations; equal output probabilities would require each permutation to have $27/6$ preimages, which is impossible. Choosing uniformly from the shrinking unassigned region avoids this problem.
''')

after('Randomized Algorithms', 'If $q=0$, the unbounded Las Vegas search never finds a target. The promise that a target exists is therefore essential. Sampling without replacement changes the distribution, so the same failure formula cannot simply be reused.', r'''
### Deriving the expected number of trials

**Supplementary derivation:** let $K$ count all trials including the successful one, and let $q>0$ be the independent success probability. After the first trial, success leaves no further work; failure restarts the same experiment. Hence

$$
\mathbb E[K]=1+(1-q)\mathbb E[K],\qquad
\mathbb E[K]=1/q.
$$

For this restart calculation the geometric waiting time has finite expectation. Be clear about its convention: counting failed trials only gives $\mathbb E[K-1]=(1-q)/q$. [Aspnes, *Notes on Randomized Algorithms*, §3.6.2](https://www.cs.yale.edu/~aspnes/classes/469/notes.pdf).

In the bounded version, finding a valid index early may finish in fewer than $k$ trials, but the **worst-case** bound remains $k$. Repeating an already-valid witness check is not necessary; the probability calculation concerns runs that have not yet succeeded.
''')

before('Randomized Algorithms', '## Revision questions', r'''
## Exam practice

These are original problems using the deck's probability model.

**1. Hiring cost.** Four distinct applicants are uniformly permuted. An interview costs $1$ and a hire costs $12$. Compute expected cost, and compare the best and worst orders.

> [!faq]- Worked solution
> $H_4=25/12$, so $\mathbb E[C]=4+12(25/12)=29$. Best order costs $4+12=16$; worst order costs $4+4\cdot12=52$. Interview cost is paid for all four applicants in every order.

**2. Change the success fraction.** One quarter of an array's entries are targets. Sample independently and uniformly with replacement. Derive the expected Las Vegas trial count and the trial budget giving bounded-search failure probability at most $0.01$.

> [!faq]- Worked solution
> The expected count is $1/(1/4)=4$. Failure after $k$ trials is $(3/4)^k$. The required budget is $k\ge\lceil\ln(0.01)/\ln(3/4)\rceil=17$. The logarithm of $3/4$ is negative, so dividing by it reverses the inequality. Sixteen trials fail with probability about $0.01002$; seventeen with about $0.00752$.
''')

after('AAPP Index', 'The notes consolidate repeated slides. Supplementary explanations and apparent slide errors are labeled explicitly. Revision questions include short answers at the end of each technical note.', r'''
## Exam practice and review

The notes have been reviewed against the supplied slides and checked with selected university materials and official documentation. Added explanations remain tied to the existing deck topics; citations appear beside the claims they support. Course administration still follows the uploaded introduction.

- [[Algorithm as recipes#Exam practice]] — sorting traces and recurrence-case selection.
- [[Divide and Conquer#Exam practice]] — recursion reuse and H-tree dimensions.
- [[PRAM#Exam practice]] — operation counts and sequential-baseline choices.
- [[ISPC#Exam practice]] — active-lane reductions and gang/task distinctions.
- [[Randomized Algorithms#Exam practice]] — expected hiring cost and sampling budgets.

The worked problems are original practice, not retrieved past-paper questions. The six decks establish the current collection's boundaries; they do not establish that every announced exam topic has already been supplied.
''')

# Structural review: keep existing metadata, diagrams, and link targets intact.
files = list(COURSE.rglob('*'))
by_stem = {p.stem: p for p in files if p.is_file() and p.suffix == '.md'}
by_name = {p.name: p for p in files if p.is_file()}
headings = {n: set(re.findall(r'^#{1,6} (.+)$', t, re.M)) for n, t in updates.items()}
for name, text in updates.items():
    assert text.split('---', 2)[1] == originals[name].split('---', 2)[1], f'Properties changed: {name}'
    assert re.findall(r'!\[\[[^\]]+\]\]', text) == re.findall(r'!\[\[[^\]]+\]\]', originals[name]), f'Images changed: {name}'
    assert text.count('```') % 2 == 0 and text.count('$$') % 2 == 0 and text.count('$') % 2 == 0
    for link in re.findall(r'\[\[([^\]]+)\]\]', text):
        target = link.replace('\\|', '|').split('|')[0]
        base, _, section = target.partition('#')
        assert base in by_stem or base in by_name, f'Missing target: {name}: {base}'
        if section and base in headings:
            assert section in headings[base], f'Missing heading: {name}: {target}'
    # Any unescaped table separator inside a wikilink would recreate the old table bug.
    for line in text.splitlines():
        if line.startswith('|'):
            for link in re.findall(r'\[\[([^\]]+)\]\]', line):
                assert not re.search(r'(?<!\\)\|', link), f'Unescaped table alias: {name}'

# Independent checks for new numerical examples.
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
assert [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)] == [[19,22],[43,50]]
assert [1*(6-8),(1+2)*8,(3+4)*5,4*(7-5),(1+4)*(5+8),(2-4)*(7+8),(1-3)*(5+6)] == [-2,24,35,8,65,-30,-22]
assert math.ceil(math.log(0.01)/math.log(0.75)) == 17
assert 0.75**17 <= 0.01 < 0.75**16
assert ((1e16 + -1e16) + 1) == 1 and (1e16 + (-1e16 + 1)) == 0
hire_counts = []
for order in itertools.permutations(range(4)):
    best = -1
    count = 0
    for rank in order:
        if rank > best:
            best = rank
            count += 1
    hire_counts.append(count)
assert sum(hire_counts)/len(hire_counts) == 25/12
assert 4 + 12*(sum(hire_counts)/len(hire_counts)) == 29
for n, txt in updates.items():
    print(n, f'{len(originals[n].split())} -> {len(txt.split())} words')
print('Validated 7 revised files, 10 original practice problems, metadata, image preservation, links, tables, and numerical examples.')

if '--install' in sys.argv:
    for n, p in paths.items():
        assert p.read_text() == originals[n], f'Note changed during preparation: {n}'
    snapshot = Path('/tmp/aapp-before-review')
    snapshot.mkdir(exist_ok=True)
    for n, p in paths.items():
        (snapshot / (n + '.txt')).write_text(originals[n])
        p.write_text(updates[n])
        assert p.read_text() == updates[n]
    print('Saved all reviewed notes and index; preserved originals in /tmp/aapp-before-review.')
