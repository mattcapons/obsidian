---
tags:
  - aapp
  - lecture
lecture: "15"
source: "[[lezione15CompetitiveAnalysis.pdf]]"
---
# Competitive Analysis

[[AAPP Index|Course index]] · Previous: [[Amortized Analysis]] · Related: [[Randomized Algorithms#Where randomness comes from]] · [[Randomized Data Structures#Comparing guarantees]]

## Overview

An **online algorithm** serves requests as they arrive, without knowing future requests. Competitive analysis compares its total cost with the minimum cost achievable by an **offline** algorithm that knows the entire sequence. The benchmark faces the same requests and legal operations; its advantage is information about the future.

The lecture develops this idea through self-organizing lists and **move-to-front (MTF)**. Its main proof uses [[Amortized Analysis#Potential method|amortized potential analysis]] to establish a factor of 4 when every adjacent swap is paid. It then distinguishes the free-forward-move model, introduces paging and **least recently used (LRU)**, and compares LRU with offline **MIN**.

The supplied deck has 40 physical PDF pages. Its cover names Fabrizio Ferrandi and lecture 15, without an academic-year label. Repeated proof slides are consolidated here. Printed slide labels diverge from physical pages starting at PDF page 23; all references below use physical PDF pages.

Source: [[lezione15CompetitiveAnalysis.pdf#page=2|Roadmap]] · [[lezione15CompetitiveAnalysis.pdf#page=3|Lists and online analysis, pp. 3–13]] · [[lezione15CompetitiveAnalysis.pdf#page=14|MTF proof and qualifications, pp. 14–32]] · [[lezione15CompetitiveAnalysis.pdf#page=33|Paging, applications and references, pp. 33–40]].

## Self-organizing lists and the cost model

Maintain an **unsorted list** $L$ containing a fixed set of $n$ distinct items. A successful request $\operatorname{ACCESS}(x)$ scans from the head until it finds $x$. Define $\operatorname{rank}_L(x)$ as its one-based position. The charge for the search is this rank: accessing the first item costs 1, the fifth costs 5.

The algorithm may rearrange the list to make later accesses cheaper. In the lecture's **paid-exchange model**, each swap of two adjacent items costs 1. For a sequence $S=(x_1,\ldots,x_m)$, $C_A(S)$ includes all search costs and paid rearrangements made by algorithm $A$. The optimization target is the whole sequence's cost.

In the slide list $[12,3,50,14,17,4]$, accessing 14 costs 4. Swapping adjacent 3 and 50 costs 1 and gives $[12,50,3,14,17,4]$. The keys' numerical values do not determine their ranks: this list is not maintained in sorted order.

| Model | Search/service cost | Reordering rule | Guarantee discussed here |
|---|---|---|---|
| Paid list update | Rank $r$ | Every adjacent swap costs 1 | MTF is 4-competitive |
| Free-forward list update | Rank $r$ | After access, the accessed item may move toward the front for free; other swaps cost 1 | MTF is 2-competitive |
| Paging with $k$ frames | 0 for a hit, 1 for a fault | Maintain a resident set of at most $k$ pages | LRU is $k$-competitive against equal-capacity OPT |

![[aapp-lecture15-models.png|720]]

*The two list-update models charge the same search differently from the subsequent rearrangement. The theorem's factor must be paired with its cost model.* [[lezione15CompetitiveAnalysis.pdf#page=13|Source PDF page 13]].

**Scope and implementation assumptions:** the list proof concerns successful accesses to a fixed item set. The deck does not prove insertion/deletion extensions. A scan and adjacent swaps use $O(1)$ temporary storage beyond the $\Theta(n)$ list. Splicing a known node to the head can take constant pointer work in a suitable linked representation, but finding that node by scanning still costs $\Theta(r)$. A hash table of node addresses would change the search model. See [[Randomized Data Structures]] for dictionaries with different guarantees.

Source: [[lezione15CompetitiveAnalysis.pdf#page=3|Rank and swap charges, pp. 3–6]] · [[lezione15CompetitiveAnalysis.pdf#page=11|MTF's exact cost]] · [[lezione15CompetitiveAnalysis.pdf#page=30|Free-move interpretation]].

## Online, offline, and the role of the adversary

An online algorithm must finish serving the current request before learning the next. It can remember previous requests and modify its state. An offline algorithm receives the entire sequence in advance and can plan its rearrangements accordingly. **OPT** denotes the lowest total cost among legal offline strategies, rather than an implementable prediction mechanism.

Worst-case absolute cost can be uninformative when comparing list strategies. For any fixed deterministic online algorithm, an adversary can request its current tail item at every step. Each search then costs $n$, giving

$$
C_A(S)\ge mn=\Omega(mn).
$$

MTF itself uses at most $2n-1$ units per request, so its worst-case total is $\Theta(mn)$. This does not tell us whether a particular expensive sequence was also intrinsically expensive for OPT.

**Quantifier clarification:** for each deterministic strategy $A$, the adversary can construct a sequence $S_A$ that is bad for that strategy. The construction need not give the same sequence for every strategy. Once constructed, compare both $A$ and OPT on that same $S_A$. The tail argument observes the online list; it is not by itself a lower bound for randomized algorithms against a request sequence fixed independently of their random choices.

Nor does offline knowledge mean that OPT is strictly cheaper on every sequence. On repeated requests to the initial head, an online algorithm can already pay the minimum possible cost. The distinction is the ability to choose decisions using the unseen suffix. The slide's Tetris illustration motivates this information restriction; no Tetris algorithm or complexity result is developed.

Source: [[lezione15CompetitiveAnalysis.pdf#page=7|Online/offline definition]] · [[lezione15CompetitiveAnalysis.pdf#page=8|Tail adversary]] · [[lezione15CompetitiveAnalysis.pdf#page=9|Why compare against OPT?]].

## Average-case analysis and locality

Suppose each request is sampled independently with $\Pr[X=x]=p(x)$. For a **fixed list ordering**, the expected cost of one search is

$$
\mathbb E[\operatorname{rank}_L(X)]
=\sum_{x\in L}p(x)\operatorname{rank}_L(x).
$$

The best fixed ordering places larger probabilities earlier. To see why, let items $a,b$ occupy positions $i<j$ but have $p(a)<p(b)$. Their present contribution minus their contribution after exchange is

$$
[p(a)i+p(b)j]-[p(b)i+p(a)j]
=(p(b)-p(a))(j-i)>0.
$$

Removing such out-of-order pairs reduces the expected search cost until probabilities are in nonincreasing order. This exchange argument optimizes a fixed ordering's search cost; it does not make paid initialization free.

For an original numerical example, let $p(A)=0.6$, $p(B)=0.3$, and $p(C)=0.1$. Ordering $[C,A,B]$ has expected cost $0.1+1.2+0.9=2.2$, whereas $[A,B,C]$ costs $0.6+0.6+0.3=1.5$. For $m$ requests to an unchanged list, linearity gives $m$ times the one-search expectation. If the ordering changes, its rank function changes too; one must analyze the state at each request and include rearrangement charges.

> [!warning] Apparent notation error on PDF page 10
> The slide specifies one access to a fixed list, but labels the left side $\mathbb E[C_A(S)]$. Its right side is the expectation of **one search**, not a general sequence total. For $m$ requests with the list fixed and the same request distribution, the total expected search cost is $m\sum_xp(x)\operatorname{rank}_L(x)$. Paid reordering costs would be additional.

A popularity-count heuristic estimates $p(x)$ from historical frequencies. MTF instead reacts immediately to the most recent request. Bursts of requests to an item can make recent activity more useful than lifetime frequency. Competitive analysis supplies a guarantee that does not require choosing a probability distribution for those bursts. This is a different use of analysis from the expectations in [[Randomized Algorithms#Where randomness comes from]].

Source: [[lezione15CompetitiveAnalysis.pdf#page=10|Fixed-order expectation and popularity heuristic]] · [[lezione15CompetitiveAnalysis.pdf#page=11|Locality]]. The exchange calculation and numerical example are supplementary explanations of these slide claims.

## Move-to-front: algorithm and exact costs

After finding $x$, MTF moves it to the head while preserving the relative order of every other item.

```text
MTF-ACCESS(x)
    scan from the head to find x at position r
    while x is not the head:
        exchange x with its immediate predecessor
    return the item x
```

The scan returns the requested item, so rearrangement does not change the access's correctness. Each swap moves $x$ one position earlier. Exactly $r-1$ swaps place it at position 1, and no swap changes the relative order of two non-$x$ items. Thus the paid-model charge is

$$
c_i=r+(r-1)=2r-1\le2r.
$$

It is $\Theta(r)$ for that request and $\Theta(n)$ in the worst case. MTF needs no frequency counters or future requests. After every access, the list orders previously requested items from most recent to least recent; never-requested items retain their original relative order at the rear.

### A locality trace

Start with the slide list $[12,3,50,14,17,4]$ and use the original sequence $S=(14,14,3,14)$.

| Request | Rank before access | Search | Swaps | Paid cost | List after MTF |
|---|---|---|---|---|---|
| 14 | 4 | 4 | 3 | 7 | $[14,12,3,50,17,4]$ |
| 14 | 1 | 1 | 0 | 1 | $[14,12,3,50,17,4]$ |
| 3 | 3 | 3 | 2 | 5 | $[3,14,12,50,17,4]$ |
| 14 | 2 | 2 | 1 | 3 | $[14,3,12,50,17,4]$ |

Total paid cost is $7+1+5+3=16$. The free-forward model charges only the searches, totaling $4+1+3+2=10$. Leaving the original list fixed would cost $4+4+2+4=14$. MTF can exploit repetition and still lose on a short sequence; competitiveness is an upper bound relative to an optimum, not a promise to beat every alternative on every input.

Source: [[lezione15CompetitiveAnalysis.pdf#page=11|MTF rule and exact charge]].

## Competitive guarantees and the additive constant

For a minimization problem, $A$ is **$\alpha$-competitive** when there is a sequence-independent additive constant $\beta$ such that

$$
\forall S,\qquad C_A(S)\le\alpha C_{\mathrm{OPT}}(S)+\beta.
$$

The slide uses $k$ for this additive constant. Here it is renamed $\beta$ so that $k$ can consistently mean paging capacity later. The bound concerns the **same sequence** under the stated models and initial conditions. For the lecture's deterministic MTF theorem, no expectation appears.

The order of quantifiers matters: choose one fixed $\alpha$ and one permitted startup bound, then the inequality must hold for every finite sequence. Setting $\beta=C_A(S)$ separately for each input would make the definition meaningless. For a fixed $n$-item list, a startup bound may depend on $n$ and initial configurations but must not grow with $m=|S|$. The lecture's factor 4 is independent of both $m$ and $n$.

With identical initial lists, the proof below gives $\beta=0$. With different initial lists, it gives an explicit $O(n^2)$ term. A finite measured ratio, such as $16/14$ against the static strategy above, neither identifies $C_{\mathrm{OPT}}$ nor proves a competitive theorem.

Source: [[lezione15CompetitiveAnalysis.pdf#page=12|Definition]] · [[lezione15CompetitiveAnalysis.pdf#page=31|Startup term]] · [[lezione15CompetitiveAnalysis.pdf#page=32|Interpretation]].

## The inversion potential

Run MTF and a comparator on the same request sequence. Write $L_i$ and $L_i^*$ for their lists after request $i$ and the associated rearrangements. The comparator may be any legal strategy, including OPT. Define

$$
\Phi_i=\Phi(L_i,L_i^*)
=2\left|\{(x,y):x\prec_{L_i}y\text{ and }y\prec_{L_i^*}x\}\right|.
$$

Here $x\prec_Ly$ means “$x$ occurs before $y$ in $L$.” Each disagreeing **unordered item pair** contributes exactly once: its orientation in the set is determined by MTF's order. These are disagreements between lists, not comparisons of numerical keys.

![[aapp-lecture15-inversions.png|720]]

*MTF order $[E,C,A,D,B]$ and comparator order $[C,A,B,D,E]$ disagree on five pairs, so the weighted potential is 10.* [[lezione15CompetitiveAnalysis.pdf#page=18|Source PDF page 18]].

Four disagreements involve $E$: $(E,C),(E,A),(E,D),(E,B)$. The remaining one is $(D,B)$. Every other pair has the same order in both lists. Thus the count is 5, not 10; the factor 2 belongs to the definition of $\Phi$.

The potential is always nonnegative and is initially zero if the lists agree. One adjacent swap changes only the order of the two swapped items: every other item lies before both or after both. It therefore creates or removes exactly one disagreement, changing $\Phi$ by $+2$ or $-2$.

The weighting anticipates MTF's paid search-plus-swap cost, approximately $2r$. When many items blocking $x$ in MTF are already behind $x$ in the comparator, promoting $x$ removes many disagreements. That potential drop offsets an expensive scan. The potential is an analytical comparison of **two** evolving states; MTF does not compute OPT or maintain this number during execution.

Source: [[lezione15CompetitiveAnalysis.pdf#page=16|Intuition]] · [[lezione15CompetitiveAnalysis.pdf#page=17|Definition, example and swap effect, pp. 17–22]].

## Proving paid-model MTF is 4-competitive

### Partition the other items around the requested item

Immediately before accessing $x$, let $r$ and $r^*$ be its ranks in MTF and the comparator. Divide every other item into four disjoint sets:

| Set | Position relative to $x$ in MTF | Position relative to $x$ in comparator |
|---|---|---|
| $A$ | Before | Before |
| $B$ | Before | After |
| $C$ | After | Before |
| $D$ | After | After |

Consequently,

$$
r=|A|+|B|+1,\qquad
r^*=|A|+|C|+1,\qquad |A|\le r^*-1.
$$

The extra 1 counts $x$ itself. Symbols such as $A\cup B$ in the diagram identify which items precede $x$; they do not say that $A$ and $B$ are separate contiguous sublists.

![[aapp-lecture15-access-partition.png|720]]

*Only pairs involving $x$ change when MTF promotes it. The diagram separates common predecessors $A$ from MTF-only predecessors $B$.* [[lezione15CompetitiveAnalysis.pdf#page=25|Source PDF page 25; printed label 26]].

### Bound the potential change

First analyze MTF's move while holding the comparator list fixed. For every $y\in A$, both lists previously had $y$ before $x$; moving $x$ before $y$ creates one inversion. For every $y\in B$, the lists previously disagreed about $x,y$; moving $x$ before $y$ removes that inversion. Items in $C\cup D$ stay behind $x$ in MTF, and pairs not involving $x$ retain their order. The exact change from MTF is therefore $2(|A|-|B|)$.

Now allow the comparator to make $t_i\ge0$ paid adjacent swaps. Their total increase in potential is at most $2t_i$, even if some actually decrease it. Hence

$$
\Delta\Phi_i\le2(|A|-|B|+t_i),\qquad
c_i^*=r^*+t_i.
$$

Grouping swaps after accesses is analytical bookkeeping between independent executions. Any comparator swaps before the first access can instead be treated as separate events: MTF pays zero then, while its potential rises by at most twice the comparator's paid cost. They obey the same factor-4 bound.

### Eliminate MTF's rank from the amortized charge

As in the previous lecture, define $\widehat c_i=c_i+\Delta\Phi_i$. Using the slide's convenient upper bound $c_i\le2r$ gives

$$
\begin{aligned}
\widehat c_i
&\le 2r+2(|A|-|B|+t_i)\\
&=2r+2\bigl(|A|-(r-1-|A|)+t_i\bigr)\\
&=4|A|+2+2t_i\\
&\le4(r^*-1)+2+2t_i\\
&=4r^*-2+2t_i\\
&\le4r^*+4t_i=4c_i^*.
\end{aligned}
$$

The cancellation of $r$ is the crucial step: the large MTF rank has been replaced by the comparator's rank and paid swaps. The last inequality uses $t_i\ge0$. Keeping the exact cost $2r-1$ would improve the intermediate estimate to $4|A|+1+2t_i$; it is unnecessary for establishing factor 4.

### Telescope over the entire sequence

Summing $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$ and rearranging yields

$$
\begin{aligned}
C_{\mathrm{MTF}}(S)
&=\sum_{i=1}^{m}\widehat c_i+\Phi_0-\Phi_m\\
&\le4\sum_{i=1}^{m}c_i^*+\Phi_0-\Phi_m\\
&\le4C_{\mathrm{OPT}}(S)+\Phi_0.
\end{aligned}
$$

The final step chooses OPT as comparator and uses $\Phi_m\ge0$. With the same starting order, $\Phi_0=0$ and MTF is 4-competitive. No probability assumption or knowledge of OPT is needed by the algorithm. Amortization is the proof technique; competitiveness is the resulting relationship between two sequence costs.

For different starting orders, at most $\binom n2$ pairs disagree, so

$$
0\le\Phi_0\le2\binom n2=n(n-1).
$$

This supplies the slide's additive startup bound. It is constant with respect to sequence length for fixed list size, not a universal constant independent of $n$.

Source: [[lezione15CompetitiveAnalysis.pdf#page=23|Four-set partition and ranks, pp. 23–25]] · [[lezione15CompetitiveAnalysis.pdf#page=26|Amortized derivation and telescoping, pp. 26–29]] · [[lezione15CompetitiveAnalysis.pdf#page=31|Different initial lists]].

### A numerical potential drop

**Original worked instance:** suppose MTF has $[A,B,C,D,E]$, the comparator has $[E,A,B,C,D]$, and $x=E$. Here $r=5$, $r^*=1$, $A=\varnothing$, and $B=\{A,B,C,D\}$. Initial potential is 8. MTF pays $5+4=9$ and ends with the comparator's order, so $\Delta\Phi=-8$ and $\widehat c=9-8=1$.

If the comparator then swaps adjacent $A,B$, it pays one extra unit and creates one inversion. Final potential becomes 2. For this combined step, $t_i=1$, comparator cost is $1+1=2$, total potential change is $-6$, and MTF's amortized charge is $9-6=3\le4\cdot2$. A large actual MTF cost is compatible with a small amortized charge because the two lists began with stored disagreement.

## What 4-competitiveness does and does not imply

The theorem bounds the entire sequence. It does not say that every actual MTF request costs at most four times the corresponding OPT request, nor that every request takes constant time. An $O(1)$ competitive **factor** compares against a benchmark that may itself have a large total cost.

**Original stress test:** start from $[A,B,C,D,E]$ and request $E,D,C,B,A$, once each. MTF always finds the requested item at rank 5:

| Request | MTF list after access | MTF paid cost | Static comparator search cost |
|---|---|---|---|
| $E$ | $[E,A,B,C,D]$ | 9 | 5 |
| $D$ | $[D,E,A,B,C]$ | 9 | 4 |
| $C$ | $[C,D,E,A,B]$ | 9 | 3 |
| $B$ | $[B,C,D,E,A]$ | 9 | 2 |
| $A$ | $[A,B,C,D,E]$ | 9 | 1 |

MTF totals 45; leaving the list unchanged totals 15. That static comparator is actually optimal here. For every unordered pair, the initially later item is requested first. Either the pair's relative order was changed earlier by a paid adjacent swap, or the first search involving that pair must scan the initially earlier item. Thus each of the $\binom n2$ pairs forces at least one cost unit, in addition to the $n$ units for finding the requested items themselves. Static order achieves the resulting lower bound $n+\binom n2$.

For general $n$, reverse-order requests therefore give

$$
\frac{C_{\mathrm{MTF}}}{C_{\mathrm{OPT}}}
=\frac{n(2n-1)}{n(n+1)/2}
=4-\frac{6}{n+1}.
$$

These examples approach factor 4 as $n$ grows. On the final request in the five-item example, MTF pays 9 while this optimal static strategy pays 1: the pointwise factor-4 statement fails even though $45\le4\cdot15$ holds globally. The potential rises during early requests and falls during later ones, explaining why individual charges and actual costs differ.

Source connection: [[lezione15CompetitiveAnalysis.pdf#page=32|The theorem concerns totals]]. The stress test, lower bound and ratio calculation above are supplementary original derivations, not an exercise supplied by the lecturer.

## Free forward moves: why the factor becomes 2

Now change the model for **both** algorithms: after access, moving the accessed item toward the front is free, while other adjacent swaps cost 1. MTF pays only $r$ and uses the unweighted inversion potential $\Psi=\Phi/2$. For its access and promotion, the same partition gives

$$
r+\Delta\Psi=r+|A|-|B|=2|A|+1\le2r^*-1.
$$

The comparator's subsequent free forward moves cannot increase disagreements with MTF: $x$ is already first in MTF, so crossing a predecessor in the comparator removes a disagreement. Each paid comparator swap increases $\Psi$ by at most 1. Including $t_i$ paid swaps gives an amortized charge at most $2r^*-1+t_i\le2(r^*+t_i)$. Telescoping proves factor 2, with an initial-$\Psi$ term if starting orders differ.

**Supplementary proof detail:** the deck states this variant without deriving it. The original source distinguishes free and paid exchanges in §2 and discusses factors 2 and 4 in §5: [Sleator and Tarjan, *Amortized Efficiency of List Update and Paging Rules* (1985)](https://www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf). Changing the cost model also changes OPT; a free-model benchmark cannot be substituted into the paid-model derivation without justification.

Source: [[lezione15CompetitiveAnalysis.pdf#page=13|Model comparison]] · [[lezione15CompetitiveAnalysis.pdf#page=30|Free-forward addendum, pp. 30–31]].

## Paging: from recency order to LRU

Paging maintains a **cache** or fast memory holding at most $k\ge1$ equal-size pages. Requests arrive one at a time. A resident page is a **hit**, charged 0; a nonresident page causes a **fault**, charged 1. The requested page must be loaded, and a full cache must evict a resident page. We count faults, not comparisons, transfer bytes, or pointer updates. There is no free prefetching.

**LRU** evicts the resident page whose last request occurred furthest in the past. Keep resident pages in most-recent-to-least-recent order. On a hit, promote the page. On a miss, evict the tail if full and insert the new page at the head.

```text
LRU-REQUEST(x)
    if x is resident:
        promote x to the most-recent position
        return HIT
    if the cache contains k pages:
        evict its least-recently-requested page
    load x and put it in the most-recent position
    return FAULT
```

The invariant is that the cache contains the last $k$ distinct pages requested, or all distinct requested pages if fewer than $k$ have appeared. Hits and misses update this invariant directly: the current page becomes most recent, and only the oldest distinct page can fall outside the retained prefix.

![[aapp-lecture15-recency-cache.png|720]]

*The recency list begins $D,B,A,C,E,F$. With three frames, $D,B,A$ are resident. Requesting $E$ changes the resident order to $E,D,B$ and evicts $A$.* [[lezione15CompetitiveAnalysis.pdf#page=33|Source PDF page 33; printed label 35]].

One can conceptualize LRU as keeping the first $k$ entries of an MTF recency list over the page universe. Its request cost is the step function

$$
f(r)=\begin{cases}0,&r\le k,\\1,&r>k.\end{cases}
$$

An implementation need not store that entire universe-wide list. More importantly, this cost is not proportional to rank. For $k\ge2$, consecutive cost increments include $0,1,0$ around the threshold, so they do not form a nondecreasing sequence as discrete convexity would require. The lecture explicitly warns against reusing the list-update proof unchanged. The two policies share recency, but their cost functions and competitive factors differ.

Source: [[lezione15CompetitiveAnalysis.pdf#page=33|Recency connection]] · [[lezione15CompetitiveAnalysis.pdf#page=34|Paging cost and offline benchmark]].

## Offline MIN and the slide's full paging trace

**MIN**, also called farthest-in-future replacement, knows the remaining request sequence. At a fault with a full cache, it evicts the resident page whose next request is furthest in the future. A page never used again has next-use time $\infty$; ties may be broken arbitrarily. In the standard equal-size paging model this policy minimizes faults.

**Supplementary optimality intuition:** evicting a page needed later preserves pages needed sooner. An exchange argument can align an optimal schedule's first differing eviction with MIN without introducing an earlier extra fault, then repeat for later differences. The claim concerns total faults, rather than minimizing the next fault's service time. MIN is used as an offline benchmark, not as a prediction available to LRU. The original paging model and MIN reference are discussed in [Sleator and Tarjan (1985), §4](https://www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf#page=6).

For the slide sequence $A,B,C,D,A,B,C,D$, both caches have capacity 3 and start empty.

| Step | Request | LRU after request, most recent first | LRU result | MIN resident set | MIN result/eviction |
|---|---|---|---|---|---|
| 1 | $A$ | $[A]$ | Fault | $\{A\}$ | Fault; space available |
| 2 | $B$ | $[B,A]$ | Fault | $\{A,B\}$ | Fault; space available |
| 3 | $C$ | $[C,B,A]$ | Fault | $\{A,B,C\}$ | Fault; space available |
| 4 | $D$ | $[D,C,B]$ | Fault; evict $A$ | $\{A,B,D\}$ | Fault; evict $C$ |
| 5 | $A$ | $[A,D,C]$ | Fault; evict $B$ | $\{A,B,D\}$ | Hit |
| 6 | $B$ | $[B,A,D]$ | Fault; evict $C$ | $\{A,B,D\}$ | Hit |
| 7 | $C$ | $[C,B,A]$ | Fault; evict $D$ | $\{B,C,D\}$ | Fault; evict $A$ (tie with $B$) |
| 8 | $D$ | $[D,C,B]$ | Fault; evict $A$ | $\{B,C,D\}$ | Hit |

At step 4, $A,B,C$ next occur at steps 5, 6 and 7; MIN evicts $C$. At step 7, neither $A$ nor $B$ will be used again, so either is a valid victim. MIN's displayed state is a set, not a claim about recency order.

![[aapp-lecture15-paging-trace.png|720]]

*The complete source trace gives eight LRU faults and five MIN faults from empty caches. The note's table makes the eviction choices explicit.* [[lezione15CompetitiveAnalysis.pdf#page=35|Source PDF page 35; printed label 37]].

The first appearances of $A,B,C,D$ force at least four faults from an empty cache. With capacity 3, a page from $A,B,C$ must be evicted to load $D$; all three occur again. At least one further fault is necessary. Thus the displayed five-fault MIN schedule meets a lower bound and is optimal for this example, independently of the general theorem.

LRU misses on every request because each return to a page follows three different other pages. The observed ratio is $8/5=1.6$; this one sequence does not establish the worst-case ratio or contradict a factor-3 bound.

Source: [[lezione15CompetitiveAnalysis.pdf#page=35|Worked trace]] · [[lezione15CompetitiveAnalysis.pdf#page=36|Cyclic pattern and its limits]].

## LRU's competitive guarantee

Let $F_{\mathrm{LRU},k}(S)$ count faults with $k$ frames and $F_{\mathrm{MIN},h}(S)$ count offline-optimal faults with $h$ frames, where $1\le h\le k$. The lecture states

$$
F_{\mathrm{LRU},k}(S)
\le\frac{k}{k-h+1}F_{\mathrm{MIN},h}(S)+h.
$$

For $h=k$, the denominator is 1, giving

$$
F_{\mathrm{LRU},k}(S)\le kF_{\mathrm{OPT},k}(S)+k.
$$

Unlike paid-model MTF's factor 4, this factor grows with cache capacity. “$k$-competitive” bounds total faults over a sequence; it does not mean that LRU incurs $k$ faults per individual request. Each request causes at most one fault in this model.

If LRU has more capacity than the benchmark, the factor improves. For example, $k=4,h=2$ gives $4/3$ and additive term 2. If the two-frame optimum has 12 faults, the bound permits at most $(4/3)12+2=18$ faults for four-frame LRU. With $k=h=4$, the corresponding bound would instead be $4\cdot12+4=52$, but the optimum in that comparison is a **four-frame** optimum, so its fault count cannot be assumed to remain 12.

The additive term accommodates startup differences and is independent of sequence length for fixed capacities. Initial contents must still be stated for a trace. The source theorem allows initially different cache contents; retaining its $+h$ term is safe for the empty-cache example as well. Formula checked against [Sleator and Tarjan, Theorem 6, printed p. 207](https://www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf#page=6).

Source: [[lezione15CompetitiveAnalysis.pdf#page=37|Unequal-capacity and equal-capacity bounds]].

### Supplementary explanation of the equal-capacity bound

The slide states the theorem without a paging proof. A phase argument explains the factor $k$ for equal capacities under demand paging:

1. Divide requests into maximal consecutive phases containing at most $k$ distinct pages. Every phase except possibly the last contains exactly $k$.
2. LRU faults at most $k$ times per phase: once requested, a page cannot be evicted until $k$ other distinct pages are requested, which cannot happen inside that phase.
3. Consider requests strictly after a phase's first request through the next phase's first request. Immediately after the initial request, its page occupies a frame. The interval requests $k$ other distinct pages, so every $k$-frame strategy must fault at least once. These intervals are disjoint.

With $q$ phases,

$$
F_{\mathrm{LRU}}\le kq,\qquad F_{\mathrm{OPT}}\ge q-1,
\qquad F_{\mathrm{LRU}}\le kF_{\mathrm{OPT}}+k.
$$

Using disjoint intervals prevents charging the same OPT fault to two phase boundaries. This proves the equal-capacity statement, not the stronger unequal-capacity formula. Source: [CMU 15-451, Online Algorithms, §4, Theorem 3 and its proof, PDF pp. 7–8](https://www.cs.cmu.edu/~15451-f24/lectures/lecture19-online.pdf#page=7).

## Real systems and the model's limits

The final application slide connects recency to two implementations. **Linux Multi-Gen LRU** groups pages into generations with similar access recency to guide page reclamation; additional signals and feedback influence eviction. **Redis's approximate LRU** samples keys and retains candidate information instead of maintaining exact global LRU order. These descriptions were checked against the [official Linux Multi-Gen LRU documentation](https://docs.kernel.org/mm/multigen_lru.html) and [Redis documentation, Approximated LRU algorithm](https://redis.io/docs/latest/develop/reference/eviction/#approximated-lru-algorithm) on 2026-11-01.

These are applications of recency reasoning, not demonstrations that the ideal LRU competitive theorem applies to those implementations. Actual page/key sizes, observation costs, writeback costs and approximate choices can differ from the equal-size, unit-fault model. No operating-system configuration, Redis benchmark, or empirical speedup is established by the lecture.

Source: [[lezione15CompetitiveAnalysis.pdf#page=38|Implementation examples]] · [[lezione15CompetitiveAnalysis.pdf#page=39|Takeaways]] · [[lezione15CompetitiveAnalysis.pdf#page=40|References]]. No additional replacement policies or randomized paging algorithms are required by this supplied deck.

## Takeaways

- Online decisions depend on requests seen so far; OPT may use the complete future sequence.
- Worst-case absolute cost, probabilistic average cost, amortized charges, and competitive factors answer different questions.
- State the model: paid MTF costs $2r-1$ and has factor 4; free-forward MTF costs $r$ and has factor 2.
- MTF's potential counts pairwise disagreements with the comparator. The four-set partition makes the cancellation explicit.
- Telescoping gives a sequence guarantee; different initial states produce an additive initial-potential term.
- LRU retains a recency prefix but counts page faults. Its equal-capacity guarantee has factor $k$, with a separate proof.
- A worked trace illustrates a theorem; it cannot establish a universal competitive ratio by itself.

## Exam practice

These are original exercises with worked solutions. Historical prompts and your attempts remain in [[Past Exam Question Bank#Online algorithms and competitive analysis]].

**1. Trace both list models.** Start with $[A,B,C,D]$ and request $C,A,C,D$. Give every rank and final list, and calculate MTF's paid-model and free-forward totals. Compare with leaving the list unchanged.

> [!faq]- Worked solution
> Ranks are $3,2,2,4$. The successive lists are $[C,A,B,D]$, $[A,C,B,D]$, $[C,A,B,D]$, and $[D,C,A,B]$. Paid charges are $5,3,3,7$, totaling 18. Free-forward searches total $3+2+2+4=11$. A static list costs $3+1+3+4=11$. Equality with that static strategy in the free model does not identify the offline optimum or prove factor 2.

**2. Identify the four sets and account for a comparator swap.** MTF starts this step with $[A,B,C,D,E]$ and the comparator with $[C,A,E,B,D]$. Request $E$. The comparator then swaps its adjacent $B,D$. Find $A,B,C,D$ as sets (distinguish set names from item names), both ranks, the actual MTF cost, initial/final potential, and amortized charge.

> [!faq]- Worked solution
> Denoting the four sets by $\mathcal A,\mathcal B,\mathcal C,\mathcal D$ to avoid name collisions: $\mathcal A=\{C,A\}$, $\mathcal B=\{B,D\}$, and $\mathcal C=\mathcal D=\varnothing$. Thus $r=5$, $r^*=3$, and MTF costs 9. Initially the four inverted pairs are $(A,C),(B,C),(B,E),(D,E)$, giving $\Phi=8$. MTF's promotion creates two and removes two inversions, leaving potential 8. The comparator's $B,D$ swap adds one inversion, so final potential is 10. Hence $\Delta\Phi=2$ and $\widehat c=11$. Comparator cost is $3+1=4$, and $11\le4\cdot4$. The exact intermediate expression gives $4|\mathcal A|+1+2t_i=11$.

**3. Telescope with different initial states.** There are six items, initial potential is 12, final potential is 6, and OPT costs 40. What bound follows from the amortized factor-4 argument? What if only nonnegativity of final potential is known?

> [!faq]- Worked solution
> Since $\sum_i\widehat c_i\le160$, actual MTF cost is at most $160+12-6=166$. Without knowing the final value, use $\Phi_m\ge0$ to get 172. The universal six-item initial bound is $6\cdot5=30$, so the stated initial value 12 is legal and gives a sharper estimate. These are upper bounds, not exact costs.

**4. Page-fault trace with a different capacity.** Both two-frame caches start empty. Use $S=(A,B,A,C,A,B)$. Trace LRU and MIN, explaining every eviction and the final fault totals.

> [!faq]- Worked solution
> LRU's recency states are $[A]$, $[B,A]$, $[A,B]$, $[C,A]$, $[A,C]$, $[B,A]$. Its results are fault, fault, hit, fault, hit, fault: 4 faults. At the $C$ request, MIN keeps $A$ (needed next) and evicts $B$; at the final $B$ request it can evict either resident page, since no requests remain. MIN also has 4 faults. Four is optimal: $A,B,C$ each cause a compulsory fault, and after loading $C$ at least one of $A,B$ must be absent even though both will be requested again. The general bound $F_{\mathrm{LRU}}\le2F_{\mathrm{OPT}}+2=10$ is valid and loose.

**5. Find the missing phase argument.** A proposed LRU proof says: “Each phase plus the first request of the next phase contains $k+1$ pages, so OPT faults once per phase.” Explain the possible counting problem and repair it.

> [!faq]- Worked solution
> Those extended phases overlap at boundary requests; a fault at a shared boundary might be counted twice. Use disjoint intervals starting strictly after each phase's first request and ending with the next phase's first request. The cache already holds the excluded first page, and each interval requests $k$ other distinct pages. Without a fault those cannot all be served from the remaining $k-1$ frames. With $q$ phases, this gives $q-1$ distinct OPT faults, while LRU has at most $kq$, yielding $kF_{\mathrm{OPT}}+k$.

**6. Explain the advantage of future knowledge with correct quantifiers.** Two-frame demand-paging caches start empty. Reveal $A,B,C$. After an online strategy serves $C$, let an adversary choose a final request from $\{A,B\}$ that is absent from its cache. Compare its total faults with OPT. Why does this not produce one fixed sequence that defeats every online strategy?

> [!faq]- Worked solution
> The first three distinct pages force at least three faults. After $C$ is loaded, at most one of $A,B$ fits alongside it, so the adversary can request an absent page and force a fourth fault. OPT, knowing which final page will be needed, retains that page and evicts the other when loading $C$, giving exactly three faults. The continuation depends on the online strategy's eviction. For a fixed chosen sequence, a strategy can coincidentally make the offline-optimal choice; the claim is “for every strategy, some sequence,” not “one sequence defeats every strategy.” This argument uses the stated demand-paging model, with the requested page resident after service and no free prefetching.

## Revision questions

1. Why does repeatedly requesting the tail give a weak basis for distinguishing list strategies?
2. What exactly is random in the fixed-order expectation calculation?
3. Why does a single adjacent swap change the inversion count by only one?
4. Which terms cancel when the four-set bound is substituted into MTF's amortized cost?
5. What does the initial potential contribute when starting orders differ?
6. Why is a factor-4 sequence guarantee compatible with an individual cost ratio of 9?
7. Which page does MIN evict, and what does “never requested again” mean for that choice?
8. Why does LRU require a separate competitive proof and a capacity parameter?

> [!faq]- Answer sketch
> 1. Every deterministic strategy can be forced to pay $n$ per search, without showing how OPT fares on that same sequence. 2. The requested item is sampled using the specified $p(x)$; the list is fixed. 3. Only the swapped pair changes relative order. 4. The $2r$ search-and-swap bound cancels the $-2r$ obtained from $|B|=r-1-|A|$. 5. An additive $\Phi_0\le n(n-1)$ in the paid model. 6. Amortized charges telescope; individual actual costs need not satisfy the comparator bound. 7. The resident page whose next request is latest, treating no future request as infinity. 8. Its service cost is a hit/fault step function, and an equal-capacity offline comparison gives factor $k$ rather than a size-independent constant.
