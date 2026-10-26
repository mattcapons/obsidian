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

![[aapp-lecture4-ram-pram.png|720]]

*RAM has one processor; PRAM has several processors communicating through shared memory in synchronous rounds.* [[lecture4-PRAM.pdf#page=4|Source slide 4]].

Source: [[lecture4-PRAM.pdf#page=4|Machine model and rounds, pp. 4–5]].

### What a synchronous round actually guarantees

Think of the read phase as taking the values needed for this step into private registers. Computation uses those saved values; the write phase publishes the results. A processor cannot use another processor's new result before that result has been produced. A **barrier** marks the point where every processor has completed the current step, so the next step may rely on all its outputs.

For example, start with $B=[10,20,30,40]$ and let processors $P_1,P_2,P_3$ compute $A[i]=B[i-1]+1$. They read 10, 20 and 30, then write $A[1]=11$, $A[2]=21$ and $A[3]=31$. The computation is independent across indices because nobody needs a newly computed $A$ value. In contrast, $A[i]=A[i-1]+1$ can denote a sequential recurrence if each iteration is meant to use the newly updated predecessor. Executing it simultaneously with old reads changes its meaning. Parallelization therefore starts by identifying **which version of each value an operation needs**.

One lecture “round” may bundle a constant number of primitive reads and arithmetic instructions. This does not affect asymptotic bounds, but exact round counts below deliberately state whether they count additions only. Unit cost does not mean that an arbitrarily long local loop can be hidden inside one round.

**Why private registers matter:** two processors can each have a variable named `sum` without a conflict, because those are different local storage locations. A conflict occurs when their addresses refer to the same shared cell, even if the source code uses different variable names.

## Memory-access rules

| Model | Concurrent reads of one cell | Concurrent writes to one cell |
|---|---|---|
| EREW | Forbidden | Forbidden |
| CREW | Allowed | Forbidden |
| CRCW | Allowed | Allowed under a specified conflict rule |

The letters mean **Exclusive/Concurrent Read** and **Exclusive/Concurrent Write**. Accessing distinct cells concurrently is allowed in all three models.

For instance, many processors reading one common scalar and writing separate output cells is legal on CREW but requires replication or a different schedule on EREW.

### Deciding legality from addresses

Suppose $P_0,P_1,P_2$ execute one access phase:

| Accesses | EREW | CREW | Reason |
|---|---|---|---|
| Read $A[0],A[1],A[2]$ | Legal | Legal | All addresses differ |
| Read $A[0],A[0],A[2]$ | Illegal | Legal | Two reads use the same cell |
| Write 7, 7, 9 to $B[0],B[0],B[2]$ | Illegal | Illegal | Equal proposed values do not remove an exclusive-write conflict |
| Write 7, 7, 9 to $B[0],B[1],B[2]$ | Legal | Legal | Values may coincide; addresses do not |

The rules apply **within the same phase**, not forever. Two processors may read the same location in different rounds on EREW. This gives a tradeoff: a stricter machine can often run the same logical computation after extra scheduling or copying.

For example, broadcasting one scalar to eight processors is immediate in CREW once the scalar is available. On EREW, use an expanding set of copies: one known copy becomes two, then four, then eight. At each copying stage, each old copy has only one reader and each new destination one writer. With separate read/write phases, this takes three copying stages and extra storage. It explains *why* concurrent-read permission can save time.

### CRCW write rules

- **Common:** all simultaneous writers must propose the same value.
- **Priority:** the writer with highest priority wins.
- **Arbitrary:** one contender wins, without a guarantee about which.
- **Random:** a winner is selected by a specified random mechanism.

> [!note] Clarification of the slides
> Page 7 groups “Arbitrary/Random” together and describes random selection. Keep the distinction explicit: an arbitrary choice does not establish a probability distribution. An analysis that uses winner probabilities needs a random rule.

An algorithm must establish that every access satisfies its model. “The hardware resolves it somehow” is not a correctness argument.

Source: [[lecture4-PRAM.pdf#page=6|Memory rules and write policies, pp. 6–7]].

### A useful CRCW example: Boolean OR

Initialize a shared flag to 0 in a separate step. Give each processor one Boolean input. Processors whose input is true write 1 to the flag; processors whose input is false do nothing. Under **common CRCW**, all simultaneous proposed writes agree, so the final flag is exactly the OR. If there are no true inputs, nobody writes and it stays 0.

Allowing false-input processors to write 0 at the same time would make this algorithm illegal under common CRCW whenever both input values occur. Under arbitrary CRCW it could also return 0 despite a true input. The conflict rule is therefore part of the proof, not a minor implementation option. On EREW, a binary OR reduction offers a logarithmic-depth alternative.

A priority-write rule selects a processor by its priority, not by the smallest numerical value it proposes. To find the first matching index, processors can have index order as their priority and only matching processors write. That does not automatically implement a minimum over unrelated data values. These examples elaborate the uses listed on [[lecture4-PRAM.pdf#page=6|slide 6]].

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

### Reading a processor-time diagram

For an addition-only reduction of eight inputs on four reserved processors, the three rounds use four, two, and one processor respectively. Thus $W=4+2+1=7$, $T_4=3$, and $C_4=4\cdot3=12$. There are five idle processor-rounds. The sequential baseline needs seven additions, so $S_4=7/3$ and $E_4^*=7/12$.

Work is the number of occupied operation slots; allocated cost is the entire rectangle of processors times rounds. An algorithm can have more work than the best sequential method because of bookkeeping or duplicated calculations, even if every allocated processor is busy. Consequently CPU utilization, work efficiency, and speedup are distinct measurements.

![[aapp-depth-pram-work-cost.png|720]]

*Original explanatory diagram: seven additions occupy a twelve-slot allocation. Gray slots are idle; colors group the reduction rounds. Counts exclude loads and barriers.*

Cost-optimality is asymptotic, so $C_p=2T^*$ can still be cost-optimal: a constant factor does not change $\Theta(T^*)$. Likewise, “work-efficient” does not promise an efficiency percentage at every processor count. It compares growth rates of total work.

### Critical path

Even unlimited processors cannot execute dependent operations simultaneously. The longest chain of dependencies determines $T_\infty$.

For a fixed computation with total work $W$:

$$
T_p\ge \max\left(\frac{W}{p},T_\infty\right).
$$

**Supplementary interpretation:** $W/T_\infty$ is its average parallelism. Reserving substantially more processors cannot remove the critical path.

**Supplementary connection to the simulation slides:** under ideal unit-cost operations and suitable scheduling, a computation of work $W$ and depth $D$ can run on CREW PRAM in $O(W/p+D)$ time. This is Brent's scheduling principle; it refines the idea of batching virtual processors. It supplies an explanation of the existing work/depth quantities, rather than a claim about actual machine timing. [Blelloch and Maggs, *Parallel Algorithms*, §25.2.4](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf).

For the tree sum, $W=\Theta(n)$ and $D=\Theta(\log n)$, giving the ideal bound $O(n/p+\log n)$. This describes a schedule for that computation. The chunk-and-tree algorithm below reorganizes the computation for the chosen $p$ and has its own $\log p$ reduction term.

A binary tree reduction of $n=2^{20}$ values has linear work and about 20 combination levels. Its abundant parallelism eventually saturates; it does not imply useful utilization of arbitrarily many processors.

Source: [[lecture4-PRAM.pdf#page=15|Work, critical path, and reporting, pp. 15–18]].

### Why work and depth give two different lower bounds

In $t$ rounds, $p$ processors can execute at most $pt$ unit operations. Finishing $W$ operations therefore requires $t\ge W/p$. Separately, if operation $b$ needs the output of $a$, they cannot occupy the same dependency step. A chain of $D$ operations requires at least $D$ rounds however large $p$ becomes. Both inequalities must hold, which is why the bound uses their **maximum**, not their sum.

For the eight-input reduction, $W=7$ and $D=3$. On two processors, $T_2\ge\max(7/2,3)$, hence at least four integer rounds. A four-round schedule exists: compute the four bottom-level additions in two batches, the two middle additions in one round, then the final addition. With four processors, three rounds suffice. With eight processors, the same dependency graph still takes three rounds. More processors remove a capacity limit, not a dependency.

The ratio $W/D$ is an average across the whole execution. It does not claim that exactly that many operations are ready in every round. Tree reduction starts with many ready operations and finishes with one. This distinction explains why a large average parallelism does not imply perfect utilization throughout a run.

## Map: matrix-vector multiplication

For $y=Ax$, assign separate rows to processors:

$$
y_i=\sum_{j=1}^n A_{ij}x_j.
$$

Different output entries are independent. They read common vector entries but write distinct $y_i$, making the natural row-based schedule CREW.

![[aapp-lecture4-map-rows.png|720]]

*Partition the matrix by rows: processors share the input vector but own independent output entries.* [[lecture4-PRAM.pdf#page=20|Source slide 20]].

**Supplementary analysis for a dense $n\times n$ matrix:** with $1\le p\le n$ and sequential dot products within each assigned row,

$$
T_p=\Theta(n\lceil n/p\rceil),\qquad W=\Theta(n^2).
$$

With $p=n$, time is $\Theta(n)$ and cost is $\Theta(n^2)$: the schedule is cost-optimal relative to ordinary dense matrix-vector multiplication. Parallelizing each dot product further introduces reductions.

Source: [[lecture4-PRAM.pdf#page=20|Map pattern]].

### Worked row decomposition

Take

$$
A=\begin{pmatrix}1&2&0\\0&3&1\\2&0&4\end{pmatrix},\qquad
x=\begin{pmatrix}2\\1\\3\end{pmatrix}.
$$

One processor per row computes $y_0=1\cdot2+2\cdot1+0\cdot3=4$, $y_1=0\cdot2+3\cdot1+1\cdot3=6$, and $y_2=2\cdot2+0\cdot1+4\cdot3=16$. No output requires another output. At a given column iteration, however, all processors read the same $x_j$, explaining the CREW requirement of this schedule.

For $n$ rows split across $p$ processors, the busiest processor owns $\lceil n/p\rceil$ rows. Each row contains a sequential loop of $n$ terms, so the largest assigned workload is $\Theta(n\lceil n/p\rceil)$. This derives the time bound rather than assuming that total work always divides perfectly by $p$. If $n=10$ and $p=4$, a balanced assignment has row counts $3,3,2,2$; completion waits for the three-row processors.

With more than $n$ processors, this **unchanged** row-only schedule cannot use the extras. To obtain further parallelism, change the algorithm so that products within a row are computed in parallel and combined by a reduction. This adds another layer of dependencies and scheduling; it is not obtained simply by replacing $p$ in the row-only formula.

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

![[aapp-lecture4-reduction-tree.png|720]]

*Eight values become four partial sums, then two, then one: tree depth is logarithmic while the number of additions is linear.* [[lecture4-PRAM.pdf#page=21|Source slide 21]].

**Memory legality:** use distinct source and destination arrays at each level, swapping them between rounds. Each source value is read by only one combining processor, and each output has one writer, so this schedule is EREW. This explicit staging avoids ambiguity in interpreting the in-place shorthand on page 14.

### Why the tree computes the same answer

At each level, a node stores the sum of one contiguous block of original inputs. Initially the blocks have size one. Combining two adjacent disjoint blocks produces their union's sum, so after $h$ levels a node represents $2^h$ inputs. The final node covers the whole array. The proof uses associativity of addition; it does not rely on all processors finishing arbitrary unrelated work at the same time.

For $[3,1,4,2,5,0,2,7]$, the successive levels are $[4,6,5,9]$, then $[10,14]$, then $[24]$. The additions total $4+2+1=7$, although each input-to-root path contains only three additions. Sum, maximum and Boolean OR have suitable associative operators. Subtraction does not: $(8-3)-1=4$ differs from $8-(3-1)=6$, so changing its grouping can change the answer.

If $n$ is not a power of two, either carry an unpaired value to the next level or pad to the next power of two with the operator's identity (0 for sum). Padding increases the number of leaves by less than a factor of two and keeps logarithmic depth. For floating-point sums, reassociation can change rounding; see [[ISPC#Reduction order and numerical results]].

### Chunk first, then reduce

With fewer processors, each sums about $n/p$ inputs locally, then the $p$ partial sums are combined in a tree:

$$
T_p=\Theta(n/p+\log p),\qquad
C_p=\Theta(n+p\log p).
$$

It is cost-optimal while $p\log p=O(n)$. Once the reduction overhead dominates local work, adding processors offers diminishing returns.

Using the optimal sequential sum as baseline, the chunk-and-tree model gives, up to constant factors,

$$
S_p=\Theta\left(\frac{n}{n/p+\log p}\right),\qquad
E_p^*=\Theta\left(\frac{n}{n+p\log p}\right).
$$

If $p\log p\ll n$, local work dominates and scaling is close to linear in this ideal model. If $p\log p\gg n$, the reduction term dominates and efficiency shrinks. Thus “work-efficient” and “efficient use of a particular allocation” answer different questions.

> [!note] Numerical heuristic in the deck
> Page 22 labels roughly 65k processors safe for $n=10^6$. But $65{,}536\log_2 65{,}536=1{,}048{,}576$, already comparable to $n$, rather than “well below” it. Treat the table as an illustration and evaluate $p\log p$ for the actual values.

Source: [[lecture4-PRAM.pdf#page=14|Reduction algorithm]] · [[lecture4-PRAM.pdf#page=21|Reduction and chunking, pp. 21–22]].

### Choosing processors with an exact small model

For $n=16$ and a power-of-two $p\le16$, initialize each local accumulator from its first element, count additions only, and use balanced chunks. Local summation takes $16/p-1$ rounds; combining partial sums takes $\log_2p$ rounds.

| $p$ | Local rounds | Tree rounds | $T_p$ | Work | Allocated cost $pT_p$ |
|---|---|---|---|---|---|
| 1 | 15 | 0 | 15 | 15 | 15 |
| 2 | 7 | 1 | 8 | 15 | 16 |
| 4 | 3 | 2 | 5 | 15 | 20 |
| 8 | 1 | 3 | 4 | 15 | 32 |
| 16 | 0 | 4 | 4 | 15 | 64 |

Moving from four to eight processors saves one round; moving from eight to sixteen saves none in this model. Work stays 15 because $p(16/p-1)+(p-1)=15$. Cost grows because increasing numbers of allocated processors wait during the tree phase. In a real run, reads and synchronization add costs, but the table already explains diminishing returns without appealing to hardware overhead.

## Prefix sum

A prefix sum produces every partial sum, not just the total:

$$
s_i=\sum_{j=1}^i a_j.
$$

Example: $[3,1,4,2]\mapsto[3,4,8,10]$.

![[aapp-lecture4-prefix-sum.png|720]]

*The slide illustrates computing every prefix through staged combinations; the CR labels mark concurrent reads. The pseudocode below gives a separate explicit construction.* [[lecture4-PRAM.pdf#page=23|Source slide 23]].

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

A later concrete application is [[Sorting#Counting sort]]: a prefix sum of key frequencies determines the output block for each key. Parallelizing that scan does not by itself resolve concurrent updates during histogram construction or record placement.

### Tracing the doubling scan

Use the note's snapshot-based algorithm on $[3,1,4,2]$:

| Stage | Offset | Values after the stage | Meaning of the last entry |
|---|---|---|---|
| Input | — | $[3,1,4,2]$ | Just the last input |
| First round | 1 | $[3,4,5,6]$ | $4+2$ |
| Second round | 2 | $[3,4,8,10]$ | $(3+1)+(4+2)$ |

After combining at offset $2^k$, entry $i$ contains the sum of the last at most $2^{k+1}$ inputs ending at $i$. The previous value and its offset neighbor summarize adjacent, disjoint intervals, so no input is counted twice. Once that interval reaches the beginning of the array, the entry is its complete prefix.

Reading a snapshot is essential. In the first round, entry 2 must read the **old** entry 1, equal to 1. If a left-to-right in-place implementation first changes entry 1 to 4, then uses it for entry 2, the claimed parallel round no longer follows this invariant. Two buffers make the intended semantics explicit.

Unlike a reduction, this scan keeps $n$ output positions across all $\lceil\log_2n\rceil$ rounds. For power-of-two $n$, the additions count is $\sum_{k=0}^{\lg n-1}(n-2^k)=n\lg n-n+1$. For $n=4$, that is five additions. The algorithm achieves low depth by doing more work than a sequential running sum.

### How the work-efficient tree scan works

**Supplementary explanation of the alternative above:** the up-sweep stores sums for subtrees. In the down-sweep, each subtree receives the sum of everything *before* it. The root receives 0; a left child receives its parent's incoming prefix, and a right child receives that prefix plus the left child's subtree sum. At the leaves, these incoming values are the exclusive prefixes. There are $O(n)$ tree nodes and two logarithmic traversals. [Blelloch, *Prefix Sums and Their Applications*, §1.2](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf).

For the original example $[3,1,4,2]$, the left subtree sums to 4 and the right to 6. The root sends prefix 0 to the left and 4 to the right. The left pair receives prefixes 0 and $0+3=3$; the right pair receives 4 and $4+4=8$. The exclusive result is therefore $[0,3,4,8]$. Adding each original input to its exclusive prefix gives the inclusive result $[3,4,8,10]$.

![[aapp-depth-pram-tree-scan.png|720]]

*Original four-element trace: subtree totals travel upward; the sum before each subtree travels downward. The leaf prefixes exclude the leaf's own value.*

![[aapp-depth-blelloch-prescan.png|720]]

*External reference diagram: Guy E. Blelloch, **Prefix Sums and Their Applications**, Figure 1.4(a), printed p. 42 (PDF page 8), diagram panel reproduced from the [author's CMU-hosted chapter](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf#page=8). It extends the same up-sweep/down-sweep idea to eight inputs; its leaf output is an exclusive scan. Original labels are retained.*

### Inclusive scan, exclusive scan, and compaction

**Supplementary clarification:** an inclusive sum includes the current element; an exclusive sum includes only earlier elements and starts with the additive identity $0$. A scan can use any associative operator; a general exclusive scan also needs an identity. Commutativity is not required when the original element order is preserved. [Blelloch, *Prefix Sums and Their Applications*, §§1.1–1.2](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf).

For $[3,1,4,2]$, the inclusive result is $[3,4,8,10]$ and the exclusive result is $[0,3,4,8]$.

**Worked compaction example:** let keep-flags be $[1,0,1,1,0]$. Their exclusive scan is $[0,1,1,2,3]$. Only kept elements write: input positions $0,2,3$ write to output positions $0,1,2$. These positions are distinct, so the output writes are exclusive; the preserved input order makes the compaction stable. The output length is the sum of the flags, $3$.

This explains a use of prefix sums already listed in the deck, without adding another sorting or graph algorithm.

## Simulating limited resources

The slides state two resource/time trade-offs.

**Fewer processors:** a computation taking $t$ rounds on $p$ processors can be simulated on $p'<p$ by batching virtual processors. A more explicit bound is $O(t\lceil p/p'\rceil)$, preserving shared memory and the original round semantics.

Example: $p=1024$, $p'=64$, $t=1000$ gives 16 batches per ideal round, hence an order-of-magnitude estimate of 16,000 simulated rounds.

**Fewer shared-memory cells:** page 25 states $O(tm/m')$ time when $m$ shared cells are simulated with $m'<m$ and $\max(p,m')$ processors.

> [!warning] Missing assumptions in the memory statement
> The deck does not give the proof or fully specify where the complete simulated state resides. Serializing accesses cannot by itself store arbitrary contents of $m$ words in only $m'$ words of total storage. Retain this as the slide's shared-memory simulation statement, subject to additional storage/model assumptions. Do not interpret it as a general bound for running a program whose entire memory footprint exceeds available memory.

The processor and memory ratios on page 26 illustrate separate overhead sources; the slide does not prove that multiplying them always gives an end-to-end runtime bound.

Source: [[lecture4-PRAM.pdf#page=25|Scalability lemmas and example, pp. 25–26]].

### Why processor batching must preserve phases

Suppose ten virtual processors must execute a round on three physical processors. Assign batches of at most three virtual processors, giving $\lceil10/3\rceil=4$ batches. Save each virtual processor's local registers between its simulated steps. To preserve the original round, collect the virtual reads before committing writes that could affect later batches; then complete the virtual computation/write phase using the original conflict policy.

Naively running the first batch's complete read–compute–write sequence before the next batch's reads can expose newly written values too early. The slowdown bound is meaningful only for a simulation that preserves the algorithm, not merely one that executes the same instructions in an arbitrary order. If a round contains $p$ active virtual operations, batching costs $O(\lceil p/p'\rceil)$ per primitive phase. Multiplying by $t$ gives the stated bound.

For the memory statement, distinguish **fast/shared capacity** from total storage. If old values are kept in an external store or in allowed processor-local state, extra transfers may trade time for scarce shared cells. If the entire machine has only $m'$ words and no such backing state, segmentation cannot retain arbitrary $m$ words. The unresolved model assumption is precisely where those values live and how they are accessed; a ratio $m/m'$ alone cannot answer it.

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

![[aapp-lecture4-scaling.png|720]]

*Strong scaling fixes total problem size; weak scaling fixes work per processor. Compare results only when the experiment is clear.* [[lecture4-PRAM.pdf#page=28|Source slide 28]].

### Two experiments with different meanings

Suppose a one-processor run on $n_0$ items takes 10 seconds. A four-processor run on the **same** $n_0$ items takes 3 seconds: strong-scaling speedup is $10/3\approx3.33$ and efficiency $10/(4\cdot3)\approx83.3\%$. Now suppose a four-processor run on $4n_0$ items takes 12 seconds. Its weak-scaling efficiency is $10/12\approx83.3\%$. It handles four times the data in only 20% more time, but this is not a 3.33-fold latency reduction for the original problem.

The 2D stencil mentioned on [[lecture4-PRAM.pdf#page=29|slides 29–30]] illustrates why weak scaling can be better. A square subdomain of side $L$ has about $L^2$ cell updates but only $O(L)$ boundary values to exchange with neighbors. With fixed total grid size, more processors mean smaller subdomains and a larger boundary-to-interior ratio. With fixed $L$ per processor, that ratio stays constant. Global barriers and communication can still prevent perfectly flat weak-scaling time.

This is also how to read the surface in [[lecture4-PRAM.pdf#page=32|slides 32–34]]: time is a function of both processor count and problem size. Strong scaling follows a fixed-size slice; weak scaling follows a path where size grows with processor count. Comparing curves taken along different paths without naming the experiment can be misleading.

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

**Supplementary derivation from the lecture's formulas:** normalize the fixed-size sequential runtime to one. Amdahl's parallel runtime is the unchanged serial part $s$ plus $(1-s)/P$. For Gustafson, normalize the observed parallel runtime to one: the sequential machine would execute the same serial part $s$ and $P$ copies of the observed parallel part $1-s$.

Neither expression includes communication or scheduling overhead. An overhead term $h(P)$ in Amdahl's normalized runtime changes the prediction to $1/(s+(1-s)/P+h(P))$. This helps explain a measured plateau without changing the ideal law.

Source: [[lecture4-PRAM.pdf#page=28|Scaling experiments, pp. 28–30]] · [[lecture4-PRAM.pdf#page=31|Scaling laws]].

### Reconciling the two serial fractions

A 100-second sequential job has 10 serial seconds and 90 parallelizable seconds. On eight ideal processors it takes $10+90/8=21.25$ seconds. Amdahl uses $s=10/100=0.1$ and predicts speedup $100/21.25\approx4.706$.

For that **same execution**, the serial fraction measured in the parallel run is $s'=10/21.25\approx0.470588$. Inserting this fraction into Gustafson's expression gives $s'+(1-s')8\approx4.706$ again. Substituting 0.1 into both laws describes different experiments, not two competing predictions for one job.

If synchronization adds five seconds to this eight-processor run, time becomes 26.25 seconds and actual speedup drops to about 3.81. The serial fraction is only one limit; overhead must be accounted for separately. This numerical example elaborates [[lecture4-PRAM.pdf#page=31|the lecture's scaling laws]].

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

## Exam practice

These are original problems under explicit idealized assumptions.

**1. Work, time, and cost.** Sum 16 values on four processors. Count only additions: each processor first sums four local values, then four partial sums are reduced by a binary tree.

> [!faq]- Worked solution
> Local sums take three rounds, followed by two tree rounds: $T_4=5$. Work is $4\cdot3+3=15$ additions. Allocated cost is $4\cdot5=20$ processor-rounds. The sequential addition count is 15, so $S_4=3$ and $E_4^*=3/4$. Reads, initialization, and barriers are deliberately excluded from this small count. The idle slots during tree reduction explain $C_4>W$.

**2. Baseline trap.** Suppose $T^*=50$, $T_1=100$, $T_4=30$. Calculate speedup and both efficiency conventions.

> [!faq]- Worked solution
> $S_4=50/30=5/3$. Best-baseline efficiency is $E_4^*=50/(4\cdot30)=5/12$. The lecture's one-processor-implementation convention gives $E_4=100/(4\cdot30)=5/6$. The larger number does not remove the implementation's extra sequential work. Always state the baseline before interpreting the result.

**3. Trace and explain a scan.** Run the doubling scan on $[2,5,1,3]$. Give both rounds, the final inclusive and exclusive results, and the number of additions.

> [!faq]- Worked solution
> Offset 1 gives $[2,7,6,4]$; offset 2 gives $[2,7,8,11]$. The inclusive result is $[2,7,8,11]$ and the exclusive result is $[0,2,7,8]$. There are three additions in the first round and two in the second, five in total. Every round reads the preceding round's values, so its updates cannot be performed using a left-to-right overwrite.

**4. Check a CRCW design.** A shared flag begins at 0. Every processor writes its Boolean input to the flag in one phase. Does common CRCW make this an OR algorithm? Repair it.

> [!faq]- Worked solution
> No. Mixed true/false inputs propose different values, violating common CRCW. Have only true-input processors write 1, leaving false-input processors idle. Initialize to 0 in an earlier phase. All writes now agree, and absence of writes correctly represents all-false input.

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
