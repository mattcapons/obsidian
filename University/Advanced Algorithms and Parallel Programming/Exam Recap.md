---
tags:
  - aapp
  - exam-recap
status: in-progress
created: 2026-10-30
updated: 2026-11-02
question-bank: "[[Past Exam Question Bank]]"
completed-sections:
  - "01 — PRAM model and memory rules"
  - "02 — Parallel performance and scaling"
  - "03 — PRAM algorithms"
  - "04 — Divide and conquer and recurrences"
  - "05 — Randomized algorithm classes"
---
# AAPP — Exam Recap

[[AAPP Index|Course index]] · [[Past Exam Question Bank|Question bank]]

Quick reminders from completed bank sections. **Prioritize frequent questions, recent exams, and corrected mistakes.** The 25 sections match the bank; sections 1–5 are complete.

%%
Future updates: keep one short paragraph per topic, normally 40–80 words. Assume the theory is already known. Preserve course-note topic order and all 25 main sections. Keep only essential definitions, formulas, examples and corrections; omit derivations, quizzes and repeated explanations. Expand sections after their answers are reviewed, preserve user additions, and update completed-sections and the date.
Section 01 provenance (primary groups; latest exam source):
Purpose/machine: 001,003,009,014,031 — 5 questions; 2026-01-22.
Rounds/communication: 005,008,011,016,021,022,024,025,028,029,034 — 11 questions; 2026-06-11.
Space/word size: 017,027,036 — 3 questions; 2026-09-10.
Access rules/hierarchy: 002,012,030,032,035 — 5 questions; 2026-06-11.
Concurrent writes: 004,006,015,018,026 — 5 questions; 2026-06-29.
Parallel time: 007,010,013,019 — 4 questions; 2024-07-24.
Limited processors: 020,023 — 2 questions; 2026-06-29.
Limited shared memory: 033 — 1 question; 2026-02-09.
All IDs above have prefix AAPP-01-. Counts assign each question once; repeated exam sources were checked for recency.
Section 02 provenance (primary groups; latest exam source):
Speedup/linear scaling: 001,004,014,024,031 — 5 questions; 2025-07-04.
Efficiency/baselines: 006,012,018,021,033 — 5 questions; 2025-11-06.
Work/cost/idling: 008,009,010,016,017,036 — 6 questions; 2026-06-29.
Work efficiency/overhead: 022,040 — 2 questions; 2026-09-10.
Matrix-vector scaling: 029 — 1 question; 2025-06-05.
Bounded processors/do-all: 019 — 1 question; 2024-09-05.
Strong/weak scaling: 013,025,027,034,041 — 5 questions; 2026-09-10.
Amdahl: 015,020,023,026 — 4 questions; 2025-01-24.
Gustafson: 005,011,028,032,035 — 5 questions; 2026-01-22.
Law comparison/interpretation: 002,003,007,030,037,038,039 — 7 questions; 2026-06-29.
Section 02 IDs have prefix AAPP-02-. All 41 questions had review feedback as of 2026-11-01. The five scaling/law groups account for 22 questions: matrix-vector, strong/weak scaling, Amdahl, Gustafson and law comparison. Each question is assigned once; all attached exam sources were checked for recency.
Section 03 provenance (primary groups; latest exam source):
Matrix-vector: 004 — 1 question; 2024-06-26.
Matrix-matrix: 001,005 — 2 questions; 2024-07-24.
Reduction/vector-sum access: 008,009 — 2 questions; 2026-09-10.
Prefix scan/access pattern: 002,003,007 — 3 questions; 2025-11-06.
Scan/reduction comparison: 006 — 1 question; 2025-07-04.
Section 03 IDs have prefix AAPP-03-. All nine questions had review feedback as of 2026-11-01. Prefix scan and its comparison with reduction account for four questions. Each question is assigned once; all attached exam sources were checked for recency. Follow PRAM theory order: map, reduction, prefix scan. Do not infer an exam exclusion from a question's age.
Section 04 provenance (primary groups; latest exam source):
Design/merge-sort example: 001,002,016,019 — 4 questions; 2026-09-10.
Recurrences/Master theorem: 003,006,008,010,011,013 — 6 questions; 2024-11-12.
Powering/time and space: 004,007,009,015,017 — 5 questions; 2026-06-29.
Block multiplication/Strassen: 005,012,014,018 — 4 questions; 2026-06-11.
Section 04 IDs have prefix AAPP-04-. All 19 questions had review feedback as of 2026-11-01. Primary groups assign each question once; topics within questions overlap. Nine prompts explicitly mention the Master theorem: 001,006,008,010,011,012,013,017,019. Questions 008 and 011 also cover binary search, auxiliary space and geometric spatial complexity. Check all sources attached to a question for recency. Follow the theory's example order: merge sort, binary search, powering, matrix multiplication/Strassen, layouts; place the recurrence tools before their applications.
Section 05 provenance (primary groups; latest exam source):
Las Vegas/Monte Carlo classification: 001,003,004 — 3 questions; 2024-11-12.
Efficiency guarantees: 002,005,007 — 3 questions; 2026-06-29.
Sampling example and error bounds: 006 — 1 question; 2026-01-22.
Exact randomized data structures: 008,009 — 2 questions; 2026-09-10.
Section 05 IDs have prefix AAPP-05-. All nine questions had review feedback as of 2026-11-02. The first three groups account for seven Las Vegas/Monte Carlo questions. Each question is assigned once; all attached exam sources were checked for recency. Follow the theory's order: classification/efficiency, sampling example and assumptions, randomized-data-structure application. Give extra emphasis to the missing treap mechanism/example in 008–009 and the sampling promise in 006.
%%

## PRAM model and memory rules

**36 reviewed questions.** Most repeated: rounds and shared-memory communication (**11 questions**). Full theory: [[PRAM]].

### PRAM definition and purpose

PRAM extends RAM to $p$ numbered processors with **private registers and globally accessible shared memory**, synchronous execution, and unit-cost primitive operations. It helps analyze parallelism, dependencies and memory conflicts before adding hardware costs. Proven inefficiency even on a sufficiently powerful PRAM implies inefficiency on comparable conventional machines; a fast PRAM algorithm still needs a hardware performance assessment.

### Rounds and shared-memory communication — most asked; June 2026

The cycle is **read → compute → write → implicit barrier**. A value written in round $r$ becomes readable in round $r+1$; explicit synchronization primitives are unnecessary between rounds. Every processor can make permitted accesses in parallel at **unit latency: one step, not zero time**. Cache, network and bandwidth penalties are abstracted away. Each processor still performs only constant primitive work per round, and same-cell accesses must obey the memory policy.

### Space and word size — September 2026

**Space counts cells used**, not access speed. Unlimited available memory does not imply infinite usage. Under the exam's unbounded-integer convention, one integer occupies one cell regardless of bit length; permitted unit-cost operations ignore that length. This is model-dependent. Shared space counts shared cells; total storage also includes private state, giving $\Theta(m+p)$ for $m$ shared cells and constant local storage per processor.

### Access rules and conflicts — June 2026

**EREW:** one reader and one writer per cell per respective phase. **CREW:** concurrent reads, exclusive writes. **CRCW:** both concurrent, with a specified write rule. A write conflict means multiple processors target the **same cell in the same write phase**. Equal values still violate exclusive write; writes to distinct cells are legal. Synchronization does not remove these same-phase conflicts.

### Model hierarchy — correction from February 2026

An unchanged valid **EREW algorithm runs on CREW and CRCW** under the same underlying machine assumptions. More permissive rules allow extra access patterns without adding accesses to the program. The reverse direction may require copying or extra rounds: for example, EREW broadcasts a value through a doubling tree rather than allowing everyone to read one cell simultaneously.

### Concurrent-write policies — June 2026

**Common:** all writers to a cell must agree; disagreement is illegal, not guaranteed to raise an exception or trigger voting. **Arbitrary:** any contender may win, so every possible winner must be acceptable; there is no “last writer” or implied probability. **Priority:** highest-priority processor wins, regardless of its data value. **Random:** selection follows a specified probability rule. The slides group arbitrary/random together; distinguish them in probabilistic arguments.

### Common CRCW examples — corrected applications

**Boolean OR:** initialize a flag to 0 in an earlier step; only true-input processors write 1. **Sortedness:** initialize a flag to 1; only processors finding an adjacent inversion write 0. Other processors do nothing, so every actual writer agrees. Both take $O(1)$ rounds and $\Theta(n)$ work with enough processors. Common writes do not themselves provide fault detection or security.

### Time versus work — foundation to remember

**$T_p(n)$ counts synchronous rounds; $W(n)$ counts operations across all processors.** Unit-cost computation, unit-cost permitted memory access and lockstep execution justify counting rounds. Equal work distribution is not assumed: processors can be idle. An eight-input tree sum uses three addition rounds but seven additions. $T^*$ is the best sequential baseline; $T_1$ is this parallel algorithm run on one processor.

### Bounded processors — June 2026

Simulating $q$ virtual processors taking $t$ rounds on $p<q$ physical processors costs $O(t\lceil q/p\rceil)$. Keep virtual states separate and preserve read-before-write ordering across batches. Also, $T_p\ge\max(W/p,D)$, where $D$ is critical-path length. A fixed constant $p$ allows only constant-factor improvement over optimal sequential time under compatible model assumptions; if $p$ grows with $n$, retain it in the bound.

### Reduced shared memory — correction from February 2026

The memory ratio is **$m/m'$**, not a processor ratio. Simulating $m$ shared cells with $m'<m$ gives the lecture bound $O(t\lceil m/m'\rceil)$ with $\max(p,m')$ processors; the remaining virtual state stays in local storage. This is an upper bound, not an exact slowdown. A simulation exploiting a small working set may save transfers; the bound alone does not prove random access is always slower. [Proof and storage assumptions](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).

## Parallel performance and scaling

**41 reviewed questions.** Most repeated: scaling and the Amdahl/Gustafson laws (**22 questions**, including the matrix-vector example). Full theory: [[PRAM#Performance quantities|Performance quantities]]; [[PRAM#Strong and weak scaling|Scaling]].

### Speedup and linear scaling — corrected calculation

**$S_p=T^*/T_p$** compares sequential and parallel time for the same problem and input; it is a factor, not a percentage. Under the course's ideal comparison, $S_p\le p$, with equality when $T_p=T^*/p$. Serial work, imbalance and overhead can prevent equality. **$n^3/(n^3/p)=p$, not $1/p$**; that calculation uses the $T_1$ baseline unless $T^*=T_1$ is established.

### Efficiency and the baseline trap

The course defines **$E_p=T_1/(pT_p)$**, using this parallel algorithm's one-processor runtime. Therefore **$pE_p=S_p$ only when $T_1=T^*$**; generally $pE_p=(T_1/T^*)S_p$. With $T_1=n^3$ and $T_p=n^3/p$, efficiency is 1, but this does not prove the algorithm is sequentially optimal. Keeping processors busy with extra work also does not establish efficiency relative to the best sequential algorithm.

### Cost and unavoidable idling — June 2026

**Cost $C_p=pT_p$ counts allocated processor-time, including idle slots; work counts actual operations**, including bookkeeping. A fixed tree-reduction schedule eventually has too few independent additions to occupy every processor. For eight inputs on four processors, counting additions only: $W=7$, $T_4=3$, $C_4=12$, and $E_4=7/12$. Idling increases cost relative to work without necessarily increasing elapsed runtime when processors are added.

### Work efficiency and extra operations — September 2026

**Work-efficient means $W(n)=O(T^*(n))$**, an asymptotic comparison, not processor utilization. Concrete overhead example: summing $n$ inputs into zero-initialized accumulators uses $n$ additions sequentially, but $n+p-1$ with $p$ nonempty chunks followed by merging. The extra $p-1$ additions are implementation-dependent and can be avoided; for $p\le n$, this version still does $O(n)$ work. A tree reduction does not inherently require extra arithmetic.

### Matrix-vector scaling — June 2025

For **$y=Ax$**, different output rows are independent. A row-based schedule for an $r\times c$ matrix takes $\Theta(c\lceil r/p\rceil)$ time. Strong scaling keeps the matrix and vector fixed while increasing $p$, with row parallelism exhausted at $p=r$. For weak scaling, keep $c$ and rows per processor fixed while growing total rows proportionally to $p$; ideal runtime stays constant. Real memory bandwidth can limit both.

### Bounded processors and do-all computations

Use the virtual-processor batching described in section 1. For **$n$ independent, equal-cost iterations** on $p$ physical processors, ideal time is $\lceil n/p\rceil$ iteration rounds and speedup is $n/\lceil n/p\rceil$, approaching $p$ with enough evenly divisible work. Eight iterations on three processors give speedup $8/3$, not 3: the last batch is incomplete. Extra virtual processors do not add physical throughput.

### Strong versus weak scaling — most asked; September 2026

**Strong scaling fixes total workload** and asks whether more processors reduce runtime, ideally toward $T_1/p$; it relates to Amdahl. **Weak scaling fixes work per processor**, increasing total work with $p$; it relates to Gustafson. Approximately constant runtime is the desired outcome, not an automatic assumption of the measurement. When work is proportional to input size, weak-scaling efficiency is $E_{\mathrm{weak}}=T_1(n_0)/T_p(pn_0)$.

### Amdahl: fixed size and diminishing returns

**$S_A(p)=1/(s_A+(1-s_A)/p)$**, where $s_A$ is the serial fraction of the **sequential runtime**. The workload stays fixed: only the parallel part's elapsed time shrinks as processors increase. For $s_A>0$, the unchanged serial duration creates a speedup ceiling of $1/s_A$; $s_A=0$ gives ideal linear speedup. This is a fixed-size model, not a fixed-time model, and additional overhead can reduce actual gains.

### Gustafson: fixed time and larger workloads — January 2026

**$S_G(p)=s_G+p(1-s_G)$**, where $s_G$ is the serial fraction of the **parallel runtime**. Grow parallel work within a fixed time budget; one processor would take $p$ times as long for that parallel work. The comparison uses the same scaled workload. Normalizing parallel time to 1 only chooses units. With a small, stable $s_G$, large systems can process proportionally larger problems in similar time, assuming manageable overhead.

### Why the laws are compatible — June 2026

**Gustafson does not prove Amdahl wrong.** Amdahl fixes problem size; Gustafson grows the parallel workload within a fixed time budget. Their serial fractions use different denominators: sequential versus parallel runtime. For the same execution, using the corresponding fractions gives the same speedup. Both laws assume ideal division of parallel work without additional overhead; neither guarantees that a real application scales well.

### Near-linear speedup does not identify the law — February 2026 correction

**Check what stays fixed before choosing a model.** Near-linear speedup can fit Amdahl when the serial fraction is tiny: $s_A=0.001$ gives $S_A(8)\approx7.94$. It can also fit Gustafson for a growing workload with a small parallel-run serial fraction. The observed curve alone is insufficient evidence; identify whether total workload is fixed or grows with processor count, and how speedup was measured.

## PRAM algorithms

**9 reviewed questions.** Most repeated: prefix scan and its comparison with reduction (**4 questions**). Latest: vector-sum memory accesses, September 2026. Full theory: [[PRAM]].

### Matrix-vector multiplication — corrected complexity

Use [[#Matrix-vector scaling — June 2025|section 2's row decomposition]]: an $n\times n$ matrix has $n$ output rows, each requiring an $n$-term dot product. For $1\le p\le n$, **$T_p=\Theta(n\lceil n/p\rceil)$ and $W=\Theta(n^2)$**; $p=n$ gives $\Theta(n)$ time. Your $n/p$ estimate omitted the work inside each row. Shared vector reads and distinct output writes make this schedule CREW.

### Matrix-matrix multiplication — corrected complexity

Classical multiplication computes **$C_{ij}=\sum_k A_{ik}B_{kj}$**: $n^2$ output tasks, each with an $n$-term dot product, so **$W=\Theta(n^3)$**. Distribute outputs over $p\le n^2$ processors using private accumulators and sequential inner loops: $T_p=\Theta(n\lceil n^2/p\rceil)$. Thus $p=n$ gives $\Theta(n^2)$ time; $p=n^2$ gives $\Theta(n)$. Reused inputs require CREW in this schedule. A dot product is not one primitive operation; parallelizing it requires a further reduction.

### Tree reduction and chunking — January 2026

A tree sum combines disjoint pairs until one total remains: **$n-1$ additions and $\Theta(\log n)$ depth**. For power-of-two $n$, the first level needs $n/2$ processors. With $1\le p\le n$, first sum chunks locally, then reduce the **$p$ partial sums**: $T_p=\Theta(n/p+\log p)$, $W=\Theta(n)$, and allocated cost $\Theta(n+p\log p)$. The final tree has $\log p$ levels, rather than $\log n$.

### Vector-sum memory accesses — September 2026 correction

**Identify the operation and schedule before choosing a memory policy.** A properly staged tree reduction is EREW: processors read disjoint pairs and write distinct next-level cells. Elementwise vector addition is also naturally EREW with disjoint index assignments. The lecture's broadcast prefix scan instead uses CREW because several processors read one block total. Saying accesses take unit time does not identify their read/write policy.

### Prefix scan and its access pattern — most repeated; November 2025

**Scan returns every prefix**, not just the total. The lecture merges equal-sized blocks, adding the left block's total to every right-block prefix, then doubles block size: $[3,1,4,2]\rightarrow[3,4,4,6]\rightarrow[3,4,8,10]$. Right-block processors concurrently read the same total and write distinct outputs: **CREW**. Read the preceding stage's values, using separate buffers. This broadcast trace differs from the note's offset-doubling trace; do not mix them.

### Scan versus reduction: what “more efficient” means

Parallel scan shortens sequential accumulation's linear dependency chain, but **scan and tree reduction can both take $\Theta(\log n)$ time** and produce different outputs. The simple broadcast scan does $\Theta(n\log n)$ work for all prefixes; reduction does $\Theta(n)$ for one total. Busier processors do not prove better efficiency. An alternative up-sweep/down-sweep scan achieves $\Theta(n)$ work and logarithmic depth, including on EREW, so the extra-work trade-off is implementation-specific.

## Divide and conquer and recurrences

**19 reviewed questions.** Most repeated: the Master theorem and its applications (**9 explicit prompts**). Recent repeats: powering, June 2026; Strassen, June 2026; a divide-and-conquer example, September 2026. Full theory: [[Divide and Conquer]]; [[Algorithm as recipes#Master theorem|Master theorem]].

### Divide, conquer, combine — September 2026

**Divide into smaller instances, solve them recursively down to base cases, then combine their answers.** Merge sort illustrates all three: split the array, recursively sort both halves, then merge the **already sorted** halves in linear time. Splitting and immediately merging unsorted halves is insufficient. Its sequential recurrence is $T(n)=2T(n/2)+\Theta(n)$; Master Case 2 gives $\Theta(n\log n)$.

### Building the recurrence and checking Master assumptions

For sequential time, **$T(n)=aT(n/b)+f(n)$** counts $a$ actual recursive calls on equally reduced sizes; $f(n)$ is nonrecursive divide/combine work and need not be constant. The standard theorem requires fixed $a\ge1$, $b>1$, eventually positive $f(n)$, constant-size base cases, and a valid case below. Ordinary rounding is allowed. Unequal splits or a failed case require another method, such as a recursion tree or substitution.

### Master theorem: the three cases — corrected conditions

Put **$d=\log_b a$**. **Case 1:** $f(n)=O(n^{d-\varepsilon})$ gives $T(n)=\Theta(n^d)$. **Case 2:** $f(n)=\Theta(n^d\log^k n)$ gives $\Theta(n^d\log^{k+1}n)$ for constant $k\ge0$. **Case 3:** $f(n)=\Omega(n^{d+\varepsilon})$ gives $\Theta(f(n))$ provided $af(n/b)\le cf(n)$ eventually. Here $\varepsilon>0$ and $0<c<1$ are constants. The outer cases require a **polynomial gap**; merely smaller/larger is insufficient, and Case 3 needs regularity.

### Binary search: one recursive call

Binary search needs a **sorted array** and follows only one half. With index bounds, worst-case $T(n)=T(n/2)+\Theta(1)$ has $a=1$, $b=2$, $d=0$: Master Case 2 gives $\Theta(\log n)$. The best case is constant when the first midpoint matches. Copying subarrays would add work and change this recurrence.

### Exponentiation by squaring — June 2026

For $x^n$, return 1 at $n=0$; otherwise compute **$y=x^{\lfloor n/2\rfloor}$ once**, then return $y^2$ if even or $xy^2$ if odd. The odd half-exponent is **$(n-1)/2$, not $n-1/2$**. Thus $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$ gives $\Theta(\log n)$ by Master Case 2 under unit-cost arithmetic. Computing both equal half-powers separately instead gives $2T(n/2)+\Theta(1)=\Theta(n)$. Exact large-integer bit complexity needs separate analysis.

### Auxiliary space — the missing distinction

**Analyze peak live storage separately from time.** Ordinary recursive powering and index-based binary search have $\Theta(\log n)$ nested constant-size frames; iterative versions use $\Theta(1)$ auxiliary words. These exclude input/output storage and assume the word model. Sequential sibling calls may reuse memory, so do not automatically sum their space costs. The Master theorem can solve a space recurrence only after that recurrence is correctly derived.

### Ordinary block multiplication versus Strassen — June 2026

Split each matrix into four quadrants. Classical multiplication uses **eight** half-size products: $T(n)=8T(n/2)+\Theta(n^2)=\Theta(n^3)$. Strassen uses **seven** chosen products of block sums/differences, then reconstructs the output: $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$. Both use Master Case 1. **$\log_2 7\approx2.80735$; $O(n^{2.8})$ is too small.** The saving repeats at every recursive level; extra additions and storage can outweigh it for small matrices.

### Geometric spatial complexity: H-tree

The theorem can analyze geometry as well as runtime. For the lecture's H-tree, **side length** satisfies $L(n)=2L(n/4)+\Theta(1)$, giving $L(n)=\Theta(\sqrt n)$ by Master Case 1. **Area is $L(n)^2=\Theta(n)$**, not $\Theta(\sqrt n)$. The coefficient 2 measures growth along one side, even though the construction contains four quarter-sized subtrees. Identify the resource before writing its recurrence.

## Randomized algorithm classes

**9 reviewed questions.** Most repeated: Las Vegas versus Monte Carlo, including efficiency and examples (**7 questions**). Latest: exact randomized data structures, September 2026. Full theory: [[Randomized Algorithms]]; [[Randomized Data Structures#Treaps: a search tree and a priority heap|Treaps]].

### Las Vegas versus Monte Carlo — most repeated

**Las Vegas preserves correctness; randomness affects runtime. Monte Carlo bounds worst-case runtime but permits quantified error or failure.** Las Vegas does not require an unbounded worst case: randomized quicksort is always correct and has a finite quadratic worst case. Conversely, a repeat-until-hit search can have arbitrarily long runs. A Monte Carlo time bound depends on input size and parameters, rather than being one constant for all inputs.

### Efficiency: expected versus worst-case — June 2026

Efficient **Las Vegas** means polynomial expected runtime for **every fixed input**, averaging over the algorithm's internal randomness, not a favorable input distribution. Finite expectation implies termination with probability one, but expected time is not a deadline. Efficient **Monte Carlo** means polynomial worst-case time **with a useful error guarantee**; include any repetitions needed to achieve that guarantee in the time budget. Bounded time alone is insufficient.

### Finding an a — January 2026

Assume half the array entries are `a`, with **independent uniform sampling with replacement**. Las Vegas samples until finding an `a`, returns its checked index, and needs **2 trials in expectation**, with no finite deterministic trial limit. Monte Carlo stops after at most 20 trials: its failure probability is **$2^{-20}$**, and any returned index is valid. `FAIL` means the search missed a witness; it does not prove absence.

### Sampling promises and failure probability

For target fraction **$q>0$**, repeat-until-hit needs $1/q$ trials in expectation, while failure after $k$ independent samples has probability **$(1-q)^k$**. If $q=0$, the unbounded search never succeeds. With just one target among $n$ entries, 20 trials become unreliable as $n$ grows. For $q=1/2$, failure at most $\delta$ needs $k\ge\lceil\log_2(1/\delta)\rceil$. Rereading one sampled index does not provide independent repetition.

### Randomized data structures with exact answers — September 2026

**True: randomness can improve shape while invariants preserve correctness.** A treap maintains BST key order and min-heap order on independent uniform random priorities; rotations preserve key order. For fixed operation sequences independent of priorities, search, insertion and deletion cost $O(\log n)$ in expectation, but $O(n)$ in the worst case. Keys $1,2,3$ with priorities $3,1,2$ give root 2 with children 1 and 3. Random input order and perfect balance are not required.

## Minimum cut

*Pending — bank section 06, AAPP-06-001–AAPP-06-012 (12 questions).* Theory: [[Minimum Cut]].

## Sorting and partitioning

*Pending — bank section 07, AAPP-07-001–AAPP-07-020 (20 questions).* Theory: [[Sorting]].

## Selection and order statistics

*Pending — bank section 08, AAPP-08-001–AAPP-08-012 (12 questions).* Theory: [[Selection and Order Statistics]].

## Primality testing

*Pending — bank section 09, AAPP-09-001–AAPP-09-007 (7 questions).* Theory: [[Primality Testing and Cryptosystems]].

## Dynamic programming and LCS

*Pending — bank section 10, AAPP-10-001–AAPP-10-019 (19 questions).* Theory: [[Dynamic Programming and LCS]].

## BDDs and memoization

*Pending — bank section 11, AAPP-11-001–AAPP-11-012 (12 questions).* Theory: [[Binary Decision Diagrams]]; [[Dynamic Programming and LCS#Memoization: solve each requested state once|LCS memoization]].

## Treaps

*Pending — bank section 12, AAPP-12-001–AAPP-12-019 (19 questions).* Theory: [[Randomized Data Structures#Treaps: a search tree and a priority heap|Randomized Data Structures — treaps]].

## Skip lists

*Pending — bank section 13, AAPP-13-001–AAPP-13-009 (9 questions).* Theory: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list|Randomized Data Structures — skip lists]].

## Disjoint sets

*Pending — bank section 14, AAPP-14-001–AAPP-14-002 (2 questions).* No dedicated theory note is currently linked in the bank.

## Amortized analysis

*Pending — bank section 15, AAPP-15-001–AAPP-15-019 (19 questions).* Theory: [[Amortized Analysis]].

## Online algorithms and competitive analysis

*Pending — bank section 16, AAPP-16-001–AAPP-16-015 (15 questions).* Theory: [[Competitive Analysis]].

## Parallel design and architectures

*Pending — bank section 17, AAPP-17-001–AAPP-17-016 (16 questions).* Bank study context: [[Course Introduction]]; this is not a dedicated treatment of all historical questions.

## Dependences and loop parallelization

*Pending — bank section 18, AAPP-18-001–AAPP-18-042 (42 questions).* No dedicated theory note is currently linked in the bank.

## Parallel patterns

*Pending — bank section 19, AAPP-19-001–AAPP-19-065 (65 questions).* Related theory: [[PRAM]] covers introductory patterns; further material will be needed for some questions.

## Task graphs and OpenMP implementations

*Pending — bank section 20, AAPP-20-001–AAPP-20-013 (13 questions).* No dedicated theory note is currently linked in the bank.

## OpenMP

*Pending — bank section 21, AAPP-21-001–AAPP-21-055 (55 questions).* No dedicated theory note is currently linked in the bank.

## Pthreads and shared-memory synchronization

*Pending — bank section 22, AAPP-22-001–AAPP-22-018 (18 questions).* No dedicated theory note is currently linked in the bank.

## MPI

*Pending — bank section 23, AAPP-23-001–AAPP-23-070 (70 questions).* No dedicated theory note is currently linked in the bank.

## CUDA

*Pending — bank section 24, AAPP-24-001–AAPP-24-008 (8 historical questions).* No dedicated theory note is currently linked in the bank. [[AAPP Index]] records that the supplied current course introduction excludes CUDA; keep this section to preserve the bank correspondence.

## Halide and high-level synthesis

*Pending — bank section 25, AAPP-25-001–AAPP-25-005 (5 questions).* No dedicated theory note is currently linked in the bank.
