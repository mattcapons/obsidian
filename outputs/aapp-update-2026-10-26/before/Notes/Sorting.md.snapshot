---
tags:
  - aapp
  - lecture
lecture: "7"
source: "[[lecture7-Sort.pdf]]"
---
# Sorting

[[AAPP Index|Course index]] · Previous: [[Minimum Cut]] · Prerequisites: [[Algorithm as recipes]] · [[Divide and Conquer]] · [[Randomized Algorithms]]

## Overview

The first half of this deck develops quicksort and its expected-time analysis. The second proves a lower bound for **comparison sorting**, then explains how counting sort and radix sort exploit integer representations to work outside that model. The supplied deck carries a 2021–2022 label; its inclusion does not establish a newer exam-specific scope statement.

Source: [[lecture7-Sort.pdf#page=4|Quicksort, pp. 4–49]] · [[lecture7-Sort.pdf#page=50|Lower bounds and integer sorting, pp. 50–88]]. Pages 89–96 contain historical background on punched cards.

## Quicksort and partitioning

Quicksort sorts an array in place by selecting a pivot, partitioning around it, recursively sorting the two sides, and doing no substantial combine step. This reverses the distribution of work in merge sort, where splitting is easy but combining is linear.

The lecture uses **inclusive, one-based bounds** and the first element as pivot. Keep this convention when tracing its code:

```text
PARTITION(A, p, q)
    x = A[p]
    i = p
    for j = p + 1 to q
        if A[j] <= x
            i = i + 1
            swap A[i], A[j]
    swap A[p], A[i]
    return i

QUICKSORT(A, p, r)
    if p < r
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q - 1)
        QUICKSORT(A, q + 1, r)
```

Call `QUICKSORT(A, 1, n)`. A subarray of zero or one element is already sorted.

### Partition invariant and correctness

At the start of iteration $j$:

- $A[p]=x$ is the pivot.
- $A[p+1\ldots i]\le x$.
- $A[i+1\ldots j-1]>x$.
- $A[j\ldots q]$ is unexamined.

Initially both examined regions are empty. If the next item is at most $x$, expanding the low region and swapping puts it there while preserving the high region. Otherwise only the high region grows. After the loop, swapping the pivot into position $i$ puts it between the two regions. Swaps preserve the input multiset. Each recursive call excludes the pivot, hence shrinks; induction on subarray length proves sorting correctness.

**Boundary clarification:** the slide's high-region label $\ge x$ is a valid weaker claim, but the actual `<=` test makes this region strictly $>x$. The code sorts duplicates correctly, although its randomized performance analysis below assumes distinct keys.

Source: [[lecture7-Sort.pdf#page=5|Design and partition invariant, pp. 5–6]] · [[lecture7-Sort.pdf#page=19|Recursive pseudocode and distinctness assumption, pp. 19–20]].

### Why the partition swap does not skip an unknown item

When $A[j]\le x$, incrementing $i$ selects the first position of the old high region. If that region was nonempty, swapping moves its known-large value to position $j$ while putting the newly discovered small value into the low region. The item moved to $j$ has already been classified, so advancing $j$ does not skip unexamined data. If the high region was empty, the swap is with the same position and is harmless.

The final swap exchanges the pivot with the last low-region element. Afterward, the pivot has all low values before it and all strictly larger values after it. With distinct keys it is at its unique sorted rank; with ties, it occupies a valid boundary position among equal keys. Correctness does not require the array to stay stable, and these long-distance swaps generally do not preserve equal-record order.

### Worked partition trace

For $[6,10,13,5,8,3,2,11]$, the pivot is 6. Only encounters with 5, 3, and 2 enlarge the low region:

| Event | Array after the swap | $i$ |
|---|---|---|
| Start | $[6,10,13,5,8,3,2,11]$ | 1 |
| Read 5 | $[6,5,13,10,8,3,2,11]$ | 2 |
| Read 3 | $[6,5,3,10,8,13,2,11]$ | 3 |
| Read 2 | $[6,5,3,2,8,13,10,11]$ | 4 |
| Final pivot swap | $[2,5,3,6,8,13,10,11]$ | 4 |

The returned pivot index is 4. Neither side is necessarily sorted yet. Partition makes seven key comparisons, one for each non-pivot element, and takes $\Theta(n)$ time on $n$ elements with $O(1)$ auxiliary space.

![[aapp-lecture7-partition.png|720]]

*The slide's completed partition trace places the pivot at its final sorted position.* [[lecture7-Sort.pdf#page=18|Source slide 18]].

## Recursion shape and running time

### Worst case

For distinct sorted or reverse-sorted input and a first-element pivot, each partition separates zero elements from $n-1$ elements:

$$
T(n)=T(n-1)+\Theta(n)=\Theta(n^2).
$$

The number of key comparisons is exactly $(n-1)+(n-2)+\cdots+1=n(n-1)/2$. The recursion can have linear depth.

### Balanced and consistently unbalanced splits

Perfectly balanced splits give $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$, with rounding and the excluded pivot suppressed.

Even repeated 1:9 splits give

$$
T(n)=T(n/10)+T(9n/10)+\Theta(n)=\Theta(n\log n).
$$

The shortest path has about $\log_{10}n$ levels and the longest about $\log_{10/9}n$. Before the shortest paths finish, each level has linear total work; every level has at most linear work. Both depth bounds are logarithmic, establishing matching asymptotic bounds. The standard equal-size Master theorem in [[Algorithm as recipes#Master theorem]] does not directly apply to these unequal subproblems.

The slide's alternating lucky/unlucky example gives $L(n)=2U(n/2)+\Theta(n)$ and $U(n)=L(n-1)+\Theta(n)$, hence $L(n)=2L(n/2-1)+\Theta(n)=\Theta(n\log n)$. This is intuition that occasional poor splits need not ruin performance, not a proof that arbitrary pivot choices are good.

Source: [[lecture7-Sort.pdf#page=21|Worst, balanced and almost-balanced cases, pp. 21–35]].

### Comparing recursion trees rather than just final formulas

With seven distinct keys and the smallest key chosen every time, subproblem sizes along the nonempty branch are $7,6,5,4,3,2$. Partition makes $6+5+4+3+2+1=21$ comparisons. With a median pivot at every partition, the root makes six comparisons, the two size-three children make two each, and the size-one leaves need none: ten comparisons in total.

These examples show why recursion depth alone is not the whole runtime: a node's partition cost depends on its subproblem size. A long chain keeps doing nearly full-size scans; a balanced tree spreads smaller scans across levels. Summing work over all nodes gives the comparison count.

![[aapp-depth-sorting-trees.png|720]]

*Original seven-key comparison: extreme pivots create a chain with 21 comparisons; median pivots create a balanced tree with ten. Labels show subproblem size and partition-comparison cost.*

A repeated 1:9 split is different from a repeated $1:(n-2)$ split. In the first, even the larger child is a fixed fraction of its parent. In the second, the larger child loses only a constant number of elements, giving linear depth and quadratic work. “Unbalanced” by itself is therefore too imprecise to determine complexity.

## Randomized quicksort

Before every partition, choose a uniformly random index in the current subarray and swap that item with its first element:

```text
RANDOMIZED-PARTITION(A, p, r)
    j = uniform random integer in [p, r]
    swap A[p], A[j]
    return PARTITION(A, p, r)
```

Use this routine in the recursive quicksort code. Assume fresh random choices and distinct keys. For every fixed input order, every pivot rank is equally likely, giving each split $k:(n-1-k)$ probability $1/n$.

This is a **Las Vegas** algorithm: every result is sorted correctly, but its runtime varies. Randomization gives an expected bound on every fixed distinct-key input; it does not eliminate quadratic executions. This connects directly to [[Randomized Algorithms#Where randomness comes from]].

### Expected-time recurrence

Let $E_n=\mathbb E[T(n)]$, with constant-time base cases. Conditioning on the pivot's rank,

$$
E_n=\frac1n\sum_{k=0}^{n-1}(E_k+E_{n-1-k})+\Theta(n)
=\frac2n\sum_{k=0}^{n-1}E_k+\Theta(n).
$$

The slide expresses this using indicators $X_k$ for the split, with $\mathbb E[X_k]=1/n$. Conditioning makes the assumptions explicit: after a split, fresh recursive random choices yield the expected costs for those sizes. Linearity alone never justifies factoring an arbitrary expectation of a product.

**Supplementary clarification:** this is an expectation over the algorithm's random choices, not a claim that real input permutations are uniform. [Aspnes's *Notes on Randomized Algorithms*, §1.3](https://www.cs.yale.edu/~aspnes/classes/469/notes.pdf) develops the same conditional recurrence.

Source: [[lecture7-Sort.pdf#page=36|Random pivots and expectation, pp. 36–43]].

### Expanding the expected recurrence for four keys

For four distinct keys, the pivot has four possible ranks. The child sizes are $(0,3),(1,2),(2,1),(3,0)$, each with probability $1/4$. Counting comparisons, every root partition costs three. Thus

$$
C_4=3+\frac14[(C_0+C_3)+(C_1+C_2)+(C_2+C_1)+(C_3+C_0)].
$$

Each child size occurs twice in the bracket, which explains the factor $2/n$ in the general recurrence. This is a weighted average over alternative root outcomes; it does **not** mean the algorithm executes all four alternatives. Within the selected alternative, however, it does execute both child sorts, so their costs add.

The rank of a uniform pivot is uniform only under the distinct-key assumption used here. If many keys are equal, multiple pivot indices can produce the same split in the printed partition algorithm, breaking the “all split sizes equally likely” argument.

### Substitution proof from the slides

Absorb the constant-size terms into a nonrecursive upper bound $cn$. For a suitable constant $a$, assume $E_k\le ak\lg k$ for $2\le k<n$, where $\lg=\log_2$. The lecture uses

$$
\sum_{k=2}^{n-1}k\lg k\le\frac12n^2\lg n-\frac18n^2.
$$

Then

$$
E_n\le\frac{2a}{n}\left(\frac12n^2\lg n-\frac18n^2\right)+cn
=an\lg n-\frac{an}{4}+cn\le an\lg n
$$

when $a\ge4c$, enlarged if necessary to cover the base cases. Thus expected time is $O(n\log n)$.

**Supplementary proof of the sum bound for even $n$:** for $k\le n/2$, $\lg k\le\lg n-1$; for all other $k<n$, $\lg k\le\lg n$. Subtract the resulting saving on the first half:

$$
\sum_{k=1}^{n-1}k\lg k
\le\frac{n(n-1)}2\lg n-\sum_{k=1}^{n/2}k
\le\frac12n^2\lg n-\frac18n^2.
$$

For odd $n$, use $m=\lfloor n/2\rfloor$ and saving $m(m+1)/2$; the additional $n\lg n/2$ slack covers the rounding. This supplies the exercise omitted on page 44.

> [!note] Reading the rendered formula
> Page 47 writes $an\lg n-(an/4-\Theta(n))$. Its outer parentheses are essential: this is $an\lg n-an/4+\Theta(n)$, not subtraction of both terms. Text extraction can lose the parentheses; the rendered slide has the correct sign.

Source: [[lecture7-Sort.pdf#page=44|Substitution proof, pp. 44–48]].

### Why the induction needs a saving term

If one replaced every $\lg k$ merely by $\lg n$, the estimate would nearly spend the entire proposed $an\lg n$ budget on the recursive calls and then still need to pay for the root's partition. The negative $an/4$ term supplies enough slack to pay that $cn$ cost.

The choice $a\ge4c$ is not an attempt to determine a machine-specific constant. It demonstrates that one fixed constant can cover every inductive step, with a possible further increase to cover the finite base cases. This is the role of constants in an asymptotic proof: a uniform guarantee for all sufficiently large inputs, not a fitted timing curve.

### Supplementary exact comparison count

Counting only comparisons of keys in partition, write $C_0=C_1=0$ and

$$
C_n=n-1+\frac2n\sum_{k=0}^{n-1}C_k.
$$

Subtract the corresponding equation for $n-1$ after multiplying each by its size:

$$
nC_n=(n+1)C_{n-1}+2(n-1).
$$

Dividing by $n(n+1)$ and telescoping gives

$$
C_n=2(n+1)H_n-4n=\Theta(n\log n).
$$

For $n=4$, $C_4=10(25/12)-16=29/6\approx4.833$, compared with six in the worst execution. This is a count of pivot-key comparisons, not swaps or total machine instructions. It also establishes the matching expected lower bound for this specific algorithm.

The telescoping step in the exact count can be made explicit. Divide the difference equation by $n(n+1)$:

$$
\frac{C_n}{n+1}-\frac{C_{n-1}}n=\frac{2(n-1)}{n(n+1)}=-\frac2n+\frac4{n+1}.
$$

Summing from 2 to $n$ cancels the intermediate left-hand terms. On the right,

$$
\frac{C_n}{n+1}=-2(H_n-1)+4(H_{n+1}-3/2)
=2H_n-4+\frac4{n+1}.
$$

Multiplying by $n+1$ yields the formula above. The harmonic number appears because the averaging recurrence creates reciprocal-size terms, connecting this calculation with the hiring analysis in [[Randomized Algorithms#Uniform random ordering]].

### Duplicates, space, and practical claims

For an all-equal array, the lecture's `<=` partition always puts the pivot at the right end. Random pivot selection cannot change that: time is still $\Theta(n^2)$. **Supplementary remedy:** a three-way partition into $<x$, $=x$, and $>x$ recurses only on the strict regions; this explains why the distinct-key assumption matters without changing the algorithm analyzed in the deck.

“In place” describes partition's constant auxiliary array storage. Ordinary recursion still uses $O(n)$ stack space in the worst case, and expected $O(\log n)$ depth for distinct keys with random pivots. Recursing on the smaller side and looping over the larger side bounds the stack by $O(\log n)$ even on bad splits. The swapping implementation is not stable.

Page 49's “typically over twice as fast as merge sort” is a historical performance claim, not an algorithmic guarantee. Hardware, key type, duplicate distribution, pivot selection and implementation determine practical results. Measure these as in [[Algorithm as recipes#Mini-labs and shortest paths]].

## Comparison-sorting lower bound

For fixed size $n$, a binary decision tree represents a comparison algorithm. An internal node compares two keys; an edge records the outcome; a leaf identifies their sorted permutation. For distinct keys, there are $n!$ possible orderings to distinguish. A binary tree of height $h$ has at most $2^h$ leaves, so

$$
2^h\ge n!,\qquad h\ge\lceil\lg(n!)\rceil=\Omega(n\log n).
$$

The deck uses Stirling's bound. An elementary alternative is $n!\ge(n/2)^{n/2}$ for even $n$, which already yields the asymptotic lower bound. Path length measures **comparisons**, and therefore lower-bounds running time in a unit-cost comparison model; it need not count every instruction exactly.

![[aapp-lecture7-decision-tree.png|720]]

*For input $[9,4,6]$, the leaf 231 denotes the order $a_2,a_3,a_1$, producing $[4,6,9]$.* [[lecture7-Sort.pdf#page=56|Source slide 56]].

Consequently merge sort and heapsort are asymptotically optimal in **worst-case comparison complexity**. This theorem does not say that each individual input requires $\Omega(n\log n)$ work: insertion sort's sorted-input best case is linear. It also does not prohibit faster algorithms that inspect integer digits or use keys as array indices.

**Supplementary model clarification:** the restriction is access to relative order through comparisons. Counting sort changes that model by indexing with the key. [MIT 6.006, Lecture 7](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/bf7d79105762bf79bbc0925438e1468a_MIT6_006F11_lec07.pdf).

Source: [[lecture7-Sort.pdf#page=51|Decision trees and lower bound, pp. 51–59]].

### Why a leaf must distinguish an ordering

Suppose two different relative orders of distinct keys reached the same leaf. The algorithm would then produce the same positional ordering for both without further comparisons, so at least one output would be wrong. That is why all $n!$ possible relative orders need distinguishable leaves, even if the algorithm physically moves elements during its execution.

For three keys, there are six orders. A tree with only two comparisons on every path has at most four leaves, so at least one input needs three comparisons. This does not mean every path must have length three. The slide's tree has some shorter paths, but its height is three. For four keys, $4!=24$ and $2^4=16<24\le32=2^5$, so the information bound requires at least five comparisons in the worst case.

The argument presumes keys are opaque except for comparisons. If a key directly selects a bucket, one operation can reveal more than a single less/greater relation. Counting sort uses exactly that additional representation information, so it does not violate the lower bound.

## Counting sort

Assume keys are integers in $\{1,\ldots,k\}$, with constant-time key access and array indexing. Counting sort builds frequencies, converts them to cumulative positions, and places records in a separate output array.

```text
COUNTING-SORT(A, k)                 // A[1..n], possibly records with keys
    C[1..k] = all zeros
    for j = 1 to n
        C[key(A[j])] += 1
    for i = 2 to k
        C[i] += C[i - 1]
    for j = n down to 1
        x = key(A[j])
        B[C[x]] = A[j]
        C[x] -= 1
    return B
```

After counting, $C[x]$ is the number of keys equal to $x$. After the prefix sum, it is the number at most $x$, hence the last output position reserved for that key. Placing a record and decrementing the pointer fills its key's reserved block from right to left. All records are placed exactly once, into blocks ordered by key, proving correctness.

This cumulative-count step is the sequential operation studied as a parallel scan in [[PRAM#Prefix sum]]. That connection alone does not make the placement loop safe in parallel: equal keys would compete to update the same counter.

### Worked count and stability

For $A=[4,1,3,4,3]$, frequencies for keys 1–4 are $[1,0,2,2]$; cumulative counts are $[1,1,3,5]$. Scanning right to left places keys into positions $3,5,2,1,4$, respectively, giving $B=[1,3,3,4,4]$.

Attach identities: $[4_a,1,3_a,4_b,3_b]$ becomes $[1,3_a,3_b,4_a,4_b]$. A later equal-key record is encountered first and assigned the rightmost free position, so earlier records stay earlier. This is **stability**, which will be needed by radix sort. Scanning left to right with this same decrementing endpoint scheme would reverse equal-key records.

![[aapp-lecture7-stability.png|720]]

*Arrows track individual equal-key records, illustrating preservation of their original order.* [[lecture7-Sort.pdf#page=79|Source slide 79]].

The four loops take $\Theta(k)+\Theta(n)+\Theta(k)+\Theta(n)=\Theta(n+k)$ time. Storage is $\Theta(k)$ for counts and $\Theta(n)$ for output. It is linear in $n$ only when $k=O(n)$; a huge sparse key range can make it impractical. For digit keys $0,\ldots,k-1$, shift the count-array convention consistently.

Source: [[lecture7-Sort.pdf#page=60|Algorithm, trace, cost and stability, pp. 60–79]].

### Seeing cumulative counts as reserved output blocks

In the example with frequencies $[1,0,2,2]$, key 1 owns output position 1, key 2 owns no positions, key 3 owns positions 2–3, and key 4 owns positions 4–5. If $P[x]$ denotes the **unchanged** cumulative frequencies, key $x$ owns the interval $P[x-1]+1,\ldots,P[x]$, with $P[0]=0$.

During placement, the working counter $C[x]$ is no longer the original total count at most $x$; it becomes the rightmost unfilled position in that reserved interval. Distinguishing these two meanings avoids confusion when tracing the decrement. The blocks are disjoint, and each has exactly as many positions as records of its key, so no record overwrites a different key's output.

For bare integers, one could simply write each key as many times as its frequency. But records can carry payloads—names, timestamps, or other fields—and a sort must move those complete records. Stable placement preserves both payload identity and the original order of equal keys. That makes counting sort useful as a digit pass, where “equal digit” records may still differ in lower digits.

![[aapp-depth-sorting-count-blocks.png|720]]

*Original block view of cumulative counts: the endpoints 1, 1, 3, 5 partition five output positions into blocks of lengths 1, 0, 2, 2.*

## Radix sort

### Least-significant-digit passes

For fixed-length nonnegative integer keys, sort by the least significant digit, then the next digit, continuing to the most significant. **Every digit sort must be stable.** Leading zeros pad shorter representations.

```text
LSD-RADIX-SORT(A, d, base)
    for position = 0 to d - 1       // least significant first
        A = stable counting sort of A by digit(A, position, base)
    return A
```

Induction invariant: after pass $t$, the sequence is sorted by its lowest $t$ digits. At pass $t+1$, different new digits are ordered by the digit sort; records with equal new digits retain their previous order, which already compares the lower digits correctly. After the last pass, this is full numerical order.

For the slide's decimal input, the stable passes are:

| Stage | Sequence |
|---|---|
| Input | 329, 457, 657, 839, 436, 720, 355 |
| Units | 720, 355, 436, 457, 657, 329, 839 |
| Tens | 720, 329, 436, 839, 355, 457, 657 |
| Hundreds | 329, 355, 436, 457, 657, 720, 839 |

![[aapp-lecture7-radix.png|720]]

*Each column is one stable digit pass; equal digits preserve the order established by earlier columns.* [[lecture7-Sort.pdf#page=81|Source slide 81]].

**Supplementary clarification of page 80:** most-significant-digit sorting is not inherently incorrect. It must recursively sort *within* buckets, preserving their higher-digit ordering. Repeated global stable passes from most to least significant are wrong: sorting $[21,12]$ first by tens gives $[12,21]$, then by units gives $[21,12]$. The lecture's “bad idea” wording should be read in the context of the simple global-pass method.

Source: [[lecture7-Sort.pdf#page=80|Digit passes and correctness, pp. 80–84]].

### Why stability carries information forward

Take $[12,11,21]$. After a units-digit pass, a stable result is $[11,21,12]$. During the tens-digit pass, 11 and 12 have equal tens digits. Keeping their current order yields $[11,12,21]$. An unstable tens pass is allowed to reverse them, producing $[12,11,21]$, which is not numerically sorted even though the tens digits are ordered.

The previous pass has already encoded useful information in the relative order of records. Stability preserves exactly the information that a later pass cannot distinguish because it sees only the current digit. This is why a “correct sort of the current digit” is insufficient unless equal-digit order is preserved.

Leading zero padding lets keys of different displayed lengths participate in the same fixed-digit argument: 7 becomes 007 when sorted with three-digit nonnegative integers. Signed integers require an explicit representation/order treatment; simply sorting their raw signed representations as unsigned digits need not give the desired numerical order.

### Choosing the digit width

For $b$-bit keys grouped into $r$-bit digits, the radix is $2^r$. With stable counting sort,

$$
T(n,b,r)=\Theta\left(\left\lceil\frac br\right\rceil(n+2^r)\right),\qquad
\text{auxiliary space}=\Theta(n+2^r).
$$

The ceiling handles a partial final digit; the slides write $b/r$ assuming divisibility. Larger $r$ reduces passes but expands the count array exponentially. For $n\ge2$, an asymptotically useful choice is $r=\min(b,\lfloor\lg n\rfloor)$, assuming $b\ge1$ and constant-time extraction of these digits. This gives $\Theta(n\lceil b/\lg n\rceil)$ up to constant factors. Do not choose $r>b$ or omit the at-least-one-pass requirement.

For keys in $[0,n^d-1]$, $b=\lceil d\lg n\rceil$ suffices and the resulting cost is $\Theta(dn)$ for $d\ge1$. Linear time in $n$ requires constant $d$; representation size is part of the cost model.

**Supplementary worked comparison:** for $n=4096$ and $b=32$, compare the proxy $\lceil b/r\rceil(n+2^r)$:

| $r$ | Passes | Count entries | Work proxy |
|---|---|---|---|
| 8 | 4 | 256 | 17,408 |
| 11 | 3 | 2,048 | 18,432 |
| 16 | 2 | 65,536 | 139,264 |

Fewer passes alone do not imply less work. This proxy omits constants and memory effects, so it is not a benchmark prediction.

> [!warning] Qualifications to slide 88
> With $n=2000$, $\lfloor\lg n\rfloor=10$, which gives four passes for 32-bit keys. Three passes require $r=11$, with 2048 counters; this remains $O(n)$ storage and is reasonable, but relaxes the exact $2^r\le n$ rule. Also, quicksort recursion levels are not uniform full-array “passes,” so the slide's comparison with 11 passes is illustrative rather than a universal operation count. Relative locality and speed require measurements.

Source: [[lecture7-Sort.pdf#page=85|Bit grouping and runtime tradeoffs, pp. 85–88]].

### Extracting a digit and interpreting the range bound

For a nonnegative integer $x$ in base $B$, digit position $j$ (zero-based from the right) is $\lfloor x/B^j\rfloor\bmod B$. For $x=329,B=10$, this gives 9, 2 and 3. With $r$-bit groups, $B=2^r$, and shifts/masks can perform the corresponding extraction when the key fits the assumed machine representation.

The interval $0\le x<n^d$ means at most $d$ base-$n$ digits: the largest $d$-digit value is $(n-1)(1+n+\cdots+n^{d-1})=n^d-1$. Hence a constant $d$ gives a constant number of passes, each on a range of $n$ digit values. If $d$ grows with input size, its factor remains in $\Theta(dn)$; it must not disappear when calling the method “linear.”

A large base is not free. In addition to reading and writing $n$ records, every counting pass must initialize and scan its counter range. That accounts for the $2^r$ term even if many digit values never occur. The useful choice near $\lg n$ balances range overhead with input scanning; the best measured choice can differ because of caches and fixed per-pass costs.

## Punched-card appendix

Pages 89–96 give historical context: holes encode records, a reader detects the selected field, an operator deposits cards into bins, and collecting the bins in order implements a digit pass. The algorithmically relevant point is that preserving arrival order within a bin supplies stability. The appendix illustrates Hollerith's equipment, later 80-column cards, and a patent passage about grouping by successive fields. It is background in the supplied deck; no explicit exam exclusion has been supplied.

Original pictures and credits remain available in [[lecture7-Sort.pdf#page=89|the source appendix, pp. 89–96]].

> [!warning] Historical correction to slide 90
> The slide conflates company formation, merger, and renaming. Hollerith established the Tabulating Machine Company in **1896**; it joined the formation of Computing-Tabulating-Recording in **1911**, which was renamed IBM in **1924**. This supplementary correction follows the [US Census Bureau's historical account](https://www.census.gov/about/history/stories/monthly/2016/january-2016.html).

## Comparison table

| Algorithm | Time | Auxiliary storage | Stable? | Main assumption |
|---|---|---|---|---|
| Insertion sort | Best $\Theta(n)$; worst $\Theta(n^2)$ | $O(1)$ | Yes with strict shifting | Comparable keys |
| Merge sort | $\Theta(n\log n)$ | $\Theta(n)$ for array version | Yes with left-first ties | Comparable keys |
| Randomized quicksort here | Expected $\Theta(n\log n)$; worst $\Theta(n^2)$ | Constant partition space; stack as discussed | No | Distinct keys for the expectation |
| Counting sort | $\Theta(n+k)$ | $\Theta(n+k)$ including output | Yes | Integer keys in bounded range |
| LSD radix sort | $\Theta(\lceil b/r\rceil(n+2^r))$ | $\Theta(n+2^r)$ | Yes | Stable passes and accessible digits |

## Takeaways

- A partition establishes separation around a pivot, not a completely sorted array.
- Random pivots improve expected time without ruling out bad executions.
- Lower bounds depend on the permitted operations and on which case is being analyzed.
- Stability is the mechanism that makes LSD radix sort correct.
- Count the key range, digit width, output storage, and recursion stack explicitly.

## Exam practice

These are original practice questions based on the supplied deck, not past exam questions.

**1. Partition and duplicates.** Apply the lecture's partition to $[3,5,3,1,4]$. Give the pivot position and the two recursive ranges. What happens on an array of $n$ equal keys?

> [!faq]- Worked solution
> Reading the second 3 gives $[3,3,5,1,4]$; reading 1 gives $[3,3,1,5,4]$; the final pivot swap gives $[1,3,3,5,4]$. The pivot is at position 3; recurse on positions 1–2 and 4–5. On equal keys, each pivot ends at the right boundary, so the recurrence is $T(n)=T(n-1)+\Theta(n)$, even with randomized pivot indices.

**2. Expected comparisons.** Use the comparison recurrence to find $C_2,C_3,C_4$. Why is this not an input-distribution assumption?

> [!faq]- Worked solution
> $C_2=1$, $C_3=2+(2/3)(0+0+1)=8/3$, and $C_4=3+(1/2)(0+0+1+8/3)=29/6$. Every pivot rank is equally likely because the algorithm chooses uniformly among distinct keys on each fixed input; we do not assume that the input order was random.

**3. Stable placement.** Counting sort receives $[2_a,1_a,2_b,1_b]$ with $k=2$. Compute the cumulative counts and stable result. What result follows from scanning forward using the same decrementing counters?

> [!faq]- Worked solution
> Frequencies are $[2,2]$ and cumulative counts $[2,4]$. A reverse scan gives $[1_a,1_b,2_a,2_b]$. A forward scan puts records into positions 4, 2, 3, 1, giving $[1_b,1_a,2_b,2_a]$: sorted by key but unstable.

**4. Model and radix budget.** Sort $n$ integers from $0$ to $n^3-1$. Explain how linear time can coexist with the comparison lower bound. For $n=1024$, how many 10-bit passes are sufficient?

> [!faq]- Worked solution
> Three base-$n$ stable counting passes each take $\Theta(n+n)$ time, totaling $\Theta(n)$. The algorithm uses digits as indices and is outside the comparison-only model. For $n=1024=2^{10}$, keys need at most 30 bits, so three 10-bit passes suffice.

**5. Locate the lost invariant.** An LSD radix implementation uses an unstable digit sort on every pass. It produces a result sorted by the most significant digit. Why is that not sufficient? Give a three-record counterexample.

> [!faq]- Worked solution
> Equal most-significant digits still need the order established by lower digits. For $[12,11,21]$, a units pass can give $[11,21,12]$. If the tens pass reverses the two records whose tens digit is 1, the result is $[12,11,21]$. Its tens digits are ordered, but the full numbers are not. The missing invariant is preservation of lower-digit order within equal current digits.

## Revision questions

1. Why must recursive calls exclude the final pivot position?
2. Why does a repeated 1:9 split still yield logarithmic depth?
3. What randomness supports the expected recurrence?
4. Does the decision-tree proof lower-bound every input's time?
5. Why is a reverse scan used in this version of counting sort?
6. What goes wrong with an unstable radix pass?
7. Why is a 16-bit digit not always better than an 8-bit digit?

> [!faq]- Answer sketch
> 1. It is already in a valid final position, and excluding it guarantees shrinking subproblems.
> 2. Each path shrinks by a fixed factor below one; even the longest path is logarithmic.
> 3. Uniform pivot selection with fresh recursive random choices, under distinctness.
> 4. No, its tree-height argument gives a worst-case lower bound.
> 5. Decrementing block endpoints assign later equal records later output positions.
> 6. It can destroy the lower-digit order established earlier.
> 7. It reduces passes but increases the counter range from 256 to 65,536 entries.
