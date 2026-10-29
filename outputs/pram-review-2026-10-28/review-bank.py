from pathlib import Path
import re

bank = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
original = bank.read_text()

reviews = {
    'AAPP-01-013': r'''**Assessment: correct.** You identify both reasons: constant-time operations and synchronized execution. Your conclusion that time is the number of cycles is the essential point.

**Suggested exam answer:** PRAM assumes unit-time basic instructions and permitted memory accesses, with processors executing synchronous steps. Therefore elapsed parallel time is proportional to the number of sequential steps/rounds until completion. Instructions executed simultaneously on different processors do not add to elapsed time; summing those operations measures work instead.

**Wording to keep precise:** “Number of instructions” here means the length of the parallel execution in steps, rather than the total instruction count over all processors. For example, eight processors each performing one operation per step for five steps give time 5 and work 40 in that simplified counting model.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. See also [the IIT Delhi course reading, “PRAM Computation Time,” printed p. 74](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/kumar_chapter3.pdf#page=10).''',
    'AAPP-01-014': r'''**Assessment: correct.** Your explanation gives the reason the statement is false: shared memory coexists with private processor state.

**Suggested exam answer:** False. Each PRAM processor has its own private registers/local storage, used for operands and intermediate results, as well as access to shared memory. Other processors cannot directly access its private registers; communication occurs through shared-memory reads and writes.

**Example:** Two processors can both have a local register named `sum` without a conflict. A conflict depends on accessing the same shared cell.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=4|slide 4]].''',
    'AAPP-01-015': r'''**Assessment: the common-write rule is correct, but the security example does not establish a valid application.** Common CW requires agreement; it does not compare results, perform majority voting, or guarantee protection against a malicious processor. If one processor proposes a different value to the same cell, that step violates the common-write rule.

**Suggested exam answer — Boolean OR:** Given $n$ Boolean inputs, initialize a shared flag to 0 in a separate step. Assign one processor to each input. A processor whose input is 1 writes 1 to the flag; a processor whose input is 0 does nothing. All concurrent writes therefore agree, so common CRCW permits them. The final flag is 1 exactly when at least one input is 1. With $n$ processors this takes a constant number of rounds.

```text
flag = 0                         // separate initialization
in parallel for i = 0, ..., n-1:
    if A[i] == 1:
        flag = 1
```

**Why the condition matters:** Letting zero-input processors write 0 in that same write phase would violate common CW when inputs contain both 0 and 1.

**Study:** [[PRAM#A useful CRCW example: Boolean OR]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].''',
    'AAPP-01-016': r'''**Assessment: correct choice; the explanation was missing.**

**Suggested exam answer:** Standard PRAM uses implicit synchronization. Processors advance through read, local-computation, and write phases in lock-step, and the next round starts only after the current round is complete. The model supplies this ordering automatically, so the algorithm does not need explicit barrier or lock calls to synchronize rounds, and no extra synchronization overhead is charged.

**Meaning of “implicit”:** The synchronization is built into the execution rules. The barrier drawn on the lecture slide represents this guarantee; it does not mean that a programmer must implement a costly barrier. Processors may still be inactive, and the algorithm must obey data dependencies and memory-access rules.

**Study:** [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [the IIT Delhi course reading on synchrony and PRAM time, printed p. 74](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/kumar_chapter3.pdf#page=10).''',
    'AAPP-01-017': r'''**Assessment: mostly incorrect; you have described access time rather than storage usage.** Thinking in cells is relevant, but constant access time and unlimited bandwidth simplify time analysis. They do not determine how much memory an algorithm needs.

**Suggested exam answer, ordered by relevance to space accounting:**

1. **Unit storage per value:** in the unbounded-integer, unit-cost variant, one cell holds one integer regardless of its bit length. Space is counted in cells, without expanding each integer into bits.
2. **Uniform, unbounded addressable memory:** count the shared cells actually used/accessed by the algorithm; the model supplies as many as needed, without hardware capacity or memory-layout bookkeeping costs. Unlimited available memory does not mean the algorithm's space usage is infinite.

**Counting convention:** The shared-space convention counts shared cells. If total storage is requested, also include processor-local storage; for example, $m$ shared cells plus a fixed positive number of registers on each of $p$ processors uses $\Theta(m+p)$ total cells. State the convention rather than silently excluding private memory.

**Limit of the available evidence:** [[lecture4-PRAM.pdf#page=4|Slide 4]] supports counting used cells, and [Tvrdik's lecture, “RAM model” and “PRAM model”](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html) explicitly states the unbounded-integer and shared-space conventions. Neither supplies an official ranking for this exam question. The ordering above is a reasoned explanation, not a verified marking scheme. Related note: [[PRAM#RAM and PRAM execution]].''',
    'AAPP-01-018': r'''**Assessment: referring back to the security example does not supply a valid example. Here is a different application, as requested.**

**Suggested exam answer — test whether an array is sorted:** Initialize a shared flag `sorted` to 1 in a separate step. Assign processor $P_i$ to adjacent elements $A[i]$ and $A[i+1]$. If $A[i]>A[i+1]$, it writes 0 to the flag; otherwise it does nothing. All simultaneous writes propose 0, satisfying common CW. Concurrent reads of shared adjacent elements are allowed by the CR part of CRCW.

```text
sorted = 1                       // separate initialization
in parallel for i = 0, ..., n-2:
    if A[i] > A[i+1]:
        sorted = 0
```

**Why it works:** A nondecreasing array has no adjacent inversion, so the flag stays 1. Otherwise at least one processor writes 0. For $[4,2,3,1]$, processors $P_0$ and $P_2$ both write 0 legally. Processors whose comparisons pass must not write 1 in the same phase. With $n-1$ processors, the test takes a constant number of rounds and $\Theta(n)$ work for $n\ge2$.

**Study and attribution:** [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]]. This worked sortedness example applies the Boolean-AND construction in [John E. Savage, *Models of Computation*, §7.9.2, proof of Theorem 7.9.2](https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter7.pdf#page=34): initialize to 1 and let only failing conditions write 0.''',
    'AAPP-01-019': r'''**Assessment: substantially correct; make the requested ordering explicit and refine the latency wording.** You identified the relevant assumptions. A memory access still takes a unit step; the idealization removes additional hardware latency and bandwidth costs.

**Suggested exam answer:** A defensible order is:

1. **Unit-time basic instructions:** each permitted basic computation has constant cost.
2. **Unit-time shared-memory access:** every processor can access any cell in constant time, with no extra bandwidth/contention penalty for accesses allowed by the chosen model.
3. **Synchronous execution:** processors advance in lock-step, with implicit synchronization and no additional synchronization overhead.

Together these assumptions let us count parallel steps to obtain $T_p(n)$. They do not imply evenly distributed work or remove algorithmic dependencies.

**About the ranking:** The available slides state these assumptions but do not give an official priority order. The ordering above follows their role in fixing operation costs and then counting global steps.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. The parallel unit-time memory-access assumption is also described by [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=4).''',
    'AAPP-01-020': r'''**Assessment: mostly correct; your virtual-processor explanation is the general answer.** Chunking can help redesign particular algorithms, such as a reduction, but a local phase followed by a parallel phase is not required for every PRAM computation.

**Suggested exam answer:** When there are more logical threads/virtual processors than physical processors, each physical processor simulates several virtual processors by time-sharing their work and retaining their separate local states. The simulation batches each original round while preserving read–compute–write ordering and the original memory-conflict policy. If $q$ virtual processors take $t$ rounds, then $p<q$ processors can simulate them in $O(t\lceil q/p\rceil)$ time with the same shared-memory assumptions. Fewer processors increase execution time; they do not create extra physical parallelism.

**Example:** Ten virtual processors on three physical processors require four batches per primitive phase. Preserve the virtual reads before committing writes that could change what later batches read; completing an entire round for one batch before reading for the next can change the result.

**Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slides 25–26]].''',
}

entry_pattern = re.compile(r'^### (AAPP-\d+-\d+)\n(.*?)(?=^### |^## |\Z)', re.M | re.S)
feedback_pattern = re.compile(r'^> \[!note\]- Feedback\n(?:>[^\n]*(?:\n|$))*', re.M)
answer_pattern = re.compile(r'\*\*My answer\*\*\s*(.*?)(?=^> \[!note\]- Feedback|\Z)', re.M | re.S)

new_attempts = []
for entry in entry_pattern.finditer(original):
    answer = answer_pattern.search(entry.group(2))
    if answer and answer.group(1).strip() not in ('', '*Write your answer here.*') and '> Not reviewed yet.' in entry.group(2):
        new_attempts.append(entry.group(1))
assert set(new_attempts) == set(reviews), f'New attempts changed: {new_attempts}'

def replace_entry(match):
    identifier, body = match.group(1, 2)
    if identifier not in reviews:
        return match.group(0)
    old_feedback = feedback_pattern.search(body)
    assert old_feedback and 'Not reviewed yet.' in old_feedback.group(0), identifier
    text = '**Reviewed: 2026-10-28.**\n\n' + reviews[identifier]
    callout = '> [!note]- Feedback\n' + '\n'.join('> ' + line if line else '>' for line in text.splitlines()) + '\n'
    return '### ' + identifier + '\n' + body[:old_feedback.start()] + callout + body[old_feedback.end():]

updated = entry_pattern.sub(replace_entry, original)
before_entries = {m.group(1): m.group(0) for m in entry_pattern.finditer(original)}
after_entries = {m.group(1): m.group(0) for m in entry_pattern.finditer(updated)}
assert len(before_entries) == len(after_entries) == 552
for identifier in before_entries:
    before, after = before_entries[identifier], after_entries[identifier]
    if identifier in reviews:
        assert feedback_pattern.sub('', before) == feedback_pattern.sub('', after), identifier
    else:
        assert before == after, identifier
assert entry_pattern.sub('', original) == entry_pattern.sub('', updated)
assert re.findall(r'^\^aapp-\d+-\d+$', original, re.M) == re.findall(r'^\^aapp-\d+-\d+$', updated, re.M)
assert updated.count('> Not reviewed yet.') == original.count('> Not reviewed yet.') - 8
assert updated.count('**Reviewed: 2026-10-28.**') == 8

notes = Path('University/Advanced Algorithms and Parallel Programming/Notes/PRAM.md').read_text()
headings = set(re.findall(r'^#{1,6} ([^\n]+)$', notes, re.M))
for text in reviews.values():
    for target in re.findall(r'\[\[PRAM#([^\]|]+)', text):
        assert target in headings, f'Unresolved PRAM heading: {target}'
assert Path('University/Advanced Algorithms and Parallel Programming/Slides/lecture4-PRAM.pdf').is_file()

backup = Path('outputs/pram-review-2026-10-28/Past Exam Question Bank.md.snapshot')
assert not backup.exists(), 'Backup already exists; inspect the current note before repeating'
backup.write_text(original)
assert bank.read_text() == original, 'Note changed during review; re-read before writing'
bank.write_text(updated)
assert bank.read_text() == updated
print('Reviewed 8 new attempts: AAPP-01-013 through AAPP-01-020.')
print('Verified all user answers and question text are unchanged; all 544 other entries, prior feedback, frontmatter, and section text are unchanged.')
print('Validated local citations and preserved all 552 block IDs.')
print('Pre-review copy:', backup)
