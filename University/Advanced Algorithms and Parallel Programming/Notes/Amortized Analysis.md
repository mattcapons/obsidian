---
tags:
  - aapp
  - lecture
lecture: "14"
source: "[[lezione14AmortizedAnalysis.pdf]]"
---
# Amortized Analysis

[[AAPP Index|Course index]] · Previous: [[Binary Decision Diagrams]] · Related: [[Randomized Algorithms#Where randomness comes from]] · [[Randomized Data Structures#Comparing guarantees]]

## Overview

Amortized analysis bounds the total cost of a sequence of operations, even when an individual operation is expensive. The lecture analyzes a growing table using the aggregate, accounting, and potential methods. These methods describe the same cost pattern from different viewpoints; none requires random inputs or random choices.

The supplied deck is labeled 2023–2024 and adapts CLRS and Demaine–Leiserson material. It studies **insertion with capacity doubling**. It does not supply a shrinking policy, hash-collision analysis, or a complete treatment of arbitrary indexed insertion.

Source: [[lezione14AmortizedAnalysis.pdf#page=3|Dynamic tables and aggregate analysis, pp. 3–20]] · [[lezione14AmortizedAnalysis.pdf#page=21|Accounting, pp. 21–25]] · [[lezione14AmortizedAnalysis.pdf#page=26|Potential method, pp. 26–43]].

## The dynamic-table model

Maintain an array with a current number $s$ of stored elements and allocated capacity $m$. Appending to a nonfull array writes one new element. Appending to a full array allocates capacity $2m$, copies all $m$ old elements, frees the old storage, then writes the new element. The first insertion creates capacity 1.

```text
APPEND(x)
    if capacity == 0
        allocate capacity 1
    else if size == capacity
        allocate a new array of capacity 2*capacity
        copy all size old elements to the new array
        free the old array
        capacity *= 2
    A[size] = x
    size += 1
```

This code uses zero-based array slots; insertion number $i$ is one-based and equals the size after the $i$th append. Under the lecture's exact-count model, charge 1 per element copy and 1 for the final insertion, leaving allocation/free overhead outside this simplified count. After $i\ge1$ appends,

$$
m_i=2^{\lceil\log_2i\rceil},\qquad
c_i=
\begin{cases}
i,&i\ge2\text{ and }i-1\text{ is a power of two},\\
1,&\text{otherwise}.
\end{cases}
$$

The first insertion costs 1. Expansions occur at $i=2,3,5,9,\ldots$: copying $i-1$ elements plus inserting one costs $i$.

![[aapp-lecture14-growth.png|720]]

*Capacities grow as 1, 2, 4, 8. The displayed seven stored items occupy an eight-slot table; previous allocations are no longer the active table.* [[lezione14AmortizedAnalysis.pdf#page=14|Source slide 14]].

Source: [[lezione14AmortizedAnalysis.pdf#page=3|Growth example and exact cost convention, pp. 3–17]].

## Worst-case per operation versus worst-case sequence

An append to a full size-$s$ table costs $s+1=\Theta(s)$ in this model. It is tempting to multiply the worst individual cost by the number of operations and report $\Theta(n^2)$ for $n$ appends.

Multiplication gives a valid loose **upper bound** $O(n^2)$, but not a tight $\Theta(n^2)$ bound. Expensive expansions cannot occur at every step. After growing capacity from $m$ to $2m$, many cheap insertions are required to fill the new table before another size-$2m$ copy is possible. The data structure's state constrains the entire cost sequence.

| Guarantee | What is bounded? | Randomness required? |
|---|---|---|
| Worst-case single operation | Largest cost for one legal operation/state | No |
| Expected cost | Average over a specified probability space | Yes, in the model or algorithm |
| Amortized cost | Total cost over every legal sequence, divided/charged across operations | No |

The treap's expected search bound in [[Randomized Data Structures]] averages over priorities. A dynamic table's constant amortized append bound holds for every sequence of appended values, even if those values were chosen adversarially. The guarantee still depends on the stated initial empty state and operation set.

Source: [[lezione14AmortizedAnalysis.pdf#page=15|The misleading product and definition, pp. 15–20]]. An independent explanation of sequence costs and potentials appears in [CMU 15-451, Amortized Analysis, §§7.1–7.3](https://www.cs.cmu.edu/afs/cs/academic/class/15451-f10/www/lectures/lect0914.pdf).

## Aggregate method

Count all insertions and all copies together. For $n\ge2$, old capacities copied are the powers of two strictly below $n$:

$$
\begin{aligned}
C(n)&=n+\sum_{j=0}^{\lfloor\log_2(n-1)\rfloor}2^j\\
&=n+2^{\lceil\log_2n\rceil}-1\\
&<3n.
\end{aligned}
$$

For $n=1$, the sum is empty and the same closed form gives 1. The geometric-sum identity follows from $1+2+\cdots+2^k=2^{k+1}-1$. The final capacity satisfies $n\le m_n<2n$, giving the last inequality. At least $n$ writes are unavoidable, so $C(n)=\Theta(n)$ and amortized append cost is $\Theta(1)$.

### Exact ten-insertion trace

| Insertion $i$ | Capacity after insertion | Copies | Actual $c_i$ | Cumulative actual cost |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 1 |
| 2 | 2 | 1 | 2 | 3 |
| 3 | 4 | 2 | 3 | 6 |
| 4 | 4 | 0 | 1 | 7 |
| 5 | 8 | 4 | 5 | 12 |
| 6 | 8 | 0 | 1 | 13 |
| 7 | 8 | 0 | 1 | 14 |
| 8 | 8 | 0 | 1 | 15 |
| 9 | 16 | 8 | 9 | 24 |
| 10 | 16 | 0 | 1 | 25 |

There are ten final writes and $1+2+4+8=15$ copies, for 25 total units. The average $25/10=2.5$ is below 3, although the ninth operation alone costs 9. An amortized bound is not a deadline of three time units for each append.

Source: [[lezione14AmortizedAnalysis.pdf#page=16|Aggregate counts and geometric sum, pp. 16–20]].

## Accounting method

Assign a fictitious charge $\widehat c_i$ to each operation. Charges pay actual work, and unused credit stays in a bank. For an initially empty account, maintain

$$
B_t=\sum_{i=1}^t(\widehat c_i-c_i)\ge0
\quad\text{for every prefix }t.
$$

Then every prefix's actual cost is at most its total charges. Proving only the final balance nonnegative would be insufficient for an argument that promises never to borrow from future operations.

Charge 3 for each insertion: one pays its immediate write and two are saved toward future copying. Between consecutive large doublings, the recent half of the full table has accumulated enough credits to pay for itself and the older half. For example, in a full eight-element table, the four recent elements can hold two credits each, paying for all eight copies into capacity 16. Credits are analytical bookkeeping; the program does not store coins.

The slide's refined accounting charges 2 for the first insertion and 3 for each later insertion. Its bank balance after insertion $i\ge1$ is

$$
B_i=2i-m_i.
$$

This is nonnegative because the active table is at least half full after append-only doubling, and it is 1 after the first insertion. The first operation's saved unit pays its copy when capacity 1 first expands. An induction or the exact table below checks that early boundary case as well as later phases.

![[aapp-lecture14-accounting.png|720]]

*The slide's refined charges and bank balances include a first-operation exception. The bank stores analytical prepaid work; it is not another physical array.* [[lezione14AmortizedAnalysis.pdf#page=25|Source slide 25]].

Source: [[lezione14AmortizedAnalysis.pdf#page=21|Accounting invariant and credit example, pp. 21–25]].

## Potential method

A potential function assigns a number $\Phi(D)$ to the current data-structure state. It represents stored credit without deciding which particular record owns each unit. Start with $\Phi(D_0)=0$ and maintain $\Phi(D_i)\ge0$. Define

$$
\widehat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1}).
$$

Positive potential change means charging more than the immediate cost and saving the excess. Negative potential change releases earlier savings. The potential itself stays nonnegative even when its change is negative.

Summing explicitly shows why the method works:

$$
\begin{aligned}
\sum_{i=1}^n\widehat c_i
&=\sum_{i=1}^n c_i
+(\Phi_1-\Phi_0)+(\Phi_2-\Phi_1)+\cdots+(\Phi_n-\Phi_{n-1})\\
&=\sum_{i=1}^n c_i+\Phi_n-\Phi_0\\
&\ge\sum_{i=1}^n c_i.
\end{aligned}
$$

The intermediate potentials cancel. Nonnegativity supplies the final inequality. The amortized charge for an individual operation can be below its actual cost because an earlier operation already contributed credit.

Source: [[lezione14AmortizedAnalysis.pdf#page=26|Definition, interpretation and telescoping, pp. 26–30]].

### A potential for capacity doubling

For a nonempty table with size $s$ and capacity $m$, choose

$$
\Phi(D)=2s-m.
$$

For the empty initial state define $\Phi(D_0)=0$ separately. After insertion $i\ge1$, this is the slide's

$$
\Phi_i=2i-2^{\lceil\log_2i\rceil}.
$$

This expression is nonnegative because $m_i<2i$. For $i=6$, size is 6 and capacity 8, giving $\Phi_6=12-8=4$.

![[aapp-lecture14-potential.png|720]]

*Six records in capacity eight store four units of potential, matching the accounting balance. The exponential is $2^{\lceil\lg i\rceil}$, not $2\lceil\lg i\rceil$.* [[lezione14AmortizedAnalysis.pdf#page=31|Source slide 31]].

### No expansion

Suppose an insertion changes $(s,m)$ to $(s+1,m)$, with $s<m$ and $s\ge1$. Its actual cost is 1 and its potential change is

$$
[2(s+1)-m]-[2s-m]=2.
$$

Therefore $\widehat c=1+2=3$. One unit pays for the write and two become saved potential.

### Expansion

Suppose the table is full with size and capacity both $m\ge1$. Before insertion, potential is $2m-m=m$. After allocating capacity $2m$ and inserting, size is $m+1$, so potential is $2(m+1)-2m=2$.

Actual work is $m$ copies plus one insertion, hence

$$
\widehat c=(m+1)+(2-m)=3.
$$

The potential drop finances most of the copying. At $m=8$, actual cost 9 combines with potential change $2-8=-6$ to give amortized cost 3. At the small expansion $m=1$, potential increases rather than decreases, but the same arithmetic still yields 3.

### First insertion: the intentional exercise

The first insertion changes the special empty state to size 1, capacity 1. Therefore

$$
c_1=1,\qquad\Phi_1=1,\qquad\Phi_0=0,
\qquad\widehat c_1=2.
$$

The generic no-expansion calculation assumed an ordinary nonempty before-state and cannot be applied blindly to zero. The logarithm formula at $i=0$ is undefined unless an explicit convention is supplied. The deck flags this first-insertion issue as an exercise on page 42; it is not an unnoticed sign error in the main argument.

Source: [[lezione14AmortizedAnalysis.pdf#page=31|Potential construction and calculations, pp. 31–42]].

### All balances in one table

| $i$ | Actual $c_i$ | $\Phi_i$ | $\Delta\Phi_i$ | Amortized $\widehat c_i$ |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 2 |
| 2 | 2 | 2 | 1 | 3 |
| 3 | 3 | 2 | 0 | 3 |
| 4 | 1 | 4 | 2 | 3 |
| 5 | 5 | 2 | $-2$ | 3 |
| 6 | 1 | 4 | 2 | 3 |
| 7 | 1 | 6 | 2 | 3 |
| 8 | 1 | 8 | 2 | 3 |
| 9 | 9 | 2 | $-6$ | 3 |
| 10 | 1 | 4 | 2 | 3 |

Total charges are $2+9\cdot3=29$. Actual work is 25 and final potential 4, so $29=25+4$. The accounting balance $B_i$ and potential $\Phi_i$ are identical in this refined scheme. Alternative valid charges may leave different amounts of unused credit; there is no unique numerical amortized charge inherent in the implementation.

## Cost-model changes and limits

### Charging allocation per slot

**Supplementary clarification prompted by the past-paper wording:** [[Past Exam Question Bank#AAPP-15-003]] explicitly charges a constant per allocated memory unit. The lecture's exact $c_i=i$ expansion count does not include that cost. The asymptotic conclusion survives, but exact constants must change.

For an illustrative model charging 1 per allocated slot, 1 per copy and 1 per inserted element, a full capacity-$m$ expansion costs $2m+m+1=3m+1$. The first allocation plus insertion costs 2. Summing all allocated capacities and copied capacities gives, for $n\ge1$,

$$
C_{\mathrm{alloc}}(n)
=n+3(m_n-1)+1=n+3m_n-2<7n.
$$

For ten insertions, write cost is 10, copy cost 15, and allocation cost $1+2+4+8+16=31$, totaling 56 rather than 25. This is an original model comparison, not an answer inserted into the question bank.

If a potential proof is desired for this model, use $\Phi'=6s-3m$ for nonempty states and zero initially. A nonexpanding insertion has charge $1+6=7$; an expansion has potential change $6-3m$, giving $(3m+1)+(6-3m)=7$. The first insertion has charge $2+3=5$. Total charges $7n-2$ minus final potential reproduce the same exact cost. Derive the constants from the model instead of memorizing “every append costs 3.”

### Why doubling matters

With a fixed multiplicative growth factor $g>1$, the copied capacities form a geometric sequence, so the total is still linear in final size, with constants depending on $g$. Growing by one slot each time instead copies $1+2+\cdots+(n-1)=\Theta(n^2)$ elements. The amortized technique exposes the policy's consequences; it does not make every resizing policy efficient.

The append-only model keeps capacity below twice the live size after the first insertion. Arbitrary insertion in the middle can still shift a linear number of records, regardless of spare capacity. Deletion, contraction and oscillation between grow/shrink thresholds require a different policy and proof. The supplied deck establishes no such extension.

Finally, starting from an arbitrary already-full table of capacity $M$ and counting only one following append can cost $\Theta(M)$. A sequence theorem must account for initial stored potential or initial construction cost; its empty-start assumption cannot be discarded.

## Takeaways

- Analyze legal cost sequences, not an impossible repetition of the single-operation maximum.
- Aggregate counting sums expensive events directly.
- Accounting proves credits never become negative on any prefix.
- Potential analysis packages those credits into a state function and telescopes.
- A negative potential **change** is useful; the required lower bound concerns potential itself.
- Exact charges depend on initial state, allocation model and supported operations.

## Exam practice

These are original exercises. Retrieved questions remain unanswered in [[Past Exam Question Bank#Amortized analysis]].

**1. Stop just after a resize.** Starting empty, perform 17 appends under the lecture's copy/write model. Compute total actual cost, final capacity and potential, and total refined amortized charge.

> [!faq]- Worked solution
> Capacity is 32. Copies total $1+2+4+8+16=31$, so actual cost is $17+31=48$. Potential is $34-32=2$. Charges are $2+16\cdot3=50$, confirming $50=48+2$. The seventeenth append itself costs 17, despite constant amortized cost.

**2. Diagnose a potential.** A proposed proof uses $\Phi=s-m$ for the same append-only table. Does it meet the lecture's nonnegative-potential condition?

> [!faq]- Worked solution
> No. Immediately after expansion to capacity 8 with size 5, it equals $-3$. The telescoping identity still holds algebraically, but the claimed upper-bound inequality does not follow from the stated conditions. Use $2s-m$ with the empty state treated separately, or prove a different valid lower-bound argument explicitly.

**3. Charge allocation explicitly.** In the illustrative per-slot allocation model above, compute total cost for $n=5$ and explain why quoting the slide's exact bound $3n$ would fail.

> [!faq]- Worked solution
> Capacity is 8. Final writes cost 5, copies cost $1+2+4=7$, and allocations cost $1+2+4+8=15$, totaling 27. This exceeds 15, although it is still linear in $n$. The appropriate exact expression is $n+3m_n-2=27$; the constant-7 amortized scheme covers it.

**4. Compare expectation and amortization.** Does proving expected constant cost over random inputs show that every sequence of $n$ operations has total $O(n)$ cost?

> [!faq]- Worked solution
> No. An expectation can average rare expensive outcomes with common cheap ones. An amortized sequence bound must control every allowed sequence under the stated starting state. The dynamic-table proof uses structural spacing of expansions, not a probability distribution.

## Revision questions

1. Why is the naive $n$ times worst-operation product loose?
2. What does the bank invariant require for every prefix?
3. How do intermediate potentials cancel?
4. Why is the first refined charge 2?
5. Does amortized constant time prevent a single linear-time append?
6. What extra proof is needed if contraction is added?

> [!faq]- Answer sketch
> 1. The table must refill before another large copy. 2. Total charges so far must cover all actual work so far. 3. Each interior potential appears once positively and once negatively. 4. Actual cost 1 plus potential rise from 0 to 1. 5. No; the expensive append is paid from earlier credit. 6. A grow/shrink policy and potential or aggregate argument that controls repeated reallocations across both operation types.
