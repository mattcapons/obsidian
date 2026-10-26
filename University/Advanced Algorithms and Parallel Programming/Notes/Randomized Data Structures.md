---
tags:
  - aapp
  - lecture
lecture: "11"
source: "[[lecture11RandomDataStructures.pdf]]"
---
# Randomized Data Structures

[[AAPP Index|Course index]] · Previous: [[Primality Testing and Cryptosystems]] · Next: [[Dynamic Programming and LCS]] · Prerequisites: [[Randomized Algorithms#Indicator variables]] · [[Divide and Conquer#Binary search]]

## Overview

Treaps and skip lists maintain an ordered dictionary with random structural choices. Searches remain exact. Randomization controls expected path lengths and update costs, without requiring the user to insert keys in random order. The supplied deck is labeled 2025–2026.

Source: [[lecture11RandomDataStructures.pdf#page=3|Dictionaries, pp. 3–8]] · [[lecture11RandomDataStructures.pdf#page=9|Treaps, pp. 9–29]] · [[lecture11RandomDataStructures.pdf#page=30|Skip lists, pp. 30–49]].

## The ordered dictionary problem

Maintain a set $S$ of keys from a totally ordered universe $(U,<)$, optionally with satellite data such as a student record. The basic operations are `Search(k)`, `Insert(k)`, and `Delete(k)`. Here keys are unique; an insertion of an existing key can reject it or update its associated record according to an explicit policy.

The extended operations are minimum, maximum, sorted listing, split, and the deck's restricted **Union**. Split at $k$ produces keys $\le k$ and keys $>k$. Union assumes **every key in the first input is smaller than every key in the second**. This is ordered concatenation/join, not arbitrary set union with overlapping ranges.

An unordered array has cheap append but linear search. A sorted array supports binary search but moving records for insertion/deletion can be linear. An ordinary binary search tree (BST) follows comparisons down pointers; sorted insertion can produce a chain. Treaps randomize the tree shape. Skip lists randomize the availability of shortcuts through sorted linked lists.

## Treaps: a search tree and a priority heap

Each node has a search key and a random priority. Use the lecture's **min-heap** convention:

- Every key in a node's left subtree is smaller, and every key in its right subtree is larger.
- A parent's priority is smaller than each child's priority.
- Priorities are pairwise distinct.

The smallest-priority item must be the root. Its key partitions all other items into a left set and right set. Repeating the argument on each set determines both subtrees uniquely. This proves **uniqueness for fixed key–priority pairs**; it does not mean a key set has only one possible treap when priorities vary.

The same structure is obtained by inserting keys into a plain BST in increasing priority order. The first item has minimum priority and becomes the root; later smaller and larger keys recursively populate the appropriate sides. Independent priorities with a uniform relative order therefore induce the same distribution as a uniformly random insertion order, regardless of the original key arrival order.

![[aapp-lecture11-treap.png|720]]

*The lecture's keys $a<b<c<d<e<f<g$ have priorities $(3,7,4,1,5,2,6)$. The root is $d/1$; BST navigation uses letters, while heap order uses numbers.* [[lecture11RandomDataStructures.pdf#page=11|Source slide 11]].

Source: [[lecture11RandomDataStructures.pdf#page=9|Random priorities, definition and uniqueness, pp. 9–13]].

### Sampling priorities and handling ties

Ideal priorities can be independent uniform reals in $[0,1)$, which are distinct with probability one. A computer stores finite bit strings, so collisions are possible. The slide's remedy extends the stored random bit strings when a comparison cannot yet distinguish them; the extra bits remain attached to those priorities for later comparisons. Do not resample a node's priority afresh at every comparison, since heap relations would then change inconsistently.

A finite implementation can alternatively use sufficiently large random priorities and an explicit tie rule, but must distinguish that implementation choice from the ideal continuous-priority distribution used in the proof. The distributional bounds below assume priorities independent of keys and an update sequence not selected by inspecting hidden priorities.

Source: [[lecture11RandomDataStructures.pdf#page=29|Priority implementation]].

## Search and harmonic path lengths

Search uses only the BST property:

```text
SEARCH(root, k)
    v = root
    while v != NIL
        if k == v.key: return v
        if k < v.key: v = v.left
        else: v = v.right
    return NOT-FOUND
```

Each decision excludes a subtree whose key range cannot contain $k$. In the example, searching for $b$ visits $d,a,c,b$; searching for $h$ visits $d,f,g$ and then NIL. There is no random choice during these searches once the treap is fixed.

Let sorted keys be $x_1<\cdots<x_n$ and let $H_t=\sum_{j=1}^t1/j$, with $H_0=0$. To search successfully for $x_m$, a key $x_j$ with $j<m$ is an ancestor exactly when it has minimum priority among $x_j,\ldots,x_m$. That event has probability $1/(m-j+1)$. Symmetrically, a larger key $x_j$ is an ancestor with probability $1/(j-m+1)$.

Count the target itself once and sum ancestor indicators:

$$
\begin{aligned}
\mathbb E[\text{visited nodes}]
&=1+\sum_{j=1}^{m-1}\frac1{m-j+1}
+\sum_{j=m+1}^{n}\frac1{j-m+1}\\
&=H_m+H_{n-m+1}-1.
\end{aligned}
$$

Thus the expected **edge depth**, with root depth zero, is one less: $H_m+H_{n-m+1}-2$. For an unsuccessful query with exactly $m$ smaller keys, the expected number of visited existing nodes is

$$
H_m+H_{n-m}.
$$

For the seven-key example and target rank $m=4$, expected visited nodes over fresh random priorities are $2H_4-1=19/6$. The displayed treap visits just one node for $d$: an individual realization need not equal its expectation. A query beyond the maximum has expected cost $H_7$ visited nodes.

Since $H_n=\Theta(\log n)$, search is $O(\log n)$ expected and $O(n)$ in a possible chain. Page 9's approximate logarithmic depth constant is not a worst-case height guarantee. The exact rank-dependent formula states precisely what is being averaged.

Source: [[lecture11RandomDataStructures.pdf#page=14|Search and harmonic bounds, pp. 14–16]]. The indicator expansion is supplementary. The original [Aragon–Seidel paper, *Randomized Search Trees*](https://faculty.washington.edu/aragon/pubs/rst89.pdf) independently establishes logarithmic expected updates and fewer than two expected rotations.

## Rotations and updates

### Why a rotation preserves search order

For a right rotation, let $b$ be the old parent and $a$ its left child. Before rotation, subtrees have ordered ranges

$$
A<a<B<b<C.
$$

After rotation, $a$ becomes parent, $b$ becomes its right child, and subtree $B$ becomes $b$'s left child. The in-order sequence remains $A,a,B,b,C$. A left rotation is the inverse transformation. Keys and priorities travel with their nodes; they are not exchanged or regenerated.

![[aapp-lecture11-rotations.png|720]]

*A rotation moves the middle subtree between two parent–child arrangements while preserving every BST key inequality. The priority numbers explain which direction repairs an insertion violation.* [[lecture11RandomDataStructures.pdf#page=20|Source slide 20]].

### Insertion: search down, rotate up

Choose the new node's priority once. Insert it as a BST leaf, then rotate it above its parent while its priority is smaller. Use a right rotation if it is a left child, a left rotation if it is a right child. Each rotation reduces the new node's depth by one. Stop at the root or a parent with smaller priority.

The BST invariant is preserved by every rotation. Before a repair, the only insertion violation is on the new node's upward path; smaller-priority ancestors remain above it when the process stops. Off-path subtree relations remain valid, yielding the unique treap for the enlarged key–priority set.

In the lecture's treap, insert $h$ with priority $0.5$. It starts as $g$'s right child. A left rotation promotes it above $g/6$, then above $f/2$, then above $d/1$. The final root is $h/0.5$; all earlier keys are in its left subtree. This particular run uses three rotations, which does not contradict a bound on the expectation.

### Expected rotations and the slide's depth convention

Suppose the final tree has $n$ keys and the inserted key has rank $m$. Before rotations, its expected edge depth equals the old tree's unsuccessful-search path length:

$$
H_{m-1}+H_{n-m}.
$$

After rotations, expected edge depth is $H_m+H_{n-m+1}-2$. Each rotation moves this node up one edge, so

$$
\begin{aligned}
\mathbb E[R]
&=H_{m-1}+H_{n-m}-(H_m+H_{n-m+1}-2)\\
&=2-\frac1m-\frac1{n-m+1}<2.
\end{aligned}
$$

For $n=7,m=4$, this is $3/2$. The harmonic identities $H_m=H_{m-1}+1/m$ and its right-side counterpart explain the cancellation. Search still costs logarithmic expected time even though rotations have constant expectation.

> [!warning] Qualifications to page 24
> Its opening “expected number of rotations is 2” should be read as a bound below 2, as its final inequality indicates. It also calls root-to-node **node counts** depths. Using edge depths throughout gives the formulas above; using node counts throughout gives the same difference. Mixing them introduces an erroneous extra rotation.

### Deletion: rotate down and remove a leaf

Find the node $x$. While it has children, rotate its smaller-priority child above it; if only one child exists, use that child. This preserves BST order and ensures the promoted child is the correct root of the remaining region. The target moves downward until it is a leaf, then is removed. During this process the target may violate heap order with a promoted child; the final treap of **retained** nodes satisfies heap order.

Deleting $f/2$ from the original example promotes $e/5$ before $g/6$ because 5 is smaller. Rotate right at $f$ to put $e$ above it. Then rotate left at $f$ to promote its sole child $g$. Remove the now-leaf $f$. The remaining right subtree of $d$ is rooted at $e$, whose right child is $g$.

Under the same random-priority and fixed-operation assumptions, deletion has logarithmic expected time and fewer than two expected rotations, by reversing an insertion into the remaining random treap. This constant-rotation statement does not apply to artificially forced sentinel priorities in the split/join constructions below.

Source: [[lecture11RandomDataStructures.pdf#page=17|Insertion, rotations and deletion, pp. 17–24]].

## Split and the restricted Union

### The lecture's dummy-root constructions

To split at a key $k$ absent from the treap, insert a temporary node with key $k$ and priority $-\infty$. It rotates to the root. **Detach and discard this temporary root**, returning its left and right subtrees. Do not run ordinary deletion and join them again. If the key $k$ already exists, the slide removes its record first, performs the absent-key split, then reinserts that record into the $\le k$ output; preserve its satellite data and priority.

For Union, choose a temporary key strictly between all left keys and all right keys, make it a root of priority $-\infty$, and attach the two treaps below it. Then run ordinary deletion of the temporary root, promoting the smaller-priority child repeatedly. The process joins the inputs while preserving their priorities and key ranges.

The lecture's treap split at $c$ yields keys $\{a,b,c\}$ and $\{d,e,f,g\}$. In the first output the original priorities force root $a/3$, right child $c/4$, and $c$'s left child $b/7$. The second output has root $d/1$ and its original right subtree $f/2$ with children $e/5,g/6$. Joining these outputs reconstructs the original treap by uniqueness.

### Direct recursion avoids needing an intermediate key

An ordered universe need not contain a representable key between adjacent input keys: consecutive integers provide a simple counterexample. The following supplementary implementation performs the same operations without artificial keys.

```text
SPLIT(T, k)                         // return (keys <= k, keys > k)
    if T == NIL: return (NIL, NIL)
    if T.key <= k
        (L, R) = SPLIT(T.right, k)
        T.right = L
        return (T, R)
    (L, R) = SPLIT(T.left, k)
    T.left = R
    return (L, T)

JOIN(L, R)                          // every key in L < every key in R
    if L == NIL: return R
    if R == NIL: return L
    if L.priority < R.priority
        L.right = JOIN(L.right, R)
        return L
    R.left = JOIN(L, R.left)
    return R
```

Split only changes pointers along a search path. For example, when $T.key\le k$, its entire left subtree belongs in the first output, while only its right subtree needs splitting. Join chooses the smaller-priority input root as the combined root; the ordering precondition determines which child can receive the other input. Induction proves both invariants. These routines mutate the input trees and return their new roots.

With $n$ total keys, expected split/join time is $O(\log n)$ under the randomized model; worst-case time is $O(n)$. In-order listing is $\Theta(n)$ because it outputs every record. Minimum/maximum follow the extreme branch and cost $O(\log n)$ expected, $O(n)$ worst case.

Source: [[lecture11RandomDataStructures.pdf#page=25|Extended operations and their analysis, pp. 25–28]].

## Skip lists: fast lanes over a sorted list

The bottom list contains **all** keys in sorted order. Each higher list contains a subset of the level below it. A node appearing on several levels forms a tower of forward pointers. A $-\infty$ header exists at every active level; a NIL check or $+\infty$ tail sentinel avoids walking beyond the end.

With two evenly spaced levels, let the express list contain $b$ keys. Search spends roughly $b$ steps in that list and at most $n/b$ in a bottom-level gap. Thus the rough cost $b+n/b$ is minimized near $b=\sqrt n$, giving about $2\sqrt n$ steps. With $k$ ideal balanced levels, the lecture obtains roughly $k n^{1/k}$; setting $k=\log_2n$ gives $2\log_2n$. These calculations motivate the hierarchy but do not describe exact counts for a random list.

Source: [[lecture11RandomDataStructures.pdf#page=31|From one list to logarithmically many, pp. 31–42]].

### Search: right while safe, otherwise down

At each level, move right while the next key is **strictly smaller** than the target. When advancing would reach or pass it, move down. At the bottom, inspect the next node for equality. This convention also records predecessors for updates.

```text
PREDECESSORS(list, k)
    x = header
    for level = topLevel down to 1
        while x.next[level] != NIL and x.next[level].key < k
            x = x.next[level]
        update[level] = x
    return update

SEARCH(list, k)
    update = PREDECESSORS(list, k)
    x = update[1].next[1]
    if x != NIL and x.key == k: return x
    return NOT-FOUND
```

The invariant says the target, if present, lies after the current predecessor, and an overshooting forward pointer cannot hide a valid key before the current position. Descending refines the same ordered interval; at level 1 no key can lie between the predecessor and its next node.

![[aapp-lecture11-skip-search.png|720]]

*The highlighted path for 72 advances along available express links and descends when the next link would overshoot. The diagram's smallest-key tower is replaced by a uniform header sentinel in the implementation below.* [[lecture11RandomDataStructures.pdf#page=41|Source slide 41]].

### Insertion and deletion

Search for the key and retain `update[level]`, the last smaller node at each level. For a new key, create a height $H\ge1$: start at 1, flip a fair coin, and increase the height after each head until the first tail. Insert the record at the bottom and splice its forward pointers at all levels $1,\ldots,H$. If necessary, extend the header's levels first. Each splice is

```text
new.next[level] = update[level].next[level]
update[level].next[level] = new
```

To delete, use the same predecessor search, unlink the target wherever it occurs, and drop empty top levels. Do not toss new promotion coins during deletion or ordinary search. Searching for an absent key leaves the structure unchanged.

For a concrete construction, insert $10,20,30,40,50$ with sampled heights $(1,3,1,2,1)$. The lists are:

```text
level 3: -infinity ------> 20 --------------------> NIL
level 2: -infinity ------> 20 --------> 40 --------> NIL
level 1: -infinity -> 10 -> 20 -> 30 -> 40 -> 50 -> NIL
```

Search for 35: at level 3 move to 20; at level 2, 40 overshoots; descend and advance to 30 at level 1. The next key 40 differs from 35, so the query fails. Insert 35 with height 2 by splicing after 20 on level 2 and after 30 on level 1. Deleting 20 later unlinks it on three levels and removes the now-empty level 3.

![[aapp-lecture11-skip-sentinels.png|720]]

*The $-\infty$ tower lets the same predecessor-search rule handle targets smaller than every stored key. Every real record still appears at the bottom.* [[lecture11RandomDataStructures.pdf#page=45|Source slide 45]].

Source: [[lecture11RandomDataStructures.pdf#page=43|Random promotion and updates, pp. 43–47]].

## Skip-list probability and complexity

For independent fair promotions,

$$
\Pr(H=h)=2^{-h},\qquad
\Pr(H\ge h)=2^{-(h-1)},\qquad h\ge1.
$$

Thus a node has exactly one level with probability $1/2$, exactly two with probability $1/4$, and so on. “Promoted zero levels” means height 1, not absence from the bottom list.

Using the tail-sum identity,

$$
\mathbb E[H]=\sum_{h\ge1}\Pr(H\ge h)=1+\frac12+\frac14+\cdots=2.
$$

The expected number of real-node forward pointers is $2n$, giving linear expected storage. Also, the union bound gives

$$
\Pr(H_{\max}>h)\le n2^{-h}.
$$

Taking $h=\lceil(\alpha+1)\log_2n\rceil$ makes this at most $n^{-\alpha}$. The hierarchy therefore has logarithmic height with high probability.

**Height alone does not prove fast search.** A short hierarchy with a huge empty express gap can still force a long bottom walk. The usual search analysis traces the path backward: at a level, each encountered node has an independent chance $1/2$ of extending upward, so the expected number of horizontal steps before an ascent is constant. Across logarithmically many relevant levels this gives logarithmic expected search cost; a concentration argument controls long paths. This supplementary proof outline explains what is missing from merely citing the height bound. [Pugh, *A Skip List Cookbook*, §2.2](https://drum.lib.umd.edu/bitstreams/17176ef8-8330-4a6c-8b75-4cd18c570bec/download).

The supplied theorem states: for each fixed $\alpha\ge1$, a constant $C_\alpha$ can be chosen so every search in the random $n$-key structure costs at most $C_\alpha\log n$ with probability at least $1-O(n^{-\alpha})$. The hidden time constant may depend on $\alpha$. This does not promise a deterministic logarithmic bound or an event of probability 1. A proof for one query needs an additional union bound over the $O(n)$ key/gap positions to obtain the simultaneous statement.

Source: [[lecture11RandomDataStructures.pdf#page=48|With-high-probability theorem, pp. 48–49]].

Insertion and deletion are also $O(\log n)$ expected, since they perform a search followed by tower splices. A bottom-only realization can produce linear search. In implementations with a height cap $O(\log N)$ for an anticipated maximum population $N$, worst-case pointer traversal is $O(n+\log N)$; the uncapped ideal coin process has no finite deterministic height bound. State the height convention when reporting a strict worst case.

**Model qualification:** Pugh's analysis assumes the operation choices do not exploit observed hidden levels. An adversary deleting every tall node would change the distribution. Likewise, two searches in the same fixed list are not independent random experiments; they traverse the same links. These are probability-model distinctions, not changes to search correctness.

## Comparing guarantees

| Property | Random treap | Skip list |
|---|---|---|
| Structural randomness | Independent priorities | Independent promotion heights |
| Search decisions | BST comparisons | Forward links and descent |
| Search/update expectation | $O(\log n)$ | $O(\log n)$ |
| Expensive structural work | Rotations; fewer than 2 expected for ordinary updates | Pointer splices through a sampled tower |
| Storage | $\Theta(n)$ nodes | $\Theta(n)$ expected pointers |
| Correctness | Exact dictionary operations | Exact dictionary operations |

These expected bounds differ from the deterministic sequence bound in [[Amortized Analysis]]. A structure can be unlucky even on a fixed sequence. The deck supplies treap split/Union, but does not give a skip-list Union procedure; the bank's skip-list union question is therefore not established as covered by these slides.

## Takeaways

- State both BST and min-heap invariants for a treap.
- Fixed priorities uniquely determine the treap; randomness supplies its distribution.
- Distinguish edge depth, visited nodes, total update time, and rotation count.
- Treap Union assumes separated key ranges.
- A skip-list bottom level contains every record; higher levels only accelerate access.
- Expected and high-probability bounds need explicit randomness assumptions.

## Exam practice

Original exercises; the retrieved prompts remain in [[Past Exam Question Bank#Treaps]] and [[Past Exam Question Bank#Skip lists]].

**1. Construct a treap.** Keys $10<20<30<40$ have priorities $4,1,3,2$. Give the tree and the search path for 30.

> [!faq]- Worked solution
> Root $20/1$ has left child $10/4$ and right child $40/2$. The latter has left child $30/3$. Search visits $20,40,30$. Each root is the smallest-priority key in its own range.

**2. Distinguish rotation and search cost.** For final size $n=9$ and inserted rank $m=5$, compute expected rotations. Does a constant expectation imply constant expected insertion time?

> [!faq]- Worked solution
> $2-1/5-1/5=8/5$. No: the initial BST search still has logarithmic expected path length. A particular run can rotate more than twice.

**3. Join a discrete universe.** Why can a dummy-key implementation fail to join a treap ending at integer 8 with one starting at integer 9? Explain a remedy.

> [!faq]- Worked solution
> There is no integer strictly between 8 and 9. Direct JOIN chooses the smaller-priority root and recursively joins the relevant boundary subtree; no new key is required. The separated-range precondition still holds.

**4. Promotion probabilities.** In a 64-key skip list, find the expected number of keys at level 4 or higher, and bound the probability of a tower above level 12.

> [!faq]- Worked solution
> Level 4 membership has probability $2^{-3}=1/8$, so expectation is 8. The union bound gives $64\cdot2^{-12}=1/64$ for height exceeding 12. Neither calculation alone proves the search-path theorem.

## Revision questions

1. What determines the treap root?
2. Why can a rotation move an entire subtree safely?
3. Is split's temporary-root removal ordinary deletion?
4. Why are the two hash-free dictionary structures still randomized?
5. Does a repeated search draw new randomness?
6. What does “with high probability” add beyond expectation?

> [!faq]- Answer sketch
> 1. Minimum priority. 2. The middle subtree's keys lie between the two rotated keys. 3. No; detach it and retain the two outputs separately. 4. They sample priorities or heights when inserting. 5. No; the stored shape is fixed. 6. It controls the probability of exceeding a stated asymptotic cost threshold, with constants chosen for a desired polynomial tail.
