---
tags:
  - aapp
  - lecture
lecture: "6"
source: "[[lecture6-MinCut.pdf]]"
---
# Minimum Cut

[[AAPP Index|Course index]] · Previous: [[Randomized Algorithms]] · Next: [[Sorting]]

## Overview

Karger's algorithm repeatedly contracts random edges until only two supernodes remain. It always returns a cut, but that cut need not be minimum. Karger–Stein improves the probability-versus-work tradeoff by sharing early contractions through recursion. This is a concrete application of [[Randomized Algorithms#Las Vegas and Monte Carlo]] and [[Divide and Conquer]].

Source: [[lecture6-MinCut.pdf#page=4|Problem and motivation, pp. 4–6]]. The supplied deck is labeled 2026–2027.

## Global cuts and s-t cuts

Let $G=(V,E)$ be a connected, undirected, unweighted graph with $n\ge2$ vertices and $m$ edges. For a **nonempty proper** subset $S\subset V$, write

$$
\delta(S)=\{\{u,v\}\in E:u\in S,\ v\in V\setminus S\},\qquad
k=\min_{\varnothing\ne S\subsetneq V}|\delta(S)|.
$$

The output is a partition $(S,V\setminus S)$ and its crossing edges. Opposite orientations describe the same cut. A cut need not split the graph into exactly two connected components. If the input is disconnected, a component and its complement give a zero cut; handle this before the connected-graph analysis.

An **s-t cut** must separate specified vertices $s,t$. The max-flow/min-cut theorem equates its minimum capacity to the maximum flow value (unit capacities here). To find a global cut through s-t computations, fix $s$ and try every other vertex $t$: every global minimum cut has some $t$ opposite $s$, while no s-t minimum can beat the global minimum.

> [!note] Historical comparison
> Page 5's “fastest” max-flow bound is presented with 1988/1992 references. Treat it as historical motivation, not a current algorithm ranking. No newer flow algorithms are required to understand this deck.

### Reading a cut as a partition

A cut chooses which vertices belong on each side; its size counts **edges crossing that boundary**, not vertices on a side. In a triangle $a,b,c$, the partition $\{a\}\mid\{b,c\}$ crosses $ab$ and $ac$, so it has size two. The edge $bc$ stays within the second side and does not count. The complementary description $\{b,c\}\mid\{a\}$ is the same undirected cut.

The graph may have many minimum cuts. In a cycle, removing any two distinct edges separates two arcs, so each such pair describes a size-two minimum cut. Karger's output need not be a particular one to be correct; fixing one cut in the proof is a way to analyze success without having to classify all of them.

The condition $\varnothing\ne S\subsetneq V$ rules out the uninteresting zero crossing count obtained by putting every vertex on one side. Connectedness ensures that every permitted cut has at least one edge, allowing the positive-$k$ division in the probability proof.

## Contraction and the invariant

Contracting $\{u,v\}$ merges its endpoints into a supernode representing the union of their original vertices. Redirect incident edges, keep **parallel edges with their multiplicities**, and delete self-loops. Sampling is uniform over edge copies, not distinct pairs of supernodes.

![[aapp-lecture6-contraction.png|720]]

*Contraction merges vertices 1 and 2. The resulting parallel edges retain the original crossing-edge counts.* [[lecture6-MinCut.pdf#page=8|Source slide 8]].

Every cut of the contracted graph lifts to a cut of the original graph with the same size. Conversely, an original cut survives a contraction exactly when the contracted endpoints lie on the same side. Thus contraction cannot introduce a smaller cut, but it can destroy the optimum we hoped to preserve.

```text
KARGER(G)
    H = a fresh copy of G; each vertex records its original members
    while number of vertices in H > 2
        choose an edge copy uniformly from the non-loop edges of H
        merge its endpoints; preserve parallel edges; remove self-loops
    return the two member sets and the edges crossing between them
```

The loop terminates after $n-2$ contractions. The membership invariant ensures that the output is a valid partition of the original vertices. There is no general optimality certificate supplied by this procedure: checking that a cut has size $c$ does not prove $c=k$.

Source: [[lecture6-MinCut.pdf#page=7|Multigraphs, contraction and algorithm, pp. 7–12]].

### What “lifting” a cut means

Suppose current supernodes are $U=\{a,b\}$, $V=\{c\}$, and $W=\{d,e\}$. A current partition $\{U,V\}\mid\{W\}$ represents the original partition $\{a,b,c\}\mid\{d,e\}$. Each edge crossing between these supernodes corresponds to one original crossing edge, so its multiplicity contributes exactly the right amount to the cut size.

An internal edge, such as $ab$ after $a,b$ merge, can never cross any later partition of the supernodes: its endpoints are permanently together. It becomes a self-loop and can be discarded. If both $ac$ and $bc$ existed before the merge, they become two edges from $U$ to $V$. Merging them into a single unweighted edge would reduce the crossing count from two to one and corrupt both the output size and the sampling probability.

In this sense, contraction restricts the family of allowable partitions: it rules out partitions that separate the merged endpoints. Minimizing over a smaller set cannot lower the optimum. The algorithm hopes that at least one original optimum stays in that smaller set until the end.

### Worked success and failure

Consider two triangles $\{a,b,c\}$ and $\{d,e,f\}$ joined by the single bridge $cd$. The minimum cut is $\{cd\}$, of size one. Contract $ab$, then $\{a,b\}c$, then $de$, then $\{d,e\}f$: the final supernodes are the triangles, and the bridge is returned. Internal parallel edges become loops and are removed when their endpoints merge.

If $cd$ is contracted first, its endpoints can never be separated later. The unique size-one cut is lost, so the final cut has size at least two. The first-step failure probability for this target cut is $1/7$, since there are seven edges. The universal bound below is deliberately more conservative.

![[aapp-depth-mincut-bridge.png|720]]

*Original diagram of the two-triangle example. The bridge is the unique minimum cut; contracting internal edges preserves it, while contracting the bridge makes its separation impossible.*

The two-triangle trace is deliberately simpler than the slide's larger graph. At each merge, write the set of original members inside the supernode and count all surviving edge copies. That makes both cut reconstruction and any accidental loss of multiplicity visible.

## Success probability

Fix **one particular** minimum cut $C$ of size $k$. With $r$ supernodes remaining, every supernode has degree at least $k$: otherwise its incident edges would lift to an original cut smaller than $k$. The degree sum therefore implies

$$
|E_r|\ge\frac{rk}{2}.
$$

Condition on $C$ having survived so far. All its $k$ edges remain, so

$$
\Pr(\text{hit }C\mid\text{survival so far})=\frac{k}{|E_r|}\le\frac2r.
$$

Use the chain rule for conditional probabilities, **not independence of contractions**:

$$
\Pr(\text{return }C)\ge\prod_{r=n}^{3}\left(1-\frac2r\right)
=\frac{n-2}{n}\frac{n-3}{n-1}\cdots\frac13
=\frac{2}{n(n-1)}=\binom n2^{-1}.
$$

If $C$ survives to two supernodes, neither side could have been merged with the other, and both sides are nonempty, so the final partition is exactly $C$. Finding *any* minimum cut is at least as likely as finding this fixed one. The formula is a lower bound, not necessarily the actual success probability.

> [!warning] Apparent wording error on slide 13
> The proof says “upper bound” the probability of success. The edge-count argument establishes a **lower bound** on survival/success; it upper-bounds the chance of contracting a target cut edge.

Source: [[lecture6-MinCut.pdf#page=13|Survival proof, pp. 13–15]].

### Unpacking the probability product

For $n=6$, the universal survival factors for a chosen optimum are:

| Supernodes before contraction | Conditional probability of avoiding the cut, at least |
|---|---|
| 6 | $1-2/6=2/3$ |
| 5 | $1-2/5=3/5$ |
| 4 | $1-2/4=1/2$ |
| 3 | $1-2/3=1/3$ |

Their product is $(2/3)(3/5)(1/2)(1/3)=1/15$. Every row assumes all earlier contractions avoided the same target cut. Without that condition the cut may already be destroyed, and counting its original $k$ edges as surviving would be unjustified.

The degree argument does not require knowing $k$ while running the algorithm. The algorithm simply samples and contracts. The proof introduces the unknown optimal value to establish a guarantee. This separation between information used by an algorithm and information used in its analysis is common in randomized algorithms.

Also, the conditional bound can be loose: the current multigraph may have many more than $rk/2$ edges, making the true chance of hitting the target less than $2/r$. We multiply guaranteed lower bounds to obtain a guarantee that works for every graph under the assumptions, not an exact prediction for one particular graph.

## Repetition and running time

Run fresh, independent trials on the **original graph** and retain the smallest returned cut. With $p_0=2/[n(n-1)]$ and $R$ trials,

$$
\Pr(\text{all trials fail})\le(1-p_0)^R\le e^{-p_0R}.
$$

It suffices to choose

$$
R=\left\lceil\binom n2\ln(1/\delta)\right\rceil
$$

for error at most $\delta\in(0,1)$. For $\delta=n^{-c}$, this is $O(n^2\log n)$ trials. A returned cut cannot be smaller than the optimum, so choosing the minimum safely combines the trials; majority voting is inappropriate for this optimization problem.

The lecture assumes $O(n^2)$ time per trial, giving $O(n^4\log n)$ time at polynomially small error.

**Supplementary implementation detail:** a multiplicity matrix uses $O(n^2)$ storage. Choose a vertex with probability proportional to its degree, then a neighbor proportional to multiplicity; every undirected edge copy has probability $1/m$. Linear scans select an edge in $O(n)$, and merging rows/columns takes $O(n)$. Across $n-2$ contractions this realizes $O(n^2)$ time under unit-cost integer arithmetic. Rebuilding a full $n^2$-entry sampling table at every contraction would instead cost $O(n^3)$ per trial.

For $n=6$, $p_0=1/15$. To guarantee error at most $0.01$, the exponential bound gives $R=\lceil15\ln100\rceil=70$. Directly solving $(14/15)^R\le0.01$ gives $R=67$. Both are valid sufficient budgets from the universal bound; neither asserts that this many trials are necessary for every six-vertex graph.

Source: [[lecture6-MinCut.pdf#page=16|Amplification and runtime]].

### Why taking the best of repeated runs works

Imagine independent trials return cut sizes 5, 4, 6, 4, and 3. The best-so-far values are 5, 4, 4, 4, and 3. If the true optimum is 3, the final result is correct because a successful trial occurred; no later feasible output can invalidate that optimum. If the true optimum were 2, the same observations would not prove success. The guarantee is probabilistic, not a certificate inferred from apparent stabilization.

The bound $1-x\le e^{-x}$ converts a product into a convenient exponential. To require $e^{-p_0R}\le\delta$, take natural logarithms: $-p_0R\le\ln\delta$. Since $p_0>0$, this gives $R\ge\ln(1/\delta)/p_0$. Decreasing the desired error by a fixed factor therefore adds a fixed multiple of $1/p_0$ trials. Asking for zero failure cannot be achieved by choosing a finite budget through this bound.

Independent trials can be executed concurrently, but doing so reduces elapsed time only if sufficient resources are available; it does not reduce the total number of trial operations. The lecture's complexity bounds here are sequential time/work bounds, not a PRAM implementation of min-cut.

## Karger–Stein

### Stop early and branch

The most dangerous contractions are near the end, when the bound $2/r$ is large. Contract only to

$$
t=\left\lceil1+\frac n{\sqrt2}\right\rceil
$$

supernodes, independently twice, and recursively solve both resulting multigraphs. Return the smaller cut, retaining original vertex memberships.

![[aapp-lecture6-recursion.png|720]]

*Two independent partial contractions give two recursive opportunities to preserve a minimum cut.* [[lecture6-MinCut.pdf#page=20|Source slide 20]].

```text
FAST-MIN-CUT(G)
    n = number of vertices in G
    if n <= 6
        return an exact minimum cut by enumerating nontrivial partitions
    t = ceil(1 + n / sqrt(2))
    H1 = contract a fresh copy of G to t vertices
    H2 = independently contract another fresh copy of G to t vertices
    C1 = FAST-MIN-CUT(H1)
    C2 = FAST-MIN-CUT(H2)
    return the smaller lifted cut among C1 and C2
```

> [!warning] Apparent base-case error on slide 19
> The slide uses $n<6$. But at $n=6$, $\lceil1+6/\sqrt2\rceil=6$, so neither branch shrinks and recursion can continue forever. Use $n\le6$ for exact enumeration. Also, `mincut(V)` must inspect the graph's edges/multiplicities, not only its vertex set.

At constant size, exact enumeration is constant-time in this model: fix one vertex on one side to avoid counting complements twice and test the $2^{n-1}-1$ nontrivial partitions. For $n=6$, that is 31 partitions.

Source: [[lecture6-MinCut.pdf#page=17|Motivation, algorithm and branching, pp. 17–20]].

### Why the threshold is about n divided by the square root of two

Partial survival is approximately $(t/n)^2$ when $n$ is large. To retain the target with probability around one half, choose $t/n\approx1/\sqrt2$. The extra 1 and ceiling make the stated finite-size inequality hold; they are not the source of the asymptotic improvement.

For $n=20$, $t=\lceil1+20/\sqrt2\rceil=16$, and partial survival is at least $16\cdot15/(20\cdot19)=12/19\approx0.632$. Both children have 16 supernodes, but usually different memberships and edges because their contraction choices differ. Recursion then uses sizes $16\to13\to11\to9\to8\to7\to6$, where exact enumeration stops it.

Fresh copies are essential. If the first `contract` mutates the only graph and the second begins from that already-contracted graph, the two children do not represent independent attempts from the parent's state. The probability recurrence would no longer describe the program.

### Partial survival and recursive success

The same telescoping product, stopped at $t$, gives

$$
\Pr(C\text{ survives to }t)\ge\prod_{r=n}^{t+1}\frac{r-2}{r}
=\frac{t(t-1)}{n(n-1)}\ge\frac12.
$$

Survival only means the recursive instance still contains the target optimum; it does **not** mean the recursive algorithm has already found it. If $P(t)$ is a lower bound on recursive success, each independent branch succeeds with probability at least $P(t)/2$. Therefore

$$
P(n)\ge1-\left(1-\frac{P(t)}2\right)^2.
$$

**Supplementary derivation of the lecture's $\Omega(1/\log n)$ bound:** let $h$ be the maximum remaining recursion depth, and take $q_0=1$, $q_h=q_{h-1}-q_{h-1}^2/4$ as a lower-bound sequence. The function $f(x)=x-x^2/4$ is increasing on $[0,1]$. Inductively $q_h\ge1/(h+1)$: from $q_{h-1}\ge1/h$,

$$
f(q_{h-1})\ge\frac1h-\frac1{4h^2}\ge\frac1{h+1}\quad(h\ge1).
$$

The rounded subproblem size is $n/\sqrt2+O(1)$ and shrinks for $n>6$, hence $h=O(\log n)$. This yields the claimed success lower bound. The recurrence and amplification are corroborated by [Vigoda's university lecture notes, §1.3](https://sites.cs.ucsb.edu/~vigoda/6550/Notes/Lec1.pdf).

To read $1-(1-P(t)/2)^2$, first lower-bound a single branch's success by “survive the partial contraction **and then** succeed recursively.” Its probability is at least $P(t)/2$. The chance that a branch fails is therefore at most $1-P(t)/2$. Independent random choices in the two branches allow their failure bounds to multiply. Subtracting the probability that both fail gives the chance that at least one succeeds.

For example, if recursive success were only $1/4$, a branch would succeed with probability at least $1/8$, and two branches would give at least $1-(7/8)^2=15/64$, not $3/4$. The latter value would incorrectly treat preservation of the cut as completed discovery of it.

### Time for one run versus amplified time

With quadratic partial-contraction work,

$$
T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n).
$$

Ignoring constant rounding, the Master theorem has $a=2$, $b=\sqrt2$, so $\log_ba=2$. Equivalently each level has $O(n^2)$ work across its branches and there are $O(\log n)$ levels. Sequential depth-first execution with matrix copies can use $O(n^2)$ peak graph storage: sizes squared decrease geometrically along the active recursion path.

Since one full recursive run succeeds with probability $\Omega(1/\log n)$, $O(\log n\log(1/\delta))$ independent full runs suffice. Thus the amplified bound is

$$
O(n^2\log^2 n\log(1/\delta)),
$$

or $O(n^2\log^3 n)$ when $\delta=n^{-c}$. For constant error, the corresponding bound is $O(n^2\log^2 n)$. Do not attach the amplified bound to a single call.

Source: [[lecture6-MinCut.pdf#page=21|Runtime and success recurrences]].

### Accounting for the recursive work by levels

Ignoring rounding, level $\ell$ has $2^\ell$ calls on graphs of size $n/(\sqrt2)^\ell$. Quadratic work per call yields

$$
2^\ell\left(\frac{n}{(\sqrt2)^\ell}\right)^2=n^2.
$$

The branching factor doubles the number of calls, but their squared sizes halve, so total work per level stays of the same order. There are logarithmically many levels, giving the extra $\log n$ in one full recursive run. Two additional logarithmic factors in the polynomial-error bound come from repeating a run whose success is only order $1/\log n$, and from demanding an error inverse-polynomial in $n$.

These are different mechanisms. The recurrence itself explains the cost of exploring the recursion tree; amplification explains how many independently randomized trees must be explored.

## How many minimum cuts can there be?

If there are $M$ distinct minimum cuts (identifying complements), one run returns each particular cut with probability at least $1/\binom n2$. These output events are disjoint, so

$$
1\ge\sum_{C\text{ minimum}}\Pr(\text{return }C)\ge M/\binom n2,
\qquad M\le\binom n2.
$$

**Supplementary clarification:** enumeration by random trials is probabilistic. A union bound gives probability at most $M e^{-R/\binom n2}$ that some minimum cut is missed after $R$ trials. Merely seeing the same cut repeatedly does not certify that all have been found. This counting argument assumes the connected, positive-minimum-cut setting of the lecture; disconnected zero-cut graphs can have exponentially many minimum partitions.

Source: [[lecture6-MinCut.pdf#page=22|Minimum-cut counting corollary]]. Pages 23–24 provide references and acknowledgments.

## Takeaways

- Preserve edge multiplicities and sample edge copies uniformly.
- Conditional survival probabilities multiply even though contractions are dependent.
- A valid output cut is not automatically an optimal cut.
- State separately single-run work, success probability, and repetition budget.
- Karger–Stein spends more effort on the risky later contractions.

## Exam practice

These are original problems based on this deck, not past exam questions.

**1. Sampling pitfall.** A multigraph has four copies of $AB$, one of $AC$, and one of $BC$. What is the probability of contracting the pair $AB$? What goes wrong if distinct pairs are sampled uniformly?

> [!faq]- Worked solution
> Uniform edge-copy sampling gives $4/6=2/3$. Uniform pair sampling gives $1/3$ and changes the distribution used in the proof. Multiplicities encode original crossing edges and cannot be discarded.

**2. Budget a run.** For $n=10$, obtain a conservative repetition budget giving failure at most $10^{-3}$, and explain the conditional probability at a stage with five supernodes.

> [!faq]- Worked solution
> $p_0=2/(10\cdot9)=1/45$, so $R=\lceil45\ln1000\rceil=311$. Conditional on survival, the chance of destroying the chosen cut at five supernodes is at most $2/5$; survival at that step is at least $3/5$. This is not an independence assertion about successive steps.

**3. Diagnose the recursion.** Apply the slide's threshold literally at $n=6$. Then explain why two partial contractions do not establish constant overall success.

> [!faq]- Worked solution
> The slide does not enter its $n<6$ base case, and computes $t=6$, so recursion does not shrink. Changing the base case to $n\le6$ repairs termination. A partial contraction preserves the target with probability at least $1/2$, but its recursive call can still fail. Branch success is bounded below by $P(t)/2$, not $1/2$.

**4. Separate preservation from discovery.** At a recursive node with $n=20$, compute $t$ and its partial-survival lower bound. If recursive success is at least $1/4$, use the simpler $1/2$ preservation bound to combine two branches.

> [!faq]- Worked solution
> $t=16$ and survival is at least $16\cdot15/(20\cdot19)=12/19$. Using the weaker $1/2$, each branch succeeds with probability at least $1/8$, so two independent branches succeed with probability at least $15/64$. The recursive call can fail even after the optimum survived the initial contraction.

## Revision questions

1. Why does a supernode of degree below $k$ contradict the original optimum?
2. Why remove loops but retain parallel edges?
3. Why retain the smallest result rather than use majority vote?
4. Which probability calculation needs independent trials?
5. What distinguishes $O(n^2\log n)$ from $O(n^2\log^3 n)$ here?

> [!faq]- Answer sketch
> 1. Separating its original member set yields a smaller original cut.
> 2. Loops cross no partition; parallel edges still contribute separately to its size.
> 3. All candidates are feasible cuts, and none can underestimate the optimum.
> 4. Amplification across fresh runs and the two independently randomized branches; within a contraction path use conditioning.
> 5. One recursive run versus enough independent recursive runs for polynomially small error.
