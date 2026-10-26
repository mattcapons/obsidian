---
tags:
  - aapp
  - lecture
lecture: "5"
source: "[[lecture5-Randomization.pdf]]"
---
# Randomized Algorithms

[[AAPP Index|Course index]] · Previous: [[ISPC]] · Next: [[Minimum Cut]] · Related: [[Algorithm as recipes#Input size and running time]]

## Overview

This deck introduces the distinction between randomness in the input model and randomness controlled by the algorithm. It develops the hiring problem with indicator variables, then compares Las Vegas and Monte Carlo algorithms using random sampling.

The key analytical habit is to say **what is random, what is fixed, and what guarantee is being measured**.

Source: [[lecture5-Randomization.pdf#page=2|Two sources of randomness, pp. 2–5]].

## Where randomness comes from

### Average-case or probabilistic analysis

The algorithm is deterministic. A probability distribution is assumed over inputs, and the cost is averaged over that distribution:

$$
\mathbb E_{x\sim D}[T(x)].
$$

For a fixed input, execution behaves the same way each time. The result depends on whether distribution $D$ models the actual workload.

### Randomized algorithm

The algorithm makes random choices during execution. Write $T(x,R)$, where $x$ is the fixed input and $R$ is the random choice sequence:

$$
\mathbb E_R[T(x,R)].
$$

A strong expected-time guarantee holds for **every fixed input**, averaging only over $R$. For example, the algorithm can randomize a candidate order rather than assume it was random initially.

![[aapp-lecture5-randomness-sources.png|720]]

*Separate a random input model from random choices made by the algorithm on a fixed input.* [[lecture5-Randomization.pdf#page=2|Source slide 2]].

| Question | Average-case analysis | Randomized algorithm |
|---|---|---|
| What varies? | Input drawn from a distribution | Random choices during execution |
| Can the same input yield different runs? | Not for a deterministic algorithm | Yes |
| Who supplies randomness? | The assumed workload model | The algorithm |

> [!note] Expectation and high probability
> A small expected cost does not by itself establish a high-probability bound. The hiring derivation in this deck proves an expectation; a stronger tail guarantee needs additional analysis. Likewise, a randomized algorithm is not automatically efficient merely because it uses random choices.

### Fixing the input before taking an expectation

Imagine the applicant ranks arrive in the fixed order $[1,2,3,4]$, with larger ranks better. Without shuffling, four hires occur every time. The random-input analysis does not change that execution; it says that this order is only one outcome among uniformly weighted permutations. After a uniform shuffle, however, this same fixed list can yield any order, so its **randomized execution** has expected hire count $H_4$.

The order of the statements matters: a worst-case expected bound means that for every fixed input, the expectation over random choices is small. It does not mean one lucky random choice works well on every input, and it does not mean every run is fast. In symbols, bounding $\max_x\mathbb E_R[T(x,R)]$ does not bound $\max_{x,R}T(x,R)$ by the same quantity.

A probability model must also specify what the elementary outcomes are. In the hiring analysis they are complete permutations; in repeated sampling they are sequences of sampled indices. An event, such as “the third arrival is hired,” is a subset of those outcomes. A random variable assigns a number, such as a hire count, to each outcome.

## Indicator variables

For an event $E_i$, define

$$
X_i=\begin{cases}1&\text{if }E_i\text{ occurs},\\0&\text{otherwise}.
\end{cases}
$$

Then

$$
\mathbb E[X_i]=1\Pr(E_i)+0\Pr(\neg E_i)=\Pr(E_i).
$$

If a total count can be written as $X=\sum_iX_i$, **linearity of expectation** gives

$$
\mathbb E[X]=\sum_i\mathbb E[X_i]=\sum_i\Pr(E_i).
$$

No independence assumption is required for this equality. Independence matters for other calculations, such as multiplying the probabilities of repeated sampling failures.

### Why dependence does not invalidate linearity

**Supplementary proof for a finite sample space:** write both variables on the same outcomes $\omega$:

$$
\mathbb E[X+Y]
=\sum_\omega (X(\omega)+Y(\omega))\Pr(\omega)
=\mathbb E[X]+\mathbb E[Y].
$$

This distributes a sum; it never replaces a joint probability with a product. For example, let $X$ indicate heads on one fair coin and let $Y=1-X$. They are dependent, but $\mathbb E[X+Y]=1=1/2+1/2$. Independence is needed for the general product rule $\mathbb E[XY]=\mathbb E[X]\mathbb E[Y]$, not for linearity. [Aspnes's Yale notes on random variables, §§3.2–3.3](https://www.cs.yale.edu/homes/aspnes/pinewiki/RandomVariables.html).

Source: [[lecture5-Randomization.pdf#page=5|Analysis tools]] · [[lecture5-Randomization.pdf#page=12|Indicators, pp. 12–13]].

### Building an indicator analysis rather than guessing a formula

Start with the quantity being counted. If it counts objects or events, give each candidate event a 0/1 indicator. Check that the total really is their sum on **each individual execution**, before taking any expectation. Then find each event probability using symmetry, counting, or conditioning; finally add those probabilities.

For the dependent coin example above, $XY=0$ on every outcome because one of $X,Y$ is zero. Thus $\mathbb E[XY]=0$, while $\mathbb E[X]\mathbb E[Y]=1/4$. This explicitly shows why a valid sum rule cannot be reused as a product rule. By contrast, $X+Y=1$ on every outcome, and its expected value is exactly the sum of the two expectations.

If events have different costs, write $C=\sum_i c_iX_i$ with fixed costs $c_i$, giving $\mathbb E[C]=\sum_i c_i\Pr(X_i=1)$. This is the same method as the hiring cost model below, with costs attached to events instead of merely counting them.

## The hiring problem

### Setup and algorithm

Interview $n$ applicants in sequence. Hire an applicant whenever they are better than everyone interviewed so far. Replacing the current hire is assumed expensive.

The analysis assumes distinct applicant quality ranks, so every prefix has a unique best applicant. Ties would require a stated comparison and tie-breaking rule.

```text
HIRE-ASSISTANT(applicants)
    best = NONE
    for each applicant in the given order
        interview applicant
        if best == NONE or applicant is better than best
            hire applicant
            best = applicant
```

**Correctness invariant:** after processing the first $i$ applicants, `best` is the highest-quality applicant in that prefix. If the next applicant is better, replacing `best` preserves the invariant; otherwise retaining it preserves the invariant. At the end, the final hire is the best overall.

The problem is to analyze **how many hires occur**, not whether the final choice is correct.

### Best and worst orders

- Best applicant first: exactly one hire.
- Increasing quality order: every applicant sets a new record, so $n$ hires.

Every applicant is still interviewed in either case.

![[aapp-lecture5-hiring-worst-case.png|720]]

*Increasing applicant quality forces a replacement at every step: this execution makes n hires.* [[lecture5-Randomization.pdf#page=8|Source slide 8]].

Source: [[lecture5-Randomization.pdf#page=7|Problem and extreme orders, pp. 7–9]].

### Uniform random ordering

Assume all $n!$ permutations of the distinct applicants are equally likely. Let $X_i$ indicate that the applicant at **position $i$** is hired. The subscript is an arrival position, not a fixed applicant identity.

![[aapp-lecture5-hiring-indicators.png|720]]

*Represent each hiring event by 1 and each non-hiring event by 0; their sum is the total number of hires.* [[lecture5-Randomization.pdf#page=12|Source slide 12]].

The applicant at position $i$ is hired precisely when they are the best of the first $i$ applicants. Under a uniform ordering, this maximum is equally likely to be in any of those $i$ positions:

$$
\Pr(X_i=1)=\frac1i.
$$

For $n=4$ and $i=3$, the third arrival is best among the first three in $8$ of $24$ orders, yielding $1/3$.

Apply linearity:

$$
\begin{aligned}
\mathbb E[X]
&=\mathbb E\left[\sum_{i=1}^nX_i\right]\\
&=\sum_{i=1}^n\mathbb E[X_i]\\
&=\sum_{i=1}^n\frac1i=H_n.
\end{aligned}
$$

The harmonic sum satisfies

$$
\ln(n+1)\le H_n\le1+\ln n,
$$

so $\mathbb E[X]=\Theta(\log n)$.

**Supplementary explanation of the upper bound:** compare the decreasing function $1/x$ with rectangles: $\sum_{i=2}^n1/i\le\int_1^n dx/x=\ln n$.

For $n=4$, $H_4=1+1/2+1/3+1/4=25/12\approx2.083$ expected hires. This can be fractional because it averages integer counts over many orders.

**Distinguish position from identity:** the probability $1/i$ concerns the applicant arriving at position $i$. An applicant of fixed quality rank has a different hiring probability. This derivation uses symmetry among the first $i$ arrival positions; it does not assign the same hiring probability to every applicant.

**Worked execution:** quality ranks $[3,1,4,2,5]$ produce hires at positions $1,3,5$. The indicators are $[1,0,1,0,1]$ and their sum is $3$. One run need not equal the expectation over random orders.

Source: [[lecture5-Randomization.pdf#page=10|Sample space, pp. 10–11]] · [[lecture5-Randomization.pdf#page=14|Probability and expectation, pp. 14–16]].

### A complete three-applicant sample space

Let rank 3 be best. Listing all six equally likely orders makes the expectation tangible:

| Order | Hire indicators by position | Number of hires |
|---|---|---|
| 1, 2, 3 | 1, 1, 1 | 3 |
| 1, 3, 2 | 1, 1, 0 | 2 |
| 2, 1, 3 | 1, 0, 1 | 2 |
| 2, 3, 1 | 1, 1, 0 | 2 |
| 3, 1, 2 | 1, 0, 0 | 1 |
| 3, 2, 1 | 1, 0, 0 | 1 |

The direct average is $11/6$. Summing column averages gives $1+3/6+2/6=1+1/2+1/3=11/6$ too. The indicator argument obtains the same answer without listing $n!$ rows for general $n$.

Why does $1/i$ not depend on $n$? Once the set of the first $i$ applicants is fixed, their relative order is uniform. Its best member is equally likely to occupy each of those $i$ positions. Applicants who have not arrived cannot affect whether the current arrival is best *so far*.

**Supplementary explanation of logarithmic growth:** group the harmonic terms into blocks $1/2$, then $1/3+1/4$, then $1/5+\cdots+1/8$, and so on. A block with $2^{j-1}$ terms, whose denominators lie between $2^{j-1}+1$ and $2^j$, contributes between $1/2$ and 1. There are logarithmically many blocks. This gives an intuitive reason for $H_n=\Theta(\log n)$ without relying only on an integral.

![[aapp-depth-random-hiring-symmetry.png|720]]

*The slide's four-applicant enumeration illustrates the same symmetry: eight of 24 orders hire the third arrival. The relevant maximum is among the first three arrivals.* [[lecture5-Randomization.pdf#page=14|Source slide 14]].

### Expected cost is not only the hire count

**Supplementary cost model:** if an interview costs $c_i$ and a hire/replacement costs $c_h$, then

$$
C=nc_i+Xc_h,\qquad
\mathbb E[C]=nc_i+c_hH_n.
$$

The number of expensive hires is logarithmic in expectation; the complete algorithm still interviews $n$ people. Do not report its total running time as $O(\log n)$ merely from the hire count.

### Active randomization

If the original arrival order is unreliable, obtain the complete list and uniformly shuffle it before interviewing. For any fixed original order, the randomized ordering has the distribution needed for the same $H_n$ expected hire count.

This moves randomness from an assumption about the outside world into the algorithm. It requires access to the complete list before processing and a genuinely uniform permutation.

**Supplementary uniform-shuffle pseudocode:**

```text
for i = n - 1 down to 1
    j = uniform random integer in [0, i]
    swap A[i] and A[j]
```

Each next position is filled by a uniformly selected remaining element, so a particular complete permutation has probability $1/n!$. The shuffle adds $\Theta(n)$ work and does not affect the final best applicant's correctness.

The slides motivate this strategy but do not give a full permutation-generation algorithm; the pseudocode is an added explanation.

**Shuffle pitfall:** swapping each position with an independently chosen index from the entire array is not generally a uniform shuffle. For three elements, that scheme has $3^3=27$ equally likely index sequences but six possible permutations; equal output probabilities would require each permutation to have $27/6$ preimages, which is impossible. Choosing uniformly from the shrinking unassigned region avoids this problem.

Source: [[lecture5-Randomization.pdf#page=17|From input assumptions to randomization, pp. 17–19]].

### Why the shrinking-range shuffle is uniform

For a specified final arrangement of three distinct applicants, the last position must receive its designated applicant with probability $1/3$. Conditional on that choice, the second position must receive its designated applicant from the two remaining ones, with probability $1/2$. The final unassigned item is forced. Therefore that arrangement has probability $(1/3)(1/2)=1/6$.

For $n$ applicants the same reasoning gives $1/n\cdot1/(n-1)\cdots1/1=1/n!$ for each target arrangement. Allowing `j == i` is necessary: a position is permitted to keep the element it already contains. The argument assumes each random choice is uniform over its permitted range. Merely calling a routine “shuffle” is not a proof of that property.

## Las Vegas and Monte Carlo

| Family | Correctness | Time | Efficient version in the lecture |
|---|---|---|---|
| Las Vegas | A returned answer is correct | Depends on random choices | Expected time polynomial on every input |
| Monte Carlo | May produce an erroneous outcome | Bounded by the chosen algorithm | Worst-case time polynomial, with a controlled error guarantee |

For Las Vegas, the usual correctness statement is supplemented by eventual termination with probability one under the algorithm's assumptions. There can still be arbitrarily long runs.

For Monte Carlo, bounding time alone is not enough: the probability of failure or error must also be quantified. The lecture's page 24 emphasizes runtime; read it together with the correctness/error discussion on pages 21–23.

Source: [[lecture5-Randomization.pdf#page=21|Families and efficiency, pp. 21–24]].

![[aapp-lecture5-las-vegas-monte-carlo.png|720]]

*Las Vegas preserves correctness with a random runtime; Monte Carlo bounds runtime while allowing controlled error or failure.* [[lecture5-Randomization.pdf#page=21|Source slide 21]].

### One-sided and two-sided error

For a decision problem:

- **One-sided error:** one kind of incorrect decision is impossible. For example, a returned witness is always valid, but the algorithm may miss an existing witness.
- **Two-sided error:** errors are possible on both YES and NO instances.

State the guarantee conditional on the **true input class**, such as “for every NO input, the probability of YES is zero.” Do not confuse this with the probability that an answer is wrong conditional on observing that answer; that would also require a distribution over inputs.

This makes precise the output-based wording used on slide 22.

### Interpreting the error direction

For the decision question “does this array contain an a?”, a bounded sampler can return YES only after reading an actual `a`. On an array with no `a`, it can never falsely return YES. On an array that contains `a`, it might sample only other entries and return NO: this is a possible **false negative**, with probability determined by the target fraction and sample budget.

Under the lecture's promise that half the entries are `a`, a NO interpretation is always a mistaken conclusion about existence; returning `FAIL` is more precise because it describes the search outcome without asserting absence. The witness returned on success is easy to check. In [[Minimum Cut]], a returned partition is also easy to check as a cut, but checking that it is *minimum* is a different task. This is why repeated min-cut trials do not automatically become Las Vegas by checking feasibility.

## Example: finding an a

The input contains $n$ symbols, exactly half `a` and half `b`, and the goal is to find any position containing `a`. Assume each trial independently samples a uniform index **with replacement**. Each trial succeeds with probability $1/2$.

![[aapp-lecture5-sampling-array.png|720]]

*Five of these ten entries are a: a uniform random lookup succeeds with probability one half.* [[lecture5-Randomization.pdf#page=25|Source slide 25]].

Source: [[lecture5-Randomization.pdf#page=25|Sampling problem]].

### Las Vegas version

```text
FIND-A-LV(A)
    repeat
        j = uniform random valid index
    until A[j] == 'a'
    return j
```

Every returned index is valid because its symbol was checked. The trial count $K$ has a geometric distribution:

$$
\Pr(K=t)=\left(\frac12\right)^{t-1}\frac12,
\qquad t=1,2,\ldots.
$$

Thus

$$
\mathbb E[K]=\frac{1}{1/2}=2.
$$

The probability that no success occurs within $k$ trials is $2^{-k}$, tending to zero. Termination is almost sure, but there is **no finite deterministic worst-case trial bound**. Under unit-cost sampling and lookup, expected time is $O(1)$.

Source: [[lecture5-Randomization.pdf#page=26|Las Vegas sampling]].

### Probability of stopping now versus still waiting

For half-target input, $\Pr(K=3)=1/8$ describes the sequence “miss, miss, hit.” The event $K>3$ means three misses, also probability $1/8$ in this special case. These are different events that happen to have equal probabilities when the hit probability is $1/2$. Generally,

$$
\Pr(K=t)=(1-q)^{t-1}q,\qquad \Pr(K>t)=(1-q)^t.
$$

The expected value 2 is not a two-trial deadline: one quarter of runs still have no success after two samples. For every finite $k$, the all-miss event has positive probability. Yet the probability of missing forever is $\lim_{k\to\infty}2^{-k}=0$, which is the precise meaning of almost-sure termination here.

### Monte Carlo version

```text
FIND-A-MC(A, k)
    for t = 1 to k
        j = uniform random valid index
        if A[j] == 'a': return j
    return FAIL
```

There are at most $k$ trials, so worst-case time is $O(k)$. Failure occurs only when all samples are `b`:

$$
\Pr(\mathrm{FAIL})=\left(\frac12\right)^k,
\qquad
\Pr(\mathrm{success})=1-2^{-k}.
$$

For $k=10$, failure probability is $1/1024\approx0.000977$.

To ensure failure probability at most $\delta\in(0,1)$, choose

$$
k\ge\left\lceil\log_2\frac1\delta\right\rceil.
$$

**Supplementary error interpretation:** `FAIL` here means “the bounded search did not find an a,” not “there is no a.” Under the promised input, an `a` certainly exists. The routine is a bounded-time randomized search with possible failure; if interpreted as a decision routine returning NO on failure, its error is one-sided.

Source: [[lecture5-Randomization.pdf#page=27|Bounded sampling and failure probability]].

### Generalizing the success probability

**Supplementary:** if a fraction $q>0$ of entries are successful targets and trials are independent with replacement, then

$$
\mathbb E[K]=\frac1q,\qquad
\Pr(\text{no success in }k\text{ trials})=(1-q)^k.
$$

If $q=0$, the unbounded Las Vegas search never finds a target. The promise that a target exists is therefore essential. Sampling without replacement changes the distribution, so the same failure formula cannot simply be reused.

### Deriving the expected number of trials

**Supplementary derivation:** let $K$ count all trials including the successful one, and let $q>0$ be the independent success probability. After the first trial, success leaves no further work; failure restarts the same experiment. Hence

$$
\mathbb E[K]=1+(1-q)\mathbb E[K],\qquad
\mathbb E[K]=1/q.
$$

For this restart calculation the geometric waiting time has finite expectation. Be clear about its convention: counting failed trials only gives $\mathbb E[K-1]=(1-q)/q$. [Aspnes, *Notes on Randomized Algorithms*, §3.6.2](https://www.cs.yale.edu/~aspnes/classes/469/notes.pdf).

In the bounded version, finding a valid index early may finish in fewer than $k$ trials, but the **worst-case** bound remains $k$. Repeating an already-valid witness check is not necessary; the probability calculation concerns runs that have not yet succeeded.

### Why independent repetition improves the guarantee

With fresh independent samples, every previous miss leaves the next hit probability unchanged. For $q=1/2$, each additional trial halves the remaining failure probability: $1/2,1/4,1/8,\ldots$. If instead one random index is selected once and then reread $k$ times, all observations are identical. Failure remains $1/2$, regardless of $k$. Repetition only amplifies success when it introduces the randomness required by the probability argument.

Sampling without replacement has a different calculation. In an array with five targets and five nontargets, the probability of three misses is

$$
\frac5{10}\frac4{9}\frac3{8}=\frac1{12},
$$

rather than $1/8$ with replacement. After five misses, a sixth distinct sample must succeed. This is a supplementary comparison to expose the model assumption, not the sampling procedure used by the slides.

The unbounded routine has $\mathbb E[K]=2$. For a version stopped after at most $k$ trials, the actual number of samples is $\min(K,k)$, so its expectation is $\sum_{t=0}^{k-1}2^{-t}=2(1-2^{-k})$, while its worst-case budget is still $k$. The equality follows because sample $t+1$ is performed exactly when the first $t$ samples missed. Worst-case budget, expected samples, and failure probability answer three different questions.

## Applications in the next lectures

[[Minimum Cut]] applies Monte Carlo analysis: a returned cut is valid, but optimality can fail, and independent repetitions reduce that risk. Its contraction proof multiplies **conditional** probabilities along a run. [[Sorting#Randomized quicksort]] instead gives a Las Vegas example: random pivots change running time while preserving sorting correctness, and conditioning on pivot rank produces an expected-time recurrence.

## Takeaways

- Always specify whether the expectation is over inputs or internal random choices.
- Indicators turn a count into a sum of event probabilities.
- Linearity of expectation does not require independence.
- The hiring result concerns the number of hires; interviewing remains linear work.
- Las Vegas trades a deterministic runtime bound for correctness; Monte Carlo uses a bounded runtime with controlled failure or error.

## Exam practice

These are original problems using the deck's probability model.

**1. Hiring cost.** Four distinct applicants are uniformly permuted. An interview costs $1$ and a hire costs $12$. Compute expected cost, and compare the best and worst orders.

> [!faq]- Worked solution
> $H_4=25/12$, so $\mathbb E[C]=4+12(25/12)=29$. Best order costs $4+12=16$; worst order costs $4+4\cdot12=52$. Interview cost is paid for all four applicants in every order.

**2. Change the success fraction.** One quarter of an array's entries are targets. Sample independently and uniformly with replacement. Derive the expected Las Vegas trial count and the trial budget giving bounded-search failure probability at most $0.01$.

> [!faq]- Worked solution
> The expected count is $1/(1/4)=4$. Failure after $k$ trials is $(3/4)^k$. The required budget is $k\ge\lceil\ln(0.01)/\ln(3/4)\rceil=17$. The logarithm of $3/4$ is negative, so dividing by it reverses the inequality. Sixteen trials fail with probability about $0.01002$; seventeen with about $0.00752$.

**3. Detect dependent repetition.** A sampler picks a uniform array index once, then checks that location 20 times. Half the array is `a`. What is its failure probability, and how should the procedure change to obtain $2^{-20}$?

> [!faq]- Worked solution
> It fails with probability $1/2$: choosing a `b` initially forces every check to miss. Sample a fresh independent uniform index on each trial to get the product $(1/2)^{20}$. Repeating a deterministic observation does not create independent evidence.

## Revision questions

1. What distribution is needed to obtain $\Pr(X_i=1)=1/i$?
2. Why can expected hires be computed without proving indicator independence?
3. Does randomizing the order remove the $n$-hire worst execution?
4. Why is the complete hiring procedure not logarithmic-time?
5. What sampling assumption gives failure probability $2^{-k}$?
6. How many trials give failure probability at most $10^{-6}$?
7. What breaks if the array contains no `a`?

> [!faq]- Answer sketch
> 1. A uniform ordering of distinct applicant ranks.
> 2. Linearity applies to dependent variables as well.
> 3. No; an increasing order remains possible, but expected hires are logarithmic for every original input order.
> 4. All $n$ applicants must be interviewed, and shuffling also takes linear work.
> 5. Independent uniform sampling with replacement and half the entries being `a`.
> 6. Twenty, since $2^{-20}\approx9.54\times10^{-7}$.
> 7. The unbounded version cannot terminate successfully; the promise was required.
