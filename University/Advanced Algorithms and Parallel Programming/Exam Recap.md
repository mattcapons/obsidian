---
tags:
  - aapp
  - exam-recap
status: complete
created: 2026-10-30
updated: 2026-11-02
question-bank: "[[Past Exam Question Bank]]"
completed-sections:
  - 01 — PRAM model and memory rules
  - 02 — Parallel performance and scaling
  - 03 — PRAM algorithms
  - 04 — Divide and conquer and recurrences
  - 05 — Randomized algorithm classes
  - 06 — Minimum cut
  - 07 — Sorting and partitioning
  - 08 — Selection and order statistics
  - 09 — Primality testing
  - 10 — Dynamic programming and LCS
  - 11 — BDDs and memoization
  - 12 — Treaps
  - 13 — Skip lists
  - 14 — Disjoint sets
  - 15 — Amortized analysis
  - 16 — Online algorithms and competitive analysis
  - 17 — Parallel design and architectures
  - 18 — Dependences and loop parallelization
  - 19 — Parallel patterns
  - 20 — Task graphs and OpenMP implementations
  - 21 — OpenMP
  - 22 — Pthreads and shared-memory synchronization
  - 23 — MPI
  - 24 — CUDA
  - 25 — Halide and high-level synthesis
---
# AAPP — Exam Recap

[[AAPP Index|Course index]] · [[Past Exam Question Bank|Question bank]]

Quick reminders for **all 25 sections and 552 questions**. Prioritize frequent topics, recent exams and important corrections. Sections 1–5 draw on reviewed attempts; sections 6–25 now also use the supplied model answers, including questions you have not attempted. Recap coverage is separate from your study progress.

**Topic index**

1. [[#PRAM model and memory rules|PRAM: model and memory rules]]
2. [[#Parallel performance and scaling|Parallel performance and scaling]]
3. [[#PRAM algorithms|PRAM algorithms]]
4. [[#Divide and conquer and recurrences|Divide and conquer and recurrences]]
5. [[#Randomized algorithm classes|Randomized algorithms]]
6. [[#Minimum cut|Minimum cut]]
7. [[#Sorting and partitioning|Sorting and partitioning]]
8. [[#Selection and order statistics|Selection and order statistics]]
9. [[#Primality testing|Primality testing]]
10. [[#Dynamic programming and LCS|Dynamic programming and LCS]]
11. [[#BDDs and memoization|BDDs and memoization]]
12. [[#Treaps|Treaps]]
13. [[#Skip lists|Skip lists]]
14. [[#Disjoint sets|Disjoint sets]]
15. [[#Amortized analysis|Amortized analysis]]
16. [[#Online algorithms and competitive analysis|Online algorithms and competitive analysis]]
17. [[#Parallel design and architectures|Parallel design and architectures]]
18. [[#Dependences and loop parallelization|Dependences and loop parallelization]]
19. [[#Parallel patterns|Parallel patterns]]
20. [[#Task graphs and OpenMP implementations|Task graphs and OpenMP implementations]]
21. [[#OpenMP|OpenMP]]
22. [[#Pthreads and shared-memory synchronization|Pthreads and shared-memory synchronization]]
23. [[#MPI|MPI]]
24. [[#CUDA|CUDA]]
25. [[#Halide and high-level synthesis|Halide and high-level synthesis]]

%%
Future updates: keep one short paragraph per topic, normally 40–80 words. Assume the theory is already known. Preserve course-note topic order and all 25 main sections. Keep only essential definitions, formulas, examples and corrections; omit derivations, quizzes and repeated explanations. Revise from available model answers or reviewed attempts, preserve user additions, and update completed-sections and the date. Recap completion does not mean the student has attempted every question. Do not change the question bank while maintaining this recap.
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
Sections 06–25 completed from the supplied model answers on 2026-11-02; 438 question entries. These are reference-answer summaries, not claims that attempts were reviewed.
Section 06 — Minimum cut: AAPP-06-001–AAPP-06-012; 12 reference-answer questions; latest exam 2026-06-29.
Section 07 — Sorting and partitioning: AAPP-07-001–AAPP-07-020; 20 reference-answer questions; latest exam 2026-09-10.
Section 08 — Selection and order statistics: AAPP-08-001–AAPP-08-012; 12 reference-answer questions; latest exam 2026-06-29.
Section 09 — Primality testing: AAPP-09-001–AAPP-09-007; 7 reference-answer questions; latest exam 2026-09-10.
Section 10 — Dynamic programming and LCS: AAPP-10-001–AAPP-10-019; 19 reference-answer questions; latest exam 2026-09-10.
Section 11 — BDDs and memoization: AAPP-11-001–AAPP-11-012; 12 reference-answer questions; latest exam 2026-06-29.
Section 12 — Treaps: AAPP-12-001–AAPP-12-019; 19 reference-answer questions; latest exam 2026-06-29.
Section 13 — Skip lists: AAPP-13-001–AAPP-13-009; 9 reference-answer questions; latest exam 2026-02-09.
Section 14 — Disjoint sets: AAPP-14-001–AAPP-14-002; 2 reference-answer questions; latest exam 2023-09-11.
Section 15 — Amortized analysis: AAPP-15-001–AAPP-15-019; 19 reference-answer questions; latest exam 2026-09-10.
Section 16 — Online algorithms and competitive analysis: AAPP-16-001–AAPP-16-015; 15 reference-answer questions; latest exam 2026-06-29.
Section 17 — Parallel design and architectures: AAPP-17-001–AAPP-17-016; 16 reference-answer questions; latest exam 2026-06-11.
Section 18 — Dependences and loop parallelization: AAPP-18-001–AAPP-18-042; 42 reference-answer questions; latest exam 2026-09-10.
Section 19 — Parallel patterns: AAPP-19-001–AAPP-19-065; 65 reference-answer questions; latest exam 2026-09-10.
Section 20 — Task graphs and OpenMP implementations: AAPP-20-001–AAPP-20-013; 13 reference-answer questions; latest exam 2026-09-10.
Section 21 — OpenMP: AAPP-21-001–AAPP-21-055; 55 reference-answer questions; latest exam 2026-09-10.
Section 22 — Pthreads and shared-memory synchronization: AAPP-22-001–AAPP-22-018; 18 reference-answer questions; latest exam 2025-02-14.
Section 23 — MPI: AAPP-23-001–AAPP-23-070; 70 reference-answer questions; latest exam 2026-09-10.
Section 24 — CUDA: AAPP-24-001–AAPP-24-008; 8 reference-answer questions; latest exam 2022-06-30.
Section 25 — Halide and high-level synthesis: AAPP-25-001–AAPP-25-005; 5 reference-answer questions; latest exam 2025-07-04.
Coverage audit: consolidate identical reference answers, check every distinct answer and question topic, and preserve course-note order where dedicated theory exists. Use the bank and primary technical documentation for remaining parallel topics. Corrected topic mismatches in recap: AAPP-19-002 asks Scan although its supplied model describes Workpile; AAPP-19-003 asks Workpile although its model describes Fork-Join. AAPP-23-028 is an OpenMP scoping question retained under MPI. No bank text was changed.
Source boundary: existing course notes were used, including the new Competitive Analysis note; the attached sorting PDF was not freshly extracted because no PDF extraction utility/library was available. Selected primary sources checked: OpenMP cancellation/firstprivate, MPI nonblocking/thread semantics, POSIX condition wait, Foster PCAM, NVIDIA CUDA, Halide and AMD HLS. Preserve historical CUDA questions without inferring current exam inclusion.
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

**12 questions.** Karger–Stein and equal-confidence comparisons dominate; latest repeat: June 2026. Theory: [[Minimum Cut]].

### Random contraction and the cut invariant

Karger repeatedly samples a **uniform random edge copy** and merges its endpoints until two supernodes remain. Preserve parallel-edge multiplicities, remove self-loops, and track original vertex memberships. The final partition is a valid cut. Contracting an edge across a particular minimum cut destroys that optimum; avoiding all its edges preserves it. Both contraction algorithms are **Monte Carlo**: checking cut feasibility does not certify minimality.

### Success probability and independent repetition — February 2026

For a fixed minimum cut, survival with $r$ supernodes is at least $1-2/r$ conditional on earlier survival. Multiplying gives **success at least $p_0=2/[n(n-1)]$**, not necessarily equality. After $R$ fresh independent runs, retaining the smallest cut gives failure at most $(1-p_0)^R\le e^{-p_0R}$. Thus $R\ge\ln(1/\delta)/p_0$ suffices. Reusing the same randomness or observing repeated cut values does not establish correctness.

### Karger–Stein: stop early and branch — most repeated

On **two independent copies**, contract to $t=\lceil1+n/\sqrt2\rceil$ supernodes, recursively solve both, and return the smaller lifted cut. Branching repeats at **every** recursive level; it does not simply finish each branch with ordinary Karger. Use exact enumeration for $n\le6$ so rounding still permits progress. Partial contraction preserves a chosen optimum with probability at least $1/2$, but recursive success must also be counted.

### One run versus amplified complexity — June 2026

In the lecture's quadratic contraction model, basic Karger costs **$O(n^2)$ per run** and $O(n^4\log n)$ for failure at most $n^{-c}$. Karger–Stein satisfies $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$ per recursive run, succeeds with probability $\Omega(1/\log n)$, and needs $O(\log^2 n)$ full runs for that confidence: **$O(n^2\log^3 n)$ total**. Its advantage is the success/time trade-off, not a cheaper individual run.

## Sorting and partitioning

**20 questions.** Most repeated: counting/radix sort (8) and comparison lower bounds (6). Recent focus: randomized expectation and stability, September 2026. Theory: [[Sorting]].

### Partition: separation, not sorting

Lomuto partition scans once, maintaining a region of keys at most the pivot, an examined greater-key region, and an unexamined region; the final swap puts the pivot at its rank. It costs **$\Theta(n)$ time and $O(1)$ auxiliary space**, and is normally unstable. Choose a uniform pivot and swap it into the designated position to randomize. Hoare returns a split boundary instead; match recursion bounds to the variant. Three-way partition handles duplicates.

### Quicksort's recursion and randomized guarantee

Balanced or fixed-ratio splits give **$\Theta(n\log n)$**; repeatedly extreme pivots give $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$. Randomized quicksort is Las Vegas: it stays correct and has expected $\Theta(n\log n)$ time on every fixed distinct-key input, but the quadratic worst case remains possible. Two-way partitioning can still handle equal keys badly; three-way partitioning addresses that separate issue. A recursion stack is additional space beyond partition's constant workspace.

### Expected-time recurrence — September 2026

A uniform pivot makes each rank equally likely, and **both** subarrays are sorted: $E_n=\frac2n\sum_{k=0}^{n-1}E_k+\Theta(n)$. Solving yields $\Theta(n\log n)$; expected pivot comparisons are $2(n+1)H_n-4n$. The expectation is over internal pivot choices, not assumed random inputs. Do not replace the random recursion with an assertion that every pivot splits exactly in half.

### Why comparison sorting needs $\Omega(n\log n)$

For distinct keys, a comparison decision tree must distinguish **$n!$ orders**. A height-$h$ binary tree has at most $2^h$ leaves, so $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. Merge sort and heapsort attain this worst-case order. The theorem does not force every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices.

### Counting sort and stable placement — most repeated

Count keys, prefix-sum their frequencies into output positions, then place records in a separate array. With $n$ records and $k$ possible keys, **time and auxiliary space are $\Theta(n+k)$**. Stability preserves the relative order of records with equal keys; using cumulative end positions, scan input right-to-left and decrement the corresponding position. Linear time needs $k=O(n)$ in this model. Parallel histogram updates need explicit collision handling.

### LSD radix sort: why stability matters — September 2026

Sort digits **from least to most significant**, using a stable digit sorter. Equal current digits must retain the order established by lower digits; an unstable pass can destroy it. Counting sort provides an appropriate pass when the digit range is modest. For $d$ digits and $k$ values per digit, time is **$\Theta(d(n+k))$**. Include the digit count and range rather than calling radix sort unconditionally linear.

## Selection and order statistics

**12 questions.** Pivot choice and expected versus worst-case linear time recur through June 2026. Theory: [[Selection and Order Statistics]].

### Quickselect and rank updates

Partition around a uniform random pivot into $L<x$, $E=x$, and $G>x$. For desired 1-based rank $i$, recurse into $L$ if $i\le|L|$; return the pivot if $i\le|L|+|E|$; otherwise recurse into $G$ with **$i-|L|-|E|$**. Only one side is solved. Correctness is exact: **Las Vegas**, expected $\Theta(n)$ time, worst-case $\Theta(n^2)$. Three-way partition handles duplicate keys without confusing their rank interval.

### Deterministic SELECT: median of medians

Group elements into fives, find each small group's median, recursively select the median of those medians, then partition the **whole original input** around it. Retain leftover elements in that partition. At least $3n/10-O(1)$ elements are certified on either inclusive side, limiting the remaining rank-search side to $7n/10+O(1)$. This is a pivot-quality guarantee, not a requirement to sort the entire input.

### Why the worst case is linear — February/June 2026

Charge pivot selection too: **$T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$**. The recursive fractions sum to less than one, leaving room for linear grouping/partition work; use substitution rather than the standard equal-size Master theorem. Groups of three lack this slack in the simple proof. Five is sufficient, not uniquely necessary. Randomized and deterministic versions share the rank logic but provide different worst-case guarantees.

## Primality testing

**7 questions.** All revisit the randomized test and its classification, most recently September 2026. Theory: [[Primality Testing and Cryptosystems]].

### Random witnesses and repeated squaring

The lecture strengthens Fermat testing by checking modular powers and **nontrivial square roots of 1**, which certify compositeness. In standard Miller–Rabin form, write $n-1=2^s d$ with odd $d$, sample a fresh uniform base in $[2,n-2]$, compute $a^d\bmod n$, then square repeatedly. Pass when the initial value is 1 or a tested value is $-1\bmod n$; otherwise reject. Handle small numbers and even candidates separately.

### One-sided Monte Carlo: what is certain

**COMPOSITE is certain; POSSIBLY-PRIME is not a proof.** A prime always passes, while a fixed odd composite passes $k$ independent standard rounds with probability at most **$4^{-k}$**. This is one-sided Monte Carlo, not Las Vegas. The bound conditions on a composite input; it is not automatically the probability that an arbitrary passing candidate is composite. Plain Fermat testing alone can be fooled by pseudoprimes and Carmichael numbers.

### Reliability and the cost model

For error at most $\delta$, choose **$k\ge\lceil\log_4(1/\delta)\rceil$** fresh independent rounds. Repeating the same base gives no independent amplification. Each round uses $O(\log n)$ modular multiplications through repeated squaring. Input length is $\Theta(\log n)$ bits, so include arithmetic bit costs when claiming bit complexity. Use the standard base domain and one-quarter error bound; the notes flag an inconsistent base-count claim in the slides.

## Dynamic programming and LCS

**19 questions.** LCS tables, space, and memoization dominate; latest memoization question: September 2026. Theory: [[Dynamic Programming and LCS]].

### Dynamic programming and memoization

Identify **overlapping states, base cases and a correct dependency recurrence**; optimization also needs optimal substructure. Memoization caches top-down calls; tabulation evaluates states in dependency order. LCS branches on prefix pairs, and both $(m-1,n)$ and $(m,n-1)$ can request $(m-1,n-1)$. Cache the complete pair; UNSEEN must differ from the valid result 0. Time counts reached states and transitions. Adding a cache to independent subproblems provides no automatic saving.

### LCS state and recurrence

Let **$C[i,j]$ be the LCS length of prefixes** $X[1..i]$ and $Y[1..j]$, with $C[i,0]=C[0,j]=0$. If final symbols match, use $1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill increasing prefix lengths or memoize recursive calls. A subsequence preserves relative order but need not be contiguous. The $mn$ constant-cost states give **$\Theta(mn)$ time**, replacing potentially exponential uncached branching.

### Space and reconstructing an actual subsequence

The full table uses **$\Theta(mn)$ space** and supports backward reconstruction through matches and maximizing predecessors in $O(m+n)$ additional time. If only the length is required, two rows reduce workspace to **$O(\min(m,n))$**, preserving $\Theta(mn)$ time. Discarding rows also discards ordinary traceback information; obtaining a witness in linear space needs a separate method such as Hirschberg. A polynomial state count can still exceed practical memory capacity.

## BDDs and memoization

**12 questions.** Unique versus computed tables is the central recurring distinction, including June 2026. Theory: [[Binary Decision Diagrams]].

### Unique table: representation and canonicity

A reduced ordered BDD uses a fixed variable order, eliminates equal-child tests, and shares identical nodes. The **unique table** maps $(variable,high,low)$ to one node/handle. Together these rules provide canonicity for the fixed order. Hash collisions require full-key comparison. Interning the same output node does **not** avoid work spent repeatedly computing its operands; compact representation and efficient operations are separate guarantees.

### Computed table: the dynamic-programming part

The **computed table** caches operation states, such as $(ITE,f,g,h)\mapsto result$, to avoid recomputing shared subproblems. This is memoization, unlike structural sharing in the unique table. Cache eviction can cause recomputation without changing mathematical answers; it does not destroy canonicity. With only the unique table, a compact DAG can still be revisited along exponentially many assignment paths. Count operand states, not just result nodes.

### ITE recursion and its bound

First handle terminals and cache hits. Choose the **earliest variable among all operands**, recurse on its high and low cofactors, then make/reuse a reduced node and cache the result. An operand independent of that variable stays unchanged. With full cache retention and expected constant-time hashing, ITE visits at most $N_fN_gN_h$ states; binary Apply has an $O(N_fN_g)$ bound. These are diagram-size bounds, not polynomial guarantees in the number of Boolean variables.

## Treaps

**19 questions.** Split and ordered join dominate; recent priorities/split/join questions run through June 2026. Theory: [[Randomized Data Structures]].

### Invariants, random priorities and exact search

A treap is a **BST on keys and min-heap on priorities**. Distinct independent random priorities with uniform relative order randomize shape without requiring random key arrival. Search uses ordinary key comparisons and remains exact. Continuous priorities are distinct almost surely; finite bit strings need a consistent tie mechanism, such as extending and storing extra random bits. Do not resample a node's priority at each comparison.

### Expected paths versus rotation counts

Under the standard fixed-operation-sequence assumptions, search and updates cost **$O(\log n)$ expected**, with an $O(n)$ possible chain. Insert as a BST leaf, then rotate upward to repair heap order; rotations preserve in-order key order. Ordinary insertion/deletion needs fewer than two rotations in expectation, but finding the position still costs logarithmic expected time. Searches perform no rotations. Expected balance does not guarantee a balanced shape on every run.

### Split, including an existing boundary key — June 2026

Split at $k$ returns **keys $\le k$ and keys $>k$**. Recursively follow the search path, reconnecting the appropriate boundary child; expected time is $O(\log n)$, worst case $O(n)$. The lecture instead promotes a $-\infty$-priority dummy separator and detaches its children. If $k$ already exists, preserve its record in the first output. Direct recursion avoids artificial separator keys and this special-case bookkeeping.

### Union means ordered join — most repeated

The lecture assumes **every key in $L$ is smaller than every key in $R$**. Choose the smaller-priority root and recursively join its boundary child with the other tree. Expected cost is $O(\log(n_L+n_R))$, worst case linear. This is not unrestricted overlapping set union. A dummy-root construction can implement the same operation, but its forced priority does not satisfy the random-priority assumptions behind the ordinary constant-expected-rotation bound.

## Skip lists

**9 questions.** Search and insertion recur most often; latest insertion question: February 2026. Theory: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list|Skip lists]].

### Search, randomness and complexity

The bottom sorted list contains every key; upper levels provide shortcuts. Start at the top, move right while the next key is below the target, then descend and check equality at the bottom. Independent geometric heights give **$O(\log n)$ expected search/update time and $O(n)$ expected pointer storage**. Answers remain exact. Worst-case paths can be linear with customary height limits; an uncapped model also depends on the realized tower height.

### Insertion and stored heights

During search, record each level's predecessor. Flip independent coins to choose the new tower height, then splice the node into every level it occupies, extending the header when necessary. Preserve sorted order and the subset relationship between levels. With promotion probability $1/2$, the new node needs a constant expected number of pointers; locating it still costs $O(\log n)$ expected time. Search and deletion do not resample existing heights.

### Union: distinguish merging from concatenation

A general construction **merges the sorted bottom lists**, resolves equal-key records under an explicit policy, then rebuilds random towers. Expected time and storage are $O(n+m)$. Ordered concatenation can instead reconnect boundary pointers, but requires all keys in the first list to precede those in the second. The supplied lecture does not prescribe one unique skip-list union algorithm; state the construction and its preconditions.

## Disjoint sets

**2 questions.** Both ask about forest representation and optimizations. Reference answers are supplied in the bank.

### Parent forests and the two optimizations

**MAKE-SET** creates a singleton root; **FIND** follows parents to a representative; **UNION** links representatives unless they already coincide. Union by rank or size attaches the shallower/smaller tree below the other. **Path compression** redirects FIND's visited nodes toward the root. Representative identities can change, but membership equivalence must remain correct. Rank is a balancing bound, not necessarily the height after compression.

### Amortized, not constant worst-case

Rank/size alone bounds height by $O(\log n)$. Combined with compression, initialization and $m$ operations cost **$O((n+m)\alpha(n))$** with $O(n)$ storage, under the standard union-find model. The inverse-Ackermann factor is a sequence guarantee; it does not say every call has constant worst-case cost. This is amortized analysis, not an expectation over random inputs. [Princeton union-find bounds](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/UF.html).

## Amortized analysis

**19 questions.** Methods, dynamic arrays and potential recur through September 2026. Theory: [[Amortized Analysis]].

### Sequence guarantees and the aggregate method

Amortized analysis bounds the **total cost of every legal operation sequence** from a stated initial state. Rare expensive operations can be paid for by preceding cheap ones; no probability distribution is assumed. Aggregate analysis sums the total cost and divides by the number of operations. This can prove constant amortized cost even when one operation is linear. Do not multiply every operation by an expensive state that cannot occur every time.

### Accounting: saved credit pays later costs

Overcharge cheap operations and retain credit for later expensive ones. The credit balance must stay nonnegative on every relevant prefix. For a doubling array, constant insertion charges save enough to pay for the next copy. The familiar charge 3 counts writes and copies with initialization handled separately. If allocating each slot also costs one, adjust the charge; **exact constants depend on the cost model**.

### Potential and the sign of its change — September 2026

Define **$\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$**. Summing telescopes: $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$. A nonnegative final potential relative to the initial one makes amortized total an upper bound. **Negative $\Delta\Phi$ releases saved credit** and is compatible with nonnegative $\Phi$. For a nonempty doubling array, $\Phi=2s-m$ gives constant amortized insertions under the copies-plus-write model; define the empty initial state separately.

### Dynamic doubling and allocation costs

Copies across resizes form a geometric sum, so **$n$ insertions cost $\Theta(n)$**, despite a $\Theta(n)$ individual resize. If allocating capacity $2m$ costs $2m$, copying costs $m$ and insertion costs 1, a full-capacity resize costs **$3m+1$**, not $m+1$. Total remains linear, but the standard potential/charge constants change. Merely increasing capacity by one would repeatedly copy growing prefixes and lose constant amortized insertion cost.

### Stack MULTIPOP and a counter with RESET

MULTIPOP removes at most the current stack size: each item can be popped only after a push, so any $n$ operations from empty cost $O(n)$. For a binary counter, bit $j$ flips at a geometric frequency, again giving constant amortized increments. RESET must avoid scanning all untouched bits: track the highest written position. Charge initialization separately; a repeated full $k$-bit reset is not automatically constant amortized.

## Online algorithms and competitive analysis

**15 questions.** Move-to-front and comparison with offline OPT recur through June 2026. Theory: [[Competitive Analysis]].

### Online versus offline and the competitive ratio

An **online** algorithm serves requests without knowing the future suffix; offline OPT can plan using the whole sequence. Competitiveness requires **$C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence**, using the same cost model and initial conditions. The startup term cannot grow with sequence length. This compares whole-sequence quality; ordinary runtime analysis still applies. An adversarial sequence is not a random-input distribution.

### Move-to-front: state the paid-swap model

Search the requested item and move it to the front, preserving other items' relative order. In the lecture, rank $r$ costs **$r+(r-1)=2r-1$** because adjacent swaps are paid. A potential of twice the order inversions against OPT proves **4-competitiveness**, plus initial potential if lists start differently. The familiar factor 2 uses a different model with free forward moves. Amortization proves the competitive guarantee; it does not make every access constant-time.

### Future knowledge and the quantifier trap — February 2026

From $[A,B,C]$, requests $C,A,A$ cost MTF $5+3+1=9$, while leaving the list unchanged costs $3+1+1=5$. This shows an advantage over that **specified heuristic**, not over every possible online strategy on one fixed sequence. An online strategy can happen to make the optimal choices on that sequence. The valid adversarial claim chooses a bad sequence for each fixed strategy; one universal defeating sequence is not required.

## Parallel design and architectures

**16 questions.** Recurring topics: hybrid models, useful granularity and PCAM; recent architecture/layout questions: February–June 2026. Reference answers: [[Past Exam Question Bank#Parallel design and architectures|Bank section]].

### Flynn taxonomy and levels of parallelism

**SISD** has one instruction/data stream; **SIMD** applies one instruction across data lanes; **MISD** is multiple instruction streams on one data stream and is uncommon; **MIMD** uses independent instruction streams on different data. CPU vector units provide SIMD, multicore CPUs/clusters MIMD, and GPUs expose SIMT groups. In the shown 256-bit units, one vector holds eight 32-bit floats or four 64-bit values; cores and vector lanes are separate parallelism levels.

### Threads, processes and hybrid programs

Threads share an address space but have separate execution state/stacks; processes normally communicate across separate address spaces. Combine **MPI across nodes, OpenMP within nodes, SIMD within cores**, and device kernels where suitable. Hybrid models are valid when coordination, transfers and oversubscription are controlled. Shared process resources do not guarantee ordered I/O: synchronize complete output records or collect and print them later. Equivalent high-level decompositions can produce similar low-level work without guaranteeing identical machine code.

### Useful parallelism and automatic parallelization

Extracting concurrency is insufficient: control total work, communication, load balance, locality and task overhead. A million tiny tasks can cost more to manage than to compute. Manual design can use domain knowledge unavailable to a compiler; correct automatic parallelization preserves semantics and may conservatively decline uncertain transformations. It is not inherently incorrect, nor is manual work always superior. Aliasing, side effects and irregular dependencies limit what can be inferred safely.

### PCAM and agglomeration — January 2026

**Partitioning → Communication → Agglomeration → Mapping**: identify fine tasks, determine dependencies/data exchange, combine tasks into useful units, then place them to balance work and communication. Agglomeration improves locality and amortizes coordination; too much removes useful concurrency. Tiling pixels is a typical example. Revisit stages as costs become clearer; the goal is suitable granularity, not the smallest possible task count. [Foster's PCAM methodology](https://www.mcs.anl.gov/~itf/dbpp/text/node15.html).

### AoS versus SoA — February 2026

**Array of structures** stores whole records together and suits operations using most fields of one object. **Structure of arrays** stores each field contiguously and suits processing the same field across many objects, often improving SIMD and GPU coalescing. Choose by actual access pattern; blocked mixtures can combine advantages. Shared addressability also does not imply uniform access cost across sockets: placement and NUMA locality still matter.

## Dependences and loop parallelization

**42 questions.** Most frequent: identifying real dependences and choosing a legal loop transformation. Latest: two-dimensional wavefront, September 2026. Reference answers: [[Past Exam Question Bank#Dependences and loop parallelization|Bank section]].

### RAW, WAR and WAW

**RAW/flow** means a consumer needs a value produced by an earlier write. **WAR/anti** means a read must precede an overwrite; **WAW/output** means write order determines the final value. RAW carries data; WAR/WAW arise from storage reuse. Analyze actual addresses with at least one write, not merely variable names. Called functions can hide shared state or I/O dependencies, so visibly separate output elements alone do not prove independence.

### Loop-carried, loop-independent and lexically forward

A loop-independent dependence stays within one iteration; a loop-carried dependence connects different iterations. Identify the carrying loop and distance/direction. A lexically forward edge follows the original iteration-vector order, then statement order within an iteration. A transformed schedule must preserve required producer-to-consumer order. Dependencies do not forbid every parallel design: independent chains, pipelines, wavefronts or an algebraically valid scan may remain possible.

### DOALL and parallel loop conditions

A **DOALL** loop has independent iterations, such as `y[i]=f(x[i])` with disjoint outputs and a pure function. Parallelize outer rows for coarse work; use `collapse(2)` only when the combined iteration space is legal and independent. Same-cell read/update within one iteration is not necessarily a cross-iteration dependence. Independence enables parallel execution, but near-linear speedup also needs sufficient work, balance and bandwidth. Check aliases and valid bounds first.

### Renaming and snapshots: preserve the values read

WAR/WAW conflicts can often be removed by private temporaries, array expansion or reading an immutable old copy, followed by the correct final store. **Renaming alone cannot remove a true RAW chain.** A snapshot is valid only if original reads were meant to see old values. Replacing every read in an in-place recurrence or transposed update with original-array data can change the sequential result. An associative reformulation is a separate algorithmic argument.

### Distance-$d$ recurrences and independent chains — June 2026

For `a[i][j]=f(a[i][j-d])`, parallelize rows and, if useful, the **$d$ column residue classes**, keeping increasing order inside each chain. A recurrence along rows instead permits parallel columns or row residue classes. The first phase must finish required producers before a consuming second phase. More threads cannot remove a genuinely sequential chain with arbitrary `f`; adding `parallel for` or `collapse` does not supply the missing values.

### Wavefront scheduling — September 2026

If a cell needs its upper and left neighbors, **equal-$i+j$ anti-diagonals** are independent after preceding fronts complete. Use a barrier between fronts or tiled tasks depending on upper/left tiles. A valid separating hyperplane makes all dependence edges point to earlier fronts. Subsequent left-to-right row recurrences can run across rows, keeping columns ordered. Tiling improves locality and reduces the cost of many small barriers.

### Fusion, loop order and scheduling overhead

Two phases updating the same index can sometimes fuse as `b[j]=f1(a[j]); a[j]=f2(b[j]);`, preserving per-element order and removing a global barrier. Otherwise retain producer/consumer synchronization. In C row-major arrays, keep the last index contiguous; correctness and locality are different questions. Triangular loops have uneven row costs and may benefit from dynamic/guided scheduling. Avoid a nested thread team for each tiny row; assign coarser blocks instead.

### Reductions, parity and arithmetic equivalence

A scalar `sum += ...` is a reduction even when all array outputs are independent; protect **every contributing phase** and preserve the original initial value. Inspect actual parity: a phase writing even columns may not affect another reading only odd columns. Floating-point reassociation can change rounding, and signed overflow is undefined. A product initialized to **zero** stays zero in defined arithmetic; privatized nonzero partial products can introduce overflow absent from that original execution.

### Literal exam-code pitfalls

Check printed bounds and increments before transforming code. January 2025 includes negative shifted indices unless a halo is specified; **September 2025's `j++` with `j>=0` does not implement a terminating reverse loop**. February 2026's doubled subscripts require enough columns and a stray parenthesis correction; September 2026 has a missing semicolon and mentions a function absent from the snippet. State any correction explicitly instead of inventing valid semantics for invalid C.

## Parallel patterns

**65 questions.** Pack/Split, Gather/Scatter, Scan and Reduce dominate; latest: Scan–Reduce, Pipeline and Pack, September 2026. Reference answers: [[Past Exam Question Bank#Parallel patterns|Bank section]]; scan/reduction theory: [[PRAM]].

### Map, Zip/Unzip and fusion

**Map** computes independent `out[i]=f(in[i])`; Zip combines aligned inputs, and Unzip separates tuple fields. For constant-cost functions, work is $\Theta(n)$ and ideal depth $O(1)$ with enough processors. Shared mutable state inside `f` breaks independence or adds contention; use private state or an explicit reduction. Fuse successive maps as `g(f(x))` when the intermediate collection is not otherwise required, saving storage and a memory pass.

### Reduce: assumptions and order

Use an **associative** operator and an identity for empty partitions. Commutativity is unnecessary if original operand order is preserved. A work-efficient tree uses $\Theta(n)$ work, $\Theta(\log n)$ depth, or $O(n/p+\log p)$ time with $p$ processors. The [[#Tree reduction and chunking — January 2026|section 3 reduction]] supplies the model. Parallel reassociation can alter floating-point rounding; ordinary concurrent writes do not themselves implement a reduction.

### Inclusive/exclusive Scan and composition — September 2026

Inclusive scan includes the current element; exclusive scan starts with the identity and includes only earlier elements. For $[3,1,4]$, addition gives $[3,4,8]$ versus $[0,3,4]$. Work-efficient tree scan has **$\Theta(n)$ work and $\Theta(\log n)$ depth**; simple doubling spends more work. Scan–Reduce can find the maximum prefix balance by scanning changes then reducing with max. If only the total is needed, the final sum prefix already provides it.

### Gather: one index per output

**`out[i]=in[index[i]]`** is output-driven. Repeated indices produce shared reads, not competing output writes. For $m$ outputs, work is $\Theta(m)$ and CREW depth $O(1)$ with $m$ processors, assuming valid indices and no harmful aliasing. A ten-entry index array can select ten values from a hundred-entry input. Gather performs final placement in Unpack/Unsplit. EREW needs unique reads, replication or a suitable schedule.

### Scatter and collision rules

**`out[index[i]]=in[i]`** is input-driven. Distinct destinations give $\Theta(n)$ work and $O(1)$ EREW depth with enough processors; a permutation scatter is the clean case. Repeated destinations require specified semantics: reject collisions, require equal values, select an arbitrary/priority winner, or merge using an associative operator. **Merge collision resolution belongs to Scatter, not ordinary Gather.** A histogram needs atomic combining or a reduction algorithm, not unsynchronized stores.

### Pack: stable filtering — September 2026

Map the predicate to Boolean flags $b_i$, compute their exclusive prefix sums $s_i$, and write selected values to **`out[s[i]]`**. The output length is the final prefix plus final flag, or zero for empty input. Selected destinations are distinct and preserve input order. With a work-efficient scan, Pack uses **$\Theta(n)$ work and $\Theta(\log n)$ depth**. The predicate must have constant cost for these bounds.

### Split and Bin

Split stably groups Boolean classes. If true elements come first, let $s_i$ count earlier true flags and $K$ be their total: destinations are **$s_i$ for true, $K+i-s_i$ for false**. One scan and collision-free scatter give $\Theta(n)$ work and $\Theta(\log n)$ depth. Bin generalizes to multiple buckets, requiring bucket counts, offsets and unique per-bucket positions. Merely choosing a bucket does not resolve write collisions.

### Unpack and Unsplit require retained metadata

Unpack uses the original mask and its prefix counts to gather packed values into selected positions, writing a defined default elsewhere. It cannot restore discarded values. Unsplit gathers from `s[i]` or `K+i-s[i]` according to the retained mask, recovering the original interleaving of both groups. Both use linear work and logarithmic scan depth; placement alone is constant-depth if positions are already supplied. Without mask/permutation information, the original layout is not generally recoverable.

### Stencil, Shift and boundaries

A stencil computes each output from a fixed-size input neighborhood; define edge behavior and preserve old-step values, usually with double buffering. Overlap between neighborhoods gives shared reads: one step has $\Theta(n)$ work and $O(1)$ CREW depth. Multiple steps need ordering. Shift reads a fixed displaced source into separate output storage, with explicit padding or cyclic wrap; it has the same work/depth and unique valid source reads, so EREW suffices.

### Pipeline: latency versus throughput — September 2026

Different items occupy ordered stages concurrently. Use synchronized bounded queues or tasks with producer/consumer dependencies. For stage times $t_1,\ldots,t_s$, startup latency is roughly $\sum t_i$, while steady-state item time cannot beat **$\max t_i$** without replicating the bottleneck stage. Good scaling needs many items, balanced sufficiently coarse stages and controlled transfer costs. A pipeline respects each item's flow dependencies; it does not erase them.

### Fork-join, barriers and Workpile

Fork-join creates/activates branches and awaits their completion; a barrier is a rendezvous among continuing participants. **Workpile** uses a pool and task queue, allowing jobs to generate further jobs; Map instead has a fixed collection. Protect the queue and count active generators: an empty queue alone does not establish termination. Tasks can run on existing worker threads, so neither a new task nor a join necessarily creates/destroys an operating-system thread.

### Parallel quicksort and fused Map–Reduce

Quicksort's independent recursive branches fit tasks, but sequential partitioning leaves **$\Theta(n)$ balanced span** against $\Theta(n\log n)$ work. Parallel partitioning can reduce balanced span to $O(\log^2 n)$; task cutoffs control overhead. For Map–Reduce, compute each transformed value directly into a local accumulator, then combine partials. Sum of squares is an example: linear work and logarithmic ideal depth, with no intermediate mapped array. These are distinct ways of reducing a sequential bottleneck.

## Task graphs and OpenMP implementations

**13 questions.** Recurring tasks: compute span/parallelism, choose threads, encode dependencies, and identify useful optimization targets. Latest graph question: September 2026.

### Work, span and average parallelism

For a weighted DAG, **$W=\sum_v w_v$** and span $D$ is the longest weighted source-to-sink path. Compute earliest finishes as $F(v)=w_v+\max_{u\to v}F(u)$. Then $W/D$ is average available parallelism and $T_p\ge\max(W/p,D)$. For an actual schedule, average busy processors is $W/T_p$. Include every edge; a missed cross-edge can change the critical path completely.

### Why rounding average parallelism is insufficient

**$\lceil W/D\rceil$ is a lower bound, not always enough threads to attain span.** Indivisible tasks, readiness times and simultaneous branch deadlines can require more. Compare explicit legal schedules for the offered thread counts; do not select solely by average utilization. Some bank graphs need three or four threads despite smaller rounded average parallelism. Real thread/task overhead can change the best measured choice again.

### Optimize span and use the right sequential baseline

Shortening a task off all critical paths cannot reduce unlimited-processor time. If several paths tie, optimizing just one may leave another unchanged; after each candidate improvement, recompute the longest path because a previously shorter branch can take over. If some nodes are pure parallel-management overhead, keep them in parallel runtime but exclude them from the sequential useful-work baseline. Consequently graph parallelism and achievable speedup need not be the same ratio.

### Encoding the graph with OpenMP tasks

Use one **`parallel` team**, one **`single` generator**, and sibling tasks generated in dependency order. Express each edge through matching `depend(in/out/inout: token)` storage and keep tokens/data alive through completion. Enclose the graph in `taskgroup` to await its descendants. Dependencies concern storage locations, not a token becoming numerically nonzero. Tasks permit unrelated ready nodes to overlap; global barriers between every visual graph level impose unnecessary edges.

## OpenMP

**55 questions.** Scheduling, data scope, tasks versus sections, and cancellation recur; latest: sections/tasks, plain loops and schedules, September 2026. The bank's answers use OpenMP 5.2 terminology.

### Teams, worksharing and an ordinary for loop

**`parallel` creates a team; `for` distributes iterations within an existing team.** Without worksharing, every thread in a parallel region executes an ordinary C loop, duplicating work and possibly racing. A literal `section` is different: one assigned thread executes that block's ordinary loop serially. `for`, `sections` and `single` do not themselves create a team. The lexical region's dynamically called routines also execute concurrently and must be thread-safe.

### Data scope: shared, private and firstprivate

**`shared` refers to one original object; `private` creates separate ordinarily uninitialized C scalars; `firstprivate` copies the encounter-time value.** It does not reinitialize a value before every iteration or copy private updates back. `default(none)` forces explicit attributes where rules do not predetermine them. Thus `private(offset)` loses an original value such as 5; use `firstprivate` or shared read-only storage. Shared scope does not provide synchronization.

### Team size, runtime support and nesting

Control requested size through `num_threads`, `omp_set_num_threads` or `OMP_NUM_THREADS`; query actual size inside the region. Dynamic adjustment, active-level/thread limits and resources also matter. Software threads can exceed physical cores, often unprofitably. Nested parallel regions may form teams or be serialized; one team plus tasks often avoids oversubscription. Compiler/runtime support and feature versions are required. Logical fork-join does not require destroying the runtime's reusable thread pool at each region exit.

### Static versus dynamic scheduling — September 2026

**Static** distributes work in advance, giving low overhead and predictable locality; explicit chunks are assigned round-robin. **Dynamic** hands out chunks as threads finish, helping irregular work at coordination/locality cost. Guided decreases chunk sizes. Large chunks reduce overhead but can worsen balance. Scheduling belongs to worksharing loops and cannot repair dependences. The `simd` scheduling modifier can round chunks to an implementation-defined SIMD width; it does not promise the literal requested chunk size.

### Single versus master; implicit barriers

**`single`** runs once on an arbitrary team thread and normally has an end barrier; legacy **`master`** runs on the primary thread and has none. Modern `masked` provides selected-thread execution. Worksharing constructs commonly already synchronize at the end, so another explicit barrier is often redundant. `nowait` removes a permitted barrier only when subsequent consumers remain correctly ordered. All required participants must encounter explicit barriers consistently.

### Sections versus tasks and completion — September 2026

Use **sections for a fixed small set of independent coarse blocks**, and tasks for irregular, dynamic or recursive work. Each section executes once; a thread can execute several. Generate recursive tasks from a single initial call in one team, with a cutoff for tiny subproblems. `taskgroup` awaits the group and descendants; `taskwait` covers relevant direct children, so whole-tree completion requires suitable recursive waits or a surrounding group.

### Task dependencies, tree traversal and BFS

`depend(in: status[i])` matches prior sibling producers of the **same storage**, not a numeric readiness test. Keep storage alive and capture indices/pointers safely. Tree traversal can create child tasks, but an ordered BST lookup still follows one chosen path. A linked list needs a task-generating traversal or indexed preprocessing. **BFS must preserve frontier levels**, claim vertices safely, and complete a frontier before advancing; an arbitrary recursive traversal is not automatically BFS.

### Memory ordering, critical, atomic and reduction

OpenMP's relaxed memory model requires synchronization for ordering and visibility; declaring data shared or adding an arbitrary `flush` does not repair a race. **Critical** protects compound state with mutual exclusion; **atomic** protects a supported individual access, not a whole protocol or phase. For aggregates use **reduction**, which initializes private partials with the identity and combines them with the intended original value. Wait before consuming the result; floating-point order can change rounding.

### Cooperative cancellation — repeated timeline questions

Enable cancellation and target the valid enclosing `parallel`, `for`, `sections` or `taskgroup`. **`cancel` activates a request; threads notice at applicable cancellation points**, including suitable explicit points and barriers. A point passed before activation has no retroactive effect. Cancellation is not forced preemption or rollback; earlier side effects remain, and lock/resource handling must stay valid. Without enabled cancellation, the directives have no cancellation effect. [OpenMP cancellation rules](https://www.openmp.org/spec-html/5.2/openmpse99.html).

### SIMD and fusing Map–Reduce — June 2026

**`simd` vectorizes suitable iterations; it does not create CPU threads.** Combine it with `parallel for` for cores plus lanes, and use `reduction` for a shared scalar. Fuse `sum += f(a[i])` when mapped values are not otherwise needed. Per-element atomics may prevent lost updates but serialize a cache line; they do not protect hidden state in `f` or replace a producer/consumer barrier.

### Monte Carlo code and hidden shared state

For a unit-circle estimate, test **`x*x+y*y<=1`**, not simply whether the expression is nonzero. Give workers appropriate independent random streams and reduce the hit count. Identical private seeds repeat samples; a private generator state is not automatically statistically independent. Also respect scoping restrictions: a scalar already private in the binding parallel region cannot simply be placed in `firstprivate` on its worksharing loop. Correct pragma syntax and declaration scope before analyzing speedup.

## Pthreads and shared-memory synchronization

**18 questions.** Most repeated: joins versus barriers, condition variables and thread lifetime. Reference answers: [[Past Exam Question Bank#Pthreads and shared-memory synchronization|Bank section]].

### Starting workers, passing arguments and returning results

`pthread_create` passes one explicit **`void *` argument** to a `void *routine(void *)`; package multiple values in a stable per-worker struct. Do not pass every worker the same changing loop-variable address. A joinable worker returns a pointer or calls `pthread_exit(value)`, and `pthread_join` retrieves it. Result storage must outlive the worker: use heap/caller storage, never its terminated stack. A join also establishes completion before consuming shared output.

### Joinable versus detached; main's lifetime

A **joinable** thread can be awaited and its result retrieved; a **detached** thread releases termination resources automatically and cannot be joined. Detached workers can still use normal synchronization, but need an explicit completion/data-lifetime protocol. Returning from initial `main` terminates the process and its workers. Use **`pthread_exit(NULL)` instead of returning**, or join the workers first; threads do not continue after the process exits.

### Mutexes, conditions and predicates

Pthreads synchronization is explicit. Guard a shared predicate with a mutex and wait as **`while (!ready) pthread_cond_wait(&cv,&mutex)`**. Waiting atomically releases the lock and reacquires it before return. Producers update the predicate and signal/broadcast. Recheck because wakeups can be spurious or another consumer may take the resource. A notification is not a stored event; the predicate determines whether proceeding is safe. [POSIX condition-wait semantics](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3p.html).

### Barriers versus joins

`pthread_barrier_wait` releases the configured participant group when everyone arrives, then can be reused for another phase. One participant receives `PTHREAD_BARRIER_SERIAL_THREAD`, not an error. **A join waits for a target to terminate**, so it does not replace a reusable rendezvous between continuing workers. A mutex instead supplies mutual exclusion. These constructs address different relationships; choose the one the computation actually needs.

### Worker pools and fixed pipelines

Spawn a fixed pool once and feed it a mutex/condition-protected task queue: this implements Workpile and avoids per-job thread creation. Termination must account for active jobs that can generate more work. A pipeline connects stage workers with bounded queues, uses empty/full predicates, and propagates end-of-stream. Different items overlap but each retains stage order. OpenMP provides higher-level scheduling/data-scoping support; both approaches still require correct shared-state and lifetime handling.

## MPI

**70 questions.** Communicators, collectives, receive sizing, deadlocks and communication/computation overlap dominate; latest repeats: September 2026. Reference answers: [[Past Exam Question Bank#MPI|Bank section]].

### Standard, implementations, processes and launch

**MPI is a specification; Open MPI and MPICH implement it.** Implementations supply libraries, headers/modules, compiler wrappers and launch/runtime integration. MPI normally coordinates separate processes across nodes, while host OpenMP uses threads inside shared-memory nodes. `mpirun -np p` launches $p$ instances; launching serial `echo` four times usually prints four lines. Scheduler launchers and singleton execution are possible. Rely on standard semantics, not incidental test-machine buffering or timing.

### Communicators and splitting — September 2026

A communicator supplies a **process group, local ranks and an isolated matching context**. Duplicate or split it to separate independent protocols. `MPI_Comm_split` groups equal colors and orders members by key; `MPI_UNDEFINED` excludes a process. In a process grid, form row/column communicators for broadcasts restricted to each row/column. The root and peer ranks are local to the chosen communicator, not automatically world ranks.

### Message matching and concrete tag use

Matching uses **communicator/context, source rank and integer tag**. For example, send lengths with `LENGTH_TAG=10` and payloads with `DATA_TAG=11` so receives cannot confuse them. `MPI_ANY_TAG`/`MPI_ANY_SOURCE` allow a dispatcher to inspect status and handle WORK/RESULT/STOP. After probing, receive the reported source/tag. Wildcards do not waive datatype/buffer requirements, and collectives do not use application tags to identify operations.

### Blocking completion is local, not a barrier

`MPI_Send` returns when its send buffer is reusable; standard mode may need a matching receive, depending on buffering. `MPI_Recv` completes when its matched data is in the receive buffer. Send completion does not imply receiver completion, and blocking one call does not stop every process. MPI synchronization is explicit. A data-moving collective's blocking return also generally concerns local completion; it is not automatically a group rendezvous.

### Deadlock and nonblocking counterexamples

Separate address spaces do not remove communication cycles. Two ranks receiving before either sends deadlock; two standard send-first peers can also depend on unavailable buffering. Use **`MPI_Sendrecv`**, complementary ordering, or post matching nonblocking sends/receives before waits. **`Irecv; Wait; Isend` can still deadlock** because the matching sends are never posted. Conversely, a temporarily waiting rank is not itself proof of a cycle; inspect the whole protocol.

### Receive capacity, Probe and message ownership

Receive `count` is buffer capacity in **datatype entries**, not bytes or a guaranteed actual length. Obtain size from a known protocol/header, or `Probe` plus `Get_count`, allocate, then receive the same source/tag. A probe does not consume the message. With competing receivers, use matched probing or serialize the probe/receive sequence. Too-small capacity causes truncation; a larger valid buffer is allowed. Count and derived datatype extent determine actual storage needs.

### Broadcast and Gather

**Bcast** distributes root's buffer to all communicator members. **Gather** collects one contribution per rank at root in rank order, including root's own contribution. Gather's **`recvcount` is per rank**, so $p$ ranks sending $k$ ordinary entries require root capacity $pk$. All members make compatible calls; root is a communicator-local rank. Receive arguments matter only where specified, and ordinary collective completion does not promise that every rank has returned.

### Scatter, leftovers and point-to-point implementation

Ordinary **Scatter** sends one equal-count block per rank; root's `sendcount` is per block. For $N$ items over $p$ ranks, **Scatterv** can use counts $\lfloor N/p\rfloor+[r<N\bmod p]$ and prefix displacements. Each receiver supplies its own scalar count. A simple point-to-point implementation sends each nonroot its slice and copies root's slice locally, avoiding a blocking self-send. Noncontiguous distributions need suitable datatypes or packing.

### Reduce is elementwise; Barrier is a rendezvous

With `count=k`, **Reduce produces $k$ reduced entries**, each combining corresponding positions across ranks; it does not collapse every buffer entry to one scalar. Use an associative supported operation and Allreduce when everyone needs the answer. **Barrier** waits for all group members to arrive, but does not exchange application data, synchronize clocks or automatically complete unrelated requests. For benchmark completion, reduce the maximum local elapsed time as appropriate.

### Overlap communication with independent computation — September 2026

Post **Irecv/Isend**, compute work independent of their active buffers, then Test/Wait before using received data or modifying send storage. A stencil computes interior cells during halo exchange, then boundaries after completion. **Nonblocking initiation permits overlap but does not guarantee background progress** throughout arbitrary computation; the implementation may need MPI calls to drive progress. Posting a receive early can also avoid unnecessary buffering/copying. [MPI nonblocking guarantees](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm).

### MPI with OpenMP and thread-support levels — June 2026

Call **`MPI_Init_thread` and check the provided level**. FUNNELED allows MPI only on the initializing thread; SERIALIZED permits calls by different threads without overlap; MULTIPLE permits concurrent calls. A primary communication thread can receive/wait while other workers compute; arbitrary `single` is insufficient for FUNNELED. Ordinary single-threaded ranks with private memory do not need a local mutex against other ranks, but shared-memory windows, threads or shared resources require their appropriate synchronization.

### Scoping and standard-compliance traps

The bank contains an OpenMP `default(none)` example inside the MPI section: explicitly scope ordinary surrounding values such as `num_steps` and `step`; loop indices may be predetermined private. More generally, match communication parameters, collective order, buffer lifetimes and requested thread support. Small tests can hide a protocol error through buffering or timing. Nonblocking calls and multithreading offer different overlap mechanisms; neither fixes an incorrect communication or data-sharing protocol by itself.

## CUDA

**8 historical questions.** Main topics: kernel/thread organization, memory and streams. These historical questions are retained to match the bank.

### Kernels, grids, blocks and warps

CUDA launches GPU kernels from a host program. Threads form **blocks**, blocks form a **grid**, and hardware executes groups of **32-thread warps**. A one-dimensional index is `blockIdx.x*blockDim.x+threadIdx.x`; guard `i<n` for partial final blocks. Threads in one block can share memory and synchronize; ordinary blocks cannot assume a particular execution order or simultaneous residence. Logical identifiers are not fixed physical-core numbers.

### Memory scope and the local-memory trap

Registers are thread-private; **shared memory is block-scoped**; global device memory is broadly accessible with required synchronization. CUDA **local memory is logically per-thread but can reside in device memory**, so “local” does not guarantee low latency. Constant/read-only paths and hardware caches have different roles from programmer-managed shared storage. Account for host/device placement and transfers. [CUDA kernel and memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

### Performance and synchronization scope

Provide enough independent work, coalesced memory access and useful kernel granularity; control register/shared-memory use and warp divergence. Transfers and launches can erase gains for small tasks. A block barrier is not a grid-wide barrier. Compared with a simple host OpenMP loop, CUDA usually requires more explicit device indexing, memory/lifetime management and tuning; OpenMP offload also has transfer costs. More nominal GPU threads do not imply all execute simultaneously.

### Streams and asynchronous submission

Ordinary operations in **one stream execute in issue order**. Submission can be asynchronous to the host; different streams may overlap when dependencies and hardware permit, but overlap is not guaranteed. Default-stream behavior depends on its mode, so separate handles alone do not prove independence. Keep the distinction between host return, device ordering and actual completion. [CUDA asynchronous execution](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/asynchronous-execution.html).

## Halide and high-level synthesis

**5 questions.** Halide algorithm/schedule separation and synthesis abstraction levels; latest HLS question: July 2025.

### Halide: algorithm versus schedule

Halide embeds image/array pipelines in C++. The **algorithm defines values; the schedule defines evaluation and storage**: loop order, tiling, vectorization, threading and placement of intermediates. Consumer/output-first scheduling is a useful heuristic because consumer loops determine producer regions and reuse; it is not reversed runtime dependency order or a guaranteed optimum. `compute_root` versus `compute_at` trades storage, locality and recomputation. [Halide producer/consumer scheduling](https://halide-lang.org/docs/tutorial/lesson_08_scheduling_2.html).

### Split and vectorize: read the generated loop shape

`split(x,x_outer,x_inner,4)` forms groups of four positions, conceptually **`x=x_min+4*x_outer+x_inner`**. `vectorize(x_inner)` applies SIMD to that inner dimension, nominally four positions at once; it does not itself create CPU threads. Nonmultiples of four need the compiler's applicable tail handling. Keep loop transformations separate from changing the mathematical function. [Halide scheduling tutorial](https://halide-lang.org/docs/tutorial/lesson_05_scheduling_1.html).

### High-level synthesis: input is not RTL

**HLS accepts a higher-level behavioral description**, commonly a supported C/C++ subset plus constraints/directives, and produces a hardware implementation such as RTL. RTL specifies registers, combinational logic and clocked transfers and is then consumed by downstream synthesis. Saying that RTL is the high-level synthesis input reverses these abstraction levels. The exact supported language/features depend on the tool. [AMD HLS introduction](https://docs.amd.com/r/en-US/ug1399-vitis-hls/Introduction).
