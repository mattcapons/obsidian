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

### Best, average, and worst case

For inputs $x$ of size $n$:

$$
T_{\mathrm{best}}(n)=\min_{|x|=n}T(x),\qquad
T_{\mathrm{worst}}(n)=\max_{|x|=n}T(x).
$$

Average-case time is an expectation over a specified input distribution. Without a distribution, an average-case claim is incomplete. [[Randomized Algorithms#Where randomness comes from]] explains how this differs from averaging over random choices made by an algorithm.

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=10|Cases and asymptotic analysis, pp. 10–13]].

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

> [!warning] Bounds and cases are different concepts
> $O$ does not mean “worst case,” and $\Omega$ does not mean “best case.” Each is a bound on whichever running-time function you are analyzing. A best-case function can have an $O$ bound; a worst-case function can have an $\Omega$ bound.

## Sorting and correctness

Sorting takes a sequence $\langle a_1,\ldots,a_n\rangle$ and produces a nondecreasing permutation. Both requirements matter: the output must be ordered **and** preserve the input multiset, including duplicate counts.

### Insertion sort

Maintain a sorted prefix. Take the next element, shift larger prefix elements one place to the right, and insert the element into the resulting gap.

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

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=8|Insertion sort and counting experiment, pp. 8–9]].

### Merge sort

Split into two halves, recursively sort each half, and merge the results. Merging repeatedly selects the smaller first remaining element from the two sorted sequences.

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

### Comparison

| Algorithm | Best case | Worst case | Standard auxiliary space |
|---|---|---|---|
| Insertion sort | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(1)$ |
| Merge sort | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n)$ |

For small or nearly sorted inputs, insertion sort can be competitive. The asymptotic comparison predicts growth, not a universal crossover size.

## Solving recurrences

Three useful approaches are a recursion tree, substitution, and the Master theorem. A recursion tree helps formulate a guess; substitution proves a bound by induction.

**Supplementary substitution example:** for $T(n)=2T(n/2)+cn$, assume $T(n/2)\le K(n/2)\log_2(n/2)$. Then

$$
T(n)\le Kn(\log_2 n-1)+cn
\le Kn\log_2n
$$

when $K\ge c$. A suitable base-case adjustment completes the upper bound. The level-cost argument supplies the matching lower bound.

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
> Dijkstra requires nonnegative edge weights. For the lazy priority-queue implementation shown, skip a popped entry when its stored distance differs from the current `dist[u]`. Otherwise stale entries can repeat edge scans, so the usual efficient implementation analysis does not directly describe the fragment as printed. A heap implementation with decrease-key has the familiar $O((V+E)\log V)$ bound; lazy heaps are commonly analyzed using $\log E$ instead.

Relaxations may expose parallel work, but dependencies between distance updates and selecting the next vertex still need a correctness argument.

Source: [[lecture2-AlgorithmAsRecipe.pdf#page=17|Benchmark experiment]] · [[lecture2-AlgorithmAsRecipe.pdf#page=22|Recurrence and Dijkstra mini-lab]].

## Takeaways

- Define the input size and operation model before writing a complexity bound.
- A sorting result must preserve the multiset as well as order it.
- Constants matter in measurements; dominant terms matter for asymptotic growth.
- Recurrences express both recursive and nonrecursive work.

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
