---
tags:
  - aapp
  - lecture
lecture: "8"
source: "[[lecture8-Select-ith.pdf]]"
---
# Selection and Order Statistics

[[AAPP Index|Course index]] · Previous: [[Sorting]] · Next supplied lecture: [[Primality Testing and Cryptosystems]] · Prerequisites: [[Sorting#Quicksort and partitioning]] · [[Randomized Algorithms]]

## Overview

Selection finds one element of a specified rank. It does not need to put every element in order. The deck first studies minimum and maximum, then develops randomized selection with linear expected time and deterministic selection with linear worst-case time. The supplied cover is labeled 2026–2027; no lecture 9 deck is present.

Source: [[lecture8-Select-ith.pdf#page=3|Problem and extreme ranks, pp. 3–8]] · [[lecture8-Select-ith.pdf#page=9|Randomized selection, pp. 9–24]] · [[lecture8-Select-ith.pdf#page=25|Deterministic selection, pp. 25–36]].

## Ranks and the cost of sorting first

Assume $n\ge1$ distinct, comparable numbers and a **one-based rank** $1\le i\le n$. The $i$th order statistic is the element larger than exactly $i-1$ input elements. Rank 1 is the minimum and rank $n$ the maximum. For even $n$, the lower and upper medians have ranks $\lfloor(n+1)/2\rfloor$ and $\lceil(n+1)/2\rceil$; a statistical convention that averages them is a different output specification.

Sorting with merge sort and returning position $i$ costs $\Theta(n\log n)$. This is a valid solution, but the sorting lower bound in [[Sorting#Comparison-sorting lower bound]] requires distinguishing every ordering. Selection asks for less information, so that lower bound does not automatically apply. The algorithms here use comparisons and constant-time array access; no integer-key assumption is required.

With duplicate keys, ranks can instead be defined by positions in a sorted multiset. The algorithms can be adapted, but the deck's probability and pivot-rank arguments explicitly assume distinct elements. Keep that assumption visible when using their bounds.

## Minimum and simultaneous minimum–maximum

To find a minimum, retain the smallest value seen so far. Initially it is $A[1]$; compare each remaining item against it and update when necessary. After processing a prefix, the retained value is its minimum, proving correctness by induction. Exactly $n-1$ comparisons are made.

Why can no comparison algorithm always use fewer? In a tournament where smaller wins, each item except the eventual minimum must lose at least once before it can be ruled out. One comparison supplies one loss, so $n-1$ are necessary. The scan is optimal in comparison count. Maximum is symmetric.

Finding both independently would use $2n-2$ comparisons. Pairing shares work: first compare the two members of a pair; only its smaller member can improve the current minimum, and only its larger member can improve the maximum. Thus each subsequent pair costs three comparisons instead of four.

```text
MIN-MAX(A[1..n])
    require n >= 1
    if n is odd
        lo = hi = A[1]
        j = 2
    else
        compare A[1] and A[2]
        lo = smaller; hi = larger
        j = 3
    while j + 1 <= n
        compare A[j] and A[j+1]
        small = smaller; large = larger
        compare small with lo; update lo if smaller
        compare large with hi; update hi if larger
        j += 2
    return (lo, hi)
```

The initialization leaves an even number of unprocessed elements. The invariant says `lo` and `hi` are the extrema of all processed pairs and initial elements. Comparing each pair as described preserves it.

| Input size | Initialization | Remaining pairs | Total comparisons |
|---|---|---|---|
| Odd $n$ | 0 | $(n-1)/2$ | $3(n-1)/2$ |
| Even $n$ | 1 | $(n-2)/2$ | $1+3(n-2)/2=3n/2-2$ |

For $[7,2,9,4,1,8]$, initialize $(lo,hi)=(2,7)$ after one comparison. Pair $(9,4)$ updates the maximum to 9 using three comparisons. Pair $(1,8)$ updates the minimum to 1 using three more: seven comparisons total instead of ten.

> [!warning] Slide wording on page 7
> “Less than $3\lfloor n/2\rfloor$” is not strict for odd $n$: the printed odd-case count equals that value. Use the two exact formulas above. Time remains $\Theta(n)$ and auxiliary space $O(1)$.

Source: [[lecture8-Select-ith.pdf#page=4|Minimum lower bound and paired extrema, pp. 4–7]].

## Randomized selection

Partition uses the same invariant as quicksort: after placing a pivot at index $r$, all elements before it are smaller and all elements after it are larger. If the current inclusive interval is $A[p..q]$, the pivot's **local rank** is $k=r-p+1$.

There are three cases. If $i=k$, return the pivot. If $i<k$, the requested element is in the left region with unchanged local rank $i$. If $i>k$, discard the $k$ elements consisting of the left region and pivot; its new rank in the right region is $i-k$.

```text
RAND-SELECT(A, p, q, i)
    require 1 <= i <= q-p+1
    if p == q: return A[p]
    j = fresh uniform random integer in [p, q]
    swap A[p], A[j]
    r = PARTITION(A, p, q)      // first-element pivot from Sorting
    k = r - p + 1
    if i == k: return A[r]
    if i < k: return RAND-SELECT(A, p, r-1, i)
    return RAND-SELECT(A, r+1, q, i-k)
```

Call with `p=1, q=n`. Bounds describe a view of the original array; copying the remaining values is unnecessary. Correctness follows from partition's rank guarantee and induction on the smaller remaining interval. The algorithm changes the array but need not sort either discarded region.

### Complete rank-update trace

The deck starts with $[6,10,13,5,8,3,2,11]$ and asks for rank 7. Suppose the first random pivot is 6. Its completed partition is

$$
[2,5,3,\boxed6,8,13,10,11].
$$

The pivot has rank 4, so recurse on $[8,13,10,11]$ with local rank $7-4=3$. To finish this illustrative execution, suppose the next pivot is 10. Partitioning that region produces $[8,\boxed{10},13,11]$. Its local rank is 2. Recurse on $[13,11]$ with rank $3-2=1$; choosing pivot 13 puts 11 before it and sends the search to the singleton 11. Return 11. The full sorted order is $[2,3,5,6,8,10,11,13]$, confirming rank 7.

![[aapp-lecture8-selection-partition.png|720]]

*The supplied first partition discards the pivot and all smaller keys. The remaining request is rank 3 within the right region; the rest of the trace above is supplementary.* [[lecture8-Select-ith.pdf#page=10|Source slide 10]].

### Worst case and the difference from quicksort

Quicksort recursively processes both sides. Selection processes at most one. If each selected side has at most $9n/10$ items, the work is bounded by the geometric series $cn+c(9n/10)+\cdots=O(n)$.

However, if each pivot is extreme and the requested rank remains in the other region, sizes decrease only by one:

$$
T(n)=T(n-1)+\Theta(n)=\Theta(n^2).
$$

Randomization makes these executions unlikely; it does not make them impossible. Selection is **Las Vegas**: correctness is certain, runtime is random. It never returns an approximate rank to meet a deadline.

## Why expected selection time is linear

Fix the input and requested rank before sampling pivots. Distinctness makes every pivot rank equiprobable. If the split has $k$ smaller elements and $n-1-k$ larger elements, the next size is at most

$$
M_k=\max(k,n-1-k).
$$

For rigor, let $F(n)$ bound the largest expected cost among all size-$n$ inputs and target ranks, and suppose the nonrecursive work is at most $an$. Use strong induction $F(s)\le Cs$ for all $s<n$. Conditional on any pivot, fresh recursive choices have expected cost at most $CM_k$, even if the requested side is smaller or selection terminates at the pivot. Therefore

$$
F(n)\le an+\frac Cn\sum_{k=0}^{n-1}M_k.
$$

For even $n=2m$, the maxima $m,m+1,\ldots,2m-1$ each occur twice:

$$
\sum_k M_k=2\sum_{j=m}^{2m-1}j=3m^2-m\le\frac34n^2.
$$

For odd $n=2m+1$, $m$ occurs once and larger values twice:

$$
\sum_kM_k=m+2\sum_{j=m+1}^{2m}j=3m^2+2m\le\frac34n^2.
$$

Consequently

$$
F(n)\le an+\frac34Cn
=Cn-\left(\frac C4-a\right)n\le Cn
$$

for $C\ge4a$, enlarged to cover the base cases. This proves $O(n)$ expected time on every fixed distinct-key input. The first partition already performs $n-1$ comparisons, giving the matching $\Omega(n)$ for this implementation.

The intuition is a **budget**: recursive work consumes at most three quarters of the proposed linear budget in expectation, leaving one quarter for partitioning. A single execution can still have many bad pivots.

> [!note] Reading the slide recurrence
> Pages 13–19 replace the actual chosen side with the larger side as an upper-bound device. The resulting relation should be read as an inequality for a dominating cost, not an exact recurrence for every requested rank. The rendered pages 22–23 contain outer parentheses: $Cn-(Cn/4-\Theta(n))$. Their algebra has no sign error.

The conditional argument above is a supplementary expansion of [[lecture8-Select-ith.pdf#page=12|the indicator/substitution proof, pp. 12–23]]. For an independent explanation of randomized and deterministic selection, see [CMU 15-451, Lecture 1, §§1.3–1.4](https://www.cs.cmu.edu/~15451-s20/lectures/lec1.pdf). The equal-size Master theorem does not directly solve this expectation over many alternative child sizes.

An iterative implementation replaces the one recursive call with updates of $(p,q,i)$, using $O(1)$ auxiliary storage in addition to in-place partitioning. The literal recursive version can have $O(n)$ stack depth in a bad execution.

## Deterministic selection with median of medians

To guarantee progress on every input, construct a pivot known to have many keys on each side. It need not be the exact median of all $n$ keys.

Use the deck's convention of **full groups of five**: form $g=\lfloor n/5\rfloor$ full groups, leave at most four leftovers out of pivot construction, and retain them for the final partition. Sort each constant-size group to obtain its third element. Recursively select a median of these $g$ group medians. Partition the entire input around this pivot and recurse on the requested side as before.

```text
SELECT(A, i)
    if length(A) < 50
        sort this bounded-size instance and return its ith element
    form floor(length(A)/5) full groups of five
    M = the median of each full group
    x = SELECT(M, ceil(length(M)/2))
    partition all of A around x; let k be x's rank
    if i == k: return x
    if i < k: return SELECT(left region, i)
    return SELECT(right region, i-k)
```

The small-instance sort has bounded cost because its size is below a fixed threshold. This does not claim sorting an arbitrarily growing input is constant time.

### Counting the elements that can be discarded

At least $\lfloor g/2\rfloor=\lfloor n/10\rfloor$ group medians are at most $x$. In each such group, that median and the two smaller elements are at most $x$. Since groups are disjoint, at least $3\lfloor n/10\rfloor$ input elements are at most $x$. The symmetric count supplies at least as many at least $x$.

The pivot itself can appear in both inclusive counts; that is harmless. For example, to bound the number **strictly larger** than $x$, subtract the count at most $x$ from $n$. For $n\ge50$,

$$
3\lfloor n/10\rfloor\ge n/4,
$$

so either recursive side has size at most $3n/4$. One way to verify the threshold is to check $50\le n\le59$ directly, then use $3\lfloor n/10\rfloor\ge3n/10-3\ge n/4$ for $n\ge60$.

![[aapp-lecture8-median-of-medians.png|720]]

*Each column is a sorted group. Counting three certified values in each qualifying column gives a constant-fraction discard guarantee; the horizontal arrangement orders group medians, not every input element.* [[lecture8-Select-ith.pdf#page=32|Source slide 32]].

For a concrete pivot example, five sorted groups are $[1,6,11,16,21]$, $[2,7,12,17,22]$, $[3,8,13,18,23]$, $[4,9,14,19,24]$, and $[5,10,15,20,25]$. Their medians are $11,12,13,14,15$, giving pivot 13. Nine certified values are at most 13 from the first three groups; nine are at least 13 from the last three. The actual partition has twelve smaller and twelve larger values. The proof only needs a guaranteed lower count, which may be weaker than the actual split. This size-25 example illustrates pivot construction; the pseudocode's base-case branch would sort it directly.

### Worst-case recurrence and its solution

Pivot selection is itself recursive and must be charged. Group processing and partitioning cost $O(n)$, so a monotone worst-case upper envelope satisfies

$$
T(n)\le T(\lfloor n/5\rfloor)+T(\lfloor3n/4\rfloor)+an.
$$

Under $T(s)\le Cs$, the right side is at most

$$
\frac C5n+\frac{3C}{4}n+an
=\frac{19}{20}Cn+an\le Cn
$$

for $C\ge20a$ and sufficiently large base-case coverage. Thus worst-case time is $\Theta(n)$. The fractions sum to less than one, leaving linear slack for local work. This is an unequal-subproblem recurrence; use substitution or a recursion-tree argument rather than the standard equal-size Master theorem.

Source: [[lecture8-Select-ith.pdf#page=30|Discard counts and analysis, pp. 30–36]]. Page 35 also uses outer parentheses correctly.

### Why the simple proof uses five rather than three

Groups of three yield two certified elements per qualifying group. Ignoring rounding, the analogous recurrence is

$$
T(n)\le T(n/3)+T(2n/3)+O(n).
$$

The child fractions sum to one, so this simple argument gives an $O(n\log n)$ upper bound, without the slack needed for the linear proof. It does **not** prove every conceivable selection algorithm using triples is non-linear. Groups of five are a sufficient choice for the supplied construction; they are not the only group size that can work.

For duplicates, a supplementary robust implementation partitions into $<x$, $=x$, and $>x$. Return $x$ when the desired rank lies in the equal block, otherwise adjust the rank by the whole discarded block. This prevents an all-equal input from defeating progress.

## Comparison and takeaways

| Method | Correctness | Time guarantee | Main reason |
|---|---|---|---|
| Sort then index | Exact | $\Theta(n\log n)$ worst case with merge/heapsort | Computes the entire order |
| Randomized selection | Exact; Las Vegas | $\Theta(n)$ expected, $\Theta(n^2)$ worst case | Uniform pivots, one selected side |
| Median-of-medians selection | Exact; deterministic | $\Theta(n)$ worst case | Guaranteed constant-fraction discard |

The deck's practical preference for randomized selection concerns overhead, not a universal timing result. The deterministic algorithm buys a stronger guarantee by doing more pivot-construction work.

## Exam practice

These are original exercises. Retrieved questions remain unanswered in [[Past Exam Question Bank#Selection and order statistics]].

**1. Local rank versus array index.** A call on $A[5..13]$ requests local rank 6. Its pivot ends at index 8. Which interval and rank are passed next?

> [!faq]- Worked solution
> The pivot's local rank is $8-5+1=4$. Since $6>4$, recurse on $A[9..13]$ with rank $6-4=2$. Passing rank 6 or subtracting the absolute index 8 would violate the subproblem specification.

**2. Paired extrema.** Compute exact comparison counts for finding minimum and maximum together for $n=9$ and $n=10$. Compare independent scans.

> [!faq]- Worked solution
> Nine items require $3(8)/2=12$ comparisons rather than 16. Ten require $1+3(8)/2=13$ rather than 18. Odd initialization consumes one element; even initialization consumes two with one comparison.

**3. Read the deterministic recurrence.** For $n=100$, how large is the group-median subproblem? Give a safe bound on the target-side subproblem using the actual certified count, then using the lecture's $3n/4$ simplification.

> [!faq]- Worked solution
> There are 20 full groups. At least $3\lfloor100/10\rfloor=30$ elements lie on each inclusive side of the pivot. Thus either strict side has at most $100-30=70$ elements. The simplified bound is 75. Both recursive costs must be included: selecting the pivot does not happen for free.

**4. Diagnose an expected-time claim.** A student says that replacing two quicksort calls with one makes selection linear in every execution. Give a counterexample and explain what the expectation proof adds.

> [!faq]- Worked solution
> Request the maximum and repeatedly choose the minimum pivot. Sizes are $n,n-1,\ldots,1$, giving quadratic work despite one recursive call. Uniform random pivot ranks make the average dominating child size at most $3n/4$; this yields linear expected work but retains the bad execution.

## Revision questions

1. Why does selection avoid the comparison-sorting lower bound?
2. Why is right-recursion rank $i-k$?
3. What probability space is used in the expected bound?
4. Why must deterministic selection charge two recursive calls?
5. Is the median of group medians necessarily the input median?
6. What changes when many keys are equal?

> [!faq]- Answer sketch
> 1. It need not distinguish all sorted orders. 2. The left region and pivot account for $k$ earlier ranks. 3. Fresh internal pivot choices, with fixed input and requested rank. 4. One constructs the pivot and one selects the target. 5. No; the proof only guarantees a sufficiently central rank. 6. The distinct-rank probability argument changes; a three-way partition handles an equal block explicitly.
