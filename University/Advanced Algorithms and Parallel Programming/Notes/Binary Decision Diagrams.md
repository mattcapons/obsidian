---
tags:
  - aapp
  - lecture
lecture: "13"
source: "[[lezione13Dynamic ProgrammingBDD.pdf]]"
---
# Binary Decision Diagrams

[[AAPP Index|Course index]] · Previous: [[Dynamic Programming and LCS]] · Next: [[Amortized Analysis]]

## Overview

A binary decision diagram represents a Boolean function by a graph of variable tests. Sharing identical subfunctions saves representation space; caching operations on those subfunctions saves computation. This connection to [[Dynamic Programming and LCS#Memoization: solve each requested state once|memoization]] explains the deck's dynamic-programming framing.

The supplied deck is labeled 2025–2026. It covers reduction and ordering, unique and computed tables, the if-then-else operation, complemented edges, composition, variable reordering, garbage collection, and decision-diagram variants including ZBDDs.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=3|ROBDDs, pp. 3–13]] · [[lezione13Dynamic ProgrammingBDD.pdf#page=14|ITE and operations, pp. 14–25]] · [[lezione13Dynamic ProgrammingBDD.pdf#page=26|Ordering and memory, pp. 26–31]] · [[lezione13Dynamic ProgrammingBDD.pdf#page=32|Variants and set diagrams, pp. 32–36]].

## Boolean functions and Shannon decomposition

Use $+$ for Boolean OR, juxtaposition for AND, and $\overline f$ for NOT. These are Boolean operators, not ordinary integer addition and multiplication. For a variable $v$, define cofactors

$$
f_{v=1}=f\big|_{v=1},\qquad f_{v=0}=f\big|_{v=0}.
$$

Every Boolean function satisfies **Shannon expansion**:

$$
f=vf_{v=1}+\overline v f_{v=0}.
$$

If $v=1$, the expression returns the first cofactor; if $v=0$, it returns the second. A decision node therefore stores $(v,g,h)$ and means “if $v$ then $g$ else $h$.” In this note and the lecture's triple notation, the **then/high child comes first**, the else/low child second. Other libraries may order their constructor arguments differently.

A full decision tree branches on all variables and has up to $2^r$ leaves for $r$ variables. A BDD is a directed acyclic graph (DAG): several incoming edges can share the same residual subfunction. Terminals 0 and 1 represent constant functions. Follow the edge labeled by the tested variable's value to evaluate an assignment.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=7|Shannon expansion, order and node triples, pp. 7–13]]. Overbars can disappear from extracted text; the rendered formulas distinguish the two cofactors.

## Reduction, ordering, and canonicity

An **ordered** BDD follows a single fixed variable order along every path, possibly skipping variables. If the order is $a<b<c$, no path may test $c$ and later test $b$. Variables need not occur on every path; a skipped variable is irrelevant to that residual function.

Two reductions are applied:

1. **Eliminate redundant tests:** if $(v,g,g)$ has identical children, replace the node by $g$, since $vg+\overline vg=g$.
2. **Merge identical subgraphs:** if nodes have the same variable and the same two child functions, use one shared node.

For example, if $f=\overline{x_1}$, both $x_2$ branches below a fixed $x_1$ value give the same constant; those $x_2$ nodes disappear. If $f=x_2$, the two $x_1$ cofactors are identical, so the root test $x_1$ disappears instead.

![[aapp-lecture13-reduction.png|720]]

*The slide first removes identical-child tests, then shares identical residual $x_3$ graphs. Reduction concerns functions below nodes, not merely labels that happen to match.* [[lezione13Dynamic ProgrammingBDD.pdf#page=5|Source slide 5]].

### Why the reduced ordered representation is unique

Fix a variable order and a Boolean function. A constant has its designated terminal. For a nonconstant function, the top variable is its earliest relevant variable in that order. Its two cofactors are mathematically determined, and their reduced diagrams are unique by induction. If the cofactors were equal, the variable would be irrelevant and removed; otherwise the triple of top variable and child diagrams determines one node. This proves uniqueness up to graph isomorphism.

An implementation that interns every triple in one **manager** can strengthen this to pointer equality: two function handles in that manager represent the same function exactly when their canonical handles match. Across separate managers, identical functions need not have identical addresses. With complement bits, compare the full signed handles, not just the underlying regular-node addresses.

Canonicity depends on a **common variable order** and consistent reductions. Two reduced diagrams for the same function under different orders need not have the same shape or size. [Bryant, *Graph-Based Algorithms for Boolean Function Manipulation*, §§2–3](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=6|Canonical representation, pp. 6–13]].

## Paths, cubes, and represented sets

A root-to-1 path fixes values of the variables it visits; untested variables are free. That conjunction is a **cube** of satisfying assignments. Different accepting paths are disjoint: at their first branch divergence they require opposite values of the same variable. Taking their OR describes the function's **onset**, the assignments where it equals 1.

The lecture's example is $f=\overline b+\overline a\,\overline c$. For order $a<c<b$, its accepting paths can be written

$$
a\overline b+\overline a c\overline b+\overline a\,\overline c.
$$

These are disjoint even though the shorter expression's two cubes overlap. The graph can share the residual $\overline b$ rather than enumerate all assignments individually. As a **characteristic function**, $f$ represents a set of bit vectors: membership means evaluating $f$ to 1. This is useful even when the set has exponentially many members.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=10|Paths and characteristic functions]]. Compactness is instance-dependent, not a guarantee for every Boolean function.

## Unique table and computed table

These tables solve different problems:

| Mechanism | Key | Stored result | Purpose |
|---|---|---|---|
| Unique table | $(v,g,h)$ | Canonical node/handle | Share representation and enforce uniqueness |
| Computed table | Operation and operand handles, e.g. $(\mathrm{ITE},f,g,h)$ | Previously computed operation result | Avoid repeated recursive computation |

Node construction first eliminates equal-child tests, then looks up the remaining triple:

```text
MAKE(v, high, low)
    if high == low: return high
    if Unique contains (v, high, low)
        return Unique[(v, high, low)]
    p = allocate node (v, high, low)
    Unique[(v, high, low)] = p
    return p
```

This assumes the children contain only variables later than $v$. A unique-table lookup is not a substitute for checking the ordering precondition.

The computed table can forget entries and recompute them later without changing the mathematical answer. The unique table must still prevent duplicate live representations of the same triple. A hash collision means two keys share a bucket, not that they describe the same function: compare complete keys before reusing a result. A lossy computed cache can overwrite an old entry, but must not turn a different key into a false cache hit.

The practical manager/cache distinction agrees with the [CUDD User's Manual, “The Manager” and “Cache”](https://www.cs.uleth.ca/~rice/cudd_docs/node3.html). Caching an operation is the memoization step; interning its output is structural sharing. Using only one table does not accomplish both jobs.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=11|Two tables, pp. 11–15]] · [[lezione13Dynamic ProgrammingBDD.pdf#page=19|Computed-table implementation and variants, pp. 19–23]].

## The if-then-else operation

Define

$$
\operatorname{ITE}(f,g,h)=fg+\overline f h.
$$

Here the condition $f$ may itself be a whole Boolean function. Evaluating one assignment chooses $g$ or $h$ according to that function's value. Common operators reduce to ITE:

| Operation | ITE expression |
|---|---|
| $f\land g$ | $\operatorname{ITE}(f,g,0)$ |
| $f\lor g$ | $\operatorname{ITE}(f,1,g)$ |
| $\neg f$ | $\operatorname{ITE}(f,0,1)$ |
| $f\oplus g$ | $\operatorname{ITE}(f,\overline g,g)$ |
| $f\Rightarrow g$ | $\operatorname{ITE}(f,g,1)$ |

These follow by considering condition values 0 and 1. Page 14 lists all sixteen two-input truth functions; the table above gives the principal constructions without repeating equivalent constant and projection cases.

### Deriving the recursive state

Choose $v$, the earliest top variable among $f,g,h$. Restrict all three inputs at that variable. Restriction commutes with Boolean operations, so

$$
\operatorname{ITE}(f,g,h)=\operatorname{ITE}\!\left(v,
\operatorname{ITE}(f_{v=1},g_{v=1},h_{v=1}),
\operatorname{ITE}(f_{v=0},g_{v=0},h_{v=0})\right).
$$

If an operand's top variable comes later than $v$, it does not depend on $v$, and **both cofactors equal that operand**. Do not descend an arbitrary child merely because another operand contains $v$.

```text
ITE(f, g, h)
    if f == 1: return g
    if f == 0: return h
    if g == h: return g
    if Computed contains (ITE, f, g, h)
        return Computed[(ITE, f, g, h)]
    v = earliest top variable of the nonterminal operands
    t = ITE(cofactor(f,v,1), cofactor(g,v,1), cofactor(h,v,1))
    e = ITE(cofactor(f,v,0), cofactor(g,v,0), cofactor(h,v,0))
    r = MAKE(v, t, e)
    Computed[(ITE, f, g, h)] = r
    return r
```

Each recursive call advances beyond $v$ in the operands that depend on it, guaranteeing progress. Terminal cases are correct directly; induction on the remaining variables proves the recursive results. Shannon expansion combines them correctly, and MAKE preserves reduced ordering and uniqueness. This explanatory pseudocode omits memory management and complemented-pointer implementation details.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=14|ITE definition and recursion, pp. 14–17]]. The two recursive branches in the rendered slide use opposite cofactors; plain text extraction can lose their overbars.

### Worked ITE example from the deck

Use order $a<b<c<d$ with $F=a+b$, $G=ac$, and $H=b+d$. Let $B$ denote the node for $b$, $C$ that for $c$, and $D$ that for $d$.

At top variable $a$:

$$
F_{a=1}=1,\quad F_{a=0}=B,\quad
G_{a=1}=C,\quad G_{a=0}=0,\quad
H_{a=1}=H_{a=0}=H.
$$

The high result is $\operatorname{ITE}(1,C,H)=C$. The low result is $\operatorname{ITE}(B,0,H)$. Split the latter at $b$: its high result is $\operatorname{ITE}(1,0,1)=0$, and its low result is $\operatorname{ITE}(0,0,D)=D$. Thus create/reuse

$$
J=(b,0,D),\qquad I=(a,C,J).
$$

Algebra independently checks the answer:

$$
I=(a+b)ac+\overline{(a+b)}(b+d)
=ac+\overline a\,\overline b d.
$$

The result reuses $C$ and $D$ from the inputs. Its root-to-1 paths say either $a=1,c=1$ (with $b,d$ irrelevant), or $a=0,b=0,d=1$ (with $c$ irrelevant). Exactly four nonterminal nodes are reachable in the result: $a,b,c,d$; only the $a$ and $b$ result triples need new nodes if absent from the manager.

![[aapp-lecture13-ite.png|720]]

*Dashed cross-diagram pointers show shared residual functions $C$ and $D$. The complementary literal on the final $a$ term is essential: the result is $ac+\overline a\,\overline b d$.* [[lezione13Dynamic ProgrammingBDD.pdf#page=18|Source slide 18]].

### What memoization does to complexity

Let the three input diagrams have $N_f,N_g,N_h$ reachable nodes, counting terminals. For a fixed order, each recursive operand is a residual handle from its corresponding input. Hence there are at most $N_fN_gN_h$ possible operand triples. If an ideal computed table retains every encountered state, each is evaluated once, with constant local work and expected constant-time hash operations:

$$
T_{\mathrm{ITE}}=O(N_fN_gN_h).
$$

The actual number of reachable triples is often much smaller. A two-input Apply operation similarly has an $O(N_fN_g)$ state bound. Without caching, identical triples can recur along many assignment paths and recursive work can be exponential in the number of variables, despite a compact shared graph. The unique table alone may still share the final nodes while failing to prevent this repeated computation.

> [!warning] Complexity qualification to page 6
> “Usually linear in size of result” is not a general worst-case bound for BDD operations. Use reachable operand states as the accounting unit; the output itself may be exponentially large in the original variable count. A bounded lossy cache can evict states, so “every state is computed once” requires the ideal retention assumption. Bryant's binary-operation product bound gives an independent check of this distinction: [Bryant, §4](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).

## Complemented edges and normalized cache arguments

A complemented handle means the negation of the function at the underlying node. Negation can then flip one bit instead of building a second graph. The canonical representation must normalize these bits consistently: the lecture and CUDD require a node's **then child to be regular**. If a proposed then child is complemented, complement both child handles and return the complement of the resulting regular node.

For example,

$$
\operatorname{ITE}(v,\overline g,h)
=\overline{\operatorname{ITE}(v,g,\overline h)}.
$$

This gives the same function with a regular then handle. Negating a handle changes function semantics even though its underlying graph address stays the same.

Cache normalization also recognizes equivalent requests, including

$$
\operatorname{ITE}(f,g,h)=\operatorname{ITE}(\overline f,h,g),
\qquad
\operatorname{ITE}(f,g,h)=\overline{\operatorname{ITE}(f,\overline g,\overline h)}.
$$

Track whether the **result** must be complemented when canonicalizing a triple. The whole-expression bars on page 22 are easy to miss. Removing them would turn some equivalences into their opposites. Pointer-address tie rules in that slide choose a repeatable representative within a running manager, not a portable ordering of functions across processes.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=20|Complemented edges and equivalent requests, pp. 20–22]]. Implementation clarification: [CUDD Programmer's Manual, “Complement Arcs”](https://www.cs.uleth.ca/~rice/cudd_docs/node4.html).

## Constant checking and composition

### Tautology and ITE_CONSTANT

An already-built canonical ROBDD is a tautology exactly when its handle is terminal 1; testing that handle is constant time. This does not mean **constructing** the BDD from an arbitrary formula is constant time.

The slide's `ITE_CONSTANT` asks whether an ITE result would be 0, 1, or nonconstant (NC), without building a full result diagram. After handling trivial cases, recursively classify its two cofactors. If either is nonconstant, or they are different constants, the full function is nonconstant. If both equal the same constant, return it. Cache these classification results with an appropriate operation tag; they are not ordinary BDD node pointers.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=23|Caches and constant checking, pp. 23–24]].

### Substituting a function for a variable

Composition $F[v\leftarrow G]$ replaces occurrences of input variable $v$ by function $G$. In the deck's formulation, $G$ does not depend on $v$.

If the top variable of $F$ is later than $v$, $F$ cannot contain $v$ and can be returned unchanged. If it is $v$, return $\operatorname{ITE}(G,F_{v=1},F_{v=0})$. If its top variable $u$ precedes $v$, recursively compose both children, then combine them with $\operatorname{ITE}(u,\text{new high},\text{new low})$.

Why not simply allocate $(u,\text{new high},\text{new low})$? Substitution may introduce an earlier variable below $u$, violating the global order. For example, start with $F=bv$ under order $a<b<v$ and substitute $G=a$. Directly making a $b$ node with child $a$ breaks the order. ITE reconstructs the canonical result $ab$, with $a$ above $b$.

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=25|Compose]]. The small counterexample is supplementary.

## Variable ordering and dynamic reordering

Different orders may expose different opportunities to share residual functions. The slide illustrates the same function under two orders:

![[aapp-lecture13-ordering.png|720]]

*Both diagrams represent the same Boolean function; their internal variable orders and graph shapes differ. Canonicity compares diagrams under one fixed order.* [[lezione13Dynamic ProgrammingBDD.pdf#page=8|Source slide 8]].

For a fully checkable supplementary example, use the multiplexer $M=sa+\overline s b$. Under order $s<a<b$, the root $s$ selects the one-node functions $a$ and $b$: three nonterminal nodes total. Under order $a<b<s$, there are five: root $a$, two different $b$ nodes, and nodes for $s$ and $\overline s$ (without complemented edges). The latter order must remember the earlier data bits before learning which one matters.

Static ordering chooses the order up front using problem structure. Dynamic reordering changes it during processing while keeping all diagrams in the manager consistent. The slide's adjacent-layer swap works by decomposing a local function into four cofactors $f_{00},f_{01},f_{10},f_{11}$, then regrouping them in the opposite variable order. The residual functions below that block stay the same, but sharing and nodes within the changed layers may change.

**Sifting** moves a variable through candidate positions by adjacent swaps, measures node counts, and retains a useful position. Variable grouping keeps related variables together, such as current-state and next-state pairs. These are heuristics: trying orders has a cost and does not guarantee a globally minimum diagram.

External handles and intermediate recursive references complicate reordering. A package must preserve valid function handles or use an explicit indirection/restart scheme; directly exchanging variable labels is insufficient. Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=26|Static ordering, adjacent swaps and sifting, pp. 26–29]].

## Garbage collection and cache validity

The manager may retain many temporary or no-longer-used nodes. Reference counting tracks incoming references, including external handles; a node with no live references can become reclaimable, with consequences propagated to its children. Mark-and-sweep instead marks all nodes reachable from live roots and reclaims unmarked nodes. Shared descendants must remain alive while any live root reaches them.

Immediate reclamation can waste work if a recently dead node is reused soon; delayed collection trades memory against reuse. The lecture discusses keeping such nodes temporarily and using collection statistics. A saturating reference count must never wrap to zero: a frozen maximum may retain extra memory, but avoids reclaiming a live object.

Cache entries do not necessarily own references. If a cached result is reclaimed, the stale entry must be invalidated before reuse. Likewise, structural reordering can invalidate cached operand relationships. CUDD removes cache entries involving dead nodes during collection and clears the cache when reordering. This qualifies the slide's blanket instruction to clear the computed table: the implementation must invalidate all unsafe entries, and may clear more for simplicity. [CUDD Programmer's Manual, “Reference Counts” and “The Cache”](https://www.cs.uleth.ca/~rice/cudd_docs/node4.html).

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=30|Garbage collection, pp. 30–31]]. The final memory-locality bullet on page 31 ends mid-sentence; no specific unfinished sorting rule is assumed here.

## Variants and zero-suppressed diagrams

Page 32 briefly distinguishes multi-valued decision diagrams (more than two branches), ADDs/MTBDDs (binary decisions with non-Boolean terminal values), and free BDDs (without one shared global variable order). Removing the ROBDD ordering restriction also removes the same simple canonical-representation guarantee. The slide calls ADDs “Analog BDDs”; the standard name is **algebraic decision diagrams**, as used by the CUDD manuals.

### ZBDD reduction is different

Zero-suppressed BDDs, also called ZBDDs or ZDDs, are useful for families of sets, especially sparse combinations. Interpret a high branch as including the current element in a represented set, and a low branch as excluding it.

In an ordinary BDD, a skipped variable is a **don't care**: either value gives the same residual function. In a ZDD set-family interpretation, an omitted variable is **absent from every represented set**. Therefore the reduction rules differ:

- ROBDD: eliminate a node if high and low children are equal.
- ZBDD: eliminate a node if its **high child is 0**, redirecting incoming edges to its low child.
- Both: merge identical remaining triples under the common order.

![[aapp-lecture13-zbdd.png|720]]

*The left reduction removes an irrelevant Boolean test; the right reduction removes a set element that never occurs. Applying the BDD equal-child rule to a ZDD would change its represented family.* [[lezione13Dynamic ProgrammingBDD.pdf#page=33|Source slide 33]].

For example, terminal 0 denotes the empty family $\varnothing$, whereas terminal 1 denotes the family $\{\varnothing\}$ containing the empty set. The family $\{\{x\}\}$ uses node $(x,1,0)$. Node $(x,1,1)$ represents both $\varnothing$ and $\{x\}$, so it cannot be removed merely because its children agree. Node $(x,0,1)$ can be removed: it represents only the empty set, with $x$ always absent.

### Why the declared variable universe matters

Over universe $\{x_1,x_2\}$, Boolean function $\overline{x_1}\,\overline{x_2}$ has only the empty selected set as a satisfying assignment. Its set-family ZDD is terminal 1. Extend the Boolean universe with a free variable $x_3$: the same formula now accepts both $\varnothing$ and $\{x_3\}$, requiring a ZDD node with both children 1. To represent only the empty set over the larger universe, the Boolean characteristic function must also require $\overline{x_3}$.

This explains page 34's “support set” qualification. Here it means the declared variable universe used to translate Boolean assignments into sets; it should not be confused with only the variables on which a Boolean function essentially depends. [CUDD User's Manual, “Constant Functions”](https://www.cs.uleth.ca/~rice/cudd_docs/node3.html) independently distinguishes the meaning of terminal 1 for BDDs and ZDDs.

Pages 35–36 illustrate a related combinational-set encoding with symbols $v_1,\overline v_1,v_2,\overline v_2$. A path chooses which literals are present in a product. The pictured product $\{v_1,v_2\}$ includes the two positive literals and omits both negative literals. The final compact graph uses a shared outside terminal and retains only the required inclusion decisions. An absent literal in such a product is not automatically the assertion that the corresponding Boolean variable is false.

![[aapp-lecture13-combinational-sets.png|720]]

*The final slide compresses the combinational family for the product containing $v_1$ and $v_2$. “I” denotes membership in the family; “O” denotes exclusion. This is a set-of-symbols representation, whose interpretation must be specified before applying Boolean intuition.* [[lezione13Dynamic ProgrammingBDD.pdf#page=36|Source slide 36]].

Source: [[lezione13Dynamic ProgrammingBDD.pdf#page=32|Variants, canonicity and combinational sets, pp. 32–36]].

## Takeaways

- A node represents a residual function; sharing turns a decision tree into a DAG.
- Reduced ordering supplies canonicity; one manager can enforce canonical handles.
- The unique table prevents duplicate nodes; the computed table prevents repeated operations.
- ITE recursively branches on the earliest operand variable and uses opposite cofactors.
- Complexity depends on visited operand states and may be exponential in the variable count.
- Complement bits, ordering, reference ownership, and ZDD semantics require explicit conventions.

## Exam practice

Original exercises. Retrieved questions remain in [[Past Exam Question Bank#BDDs and memoization]].

**1. Reduce a function.** Under order $a<b<c$, reduce $f=ab+\overline a bc+\overline a b\overline c$. What remains?

> [!faq]- Worked solution
> Factor the last terms: $\overline a b(c+\overline c)=\overline a b$. Thus $f=ab+\overline a b=b$. Both $a$ cofactors are $b$; the $a$ test is removed, and $c$ is irrelevant. The reduced diagram is one $b$ node with high 1 and low 0.

**2. Explain the two tables.** ITE encounters a previously seen operand triple, but its computed-cache entry was evicted. The unique table still contains every live result node. Is correctness lost? What guarantee is lost?

> [!faq]- Worked solution
> Correctness is retained: recursion recomputes the same function and MAKE reuses existing canonical nodes. The no-recomputation guarantee is lost, so the ideal “one evaluation per triple” complexity argument cannot be asserted for an arbitrarily lossy cache.

**3. Compose without breaking order.** Let $F=bv$ with order $a<b<v$, and substitute $v\leftarrow a$. Draw the reduced result and explain why raw node allocation is unsafe.

> [!faq]- Worked solution
> The result is $ab$: root $a$, high child the function $b$, low child 0. A raw $b$ root with high child $a$ tests $a$ after $b$ and breaks the order. ITE reconstructs the correct ordered representation.

**4. Separate ZDD rules.** Interpret $(x,1,1)$ as a ZDD node. May it be removed? Compare $(x,0,1)$.

> [!faq]- Worked solution
> $(x,1,1)$ represents $\{\varnothing,\{x\}\}$ and must stay. $(x,0,1)$ represents $\{\varnothing\}$, so zero suppression removes the $x$ node. The ordinary BDD equal-child reduction would answer the first question differently because its semantics differ.

## Revision questions

1. What are the two Shannon cofactors?
2. When do canonical pointer comparisons work?
3. What is the memoized state for ITE?
4. Why does a skipped top variable leave an operand unchanged?
5. Is tautology checking always constant time from an arbitrary formula?
6. Why can a garbage collector invalidate a computed cache?

> [!faq]- Answer sketch
> 1. Restrictions at variable values 1 and 0. 2. Within one manager, fixed order, reduction and handle normalization. 3. The operation and three operand handles. 4. That residual function does not depend on the variable. 5. Only testing an already-built canonical handle against terminal 1 is constant time; construction may be expensive. 6. A cached pointer may refer to a node that has been reclaimed, unless cache references explicitly keep it alive.
