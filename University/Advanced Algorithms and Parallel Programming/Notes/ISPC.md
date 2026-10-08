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

The slides compare manual low-level vector coding, C/C++ compiler auto-vectorization, and ISPC. Their statement that auto-vectorization is “disabled by default” should not be treated as universal: the behavior depends on the compiler and selected optimization flags.

Source: [[lecture4b-ISPC.pdf#page=5|Architecture and approaches, pp. 5–8]].

## Compilation and integration

ISPC compiles its source into object code and can generate a header exposing exported functions. A C/C++ application includes the generated interface and links the object code with its own code. Task-based code additionally needs an appropriate task runtime.

This lets the application delegate computational kernels while retaining its surrounding C/C++ structure. The compilation diagram is in [[lecture4b-ISPC.pdf#page=10|page 10]].

The deck links the [ISPC user guide](https://ispc.github.io/ispc.html) and [downloads](https://ispc.github.io/downloads.html). The user guide was consulted for the focused language clarifications below; examples in this note are study examples, not a compiled project.

## Gangs and program instances

An ISPC function runs as a **gang** of logical program instances. Each instance handles its own data while following the same program.

- `programIndex` identifies an instance within its gang.
- `programCount` is the gang size.

Do not hard-code a gang size into an algorithm unless the target-specific assumption is intentional. Logical gang size and hardware vector width are related but should not be casually equated for every target.

Source: [[lecture4b-ISPC.pdf#page=16|Gang execution, pp. 16–18]] · [[lecture4b-ISPC.pdf#page=28|Instance identifiers]].

## Uniform and varying data

| Qualifier | Meaning | Example in the sine kernel |
|---|---|---|
| `uniform` | One value for the gang | Array size, term count, common loop counter |
| `varying` | A value per instance | Current input, accumulated result |

The default for ordinary local scalar declarations is `varying`. A uniform input can participate in a varying expression, but assigning an arbitrary varying result to a uniform variable is invalid. These details are documented in the [official qualifier reference](https://ispc.github.io/ispc.html#uniform-and-varying-qualifiers).

“Varying/private” describes per-instance values; it does not imply that all memory referenced by an instance is isolated. Instances can access shared array storage and can race if their writes collide.

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

For input $[1,7,3,8,9,2,6,0]$ and threshold $5$, the final count is $4$. Every element is examined once, so counting work is linear in the input length, plus a small gang-level reduction.

Source: [[lecture4b-ISPC.pdf#page=26|Counting problem]] · [[lecture4b-ISPC.pdf#page=32|High-level reduction]].

### shuffle and extract

- `shuffle(value, index)` obtains another instance's value, with source indices that may vary by instance.
- `extract(value, index)` selects one instance's value using a uniform index and produces a uniform scalar.

These focused semantics were checked against the [official cross-instance reference](https://ispc.github.io/ispc.html#cross-program-instance-operations).

The manual reduction on page 31 doubles its group size each round. With four initial counts $[2,1,3,4]$, the first stage establishes pair totals at the first lane of each pair: lane 0 has 3, lane 2 has 7. The next stage establishes the total 10 at lane 0; `extract(counter, 0)` returns it. Other lanes need not contain a valid global sum.

This is the same binary reduction idea as [[PRAM#Reduction]]. If the gang size is not a power of two, bounds checks for source indices matter. Prefer a built-in reduction when it expresses the operation; use manual communication when a needed pattern is not provided.

The screenshot on page 33 shows overlapping timing ranges for the manual and built-in versions. It supports the example comparison, not a universal performance ranking.

Source: [[lecture4b-ISPC.pdf#page=25|Communication overview]] · [[lecture4b-ISPC.pdf#page=29|shuffle and extract, pp. 29–30]] · [[lecture4b-ISPC.pdf#page=31|Manual reduction]] · [[lecture4b-ISPC.pdf#page=33|Timings]].

## Tasks and multicore execution

An ISPC task is a unit of work executed by a gang. A task function is declared with `task` and returns `void`.

- `launch[n]` launches $n$ tasks.
- `taskIndex` identifies a task; `taskCount` gives the task count.
- `sync` waits for tasks launched by the current function.

A launching function implicitly waits before returning, as confirmed by the [official tasking reference](https://ispc.github.io/ispc.html#tasking-model). This allows the caller to use the completed output after the call returns.

The runtime maps tasks to worker threads. Tasks are not guaranteed to correspond one-to-one to physical cores. The deck uses the example runtime `examples/common/tasksys.cpp` and mentions OpenMP, TBB, and pthreads as other approaches to multicore parallelism.

Source: [[lecture4b-ISPC.pdf#page=36|Task model, pp. 36–37]] · [[lecture4b-ISPC.pdf#page=42|Multicore takeaway]].

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

Source: [[lecture4b-ISPC.pdf#page=39|Gang-only implementation]] · [[lecture4b-ISPC.pdf#page=40|Task implementation]] · [[lecture4b-ISPC.pdf#page=41|Resource usage]].

## Mandelbrot exercise

For each complex parameter $c$, define

$$
z_0=0,\qquad z_{k+1}=z_k^2+c.
$$

The Mandelbrot set consists of parameters for which the sequence stays bounded. The slide examples are:

- $c=1$: $0,1,2,5,\ldots$, which escapes.
- $c=-1$: $0,-1,0,-1,\ldots$, which remains bounded.

A renderer assigns each pixel a complex parameter and records an escape iteration, or a maximum iteration count. Different pixels are independent, making the exercise suitable for SIMD and task decomposition.

**Supplementary implementation reasoning:** nearby pixels may require very different iteration counts. Within a gang, this leads to inactive lanes waiting for longer-running lanes; across tasks, it can cause load imbalance. Use moderate-sized tiles and measure both computation time and load distribution. A finite maximum iteration count approximates the image and does not prove membership for every non-escaping sample.

Source: [[lecture4b-ISPC.pdf#page=43|Exercise and set definition, pp. 43–44]] · [[lecture4b-ISPC.pdf#page=45|Rendering diagram]].

## Takeaways

- Gang-level SIMD and multicore tasks are distinct levels of parallelism.
- `uniform` and `varying` express whether values differ between instances.
- Independent outputs fit `foreach`; global outputs need communication or reduction.
- Correctness and numerical equivalence must be checked before benchmarking.

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
