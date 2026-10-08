---
tags:
  - aapp
  - lecture
lecture: "3"
source: "[[lecture3-DandC.pdf]]"
---
# Divide and Conquer

[[AAPP Index|Course index]] · Previous: [[Algorithm as recipes]] · Next: [[PRAM]]

## Overview

Divide and conquer builds an algorithm from three steps:

1. **Divide** the instance into smaller subproblems.
2. **Conquer** by solving them recursively, stopping at base cases.
3. **Combine** their solutions into a solution of the original instance.

The crucial analysis question is how many recursive calls are made, how much smaller they are, and how much work occurs outside those calls. Recursion alone does not guarantee a faster algorithm.

Source: [[lecture3-DandC.pdf#page=2|Design paradigm]]. For recurrence tools, see [[Algorithm as recipes#Solving recurrences]].

## Merge sort as the template

Merge sort divides an array into two halves, recursively sorts both, and performs a linear merge:

$$
T(n)=2T(n/2)+\Theta(n).
$$

Here $a=2$, $b=2$, and $n^{\log_ba}=n$. Case 2 of the Master theorem gives $\Theta(n\log n)$. Each level contributes linear total work.

Source: [[lecture3-DandC.pdf#page=4|Merge sort and theorem review, pp. 4–7]].

## Binary search

**Problem:** find a target in a sorted array, or determine that it is absent.

Compare the target with the middle element. If they are equal, stop. If the target is smaller, search the left part; otherwise search the right part. Sortedness justifies discarding the other half.

```text
BINARY-SEARCH(A, target, lo, hi)       // inclusive bounds
    if lo > hi: return NOT-FOUND
    mid = lo + floor((hi - lo) / 2)
    if A[mid] == target: return mid
    if target < A[mid]
        return BINARY-SEARCH(A, target, lo, mid - 1)
    return BINARY-SEARCH(A, target, mid + 1, hi)
```

For $[3,5,7,8,9,12,15]$ and target $9$, compare with $8$, then search $[9,12,15]$; compare with $12$, then find $9$.

There is only **one** recursive call per level:

$$
T(n)=T(n/2)+\Theta(1)=\Theta(\log n)
$$

in the worst case. Finding the target immediately takes constant time. The divide step forms two possible regions, but the algorithm only solves one of them.

**Supplementary space distinction:** the recursive version uses $O(\log n)$ stack space; an iterative version uses $O(1)$ auxiliary space.

Source: [[lecture3-DandC.pdf#page=8|Binary search, pp. 8–16]].

## Exponentiation by squaring

**Problem:** compute $a^n$ for a nonnegative integer $n$.

Repeated multiplication takes $\Theta(n)$ multiplications. Instead use:

$$
a^n=
\begin{cases}
1 & n=0,\\
(a^{n/2})^2 & n>0\text{ even},\\
a(a^{(n-1)/2})^2 & n\text{ odd}.
\end{cases}
$$

```text
POWER(a, n)
    if n == 0: return 1
    half = POWER(a, floor(n / 2))
    result = half * half
    if n is odd: result = result * a
    return result
```

Compute `half` once and reuse it. Computing the same half-power twice would change the recurrence to $2T(n/2)+\Theta(1)$ and lose the logarithmic improvement.

Example: $a^{13}$ is formed by successively computing $a^1$, $a^3=(a^1)^2a$, $a^6=(a^3)^2$, and $a^{13}=(a^6)^2a$.

$$
T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)
$$

for growing positive $n$.

> [!note] Cost model
> The bound counts arithmetic operations at unit cost, as in the slides. When exact integer values become very large, multiplication is not constant-time; bit complexity requires a separate analysis.

Source: [[lecture3-DandC.pdf#page=17|Powering a number, pp. 17–19]].

## Matrix multiplication

For square matrices $A,B$ of dimension $n$, their product $C=AB$ satisfies

$$
c_{ij}=\sum_{k=1}^n a_{ik}b_{kj}.
$$

The ordinary triple loop computes $n^2$ entries using $n$ multiplication/addition steps each, giving $\Theta(n^3)$ time.

### Ordinary block recursion

Partition each matrix into four $(n/2)\times(n/2)$ blocks:

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
B=\begin{pmatrix}e&f\\g&h\end{pmatrix},\quad
C=\begin{pmatrix}r&s\\t&u\end{pmatrix}.
$$

Then

$$
r=ae+bg,\quad s=af+bh,\quad
t=ce+dg,\quad u=cf+dh.
$$

This uses **eight** recursive matrix multiplications and four block additions. A block addition touches $\Theta(n^2)$ entries at this scale, so

$$
T(n)=8T(n/2)+\Theta(n^2).
$$

Since $n^{\log_2 8}=n^3$, Case 1 gives $\Theta(n^3)$. The algorithm reorganizes the computation without improving its asymptotic arithmetic count.

Source: [[lecture3-DandC.pdf#page=20|Matrix multiplication, pp. 20–27]].

## Strassen's algorithm

Strassen reduces the recursive multiplication count from eight to seven, at the cost of extra block additions and subtractions.

Using the same block names as above, the slides define:

$$
\begin{aligned}
P_1&=a(f-h), &P_2&=(a+b)h,\\
P_3&=(c+d)e, &P_4&=d(g-e),\\
P_5&=(a+d)(e+h), &P_6&=(b-d)(g+h),\\
P_7&=(a-c)(e+f).
\end{aligned}
$$

Reconstruct the output blocks with

$$
\begin{aligned}
r&=P_5+P_4-P_2+P_6,\\
s&=P_1+P_2,\\
t&=P_3+P_4,\\
u&=P_5+P_1-P_3-P_7.
\end{aligned}
$$

### Why the formulas work

Expand the expression for $r$ without changing multiplication order:

$$
\begin{aligned}
r={}&(ae+ah+de+dh)+(dg-de)\\
&-(ah+bh)+(bg+bh-dg-dh)\\
={}&ae+bg.
\end{aligned}
$$

The extra terms cancel. The other output blocks can be checked similarly. This is valid for matrix blocks because it does **not** assume that multiplication commutes.

### Complexity

Seven recursive multiplications and 18 block additions/subtractions give

$$
T(n)=7T(n/2)+\Theta(n^2)
=\Theta(n^{\log_2 7})\approx\Theta(n^{2.807}).
$$

The improvement is in the exponent, so its relative significance grows with $n$. Extra constants and storage still affect the practical crossover.

> [!warning] Historical performance claims in the slides
> Pages 37–38 give a crossover of about $n=32$ and call an exponent around $2.376$ “best to date.” These are claims in the slide material, not current universal performance facts. Use the derived $\log_2 7$ exponent for this lecture; do not memorize a universal crossover or a current record from these pages.

**Supplementary implementation detail:** simple recursive presentations assume power-of-two dimensions. Padding to the next power of two retains the asymptotic bound, although it introduces practical overhead. Small blocks are usually handled by a base-case implementation rather than indefinite recursion.

Source: [[lecture3-DandC.pdf#page=29|Seven products and reconstruction, pp. 29–32]] · [[lecture3-DandC.pdf#page=33|Algorithm and analysis, pp. 33–38]].

## VLSI tree layouts

The final example changes the quantity being analyzed: instead of running time, analyze the **area** needed to embed a complete binary tree with $n$ leaves in a grid.

### Straightforward layout

The illustrated layout places two child subtrees side by side. Its height and width satisfy

$$
H(n)=H(n/2)+\Theta(1)=\Theta(\log n),
$$

$$
W(n)=2W(n/2)+\Theta(1)=\Theta(n).
$$

Thus its bounding area is $H(n)W(n)=\Theta(n\log n)$.

### H-tree layout

The H-shaped construction packs four quarter-sized subtrees into a roughly square layout. Its side length obeys

$$
L(n)=2L(n/4)+\Theta(1).
$$

The Master theorem reference term is $n^{\log_4 2}=\sqrt n$, so $L(n)=\Theta(\sqrt n)$ and the area is $L(n)^2=\Theta(n)$.

**Supplementary optimality explanation:** under the pictured grid model with distinct constant-area node locations, a tree with $n$ leaves already needs $\Omega(n)$ area. The H-tree therefore matches this order of growth.

Source: [[lecture3-DandC.pdf#page=39|Layouts, pp. 39–46]].

![[lecture3-DandC.pdf#page=46]]

## Comparison table

| Example | Recurrence | Result |
|---|---|---|
| Merge sort | $2T(n/2)+\Theta(n)$ | $\Theta(n\log n)$ |
| Binary search | $T(n/2)+\Theta(1)$ | $\Theta(\log n)$ worst-case time |
| Exponentiation by squaring | $T(n/2)+\Theta(1)$ | $\Theta(\log n)$ arithmetic operations |
| Ordinary recursive matrix product | $8T(n/2)+\Theta(n^2)$ | $\Theta(n^3)$ |
| Strassen | $7T(n/2)+\Theta(n^2)$ | $\Theta(n^{\log_2 7})$ |
| H-tree side length | $2L(n/4)+\Theta(1)$ | $\Theta(\sqrt n)$ length; $\Theta(n)$ area |

## Takeaways

- Count recursive calls actually executed, not all subproblems that could be chosen.
- Reuse duplicate subproblem results, as in exponentiation.
- Dividing into blocks is not enough: reducing expensive recursive work makes Strassen faster asymptotically.
- Recurrences can describe time, dimensions, and other resources.

## Revision questions

1. Why does binary search use $a=1$, not $a=2$?
2. What happens if `POWER` recursively computes the half-power twice?
3. Why does ordinary block multiplication remain cubic?
4. Why must Strassen's verification preserve factor order?
5. Why does a square with side $\Theta(\sqrt n)$ have area $\Theta(n)$?

> [!faq]- Answer sketch
> 1. It discards one half and searches only the other.
> 2. The recurrence becomes $2T(n/2)+\Theta(1)$, giving linear operation count.
> 3. Eight half-sized products generate the reference exponent $\log_2 8=3$.
> 4. Matrix multiplication is generally noncommutative.
> 5. Area is the product of the two side lengths.
