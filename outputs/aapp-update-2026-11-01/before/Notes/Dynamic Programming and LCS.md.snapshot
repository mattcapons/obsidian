---
tags:
  - aapp
  - lecture
lecture: "12"
source: "[[lezione12DynamicProgramming.pdf]]"
---
# Dynamic Programming and LCS

[[AAPP Index|Course index]] · Previous: [[Randomized Data Structures]] · Next: [[Binary Decision Diagrams]] · Related: [[Divide and Conquer]]

## Overview

Dynamic programming solves a manageable collection of related subproblems and reuses their answers. The lecture develops this idea through the **longest common subsequence** problem: define prefix states, prove a recurrence, expose repeated recursive calls, then use memoization or a bottom-up table. The supplied deck is labeled 2021–2022 and adapts Demaine–Leiserson's 2005 material.

Source: [[lezione12DynamicProgramming.pdf#page=4|LCS and its recurrence, pp. 4–19]] · [[lezione12DynamicProgramming.pdf#page=20|Recursion and memoization, pp. 20–29]] · [[lezione12DynamicProgramming.pdf#page=30|Tabulation and reconstruction, pp. 30–33]].

The term “programming” here means planning/optimization, rather than writing source code. Page 3 supplies historical motivation; no historical date or anecdote is needed for the algorithmic proofs below.

## Subsequences and the output specification

A subsequence is obtained by deleting zero or more positions while preserving the order of the remaining symbols. It need not be contiguous. A **substring** must occupy consecutive positions and is a different problem.

For $X=\texttt{ABCBDAB}$ and $Y=\texttt{BDCABA}$, the sequence $\texttt{BCBA}$ is common: choose positions $(2,3,4,6)$ in $X$ and $(1,3,5,6)$ in $Y$. Its length is 4. Another longest common subsequence is $\texttt{BDAB}$, so the task is to return **a** longest sequence, not necessarily a unique one. The optimal length is uniquely defined even when several sequences achieve it.

An LCS algorithm should distinguish two outputs:

1. The optimal **length**, an integer.
2. One **witness sequence** attaining that length.

The length table establishes the optimum; reconstruction supplies a witness. Storing only one witness does not enumerate all optima, which may be numerous.

Source: [[lezione12DynamicProgramming.pdf#page=4|Problem and example, pp. 4–7]].

### Brute force and repeated symbols

There are $2^m$ choices of kept positions in an $m$-symbol sequence. For each, scan $Y$ from left to right, advancing a subsequence pointer whenever the next needed symbol appears. Accept when all requested symbols have been matched. A candidate longer than $Y$ can be rejected immediately; scanning a potentially valid candidate costs $O(n)$, assuming constant-time symbol access. Enumerating candidates gives an exponential approach, conventionally bounded by $O((m+n)2^m)$ when candidate construction is charged explicitly; the slide's $O(n2^m)$ focuses on checking.

> [!warning] Wording on page 9
> Bit masks give distinct **position selections**, not necessarily distinct symbol sequences. For $X=\texttt{AA}$, selecting position 1 or position 2 produces the same sequence $\texttt{A}$. This does not rescue brute force: the position-mask procedure still enumerates $2^m$ choices, including duplicates.

## State definition and recurrence

Let $m=|X|$, $n=|Y|$, with one-based symbol indexing. Define

$$
c[i,j]=\text{length of an LCS of }X[1..i]\text{ and }Y[1..j].
$$

The state records **prefix lengths**, not the symbols at which a substring starts. Include the empty prefixes:

$$
c[i,0]=c[0,j]=0.
$$

For positive $i,j$,

$$
c[i,j]=
\begin{cases}
c[i-1,j-1]+1,&X[i]=Y[j],\\
\max(c[i-1,j],c[i,j-1]),&X[i]\ne Y[j].
\end{cases}
$$

The answer length is $c[m,n]$. Every dependency decreases $i+j$, so the recurrence terminates with the stated base cases. The slides omit those base cases from their abbreviated recursive code; an implementation must supply them.

### Equal last symbols: why taking the diagonal is valid

Suppose both final symbols are $a$. Appending $a$ to any LCS of the shorter prefixes yields a common subsequence of length $c[i-1,j-1]+1$, so the optimum is at least this large.

For the reverse direction, an optimal common sequence must end in $a$; otherwise it could be extended by the matching final symbols, contradicting optimality. Its last $a$ can be aligned with $X[i]$ and $Y[j]$, leaving all earlier matches before those positions. Removing that final symbol leaves a common subsequence of $X[1..i-1]$ and $Y[1..j-1]$, of length at most $c[i-1,j-1]$. Thus the optimum is at most $c[i-1,j-1]+1$, proving equality.

The cut-and-paste viewpoint says the remaining prefix must itself be optimal: replacing a shorter prefix witness with a longer common one and appending $a$ would improve the supposed optimum.

### Unequal last symbols: why taking the maximum is valid

If $X[i]\ne Y[j]$, the final positions cannot be matched to one another. A common subsequence alignment cannot use **both** final positions as two separate matches: using $X[i]$ before a match at $Y[j]$ would require a later position in $X$, and using $Y[j]$ first would require a later position in $Y$. Therefore at least one final position is unused.

If $X[i]$ is unused, the solution is feasible for state $(i-1,j)$; if $Y[j]$ is unused, it is feasible for $(i,j-1)$. This bounds the full optimum above by their maximum. Conversely, either shorter-prefix solution is also feasible for the full prefixes, giving the matching lower bound. Hence the recurrence is exact.

This is **optimal substructure**: an optimal solution can be built from optimal solutions to the appropriate smaller states. Merely guessing a plausible local rule is not enough; both feasibility and optimality need justification.

Source: [[lezione12DynamicProgramming.pdf#page=12|Prefix definition and cut-and-paste proof, pp. 12–19]]. For an independent treatment of both recurrence cases, see [CMU 15-451, Dynamic Programming, §11.3](https://www.cs.cmu.edu/afs/cs/academic/class/15451-f10/www/lectures/lect0928.pdf). Only its LCS discussion is used here.

## Overlapping subproblems

A direct recursive implementation evaluates the recurrence every time a state is requested. A mismatch at $(i,j)$ calls $(i-1,j)$ and $(i,j-1)$; both can subsequently request $(i-1,j-1)$. Identical input states are recomputed on different branches.

![[aapp-lecture12-overlap.png|720]]

*The highlighted occurrences of state $(6,5)$ represent the same prefix problem. Merging repeated states converts a recursion tree into a dependency DAG.* [[lezione12DynamicProgramming.pdf#page=24|Source slide 24]].

There are only $mn$ positive-index states, or $(m+1)(n+1)$ including boundary states. Their recursive **occurrences** can be exponentially more numerous.

For a supplementary exact worst-case example, let every symbol of $X$ be `A` and every symbol of $Y$ be `B`. All positive states mismatch, so the number $N(i,j)$ of recursive calls satisfies

$$
N(i,j)=1+N(i-1,j)+N(i,j-1),\qquad N(0,j)=N(i,0)=1.
$$

Its solution is $N(i,j)=2\binom{i+j}{i}-1$. At $(3,3)$ this is 39 calls for only nine positive states. At $(r,r)$, the central binomial coefficient grows like $4^r/\sqrt{\pi r}$, so the work is exponential. The lecture's $O(m+n)$ path depth explains that long branching is possible, but depth alone is not an exponential lower-bound proof: a chain can also have that depth.

Source: [[lezione12DynamicProgramming.pdf#page=20|Recursive algorithm and overlapping states, pp. 20–26]].

## Memoization: solve each requested state once

Initialize boundary entries to zero and other entries to an **UNSEEN** marker. Zero cannot serve as that marker because an LCS length of zero is a legitimate computed answer.

```text
MEMO-LCS(i, j)
    if i == 0 or j == 0: return 0
    if memo[i,j] != UNSEEN: return memo[i,j]
    if X[i] == Y[j]
        memo[i,j] = 1 + MEMO-LCS(i-1, j-1)
    else
        memo[i,j] = max(MEMO-LCS(i-1, j), MEMO-LCS(i, j-1))
    return memo[i,j]
```

Each new state performs constant local work plus at most two recursive requests. The table ensures that any later request returns the saved value. With $O(1)$ table access, total recurrence-evaluation time is $O(mn)$, since there are $O(mn)$ states and outgoing dependencies. Do not multiply the time for a fully expanded recursive call by the number of table entries; that would charge the same work repeatedly again.

Worst-case time is $\Theta(mn)$, and a dense memo table occupies $\Theta(mn)$ space for positive lengths. A lazy evaluation can visit fewer states on an easy input: identical sequences can follow a diagonal chain. Allocating and explicitly initializing the entire dense table still costs $\Theta(mn)$ even on that input. The recursive stack is at most $O(m+n)$ deep, included within the overall dense-table space bound.

Source: [[lezione12DynamicProgramming.pdf#page=27|Memoization, pp. 27–29]]. The same reuse principle appears in [[Binary Decision Diagrams#Unique table and computed table]], where the cached state is an operand tuple rather than a pair of prefix lengths.

## Bottom-up tabulation

Instead of requesting states recursively, choose an order in which every dependency is already known. Increasing $i$ and then increasing $j$ works: the upper entry lies in the previous row, the left entry earlier in this row, and the diagonal in the previous row.

```text
LCS-TABLE(X[1..m], Y[1..n])
    c[0..m, 0..n] = 0
    for i = 1 to m
        for j = 1 to n
            if X[i] == Y[j]
                c[i,j] = c[i-1,j-1] + 1
            else
                c[i,j] = max(c[i-1,j], c[i,j-1])
    return c
```

Induct on $i+j$: all predecessor values are correct when a cell is filled, and the proven recurrence then makes that cell correct. This provides a correctness proof for the evaluation schedule as well as the formula. There are exactly $mn$ interior updates, giving $\Theta(mn)$ time and $\Theta(mn)$ table storage. The DP is deterministic, not a randomized expected-time procedure.

### Complete small table

For $X=\texttt{ABAC}$ and $Y=\texttt{BAC}$, place $X$ along rows and $Y$ along columns:

| $X$ prefix / $Y$ prefix | Empty | B | A | C |
|---|---|---|---|---|
| Empty | 0 | 0 | 0 | 0 |
| A | 0 | 0 | 1 | 1 |
| AB | 0 | 1 | 1 | 1 |
| ABA | 0 | 1 | 2 | 2 |
| ABAC | 0 | 1 | 2 | 3 |

At $(1,2)$, `A` matches `A`, so $c[1,2]=c[0,1]+1=1$. At $(2,2)$, `B` differs from `A`, so take $\max(c[1,2],c[2,1])=1$. At $(3,2)$, matching `A` gives $c[2,1]+1=2$. At $(4,3)$, matching `C` gives $c[3,2]+1=3$. Every cell counts the optimum for its **own pair of prefixes**, not for the whole input.

### The lecture's complete example

The slide places $X=\texttt{ABCBDAB}$ along **columns** and $Y=\texttt{BDCABA}$ along rows. The following transposed display has entry $c[i,j]$ at column $i$, row $j$:

| $Y$ prefix / $X$ prefix | Empty | A | AB | ABC | ABCB | ABCBD | ABCBDA | ABCBDAB |
|---|---|---|---|---|---|---|---|---|
| Empty | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| B | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| BD | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2 |
| BDC | 0 | 0 | 1 | 2 | 2 | 2 | 2 | 2 |
| BDCA | 0 | 1 | 1 | 2 | 2 | 2 | 3 | 3 |
| BDCAB | 0 | 1 | 2 | 2 | 3 | 3 | 3 | 4 |
| BDCABA | 0 | 1 | 2 | 2 | 3 | 3 | 4 | 4 |

The lower-right value 4 proves no common subsequence is longer than the example witnesses. The visual and the pseudocode use different display axes but the same mathematical states.

![[aapp-lecture12-lcs-table.png|720]]

*The shaded path traces a witness backward through the prefix table. Diagonal moves record matched symbols; horizontal or vertical moves discard an unmatched endpoint.* [[lezione12DynamicProgramming.pdf#page=32|Source slide 32]].

## Reconstructing a longest common subsequence

Start at $(m,n)$. If the final symbols match, record that symbol and move diagonally. Otherwise move to a predecessor with the same optimum value. If the upper and left values tie, either can lead to an optimum; use a deterministic tie rule if a reproducible witness is desired.

```text
RECONSTRUCT(X, Y, c)
    i = length(X); j = length(Y)
    reversedAnswer = empty list
    while i > 0 and j > 0
        if X[i] == Y[j]
            append X[i] to reversedAnswer
            i -= 1; j -= 1
        else if c[i-1,j] >= c[i,j-1]
            i -= 1
        else
            j -= 1
    reverse reversedAnswer
    return reversedAnswer
```

For the small example, states $(4,3)\to(3,2)\to(2,1)\to(1,0)$ record `C`, `A`, `B`. Reverse them to obtain `BAC`, which has length 3 and occurs in both inputs.

For the lecture example, choose the tie toward $(7,5)$ from $(7,6)$, then match `B` at $(7,5)$ and `A` at $(6,4)$. Move from $(5,3)$ to $(4,3)$, then to $(3,3)$, match `C`, move from $(2,2)$ to $(2,1)$, and match `B`. The reverse list is `BACB`, yielding `BCAB`. It differs from the opening witness `BCBA`, but both have the certified optimal length 4.

Every reconstruction step decreases at least one index, so tracing costs $O(m+n)$ time after table construction and stores $O(\min(m,n))$ output symbols. Keeping a direction arrow at each cell is optional: the values and input symbols suffice. The full-table algorithm still occupies $\Theta(mn)$ space overall.

## Reducing space and preserving the right claim

To compute **only the length**, retain the previous row and current row. Orient the shorter sequence along the columns, so each row has $\min(m,n)+1$ entries. At a match, read the previous row's diagonal; at a mismatch, read the previous row's same column and current row's previous column. After finishing a row, swap the row buffers and reset the first column to zero.

For the small example the row buffers progress through $[0,0,0,0]$, $[0,0,1,1]$, $[0,1,1,1]$, $[0,1,2,2]$, and $[0,1,2,3]$. Time remains $\Theta(mn)$; auxiliary table space becomes $O(\min(m,n))$.

If using one row, save the old diagonal before overwriting an entry. A left-to-right update otherwise destroys the previous row's value needed for the next diagonal. With $X=\texttt{A}$ and $Y=\texttt{AA}$, erroneously using an updated diagonal could count the single `A` twice.

> [!note] Scope of page 33's space exercise
> Two-row storage solves the **length** problem in linear space, but discards most information used by ordinary backward reconstruction. Do not claim the printed traceback works unchanged after deleting the table. Recovering a witness in linear auxiliary space requires a separate divide-and-conquer reconstruction method or additional recomputation; that algorithm is not supplied in this deck.

## Design checklist and takeaways

For a new DP, state the meaning of each state before writing a recurrence. Supply base cases, prove the choice covers all valid optima, count distinct states, count work/dependencies per state, and choose a legal evaluation order. Finally specify whether the stored answers are lengths, witnesses, or both.

LCS has both hallmarks: **optimal substructure** proves the recurrence, while **overlapping subproblems** explains why saving results improves naive recursion. These are separate arguments. Memoization changes how the recurrence is evaluated, not what it means. General DP is not automatically polynomial: its state count and transition cost must be bounded for the particular problem.

## Exam practice

These are original problems. Retrieved questions remain in [[Past Exam Question Bank#Dynamic programming and LCS]] and [[Past Exam Question Bank#BDDs and memoization]].

**1. Trace a new instance.** Compute the length table for $X=\texttt{ABA}$ and $Y=\texttt{BAA}$, then return one LCS.

> [!faq]- Worked solution
> With columns empty, B, A, A, the rows are $[0,0,0,0]$, $[0,0,1,1]$, $[0,1,1,1]$, and $[0,1,2,2]$. The optimum is 2. A traceback can return `BA` (positions 2,3 in $X$, 1,3 in $Y$); `AA` is another optimum. A length table does not force a unique witness.

**2. Diagnose a recurrence.** A student uses $c[i,j]=0$ whenever $X[i]\ne Y[j]$. Which problem resembles that recurrence, and why is it wrong for LCS?

> [!faq]- Worked solution
> Resetting at a mismatch is appropriate for the length of a common **substring ending at those positions**, together with a maximum over endpoints. LCS may skip endpoints. For `AB` and `ACB`, the optimum subsequence `AB` has length 2 despite the intervening mismatch. The LCS state must retain the best shorter-prefix answer via a maximum.

**3. Count states versus calls.** Both inputs have length 3 and use disjoint alphabets. How many calls does direct recursive evaluation make? How many positive table states can memoization evaluate?

> [!faq]- Worked solution
> Direct recursion makes $2\binom63-1=39$ calls. There are only $3\cdot3=9$ positive states. Boundary calls may still recur, but there are only constantly many outgoing requests per computed state, giving $O(mn)$ total requests.

**4. Report the right space bound.** A two-row implementation returns an LCS length of 40. Can it immediately follow the full-table traceback to return the 40 symbols?

> [!faq]- Worked solution
> No. Earlier predecessor values have been discarded. It has proved a length using $O(\min(m,n))$ auxiliary table storage, not stored the original traceback. Retain the full table or use a separately justified reconstruction procedure.

## Revision questions

1. What exactly does $c[i,j]$ represent?
2. Why are empty-prefix states zero?
3. Why is a zero result different from an uncomputed entry?
4. What makes a bottom-up ordering valid?
5. Why can two correct tracebacks return different strings?
6. What work is lost when exponential recursion is memoized?

> [!faq]- Answer sketch
> 1. The optimum common-subsequence length for two specified prefixes. 2. The empty sequence has no nonempty subsequence. 3. Zero is a possible optimum and must be cached as such. 4. All dependencies precede the state using them. 5. Tied predecessor values can represent different optimal witnesses. 6. Repeated evaluation of identical states; each distinct requested state is solved once.
