from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
out = Path('outputs/performance-review-2026-11-01')

feedback = {
8: r'''**Assessment: correct.** You correctly count executed operations across all processors and exclude idle slots. Count all basic operations required by the algorithm, including extra bookkeeping, rather than only useful arithmetic.

**Suggested exam answer:** Work $W(n)$ is the total number of basic operations actually executed by all processors during a PRAM computation. If $a_r$ operations execute in round $r$, then $W=\sum_r a_r$. Simultaneous operations count separately; idle processors contribute no operations. Allocated cost is instead $C_p=pT_p$, so $W\le C_p$ under the unit-operation convention.

**Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]].''',

9: r'''**Assessment: correct; use “allocated processor-time” for precision.** Your formula and inclusion of idle processors are right. Cost does not count every processor physically present in a machine: it counts the $p$ processors allocated to this computation for its duration.

**Suggested exam answer:** PRAM cost is $C_p(n)=pT_p(n)$, the number of allocated processors multiplied by the parallel execution time. It includes idle processor-time within that allocation. Work counts actual operations and can be smaller. For example, four processors reserved for three rounds cost 12 processor-rounds even if only seven operations execute.

**Study:** [[PRAM#Work versus cost]]; [[PRAM#Reading a processor-time diagram]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

10: r'''**Assessment: correct by reference to 009; supply the formula directly in an exam.** Your preceding definition applies here. The sequential baseline is needed to assess cost optimality, rather than to define cost itself.

**Suggested exam answer:** If execution on $p$ processors takes $T_p(n)$ time, its cost is $C_p(n)=pT_p(n)$. This is allocated processor-time, including idle time. Relative to the best sequential baseline $T^*(n)$, the implementation is cost-optimal when $C_p(n)=\Theta(T^*(n))$.

**Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

11: r'''**Assessment: mostly correct; distinguish the fixed budget from normalization.** You correctly identify Gustafson and the sequential comparison. The runtime is kept at a chosen budget, such as 10 seconds; writing it as 1 simply chooses normalized units. Growing the parallel workload as processors increase is the defining experiment.

**Suggested exam answer:** A fixed-time model keeps the parallel runtime approximately constant while increasing the amount of work with the number of processors. This is Gustafson's viewpoint. If $s_G$ is the serial fraction of the parallel runtime, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. It compares the time of the same scaled workload on one processor with its time on $p$ processors, assuming ideal parallel execution and unchanged serial work.

**Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

12: r'''**Assessment: correct formula and main interpretation; qualify the “no idling” explanation.** Efficiency compares runtimes and allocated cost. On real systems, overhead can lower efficiency even when processors are active. Keeping processors busy with duplicated or unnecessary work also does not establish efficiency relative to the best sequential algorithm.

**Suggested exam answer:** The course defines $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1$ is the runtime of the parallel algorithm on one processor and $T_p$ its runtime on $p$ processors. Ideal linear scaling gives $T_p=T_1/p$ and $E_p=1$. Lower efficiency indicates that the allocated processor-time exceeds the one-processor baseline, for example through idle capacity or additional overhead. $T_1$ need not equal the best sequential time $T^*$.

**Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

13: r'''**Assessment: mostly correct; define weak scaling through fixed work per processor.** Your association of strong scaling with Amdahl and scaled workloads with Gustafson is right. In a weak-scaling measurement, constant runtime is the desired result; the experiment fixes work per processor and measures whether runtime stays constant. Normalizing time to 1 does not make arbitrary workloads finish in the same time.

**Suggested exam answer:** Strong scaling fixes total workload and increases processor count to reduce runtime; Amdahl models this with $S_A(p)=1/(s_A+(1-s_A)/p)$ for serial fraction $s_A$ of sequential runtime. Weak scaling increases total workload in proportion to processor count, keeping work per processor fixed; good weak scaling keeps runtime approximately constant. Gustafson's fixed-time model explains the benefit of growing the parallel workload, with $S_G(p)=s_G+p(1-s_G)$, where $s_G$ is measured in the parallel run. Both ideal laws omit additional overhead.

**Study:** [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

14: r'''**Assessment: correct.** Your formula and definitions match the course. State explicitly that both runtimes solve the same problem on the same input.

**Suggested exam answer:** Speedup on $p$ processors is $S_p(n)=T^*(n)/T_p(n)$, where $T^*$ is the best sequential runtime used as the baseline and $T_p$ is the PRAM runtime on $p$ processors for the same problem and input. A speedup of 4 means parallel execution takes one quarter of the sequential time. The best sequential baseline $T^*$ can differ from $T_1$ for the parallel algorithm.

**Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=11|slide 11]].''',

15: r'''**Assessment: correct.** You identify the fixed workload and the changing runtime. Add the ideal formula if space permits.

**Suggested exam answer:** No. Amdahl uses a fixed-size problem: its workload remains the same as processors are added. If $s_A$ is the serial fraction of the sequential runtime, ideal speedup is $S_A(p)=1/(s_A+(1-s_A)/p)$. When $s_A>0$, speedup approaches $1/s_A$ as $p$ grows. Gustafson is associated with a fixed-time, scaled-workload model.

**Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

16: r'''**Assessment: revision cross-reference to 008; that definition is correct.** Write a self-contained definition when answering an individual exam question.

**Suggested exam answer:** Work $W(n)$ is the total number of basic operations actually executed across all processors. Equivalently, sum the number of executed operations over all rounds. Concurrent operations count separately and idle processor slots do not count. For a reduction of eight inputs, counting additions only, $W=4+2+1=7$ even though the parallel execution has three addition rounds.

**Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]].''',

17: r'''**Assessment: revision cross-reference to 009; that definition is correct.** Include the formula and the treatment of idle processors directly in an exam answer.

**Suggested exam answer:** Cost is $C_p(n)=pT_p(n)$, the total processor-time allocated to the PRAM application. All $p$ allocated processors count for the full runtime, including rounds in which some are idle. Thus cost can exceed work, which counts only executed operations. For four processors over three rounds, cost is 12 processor-rounds.

**Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

18: r'''**Assessment: correct.** You correctly distinguish the two baselines and give the condition for equality. Phrase the initial answer as “not necessarily,” since equality does hold when $T_1=T^*$.

**Suggested exam answer:** Not necessarily. Under the course definitions, $pE_p(n)=T_1(n)/T_p(n)$ while $S_p(n)=T^*(n)/T_p(n)$. Consequently, $pE_p=S_p$ exactly when the two sequential baselines agree, $T_1=T^*$. In general, $pE_p=(T_1/T^*)S_p$. Running a parallel algorithm on one processor can require more work than the best sequential algorithm.

**Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

19: r'''**Assessment: mostly correct simulation argument; quantify the do-all speedup.** Your virtual-processor explanation is sound. The simulation gives a bound on runtime, rather than an exact slowdown for every algorithm. Saying that speedup uses the physical processor count does not yet describe its behavior for independent iterations.

**Suggested exam answer:** If $p$ virtual processors require $t$ rounds, $p'<p$ physical processors can simulate them by batching, in $O(t\lceil p/p'\rceil)$ time with the same shared memory. Save virtual local states and preserve the original read–compute–write ordering and access policy. For a do-all computation of $n$ independent, equal-cost iterations, $p'$ processors need $\lceil n/p'\rceil$ iteration rounds. Relative to $n$ sequential rounds, ideal speedup is $n/\lceil n/p'\rceil$, approximately $p'$ for enough evenly divisible work. Extra virtual processors do not provide extra physical throughput.

**Example:** Eight independent unit-time iterations on three processors take three rounds, so speedup is $8/3$, below 3 because the last batch is incomplete. Fixed setup or other serial work can reduce speedup further.

**Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slide 25]].''',

20: r'''**Assessment: correct True/False choice; include the explanation locally.** The statement describes Amdahl's fixed-workload assumption. Runtime improvement is an ideal prediction when some work is parallelizable, rather than a guarantee on real hardware.

**Suggested exam answer:** True as a description of Amdahl's model. The input and total computational task stay fixed when processor count increases. The serial part retains its duration, while the parallelizable part is ideally divided among $p$ processors. For serial fraction $s_A$ of the sequential runtime, $T_p/T_{\mathrm{seq}}=s_A+(1-s_A)/p$. Its reciprocal is speedup. The same data is processed sooner when parallelism is available; communication or scheduling overhead can limit real gains.

**Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

21: r'''**Assessment: revision cross-reference to 006; the earlier formula is correct.** This question explicitly asks for the formula, so write it directly.

**Suggested exam answer:** $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1$ is the parallel algorithm's runtime on one processor and $T_p$ is its runtime on $p$ processors. The denominator is allocated processor-time. Ideal linear scaling gives efficiency 1. Since the course defines speedup using $T^*$, the identity $E_p=S_p/p$ additionally requires $T_1=T^*$.

**Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

22: r'''**Assessment: plausible idea, but incomplete without actual operation counts.** A reduction does not automatically do extra arithmetic: an ordinary binary-tree sum and an optimal sequential sum both use $n-1$ additions. Specify which parallelization operations add work. Idle processors increase cost, not work.

**Suggested exam answer:** Parallelizing a sum can introduce extra accumulator and merge operations. For example, a sequential loop that initializes one accumulator to 0 and adds eight inputs performs eight additions. In a parallel version, four processors each initialize an accumulator to 0 and add two inputs: eight additions in total. Combining the four partial sums needs three further additions, giving 11 additions versus eight sequentially. The extra work comes from the chosen partial-sum implementation. These counts isolate additions and consistently omit loads, stores, and initialization instructions.

**Qualification:** This overhead is implementation-dependent. Seeding each partial sum with its first input can avoid the redundant additions to zero. Extra work must be demonstrated, rather than inferred from the presence of a reduction.

**Study:** [[PRAM#Work versus cost]]; [[PRAM#Reduction]]; [[PRAM#Chunk first, then reduce]]; [[lecture4-PRAM.pdf#page=15|slide 15]].''',

23: r'''**Assessment: correct identification; state what “fixed-size” means.** Referring to earlier explanations is sufficient for your revision shorthand, but an exam answer needs the defining assumption.

**Suggested exam answer:** A fixed-size model holds the input and computational workload constant while increasing the number of processors. It asks how much the same problem's runtime can decrease. This is Amdahl's viewpoint: with sequential serial fraction $s_A$, $S_A(p)=1/(s_A+(1-s_A)/p)$.

**Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

24: r'''**Assessment: no solution supplied; the key condition is perfect linear speedup.** The question concerns the course's ideal comparison for the same problem and input, with compatible unit-cost operations and a best sequential baseline.

**Suggested exam answer:** Since $S_p=T^*/T_p$, equality $S_p=p$ holds when $T_p=T^*/p$, equivalently when allocated cost $pT_p$ exactly matches the sequential baseline $T^*$. This is ideal linear speedup: the baseline work is perfectly distributed with no lost processor-time or additional overhead. Strict inequality $S_p<p$ holds when $T_p>T^*/p$, for example because of serial dependencies, load imbalance, idle slots, or extra executed operations. Keeping every processor busy is insufficient if the parallel implementation does more work than the sequential baseline.

**Amdahl illustration:** With $T^*=T_{\mathrm{seq}}$ and the ideal fixed-size formula, $S_p=1/(s_A+(1-s_A)/p)$. For $p>1$, $s_A=0$ gives $S_p=p$, while $s_A>0$ gives $S_p<p$. Even with $s_A=0$, real overhead can prevent equality. The bound $S_p\le p$ assumes the stated ideal comparison; changing the baseline, workload, or machine cost assumptions changes that comparison.

**Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=11|slide 11]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

25: r'''**Assessment: revision cross-reference; refine the earlier weak-scaling definition.** Keep work per processor fixed. Approximately constant runtime is the desired scaling behavior, rather than a condition automatically satisfied by an implementation.

**Suggested exam answer:** Weak scaling increases total workload proportionally to the number of processors, holding work per processor fixed. For a baseline workload $n_0$ per processor, compare $T_1(n_0)$ with $T_p(pn_0)$ when workload is proportional to $n$. Good weak scaling keeps those runtimes approximately equal. It is associated with Gustafson's scaled-workload, fixed-time viewpoint. Gustafson's scaled speedup compares sequential and parallel execution of the same larger workload; that ratio differs from the weak-scaling efficiency measurement.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]].''',

26: r'''**Assessment: correct law identified; give its speedup and limiting behavior.** Referring to Amdahl alone does not supply the requested discussion.

**Suggested exam answer:** For a fixed-size workload with serial fraction $s_A$ measured in sequential runtime, ideal speedup is $S_A(p)=1/(s_A+(1-s_A)/p)$. Only the parallel part is divided by $p$; the serial duration stays fixed. If $s_A>0$, increasing processor count gives diminishing gains and speedup approaches $1/s_A$. If $s_A=0$, the ideal formula gives $S_A=p$. The formula assumes perfect distribution of parallel work and no additional overhead.

**Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

27: r'''**Assessment: revision cross-reference; make the two experiments explicit.** Your earlier distinction is useful, with the correction that weak scaling fixes work per processor and measures the resulting runtime.

**Suggested exam answer:** Strong scaling holds total workload fixed and adds processors to reduce runtime; Amdahl's law describes the ideal fixed-size speedup and its serial bottleneck. Weak scaling holds work per processor fixed, so total work grows with processor count; good behavior is approximately constant runtime. Gustafson's law describes the benefit of scaling the parallel workload within a fixed time budget. The serial fractions in the two laws refer to sequential and parallel runtime respectively.

**Study:** [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

28: r'''**Assessment: revision cross-reference; use the precise interpretation established in our discussion.** Gustafson reconstructs the sequential time of the same scaled workload. Multiplication by $p$ accounts for the work performed concurrently by all processors.

**Suggested exam answer:** With parallel runtime normalized to 1 and its serial fraction denoted by $s_G$, Gustafson's scaled speedup is $S_G(p)=s_G+p(1-s_G)$. A sequential processor executes the serial part once and takes $p$ times as long for the work completed during the parallel phase. Thus $S_G$ is the factor by which sequential execution of that same scaled workload would take longer. The model grows parallel work with processor count while holding the parallel time budget fixed. For fixed $s_G<1$, scaled speedup grows linearly with $p$ under the ideal assumptions.

**Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

29: r'''**Assessment: mostly correct strong-scaling idea; use matrix-vector multiplication and specify how the weak-scaling input grows.** The supplied example computes each matrix row dotted with one shared vector. Different output rows are independent. “Good strong scaling” is possible in the ideal model within the available row parallelism; it is not guaranteed for arbitrary processor counts or real memory systems.

**Suggested exam answer:** In $y=Ax$, separate processors can compute independent output rows. For a fixed $r\times c$ matrix and vector of length $c$, a row-based PRAM schedule takes $\Theta(c\lceil r/p\rceil)$ time, so increasing $p\le r$ reduces runtime while input size remains fixed: strong scaling. For weak scaling, one concrete choice is to grow the number of rows proportionally to $p$ while keeping $c$ and rows per processor fixed. Each processor then performs the same number of dot-product operations, so ideal runtime stays approximately constant while the total matrix grows. Real bandwidth, communication, and imbalance can limit either scaling behavior.

**Study:** [[PRAM#Map: matrix-vector multiplication]]; [[PRAM#Worked row decomposition]]; [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=20|slide 20]]; [[lecture4-PRAM.pdf#page=28|slide 28]].''',

30: r'''**Assessment: partly correct; explain the unchanged serial time and the growing workload.** You correctly identify Amdahl's ceiling when the serial fraction is positive. The parallelizable fraction of the original sequential workload remains fixed; its elapsed parallel execution time decreases. Gustafson's growth describes larger workloads and assumes a parallel-time serial fraction below 1.

**Suggested exam answer:** Amdahl fixes problem size. As $p$ increases, $(1-s_A)/p$ shrinks while serial time $s_A$ remains, so $S_A(p)=1/(s_A+(1-s_A)/p)$ approaches $1/s_A$ for $s_A>0$. Gustafson changes the experiment by increasing parallel work within a fixed runtime: $S_G(p)=s_G+p(1-s_G)$. For fixed $s_G<1$, scaled speedup grows linearly with processor count. This explains why many processors can remain useful for larger problems; it does not eliminate the serial bottleneck for a fixed problem. Both laws use ideal assumptions and different serial-fraction baselines.

**Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

31: r'''**Assessment: speedup is inverted; efficiency is correct; optimality does not follow.** $(n^3)/(n^3/p)=p$, rather than $1/p$. Also, being given $T_1=n^3$ does not establish that no better sequential algorithm exists.

**Suggested exam answer:** The speedup relative to the one-processor execution is $T_1/T_p=n^3/(n^3/p)=p$, and efficiency is $E_p=T_1/(pT_p)=1$. Thus the formulas describe ideal linear scaling relative to $T_1$ in the processor range where the stated runtime model applies. With the course's definition $S_p=T^*/T_p$, the exact expression is $S_p=pT^*(n)/n^3$. If the intended additional assumption is $T^*=T_1=n^3$, then $S_p=p$ and the cost $pT_p=n^3$ matches that sequential baseline. The supplied runtimes alone do not prove $T_1=T^*$ or establish a detailed processor schedule.

**Study:** [[PRAM#Performance quantities]]; [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

32: r'''**Assessment: incomplete; explain why a large processor count can still be useful.** The implication for massively parallel systems follows from growing the amount of parallel work, rather than repeatedly accelerating a fixed small problem.

**Suggested exam answer:** Weak scaling keeps work per processor fixed as processors and total work increase. Gustafson's fixed-time model expresses the associated opportunity: for parallel-run serial fraction $s_G$, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. If $s_G$ remains small, it is close to $p$, so a massively parallel system can solve a proportionally larger problem within roughly the same time budget. This requires sufficient independent work and controlled serial, communication, and synchronization costs. The law supports this possibility; it does not guarantee that every growing application scales well.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

33: r'''**Assessment: correct; add a one-line derivation.** The prompt explicitly supplies the baseline equality needed for your identity.

**Suggested exam answer:** Since $T^*(n)=T_1(n)$, $S_p(n)=T_1(n)/T_p(n)$ and $E_p(n)=T_1(n)/(pT_p(n))$. Therefore $S_p(n)=pE_p(n)$, equivalently $E_p=S_p/p$. With these matching baselines, ideal speedup $S_p=p$ gives efficiency 1.

**Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].''',

34: r'''**Assessment: revision cross-reference; include the experiment, ideal behavior, and limitations.** These are the key aspects an exam answer should state directly.

**Suggested exam answer:** Strong scalability measures how runtime changes when processor count increases for the same fixed total problem. Ideally, $T_p\approx T_1/p$ and speedup relative to $T_1$ is approximately $p$. Measure fixed-input runtimes over increasing processor counts and examine speedup and efficiency. Serial dependencies, limited parallelism, load imbalance, and real communication or synchronization overhead eventually limit gains. Amdahl's fixed-size model gives a ceiling $1/s_A$ when the sequential serial fraction $s_A$ is positive.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]].''',

35: r'''**Assessment: revision cross-reference; include the workload assumption and the runtime baseline of the serial fraction.** Your later explanation of sequential time for a scaled workload is the useful interpretation here.

**Suggested exam answer:** Gustafson considers growing the parallel workload with processor count while keeping parallel runtime fixed. If $s_G$ is the serial fraction of that parallel run, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. It compares one-processor and $p$-processor execution of the same scaled problem. For a small, approximately constant $s_G$, scaled speedup can remain close to linear, supporting the usefulness of large systems for larger workloads. This relates to weak scaling; it assumes enough parallel work and manageable serial and communication costs. See also [Gustafson's fixed-size and scaled-size comparison](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).

**Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

36: r'''**Assessment: correct example and effect; make the cost calculation explicit.** In a fixed tree-reduction schedule, later levels have fewer independent operations, so the allocated processors cannot all stay busy. Idle slots contribute to allocated cost without adding work. They do not necessarily make elapsed runtime increase when more processors are added.

**Suggested exam answer:** Consider summing eight inputs by a binary tree on four allocated processors. Counting addition rounds only, the three levels execute 4, 2, and 1 additions. Thus $W=7$, $T_4=3$, and $C_4=4\cdot3=12$. The last two levels have insufficient independent additions to occupy every processor, leaving five idle slots. A one-processor execution needs seven additions, so $E_4=7/12\approx0.583$. The dependencies impose this loss of utilization for the stated schedule. Efficiency 1 is the ideal upper value for this fixed-computation PRAM comparison.

**Study:** [[PRAM#Reading a processor-time diagram]]; [[PRAM#Reduction]]; [[lecture4-PRAM.pdf#page=21|slide 21]].''',

37: r'''**Assessment: not justified; near-linear speedup alone does not distinguish the models.** Amdahl can predict nearly linear speedup over the measured processor range if its serial fraction is sufficiently small. Its eventual ceiling does not imply visibly diminishing returns at every processor count.

**Suggested exam answer:** More information about the experiment is needed. If the workload is fixed, near-linear speedup is compatible with Amdahl when the sequential serial fraction is small; with $s_A=0$, its ideal formula gives exactly $S_A=p$. If the workload grows with processor count at approximately fixed runtime, near-linear scaled speedup is consistent with Gustafson and a small parallel-run serial fraction $s_G$. Identify what remains fixed and how speedup is defined before selecting a model. The observed curve alone is insufficient.

**Example:** Amdahl with $s_A=0.001$ and $p=8$ gives $S_A=1/(0.001+0.999/8)\approx7.94$, very close to 8 despite using a fixed-size model. This counterexample follows directly from the formula; it is not a claim about which experiment the question omitted.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

38: r'''**Assessment: revision cross-reference; summarize the two laws with their assumptions.** The interpretation in terms of time and processors is essential, rather than just naming the formulas.

**Suggested exam answer:** Amdahl holds problem size fixed and models how adding processors reduces runtime: $S_A(p)=1/(s_A+(1-s_A)/p)$, where $s_A$ is the serial fraction of sequential runtime. For $s_A>0$, speedup approaches $1/s_A$. Gustafson keeps a parallel time budget fixed while increasing parallel workload: $S_G(p)=s_G+p(1-s_G)$, where $s_G$ is measured in the parallel run. This can give near-linear scaled speedup for small $s_G$. The laws correspond to fixed-size and scaled-size viewpoints, associated with strong and weak scaling. They are compatible; their workloads and serial-fraction baselines differ. Real overhead must be assessed separately.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

39: r'''**Assessment: revision cross-reference; give both runtime constructions explicitly.** Both speedups compare sequential and parallel execution of the same workload within each calculation; the workload may grow across Gustafson's processor-count experiments.

**Suggested exam answer:** Amdahl normalizes a fixed problem's sequential time to 1. With sequential serial fraction $s_A$, its parallel time is $s_A+(1-s_A)/p$, so speedup is $1/(s_A+(1-s_A)/p)$. Gustafson normalizes the scaled problem's parallel time to 1. With parallel-run serial fraction $s_G$, its sequential time would be $s_G+p(1-s_G)$, which is also its scaled speedup. The fractions use different denominators, and both formulas assume ideal parallelization without extra overhead.

**Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].''',

40: r'''**Assessment: incomplete by reference; work efficiency and a concrete overhead example still need to be supplied.** Your earlier work definition is correct. Work efficiency is an asymptotic comparison, rather than the fraction of allocated processor-time that is busy.

**Suggested exam answer:** A parallel algorithm is work-efficient if $W(n)=O(T^*(n))$: its total executed operations are within a constant factor of the best sequential baseline. Parallelization may add initialization, duplicated calculations, or bookkeeping and merging operations. For example, summing $n$ values sequentially into one accumulator initialized to 0 uses $n$ additions. With $p$ nonempty chunks, initializing each partial accumulator to 0 and adding its inputs still uses $n$ additions, then merging the $p$ partials adds $p-1$ more. The parallel implementation therefore uses $n+p-1$ additions. Counting additions only, this demonstrates extra executed work, and it remains $O(n)$ for $p\le n$: more operations do not automatically destroy work efficiency. Idle processors affect cost rather than work.

**Model detail:** The example's extra additions depend on its accumulator initialization strategy and can be optimized away; it demonstrates one concrete implementation rather than a lower bound for parallel summation.

**Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]]. The asymptotic definition is also given by [Blelloch and Maggs, §25.2.3](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=9).''',

41: r'''**Assessment: revision cross-reference; use the corrected definition of weak scalability.** State what is fixed in the experiment and what successful performance looks like.

**Suggested exam answer:** Weak scalability measures runtime as processors and total work increase together, keeping work per processor fixed. If one processor handles workload $n_0$ in $T_1(n_0)$, ideal weak scaling gives $T_p(pn_0)\approx T_1(n_0)$ when work grows proportionally to $n$. Weak-scaling efficiency can be reported as $E_{\mathrm{weak}}=T_1(n_0)/T_p(pn_0)$. Communication, global synchronization, serial work, or imbalance can make runtime grow. Gustafson's fixed-time, scaled-workload viewpoint explains the benefit of larger systems, while constant measured runtime remains a result to verify.

**Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Two experiments with different meanings]]; [[lecture4-PRAM.pdf#page=28|slide 28]].''',
}

assert set(feedback) == set(range(8, 42))
original = bank_path.read_bytes()
text = original.decode('utf-8')
snapshot = (out / 'Past Exam Question Bank.md.snapshot').read_text()
for number, body in feedback.items():
    qid = f'AAPP-02-{number:03d}'
    pattern = rf'(^### {qid}\n.*?)(?=^### |^## |\Z)'
    match = re.search(pattern, text, re.M | re.S)
    before = re.search(pattern, snapshot, re.M | re.S)
    assert match and before, qid
    assert match[1] == before[1], f'{qid} changed during review'
    old = '> [!note]- Feedback\n> Not reviewed yet.'
    assert match[1].count(old) == 1, qid
    callout = '> [!note]- Feedback\n> **Reviewed: 2026-11-01.**\n>\n'
    callout += '\n'.join('> ' + line if line else '>' for line in body.splitlines())
    text = text[:match.start()] + match[1].replace(old, callout) + text[match.end():]

assert bank_path.read_bytes() == original, 'Note changed while preparing corrections'
bank_path.write_bytes(text.encode('utf-8'))
print('Added feedback to AAPP-02-008–041. Original answers and earlier feedback preserved.')
