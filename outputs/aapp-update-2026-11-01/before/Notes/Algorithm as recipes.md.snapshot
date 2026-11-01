---
tags:
  - aapp
  - lecture
lecture: "2"
source: "[[lecture2-AlgorithmAsRecipe.pdf]]"
---
# Algorithm as recipes

[[AAPP Index|Course index]] · Previous: [[Course Introduction]] · Next: [[Divide and Conquer]]

## Overview

This review connects algorithms, input size, running time, sorting, and recurrences. Its guiding questions are **what grows with the input, and where is the bottleneck?** The deck itself carries a 2023–2024 label, although it is part of the supplied collection.

An algorithm is a finite, well-defined procedure that maps inputs to an output. Correctness and performance are separate questions: first establish that the answer is right, then determine the resources needed to obtain it.

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=3|Definition and recipe analogy, pp. 3–6]].

## Input size and running time

Let $n$ describe the input size and let $T(n)$ count operations in a specified model. For sorting, $n$ is usually the number of elements. For a graph, both vertex and edge counts may matter.

The carbonara analogy illustrates two ideas: a larger workload takes more time, and adding helpers only helps the parts that can be performed independently. A shared bottleneck can remain. [[PRAM]] later makes this distinction precise through work and the critical path.

Analysis abstracts away machine-specific timings. Benchmarking complements it by revealing constants, memory behavior, and the crossover between implementations. Neither replaces correctness.

### Turning an input into a cost function

The input size must describe the data the algorithm actually processes. A list with $n$ fixed-size keys has $n$ items; an $n\times n$ matrix has $n^2$ entries, even though its dimension is called $n$. An adjacency-list graph uses space proportional to $V+E$, whereas an adjacency matrix has $V^2$ entries. Calling all of these inputs “size $n$” without specifying the convention makes complexity comparisons ambiguous.

Next choose an operation: key comparisons for sorting, additions for a reduction, or edge examinations for a graph scan. A loop over every array element performs $n$ iterations. A nested loop with both indices ranging independently over $n$ values has $n^2$ iterations; a triangular loop with the inner index running only to the outer index has $1+2+\cdots+n=n(n+1)/2$. The latter is still quadratic even though it does about half as many iterations.

Under a unit-cost model, a bounded number of instructions per iteration changes the count by a constant factor. It cannot hide operations on arbitrarily large objects: comparing long strings or multiplying very large integers may itself require substantial work. The slides' arithmetic models assume the operands fit the chosen basic-operation convention.

### Best, average, and worst case

For inputs $x$ of size $n$:

$$
T_{\mathrm{best}}(n)=\min_{|x|=n}T(x),\qquad
T_{\mathrm{worst}}(n)=\max_{|x|=n}T(x).
$$

Average-case time is an expectation over a specified input distribution. Without a distribution, an average-case claim is incomplete. [[Randomized Algorithms#Where randomness comes from]] explains how this differs from averaging over random choices made by an algorithm.

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=10|Cases and asymptotic analysis, pp. 10–13]].

**One problem, three cost functions:** sequentially search for a key in a length-$n$ array. Finding it at the first position costs one comparison; finding it last or proving absence costs $n$. If the key is promised present and each position is equally likely, the average is

$$
\frac{1+2+\cdots+n}{n}=\frac{n+1}{2}.
$$

Thus the best case is $\Theta(1)$, while average and worst cases are both $\Theta(n)$ for this model. Changing the probability of absence or the distribution of positions changes the average. An “average” is not generally obtained by taking the midpoint between best and worst; this example happens to have evenly spaced, equally likely costs.

## Asymptotic notation

For eventually nonnegative functions $f$ and $g$:

| Notation | Meaning | Formal condition for sufficiently large $n$ |
|---|---|---|
| $f(n)=O(g(n))$ | Upper bound | $f(n)\le c g(n)$ for some $c>0$ |
| $f(n)=\Omega(g(n))$ | Lower bound | $f(n)\ge c g(n)$ for some $c>0$ |
| $f(n)=\Theta(g(n))$ | Tight bound | $c_1g(n)\le f(n)\le c_2g(n)$ for some $c_1,c_2>0$ |
| $f(n)=o(g(n))$ | Strictly smaller asymptotic order | For every $c>0$, eventually $f(n)<cg(n)$ |
| $f(n)=\omega(g(n))$ | Strictly larger asymptotic order | For every $c>0$, eventually $f(n)>cg(n)$ |

For example:

$$
3n^3+90n^2-5n+6046=\Theta(n^3),\qquad
2n^2=o(n^3).
$$

The first result follows by bounding the polynomial above and below by constant multiples of $n^3$ once $n$ is sufficiently large. The second follows because $2n^2/n^3=2/n\to0$.

### What the constants in a bound do

Consider $f(n)=3n^2+2n+7$ for integer $n\ge1$. Because $n\le n^2$ and $1\le n^2$,

$$
3n^2\le f(n)\le3n^2+2n^2+7n^2=12n^2.
$$

Here $c_1=3$, $c_2=12$, and $n_0=1$ prove $f(n)=\Theta(n^2)$. The constants need not be the smallest possible; they only have to be fixed independently of $n$. An upper bound $f(n)\le c(n)n$ with $c(n)=3n+9$ does **not** prove $O(n)$, because its supposed constant grows with input size.

For a contrasting example, $n^2\le n^3$ when $n\ge1$, so $n^2=O(n^3)$. It is not $\Theta(n^3)$: no fixed positive lower constant can satisfy $cn^3\le n^2$ for arbitrarily large $n$. Tightness requires both directions.

![[aapp-depth-recipes-bounds.png|720]]

*Original illustration of the explicit bound $3n^2\le3n^2+2n+7\le12n^2$ for $n\ge1$. The inequalities, rather than the finite plot alone, prove the asymptotic claim.*

### Comparing growth rates

For positive $g(n)$, the ratio $f(n)/g(n)$ is often a useful first check:

- Ratio tending to zero establishes $f=o(g)$.
- Ratio tending to a finite positive constant establishes $f=\Theta(g)$.
- Ratio tending to infinity establishes $f=\omega(g)$.

The converse for $\Theta$ need not give a limit: a bounded positive oscillating ratio can still establish a tight bound. Also, changing the logarithm's base multiplies it by a constant, because $\log_b n=\log_a n/\log_a b$ for fixed $a,b>1$.

For example, $\log n=o(n^{1/2})$ and $n\log n=o(n^2)$. When proving a bound, state the constants and the threshold beyond which the inequality holds; do not only say “drop small terms.” This is supplementary reasoning for the notation in slides 11–13.

> [!warning] Bounds and cases are different concepts
> $O$ does not mean “worst case,” and $\Omega$ does not mean “best case.” Each is a bound on whichever running-time function you are analyzing. A best-case function can have an $O$ bound; a worst-case function can have an $\Omega$ bound.

## Sorting and correctness

Sorting takes a sequence $\langle a_1,\ldots,a_n\rangle$ and produces a nondecreasing permutation. Both requirements matter: the output must be ordered **and** preserve the input multiset, including duplicate counts.

### Insertion sort

Maintain a sorted prefix. Take the next element, shift larger prefix elements one place to the right, and insert the element into the resulting gap.

![[aapp-lecture2-insertion-sort.png|720]]

*The green prefix is already sorted; the next key must be inserted into its correct position.* [[lecture2-AlgorithmAsRecipe.pdf#page=8|Source slide 8]].

```text
INSERTION-SORT(A)                 // zero-based indexing
    for j = 1 to length(A) - 1
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
```

**Invariant:** before iteration $j$, $A[0\ldots j-1]$ is sorted and contains the original prefix elements. Shifting preserves those elements, and inserting `key` produces a sorted prefix of length $j+1$. The invariant holds initially for one element and implies a sorted array at termination.

Example: with sorted prefix $[2,4,8,9]$ and next key $3$, shift $9,8,4$ and obtain $[2,3,4,8,9]$.

- Sorted input: constant work per outer iteration, so $\Theta(n)$ time.
- Reverse order: iteration $j$ shifts $j$ elements, so the total is

$$
\sum_{j=1}^{n-1}j=\frac{n(n-1)}2=\Theta(n^2).
$$

- **Supplementary:** under a uniformly random ordering of distinct values, each pair is inverted with probability $1/2$. Expected shifts are $n(n-1)/4$, giving $\Theta(n^2)$ expected time.

Insertion sort uses constant auxiliary space and is stable with the strict comparison `>`: equal keys are not shifted past each other.

**Supplementary worked count:** an inversion is a pair $i<j$ with $A[i]>A[j]$. Each rightward shift removes one inversion, so the total number of shifts is the initial inversion count. In $[4,1,3,2]$, the inversions are $(4,1),(4,3),(4,2),(3,2)$: four shifts in total. The outer-loop overhead remains linear even when there are no inversions. This explains why nearly sorted inputs can be cheap.

The linear best case and quadratic worst case should always be attached to the stated input conditions. The underlying operation-count approach is also explained in [MIT's insertion-sort and merge-sort lecture](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/resources/lecture-1-administrivia-introduction-analysis-of-algorithms-insertion-sort-mergesort/index.html).

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=8|Insertion sort and counting experiment, pp. 8–9]].

**Counting the actual comparison test:** the page 9 code increments `comp` only when `i >= 0` holds and `A[i] > key` is evaluated. For $[4,1,3,2]$, the three insertions make 1, 2 and 3 key comparisons respectively, while they shift 1, 1 and 2 elements. Total: six comparisons and four shifts. When a key reaches the beginning, the failed index test ends the loop without another key comparison. This is why “number of comparisons = shifts + one per insertion” is not universally exact.

Saving `key` before shifting is necessary because its original array cell can be overwritten. The variable is part of the correctness argument: shifting makes a gap, and the saved value fills it. The sorted-prefix invariant also says nothing about the untouched suffix being sorted; the outer loop gradually brings that suffix into the invariant.

### Merge sort

Split into two halves, recursively sort each half, and merge the results. Merging repeatedly selects the smaller first remaining element from the two sorted sequences.

![[aapp-lecture2-merge-sort.png|720]]

*Divide the array, solve the two halves, then merge the sorted results.* [[lecture2-AlgorithmAsRecipe.pdf#page=14|Source slide 14]].

```text
MERGE-SORT(A)
    if length(A) <= 1: return A
    split A into left and right
    return MERGE(MERGE-SORT(left), MERGE-SORT(right))
```

Correctness follows inductively: the recursive calls return sorted permutations of their halves; merging preserves all elements and puts them in order.

For powers of two, with constant-size base cases:

$$
T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n).
$$

Each recursion level has $\Theta(n)$ total merge work, and there are $\Theta(\log n)$ levels. Standard array implementations use $\Theta(n)$ auxiliary storage. Stability requires resolving equal keys in favor of the left half.

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=14|Merge sort and recursion tree, pp. 14–15]].

### Looking inside the merge

Merge $L=[2,5,8]$ and $R=[1,5,7]$. Compare the two first unconsumed values, append the smaller, and advance only that side's pointer:

| Compared heads | Chosen item | Output so far |
|---|---|---|
| 2 and 1 | Right 1 | $[1]$ |
| 2 and 5 | Left 2 | $[1,2]$ |
| 5 and 5 | Left 5 | $[1,2,5_L]$ |
| 8 and 5 | Right 5 | $[1,2,5_L,5_R]$ |
| 8 and 7 | Right 7 | $[1,2,5_L,5_R,7]$ |
| Right exhausted | Append left remainder | $[1,2,5_L,5_R,7,8]$ |

Why can the smaller head be emitted safely? Every remaining item behind either head is at least that head, because each input list is sorted. Therefore the smaller head is a smallest remaining item overall. This preserves the invariant that the output contains exactly the smallest items removed so far, in order. When one side is exhausted, the other is already sorted and can simply be appended.

Merging lengths $a,b$ moves exactly $a+b$ items and makes at most $a+b-1$ key comparisons when both are nonempty. It needs no fresh sorting inside the merge. Selecting the left equal key first preserves original cross-half order, which is how merge sort retains stability.

### Comparison

| Algorithm | Best case | Worst case | Standard auxiliary space |
|---|---|---|---|
| Insertion sort | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(1)$ |
| Merge sort | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n)$ |

For small or nearly sorted inputs, insertion sort can be competitive. The asymptotic comparison predicts growth, not a universal crossover size.

![[aapp-lecture2-growth-comparison.png|720]]

*The gap between quadratic and n log n growth widens as the input grows. The vertical axis uses a logarithmic scale.* [[lecture2-AlgorithmAsRecipe.pdf#page=16|Source slide 16]].

## Solving recurrences

Three useful approaches are a recursion tree, substitution, and the Master theorem. A recursion tree helps formulate a guess; substitution proves a bound by induction.

![[aapp-lecture2-recursion-tree.png|720]]

*At each level, the total merge work is proportional to n. There are logarithmically many levels.* [[lecture2-AlgorithmAsRecipe.pdf#page=15|Source slide 15]].

**Supplementary substitution proof:** take powers of two, $T(1)=d>0$, and $T(n)=2T(n/2)+cn$ with $c>0$. Prove $T(n)\le Kn\log_2n+Dn$ using $K\ge c$ and $D\ge d$.

The base case gives $T(1)=d\le D$. For the induction step,

$$
\begin{aligned}
T(n)&\le 2\left(K\frac n2\log_2\frac n2+D\frac n2\right)+cn\\
&=Kn\log_2n+Dn+(c-K)n\\
&\le Kn\log_2n+Dn.
\end{aligned}
$$

This makes the base-case constant explicit. For this exact recurrence, expanding levels gives $T(n)=dn+cn\log_2n$, supplying both the upper and lower bound. Hence $T(n)=\Theta(n\log n)$. For a nonrecursive term specified only as $\Theta(n)$, use constant upper and lower multiples of $n$ rather than asserting an exact equality.

### Reading a recursion tree level by level

For $T(n)=aT(n/b)+f(n)$, depth $\ell$ has $a^\ell$ subproblems, each of size $n/b^\ell$. The **total** nonrecursive work at that depth is therefore $a^\ell f(n/b^\ell)$. Recursion reaches constant size when $n/b^h=1$, giving $h=\log_b n$. The number of leaves is $a^h=a^{\log_b n}=n^{\log_ba}$: this is where the Master theorem's reference term comes from.

For merge sort on eight values with nonrecursive work equal to the subproblem size, the internal levels have costs $8$, $2\cdot4=8$, and $4\cdot2=8$. There are eight constant-size leaves. With $T(1)=1$, the total is $8+8+8+8=32$. The logarithmic number of levels multiplies linear work **across a whole level**, not the work of one selected recursive path.

The three Master cases ask where most work accumulates: near the leaves, spread across levels, or near the root. This is an interpretation of the theorem, while the polynomial-gap and regularity conditions below are what justify choosing a case.

### Master theorem

For

$$
T(n)=aT(n/b)+f(n),\qquad a\ge1,\ b>1,
$$

compare $f(n)$ with $n^d$, where $d=\log_b a$.

| Case | Condition | Result |
|---|---|---|
| 1 | $f(n)=O(n^{d-\varepsilon})$ for some $\varepsilon>0$ | $T(n)=\Theta(n^d)$ |
| 2 | $f(n)=\Theta(n^d\log^k n)$ for $k\ge0$ | $T(n)=\Theta(n^d\log^{k+1}n)$ |
| 3 | $f(n)=\Omega(n^{d+\varepsilon})$ and $af(n/b)\le cf(n)$ for some $c<1$, eventually | $T(n)=\Theta(f(n))$ |

In Cases 1 and 3, the difference must be polynomial. Merely being smaller or larger is insufficient. In Case 3, do not omit the regularity condition.

**Application checklist:** $a,b$ must be constants, and the nonrecursive cost must be eventually positive. Identify $a,b,f(n)$, compute $d=\log_ba$, and justify a case. If a condition fails, use a recursion tree or substitution. In standard balanced recurrences, floors and ceilings do not alter these asymptotic results. This is the form used in [MIT's Master theorem practice sheet](https://people.csail.mit.edu/thies/6.046-web/master.pdf).

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=18|Methods and Master theorem, pp. 18–21]].

### Worked examples

For $T(n)=4T(n/2)+f(n)$, the reference term is $n^{\log_2 4}=n^2$:

- $f(n)=n$: Case 1, giving $\Theta(n^2)$.
- $f(n)=n^2$: Case 2 with $k=0$, giving $\Theta(n^2\log n)$.
- $f(n)=n^3$: Case 3; $4(n/2)^3=n^3/2$, so regularity holds and the result is $\Theta(n^3)$.
- $f(n)=n^2/\log n$: none of the stated cases applies. It is smaller than $n^2$, but not polynomially smaller.

**Supplementary solution to the last example:** take $n=2^m$ and stop recursion at a constant size greater than one, avoiding $\log1$. At level $\ell$, the total nonrecursive work is proportional to

$$
4^\ell\frac{(n/2^\ell)^2}{\log_2(n/2^\ell)}
=\frac{n^2}{m-\ell}.
$$

Summing levels gives $\Theta(n^2H_m)=\Theta(n^2\log\log n)$, with $\Theta(n^2)$ leaf work. This illustrates why “Master theorem does not apply” is not the same as “the recurrence cannot be solved.”

## Mini-labs and shortest paths

The slides propose counting insertion-sort comparisons and shifts, benchmarking insertion versus merge sort, and computing recurrence values. Predict the growth first, then test sorted, random, and reversed data. Record the input size, distribution, compiler settings, and multiple timing runs.

For $T(1)=1$ and $T(n)=2T(n/2)+n$ at powers of two, the exact value is $n(1+\log_2n)$. Consequently $T(n)/(n\log_2 n)$ approaches $1$.

The Dijkstra fragment illustrates a graph problem whose input size is described by vertices and edges. Relaxing $(u,v)$ means replacing `dist[v]` when `dist[u] + weight(u,v)` is smaller.

> [!note] Supplementary clarification of the slide code
> Dijkstra requires nonnegative edge weights. In the lazy priority-queue version, add `if (d != dist[u]) continue;` immediately after popping an entry. This avoids rescanning edges for obsolete distances. An indexed binary heap with decrease-key gives $O((V+E)\log V)$; the lazy heap can have $O(E)$ entries and is bounded by $O(V+(E+1)\log(E+2))$, including initialization. For simple graphs this is commonly expressed with a $\log V$ factor. The distinction and stale-entry check are explained in the [implementation's own documentation](https://cp-algorithms.com/graph/dijkstra_sparse.html#priority_queue).

Relaxations may expose parallel work, but dependencies between distance updates and selecting the next vertex still need a correctness argument.

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=17|Benchmark experiment]] · [[lecture2-AlgorithmAsRecipe.pdf#page=22|Recurrence and Dijkstra mini-lab]].

### Understanding the Dijkstra fragment

A tentative distance is the length of the best source-to-vertex path discovered so far. Initialize the source to 0 and other vertices to infinity. The priority queue repeatedly selects the smallest tentative distance; relaxation asks whether going through that vertex improves a neighbor's current estimate.

For edges $s\to a$ of weight 4, $s\to b$ of weight 1, and $b\to a$ of weight 2, processing $s$ discovers distances 4 and 1. Processing $b$ next improves $a$ to $1+2=3$. In a lazy queue, both `(4,a)` and `(3,a)` can now be present. The distance-3 entry is current; the distance-4 entry is stale and should be skipped when popped.

Nonnegative weights are needed for the greedy finalization argument: extending a route cannot make it cheaper by traversing an unseen negative edge. The queue orders discovered candidates, rather than magically knowing all shortest paths. This explanation stays within the shortest-path fragment on [[lecture2-AlgorithmAsRecipe.pdf#page=22|slide 22]]; it is not a separate treatment of graph algorithms.

### What the recurrence mini-lab measures

The function on page 22 **computes the numerical value** of a recurrence: `2*T(n/2) + n`. The multiplication by two does not call `T` twice. Evaluating this code has one recursive call per level, even though its returned value is $n(1+\log_2n)$ on powers of two. Do not confuse a program that evaluates a mathematical cost formula with a program whose own runtime equals that formula.

For an actual sorting benchmark, restore the same unsorted input before each algorithm's timed run; otherwise the second algorithm may receive an already sorted array. Keep copying and data generation outside the timed region if the intended measurement is sorting alone. Test the sorted output and preserved multiset, since a wrong program can appear fast. The slide's `bench` reports a mean over repetitions; a median is an alternative robust summary, not what that particular code computes.

## Takeaways

- Define the input size and operation model before writing a complexity bound.
- A sorting result must preserve the multiset as well as order it.
- Constants matter in measurements; dominant terms matter for asymptotic growth.
- Recurrences express both recursive and nonrecursive work.

## Exam practice

These are original practice questions based on the supplied deck, not past exam questions.

**1. Trace and count.** Sort $[4,1,3,2]$ by insertion sort. Count element shifts, then explain why the count is not the same as elapsed time.

> [!faq]- Worked solution
> The arrays after each insertion are $[1,4,3,2]$, $[1,3,4,2]$, and $[1,2,3,4]$. Shift counts are $1,1,2$, totaling $4$. Time also includes comparisons, key writes, loop control, and machine-dependent costs.

**2. Select a recurrence case.** Solve $T(n)=3T(n/2)+n^2$. Then explain why simply calling the nonrecursive term “larger” is insufficient.

> [!faq]- Worked solution
> The reference exponent is $d=\log_2 3\approx1.585$. The gap $2-d>0$ is polynomial. Regularity holds because $3(n/2)^2=(3/4)n^2$. Case 3 gives $\Theta(n^2)$. A positive polynomial gap and regularity are both required, rather than just a qualitative comparison.

**3. Explain a numerical recurrence experiment.** With $T(1)=1$ and $T(n)=2T(n/2)+n$, compute $T(8)$. Does the slide's code `return 2*T(n/2)+n` itself execute two recursive calls?

> [!faq]- Worked solution
> $T(2)=4$, $T(4)=12$, $T(8)=32$. The code executes one recursive call and doubles its result; on powers of two its own call depth is logarithmic. A returned cost value of 32 does not mean the evaluator executed 32 elementary steps.

## Revision questions

1. Why is $n^2$ both $O(n^3)$ and $\Theta(n^2)$?
2. What makes insertion sort quadratic on reversed input?
3. Why does merge sort do linear work at each level?
4. Why does $n^2/\log n$ not fit Case 1 for reference term $n^2$?
5. What assumption is needed for an average-case analysis?

> [!faq]- Answer sketch
> 1. Upper bounds need not be tight; $n^3$ is a valid larger bound.
> 2. Every new key must move past the entire sorted prefix.
> 3. All subarrays at one level together contain $n$ elements.
> 4. The ratio decreases logarithmically rather than as a fixed power of $n$.
> 5. A probability distribution over inputs.
