---
tags:
  - aapp
  - lecture
lecture: "4"
source: "[[lecture4-PRAM.pdf]]"
---
# PRAM

[[AAPP Index|Course index]] · Previous: [[Divide and Conquer]] · Next: [[ISPC]]

## Overview

The **Parallel Random Access Machine** is an abstract model for reasoning about parallel algorithms. It isolates dependencies, memory conflicts, and available parallelism before adding hardware costs such as cache misses, bandwidth limits, or thread scheduling.

A fast PRAM algorithm is not automatically fast in practice. Its ideal behavior supplies a starting point for asking what a real implementation, such as [[ISPC]], can achieve.

Source: [[lecture4-PRAM.pdf#page=2|Roadmap and motivation, pp. 2–3]].

## RAM and PRAM execution

A RAM has one processor, registers, addressable memory, and unit-cost basic operations. PRAM replicates the processor: $P_0,\ldots,P_{p-1}$ have private registers but communicate through shared memory.

The slide presentation divides execution into synchronous rounds:

1. Read input or shared memory.
2. Compute locally.
3. Write output or shared memory.
4. Complete the round before beginning the next.

Processors can be idle. Each knows its identifier, allowing distinct processors to work on different indices. A round's legality depends on the simultaneous access rules.

The model idealizes shared-memory access as unit-time. It does not charge realistic cache, network, bandwidth, or synchronization overhead.

Source: [[lecture4-PRAM.pdf#page=4|Machine model and rounds, pp. 4–5]].

## Memory-access rules

| Model | Concurrent reads of one cell | Concurrent writes to one cell |
|---|---|---|
| EREW | Forbidden | Forbidden |
| CREW | Allowed | Forbidden |
| CRCW | Allowed | Allowed under a specified conflict rule |

The letters mean **Exclusive/Concurrent Read** and **Exclusive/Concurrent Write**. Accessing distinct cells concurrently is allowed in all three models.

For instance, many processors reading one common scalar and writing separate output cells is legal on CREW but requires replication or a different schedule on EREW.

### CRCW write rules

- **Common:** all simultaneous writers must propose the same value.
- **Priority:** the writer with highest priority wins.
- **Arbitrary:** one contender wins, without a guarantee about which.
- **Random:** a winner is selected by a specified random mechanism.

> [!note] Clarification of the slides
> Page 7 groups “Arbitrary/Random” together and describes random selection. Keep the distinction explicit: an arbitrary choice does not establish a probability distribution. An analysis that uses winner probabilities needs a random rule.

An algorithm must establish that every access satisfies its model. “The hardware resolves it somehow” is not a correctness argument.

Source: [[lecture4-PRAM.pdf#page=6|Memory rules and write policies, pp. 6–7]].

## Performance quantities

Distinguish the following before comparing formulas:

| Symbol | Meaning |
|---|---|
| $T^*(n)$ | Best sequential baseline used for the comparison |
| $T_1(n)$ | Time of this parallel algorithm when executed on one processor |
| $T_p(n)$ | Time on $p$ processors |
| $W(n)$ | Total operations actually performed across processors |
| $C_p(n)=pT_p(n)$ | Allocated processor-time, including idle capacity |
| $T_\infty(n)$ | Critical-path time for the algorithm with enough processors |

### Speedup and efficiency

The lecture defines

$$
S_p(n)=\frac{T^*(n)}{T_p(n)},\qquad
E_p(n)=\frac{T_1(n)}{pT_p(n)}.
$$

> [!warning] Baseline distinction
> With these definitions, $E_p=S_p/p$ only when $T_1=T^*$. More generally,
> $$E_p=\frac{T_1}{T^*}\frac{S_p}{p}.$$
> To express efficiency relative to the best sequential baseline, use $E_p^*=T^*/(pT_p)=S_p/p$ and say which convention you use.

Example from the slides: if $T^*\approx T_1=80$ ms and $T_8=11$ ms, then $S_8=80/11\approx7.27$ and $E_8\approx0.909$. Using 32 processors with $T_{32}=5.7$ ms reduces latency further, but costs $32\cdot5.7=182.4$ processor-ms, versus $88$ for eight processors.

Source: [[lecture4-PRAM.pdf#page=8|Metric definitions]] · [[lecture4-PRAM.pdf#page=10|Baselines and examples, pp. 10–13]].

### Work versus cost

Under the unit-operation model,

$$
W(n)\le pT_p(n)=C_p(n).
$$

Idle processors contribute to cost but not useful operations. A work-efficient algorithm has $W(n)=O(T^*(n))$. For comparison with the best sequential baseline, cost optimality means $C_p(n)=\Theta(T^*(n))$.

Page 8 describes cost optimality with $T_1$; check that $T_1$ itself is competitive with $T^*$ before interpreting this as optimal relative to the sequential problem.

### Critical path

Even unlimited processors cannot execute dependent operations simultaneously. The longest chain of dependencies determines $T_\infty$.

For a fixed computation with total work $W$:

$$
T_p\ge \max\left(\frac{W}{p},T_\infty\right).
$$

**Supplementary interpretation:** $W/T_\infty$ is its average parallelism. Reserving substantially more processors cannot remove the critical path.

A binary tree reduction of $n=2^{20}$ values has linear work and about 20 combination levels. Its abundant parallelism eventually saturates; it does not imply useful utilization of arbitrarily many processors.

Source: [[lecture4-PRAM.pdf#page=15|Work, critical path, and reporting, pp. 15–18]].

## Map: matrix-vector multiplication

For $y=Ax$, assign separate rows to processors:

$$
y_i=\sum_{j=1}^n A_{ij}x_j.
$$

Different output entries are independent. They read common vector entries but write distinct $y_i$, making the natural row-based schedule CREW.

**Supplementary analysis for a dense $n\times n$ matrix:** with $1\le p\le n$ and sequential dot products within each assigned row,

$$
T_p=\Theta(n\lceil n/p\rceil),\qquad W=\Theta(n^2).
$$

With $p=n$, time is $\Theta(n)$ and cost is $\Theta(n^2)$: the schedule is cost-optimal relative to ordinary dense matrix-vector multiplication. Parallelizing each dot product further introduces reductions.

Source: [[lecture4-PRAM.pdf#page=20|Map pattern]].

## Reduction

To sum $n$ values, combine pairs, then pairs of partial sums, until one sum remains. For $n=8$:

```text
8 values → 4 pair sums → 2 sums → 1 result
```

There are $\log_2 n$ combination rounds and $n-1$ additions:

$$
T_p=\Theta(\log n)\text{ for }p=\Theta(n),\qquad
W=\Theta(n),\qquad C_p=\Theta(n\log n).
$$

This is work-efficient but not cost-optimal at that processor allocation: more processors become idle at each level.

**Memory legality:** use distinct source and destination arrays at each level, swapping them between rounds. Each source value is read by only one combining processor, and each output has one writer, so this schedule is EREW. This explicit staging avoids ambiguity in interpreting the in-place shorthand on page 14.

### Chunk first, then reduce

With fewer processors, each sums about $n/p$ inputs locally, then the $p$ partial sums are combined in a tree:

$$
T_p=\Theta(n/p+\log p),\qquad
C_p=\Theta(n+p\log p).
$$

It is cost-optimal while $p\log p=O(n)$. Once the reduction overhead dominates local work, adding processors offers diminishing returns.

> [!note] Numerical heuristic in the deck
> Page 22 labels roughly 65k processors safe for $n=10^6$. But $65{,}536\log_2 65{,}536=1{,}048{,}576$, already comparable to $n$, rather than “well below” it. Treat the table as an illustration and evaluate $p\log p$ for the actual values.

Source: [[lecture4-PRAM.pdf#page=14|Reduction algorithm]] · [[lecture4-PRAM.pdf#page=21|Reduction and chunking, pp. 21–22]].

## Prefix sum

A prefix sum produces every partial sum, not just the total:

$$
s_i=\sum_{j=1}^i a_j.
$$

Example: $[3,1,4,2]\mapsto[3,4,8,10]$.

**Supplementary logarithmic-depth construction:** at round $k$, combine each entry with the entry $2^k$ positions before it, when that index exists. Read a snapshot of the preceding round and write a separate output array. This gives one explicit implementation of the slide's depth bound; it is not a transcription of every arrow in its diagram.

```text
S = A
for k = 0 to ceil(log2(n)) - 1
    in parallel for each i
        next[i] = S[i]
        if i >= 2^k: next[i] += S[i - 2^k]
    S = next
```

After each round, the covered interval doubles. This simple construction has $\Theta(\log n)$ depth and $\Theta(n\log n)$ work. Concurrent reads occur, so CREW suffices. The slide's depth claim alone does not establish linear work.

**Supplementary alternative:** an up-sweep/down-sweep tree scan can achieve linear work and logarithmic depth. Thus two algorithms may have the same depth while different work costs.

Prefix sums support compaction, partitioning, and assigning output positions: if an element should be kept, a prefix count of keep-flags tells it where to write.

Source: [[lecture4-PRAM.pdf#page=23|Prefix-sum pattern]].

## Simulating limited resources

The slides state two resource/time trade-offs.

**Fewer processors:** a computation taking $t$ rounds on $p$ processors can be simulated on $p'<p$ by batching virtual processors. A more explicit bound is $O(t\lceil p/p'\rceil)$, preserving shared memory and the original round semantics.

Example: $p=1024$, $p'=64$, $t=1000$ gives 16 batches per ideal round, hence an order-of-magnitude estimate of 16,000 simulated rounds.

**Fewer shared-memory cells:** page 25 states $O(tm/m')$ time when $m$ shared cells are simulated with $m'<m$ and $\max(p,m')$ processors.

> [!warning] Missing assumptions in the memory statement
> The deck does not give the proof or fully specify where the complete simulated state resides. Serializing accesses cannot by itself store arbitrary contents of $m$ words in only $m'$ words of total storage. Retain this as the slide's shared-memory simulation statement, subject to additional storage/model assumptions. Do not interpret it as a general bound for running a program whose entire memory footprint exceeds available memory.

The processor and memory ratios on page 26 illustrate separate overhead sources; the slide does not prove that multiplying them always gives an end-to-end runtime bound.

Source: [[lecture4-PRAM.pdf#page=25|Scalability lemmas and example, pp. 25–26]].

## Strong and weak scaling

| Experiment | Fixed quantity | Question | Good behavior |
|---|---|---|---|
| Strong scaling | Total problem size $N$ | Can the same problem finish sooner? | Time decreases as $P$ grows |
| Weak scaling | Work per processor, $N/P$ | Can a larger problem finish in similar time? | Time stays approximately constant |

For strong scaling, run the same $N$ with $P=1,2,4,\ldots$ and report timings, the chosen baseline, speedup, efficiency, and cost. A plateau suggests that dependencies or practical overheads dominate.

For weak scaling, fix local workload $n_0$, set $N=Pn_0$, and use

$$
E_{\mathrm{weak}}(P)=\frac{T_1(n_0)}{T_P(Pn_0)}.
$$

The growing problem can expose communication and global synchronization costs even when local work remains constant.

### Amdahl's law

With serial fraction $s$ of the **fixed-size sequential runtime**, ideal speedup is

$$
S(P)=\frac{1}{s+(1-s)/P}.
$$

As $P\to\infty$, speedup approaches $1/s$ when $s>0$. For $s=0.1$, $S(8)=1/(0.1+0.9/8)\approx4.71$, and the limiting speedup is 10.

### Gustafson's law

For a scaled workload measured at fixed parallel runtime, let $s$ be the serial fraction of that **parallel run**. The scaled speedup is

$$
S(P)=s+(1-s)P.
$$

With $s=0.1$ and $P=8$, it is $7.3$. This does not contradict Amdahl: the workload and definition of the measured serial fraction differ.

Source: [[lecture4-PRAM.pdf#page=28|Scaling experiments, pp. 28–30]] · [[lecture4-PRAM.pdf#page=31|Scaling laws]].

## Labs and performance reporting

The deck proposes simulations of memory conflicts, reduction and prefix sum, scaling-law exploration, stencil scaling, and resource simulation. The notebook names in the slides are references; those notebook files were not supplied with the PDFs.

A useful report includes the problem size, model, processor count, algorithm, timing procedure, baseline, $T_p$, speedup, efficiency, cost, work, and critical-path limitation. For real measurements, use repeated runs and compare medians rather than one observation.

Source: [[lecture4-PRAM.pdf#page=18|Reporting template]] · [[lecture4-PRAM.pdf#page=35|Lab overview]].

## Takeaways

- State the memory model before claiming a parallel algorithm is legal.
- Separate useful work from reserved processor-time.
- A critical path survives even with unlimited processors.
- Speedup and efficiency comparisons require consistent baselines.
- Strong and weak scaling fix different quantities.

## Revision questions

1. Can two CREW processors write the same value into one cell simultaneously?
2. Why is an $n$-processor tree sum work-efficient but not cost-optimal?
3. When is chunk-and-tree summation cost-optimal?
4. When does the lecture's $E_p$ equal $S_p/p$?
5. What stays fixed in weak scaling?
6. What speedup limit does Amdahl predict for $s=0.2$?

> [!faq]- Answer sketch
> 1. No: exclusive writes forbid it even when values agree.
> 2. It performs $\Theta(n)$ operations but reserves $\Theta(n\log n)$ processor-time.
> 3. When $p\log p=O(n)$.
> 4. When $T_1=T^*$.
> 5. Work per processor; the total problem grows with processor count.
> 6. Five, under the ideal fixed-size assumptions.
