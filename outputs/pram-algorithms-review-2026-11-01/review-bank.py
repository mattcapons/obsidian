from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
out = Path('outputs/pram-algorithms-review-2026-11-01')

feedback = {
1: r'''**Assessment: correct row–column idea, but the complexity counts matrix–vector work.** An $n\times n$ matrix product has $n^2$ output entries, each requiring a dot product of length $n$. Your function `linear_combination` hides that inner loop; it is not a unit-time operation. Both output loops can run in parallel, but each dot product needs either sequential accumulation or an explicitly parallel reduction.

**Suggested exam answer:** For dense square matrices, $C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$. One simple PRAM algorithm assigns output entries to processors, with a private accumulator per entry:

```text
parallel for each pair (i, j), scheduled over p processors:
    s = 0                         // private accumulator
    for k = 0 to n - 1:           // sequential within this task
        s = s + A[i,k] * B[k,j]
    C[i,j] = s
```

For this schedule, $W=\Theta(n^3)$ and $T_p=\Theta(n\lceil n^2/p\rceil)$ for $1\le p\le n^2$. Thus $p=n$ gives $\Theta(n^2)$ time, while $p=n^2$ gives $\Theta(n)$ time. Shared input entries may have several readers, while each output has one writer, so CREW suffices.

**Further parallelism:** Parallelizing the products within each dot product and reducing them can give $O(\log n)$ time with $\Theta(n^3)$ processors and $\Theta(n^3)$ work. The processor allocation and reduction must be stated. These are classical multiplication bounds, rather than lower bounds for every multiplication algorithm. See [Blelloch and Maggs, §25.8.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=37).

**Course scope:** The supplied PRAM deck illustrates matrix–vector multiplication; the construction above explicitly answers a matrix–matrix interpretation. The bank also contains a matrix–matrix prompt from July 2024 in [[#AAPP-03-005]]. The age of a question does not establish its exclusion from a future exam; no such exclusion has been verified here.

**Study:** [[Divide and Conquer#Matrix multiplication]]; compare [[PRAM#Map: matrix-vector multiplication]].''',

2: r'''**Assessment: correct for the broadcast scan illustrated in the lecture.** Your example matches the diagram when positions are numbered from 1. Be explicit that processors read the same intermediate cell during the same read phase; simultaneous reads of different cells do not require concurrent-read permission.

**Suggested exam answer:** True for the lecture's broadcast implementation. After the first pairwise stage, cell 2 contains $a_1+a_2$. In the next stage, processors computing prefixes 3 and 4 both read that cell and add it to their respective right-half partial sums. For eight inputs, a later stage similarly broadcasts the sum in cell 4 to processors computing prefixes 5 through 8. The resulting prefix entries have distinct writers, so this implementation uses CREW. The first pairwise stage does not need this shared-prefix broadcast.

**Qualification:** This describes the diagram's implementation. Prefix scan can also be implemented on EREW with a different schedule, so concurrent reads are not an unavoidable property of the prefix-sum problem itself.

**Study:** [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=23|slide 23, green CR labels]]; [[PRAM#How the work-efficient tree scan works]].''',

3: r'''**Assessment: no algorithm supplied; prefix scan is covered in the PRAM material.** “Scan” is another name for the prefix operation. The inclusive sum scan outputs $S_i=\sum_{j=1}^{i}a_j$ for every position, rather than returning only the final total.

**Suggested exam answer:** In the lecture's broadcast pattern, start with blocks of one input. At each stage, combine adjacent blocks of equal size: the prefixes in the left block stay unchanged, and the total of that left block is added to every local prefix in the right block. Double the block size and synchronize before the next stage. Each stage reads the preceding stage's values; use separate input/output buffers to make that ordering explicit. After $\lceil\log_2 n\rceil$ stages, each position holds its complete prefix. Padding with zeros handles a non-power-of-two length without changing the asymptotic bounds.

**Example following that pattern:** $[3,1,4,2]\rightarrow[3,4,4,6]\rightarrow[3,4,8,10]$. In the second stage, the left total 4 is read by both right-half processors.

**Complexity and memory rule:** This simple broadcast implementation has $\Theta(\log n)$ time with $O(n)$ processors, $\Theta(n\log n)$ work, concurrent reads of shared block totals, and exclusive writes. A work-efficient tree scan can instead achieve $\Theta(n)$ work and logarithmic depth. The note's separate offset-doubling construction has different intermediate arrays; do not mix its trace with this broadcast trace.

**Study:** [[PRAM#Prefix sum]]; [[PRAM#How the work-efficient tree scan works]]; [[lecture4-PRAM.pdf#page=23|slide 23]].''',

4: r'''**Assessment: correct decomposition and CREW policy; the time bound is missing a factor of $n$.** There are $n$ independent output rows, but each row needs $n$ products and additions. Assigning $n/p$ rows to a processor therefore requires $\Theta(n^2/p)$ time in the divisible case, rather than $O(n/p)$.

**Suggested exam answer:** For an $n\times n$ matrix and length-$n$ vector, compute $y_i=\sum_{j=0}^{n-1}A_{ij}x_j$. Assign independent rows to processors:

```text
parallel for each row i, scheduled over p processors:
    s = 0                         // private accumulator
    for j = 0 to n - 1:
        s = s + A[i,j] * x[j]
    y[i] = s
```

The row-based schedule takes $T_p=\Theta(n\lceil n/p\rceil)$ for $1\le p\le n$, with $W=\Theta(n^2)$. At $p=n$, time is $\Theta(n)$, rather than constant. Processors read distinct matrix rows, may read the same vector element simultaneously, and write distinct outputs: CREW suffices. More than $n$ processors cannot help this unchanged row-only schedule; further parallelism needs a reduction within each row.

**Study:** [[PRAM#Map: matrix-vector multiplication]]; [[PRAM#Worked row decomposition]]; [[lecture4-PRAM.pdf#page=20|slide 20]].''',

5: r'''**Assessment: the reference needs correcting: the immediately preceding answer describes matrix–vector multiplication.** The matrix–matrix idea is in 001, whose complexity also needs the correction given there. Matrix–matrix multiplication has $n^2$ dot products, whereas matrix–vector multiplication has $n$.

**Suggested exam answer:** For two $n\times n$ matrices, each output is $C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$. Compute different output entries in parallel, with one private sequential accumulator for each entry and one final writer to $C_{ij}$. This classical method performs $\Theta(n^3)$ work. With $p\le n^2$ processors distributing the $n^2$ output tasks, its time is $\Theta(n\lceil n^2/p\rceil)$. In particular, $n^2$ processors give $\Theta(n)$ time; $n$ processors give $\Theta(n^2)$ time. Reused input entries require concurrent reads in the natural schedule, while output writes are exclusive. Parallel reductions within dot products offer another allocation/time trade-off.

**Pseudocode:** See the corrected explicit algorithm in [[#AAPP-03-001]].

**Study:** [[Divide and Conquer#Matrix multiplication]]; compare [[PRAM#Map: matrix-vector multiplication]].''',

6: r'''**Assessment: partly correct utilization intuition, but “more efficient” needs a metric and a named algorithm.** A scan can keep more addition tasks active across stages, but extra activity can also mean extra work. Scan computes every prefix; reduction computes one total. A standard tree reduction already has logarithmic depth. Its active processor count halves at each level; the idle count itself does not generally double.

**Suggested exam answer:** Compared with sequential accumulation, a parallel scan replaces a linear dependency chain with logarithmic-depth stages and returns all prefix sums. Compared with a parallel tree reduction, a scan is not inherently faster: both can take $\Theta(\log n)$ time with enough processors, and they produce different outputs. In the lecture's simple broadcast scan, the trade-off is obtaining every prefix through more intermediate operations and concurrent reads: work is $\Theta(n\log n)$, while a tree reduction needs only $\Theta(n)$ work for one total. Better processor utilization alone does not prove lower work or cost.

**Small comparison:** For four inputs, a tree reduction needs three additions. The broadcast scan in 003 needs four additions and returns four prefixes. With eight inputs, that scan performs $4\cdot3=12$ additions, while reduction performs seven.

**Source qualification:** The exam does not define “basic sum” or the efficiency metric. A universal claim that scan beats reduction is therefore unsupported. The extra-work trade-off is specific to the simple scan: a work-efficient tree scan can compute all prefixes with linear work and logarithmic depth, including on EREW. See [Blelloch, *Prefix Sums and Their Applications*, §1.2](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf#page=5).

**Study:** [[PRAM#Reduction]]; [[PRAM#Prefix sum]]; [[PRAM#How the work-efficient tree scan works]]; [[lecture4-PRAM.pdf#page=21|slide 21]]; [[lecture4-PRAM.pdf#page=23|slide 23]].''',

7: r'''**Assessment: correct general PRAM idealization, but the algorithm-specific access pattern is missing.** The question asks which reads and writes the prefix algorithm uses. Unit-time access explains their cost; it does not identify which accesses are legal.

**Suggested exam answer:** The lecture's broadcast prefix scan uses concurrent reads and exclusive writes, so CREW suffices. Several processors may read the same left-block total during a stage; for example, the partial sum in cell 2 is read by the processors computing prefixes 3 and 4. Each processor writes its own distinct prefix/output cell. All reads use the preceding stage's values, and the synchronous stage boundary orders the writes before the next stage. Each permitted memory access has unit cost, so the constant-work stages give $\Theta(\log n)$ parallel time with enough processors. No concurrent writes are required.

**Qualification:** This is the access policy of the illustrated broadcast implementation; other scan algorithms can satisfy EREW.

**Study:** [[PRAM#Memory-access rules]]; [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=23|slide 23]].''',

8: r'''**Assessment: mostly correct; refine the processor threshold and the chunked reduction term.** Your reduction explanation and logarithmic bound are sound. The first level needs about $n/2$ addition tasks, rather than more than $n$ processors. With chunking, the final tree combines $p$ partial sums, so that phase has $\Theta(\log p)$ time. Your $O(n/p+\log n)$ remains a valid upper bound for $1\le p\le n$; $n/p+\log p$ identifies the two phases more directly.

**Suggested exam answer:** Sequential summation needs $\Theta(n)$ time. A balanced binary reduction combines disjoint pairs at each level, requiring $\Theta(\log n)$ parallel time with $\Theta(n)$ processors and $n-1$ additions in total. For $n$ a power of two, $n/2$ processors suffice for the first level. With $1\le p\le n$, each processor can first sum a chunk of about $n/p$ inputs, then reduce the $p$ partial sums in a tree. This gives $T_p=\Theta(n/p+\log p)$ and $W=\Theta(n)$. If all $p$ processors remain allocated, cost is $\Theta(n+p\log p)$; it includes idle slots during the tree phase. Distinct read operands and write destinations make a properly staged tree reduction EREW.

**Example, counting additions only:** For 16 values and four processors, each four-value chunk needs three additions, then the four partial sums need two tree rounds. Thus $T_4=3+2=5$ addition rounds, while total work is $4\cdot3+3=15$ additions.

**Study:** [[PRAM#Reduction]]; [[PRAM#Chunk first, then reduce]]; [[PRAM#Choosing processors with an exact small model]]; [[lecture4-PRAM.pdf#page=21|slides 21–22]].''',

9: r'''**Assessment: revision cross-reference, but distinguish a plain vector sum from a prefix scan.** The source says “vector sum” without specifying a schedule. The CREW answer for the broadcast prefix scan should not automatically be applied to a reduction that returns one total.

**Suggested exam answer, interpreting vector sum as $\sum_i a_i$:** A standard pairwise tree reduction can use EREW. At each level, processors handle disjoint pairs of input/partial-sum cells, perform their reads in a constant number of read steps, compute a sum, and write to distinct cells of the next level. No shared cell needs multiple readers or writers in the same access phase. Separate level buffers and synchronous rounds preserve the old values until all needed reads complete. Unit-cost accesses and a logarithmic number of levels give logarithmic parallel time with enough processors.

**Other interpretations:** Elementwise vector addition $c_i=a_i+b_i$ is also naturally EREW with disjoint index assignments. If “vector sum” refers to the broadcast **prefix** algorithm illustrated on slide 23, use the CREW explanation in [[#AAPP-03-007]]: common block totals are read by several processors and each output has one writer. State which operation and schedule you are analyzing; the phrase alone does not determine one access policy.

**Study:** [[PRAM#Reduction]]; [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=21|slide 21]]; [[lecture4-PRAM.pdf#page=23|slide 23]].''',
}

assert set(feedback) == set(range(1, 10))
original = bank_path.read_bytes()
text = original.decode('utf-8')
snapshot = (out / 'Past Exam Question Bank.md.snapshot').read_text()
for number, body in feedback.items():
    qid = f'AAPP-03-{number:03d}'
    pattern = rf'(^### {qid}\n.*?)(?=^### |^## |\Z)'
    match = re.search(pattern, text, re.M | re.S)
    before = re.search(pattern, snapshot, re.M | re.S)
    assert match and before, qid
    assert match[1] == before[1], f'{qid} changed during review'
    old = '> [!note]- Feedback\n> Not reviewed yet.'
    assert match[1].count(old) == 1, qid
    callout = '> [!note]- Feedback\n> **Reviewed: 2026-11-01.**\n>\n'
    callout += '\n'.join('> ' + line if line else '>' for line in body.splitlines())
    text = text[:match.start()] + match[1].replace(old, callout) + text[match.end():]

assert bank_path.read_bytes() == original, 'Note changed while preparing corrections'
bank_path.write_bytes(text.encode('utf-8'))
print('Added feedback to AAPP-03-001–009. Original answers and all other sections preserved.')
