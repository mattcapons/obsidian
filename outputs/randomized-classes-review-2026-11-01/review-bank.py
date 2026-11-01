from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
out = Path('outputs/randomized-classes-review-2026-11-01')

feedback = {
1: r'''**Assessment: mostly correct; make the guarantees precise.** You correctly distinguish bounded-time possible error from zero-error random runtime. A randomized algorithm need not have both a random answer and a random runtime. Also, a Monte Carlo time bound is a function of input size and the chosen parameters, rather than one fixed constant for every input.

**Suggested exam answer:** A Las Vegas algorithm never returns an incorrect solution; randomness affects its execution time. Under the usual finite-expected-time guarantee it terminates with probability one, although some algorithms allow arbitrarily long runs. A Monte Carlo algorithm has a stated worst-case runtime bound and may return an incorrect answer or fail to find the requested solution with a specified probability. Its error guarantee must be stated. Independent repetition can often reduce that probability. Las Vegas does not necessarily have an unbounded worst-case runtime: randomized quicksort is always correct and still has a finite quadratic worst case.

**Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Sorting#Randomized quicksort]]; [[lecture5-Randomization.pdf#page=21|slides 21–24]].''',

2: r'''**Assessment: correct runtime criteria; add what is being averaged and the Monte Carlo error guarantee.** Your expected-polynomial versus worst-case-polynomial distinction matches the lecture. The Las Vegas expectation is over internal random choices for each fixed input, rather than over a favorable distribution of inputs.

**Suggested exam answer:** An efficient Las Vegas algorithm is zero-error and has expected runtime bounded by a polynomial in input size on every valid input. In symbols, for some polynomial $P$, $\mathbb E_R[T(x,R)]\le P(|x|)$ for each input $x$. An efficient Monte Carlo algorithm has polynomial worst-case runtime on every valid input, together with a specified useful error bound. For a standard bounded-error decision algorithm, one can require error at most $1/3$ on each input; the particular constant is conventional and can often be improved by independent repetition. The repetition needed to achieve the required guarantee must also fit the polynomial budget.

**Course wording:** Slide 24 states the runtime criteria; slide 23 explicitly adds bounded error for Monte Carlo. Read those statements together.

**Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Randomized Algorithms#Fixing the input before taking an expectation]]; [[lecture5-Randomization.pdf#page=23|slides 23–24]].''',

3: r'''**Assessment: revision cross-reference; your main distinction in 001 is correct with the qualifications there.** Give the guarantees directly when answering an individual exam question.

**Suggested exam answer:** Las Vegas algorithms preserve correctness: any returned solution is correct, while runtime depends on the random choices and is usually analyzed in expectation. Monte Carlo algorithms have a stated worst-case runtime bound while allowing a quantified probability of error or failure. Efficient Las Vegas algorithms have polynomial expected time for each input; efficient Monte Carlo algorithms have polynomial worst-case time with a controlled error guarantee. Randomized quicksort illustrates zero-error random runtime, while the lecture's bounded random search illustrates bounded time with possible failure.

**Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Randomized Algorithms#Example: finding an a]]; [[lecture5-Randomization.pdf#page=21|slides 21–27]].''',

4: r'''**Assessment: mostly correct; distinguish an unbounded worst case from a positive probability of never finishing.** A Las Vegas algorithm can have arbitrarily long executions, but this is not required of every Las Vegas algorithm. A finite expected runtime implies termination with probability one; it does not provide a deterministic deadline.

**Suggested exam answer:** Las Vegas algorithms are zero-error and are efficient when expected runtime is polynomial on every input. In the lecture's repeat-until-hit example, no finite deterministic trial bound exists, yet termination has probability one and the expectation is finite under the promised target fraction. Other Las Vegas algorithms have finite worst-case bounds: standard randomized quicksort on distinct keys has expected $\Theta(n\log n)$ time and worst-case $\Theta(n^2)$ time. Monte Carlo algorithms instead have a stated worst-case time bound and permit controlled error or failure; efficient versions use polynomial time with a suitable error guarantee. A polynomial expectation and a polynomial worst-case bound are different guarantees.

**Study:** [[Randomized Algorithms#Las Vegas version]]; [[Randomized Algorithms#Probability of stopping now versus still waiting]]; [[Sorting#Randomized quicksort]]; [[lecture5-Randomization.pdf#page=26|slides 26–27]].''',

5: r'''**Assessment: revision cross-reference; combine the classification with the efficiency criteria.** Your answer in 002 supplies the correct runtime distinction. Include the correctness/error requirements as well.

**Suggested exam answer:** A Las Vegas algorithm gives a correct answer whenever it terminates; an efficient version has polynomial expected runtime for every fixed valid input, averaging over its own random choices. Under that guarantee termination occurs with probability one. A Monte Carlo algorithm has a bounded worst-case runtime and a specified probability of error or failure. An efficient version has polynomial worst-case runtime and meets the required error guarantee, including any repetitions used to improve reliability. A Las Vegas run need not finish within its expected time, and bounded time alone does not make an unreliable Monte Carlo solver adequate.

**Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[lecture5-Randomization.pdf#page=23|slides 23–24]].''',

6: r'''**Assessment: good examples; add the input promise, sampling model, and probabilities.** Your repeat-until-found versus 20-trial distinction matches the lecture. “Always finds a” needs the promise that an `a` exists and should be expressed as termination with probability one. If no `a` exists, the unbounded loop never succeeds. Twenty trials alone do not establish a useful success probability for an arbitrary array.

**Suggested exam answer:** Las Vegas is zero-error with runtime analyzed in expectation; efficient versions have polynomial expected time on each input. Monte Carlo has a stated worst-case time bound with controlled error or failure; efficient versions meet the required error guarantee in polynomial worst-case time. For the lecture's example, assume an array with half its entries equal to `a`, and take independent uniform samples with replacement. The Las Vegas version samples until it reads an `a` and returns that index. Every returned index is valid, expected trial count is $1/(1/2)=2$, and termination has probability one, with no finite deterministic trial limit. The Monte Carlo version samples at most 20 times, returning a valid index if found and `FAIL` otherwise. It uses at most 20 samples, and $\Pr(\mathrm{FAIL})=(1/2)^{20}=2^{-20}\approx9.54\times10^{-7}$.

**Error interpretation:** `FAIL` means that the bounded search did not find a witness. It does not establish that the array contains no `a`. If failure is reported as a membership answer NO, an existing `a` can be missed: a false negative. This is the bounded-sampling example used in the lecture's Monte Carlo discussion.

**Why the promise matters:** With target fraction $q>0$, the expected repeat-until-hit count is $1/q$ and the 20-trial failure probability is $(1-q)^{20}$. If there is only one `a` among $n$ entries, the latter is $(1-1/n)^{20}$ and approaches 1 as $n$ grows. Thus 20 trials are not uniformly reliable without a lower bound on the target fraction. These sample-time bounds assume unit-cost random indexing and lookup.

**Study:** [[Randomized Algorithms#Example: finding an a]]; [[Randomized Algorithms#Generalizing the success probability]]; [[Randomized Algorithms#Interpreting the error direction]]; [[lecture5-Randomization.pdf#page=25|slides 25–27]].''',

7: r'''**Assessment: revision cross-reference; the earlier classification and runtime criteria are mostly correct.** State both guarantees explicitly and identify the source of the expectation.

**Suggested exam answer:** In a Las Vegas algorithm, randomness affects performance while correctness is preserved; finite expected time gives termination with probability one. It is efficient when, for every valid input, expected runtime over internal random choices is polynomial in input size. A Monte Carlo algorithm has a stated worst-case runtime bound and a quantified probability of error or failure. Efficient versions have polynomial worst-case time and meet an appropriate error guarantee, often improved through independent repetition. Some Las Vegas algorithms have finite worst-case bounds, so “Las Vegas always has an infinite worst case” is not a defining distinction.

**Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[lecture5-Randomization.pdf#page=21|slides 21–24]].''',

8: r'''**Assessment: relevant zero-error intuition, but the data-structure mechanism and example are missing.** The question asks how randomness can improve structure or operation costs while searches remain exact. A general polynomial-time comparison does not explain that benefit.

**Suggested exam answer:** Random choices can determine a data structure's shape while its invariants guarantee correct answers. For example, a treap stores keys in binary-search-tree order and gives each node an independent random priority, maintaining a heap order on priorities. Rotations preserve key order while restoring the priority invariant, so searches and updates remain correct for every valid priority assignment. Under the standard model of independent distinct priorities and a fixed operation sequence independent of those priorities, search, insertion, and deletion take $O(\log n)$ expected time, although a worst-case chain can take $O(n)$. Thus randomness supplies favorable expected structure without requiring the keys to arrive in random order. Expected performance does not imply perfect balance on every run.

**Study:** [[Randomized Data Structures#Overview]]; [[Randomized Data Structures#Treaps: a search tree and a priority heap]]; [[Randomized Data Structures#Search and harmonic path lengths]]; [[Randomized Data Structures#Rotations and updates]]; [[lecture11RandomDataStructures.pdf#page=9|slides 9–17]].''',

9: r'''**Assessment: no answer supplied; the statement is True under the usual randomized-data-structure assumptions.** Randomization can choose the shape, while deterministic structural invariants preserve the meaning of every operation.

**Suggested exam answer:** True. A treap maintains binary-search-tree order on keys and heap order on independent random priorities. Rotations preserve key order and restore the priority invariant, avoiding the need for deterministic balance factors or coloring rules. Search, insertion, and deletion remain exact and have $O(\log n)$ expected cost for fixed operation sequences independent of the sampled priorities. A possible worst-case chain still costs $O(n)$ per operation. The expectation concerns the priorities, rather than random user inputs. See [Aspnes, randomized search trees, §§6.3–6.3.1](https://www.cs.yale.edu/~aspnes/classes/469/notes.pdf#page=139).

**Concrete example:** Insert keys $1,2,3$ in that order. An ordinary unbalanced BST forms a rightward chain. Assign treap priorities $(3,1,2)$ to those keys and use the lecture's min-heap convention. Inserting key 2 rotates it above key 1; inserting key 3 gives a tree with root 2, left child 1, and right child 3. Searches are still ordinary exact BST comparisons. This example illustrates how priorities change shape; the logarithmic expected bound comes from analysis over all independent priority choices, rather than from this one balanced instance.

**Study:** [[Randomized Data Structures#Treaps: a search tree and a priority heap]]; [[Randomized Data Structures#Why a rotation preserves search order]]; [[Randomized Data Structures#Insertion: search down, rotate up]]; [[lecture11RandomDataStructures.pdf#page=9|slides 9–20]].''',
}

assert set(feedback) == set(range(1, 10))
original = bank_path.read_bytes()
text = original.decode('utf-8')
snapshot = (out / 'Past Exam Question Bank.md.snapshot').read_text()
for number, body in feedback.items():
    qid = f'AAPP-05-{number:03d}'
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
print('Added feedback to AAPP-05-001–009. Original answers and all other sections preserved.')
