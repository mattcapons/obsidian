from pathlib import Path
import re

bank_path = Path('University/Advanced Algorithms and Parallel Programming/Past Exam Question Bank.md')

feedback = {
21: r'''**Assessment: mostly correct; refine the reason.** True is the intended answer. Your write-in-one-round/read-in-the-next explanation is correct. Synchronization primitives also enforce ordering and mutual exclusion in real programs; they are not mainly a remedy for mixed read/write conflicts. PRAM supplies the required phase ordering as part of the model. Same-phase read/read and write/write restrictions still apply.

**Suggested exam answer:** True, for exchanging data between synchronous PRAM rounds. All processors execute read, compute, and write phases in lockstep, with an implicit global barrier before the next round. A value written in round $r$ can therefore be read in round $r+1$ without programming a lock, signal, or barrier. The algorithm must still obey its EREW/CREW/CRCW memory-access rules.

**Study:** [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=5|slide 5]].''',

22: r'''**Assessment: partly correct; unit latency does not mean zero latency.** You correctly identify the idealization of bandwidth and simultaneous access. A permitted access costs one model step, independently of processor, address, or other permitted accesses. PRAM does not require a particular physical implementation such as a private channel per processor.

**Suggested exam answer:** Every processor can read or write any shared-memory cell in constant, unit time. All $p$ processors can perform permitted accesses simultaneously, with no extra penalty for network distance, cache misses, bandwidth saturation, or contention between permitted accesses. This makes communication costs independent of the machine's physical layout. Same-cell accesses must still satisfy the selected EREW/CREW/CRCW rule. Each access takes one model step, rather than zero time.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=4|slide 4]]. See also [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=4).''',

23: r'''**Assessment: incomplete; state the time bound and distinguish a fixed constant from a parameter.** You recognize that fewer processors limit parallelism, but the question needs a complexity statement. A processor bound does not make an algorithm inappropriate; excess virtual processors can be simulated.

**Suggested exam answer:** With $p$ available processors, at most $p$ basic operations execute per step, so an execution doing $W(n)$ operations needs at least $W(n)/p$ time; dependencies can impose a larger bound. If an algorithm uses $q>p$ virtual processors for $t(n)$ rounds, batching them gives a simulation in $O(t(n)\lceil q/p\rceil)$ time, preserving the shared memory and phase/access rules. If $p$ is a fixed constant independent of input size, parallelism can improve time only by a constant factor relative to an optimal sequential solution under the same instruction and memory assumptions. If $p=p(n)$ grows with $n$, retain it in the bound $T_p(n)$.

**Example:** Chunked summation takes $O(n/p+\log p)$ time for $1\le p\le n$. For fixed $p$, its worst-case time is $\Theta(n)$, like sequential summation.

**Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why work and depth give two different lower bounds]]; [[lecture4-PRAM.pdf#page=25|slide 25]].''',

24: r'''**Assessment: mostly correct about parallel access; replace “no latency” and describe the exchange.** Unit-time access means a fixed one-step latency. It also does not mean every processor can access arbitrarily many cells in one step, or that all same-cell accesses are legal.

**Suggested exam answer:** Processors communicate indirectly through shared memory: one processor writes a value, and another reads it in a subsequent round. Each permitted read/write has unit latency, independent of processor or address. All processors can make their permitted accesses in parallel, without an additional bandwidth or network-contention penalty. Same-cell accesses remain subject to EREW/CREW/CRCW rules. A value written in the write phase cannot already be observed during that round's earlier read phase.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]].''',

25: r'''**Assessment: mostly correct; synchronization does not eliminate every memory conflict.** Your account of lockstep phases and ideal shared-memory access is sound. Separate read and write phases prevent overlap between those phases, but simultaneous readers or writers can still violate the model's access policy. Access latency is fixed at one model step, with realistic additional delays ignored.

**Suggested exam answer:** PRAM assumes synchronous read–compute–write rounds with an implicit barrier, so the programmer does not implement synchronization between rounds. Communication uses globally addressable shared memory with unit-time permitted accesses in parallel. Cache behavior, network delays, bandwidth limits, and realistic synchronization overheads are abstracted away. Algorithm design can therefore focus on dependencies, parallel time, total work, and legal memory access. The algorithm must still satisfy EREW/CREW/CRCW rules, and a good PRAM bound must be reassessed when mapping it to real hardware.

**Study:** [[PRAM#Overview]]; [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=3|slides 3–6]].''',

26: r'''**Assessment: partly correct; explain each rule's correctness obligation.** Your common-write idea is useful, but the agreed value need not be a fixed constant chosen in advance: all actual writers to a cell must agree in that phase. An arbitrary or random winner does not make individual computations less important. Every possible winning value must satisfy the required correctness condition; probability-based claims need a specified random rule and analysis.

**Suggested exam answer:** The CW rule determines which algorithms and correctness proofs are valid. In **common CW**, all simultaneous writers to a cell must propose the same value. In **priority CW**, the highest-priority contender wins, allowing deterministic selection by processor priority. In **arbitrary CW**, any contender may win, so correctness must hold for every permitted winner. A **random CW** rule specifies a random winner and can support a probabilistic analysis. The same access pattern may be correct under one rule and incorrect under another.

**Example:** To compute Boolean OR under common CRCW, first set a flag to 0, then let only processors with true inputs write 1. All writers agree. Letting false-input processors also write 0 would violate common CW, and an arbitrary winner could give the wrong OR.

**Course terminology:** Slide 7 groups “Arbitrary/Random” together. Keep the unspecified-winner versus probabilistic-winner distinction explicit.

**Study:** [[PRAM#CRCW write rules]]; [[PRAM#A useful CRCW example: Boolean OR]]; [[lecture4-PRAM.pdf#page=7|slide 7]]; [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).''',

27: r'''**Assessment: correct; add the consequence for the cost model.** You correctly distinguish an unbounded integer from a fixed-width machine word. Be explicit that the question assumes the unbounded-word variant; an unbounded number of cells is a separate assumption.

**Suggested exam answer:** In the assumed variant, one cell stores an arbitrarily large integer without overflow or splitting it across words. Under the unit-cost instruction assumption, permitted primitive operations cost constant time independently of operand bit length, and space counts cells rather than bits. Real fixed-width machines may need several words and extra operations, so these bounds need not describe bit complexity. This word-size convention is model-dependent. See [Tvrdík, RAM model and constrained PRAM models](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).

**Example:** $2^{1000}$ occupies one cell under this assumption, although its binary representation requires 1001 bits. This does not mean an arbitrarily long sequence of operations takes one step.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]. The slide says one word/integer per cell; the exam prompt supplies the explicit unbounded-integer assumption.''',

28: r'''**Assessment: correct.** You identified global phase synchronization and the four phases used in the course. Add that the barrier is implicit in the ideal model, rather than an explicit runtime primitive with a separately analyzed waiting cost.

**Suggested exam answer:** PRAM uses synchronous, lockstep execution. Every round consists of read, local compute, write, and an implicit global barrier before the next round. No processor starts the next round until the current round is complete. Processors may be idle, and synchronization overhead is abstracted away. Textbooks that list only three read–compute–write phases include the same synchronization implicitly.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=5|slide 5]].''',

29: r'''**Assessment: correct central idea; make the answer self-contained.** “Unit-time simultaneous access” identifies the relevant assumption. In an exam, state what it guarantees directly; a reference to previous answers does not provide the requested explanation.

**Suggested exam answer:** The simplifying assumption is that every processor can access any shared-memory cell in unit time, and all processors can perform permitted accesses in parallel. The model therefore ignores extra costs from network distance, cache behavior, or limited aggregate memory bandwidth. Same-cell accesses still obey EREW/CREW/CRCW rules.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]].''',

30: r'''**Assessment: correct for exclusive-write PRAM, but too restrictive as a general definition.** You correctly identify the same address and simultaneous writes. Competing writes can also occur on CRCW, where the write rule specifies how they are handled. Equal proposed values still violate exclusive write.

**Suggested exam answer:** “A write conflict occurs when two or more processors attempt to write to the same shared-memory cell in the same write phase.” On EREW or CREW, this is illegal even when their proposed values coincide. On CRCW, the specified rule applies: common CW requires agreement, while priority or arbitrary CW selects a winning writer. Writes to different cells, or to the same cell in different rounds, do not create this simultaneous-write conflict.

**Study:** [[PRAM#Memory-access rules]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].''',

31: r'''**Assessment: mostly correct; connect portability to analysis of parallelism.** Your explanation of easier initial design and adapting an abstract algorithm to architectures is sound. Add what can actually be measured and what the model cannot predict by itself.

**Suggested exam answer:** PRAM provides a simple, machine-independent framework for designing parallel algorithms and analyzing their parallel time, work, dependencies, and memory conflicts. It helps identify available parallelism and compare algorithms before hardware details obscure the analysis. It also provides an optimistic benchmark: real implementations must add communication, bandwidth, cache, and synchronization costs. A PRAM algorithm is therefore a useful starting point for implementation, while a fast PRAM bound alone does not guarantee good real performance.

**Study:** [[PRAM#Overview]]; [[lecture4-PRAM.pdf#page=3|slide 3]]; [[lecture4-PRAM.pdf#page=24|slide 24]].''',

32: r'''**Assessment: incorrect; the intended answer is True.** You have reversed the direction of the model hierarchy. A more permissive machine allows additional access patterns; it does not force the program to make additional simultaneous accesses.

**Suggested exam answer:** Yes, assuming the same processors, instruction set, memory, and synchronous execution semantics. A valid EREW algorithm never has simultaneous readers or writers to one cell. Every access it makes is therefore also legal on CREW and on CRCW. Running the unchanged program preserves its access pattern and result; the CRCW write-resolution rule is never needed to choose between competing writers. Thus EREW algorithms run unchanged on these more permissive models.

**Direction matters:** A CREW algorithm that has several processors read the same cell in one phase is not automatically legal on EREW. That reverse direction may require copying or extra rounds.

**Study:** [[PRAM#Memory-access rules]]; [[PRAM#Deciding legality from addresses]]; [[lecture4-PRAM.pdf#page=6|slide 6]]. The access restrictions are also defined by [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).''',

33: r'''**Assessment: plausible conclusion, but correct the ratio and qualify what the lemma proves.** The memory ratio is $m/m'$, with $m$ simulated shared cells and $m'$ available shared cells. $p/p'$ is the processor ratio. For fixed $m,m'$, the stated ratio is unchanged by access order; a small working set can help only if the simulation exploits it.

**Suggested exam answer:** I would generally expect more degradation when accesses are spread over many simulated memory segments, because more serialized segment visits may be needed. A small working set that fits in the available shared memory may permit reuse and fewer visits. The slide's general simulation bound is $O(t\lceil m/m'\rceil)$ time, using $\max(p,m')$ processors. This is an upper bound, rather than an exact slowdown or a proof that one access pattern is always slower. The locality advantage is an inference about a simulation that exploits the working set. In the original ideal PRAM, random versus nearby addresses alone has no extra access cost.

**Storage assumption:** Reducing shared memory does not remove the simulated state. A standard proof retains the virtual cells in processor-local memory and uses the smaller shared memory for transfers; it does not store arbitrary $m$ words in $m'$ words of total storage. See [Tvrdík, “Simulation of large PRAMs on small PRAMs,” second lemma and proof](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).

**Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slides 25–26]].''',

34: r'''**Assessment: mostly correct; make synchronization and the amount of work per round explicit.** Your phase order and unit-cost idea are right. Three read–compute–write phases with implicit synchronization describe the same ordering as the course's four-phase presentation. Use “PRAM” rather than “RRAM.” Unbounded memory capacity does not allow one processor to access arbitrarily many cells in one step.

**Suggested exam answer:** A PRAM consists of processors with private registers that communicate through globally addressable shared memory. They execute synchronous rounds: read a shared value into local state, perform a basic local computation, write a result, and synchronize before the next round. Each processor performs only a constant amount of primitive work per round and may be idle. Permitted memory accesses and basic operations have unit cost. Simultaneous accesses must obey the chosen EREW/CREW/CRCW policy.

**Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–6]].''',

35: r'''**Assessment: mostly correct for exclusive access; add CRCW and the phase distinction.** You correctly identify same-cell access by multiple processors under an exclusive policy. The answer should also explain how concurrent writes are handled, including illegal disagreement under common CW. Two reads do not corrupt a value, but they still violate an exclusive-read rule.

**Suggested exam answer:** Simultaneous accesses to the same shared cell can produce read/read or write/write conflicts. On EREW, both are forbidden. On CREW, concurrent reads are allowed but concurrent writes are forbidden. On CRCW, concurrent writes follow a specified rule: common requires identical proposed values, priority selects the highest-priority writer, and arbitrary selects an unspecified contender. Different values violate common CW. Read and write phases are separated, so they do not overlap within a round. Accesses to distinct cells remain legal in parallel.

**Study:** [[PRAM#Memory-access rules]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=5|slides 5–7]].''',

36: r'''**Assessment: mostly correct; complete the shared-memory description and qualify “unlimited simultaneous accesses.”** Your main complexity argument is right: a round contains a constant number of unit-cost phases. The model lets all available processors access memory in parallel, subject to the access policy, rather than letting one processor perform an unbounded number of accesses in a round.

**Suggested exam answer:** Shared memory is a globally addressable array of cells through which processors communicate. In the ideal model its capacity is unbounded, and each permitted access costs one time unit independently of address or processor. All processors can make permitted accesses in parallel, subject to EREW/CREW/CRCW rules, without extra cache, network, bandwidth, or synchronization costs. Consequently, for a stated processor count $p$, parallel time $T_p(n)$ counts synchronous constant-time rounds. Operations performed concurrently do not add to elapsed time, although they do add to total work $W(n)$. Dependencies and repeated accesses across rounds still contribute to time.

**Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Performance quantities]]; [[lecture4-PRAM.pdf#page=4|slides 4–6]].''',
}

original = bank_path.read_bytes()
text = original.decode('utf-8')
for number, body in feedback.items():
    qid = f'AAPP-01-{number:03d}'
    pattern = rf'(^### {qid}\n.*?)(?=^### |^## |\Z)'
    match = re.search(pattern, text, re.M | re.S)
    if match is None:
        raise RuntimeError(f'Missing question: {qid}')
    old = '> [!note]- Feedback\n> Not reviewed yet.'
    if match[1].count(old) != 1:
        raise RuntimeError(f'Feedback already changed: {qid}')
    callout = '> [!note]- Feedback\n> **Reviewed: 2026-10-30.**\n>\n'
    callout += '\n'.join('> ' + line if line else '>' for line in body.splitlines())
    updated = match[1].replace(old, callout)
    text = text[:match.start()] + updated + text[match.end():]

# Preserve all original attempts and every part outside the selected feedback.
def without_feedback(s):
    for number in feedback:
        qid = f'AAPP-01-{number:03d}'
        pattern = rf'(^### {qid}\n.*?)(?=^### |^## |\Z)'
        match = re.search(pattern, s, re.M | re.S)
        block = match[1]
        block = re.sub(r'> \[!note\]- Feedback\n(?:>[^\n]*\n?)*', '[REVIEW]', block)
        s = s[:match.start()] + block + s[match.end():]
    return s

assert without_feedback(original.decode('utf-8')) == without_feedback(text)
assert [int(n) for n in re.findall(r'^### AAPP-01-(\d+)$', text, re.M)] == list(range(1, 37))
assert text.count('**Reviewed: 2026-10-30.**') == 16
assert bank_path.read_bytes() == original, 'Note changed while preparing corrections'
bank_path.write_bytes(text.encode('utf-8'))
print('Added feedback to AAPP-01-021–036; all original attempts and other text preserved.')
