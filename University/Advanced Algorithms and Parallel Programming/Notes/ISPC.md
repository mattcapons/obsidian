---
tags:
  - aapp
  - lecture
lecture: "4b"
source: "[[lecture4b-ISPC.pdf]]"
---
# ISPC

[[AAPP Index|Course index]] · Previous: [[PRAM]] · Next: [[Randomized Algorithms]]

## Overview

**Intel Implicit SPMD Program Compiler (ISPC)** expresses data-parallel computation in a C-like language. The lecture moves through single-core SIMD, communication within a gang, and multicore tasks.

The course uses [[PRAM]] to reason about parallel patterns; ISPC implements related patterns on real hardware. ISPC is not a literal PRAM machine: vector widths, memory access, masks, and scheduling affect performance.

Source: [[lecture4b-ISPC.pdf#page=3|Roadmap and introduction, pp. 3–9]].

## Two levels of parallelism

| Level | Mechanism | What executes in parallel? |
|---|---|---|
| Within a core | SIMD | Multiple data elements processed by vector instructions |
| Across cores | Tasks and a runtime | Multiple gangs scheduled onto worker threads |

**SIMD** means one instruction operates on several data values. **SPMD** means several logical instances execute the same program on different data. ISPC maps its SPMD expression onto SIMD hardware.

This distinction matters: creating eight logical instances does not mean creating eight operating-system threads. Conversely, one gang's vectorized execution does not by itself spread work across all CPU cores.

![[aapp-lecture4b-multicore-architecture.png|720]]

*A simplified multicore architecture: cores have local caches and share lower-level memory resources.* [[lecture4b-ISPC.pdf#page=5|Source slide 5]].

The slides compare manual low-level vector coding, C/C++ compiler auto-vectorization, and ISPC. Their statement that auto-vectorization is “disabled by default” should not be treated as universal: the behavior depends on the compiler and selected optimization flags.

Source: [[lecture4b-ISPC.pdf#page=5|Architecture and approaches, pp. 5–8]].

### From scalar instructions to a gang

A scalar statement such as `y = x * x` operates on one value. Imagine a four-lane vector instruction whose inputs are $[1,2,3,4]$: it can produce $[1,4,9,16]$ with one issued multiplication instruction acting on four lanes. ISPC lets the source describe the per-instance calculation while the compiler arranges vector instructions and masks.

This does not make an arbitrary four-step dependency chain four times faster. If one result is needed before the next can be computed, those operations remain sequential within each instance. The sine example obtains vector parallelism **across input values**; successive Taylor terms for one input still depend on earlier terms. More cores then provide a second opportunity to run multiple gangs at once.

![[aapp-depth-ispc-simd.png|720]]

*The lecture's scalar/vector comparison: a SIMD instruction applies the same operation to several lanes. This is different from launching several operating-system threads.* [[lecture4b-ISPC.pdf#page=6|Source slide 6]].

## Compilation and integration

ISPC compiles its source into object code and can generate a header exposing exported functions. A C/C++ application includes the generated interface and links the object code with its own code. Task-based code additionally needs an appropriate task runtime.

This lets the application delegate computational kernels while retaining its surrounding C/C++ structure. The compilation diagram is in [[lecture4b-ISPC.pdf#page=10|page 10]].

![[aapp-lecture4b-compilation.png|720]]

*Compile the ISPC kernel and C/C++ application separately, then link their object files into one application.* [[lecture4b-ISPC.pdf#page=10|Source slide 10]].

The deck links the [ISPC user guide](https://ispc.github.io/ispc.html) and [downloads](https://ispc.github.io/downloads.html). The user guide was consulted for the focused language clarifications below; examples in this note are study examples, not a compiled project.

The generated header tells the C/C++ caller the exported function's interface; the object file contains its compiled implementation. Linking resolves that interface to executable code. A call passes array addresses and scalar parameters, so the caller and kernel must agree on data types, layout, lengths and who owns the memory. Declaring a function `export` exposes an entry point; it does not copy every input array automatically or create a multicore task schedule.

A useful way to read the compilation picture is to follow one kernel: `.ispc` source becomes an object plus interface information; the C++ translation unit uses that interface; the linker combines the pieces. The task runtime is an additional dependency only when task operations are used. This explains the stages without assuming a particular installed compiler version or target flag.

## Gangs and program instances

An ISPC function runs as a **gang** of logical program instances. Each instance handles its own data while following the same program.

- `programIndex` identifies an instance within its gang.
- `programCount` is the gang size.

Do not hard-code a gang size into an algorithm unless the target-specific assumption is intentional. Logical gang size and hardware vector width are related but should not be casually equated for every target.

![[aapp-lecture4b-gang-execution.png|720]]

*A gang handles successive groups of array elements; the colors distinguish logical program instances, rather than separate OS threads.* [[lecture4b-ISPC.pdf#page=17|Source slide 17]].

Source: [[lecture4b-ISPC.pdf#page=16|Gang execution, pp. 16–18]] · [[lecture4b-ISPC.pdf#page=28|Instance identifiers]].

## Uniform and varying data

| Qualifier | Meaning | Example in the sine kernel |
|---|---|---|
| `uniform` | One value for the gang | Array size, term count, common loop counter |
| `varying` | A value per instance | Current input, accumulated result |

The default for ordinary local scalar declarations is `varying`. A uniform input can participate in a varying expression, but assigning an arbitrary varying result to a uniform variable is invalid. These details are documented in the [official qualifier reference](https://ispc.github.io/ispc.html#uniform-and-varying-qualifiers).

“Varying/private” describes per-instance values; it does not imply that all memory referenced by an instance is isolated. Instances can access shared array storage and can race if their writes collide.

### Values, addresses, and ownership

For a four-instance illustration, a uniform `size = 10` is one shared logical value. A varying index might have values $[0,1,2,3]$, and loading `vin[i]` then produces four input values. The array parameter may designate one common array even though different instances index different elements. “Uniform array parameter” does not mean all array entries contain the same number.

Likewise, distinct varying indices must be justified. If the indices are $[0,1,1,3]$ and all active instances write `vout[i]`, two writes target element 1. Having separate varying local values does not make the destinations separate. In the lecture's `foreach` map, each iteration owns its output index, which supplies the required argument for noncolliding writes.

A uniform loop counter is appropriate for the fixed Taylor term loop because every participating instance advances through the same term numbers. It would not describe independent iteration counts for pixels that escape at different times. Qualifiers express an invariant about values; they are not annotations to apply merely because one hopes for faster code.

### Masks and divergence

**Supplementary language clarification:** a gang shares a program counter, while an execution mask identifies the active instances. A varying conditional can run both branches under different masks; varying loops continue until all participating instances finish. [Official ISPC execution model](https://ispc.github.io/ispc.html#control-flow-within-a-gang).

For four lanes with inputs $[1,7,3,8]$ and condition `x > 5`, the true-branch mask is $[0,1,0,1]$. Only lanes 1 and 3 update their varying counters. A `uniform` counter would not represent four independent local counts.

In a Mandelbrot gang where iteration counts are $[2,2,2,100]$, the long-running pixel keeps the loop going after the other three lanes become inactive. The pixels are independent, but their different control paths can reduce SIMD utilization.

### A masked branch, step by step

For inputs $[1,7,3,8]$, suppose the code says `if (x > 5) y = x*2; else y = x+1;`. The true mask activates lanes 1 and 3, writing 14 and 16 there. The false mask activates lanes 0 and 2, writing 2 and 4. After reconvergence, the gang has $y=[2,14,4,16]$.

Both paths may require issued instructions, even though each logical instance takes only one path. An inactive lane does not “help” execute the other lane's work. As a simple utilization model, if each path costs one equal-cost vector arithmetic instruction, these two issued instructions contain eight lane slots but perform only four useful lane updates: 50% utilization of those arithmetic slots. Real instruction costs and compiler transformations can change the timing; the example isolates the effect of masks.

![[aapp-depth-ispc-masks.png|720]]

*Original four-lane branch trace. Each branch updates only its active lanes, then the results reconverge into one varying value.*

## The foreach statement

```c
foreach (i = 0 ... size) {
    vout[i] = vin[i] * vin[i];
}
```

The domain is half-open: $0\le i<\texttt{size}$. `foreach` distributes the iterations across program instances, including a partially occupied final group when necessary.

For `foreach (i = 0 ... 2)`, only indices 0 and 1 are written. Index 2 is not assigned by that loop; its value depends on prior initialization. The slide's `forach` spelling is a typo.

A `foreach` over independent output cells naturally expresses a map. A two-dimensional domain can cover matrix rows and columns.

Source: [[lecture4b-ISPC.pdf#page=19|foreach syntax]].

### Handling a partial final group

With ten elements and a four-instance gang, an illustrative contiguous schedule processes indices 0–3, then 4–7, then 8–9 with only two valid lanes. The last two lane positions must not read or write past the array. `foreach` provides the domain handling; this drawing is a possible schedule, not a promise that every target distributes all iteration spaces identically.

The distinction between iteration index and `programIndex` matters here. The iteration index ranges over all ten elements; `programIndex` identifies one of the four instances and is reused as the gang processes more elements. Writing `vout[programIndex]` when the intended destination is `vout[i]` would repeatedly overwrite only the first four entries in such a schedule.

For very small arrays, many lanes can be inactive even without branches. That and call overhead explain why exposing SIMD does not guarantee useful speedup for every input size.

## Example: approximating sine

The sine Taylor series is

$$
\sin x=\sum_{j=0}^{\infty}(-1)^j\frac{x^{2j+1}}{(2j+1)!}.
$$

For exactly $N$ terms, use $j=0,\ldots,N-1$. For $N=3$:

$$
\sin x\approx x-\frac{x^3}{6}+\frac{x^5}{120}.
$$

Each input array element can be processed independently. In the slide implementation, the partial sum and numerator vary by instance; the factorial denominator, sign, and series-loop index are uniform because all instances evaluate the same number of terms.

Source: [[lecture4b-ISPC.pdf#page=12|Taylor series]] · [[lecture4b-ISPC.pdf#page=14|C++ kernel]] · [[lecture4b-ISPC.pdf#page=20|ISPC kernel]].

### Corrected explanatory kernel

> [!warning] Issues in the slide code
> The printed loop starts with the $j=0$ term and then runs from $j=1$ through `terms`, inclusive. It therefore computes `terms + 1` terms, conflicting with comments implying that `terms == 1` gives only the initial term. On page 22, the unrolled numerator update uses assignment where multiplication is needed to advance the power. An integer factorial denominator can also overflow quickly.

The following supplementary version defines `terms` as the **total** number of terms, assumed at least one. It updates a term directly rather than forming a factorial:

$$
t_0=x,\qquad
t_j=-t_{j-1}\frac{x^2}{(2j)(2j+1)}.
$$

```c
// Explanatory ISPC kernel; terms >= 1.
export void sinx_study(const uniform float vin[],
                       uniform float vout[],
                       uniform int size,
                       uniform int terms) {
    foreach (i = 0 ... size) {
        float x = vin[i];
        float term = x;
        float sum = x;
        for (uniform int j = 1; j < terms; ++j) {
            uniform float a = 2.0f * j;
            uniform float b = a + 1.0f;
            term *= -(x * x) / (a * b);
            sum += term;
        }
        vout[i] = sum;
    }
}
```

For fixed term count $N$ and array length $n$, total arithmetic work is $\Theta(nN)$. Vector execution can process several independent inputs together, but does not remove this work.

This is a teaching approximation, not a replacement for a numerical library. Large arguments, finite precision, and an insufficient truncation order affect accuracy. Validate against a reference before comparing performance.

**Supplementary numerical check:** for $x=1$ and exactly three terms, the corrected kernel should approximate $1-1/6+1/120=101/120\approx0.8416667$. For $x=0$, every term is zero; for $x=-1$, the result is the negative of the value at $1$. These checks expose indexing and sign errors without treating a timing result as evidence of correctness.

### Deriving the term update and its limitation

Starting from $t_{j-1}=(-1)^{j-1}x^{2j-1}/(2j-1)!$, form the ratio to the next term:

$$
\frac{t_j}{t_{j-1}}=-\frac{x^2}{(2j)(2j+1)}.
$$

The next power adds two factors of $x$, the factorial adds the two successive integers, and the sign flips. This gives the update in the kernel directly and explains each part of the formula. At $x=1$, the first terms are $1,-1/6,1/120$; at $x=2$, they are $2,-8/6,32/120$, giving $14/15\approx0.933333$ after three terms.

**Supplementary accuracy reasoning:** on $|x|\le1$, the alternating terms decrease in magnitude, so truncating after three terms has error at most $|x|^7/7!\le1/5040\approx0.0001984$ in exact arithmetic. This is a truncation bound, separate from floating-point rounding. Large $|x|$ does not satisfy the same simple decreasing-from-the-start argument; production sine functions use range reduction and more carefully designed approximations. The lecture kernel is useful for studying independent arithmetic work, but its domain and requested accuracy must be fixed before comparing implementations.

### Reading the timing screenshots

The examples on pages 21 and 23 show C++ timings smaller than the corresponding ISPC timings in those particular runs. They do not establish that ISPC is always faster. Warm-up, optimization settings, vectorization, memory access, and implementation correctness all affect comparisons.

The manual C++ unrolling example groups eight elements to expose independent operations. Its arithmetic typo must be corrected before treating a timing comparison as a comparison of equivalent computations.

Source: [[lecture4b-ISPC.pdf#page=21|Initial timing comparison]] · [[lecture4b-ISPC.pdf#page=22|Unrolled code]] · [[lecture4b-ISPC.pdf#page=23|Second timing comparison]].

## Communication and reductions

Once each instance has produced a local value, a computation may need to combine those values. The lecture uses counting values above a threshold as its example.

### Local counts

```c
export uniform int count_greater_than(
    const uniform float vin[],
    uniform int size,
    uniform float threshold) {
    int counter = 0;
    foreach (i = 0 ... size) {
        if (vin[i] > threshold) {
            ++counter;
        }
    }
    return reduce_add(counter);
}
```

`counter` is varying: each instance accumulates its own count. `reduce_add` combines the active instances' values into a uniform result. This behavior is specified in the [official reduction reference](https://ispc.github.io/ispc.html#reductions).

The condition can differ between instances. A mask selects which instances execute the increment. A varying branch should therefore be understood in terms of active instances rather than independent CPU threads.

**Why reduce after the loop?** Accumulate varying local totals during `foreach`, then call `reduce_add` once. Repeated cross-lane reductions inside the loop can spend more time communicating than vectorization saves. Favor contiguous lane accesses where the data permits. These principles are explained in the [ISPC performance guide](https://ispc.github.io/perfguide.html#implementing-reductions-efficiently).

In the row-major matrix example, neighboring column lanes read neighboring entries of $B$ at a fixed $k$, while sharing the row's $A$ value. This favorable lane access is different from the full cache behavior across all $k$ iterations; SIMD-friendly code can still have memory bottlenecks.

For input $[1,7,3,8,9,2,6,0]$ and threshold $5$, the final count is $4$. Every element is examined once, so counting work is linear in the input length, plus a small gang-level reduction.

Source: [[lecture4b-ISPC.pdf#page=26|Counting problem]] · [[lecture4b-ISPC.pdf#page=32|High-level reduction]].

### Following local counts across groups

For the eight-element threshold example and a four-instance contiguous schedule, the first group $[1,7,3,8]$ contributes local increments $[0,1,0,1]$. The second group $[9,2,6,0]$ contributes $[1,0,1,0]$. The varying counters finish as $[1,1,1,1]$, then the reduction returns the scalar 4.

The varying `counter` is declared outside `foreach`, so each instance retains its running count across the iterations assigned to it. If it were reset at every group, earlier contributions would be lost. Each increment is local, avoiding a shared global counter with conflicting updates. The final reduction is where communication occurs deliberately.

For a different valid assignment of iterations to instances, the individual local counts could differ while their sum remains 4. The correctness invariant is that the sum of local counters equals the number of matching elements processed so far, not that a particular lane must count a particular input subset.

### shuffle and extract

- `shuffle(value, index)` obtains another instance's value, with source indices that may vary by instance.
- `extract(value, index)` selects one instance's value using a uniform index and produces a uniform scalar.

These focused semantics were checked against the [official cross-instance reference](https://ispc.github.io/ispc.html#cross-program-instance-operations).

The manual reduction on page 31 doubles its group size each round. With four initial counts $[2,1,3,4]$, the first stage establishes pair totals at the first lane of each pair: lane 0 has 3, lane 2 has 7. The next stage establishes the total 10 at lane 0; `extract(counter, 0)` returns it. Other lanes need not contain a valid global sum.

This is the same binary reduction idea as [[PRAM#Reduction]]. If the gang size is not a power of two, bounds checks for source indices matter. Prefer a built-in reduction when it expresses the operation; use manual communication when a needed pattern is not provided.

The screenshot on page 33 shows overlapping timing ranges for the manual and built-in versions. It supports the example comparison, not a universal performance ranking.

Source: [[lecture4b-ISPC.pdf#page=25|Communication overview]] · [[lecture4b-ISPC.pdf#page=29|shuffle and extract, pp. 29–30]] · [[lecture4b-ISPC.pdf#page=31|Manual reduction]] · [[lecture4b-ISPC.pdf#page=33|Timings]].

### What the manual shuffle reduction actually changes

The page 31 code updates more lanes than just the group leaders. Starting from $[2,1,3,4]$, its first group size is 2 and source indices are $[1,1,3,3]$. The shuffled values are $[1,1,4,4]$, so counters become $[3,2,7,8]$. Only lanes 0 and 2 are now meaningful pair leaders. At group size 4, all lanes select lane 2's value 7, giving $[10,9,14,15]$. Only lane 0 is the leader for the complete group and holds the total 10.

This explains why extracting lane 0 is correct while reducing **all four final counters** again would be wrong. The invariant is about the first lane of each group; other lanes are temporary values and need not describe disjoint sets. For this trace the shuffle sources are active and in range. A generalized manual routine must also establish those conditions under its masks. The built-in reduction avoids making the programmer maintain this particular leader invariant.

![[aapp-depth-ispc-manual-reduction.png|720]]

*The lecture marks the first instance of each group as the one with a valid partial result; shaded nonleaders should not be interpreted as additional independent totals.* [[lecture4b-ISPC.pdf#page=27|Source slide 27]].

## Tasks and multicore execution

An ISPC task is a unit of work executed by a gang. A task function is declared with `task` and returns `void`.

- `launch[n]` launches $n$ tasks.
- `taskIndex` identifies a task; `taskCount` gives the task count.
- `sync` waits for tasks launched by the current function.

A launching function implicitly waits before returning, as confirmed by the [official tasking reference](https://ispc.github.io/ispc.html#tasking-model). This allows the caller to use the completed output after the call returns.

The runtime maps tasks to worker threads. Tasks are not guaranteed to correspond one-to-one to physical cores. The deck uses the example runtime `examples/common/tasksys.cpp` and mentions OpenMP, TBB, and pthreads as other approaches to multicore parallelism.

Source: [[lecture4b-ISPC.pdf#page=36|Task model, pp. 36–37]] · [[lecture4b-ISPC.pdf#page=42|Multicore takeaway]].

### Task granularity and completion

Suppose eight equal row tasks run on a runtime with two worker threads. At most two workers execute tasks simultaneously; the remaining tasks wait to be scheduled. Each executing task uses a gang internally. The tasks may complete in a different order from their indices, but if they write disjoint rows the final matrix is unaffected by that order.

Launching one task per scalar multiplication would expose many tasks but require coordination to combine products and incur large scheduling overhead. A row task groups substantial work and owns a clear output region. Conversely, one task for the entire matrix would offer only one unit of work to the multicore scheduler. Task granularity is the amount of useful work placed between scheduling events.

A caller must not consume a task's output while the task can still be writing it. The `sync`/return guarantee supplies completion at the function boundary; it is not a mechanism that repairs conflicting writes among simultaneously executing tasks. This is the distinction between waiting for work to finish and proving that the work is race-free.

## Example: matrix multiplication with tasks

As in [[Divide and Conquer#Matrix multiplication]],

$$
C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}.
$$

The first ISPC implementation uses `foreach` across output entries but launches no tasks. It uses gang-level parallelism; the slide's “serial” label means absence of multicore task parallelism, not absence of SIMD.

The task implementation assigns **one row to each task**. Its structure is:

```text
task MATMUL-ROW(A, B, C, n)
    row = taskIndex
    foreach column in [0, n)
        value = 0
        for k in [0, n)
            value += A[row*n + k] * B[k*n + column]
        C[row*n + column] = value

export MATMUL(A, B, C, n)
    launch[n] MATMUL-ROW(A, B, C, n)
    // completion is guaranteed before this function returns
```

Rows can run on different cores; columns within a task use SIMD; each dot product still performs its $k$ iterations in sequence. The arithmetic work remains $\Theta(n^3)$.

Distinct tasks write different rows, and distinct column iterations write different cells. The reasoning assumes output storage does not overlap the input matrices. Performance still depends on layout, memory traffic, and task overhead.

Page 41 illustrates broader CPU utilization with tasks. Utilization alone is not a speedup measurement: use the metrics in [[PRAM#Performance quantities]] to evaluate whether the extra resources reduce time efficiently.

![[aapp-lecture4b-task-utilization.png|720]]

*The slide screenshot contrasts one busy worker with broad CPU utilization after enabling multicore tasks; it does not by itself measure speedup.* [[lecture4b-ISPC.pdf#page=41|Source slide 41]].

Source: [[lecture4b-ISPC.pdf#page=39|Gang-only implementation]] · [[lecture4b-ISPC.pdf#page=40|Task implementation]] · [[lecture4b-ISPC.pdf#page=41|Resource usage]].

### Reading one task's memory accesses

For row $i$ and four neighboring columns $j,j+1,j+2,j+3$, one iteration of the $k$ loop reads the same $A_{ik}$ but four adjacent entries $B_{k,j},\ldots,B_{k,j+3}$. Each lane accumulates a different $C$ entry. The next $k$ iteration advances to another row of $B$, while the partial sums stay local.

This layout explains both the opportunity and the limit: adjacent lane accesses can become efficient vector loads, but repeatedly streaming the rows of $B$ for many output rows can still move considerable data. SIMD width is not a bound on total memory bandwidth, and assigning more row tasks does not make memory traffic free. The [official ISPC performance guide](https://ispc.github.io/perfguide.html#understanding-gather-and-scatter) discusses coherent accesses; this row-by-row trace explains that principle for the supplied kernel.

## Mandelbrot exercise

For each complex parameter $c$, define

$$
z_0=0,\qquad z_{k+1}=z_k^2+c.
$$

The Mandelbrot set consists of parameters for which the sequence stays bounded. The slide examples are:

- $c=1$: $0,1,2,5,\ldots$, which escapes.
- $c=-1$: $0,-1,0,-1,\ldots$, which remains bounded.

A renderer assigns each pixel a complex parameter and records an escape iteration, or a maximum iteration count. Different pixels are independent, making the exercise suitable for SIMD and task decomposition.

![[aapp-lecture4b-mandelbrot-complex-plane.png|600]]

*A rendered view of the Mandelbrot set in the complex plane: black depicts the set, with colored bands outside it.* [Image: Lars H. Rohwedder / Wikimedia Commons, public domain](https://commons.wikimedia.org/wiki/File:Mandelbrot_Set_in_Complex_Plane.png).

**Supplementary implementation reasoning:** nearby pixels may require very different iteration counts. Within a gang, this leads to inactive lanes waiting for longer-running lanes; across tasks, it can cause load imbalance. Use moderate-sized tiles and measure both computation time and load distribution. A finite maximum iteration count approximates the image and does not prove membership for every non-escaping sample.

Source: [[lecture4b-ISPC.pdf#page=43|Exercise and set definition, pp. 43–44]] · [[lecture4b-ISPC.pdf#page=45|Rendering diagram]].

### From complex arithmetic to a pixel loop

Write $z=x+iy$ and $c=a+ib$. Expanding $z^2+c$ gives

$$
x_{\mathrm{next}}=x^2-y^2+a,\qquad
y_{\mathrm{next}}=2xy+b.
$$

Both expressions must use the **old** $x,y$. Overwriting $x$ before computing the new $y$ changes the recurrence. A renderer maps a pixel column and row to $a,b$ in a chosen complex-plane rectangle, initializes $x=y=0$, then iterates until escape or its iteration budget. This connects the formula on slide 44 to the coordinate picture on slide 45.

For the example escape counts $[2,2,2,100]$, equal-cost iteration arithmetic performs 106 useful lane-iterations while a four-lane gang spends up to $4\cdot100=400$ lane-iteration slots, about 26.5% utilization in that simplified model. This is not a claim about measured CPU efficiency; it isolates divergence. Tasks can spread tiles across cores, but uneven escape times within a gang remain a separate SIMD issue.

![[aapp-depth-ispc-pixel-map.png|720]]

*The slide maps a complex parameter to a pixel and colors it using the iteration count. Read the parameter $c$ as fixed for a pixel while $z$ changes through the recurrence.* [[lecture4b-ISPC.pdf#page=45|Source slide 45]].

## Reduction order and numerical results

**Supplementary connection to the lecture examples:** real-number addition is associative, but floating-point addition can lose that property through rounding. A tree reduction may therefore differ from a sequential accumulation even when both implement the same mathematical sum. Compare floating-point outputs with a stated tolerance; exact integer counting remains exact when the integer range is sufficient. [Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic*](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

For instance, in double precision, $(10^{16}+(-10^{16}))+1$ is $1$, while $10^{16}+((-10^{16})+1)$ can be $0$. This is a rounding example, not an algebraic difference in the intended mathematical result.

For benchmark comparisons, use the same inputs, term count, output accuracy requirement, and comparable optimization settings. Check the answers first, separate warm-up from measured runs, and report repeated timings. The presence of SIMD or higher CPU utilization alone does not establish speedup.

## Takeaways

- Gang-level SIMD and multicore tasks are distinct levels of parallelism.
- `uniform` and `varying` express whether values differ between instances.
- Independent outputs fit `foreach`; global outputs need communication or reduction.
- Correctness and numerical equivalence must be checked before benchmarking.

## Exam practice

These are original traces of the language ideas covered by the slides.

**1. Trace a reduction.** Four instances have local counters $[2,1,3,4]$ after `foreach`. What does `reduce_add(counter)` return? What changes if it is called while only lanes 1 and 3 are active?

> [!faq]- Worked solution
> With all four active, it returns the uniform value $10$. With only lanes 1 and 3 active, the reduction includes their values only, giving $1+4=5$. A reduction inside a varying branch is not automatically a reduction over the whole gang. Place the final count reduction after the conditional and loop, as in the note's kernel.

**2. Separate the parallelism levels.** A gang has eight logical instances. A row-task matrix multiplication launches 100 tasks on a four-worker runtime. Does this create 800 OS threads?

> [!faq]- Worked solution
> No. A task executes a gang's SPMD work using SIMD execution; the runtime schedules tasks on four workers. The task count, logical instance count, hardware vector width, and worker count are different quantities. Multiple tasks must be scheduled on each worker over time.

**3. Check a manual reduction.** In the page 31 four-lane trace, why is the final vector $[10,9,14,15]$ compatible with a correct result of 10? Would summing it be valid?

> [!faq]- Worked solution
> Only each group's first lane is required to hold that group's correct sum. After the final stage there is one group, led by lane 0. The other entries contain overlapping/duplicated intermediate contributions. `extract(counter,0)` returns 10; summing the final vector would return 48 and double-count contributions.

## Revision questions

1. Does one gang imply one thread per instance?
2. Why can the sine-loop index be uniform while its partial sums vary?
3. Does `foreach (i = 0 ... 2)` write index 2?
4. Why is the counting variable varying?
5. How does the task-based matrix example use both parallelism levels?
6. Why can Mandelbrot be independent per pixel but still inefficient in SIMD?

> [!faq]- Answer sketch
> 1. No; logical instances map to SIMD execution rather than separate OS threads.
> 2. All instances use the same iteration number but different input values.
> 3. No; the upper bound is excluded.
> 4. Each instance counts its own assigned values before reduction.
> 5. Tasks distribute rows across workers; foreach processes columns within each gang.
> 6. Unequal escape times leave some lanes inactive while others continue.
