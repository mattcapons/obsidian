from pathlib import Path
import re

bank = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')
original = bank.read_text()

reviews = {
    'AAPP-01-001': r'''**Assessment: mostly correct; add the memory assumptions.** Your definition and phase sequence are sound. Synchronization fixes the ordering of phases, but the algorithm must still satisfy the access rules.

**Suggested exam answer:** PRAM means Parallel Random Access Machine. It extends RAM to $p$ identical processors, each with private registers and a processor ID, communicating through a globally addressable shared memory. Processors execute synchronous rounds: read, compute locally, write, and synchronize before the next round. Basic operations and permitted shared-memory accesses take constant time; realistic communication and synchronization overheads are abstracted away. EREW, CREW, and CRCW specify which simultaneous accesses to the same cell are legal.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|lecture slides 4–6]]. The shared-memory and unit-time assumptions are also described by [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=3).''',
    'AAPP-01-002': r'''**Assessment: mostly correct; define the acronyms explicitly.** Your explanation that exclusive writes still permit parallel writes to different cells is correct. All processors follow the same phases, but a processor may be idle. “CREW is most used” is unnecessary here. Arbitrary selection and random selection should be distinguished.

**Suggested exam answer:** The rules concern access to the **same shared-memory cell in the same phase**. EREW means Exclusive Read, Exclusive Write: at most one reader and at most one writer per cell. CREW means Concurrent Read, Exclusive Write: several processors may read a cell, but at most one may write it. CRCW means Concurrent Read, Concurrent Write: both are permitted, with a specified write rule such as common, arbitrary, or priority. Concurrent access to distinct cells is permitted in all three models.

**Study:** [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=6|slide 6]]. See also [Middelburg, classification of PRAMs, printed p. 564](https://pure.uva.nl/ws/files/228009805/Imperative_Process_Algebra_and_Models_of_Parallel_Computation.pdf#page=38).''',
    'AAPP-01-003': r'''**Assessment: correct starting point, but incomplete as a definition.** Add shared memory, private registers, synchronous execution, and the unit-time assumption.

**Suggested exam answer:** A Parallel Random Access Machine is an idealized shared-memory parallel computer consisting of multiple RAM processors with private registers. They execute synchronously and communicate by reading and writing shared memory. Basic operations and permitted memory accesses take unit time, under a specified memory-access policy.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]; [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=3).''',
    'AAPP-01-004': r'''**Assessment: the central rule is correct; change “an error is raised.”** The model does not guarantee a runtime exception. An algorithm that proposes different values in a common-write phase violates the model; the slides call its state undefined.

**Suggested exam answer:** Common CRCW permits concurrent reads and concurrent writes to the same memory cell, provided that all simultaneous writers to that cell propose the same value. The algorithm must guarantee this condition. Conflicting values make that step illegal under common CRCW.

**Study:** [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=7|slide 7]]; [Karp and Ramachandran, §2.1, printed p. 873](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).''',
    'AAPP-01-005': r'''**Assessment: correct for the course presentation.** You identified all four phases and their purposes. Specify that synchronization is implicit in the ideal PRAM model; it does not require a programmed barrier with realistic waiting overhead.

**Suggested exam answer:** Each synchronous round consists of: (1) read the required shared-memory/input value into private registers; (2) perform a basic local computation; (3) write the result to shared memory/output, obeying the memory-access rule; and (4) synchronize before starting the next round. Processors may be idle in a phase.

**Convention:** The course lists the barrier as a fourth phase. Textbooks often describe three read–compute–write phases with synchronization implicit. These describe the same ordering, rather than different algorithms.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [Blelloch, Dhulipala and Sun, §8.1](https://www.cs.cmu.edu/~guyb/paralg/paralg/parallel.pdf#page=52).''',
    'AAPP-01-006': r'''**Assessment: partly correct; remove “who writes last” and “the result is not critical.”** You correctly say the winner is unspecified. However, the model defines simultaneous writes, with no chronological last writer. Correctness must hold for every permitted winner.

**Suggested exam answer:** Under arbitrary concurrent write, when several processors write to the same cell in one phase, exactly one contender succeeds, with no guarantee about which. The algorithm must produce a correct result regardless of that choice. “Arbitrary” does not imply any probability distribution; a random-write rule would specify one.

**Course wording:** [[lecture4-PRAM.pdf#page=7|Slide 7]] groups “Arbitrary/Random” together and says a randomly chosen writer succeeds. For the exam, state that one unspecified contender succeeds, then mention the slide's terminology if needed. The precise distinction is already explained in [[PRAM#CRCW write rules]] and supported by [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).''',
    'AAPP-01-007': r'''**Assessment: relevant notation, but it does not answer how time is counted.** Your $T^*$ and $T_1$ distinction is useful for performance comparisons. Use $T_p(n)$, with $n$ for input size and $p$ for processor count, to avoid confusing these quantities.

**Suggested exam answer:** For a fixed input size $n$ and processor count $p$, parallel time $T_p(n)$ is the number of synchronous constant-time steps/rounds until the algorithm finishes. Operations performed simultaneously count as one time step, not one step per processor. Analyze the dependent sequence of rounds, including loops and inactive periods; total operations across processors measure work instead.

**Example:** A tree reduction of $n$ inputs has $\Theta(\log n)$ parallel time with enough processors, while performing $\Theta(n)$ total work.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Performance quantities]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [Blelloch, Dhulipala and Sun, §8.1](https://www.cs.cmu.edu/~guyb/paralg/paralg/parallel.pdf#page=52).''',
    'AAPP-01-008': r'''**Assessment: no answer supplied; reference answer below.**

**Suggested exam answer:** Processors communicate indirectly: one writes a value into a shared-memory cell and another reads it in a subsequent read phase. Each permitted access has unit latency, independent of processor or address. All processors may perform permitted accesses in parallel without an extra bandwidth or network-contention penalty. Accesses to the same cell must still obey EREW/CREW/CRCW rules.

**Timing example:** If $P_0$ writes 7 to $A$ during round $r$, $P_1$ can read that new value in round $r+1$. The read phase of round $r$ happens before that write.

**Meaning of the idealization:** “No communication overhead” removes additional hardware delays; a read or write still occupies a model step. It does not mean that dependent communication can happen instantaneously within the same read phase.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. The bandwidth and latency idealization is discussed explicitly by [Culler et al., *LogP*, §6.1](https://www.cs.cornell.edu/tve/papers-ucb/ppopp93.pdf#page=18).''',
    'AAPP-01-009': r'''**Assessment: no answer supplied; the intended answer is True, under the usual model comparison.**

**Suggested exam answer:** PRAM is an optimistic model: it gives processors unit-time access to shared memory and removes realistic communication and synchronization overheads. If a problem is proven to have no efficient solution even in an appropriately powerful PRAM model, conventional parallel machines with comparable computational operations and resources cannot overcome that lower bound merely through their architecture. They must also contend with costs that PRAM ignores.

**Qualification:** The comparison must use compatible processor counts, operations, and memory rules. A bound for a restricted EREW model alone need not apply unchanged to CRCW. Also, “no efficient solution exists” is stronger than “we have not found one.” The reverse implication fails: an efficient PRAM algorithm may perform poorly on real hardware.

**Study and source:** [[PRAM#Overview]]; [[lecture4-PRAM.pdf#page=3|slide 3]]. [Pavel Tvrdik's university lecture, “PRAM model”](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html) explicitly presents the exam's statement as a reason to use PRAM as a benchmark. The qualifications above explain the intended comparison; the available exam PDF contains no marking key.''',
    'AAPP-01-010': r'''**Assessment: incorrect; equal work distribution is not a PRAM assumption.** Work assignment is a property of the algorithm and schedule. Dependencies can leave processors idle even on an ideal PRAM.

**Suggested exam answer:** The main assumptions are that basic instructions and permitted memory accesses take constant/unit time, and that processors execute synchronously in lock-step. Communication and synchronization have no additional hardware overhead. Therefore elapsed parallel time can be measured by counting synchronous steps until completion.

**Counterexample to your answer:** Near the end of a tree reduction, only one addition remains. The other processors are idle, but the computation is still a valid PRAM computation.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Reading a processor-time diagram]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]].''',
    'AAPP-01-011': r'''**Assessment: no answer supplied; reference answer below.**

**Suggested exam answer:** Every processor can access any shared-memory cell in unit time, independent of the address or the number of other permitted simultaneous accesses. The model therefore abstracts away interconnection topology, cache effects, bandwidth limitations, and additional communication latency. Same-cell accesses must still satisfy the selected memory-access rules.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]; [Culler et al., *LogP*, §6.1](https://www.cs.cornell.edu/tve/papers-ucb/ppopp93.pdf#page=18).''',
    'AAPP-01-012': r'''**Assessment: partly correct; separate the conflict from the rule that handles it.** Your examples identify illegal exclusive writes and an illegal common-write case. However, two processors targeting one shared cell in the same write phase already constitute write contention, even if their values agree. A CRCW policy specifies how such simultaneous writes are handled.

**Suggested exam answer:** A write conflict occurs when two or more processors attempt to write to the same shared-memory cell in the same write phase. Exclusive-write models prohibit this, even for equal values. CRCW permits it under its specified rule: common requires all values to agree, arbitrary lets one unspecified writer succeed, and priority selects the writer with highest priority. Writes to distinct cells do not conflict.

**Study:** [[PRAM#Deciding legality from addresses]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].''',
}

entry_pattern = re.compile(r'^### (AAPP-\d+-\d+)\n(.*?)(?=^### |^## |\Z)', re.M | re.S)
feedback_pattern = re.compile(r'^> \[!note\]- Feedback\n(?:>[^\n]*(?:\n|$))*', re.M)

attempted = []
for entry in entry_pattern.finditer(original):
    answer = re.search(r'\*\*My answer\*\*\s*(.*?)(?=^> \[!note\]- Feedback|\Z)', entry.group(2), re.M | re.S)
    if answer and answer.group(1).strip() not in ('', '*Write your answer here.*'):
        attempted.append(entry.group(1))
assert set(attempted) == set(reviews), f'Attempts changed: {attempted}'

def replace_entry(match):
    identifier, body = match.group(1, 2)
    if identifier not in reviews:
        return match.group(0)
    old_feedback = feedback_pattern.search(body)
    assert old_feedback, identifier
    assert 'Not reviewed yet.' in old_feedback.group(0), f'{identifier} already reviewed'
    text = '**Reviewed: 2026-10-27.**\n\n' + reviews[identifier]
    callout = '> [!note]- Feedback\n' + '\n'.join('> ' + line if line else '>' for line in text.splitlines()) + '\n'
    return '### ' + identifier + '\n' + body[:old_feedback.start()] + callout + body[old_feedback.end():]

updated = entry_pattern.sub(replace_entry, original)
updated = updated.replace('status: unanswered\n', 'status: in-progress\n', 1)
old_intro = 'Questions collected from the supplied 2022–2026 exams, grouped by subject for revision and future reference answers. **No answers or newly generated questions are included.**'
new_intro = 'Questions collected from the supplied 2022–2026 exams, grouped by subject for revision and practice. Original prompts are preserved, with your attempts and review feedback beneath the questions you have worked on.'
assert old_intro in updated
updated = updated.replace(old_intro, new_intro, 1)

before_entries = {m.group(1): m.group(0) for m in entry_pattern.finditer(original)}
after_entries = {m.group(1): m.group(0) for m in entry_pattern.finditer(updated)}
assert len(before_entries) == len(after_entries) == 552
for identifier in before_entries:
    before, after = before_entries[identifier], after_entries[identifier]
    if identifier in reviews:
        assert feedback_pattern.sub('', before) == feedback_pattern.sub('', after), identifier
    else:
        assert before == after, identifier
assert re.findall(r'^\^aapp-\d+-\d+$', original, re.M) == re.findall(r'^\^aapp-\d+-\d+$', updated, re.M)
assert re.findall(r'!?\[\[.*?\]\]', original[:original.index('## PRAM model and memory rules')]) == re.findall(r'!?\[\[.*?\]\]', updated[:updated.index('## PRAM model and memory rules')])
assert updated.count('> Not reviewed yet.') == original.count('> Not reviewed yet.') - 12
assert original.split('---', 2)[1].replace('status: unanswered', 'status: in-progress') == updated.split('---', 2)[1]

# Resolve the new local citations and the exact heading targets.
notes = Path('University/Advanced Algorithms and Parallel Programming/Notes/PRAM.md').read_text()
headings = set(re.findall(r'^#{1,6} ([^\n]+)$', notes, re.M))
for text in reviews.values():
    for target in re.findall(r'\[\[PRAM#([^\]|]+)', text):
        assert target in headings, f'Unresolved PRAM heading: {target}'
assert Path('University/Advanced Algorithms and Parallel Programming/Slides/lecture4-PRAM.pdf').is_file()

backup = Path('outputs/pram-review-2026-10-27/Past Exam Question Bank.md.snapshot')
assert not backup.exists(), 'Review backup already exists; inspect the current note before repeating'
backup.write_text(original)
assert bank.read_text() == original, 'Note changed during review; re-read before writing'
bank.write_text(updated)
assert bank.read_text() == updated
print('Reviewed 12 attempts (AAPP-01-001 through AAPP-01-012).')
print('Preserved all original attempts, question bodies, IDs, and 540 untouched question entries.')
print('Validated local feedback citations; updated bank status and introduction.')
print('Saved the pre-review note to:', backup)
