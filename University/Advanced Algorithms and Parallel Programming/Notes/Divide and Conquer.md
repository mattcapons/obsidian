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

### Turning the design into an exam answer

For correctness, use induction on input size: establish the base case, assume recursive calls solve smaller instances, then explain why combining those answers solves this instance. For complexity, count the calls actually made and charge the divide/combine work separately. A split into two pieces does not imply two recursive calls, and a block addition is not constant-time when blocks grow.

The supplied deck adapts these examples from [Demaine and Leiserson's MIT divide-and-conquer notes](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/9cdb6914be3e87215cb86f327ee4180b_lec3.pdf). Use only the matching examples here; that external lecture also contains material outside the supplied deck.

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

![[aapp-lecture3-binary-search.png|720]]

*After discarding the left half, binary search compares the target 9 with the middle of the remaining region, 12.* [[lecture3-DandC.pdf#page=12|Source slide 12]].

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

![[aapp-lecture3-matrix-blocks.png|720]]

*Each output block is a sum of two block products: ordinary recursion still needs eight recursive multiplications.* [[lecture3-DandC.pdf#page=23|Source slide 23]].

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

### Numerical check of the seven products

**Supplementary worked example:** let

$$
A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad
B=\begin{pmatrix}5&6\\7&8\end{pmatrix}.
$$

Using the lecture's $P_i$ convention gives

$$
(P_1,P_2,P_3,P_4,P_5,P_6,P_7)=(-2,24,35,8,65,-30,-22).
$$

Consequently $r=65+8-24-30=19$, $s=-2+24=22$, $t=35+8=43$, and $u=65-2-35+22=50$:

$$
AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}.
$$

Checking by the ordinary row-column rule produces the same result. Product numbering differs across textbooks, so keep each set of product formulas together with its corresponding reconstruction formulas.

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

![[aapp-lecture3-tree-layout.png|720]]

*The straightforward tree layout grows linearly in width and logarithmically in height.* [[lecture3-DandC.pdf#page=43|Source slide 43]].

### H-tree layout

The H-shaped construction packs four quarter-sized subtrees into a roughly square layout. Its side length obeys

$$
L(n)=2L(n/4)+\Theta(1).
$$

The Master theorem reference term is $n^{\log_4 2}=\sqrt n$, so $L(n)=\Theta(\sqrt n)$ and the area is $L(n)^2=\Theta(n)$.

**Supplementary optimality explanation:** under the pictured grid model with distinct constant-area node locations, a tree with $n$ leaves already needs $\Omega(n)$ area. The H-tree therefore matches this order of growth.

Source: [[lecture3-DandC.pdf#page=39|Layouts, pp. 39–46]].

![[aapp-lecture3-h-tree.png|720]]

*The H-tree packs four smaller subtrees into a square-like region, reducing the area to linear growth.* [[lecture3-DandC.pdf#page=46|Source slide 46]].

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

## Exam practice

These are original problems using the deck's algorithms and layouts.

**1. Explain duplicate recursion.** A power routine makes two independent calls to compute $a^{n/2}$, then multiplies their results. Compare it with computing that value once and storing it.

> [!faq]- Worked solution
> For even powers of two, duplicate calls give $T(n)=2T(n/2)+\Theta(1)=\Theta(n)$. Reusing a single result gives $T(n)=T(n/2)+\Theta(1)=\Theta(\log n)$. Both are correct, but their computation trees differ. Counting the mathematical expression's two factors as two necessary calls misses the opportunity to reuse a value.

**2. Analyze a layout rather than runtime.** An H-tree side length satisfies $L(n)=2L(n/4)+c$, with $L(1)=\ell_0>0$. Derive the side length and area for $n=4^k$.

> [!faq]- Worked solution
> Expansion gives $L(n)=2^k\ell_0+c(2^k-1)$. Since $2^k=\sqrt n$, the side is $\Theta(\sqrt n)$ and the square's area is $\Theta(n)$. The recurrence counts side length, so its answer must be squared to obtain area.

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
