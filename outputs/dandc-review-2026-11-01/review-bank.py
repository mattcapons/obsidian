from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
out = Path('outputs/dandc-review-2026-11-01')

feedback = {
1: r'''**Assessment: mostly correct; add combination and refine the recurrence explanation.** Your examples and the connection to recurrences are sound. Divide and conquer also needs base cases and a rule for combining subproblem solutions. In binary search, the array must be sorted and only one of the two possible halves is searched. The nonrecursive cost $f(n)$ need not be constant: merging or adding matrix blocks can take growing time.

**Suggested exam answer:** Divide and conquer divides an instance into smaller subproblems, solves them recursively until base cases are reached, and combines their solutions. Merge sort solves both halves and merges them, giving $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$. Binary search follows only one half of a sorted array, giving worst-case $T(n)=T(n/2)+\Theta(1)=\Theta(\log n)$ when using indices. Many balanced algorithms yield $T(n)=aT(n/b)+f(n)$, where $a$ counts recursive calls, $n/b$ is their size, and $f(n)$ counts work outside recursion. The Master theorem quickly solves recurrences that meet its assumptions and one of its cases; it does not apply to every divide-and-conquer algorithm.

**Study:** [[Divide and Conquer#Overview]]; [[Divide and Conquer#Binary search]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=2|slide 2]].''',

2: r'''**Assessment: revision cross-reference; the main idea in 001 is correct with the additions noted there.** A self-contained definition should state all three stages and the base case.

**Suggested exam answer:** Divide and conquer has three stages: divide an instance into smaller instances of the same problem, conquer by solving them recursively, and combine their answers. Directly solve sufficiently small instances as base cases. Recursive arguments must shrink so the algorithm terminates, and the combination rule must produce a correct solution. For example, merge sort recursively sorts two halves and merges the sorted results. Splitting a problem is useful only if the resulting recursion and combination costs are favorable.

**Study:** [[Divide and Conquer#Overview]]; [[Divide and Conquer#From a recursive specification to a proof]]; [[lecture3-DandC.pdf#page=2|slide 2]].''',

3: r'''**Assessment: revision cross-reference; explicitly show how the cost recurrence is built.** A recurrence describes the actual recursive calls and the nonrecursive work, rather than dividing an already-known complexity by the number of pieces.

**Suggested exam answer:** Specify the input-size measure and base-case cost, count the recursive calls and their sizes, and add the divide/combine work. For $a$ equal-size calls on size $n/b$, sequential time satisfies $T(n)=aT(n/b)+f(n)$ with a constant-size base case. Identify $a,b,f(n)$, check the Master theorem's assumptions and case conditions, and solve it. If they fail, use a recursion tree, substitution, or another suitable method. For merge sort, $a=b=2$ and $f(n)=\Theta(n)$, giving $\Theta(n\log n)$. Count calls actually executed: binary search uses one half, not both.

**Study:** [[Algorithm as recipes#Solving recurrences]]; [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Merge sort as the template]].''',

4: r'''**Assessment: correct central argument; add odd exponents, a base case, and the cost model.** You correctly explain that the equal half-power must be computed once and reused. An exponent is not always even, so halving needs a floor and sometimes one extra multiplication.

**Suggested exam answer:** To compute $x^n$ for a nonnegative integer $n$, return 1 at $n=0$. Otherwise compute $y=x^{\lfloor n/2\rfloor}$ recursively once. Return $y^2$ for even $n$ and $xy^2$ for odd $n$. Thus $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ for growing positive $n$, counting arithmetic at unit cost. Repeated multiplication takes $\Theta(n)$ operations. Calling the half-power routine twice would instead give $2T(n/2)+\Theta(1)=\Theta(n)$ and lose the improvement. Exact large-integer bit complexity requires a separate analysis.

**Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].''',

5: r'''**Assessment: mostly correct mechanism; use the exact exponent and explain the recursive saving.** You correctly identify seven recursive products, additional additions/subtractions, and reconstruction. The improvement repeats at every level. Formally, $O(n^{2.8})$ is too small: $\log_2 7\approx2.8073549>2.8$. Use $\Theta(n^{\log_2 7})$, or give 2.807 as an approximate exponent.

**Suggested exam answer:** Strassen is a divide-and-conquer matrix-multiplication algorithm. Partition each $n\times n$ input into four $(n/2)\times(n/2)$ blocks. Ordinary block multiplication uses eight recursive products; Strassen uses seven specially chosen products and reconstructs the four output blocks through additions and subtractions. With the lecture's block names $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ and $B=\begin{pmatrix}e&f\\g&h\end{pmatrix}$, compute

$$
\begin{aligned}
P_1&=a(f-h),&P_2&=(a+b)h,\\
P_3&=(c+d)e,&P_4&=d(g-e),\\
P_5&=(a+d)(e+h),&P_6&=(b-d)(g+h),\\
P_7&=(a-c)(e+f).
\end{aligned}
$$

Then $C_{11}=P_5+P_4-P_2+P_6$, $C_{12}=P_1+P_2$, $C_{21}=P_3+P_4$, and $C_{22}=P_5+P_1-P_3-P_7$. Recursively apply the same method down to a small base case. The block additions cost $\Theta(n^2)$ per call, yielding $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$, compared with $\Theta(n^3)$ for the classical method. Extra constants and storage affect practical performance, so a smaller exponent does not guarantee an advantage for every matrix size.

**Study:** [[Divide and Conquer#Strassen's algorithm]]; [[Divide and Conquer#Complexity]]; [[Divide and Conquer#Why saving one product compounds]]; [[lecture3-DandC.pdf#page=29|slides 29–38]].''',

6: r'''**Assessment: revision cross-reference; explain the recurrence structure and the theorem's limits.** Your first answer identifies the main reason for using it, with the correction that divide/combine cost is a function $f(n)$ and can grow with $n$.

**Suggested exam answer:** Many divide-and-conquer runtimes have the form $T(n)=aT(n/b)+f(n)$: $a$ recursive calls on equal reduced sizes and nonrecursive divide/combine cost $f(n)$. The Master theorem compares $f(n)$ with $n^{\log_b a}$ and gives an asymptotic bound without expanding every recursion level. It requires constants $a\ge1$, $b>1$, an eventually positive cost, suitable base cases, and one of the theorem's case conditions. Polynomial separation is required in Cases 1 and 3, and Case 3 also needs regularity. Other recurrences require another analysis method.

**Study:** [[Algorithm as recipes#Master theorem]]; [[Algorithm as recipes#Reading a recursion tree level by level]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].''',

7: r'''**Assessment: the time argument is correct by reference to 004; space was missing.** Count the live recursion frames, not the total number of multiplications, and state whether the implementation is recursive or iterative.

**Suggested exam answer:** Compute $y=x^{\lfloor n/2\rfloor}$ once, then return $y^2$ or $xy^2$ according to the parity of $n$, with $x^0=1$. The time recurrence is $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$, giving $\Theta(\log n)$ unit-cost arithmetic operations. The ordinary recursive implementation has $\Theta(\log n)$ nested calls and a constant number of words per frame, so auxiliary stack space is $\Theta(\log n)$. Equivalently, $S(n)=S(\lfloor n/2\rfloor)+\Theta(1)$. An iterative exponentiation-by-squaring implementation uses $\Theta(1)$ auxiliary words while retaining logarithmic arithmetic-operation count. These space bounds use the course's word model and exclude input/output storage; they do not assert constant-bit storage for arbitrarily large powers.

**Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[Divide and Conquer#Following the calls and returns of POWER]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].''',

8: r'''**Assessment: correct reference term and result shapes, but substantial parts are missing.** State the exact case conditions, apply them to binary search, and answer the space question. $f(n)$ is nonrecursive cost, which need not be fixed or constant.

**Suggested exam answer — theorem:** For $T(n)=aT(n/b)+f(n)$ with constants $a\ge1$, $b>1$, constant-size base cases, and eventually positive $f(n)$, put $d=\log_b a$. In the form used in the notes:

1. If $f(n)=O(n^{d-\varepsilon})$ for some constant $\varepsilon>0$, then $T(n)=\Theta(n^d)$.
2. If $f(n)=\Theta(n^d\log^k n)$ for a constant $k\ge0$, then $T(n)=\Theta(n^d\log^{k+1}n)$.
3. If $f(n)=\Omega(n^{d+\varepsilon})$ for some constant $\varepsilon>0$ and $af(n/b)\le cf(n)$ for some constant $0<c<1$ and all sufficiently large $n$, then $T(n)=\Theta(f(n))$.

The outer cases require a polynomial gap, rather than merely being smaller or larger. The recurrence has equal-size subproblems, up to standard floor/ceiling rounding. Some recurrences satisfy none of these cases. This statement matches [MIT's Master theorem sheet](https://people.csail.mit.edu/thies/6.046-web/master.pdf#page=1).

**Application to binary search:** For a sorted array represented by index bounds, only one half is searched. Worst-case $T(n)=T(n/2)+\Theta(1)$ has $a=1,b=2,d=0$ and $f(n)=\Theta(1)=\Theta(n^0\log^0 n)$. Case 2 gives $\Theta(\log n)$ time. The best case is constant time if the first midpoint matches.

**Space or spatial complexity:** The theorem solves suitable recurrences for other resources too, but first derive the right recurrence. Recursive index-based binary search has $S(n)=S(n/2)+\Theta(1)=\Theta(\log n)$ stack words; an iterative version needs $\Theta(1)$ auxiliary words. Sequential sibling calls can reuse storage, so peak space does not automatically add their space costs. For the lecture's geometric example, H-tree side length satisfies $L(n)=2L(n/4)+\Theta(1)=\Theta(\sqrt n)$, and its area is $L(n)^2=\Theta(n)$. The side-length result must be squared to obtain area.

**Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Binary search]]; [[Divide and Conquer#H-tree layout]]; [[lecture3-DandC.pdf#page=5|slides 5–7]]; [[lecture3-DandC.pdf#page=46|slide 46]].''',

9: r'''**Assessment: revision cross-reference to 004; include the odd case and reuse rule.** The logarithmic bound depends on making one recursive call per level.

**Suggested exam answer:** To compute $x^n$, return 1 when $n=0$; otherwise recursively compute $y=x^{\lfloor n/2\rfloor}$ once and reuse it. Return $y^2$ for even $n$, or $xy^2$ for odd $n$. The exponent halves at each level and combination uses at most two multiplications, so $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ under unit-cost arithmetic. Recursively computing the two equal half-powers separately would require linear arithmetic work instead.

**Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].''',

10: r'''**Assessment: revision cross-reference, but the earlier answer did not list the required conditions.** “It looks like $aT(n/b)+f(n)$” alone is insufficient: the constants, cost assumptions, and a valid case must also be checked.

**Suggested exam answer:** Use a recurrence $T(n)=aT(n/b)+f(n)$ with fixed constants $a\ge1$ and $b>1$, eventually positive nonrecursive cost $f(n)$, and constant-size base cases. Subproblems have the same size $n/b$, allowing ordinary floor/ceiling rounding. With $d=\log_b a$, establish either a polynomially smaller $f(n)$, the boundary form $f(n)=\Theta(n^d\log^k n)$ with constant $k\ge0$, or a polynomially larger $f(n)$ satisfying regularity $af(n/b)\le cf(n)$ for some $0<c<1$ eventually. If no case applies, this version of the theorem gives no result. Unequal recursive sizes or a nonconstant $a$ do not fit this standard form directly.

**Study:** [[Algorithm as recipes#Master theorem]]; full cases in [[#AAPP-04-008]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].''',

11: r'''**Assessment: correct recurrence and Case 2 application; fix the odd exponent and complete the theorem/space discussion.** For odd $n$, use $(n-1)/2$, not $n-1/2$. Those expressions differ: with $n=5$, the former is 2 and the latter 4.5. Compute the half-power once. Your $a=1$, $b=2$ analysis correctly counts that single recursive call.

**Suggested exam answer:** The Master theorem uses $T(n)=aT(n/b)+f(n)$ with constants $a\ge1,b>1$, eventually positive $f(n)$, and suitable constant-size base cases. Put $d=\log_b a$. Case 1 requires $f(n)=O(n^{d-\varepsilon})$ and gives $\Theta(n^d)$. Case 2 has $f(n)=\Theta(n^d\log^k n)$, $k\ge0$, and gives $\Theta(n^d\log^{k+1}n)$. Case 3 requires $f(n)=\Omega(n^{d+\varepsilon})$ and regularity $af(n/b)\le cf(n)$ eventually, for constants $\varepsilon>0$ and $0<c<1$; it gives $\Theta(f(n))$.

**Powering:** Use $x^0=1$ and $x^n=(x^{n/2})^2$ for even $n$, or $x^n=x(x^{(n-1)/2})^2$ for odd $n$. Reusing the recursive result gives $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. Here $d=\log_2 1=0$, so Case 2 with $k=0$ gives $\Theta(\log n)$ unit-cost time.

**Space:** Yes, the theorem can help when a correctly derived space recurrence has the required form. Ordinary recursive powering has $S(n)=S(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ auxiliary stack words. The iterative version uses $\Theta(1)$ auxiliary words. This must be analyzed separately from time. For geometric spatial complexity, the lecture's H-tree similarly uses $L(n)=2L(n/4)+\Theta(1)$ for side length and then squares the result to get linear area.

**Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Exponentiation by squaring]]; [[Divide and Conquer#H-tree layout]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].''',

12: r'''**Assessment: correct for ordinary block multiplication, but the Strassen comparison and recurrence analysis are missing.** Ordinary divide-and-conquer multiplication has the same cubic order as the triple loop. Strassen changes the number of recursive products, so its asymptotic bound differs.

**Suggested exam answer:** The Master theorem applies to balanced recurrences $T(n)=aT(n/b)+f(n)$ with constant $a\ge1,b>1$, positive nonrecursive cost, appropriate base cases, and one of its valid case conditions. Ordinary multiplication partitions each matrix into four quadrants, but each output block needs two products: eight recursive multiplications overall. Thus $T(n)=8T(n/2)+\Theta(n^2)$. Since $d=\log_2 8=3$ and $f(n)=\Theta(n^2)$ is polynomially smaller, Case 1 gives $\Theta(n^3)$.

Strassen uses seven recursive products and extra block additions/subtractions, giving $T(n)=7T(n/2)+\Theta(n^2)$. Now $d=\log_2 7\approx2.807>2$, so Case 1 gives $\Theta(n^{\log_2 7})$. The saving compounds across recursion levels. These are arithmetic-operation bounds; merely partitioning into quadrants does not produce the improved exponent.

**Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Ordinary block recursion]]; [[Divide and Conquer#Complexity]]; [[lecture3-DandC.pdf#page=23|slide 23]]; [[lecture3-DandC.pdf#page=38|slide 38]].''',

13: r'''**Assessment: revision cross-reference; give both the usefulness and the assumptions explicitly.** The principle in 001 is sound, but the restrictions should be stated.

**Suggested exam answer:** Divide-and-conquer algorithms often generate $T(n)=aT(n/b)+f(n)$, with a fixed number of equal-size smaller calls plus divide/combine work. The Master theorem compares $f(n)$ with $n^{\log_b a}$ and quickly yields an asymptotic bound when a case applies. It assumes constant $a\ge1,b>1$, eventually positive cost, and suitable base cases. Cases 1 and 3 require polynomial separation; Case 3 additionally requires $af(n/b)\le cf(n)$ for some $c<1$ eventually. The boundary case covers $f(n)=\Theta(n^{\log_b a}\log^k n)$ for $k\ge0$. Other recurrences need another method.

**Study:** [[Algorithm as recipes#Master theorem]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].''',

14: r'''**Assessment: revision cross-reference to 005; the class is divide and conquer.** Use the corrected exponent and identify how the seven-product saving is repeated recursively.

**Suggested exam answer:** Strassen belongs to divide and conquer. It splits two square matrices into quadrants, recursively computes seven products of chosen sums/differences of those blocks, and combines the products to reconstruct the output quadrants. Ordinary block multiplication uses eight recursive products. The extra additions and subtractions still cost $\Theta(n^2)$ per call, giving $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$, compared with classical $\Theta(n^3)$ time. Its smaller exponent provides an asymptotic improvement, while practical crossover depends on implementation costs.

**Study:** [[Divide and Conquer#Strassen's algorithm]]; [[Divide and Conquer#Complexity]]; product formulas in [[#AAPP-04-005]]; [[lecture3-DandC.pdf#page=29|slides 29–38]].''',

15: r'''**Assessment: revision cross-reference to 004; explicitly name divide and conquer and handle both parities.** One recursive subproblem still fits the course's divide-and-conquer classification.

**Suggested exam answer:** Exponentiation by squaring is a divide-and-conquer algorithm. For $x^n$, stop at $n=0$ with result 1. Compute the smaller power $y=x^{\lfloor n/2\rfloor}$ once, then combine it as $y^2$ for even $n$ or $xy^2$ for odd $n$. The recursive exponent halves and combination takes constant arithmetic work, so $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ under the unit-cost model. Reusing $y$ is essential; the repeated equal factor is not a second required recursive call.

**Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].''',

16: r'''**Assessment: mostly correct; say “recursively sort” before merging.** Your final description of splitting to single elements and merging upward gives the right structure. A merge relies on both input halves already being sorted; splitting an unsorted array and immediately merging its unsorted halves does not implement merge sort.

**Suggested exam answer:** Merge sort illustrates divide and conquer. Divide the array into two nearly equal halves. Conquer by recursively sorting both halves, stopping at arrays of size zero or one, which are already sorted. Combine by repeatedly taking the smaller next element from the two sorted halves. This linear-time merge produces the sorted full array. Its sequential recurrence is $T(n)=2T(n/2)+\Theta(n)$, with constant base-case cost, giving $\Theta(n\log n)$ time by Master Case 2.

**Study:** [[Divide and Conquer#Merge sort as the template]]; [[Algorithm as recipes#Looking inside the merge]]; [[lecture3-DandC.pdf#page=4|slide 4]].''',

17: r'''**Assessment: revision cross-reference; state the one-call recurrence and the exact Master case.** The idea in 004 is correct, with the odd-exponent correction explained in 011.

**Suggested exam answer:** Compute $x^{\lfloor n/2\rfloor}$ once and square the result; multiply by $x$ once more if $n$ is odd. Stop at $n=0$ with result 1. This gives $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. For the Master theorem, $a=1,b=2$ and $n^{\log_2 1}=1$. The nonrecursive cost is $\Theta(1)$, so Case 2 with $k=0$ gives $\Theta(\log n)$ unit-cost arithmetic time. Computing the same half-power twice would change the recurrence and result in linear work.

**Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=19|slide 19]].''',

18: r'''**Assessment: revision cross-reference to 005; replace the rounded $O(n^{2.8})$ claim with the exact bound.** For this comparison, the recurrences show why the exponent changes.

**Suggested exam answer:** Classical matrix multiplication takes $\Theta(n^3)$ time; its ordinary block-recursive form uses eight half-size products and has $T(n)=8T(n/2)+\Theta(n^2)$. Strassen uses seven half-size products of block sums/differences and reconstructs the result through additional additions/subtractions. Its recurrence is $T(n)=7T(n/2)+\Theta(n^2)$, giving $\Theta(n^{\log_2 7})$ arithmetic operations, with exponent approximately 2.807. This is asymptotically smaller than cubic time. The reduction from eight to seven occurs at every recursive level, though extra overhead can outweigh the saving for small matrices.

**Study:** [[Divide and Conquer#Ordinary block recursion]]; [[Divide and Conquer#Complexity]]; [[Divide and Conquer#Why saving one product compounds]]; [[lecture3-DandC.pdf#page=38|slide 38]].''',

19: r'''**Assessment: revision cross-reference; one concrete example and its recurrence make a complete answer.** Merge sort, already discussed in 016 and in the lecture, gives a direct illustration.

**Suggested exam answer:** Merge sort divides an array into two halves, recursively sorts each half, and merges the sorted results in linear time, stopping at constant-size arrays. Its recurrence is $T(n)=2T(n/2)+\Theta(n)$. The Master theorem has $a=2,b=2$, so $n^{\log_b a}=n$ matches the nonrecursive cost. Case 2 gives $T(n)=\Theta(n\log n)$. The theorem is useful because many balanced divide-and-conquer algorithms have this fixed-number, fixed-ratio structure, allowing their bounds to be derived by checking standard cases. Its assumptions must be verified rather than applied to every recursive algorithm.

**Study:** [[Divide and Conquer#Merge sort as the template]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=4|slides 4–7]].''',
}

assert set(feedback) == set(range(1, 20))
original = bank_path.read_bytes()
text = original.decode('utf-8')
snapshot = (out / 'Past Exam Question Bank.md.snapshot').read_text()
for number, body in feedback.items():
    qid = f'AAPP-04-{number:03d}'
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
print('Added feedback to AAPP-04-001–019. Original answers and all other sections preserved.')
