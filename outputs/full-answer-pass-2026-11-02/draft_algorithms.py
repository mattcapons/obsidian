from pathlib import Path
import json,re

out=Path('outputs/full-answer-pass-2026-11-02')
questions=json.loads((out/'questions.json').read_text())
answers={}
for q in questions:
    if q['has_existing_model']:
        plain='\n'.join(line[2:] if line.startswith('> ') else '' if line=='>' else line for line in q['feedback'].strip().splitlines())
        start=plain.index('**Suggested exam answer')
        answers[q['id']]=plain[start:].strip()

def add(section,ids,body,study):
    if isinstance(ids,int):ids=[ids]
    for n in ids:
        key=f'AAPP-{section:02d}-{n:03d}'
        assert key not in answers,key
        answers[key]=body.strip()+('\n\nStudy: '+study if study else '')

ks=r'''Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.

With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.'''
add(6,[3,4,5,6,7,9,10,12],ks,'[[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].')
add(6,8,r'''Basic Karger replaces deterministic global-cut approaches based on repeated s–t min-cut/max-flow computations with random edge contraction. Repeatedly merge uniformly chosen edge copies until two supernodes remain; preserve multiplicities and remove loops. The remaining crossing edges define a valid cut, but it may not be minimum. A run costs $O(n^2)$ in the lecture model; success is at least $2/[n(n-1)]$. Independent repetition and choosing the smallest output give $O(n^4\log n)$ bounded total time for inverse-polynomial error. Randomness affects optimality, not whether the prescribed operation budget exists. A historical comparison does not establish superiority over every modern deterministic algorithm.''','[[Minimum Cut#Global cuts and s-t cuts]]; [[Minimum Cut#Repetition and running time]].')
add(6,11,r'''Fix a minimum cut. Contracting one of its crossing edges merges vertices that this cut must separate, destroying that particular optimum; other minimum cuts may still survive. If all contractions avoid a fixed minimum cut, the final two supernodes return it. A run succeeds with probability at least $p_0=2/[n(n-1)]$. Run fresh independent trials from the original graph and retain the smallest cut. Since no valid cut beats the true optimum, any successful trial makes the combined result correct. After $R$ trials, failure is at most $(1-p_0)^R\le e^{-p_0R}$; $R\ge\ln(1/\delta)/p_0$ suffices. Reusing identical random choices gives no such amplification, and observing repeated cut values does not certify optimality.''','[[Minimum Cut#Success probability]]; [[Minimum Cut#Why taking the best of repeated runs works]].')

lower=r'''For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.'''
count=r'''Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.'''
part=r'''One valid variant is Lomuto partition (inclusive bounds):
```text
PARTITION(A,l,r):
    x=A[r]; i=l
    for j=l..r-1:
        if A[j] <= x: swap(A[i],A[j]); i++
    swap(A[i],A[r]); return i
```
The invariant has keys $\le x$ before $i$, keys $>x$ in the examined middle region, and unexamined keys ahead of $j$. The returned pivot is in its final rank position. A partition takes $\Theta(r-l+1)$ time and $O(1)$ auxiliary space; it is normally unstable. Randomize by choosing a uniform pivot index and swapping it into $r$ before partitioning. Hoare partition returns a split boundary rather than necessarily a final pivot index; recursion bounds must match it. Three-way partition groups $<x,=x,>x$ and handles many duplicates well. Partition is also used by Quickselect.'''
for ids,body in [([1,5,6,10,13,16,18,20],count),([2,3,4,8,12,15],lower),([7,9,11],part)]:add(7,ids,body,'[[Sorting]].')
add(7,14,r'''Quicksort is divide and conquer: partition around a pivot and recursively sort both remaining parts. Consistently extreme pivots give $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$; balanced splits give $\Theta(n\log n)$. Uniform independent random pivots give expected $\Theta(n\log n)$ time for each fixed distinct-key input while retaining the quadratic worst case. This randomized version is Las Vegas: sorting correctness is exact and expected runtime is polynomial, so it is efficient in that theoretical sense. Randomization mitigates input-order sensitivity; three-way partition handles duplicates, and an introspective switch to heapsort can enforce $O(n\log n)$ worst-case time.''','[[Sorting#Randomized quicksort]].')
add(7,17,r'''Balanced pivot ranks give $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$; any fixed nontrivial constant-ratio split also has logarithmic height and this order. Repeated smallest/largest pivots give $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$. This concerns the recursion tree over the whole run, not just one good or bad pivot. Equal keys require attention to the partition variant: a two-way implementation can produce extreme splits even after randomization.''','[[Sorting#Recursion shape and running time]].')
add(7,19,r'''With a uniform pivot and distinct keys, its rank $k+1$ is uniform over $k=0,\ldots,n-1$. Both resulting sorts execute, giving $E_n=\frac1n\sum_{k=0}^{n-1}(E_k+E_{n-1-k})+\Theta(n)=\frac2n\sum_{k=0}^{n-1}E_k+\Theta(n)$. Solving by substitution or the comparison-count recurrence gives expected $\Theta(n\log n)$; in particular expected pivot comparisons are $2(n+1)H_n-4n$. Random choices can still repeatedly pick an extreme pivot, so a quadratic execution remains possible. Expectation is over fresh internal randomness for each fixed input, not an assumption that user inputs are uniform.''','[[Sorting#Expected-time recurrence]]; [[Sorting#Supplementary exact comparison count]].')

select=r'''Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
```text
SELECT(A,i,pivot_rule):
    if |A| <= constant: sort A; return A[i]
    x = pivot_rule(A)
    partition A into L (<x), E (=x), G (>x)
    if i <= |L|: return SELECT(L,i,pivot_rule)
    if i <= |L|+|E|: return x
    return SELECT(G,i-|L|-|E|,pivot_rule)
```
Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.'''
median=r'''Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.'''
add(8,[1,2,4,5,6],select,'[[Selection and Order Statistics#Randomized selection]].')
add(8,[3,8,11],median,'[[Selection and Order Statistics#Deterministic selection with median of medians]].')
add(8,[7,9,10,12],select+'\n\nFor deterministic pivot_rule, use the following construction.\n\n'+median,'[[Selection and Order Statistics]].')
prime=r'''The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.

This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.'''
add(9,list(range(1,8)),prime,'[[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].')

lcs=r'''For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
```text
for i=1..m:
    for j=1..n:
        if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
        else: C[i,j]=max(C[i-1,j],C[i,j-1])
return C[m,n]
```
The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.'''
space=r'''For the standard full-table LCS algorithm on lengths $m,n$, auxiliary space is $\Theta(mn)$, with at most $O(m+n)$ traceback/recursive-stack cost. If only the length is needed, two rows (or a careful one-row update) reduce auxiliary space to $O(\min(m,n))$, keeping $\Theta(mn)$ time. The ordinary traceback cannot be used after discarding its table. A witness in linear auxiliary space requires a separate reconstruction method such as Hirschberg, not just deletion of old rows. State whether the task asks for a length or an actual subsequence.'''
dp=r'''Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.'''
add(10,[1,2,3,5,7,11,12,13,14,18],lcs,'[[Dynamic Programming and LCS]].')
add(10,[4],lcs+'\n\n'+space,'[[Dynamic Programming and LCS#Reducing space and preserving the right claim]].')
add(10,[8,9,17],space,'[[Dynamic Programming and LCS#Reducing space and preserving the right claim]].')
add(10,10,'The standard dynamic-programming LCS table takes $\Theta(mn)$ time for sequence lengths $m,n$, since it evaluates $mn$ constant-cost states. This is $\Theta(n^2)$ when both lengths are $n$. Naive uncached recursion can be exponential; a memoized algorithm evaluates only reached states, but a fully allocated/initialized dense table still has $\Theta(mn)$ overhead.', '[[Dynamic Programming and LCS#Bottom-up tabulation]].')
add(10,[6,15,16,19],dp+'\n\nFor a concrete repeated state, with both final symbols unequal, branches $(m-1,n)$ and $(m,n-1)$ can both request $(m-1,n-1)`. Cache by the complete state pair. An UNSEEN marker must differ from 0, which is a valid LCS length.'.replace('$(m-1,n-1)`','$(m-1,n-1)$'),'[[Dynamic Programming and LCS#Memoization: solve each requested state once]].')

tables=r'''The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.'''
ite=r'''Memoization is top-down dynamic programming on operand states. For ITE, choose the earliest variable among the three arguments, recursively compute its two cofactor results, and construct one reduced node:
```text
ITE(f,g,h):
    if f==1: return g
    if f==0: return h
    if g==h: return g
    if cache contains (f,g,h): return cache[(f,g,h)]
    v=earliest top variable of f,g,h
    hi=ITE(f|v=1,g|v=1,h|v=1)
    lo=ITE(f|v=0,g|v=0,h|v=0)
    r=MAKE_UNIQUE(v,hi,lo)
    cache[(f,g,h)]=r; return r
```
An operand that does not depend on $v$ is unchanged by either cofactor. With ideal retention and expected constant-time hashing, there are at most $N_fN_gN_h$ operand triples, so time is $O(N_fN_gN_h)$; binary Apply has an $O(N_fN_g)$ bound. Without the computed table, reconvergent assignment paths can repeatedly expand the same state exponentially in variable count even while the unique table keeps the result compact. Neither result size alone nor a finite lossy cache guarantees the ideal once-per-state bound.'''
add(11,[1,6],dp+'\n\nBDD operations cache tuples of operand handles in the computed table; a node unique table provides structural sharing, which is a separate job.','[[Binary Decision Diagrams#Unique table and computed table]].')
add(11,[3,4,5,9,12],tables,'[[Binary Decision Diagrams#Unique table and computed table]].')
add(11,[2,7,8,10,11],tables+'\n\n'+ite,'[[Binary Decision Diagrams#What memoization does to complexity]].')

treap=r'''A treap is a BST on keys and, in the lecture, a min-heap on distinct independent random priorities. Comparisons search as in a BST, so correctness holds for every valid shape. The priority order randomizes shape independently of key arrival order. Under the standard fixed-operation-sequence model, searches and updates cost $O(\log n)$ expected, but a chain gives $O(n)$ worst case. Searches do not perform rotations. Updating heap order uses rotations that preserve BST order; fewer than two expected rotations per ordinary insertion/deletion does not make the preceding search constant time.'''
split=r'''Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
```text
SPLIT(T,k):
    if T==NIL: return (NIL,NIL)
    if T.key<=k:
        (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
    (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
```
Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.'''
join=r'''The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
```text
JOIN(L,R):
    if L==NIL: return R
    if R==NIL: return L
    if L.priority<R.priority:
        L.right=JOIN(L.right,R); return L
    R.left=JOIN(L,R.left); return R
```
Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.'''
ties=r'''Independent continuous random priorities are distinct with probability one. For finite random bit strings, collisions are possible: the lecture extends and stores additional random bits when priorities cannot yet be distinguished. Keep each node's resulting priority stable across comparisons. A sufficiently wide finite random priority with explicit tie-breaking is another implementation convention, but exact distributional claims must match it. Independent random priority order gives the same shape distribution as a random-order BST, hence logarithmic expected search paths; it does not guarantee a deterministically balanced tree.'''
add(12,[1,7,15,19],join,'[[Randomized Data Structures#Split and the restricted Union]].')
add(12,[2,3,13,14],split+'\n\n'+join,'[[Randomized Data Structures#Split and the restricted Union]].')
add(12,[5,6,11,12,16,18],split,'[[Randomized Data Structures#Split and the restricted Union]].')
add(12,[4,8],treap,'[[Randomized Data Structures#Search and harmonic path lengths]].')
add(12,9,join+'\n\n'+treap,'[[Randomized Data Structures]].')
add(12,10,treap+'\n\n'+ties,'[[Randomized Data Structures#Sampling priorities and handling ties]].')
add(12,17,ties,'[[Randomized Data Structures#Sampling priorities and handling ties]].')

skip=r'''A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.'''
skipinsert=r'''Find the insertion position and record each level's predecessor. Sample a new tower height by independent coin flips, insert the node in the bottom list, and splice its forward pointers at each level it occupies; extend the header if needed. Preserve sorted order and the fact that higher levels are subsets of lower ones. Expected search-plus-update time is $O(\log n)$ and expected new pointers are constant for promotion probability $1/2$. Worst-case search can cost $O(n)$ with a customary bounded height; in an uncapped model state the bound in terms of the realized height as well. Searches and deletion do not resample stored heights.'''
add(13,[1,5,7,9],skip+'\n\n'+skipinsert,'[[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].')
add(13,[2,4,6,8],skip,'[[Randomized Data Structures#Search: right while safe, otherwise down]].')
add(13,3,skip+'\n\nA general correct union construction merges the two sorted bottom lists, resolves duplicate-key records under an explicit policy, then rebuilds a skip list on the merged keys using independent geometric heights. This takes $O(n+m)$ expected time and storage, including expected pointer creation. Ordered concatenation can instead reconnect boundary pointers, but needs the precondition that all keys in the first list precede all keys in the second. The supplied deck does not specify one unique skip-list union algorithm; this is an explicit construction, not a claim about an unseen marking scheme.','[[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].')
dsu=r'''Maintain disjoint sets as rooted parent forests. MAKE-SET(x) initializes parent[x]=x and rank/size metadata; FIND(x) returns the root; UNION(x,y) links the representatives unless already equal. Union by rank or size attaches the shallower/smaller tree below the other. Path compression redirects visited FIND nodes toward the root. Together they give inverse-Ackermann amortized cost: $O((n+m)\alpha(n))$ for initialization and $m$ operations, with $O(n)$ storage. This is a sequence guarantee, not a claim that every individual call takes constant worst-case time. With rank/size alone tree height is $O(\log n)$. Representative identities may change; membership equivalence is preserved.'''
add(14,[1,2],dsu,'Reference topic: disjoint-set forests; the supplied dedicated algorithm notes do not contain a full disjoint-set lecture.')

amort=r'''Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.'''
potential=r'''Choose a potential $\Phi(D)$ representing stored credit; require it to be bounded below relative to its initial value (usually $\Phi_0=0$ and $\Phi_i\ge0$). Define $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$. Then $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$, so nonnegative final potential bounds actual total by amortized total. A negative change releases earlier credit, and is compatible with a nonnegative potential. For a nonempty doubling array of size $s$ and capacity $m$, $\Phi=2s-m$ gives constant amortized insertion cost when charging copies and the inserted element; use a separate initial empty-state convention. Allocation-per-slot charges need adjusted constants.'''
account=r'''The accounting method overcharges cheap operations and stores credits to pay for later expensive operations, maintaining a nonnegative total credit balance. For a doubling dynamic array, charging a constant per insertion pays for its own write and saves enough to copy elements at the next expansion. With copies/write cost only the standard charge is at most 3 per insertion, treating initialization separately. If allocation is charged per slot as in question 003, a larger constant charge is needed. The method proves worst-case total sequence bounds for stateful data structures; it is not an average over random executions.'''
add(15,[4,8,10,11,12,15,17,18],amort,'[[Amortized Analysis]].')
add(15,[5,9,16],account,'[[Amortized Analysis#Accounting method]].')
add(15,[6,7,14,19],potential,'[[Amortized Analysis#Potential method]].')
add(15,13,potential,'[[Amortized Analysis#Potential method]].')
add(15,1,r'''A naive RESET scans all $k$ bits and costs $\Theta(k)$ even if almost none have been touched. Maintain h, the highest bit written since the last reset (initially -1), in addition to the given counter:
```text
INCREMENT(A,k):
    i=0
    while i<k and A[i]==1: A[i]=0; i++
    if i<k: A[i]=1; h=max(h,i)
RESET(A):
    for i=0..h: A[i]=0
    h=-1
```
For the specified $n-1$ increments from zero, bit j flips at most $\lfloor(n-1)/2^j\rfloor$ times, so fewer than $2(n-1)$ bit flips occur. RESET visits at most $\min(k,1+\lfloor\log_2(n-1)\rfloor)$ touched positions for $n>1$ (zero for $n=1$). Total is $O(n)$ and each operation has $O(1)$ amortized cost, although an individual increment or reset can be more expensive. Counter initialization is a separate $O(k)$ cost if it is charged.''','[[Amortized Analysis#Aggregate method]].')
add(15,2,r'''MULTIPOP(k) performs $t=\min(k,s)$ pops, costing $\Theta(1+t)$ including loop overhead. It can be linear in current stack size, but every item can be popped only after being pushed. Over n operations from empty, total successful pops are at most total pushes, hence total cost is $O(n)$ and amortized cost is $O(1)$ per operation. A sequence of n-1 pushes followed by MULTIPOP(n-1) exhibits an expensive final operation but only linear total cost. Using potential $\Phi=s$, PUSH has amortized cost 2, POP cost 0, and MULTIPOP's t pop-cost is canceled by a potential drop t, leaving at most constant loop overhead.''','[[Amortized Analysis#Potential method]].')
add(15,3,r'''Charge one per allocated slot, copied element, and inserted element, as the question specifies. A resize from full capacity m costs $2m+m+1=3m+1$; a nonresize insertion costs 1. Let $M=2^{\lceil\log_2 n\rceil}$ be final capacity. Including the initial one-slot allocation, n insertions cost $n+3M-2<7n$; if that initial allocation was prepaid, subtract 1. Thus total cost is $\Theta(n)$ and amortized insertion cost $\Theta(1)$, despite a $\Theta(n)$ single resize. This follows by geometric summation of allocation and copy sizes. Alternatively use potential $6s-3m$ for nonempty states and zero initially: ordinary and resize charges are 7, and the first allocation/insertion has charge 5. The familiar charge 3 omits allocation-per-slot cost and is not the same exact model.''','[[Amortized Analysis#Charging allocation per slot]].')

online=r'''An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.'''
mtf=r'''Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.'''
add(16,[1,2,5,6,9,15],online+'\n\n'+mtf,'[[Competitive Analysis]].')
add(16,[3,4,7,8,10,11,12,14],mtf,'[[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].')
add(16,13,r'''Requests must be served before future requests are known, so reordering trades current cost against unknown future benefits. In the lecture's paid-swap model, start at [A,B,C] and request C,A,A. MTF pays 5,3,1 (search plus forward swaps), totaling 9; an offline strategy that leaves the list unchanged pays 3,1,1=5. Thus future knowledge can help against a specified online heuristic. However, the wording “one fixed sequence cheaper than any online strategy” is too strong: an online strategy can happen to make the offline-optimal decisions on that sequence. The valid adversarial quantifier is: for each fixed deterministic online strategy, a suitable bad sequence can be chosen; it need not be the same sequence for all strategies.''','[[Competitive Analysis#Online, offline, and the role of the adversary]].')

(out/'answers-algorithms.json').write_text(json.dumps(answers,indent=2,ensure_ascii=False)+'\n')
expected=[q['id'] for q in questions if q['section']<=16]
assert set(expected)==set(answers),(set(expected)-set(answers),set(answers)-set(expected))
print(f'Prepared {len(answers)} model answers covering sections 01–16.')
