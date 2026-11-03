---
tags:
  - aapp
  - exam-practice
  - question-bank
status: in-progress
created: 2026-10-15
---
# AAPP — Past Exam Question Bank

[[AAPP Index|Course index]]

Questions collected from the supplied 2022–2026 exams, grouped by subject for revision and practice. Original prompts are preserved, with your attempts, review feedback, and a collapsed **Model answer** for every question.

> [!info] How to use this bank
> Each entry has a stable question ID and an original exam/page reference. Write beneath **My answer**, replacing the placeholder with your reasoning, calculations, or code. The exams repeatedly state that an unsupported answer is invalid. Points in parentheses are the original marks where available.
>
> When ready, ask: “Correct my answer to AAPP-01-001” or “Review the answers I have filled in under PRAM model and memory rules.” Feedback will go in the collapsed **Feedback** callout beneath your answer, preserving your attempt. Your **My answer** space stays available for practice, even when a reference answer is provided below it.

## Contents

- [[#PRAM model and memory rules]] — 36 questions
- [[#Parallel performance and scaling]] — 41 questions
- [[#PRAM algorithms]] — 9 questions
- [[#Divide and conquer and recurrences]] — 19 questions
- [[#Randomized algorithm classes]] — 9 questions
- [[#Minimum cut]] — 12 questions
- [[#Sorting and partitioning]] — 20 questions
- [[#Selection and order statistics]] — 12 questions
- [[#Primality testing]] — 7 questions
- [[#Dynamic programming and LCS]] — 19 questions
- [[#BDDs and memoization]] — 12 questions
- [[#Treaps]] — 19 questions
- [[#Skip lists]] — 9 questions
- [[#Disjoint sets]] — 2 questions
- [[#Amortized analysis]] — 19 questions
- [[#Online algorithms and competitive analysis]] — 15 questions
- [[#Parallel design and architectures]] — 16 questions
- [[#Dependences and loop parallelization]] — 42 questions
- [[#Parallel patterns]] — 65 questions
- [[#Task graphs and OpenMP implementations]] — 13 questions
- [[#OpenMP]] — 55 questions
- [[#Pthreads and shared-memory synchronization]] — 18 questions
- [[#MPI]] — 70 questions
- [[#CUDA]] — 8 questions
- [[#Halide and high-level synthesis]] — 5 questions

> [!tip] Reference answers added — 2026-11-02
> Every one of the 552 entries has a collapsed **Model answer**, including previously unanswered or incomplete questions. Your original attempts and existing feedback are preserved. Try a question under **My answer** whenever useful, then expand the reference or request correction by its stable ID.
>
> Model answers state necessary assumptions, distinguish expected/worst-case/amortized costs, and flag defects in the printed source. Where the supplied notes do not identify a lecture-specific example, a standard example is explicitly labelled. Programming-model references use official OpenMP/MPI/CUDA/Halide documentation or the POSIX manual. Code is exam-style pseudocode or an illustrative snippet unless stated otherwise.

## Editorial conventions

- Repeated questions with identical extracted wording are listed once with all their sources; distinct wording and technical variants are retained. Questions in the 2022 A/B papers are therefore combined only when their wording matches.
- Original exercise/subquestion labels, requirements, numerical values, and code are preserved. Blank answer lines, cover instructions, and challenge-based exemptions are omitted. A multi-part prompt without separate letter labels remains one entry.
- Page links use physical PDF pages. Embedded source pages retain task graphs, task weights, and cancellation timelines that plain text cannot capture. Some diagrams are shared by several entries.
- Source filenames identify exam sessions. Some PDFs contain copied footers with a different date; follow the linked source rather than treating a footer as a separate exam.
- Wording, claims to discuss, and apparent source errors are left as questions, not corrected into answers. In particular, check the bounds and increment in the September 2025 loop exactly as printed.
- Links to existing notes indicate related study material, not a guarantee that every question is already covered. Topics without a dedicated note remain included.

> [!warning] Future review pass
> When correction is requested, review the specified attempts using the course notes and source PDFs. Preserve the original answers and add feedback separately: identify what is correct, explain errors or omissions, and provide a corrected answer. Preserve assumptions and distinguish expected, worst-case, and amortized bounds. Where material is still missing, mark feedback as pending rather than inventing a course-specific explanation. Reference answers are now explicitly requested for all questions. Continue preserving **My answer** as your practice space; future corrections should assess your attempt independently of the supplied model.

## PRAM model and memory rules

Related notes: [[PRAM]].

### AAPP-01-001

Describe the main characteristics of a PRAM model. (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=2|2022-11-08-1st · Exercise 1A · p. 2]]

^aapp-01-001

**My answer**

A PRAM model stand for  Parallel Random Access Machine. It is an extension of the RAM model, with the addition of multiple compute units. It is based on a cycle based behavior, where there are 4 states: Read, Compute, Write, Barrier. All units are syncronized to be in the same state and cycle togheter. This way  we can avoid many data conflicts that would arise. There are still some so we have different combination of Concurrent or Exclusive  behavior for the Read and the Write. 

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: mostly correct; add the memory assumptions.** Your definition and phase sequence are sound. Synchronization fixes the ordering of phases, but the algorithm must still satisfy the access rules.
>
> **Suggested exam answer:** PRAM means Parallel Random Access Machine. It extends RAM to $p$ identical processors, each with private registers and a processor ID, communicating through a globally addressable shared memory. Processors execute synchronous rounds: read, compute locally, write, and synchronize before the next round. Basic operations and permitted shared-memory accesses take constant time; realistic communication and synchronization overheads are abstracted away. EREW, CREW, and CRCW specify which simultaneous accesses to the same cell are legal.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|lecture slides 4–6]]. The shared-memory and unit-time assumptions are also described by [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=3).

> [!success]- Model answer
> **Suggested exam answer:** PRAM means Parallel Random Access Machine. It extends RAM to $p$ identical processors, each with private registers and a processor ID, communicating through a globally addressable shared memory. Processors execute synchronous rounds: read, compute locally, write, and synchronize before the next round. Basic operations and permitted shared-memory accesses take constant time; realistic communication and synchronization overheads are abstracted away. EREW, CREW, and CRCW specify which simultaneous accesses to the same cell are legal.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|lecture slides 4–6]]. The shared-memory and unit-time assumptions are also described by [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=3).

### AAPP-01-002

Please describe the type of Read/Write abilities a PRAM may have. (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1B · p. 2]]

^aapp-01-002

**My answer**

A PRAM model has multiple compute units and each one has to read or write at the same time. So there are no real read/write conflicts, but just read/read and write/write. In order to regulate those we can choose EREW, CREW, CRCW. CREW is most used because the read can happen concurrently which usually does not cause problems, while the write can't happen concurrently on the same element, but it can on 2 different elements. CRCW introduces new choices because we can choose different ways to select which of the concurrent writers can win, for example random or priority based.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: mostly correct; define the acronyms explicitly.** Your explanation that exclusive writes still permit parallel writes to different cells is correct. All processors follow the same phases, but a processor may be idle. “CREW is most used” is unnecessary here. Arbitrary selection and random selection should be distinguished.
>
> **Suggested exam answer:** The rules concern access to the **same shared-memory cell in the same phase**. EREW means Exclusive Read, Exclusive Write: at most one reader and at most one writer per cell. CREW means Concurrent Read, Exclusive Write: several processors may read a cell, but at most one may write it. CRCW means Concurrent Read, Concurrent Write: both are permitted, with a specified write rule such as common, arbitrary, or priority. Concurrent access to distinct cells is permitted in all three models.
>
> **Study:** [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=6|slide 6]]. See also [Middelburg, classification of PRAMs, printed p. 564](https://pure.uva.nl/ws/files/228009805/Imperative_Process_Algebra_and_Models_of_Parallel_Computation.pdf#page=38).

> [!success]- Model answer
> **Suggested exam answer:** The rules concern access to the **same shared-memory cell in the same phase**. EREW means Exclusive Read, Exclusive Write: at most one reader and at most one writer per cell. CREW means Concurrent Read, Exclusive Write: several processors may read a cell, but at most one may write it. CRCW means Concurrent Read, Concurrent Write: both are permitted, with a specified write rule such as common, arbitrary, or priority. Concurrent access to distinct cells is permitted in all three models.
>
> **Study:** [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=6|slide 6]]. See also [Middelburg, classification of PRAMs, printed p. 564](https://pure.uva.nl/ws/files/228009805/Imperative_Process_Algebra_and_Models_of_Parallel_Computation.pdf#page=38).

### AAPP-01-003

Please define a PRAM. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1A · p. 2]]

^aapp-01-003

**My answer**

PRAM stands for Parallel Random Access Machine. It is an extension of the RAM model, but with multiple compute units.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: correct starting point, but incomplete as a definition.** Add shared memory, private registers, synchronous execution, and the unit-time assumption.
>
> **Suggested exam answer:** A Parallel Random Access Machine is an idealized shared-memory parallel computer consisting of multiple RAM processors with private registers. They execute synchronously and communicate by reading and writing shared memory. Basic operations and permitted memory accesses take unit time, under a specified memory-access policy.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]; [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=3).

> [!success]- Model answer
> **Suggested exam answer:** A Parallel Random Access Machine is an idealized shared-memory parallel computer consisting of multiple RAM processors with private registers. They execute synchronously and communicate by reading and writing shared memory. Basic operations and permitted memory accesses take unit time, under a specified memory-access policy.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]; [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=3).

### AAPP-01-004

Please describe what “Common CRCW” means. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1B · p. 2]]

^aapp-01-004

**My answer**

In CRCW the writes can be concurrent on the same element, but it need a strategy to handle them. The common strategy is that all writes on the same element must be the same, so if a writer is different than the others an error is raised.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: the central rule is correct; change “an error is raised.”** The model does not guarantee a runtime exception. An algorithm that proposes different values in a common-write phase violates the model; the slides call its state undefined.
>
> **Suggested exam answer:** Common CRCW permits concurrent reads and concurrent writes to the same memory cell, provided that all simultaneous writers to that cell propose the same value. The algorithm must guarantee this condition. Conflicting values make that step illegal under common CRCW.
>
> **Study:** [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=7|slide 7]]; [Karp and Ramachandran, §2.1, printed p. 873](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

> [!success]- Model answer
> **Suggested exam answer:** Common CRCW permits concurrent reads and concurrent writes to the same memory cell, provided that all simultaneous writers to that cell propose the same value. The algorithm must guarantee this condition. Conflicting values make that step illegal under common CRCW.
>
> **Study:** [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=7|slide 7]]; [Karp and Ramachandran, §2.1, printed p. 873](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

### AAPP-01-005

Please define the different phases followed in a PRAM computation. (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1A · p. 2]]

^aapp-01-005

**My answer**

There are 4 different phases in a PRAM computation. Read, all units read the data they need, this is usually concurrent but it can be exclusive too. Compute, they utilize the data to obtain a result, each locally. Write, every unit writes their result, it can be concurrent or exclusive. Barrier, halts the units until all are ready to allow synchronization.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: correct for the course presentation.** You identified all four phases and their purposes. Specify that synchronization is implicit in the ideal PRAM model; it does not require a programmed barrier with realistic waiting overhead.
>
> **Suggested exam answer:** Each synchronous round consists of: (1) read the required shared-memory/input value into private registers; (2) perform a basic local computation; (3) write the result to shared memory/output, obeying the memory-access rule; and (4) synchronize before starting the next round. Processors may be idle in a phase.
>
> **Convention:** The course lists the barrier as a fourth phase. Textbooks often describe three read–compute–write phases with synchronization implicit. These describe the same ordering, rather than different algorithms.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [Blelloch, Dhulipala and Sun, §8.1](https://www.cs.cmu.edu/~guyb/paralg/paralg/parallel.pdf#page=52).

> [!success]- Model answer
> **Suggested exam answer:** Each synchronous round consists of: (1) read the required shared-memory/input value into private registers; (2) perform a basic local computation; (3) write the result to shared memory/output, obeying the memory-access rule; and (4) synchronize before starting the next round. Processors may be idle in a phase.
>
> **Convention:** The course lists the barrier as a fourth phase. Textbooks often describe three read–compute–write phases with synchronization implicit. These describe the same ordering, rather than different algorithms.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [Blelloch, Dhulipala and Sun, §8.1](https://www.cs.cmu.edu/~guyb/paralg/paralg/parallel.pdf#page=52).

### AAPP-01-006

Please describe what “Arbitrary CW” means. (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1B · p. 2]]

^aapp-01-006

**My answer**

When the writes are concurrent in PRAM there is a need for a strategy on how to handle them. The arbitrary strategy means that there is no guarantee on which succeeds but is just who writes last. It is used when the result is not critical and can vary.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: partly correct; remove “who writes last” and “the result is not critical.”** You correctly say the winner is unspecified. However, the model defines simultaneous writes, with no chronological last writer. Correctness must hold for every permitted winner.
>
> **Suggested exam answer:** Under arbitrary concurrent write, when several processors write to the same cell in one phase, exactly one contender succeeds, with no guarantee about which. The algorithm must produce a correct result regardless of that choice. “Arbitrary” does not imply any probability distribution; a random-write rule would specify one.
>
> **Course wording:** [[lecture4-PRAM.pdf#page=7|Slide 7]] groups “Arbitrary/Random” together and says a randomly chosen writer succeeds. For the exam, state that one unspecified contender succeeds, then mention the slide's terminology if needed. The precise distinction is already explained in [[PRAM#CRCW write rules]] and supported by [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

> [!success]- Model answer
> **Suggested exam answer:** Under arbitrary concurrent write, when several processors write to the same cell in one phase, exactly one contender succeeds, with no guarantee about which. The algorithm must produce a correct result regardless of that choice. “Arbitrary” does not imply any probability distribution; a random-write rule would specify one.
>
> **Course wording:** [[lecture4-PRAM.pdf#page=7|Slide 7]] groups “Arbitrary/Random” together and says a randomly chosen writer succeeds. For the exam, state that one unspecified contender succeeds, then mention the slide's terminology if needed. The precise distinction is already explained in [[PRAM#CRCW write rules]] and supported by [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

### AAPP-01-007

How the time complexity in a PRAM model is computed? (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1A · p. 2]]

^aapp-01-007

**My answer**

First there is the time complexity T* of the best sequential algorithm with the same function. Then there is the T1 which is the parallel algorithm but run on a single processor and then Tn which is on n processors.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: relevant notation, but it does not answer how time is counted.** Your $T^*$ and $T_1$ distinction is useful for performance comparisons. Use $T_p(n)$, with $n$ for input size and $p$ for processor count, to avoid confusing these quantities.
>
> **Suggested exam answer:** For a fixed input size $n$ and processor count $p$, parallel time $T_p(n)$ is the number of synchronous constant-time steps/rounds until the algorithm finishes. Operations performed simultaneously count as one time step, not one step per processor. Analyze the dependent sequence of rounds, including loops and inactive periods; total operations across processors measure work instead.
>
> **Example:** A tree reduction of $n$ inputs has $\Theta(\log n)$ parallel time with enough processors, while performing $\Theta(n)$ total work.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Performance quantities]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [Blelloch, Dhulipala and Sun, §8.1](https://www.cs.cmu.edu/~guyb/paralg/paralg/parallel.pdf#page=52).

> [!success]- Model answer
> **Suggested exam answer:** For a fixed input size $n$ and processor count $p$, parallel time $T_p(n)$ is the number of synchronous constant-time steps/rounds until the algorithm finishes. Operations performed simultaneously count as one time step, not one step per processor. Analyze the dependent sequence of rounds, including loops and inactive periods; total operations across processors measure work instead.
>
> **Example:** A tree reduction of $n$ inputs has $\Theta(\log n)$ parallel time with enough processors, while performing $\Theta(n)$ total work.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Performance quantities]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [Blelloch, Dhulipala and Sun, §8.1](https://www.cs.cmu.edu/~guyb/paralg/paralg/parallel.pdf#page=52).

### AAPP-01-008

How is the communication via shared memory performed in a PRAM model? (latency vs parallel accesses) (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1B · p. 2]]

^aapp-01-008

**My answer**

I don't know

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: no answer supplied; reference answer below.**
>
> **Suggested exam answer:** Processors communicate indirectly: one writes a value into a shared-memory cell and another reads it in a subsequent read phase. Each permitted access has unit latency, independent of processor or address. All processors may perform permitted accesses in parallel without an extra bandwidth or network-contention penalty. Accesses to the same cell must still obey EREW/CREW/CRCW rules.
>
> **Timing example:** If $P_0$ writes 7 to $A$ during round $r$, $P_1$ can read that new value in round $r+1$. The read phase of round $r$ happens before that write.
>
> **Meaning of the idealization:** “No communication overhead” removes additional hardware delays; a read or write still occupies a model step. It does not mean that dependent communication can happen instantaneously within the same read phase.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. The bandwidth and latency idealization is discussed explicitly by [Culler et al., *LogP*, §6.1](https://www.cs.cornell.edu/tve/papers-ucb/ppopp93.pdf#page=18).

> [!success]- Model answer
> **Suggested exam answer:** Processors communicate indirectly: one writes a value into a shared-memory cell and another reads it in a subsequent read phase. Each permitted access has unit latency, independent of processor or address. All processors may perform permitted accesses in parallel without an extra bandwidth or network-contention penalty. Accesses to the same cell must still obey EREW/CREW/CRCW rules.
>
> **Timing example:** If $P_0$ writes 7 to $A$ during round $r$, $P_1$ can read that new value in round $r+1$. The read phase of round $r$ happens before that write.
>
> **Meaning of the idealization:** “No communication overhead” removes additional hardware delays; a read or write still occupies a model step. It does not mean that dependent communication can happen instantaneously within the same read phase.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. The bandwidth and latency idealization is discussed explicitly by [Culler et al., *LogP*, §6.1](https://www.cs.cornell.edu/tve/papers-ucb/ppopp93.pdf#page=18).

### AAPP-01-009

Discuss the following sentence: “If a problem has no feasible/efficient solution on PRAM, it has no feasible/efficient solution for any parallel machine.” True or False? (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1C · p. 2]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1C · p. 2]]

^aapp-01-009

**My answer**

I don't know

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: no answer supplied; the intended answer is True, under the usual model comparison.**
>
> **Suggested exam answer:** PRAM is an optimistic model: it gives processors unit-time access to shared memory and removes realistic communication and synchronization overheads. If a problem is proven to have no efficient solution even in an appropriately powerful PRAM model, conventional parallel machines with comparable computational operations and resources cannot overcome that lower bound merely through their architecture. They must also contend with costs that PRAM ignores.
>
> **Qualification:** The comparison must use compatible processor counts, operations, and memory rules. A bound for a restricted EREW model alone need not apply unchanged to CRCW. Also, “no efficient solution exists” is stronger than “we have not found one.” The reverse implication fails: an efficient PRAM algorithm may perform poorly on real hardware.
>
> **Study and source:** [[PRAM#Overview]]; [[lecture4-PRAM.pdf#page=3|slide 3]]. [Pavel Tvrdik's university lecture, “PRAM model”](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html) explicitly presents the exam's statement as a reason to use PRAM as a benchmark. The qualifications above explain the intended comparison; the available exam PDF contains no marking key.

> [!success]- Model answer
> **Suggested exam answer:** PRAM is an optimistic model: it gives processors unit-time access to shared memory and removes realistic communication and synchronization overheads. If a problem is proven to have no efficient solution even in an appropriately powerful PRAM model, conventional parallel machines with comparable computational operations and resources cannot overcome that lower bound merely through their architecture. They must also contend with costs that PRAM ignores.
>
> **Qualification:** The comparison must use compatible processor counts, operations, and memory rules. A bound for a restricted EREW model alone need not apply unchanged to CRCW. Also, “no efficient solution exists” is stronger than “we have not found one.” The reverse implication fails: an efficient PRAM algorithm may perform poorly on real hardware.
>
> **Study and source:** [[PRAM#Overview]]; [[lecture4-PRAM.pdf#page=3|slide 3]]. [Pavel Tvrdik's university lecture, “PRAM model”](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html) explicitly presents the exam's statement as a reason to use PRAM as a benchmark. The qualifications above explain the intended comparison; the available exam PDF contains no marking key.

### AAPP-01-010

Which of the PRAM model’s assumptions help to compute the time complexity? (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1A · p. 2]]

^aapp-01-010

**My answer**

That work is split evenly among all processors.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: incorrect; equal work distribution is not a PRAM assumption.** Work assignment is a property of the algorithm and schedule. Dependencies can leave processors idle even on an ideal PRAM.
>
> **Suggested exam answer:** The main assumptions are that basic instructions and permitted memory accesses take constant/unit time, and that processors execute synchronously in lock-step. Communication and synchronization have no additional hardware overhead. Therefore elapsed parallel time can be measured by counting synchronous steps until completion.
>
> **Counterexample to your answer:** Near the end of a tree reduction, only one addition remains. The other processors are idle, but the computation is still a valid PRAM computation.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Reading a processor-time diagram]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]].

> [!success]- Model answer
> **Suggested exam answer:** The main assumptions are that basic instructions and permitted memory accesses take constant/unit time, and that processors execute synchronously in lock-step. Communication and synchronization have no additional hardware overhead. Therefore elapsed parallel time can be measured by counting synchronous steps until completion.
>
> **Counterexample to your answer:** Near the end of a tree reduction, only one addition remains. The other processors are idle, but the computation is still a valid PRAM computation.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Reading a processor-time diagram]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]].

### AAPP-01-011

Which of the assumptions of the PRAM model simplifies the communication between processor and memory? (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1B · p. 2]]

^aapp-01-011

**My answer**

I don't know

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: no answer supplied; reference answer below.**
>
> **Suggested exam answer:** Every processor can access any shared-memory cell in unit time, independent of the address or the number of other permitted simultaneous accesses. The model therefore abstracts away interconnection topology, cache effects, bandwidth limitations, and additional communication latency. Same-cell accesses must still satisfy the selected memory-access rules.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]; [Culler et al., *LogP*, §6.1](https://www.cs.cornell.edu/tve/papers-ucb/ppopp93.pdf#page=18).

> [!success]- Model answer
> **Suggested exam answer:** Every processor can access any shared-memory cell in unit time, independent of the address or the number of other permitted simultaneous accesses. The model therefore abstracts away interconnection topology, cache effects, bandwidth limitations, and additional communication latency. Same-cell accesses must still satisfy the selected memory-access rules.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]; [Culler et al., *LogP*, §6.1](https://www.cs.cornell.edu/tve/papers-ucb/ppopp93.pdf#page=18).

### AAPP-01-012

Please define when a write conflict occurs in a PRAM model. (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1C · p. 2]]

^aapp-01-012

**My answer**

Either when the write is exclusive and 2 units want to write the same element in the same cycle. Otherwise if the write is concurrent and the strategy is common all results must be the same for a single element, so if 2 writes differ there is a write conflict.

> [!note]- Feedback
> **Reviewed: 2026-10-27.**
>
> **Assessment: partly correct; separate the conflict from the rule that handles it.** Your examples identify illegal exclusive writes and an illegal common-write case. However, two processors targeting one shared cell in the same write phase already constitute write contention, even if their values agree. A CRCW policy specifies how such simultaneous writes are handled.
>
> **Suggested exam answer:** A write conflict occurs when two or more processors attempt to write to the same shared-memory cell in the same write phase. Exclusive-write models prohibit this, even for equal values. CRCW permits it under its specified rule: common requires all values to agree, arbitrary lets one unspecified writer succeed, and priority selects the writer with highest priority. Writes to distinct cells do not conflict.
>
> **Study:** [[PRAM#Deciding legality from addresses]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].

> [!success]- Model answer
> **Suggested exam answer:** A write conflict occurs when two or more processors attempt to write to the same shared-memory cell in the same write phase. Exclusive-write models prohibit this, even for equal values. CRCW permits it under its specified rule: common requires all values to agree, arbitrary lets one unspecified writer succeed, and priority selects the writer with highest priority. Writes to distinct cells do not conflict.
>
> **Study:** [[PRAM#Deciding legality from addresses]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].

### AAPP-01-013

Explain why, in the PRAM model, the number of instructions executed is used as time complexity. (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=2|2023-11-09-1st · Exercise 1A · p. 2]]

^aapp-01-013

**My answer**

Because PRAM follows a strict cycle based behavior, where each instruction is constant time and all processors are synchronized. So the abstraction allows to consider a cycle or step as a constant time for all processor at the same time and the time is simplified as the total number of cycles. 

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: correct.** You identify both reasons: constant-time operations and synchronized execution. Your conclusion that time is the number of cycles is the essential point.
>
> **Suggested exam answer:** PRAM assumes unit-time basic instructions and permitted memory accesses, with processors executing synchronous steps. Therefore elapsed parallel time is proportional to the number of sequential steps/rounds until completion. Instructions executed simultaneously on different processors do not add to elapsed time; summing those operations measures work instead.
>
> **Wording to keep precise:** “Number of instructions” here means the length of the parallel execution in steps, rather than the total instruction count over all processors. For example, eight processors each performing one operation per step for five steps give time 5 and work 40 in that simplified counting model.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. See also [the IIT Delhi course reading, “PRAM Computation Time,” printed p. 74](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/kumar_chapter3.pdf#page=10).

> [!success]- Model answer
> **Suggested exam answer:** PRAM assumes unit-time basic instructions and permitted memory accesses, with processors executing synchronous steps. Therefore elapsed parallel time is proportional to the number of sequential steps/rounds until completion. Instructions executed simultaneously on different processors do not add to elapsed time; summing those operations measures work instead.
>
> **Wording to keep precise:** “Number of instructions” here means the length of the parallel execution in steps, rather than the total instruction count over all processors. For example, eight processors each performing one operation per step for five steps give time 5 and work 40 in that simplified counting model.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. See also [the IIT Delhi course reading, “PRAM Computation Time,” printed p. 74](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/kumar_chapter3.pdf#page=10).

### AAPP-01-014

Please discuss the following sentence: “In a PRAM model, processors do not have private local memories”. True/False? (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1A · p. 2]]

^aapp-01-014

**My answer**

This is false. There is a shared access memory, but each processor has also its own private registers used to load values from memory and record intermediate results.

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: correct.** Your explanation gives the reason the statement is false: shared memory coexists with private processor state.
>
> **Suggested exam answer:** False. Each PRAM processor has its own private registers/local storage, used for operands and intermediate results, as well as access to shared memory. Other processors cannot directly access its private registers; communication occurs through shared-memory reads and writes.
>
> **Example:** Two processors can both have a local register named `sum` without a conflict. A conflict depends on accessing the same shared cell.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=4|slide 4]].

> [!success]- Model answer
> **Suggested exam answer:** False. Each PRAM processor has its own private registers/local storage, used for operands and intermediate results, as well as access to shared memory. Other processors cannot directly access its private registers; communication occurs through shared-memory reads and writes.
>
> **Example:** Two processors can both have a local register named `sum` without a conflict. A conflict depends on accessing the same shared cell.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=4|slide 4]].

### AAPP-01-015

Please provide an example of a PRAM application relying on a Common CW policy. (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1C · p. 2]]

^aapp-01-015

**My answer**

For the common policy all resulting writes must report the same value. This is used for security application where the computation is repeated multiple time in parallel by different physical units and the result must be the same. This prevents an attacker from disturbing the behavior of a single unit. 

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: the common-write rule is correct, but the security example does not establish a valid application.** Common CW requires agreement; it does not compare results, perform majority voting, or guarantee protection against a malicious processor. If one processor proposes a different value to the same cell, that step violates the common-write rule.
>
> **Suggested exam answer — Boolean OR:** Given $n$ Boolean inputs, initialize a shared flag to 0 in a separate step. Assign one processor to each input. A processor whose input is 1 writes 1 to the flag; a processor whose input is 0 does nothing. All concurrent writes therefore agree, so common CRCW permits them. The final flag is 1 exactly when at least one input is 1. With $n$ processors this takes a constant number of rounds.
>
> ```text
> flag = 0                         // separate initialization
> in parallel for i = 0, ..., n-1:
>     if A[i] == 1:
>         flag = 1
> ```
>
> **Why the condition matters:** Letting zero-input processors write 0 in that same write phase would violate common CW when inputs contain both 0 and 1.
>
> **Study:** [[PRAM#A useful CRCW example: Boolean OR]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].

> [!success]- Model answer
> **Suggested exam answer — Boolean OR:** Given $n$ Boolean inputs, initialize a shared flag to 0 in a separate step. Assign one processor to each input. A processor whose input is 1 writes 1 to the flag; a processor whose input is 0 does nothing. All concurrent writes therefore agree, so common CRCW permits them. The final flag is 1 exactly when at least one input is 1. With $n$ processors this takes a constant number of rounds.
>
> ```text
> flag = 0                         // separate initialization
> in parallel for i = 0, ..., n-1:
>     if A[i] == 1:
>         flag = 1
> ```
>
> **Why the condition matters:** Letting zero-input processors write 0 in that same write phase would violate common CW when inputs contain both 0 and 1.
>
> **Study:** [[PRAM#A useful CRCW example: Boolean OR]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].

### AAPP-01-016

Are PRAM architectures using explicit or implicit synchronizations? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1A · p. 2]]

^aapp-01-016

**My answer**

It is implicit, but i am not sure what it means.

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: correct choice; the explanation was missing.**
>
> **Suggested exam answer:** Standard PRAM uses implicit synchronization. Processors advance through read, local-computation, and write phases in lock-step, and the next round starts only after the current round is complete. The model supplies this ordering automatically, so the algorithm does not need explicit barrier or lock calls to synchronize rounds, and no extra synchronization overhead is charged.
>
> **Meaning of “implicit”:** The synchronization is built into the execution rules. The barrier drawn on the lecture slide represents this guarantee; it does not mean that a programmer must implement a costly barrier. Processors may still be inactive, and the algorithm must obey data dependencies and memory-access rules.
>
> **Study:** [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [the IIT Delhi course reading on synchrony and PRAM time, printed p. 74](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/kumar_chapter3.pdf#page=10).

> [!success]- Model answer
> **Suggested exam answer:** Standard PRAM uses implicit synchronization. Processors advance through read, local-computation, and write phases in lock-step, and the next round starts only after the current round is complete. The model supplies this ordering automatically, so the algorithm does not need explicit barrier or lock calls to synchronize rounds, and no extra synchronization overhead is charged.
>
> **Meaning of “implicit”:** The synchronization is built into the execution rules. The barrier drawn on the lecture slide represents this guarantee; it does not mean that a programmer must implement a costly barrier. Processors may still be inactive, and the algorithm must obey data dependencies and memory-access rules.
>
> **Study:** [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=5|slide 5]]; [the IIT Delhi course reading on synchrony and PRAM time, printed p. 74](https://www.cse.iitd.ac.in/~rijurekha/col730_2022/kumar_chapter3.pdf#page=10).

### AAPP-01-017

Explain the factors that simplify the computation of space complexity in a PRAM application, giving them in order of priority. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1A · p. 2]]

^aapp-01-017

**My answer**

The shared access memory has unitary cells and the access is constant as well as infinite bandwidth.

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: mostly incorrect; you have described access time rather than storage usage.** Thinking in cells is relevant, but constant access time and unlimited bandwidth simplify time analysis. They do not determine how much memory an algorithm needs.
>
> **Suggested exam answer, ordered by relevance to space accounting:**
>
> 1. **Unit storage per value:** in the unbounded-integer, unit-cost variant, one cell holds one integer regardless of its bit length. Space is counted in cells, without expanding each integer into bits.
> 2. **Uniform, unbounded addressable memory:** count the shared cells actually used/accessed by the algorithm; the model supplies as many as needed, without hardware capacity or memory-layout bookkeeping costs. Unlimited available memory does not mean the algorithm's space usage is infinite.
>
> **Counting convention:** The shared-space convention counts shared cells. If total storage is requested, also include processor-local storage; for example, $m$ shared cells plus a fixed positive number of registers on each of $p$ processors uses $\Theta(m+p)$ total cells. State the convention rather than silently excluding private memory.
>
> **Limit of the available evidence:** [[lecture4-PRAM.pdf#page=4|Slide 4]] supports counting used cells, and [Tvrdik's lecture, “RAM model” and “PRAM model”](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html) explicitly states the unbounded-integer and shared-space conventions. Neither supplies an official ranking for this exam question. The ordering above is a reasoned explanation, not a verified marking scheme. Related note: [[PRAM#RAM and PRAM execution]].

> [!success]- Model answer
> **Suggested exam answer, ordered by relevance to space accounting:**
>
> 1. **Unit storage per value:** in the unbounded-integer, unit-cost variant, one cell holds one integer regardless of its bit length. Space is counted in cells, without expanding each integer into bits.
> 2. **Uniform, unbounded addressable memory:** count the shared cells actually used/accessed by the algorithm; the model supplies as many as needed, without hardware capacity or memory-layout bookkeeping costs. Unlimited available memory does not mean the algorithm's space usage is infinite.
>
> **Counting convention:** The shared-space convention counts shared cells. If total storage is requested, also include processor-local storage; for example, $m$ shared cells plus a fixed positive number of registers on each of $p$ processors uses $\Theta(m+p)$ total cells. State the convention rather than silently excluding private memory.
>
> **Limit of the available evidence:** [[lecture4-PRAM.pdf#page=4|Slide 4]] supports counting used cells, and [Tvrdik's lecture, “RAM model” and “PRAM model”](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html) explicitly states the unbounded-integer and shared-space conventions. Neither supplies an official ranking for this exam question. The ordering above is a reasoned explanation, not a verified marking scheme. Related note: [[PRAM#RAM and PRAM execution]].

### AAPP-01-018

Please describe an example of Common CRCW with a PRAM model. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1D · p. 2]]

^aapp-01-018

**My answer**

Same answer as before. Maybe give me a different example here.

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: referring back to the security example does not supply a valid example. Here is a different application, as requested.**
>
> **Suggested exam answer — test whether an array is sorted:** Initialize a shared flag `sorted` to 1 in a separate step. Assign processor $P_i$ to adjacent elements $A[i]$ and $A[i+1]$. If $A[i]>A[i+1]$, it writes 0 to the flag; otherwise it does nothing. All simultaneous writes propose 0, satisfying common CW. Concurrent reads of shared adjacent elements are allowed by the CR part of CRCW.
>
> ```text
> sorted = 1                       // separate initialization
> in parallel for i = 0, ..., n-2:
>     if A[i] > A[i+1]:
>         sorted = 0
> ```
>
> **Why it works:** A nondecreasing array has no adjacent inversion, so the flag stays 1. Otherwise at least one processor writes 0. For $[4,2,3,1]$, processors $P_0$ and $P_2$ both write 0 legally. Processors whose comparisons pass must not write 1 in the same phase. With $n-1$ processors, the test takes a constant number of rounds and $\Theta(n)$ work for $n\ge2$.
>
> **Study and attribution:** [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]]. This worked sortedness example applies the Boolean-AND construction in [John E. Savage, *Models of Computation*, §7.9.2, proof of Theorem 7.9.2](https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter7.pdf#page=34): initialize to 1 and let only failing conditions write 0.


> [!success]- Model answer
> **Suggested exam answer — test whether an array is sorted:** Initialize a shared flag `sorted` to 1 in a separate step. Assign processor $P_i$ to adjacent elements $A[i]$ and $A[i+1]$. If $A[i]>A[i+1]$, it writes 0 to the flag; otherwise it does nothing. All simultaneous writes propose 0, satisfying common CW. Concurrent reads of shared adjacent elements are allowed by the CR part of CRCW.
>
> ```text
> sorted = 1                       // separate initialization
> in parallel for i = 0, ..., n-2:
>     if A[i] > A[i+1]:
>         sorted = 0
> ```
>
> **Why it works:** A nondecreasing array has no adjacent inversion, so the flag stays 1. Otherwise at least one processor writes 0. For $[4,2,3,1]$, processors $P_0$ and $P_2$ both write 0 legally. Processors whose comparisons pass must not write 1 in the same phase. With $n-1$ processors, the test takes a constant number of rounds and $\Theta(n)$ work for $n\ge2$.
>
> **Study and attribution:** [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]]. This worked sortedness example applies the Boolean-AND construction in [John E. Savage, *Models of Computation*, §7.9.2, proof of Theorem 7.9.2](https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter7.pdf#page=34): initialize to 1 and let only failing conditions write 0.

### AAPP-01-019

Explain the factors that simplify the computation of time complexity in a PRAM application, giving them in order of priority. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1A · p. 2]]

^aapp-01-019

**My answer**

The processor instructions  are unitary time and the memory accesses are too with no limitation in bandwidth and latency. The model also follows a cycle based behavior with all processor synchronized, so that can be considered a fixed time step.

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: substantially correct; make the requested ordering explicit and refine the latency wording.** You identified the relevant assumptions. A memory access still takes a unit step; the idealization removes additional hardware latency and bandwidth costs.
>
> **Suggested exam answer:** A defensible order is:
>
> 1. **Unit-time basic instructions:** each permitted basic computation has constant cost.
> 2. **Unit-time shared-memory access:** every processor can access any cell in constant time, with no extra bandwidth/contention penalty for accesses allowed by the chosen model.
> 3. **Synchronous execution:** processors advance in lock-step, with implicit synchronization and no additional synchronization overhead.
>
> Together these assumptions let us count parallel steps to obtain $T_p(n)$. They do not imply evenly distributed work or remove algorithmic dependencies.
>
> **About the ranking:** The available slides state these assumptions but do not give an official priority order. The ordering above follows their role in fixing operation costs and then counting global steps.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. The parallel unit-time memory-access assumption is also described by [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=4).

> [!success]- Model answer
> **Suggested exam answer:** A defensible order is:
>
> 1. **Unit-time basic instructions:** each permitted basic computation has constant cost.
> 2. **Unit-time shared-memory access:** every processor can access any cell in constant time, with no extra bandwidth/contention penalty for accesses allowed by the chosen model.
> 3. **Synchronous execution:** processors advance in lock-step, with implicit synchronization and no additional synchronization overhead.
>
> Together these assumptions let us count parallel steps to obtain $T_p(n)$. They do not imply evenly distributed work or remove algorithmic dependencies.
>
> **About the ranking:** The available slides state these assumptions but do not give an official priority order. The ordering above follows their role in fixing operation costs and then counting global steps.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]]. The parallel unit-time memory-access assumption is also described by [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=4).

### AAPP-01-020

Please describe what happens in a PRAM model when the number of threads exceeds the number of processors. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1D · p. 2]]

^aapp-01-020

**My answer**

It can use chunking, so a first phase where more instructions are executed locally and then a more parallel phase. Otherwise there are virtual processor that can appear to the model like enough for the task, but the workload is divided among less processor so each does the work of more than 1 virtual processor.

> [!note]- Feedback
> **Reviewed: 2026-10-28.**
>
> **Assessment: mostly correct; your virtual-processor explanation is the general answer.** Chunking can help redesign particular algorithms, such as a reduction, but a local phase followed by a parallel phase is not required for every PRAM computation.
>
> **Suggested exam answer:** When there are more logical threads/virtual processors than physical processors, each physical processor simulates several virtual processors by time-sharing their work and retaining their separate local states. The simulation batches each original round while preserving read–compute–write ordering and the original memory-conflict policy. If $q$ virtual processors take $t$ rounds, then $p<q$ processors can simulate them in $O(t\lceil q/p\rceil)$ time with the same shared-memory assumptions. Fewer processors increase execution time; they do not create extra physical parallelism.
>
> **Example:** Ten virtual processors on three physical processors require four batches per primitive phase. Preserve the virtual reads before committing writes that could change what later batches read; completing an entire round for one batch before reading for the next can change the result.
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slides 25–26]].

> [!success]- Model answer
> **Suggested exam answer:** When there are more logical threads/virtual processors than physical processors, each physical processor simulates several virtual processors by time-sharing their work and retaining their separate local states. The simulation batches each original round while preserving read–compute–write ordering and the original memory-conflict policy. If $q$ virtual processors take $t$ rounds, then $p<q$ processors can simulate them in $O(t\lceil q/p\rceil)$ time with the same shared-memory assumptions. Fewer processors increase execution time; they do not create extra physical parallelism.
>
> **Example:** Ten virtual processors on three physical processors require four batches per primitive phase. Preserve the virtual reads before committing writes that could change what later batches read; completing an entire round for one batch before reading for the next can change the result.
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slides 25–26]].

### AAPP-01-021

“In a PRAM model, synchronization primitives are not required when data is exchanged through the shared memory.” True/False? Why? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1A · p. 2]]

^aapp-01-021

**My answer**

True, synchronization primitives are used mainly for read/write conflict. But in a PRAM model all processor are synchronized, so read and write phase never overlap. In order to exchange data, the data is written in memory and on the next cycle it is read.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct; refine the reason.** True is the intended answer. Your write-in-one-round/read-in-the-next explanation is correct. Synchronization primitives also enforce ordering and mutual exclusion in real programs; they are not mainly a remedy for mixed read/write conflicts. PRAM supplies the required phase ordering as part of the model. Same-phase read/read and write/write restrictions still apply.
>
> **Suggested exam answer:** True, for exchanging data between synchronous PRAM rounds. All processors execute read, compute, and write phases in lockstep, with an implicit global barrier before the next round. A value written in round $r$ can therefore be read in round $r+1$ without programming a lock, signal, or barrier. The algorithm must still obey its EREW/CREW/CRCW memory-access rules.
>
> **Study:** [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=5|slide 5]].

> [!success]- Model answer
> **Suggested exam answer:** True, for exchanging data between synchronous PRAM rounds. All processors execute read, compute, and write phases in lockstep, with an implicit global barrier before the next round. A value written in round $r$ can therefore be read in round $r+1$ without programming a lock, signal, or barrier. The algorithm must still obey its EREW/CREW/CRCW memory-access rules.
>
> **Study:** [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=5|slide 5]].

### AAPP-01-022

In a PRAM model, “all processors can access all memory cells in unit time. Could you please provide a detailed explanation of the implications of this assumption? (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1A · p. 2]]

^aapp-01-022

**My answer**

This phrase has mainly 2 implications. The first is that an arbitrary amout of processor can access memory through a private channel at the same time, while normally this would have bandwidth issues. The second  is that to have unit time there must be no latency, which is impossible in real systems. 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: partly correct; unit latency does not mean zero latency.** You correctly identify the idealization of bandwidth and simultaneous access. A permitted access costs one model step, independently of processor, address, or other permitted accesses. PRAM does not require a particular physical implementation such as a private channel per processor.
>
> **Suggested exam answer:** Every processor can read or write any shared-memory cell in constant, unit time. All $p$ processors can perform permitted accesses simultaneously, with no extra penalty for network distance, cache misses, bandwidth saturation, or contention between permitted accesses. This makes communication costs independent of the machine's physical layout. Same-cell accesses must still satisfy the selected EREW/CREW/CRCW rule. Each access takes one model step, rather than zero time.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=4|slide 4]]. See also [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=4).

> [!success]- Model answer
> **Suggested exam answer:** Every processor can read or write any shared-memory cell in constant, unit time. All $p$ processors can perform permitted accesses simultaneously, with no extra penalty for network distance, cache misses, bandwidth saturation, or contention between permitted accesses. This makes communication costs independent of the machine's physical layout. Same-cell accesses must still satisfy the selected EREW/CREW/CRCW rule. Each access takes one model step, rather than zero time.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=4|slide 4]]. See also [Blelloch and Maggs, §25.2.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=4).

### AAPP-01-023

What can be said about the time complexity of a PRAM-based application when the PRAM model has a bounded number of processors? (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1A · p. 2]]
Source: [[Tema Esame 2026-6-29-1st.pdf#page=2|2026-6-29-1st · Exercise 1A · p. 2]]

^aapp-01-023

**My answer**

I would say that a pram model can be scaled to any number of processors, so the algorithm should take advantage of that. But with a bounded amount there is a hard cap to possible performance and the normal algorithm might generalize too much for a fixed amount of processors.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: incomplete; state the time bound and distinguish a fixed constant from a parameter.** You recognize that fewer processors limit parallelism, but the question needs a complexity statement. A processor bound does not make an algorithm inappropriate; excess virtual processors can be simulated.
>
> **Suggested exam answer:** With $p$ available processors, at most $p$ basic operations execute per step, so an execution doing $W(n)$ operations needs at least $W(n)/p$ time; dependencies can impose a larger bound. If an algorithm uses $q>p$ virtual processors for $t(n)$ rounds, batching them gives a simulation in $O(t(n)\lceil q/p\rceil)$ time, preserving the shared memory and phase/access rules. If $p$ is a fixed constant independent of input size, parallelism can improve time only by a constant factor relative to an optimal sequential solution under the same instruction and memory assumptions. If $p=p(n)$ grows with $n$, retain it in the bound $T_p(n)$.
>
> **Example:** Chunked summation takes $O(n/p+\log p)$ time for $1\le p\le n$. For fixed $p$, its worst-case time is $\Theta(n)$, like sequential summation.
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why work and depth give two different lower bounds]]; [[lecture4-PRAM.pdf#page=25|slide 25]].

> [!success]- Model answer
> **Suggested exam answer:** With $p$ available processors, at most $p$ basic operations execute per step, so an execution doing $W(n)$ operations needs at least $W(n)/p$ time; dependencies can impose a larger bound. If an algorithm uses $q>p$ virtual processors for $t(n)$ rounds, batching them gives a simulation in $O(t(n)\lceil q/p\rceil)$ time, preserving the shared memory and phase/access rules. If $p$ is a fixed constant independent of input size, parallelism can improve time only by a constant factor relative to an optimal sequential solution under the same instruction and memory assumptions. If $p=p(n)$ grows with $n$, retain it in the bound $T_p(n)$.
>
> **Example:** Chunked summation takes $O(n/p+\log p)$ time for $1\le p\le n$. For fixed $p$, its worst-case time is $\Theta(n)$, like sequential summation.
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why work and depth give two different lower bounds]]; [[lecture4-PRAM.pdf#page=25|slide 25]].

### AAPP-01-024

How is the communication via shared memory performed in a PRAM model? (latency vs parallel accesses)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1B · p. 2]]

^aapp-01-024

**My answer**

All memory access in a PRAM model is parallel and unit time, which means that an arbitrary amount of processors can access the memory at the same time with no bandwidth limit and with no latency.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct about parallel access; replace “no latency” and describe the exchange.** Unit-time access means a fixed one-step latency. It also does not mean every processor can access arbitrarily many cells in one step, or that all same-cell accesses are legal.
>
> **Suggested exam answer:** Processors communicate indirectly through shared memory: one processor writes a value, and another reads it in a subsequent round. Each permitted read/write has unit latency, independent of processor or address. All processors can make their permitted accesses in parallel, without an additional bandwidth or network-contention penalty. Same-cell accesses remain subject to EREW/CREW/CRCW rules. A value written in the write phase cannot already be observed during that round's earlier read phase.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]].

> [!success]- Model answer
> **Suggested exam answer:** Processors communicate indirectly through shared memory: one processor writes a value, and another reads it in a subsequent round. Each permitted read/write has unit latency, independent of processor or address. All processors can make their permitted accesses in parallel, without an additional bandwidth or network-contention penalty. Same-cell accesses remain subject to EREW/CREW/CRCW rules. A value written in the write phase cannot already be observed during that round's earlier read phase.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#What a synchronous round actually guarantees]]; [[lecture4-PRAM.pdf#page=4|slides 4–5]].

### AAPP-01-025

How does the PRAM model abstract away synchronization and communication, and what are the implications for algorithm design? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1A · p. 2]]

^aapp-01-025

**My answer**

The PRAM model guarantees that all computes units follow a fixed phase cycle and are synchronized. For communication all processor have simultaneous unit time acces to the shared memory. The implications for algorithm design is that no read/write conflicts can happen and the memory is not affected by caching, bandwidth or latency issues. 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct; synchronization does not eliminate every memory conflict.** Your account of lockstep phases and ideal shared-memory access is sound. Separate read and write phases prevent overlap between those phases, but simultaneous readers or writers can still violate the model's access policy. Access latency is fixed at one model step, with realistic additional delays ignored.
>
> **Suggested exam answer:** PRAM assumes synchronous read–compute–write rounds with an implicit barrier, so the programmer does not implement synchronization between rounds. Communication uses globally addressable shared memory with unit-time permitted accesses in parallel. Cache behavior, network delays, bandwidth limits, and realistic synchronization overheads are abstracted away. Algorithm design can therefore focus on dependencies, parallel time, total work, and legal memory access. The algorithm must still satisfy EREW/CREW/CRCW rules, and a good PRAM bound must be reassessed when mapping it to real hardware.
>
> **Study:** [[PRAM#Overview]]; [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=3|slides 3–6]].

> [!success]- Model answer
> **Suggested exam answer:** PRAM assumes synchronous read–compute–write rounds with an implicit barrier, so the programmer does not implement synchronization between rounds. Communication uses globally addressable shared memory with unit-time permitted accesses in parallel. Cache behavior, network delays, bandwidth limits, and realistic synchronization overheads are abstracted away. Algorithm design can therefore focus on dependencies, parallel time, total work, and legal memory access. The algorithm must still satisfy EREW/CREW/CRCW rules, and a good PRAM bound must be reassessed when mapping it to real hardware.
>
> **Study:** [[PRAM#Overview]]; [[PRAM#Memory-access rules]]; [[lecture4-PRAM.pdf#page=3|slides 3–6]].

### AAPP-01-026

How do the different types of concurrent write (CW) models affect algorithm design in PRAM? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1B · p. 2]]
Source: [[Tema Esame 2026-6-29-1st.pdf#page=2|2026-6-29-1st · Exercise 1C · p. 2]]

^aapp-01-026

**My answer**

I could go on about what each model does but all i can say about the algorithm design is that random allows the individual computations to matter less. While common allows to have algorithms that only write if the result is a predetermined value, which must be the same for all units.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: partly correct; explain each rule's correctness obligation.** Your common-write idea is useful, but the agreed value need not be a fixed constant chosen in advance: all actual writers to a cell must agree in that phase. An arbitrary or random winner does not make individual computations less important. Every possible winning value must satisfy the required correctness condition; probability-based claims need a specified random rule and analysis.
>
> **Suggested exam answer:** The CW rule determines which algorithms and correctness proofs are valid. In **common CW**, all simultaneous writers to a cell must propose the same value. In **priority CW**, the highest-priority contender wins, allowing deterministic selection by processor priority. In **arbitrary CW**, any contender may win, so correctness must hold for every permitted winner. A **random CW** rule specifies a random winner and can support a probabilistic analysis. The same access pattern may be correct under one rule and incorrect under another.
>
> **Example:** To compute Boolean OR under common CRCW, first set a flag to 0, then let only processors with true inputs write 1. All writers agree. Letting false-input processors also write 0 would violate common CW, and an arbitrary winner could give the wrong OR.
>
> **Course terminology:** Slide 7 groups “Arbitrary/Random” together. Keep the unspecified-winner versus probabilistic-winner distinction explicit.
>
> **Study:** [[PRAM#CRCW write rules]]; [[PRAM#A useful CRCW example: Boolean OR]]; [[lecture4-PRAM.pdf#page=7|slide 7]]; [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

> [!success]- Model answer
> **Suggested exam answer:** The CW rule determines which algorithms and correctness proofs are valid. In **common CW**, all simultaneous writers to a cell must propose the same value. In **priority CW**, the highest-priority contender wins, allowing deterministic selection by processor priority. In **arbitrary CW**, any contender may win, so correctness must hold for every permitted winner. A **random CW** rule specifies a random winner and can support a probabilistic analysis. The same access pattern may be correct under one rule and incorrect under another.
>
> **Example:** To compute Boolean OR under common CRCW, first set a flag to 0, then let only processors with true inputs write 1. All writers agree. Letting false-input processors also write 0 would violate common CW, and an arbitrary winner could give the wrong OR.
>
> **Course terminology:** Slide 7 groups “Arbitrary/Random” together. Keep the unspecified-winner versus probabilistic-winner distinction explicit.
>
> **Study:** [[PRAM#CRCW write rules]]; [[PRAM#A useful CRCW example: Boolean OR]]; [[lecture4-PRAM.pdf#page=7|slide 7]]; [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

### AAPP-01-027

What does it imply that each memory cell can hold an integer of unbounded size in a PRAM? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1A · p. 2]]
Source: [[Tema Esame 2026-9-10-1st.pdf#page=2|2026-9-10-1st · Exercise 1A · p. 2]]

^aapp-01-027

**My answer**

It means that each individual cell has no limits of what value it can hold. Normally a memory element has a fixed size in bits, which determins what the bound for the representable value are, while in PRAM this bound don't exist. So if normally a bigger data would require multiple memory cells and a more complex logic to handle it, in PRAM this is simplified. 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct; add the consequence for the cost model.** You correctly distinguish an unbounded integer from a fixed-width machine word. Be explicit that the question assumes the unbounded-word variant; an unbounded number of cells is a separate assumption.
>
> **Suggested exam answer:** In the assumed variant, one cell stores an arbitrarily large integer without overflow or splitting it across words. Under the unit-cost instruction assumption, permitted primitive operations cost constant time independently of operand bit length, and space counts cells rather than bits. Real fixed-width machines may need several words and extra operations, so these bounds need not describe bit complexity. This word-size convention is model-dependent. See [Tvrdík, RAM model and constrained PRAM models](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).
>
> **Example:** $2^{1000}$ occupies one cell under this assumption, although its binary representation requires 1001 bits. This does not mean an arbitrarily long sequence of operations takes one step.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]. The slide says one word/integer per cell; the exam prompt supplies the explicit unbounded-integer assumption.

> [!success]- Model answer
> **Suggested exam answer:** In the assumed variant, one cell stores an arbitrarily large integer without overflow or splitting it across words. Under the unit-cost instruction assumption, permitted primitive operations cost constant time independently of operand bit length, and space counts cells rather than bits. Real fixed-width machines may need several words and extra operations, so these bounds need not describe bit complexity. This word-size convention is model-dependent. See [Tvrdík, RAM model and constrained PRAM models](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).
>
> **Example:** $2^{1000}$ occupies one cell under this assumption, although its binary representation requires 1001 bits. This does not mean an arbitrarily long sequence of operations takes one step.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]]. The slide says one word/integer per cell; the exam prompt supplies the explicit unbounded-integer assumption.

### AAPP-01-028

What kind of synchronization does PRAM use? (1)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1A · p. 2]]
Source: [[Tema Esame 2026-1-22-1st.pdf#page=2|2026-1-22-1st · Exercise 1A · p. 2]]

^aapp-01-028

**My answer**

PRAM uses a fixed cycle, phase based behavior for all processors. All processors are synchronized to be in the same phase at the same time and only advance to the next when all are done. The phases are: Read, Compute, Write, Barrier(implies synchronization). 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct.** You identified global phase synchronization and the four phases used in the course. Add that the barrier is implicit in the ideal model, rather than an explicit runtime primitive with a separately analyzed waiting cost.
>
> **Suggested exam answer:** PRAM uses synchronous, lockstep execution. Every round consists of read, local compute, write, and an implicit global barrier before the next round. No processor starts the next round until the current round is complete. Processors may be idle, and synchronization overhead is abstracted away. Textbooks that list only three read–compute–write phases include the same synchronization implicitly.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=5|slide 5]].

> [!success]- Model answer
> **Suggested exam answer:** PRAM uses synchronous, lockstep execution. Every round consists of read, local compute, write, and an implicit global barrier before the next round. No processor starts the next round until the current round is complete. Processors may be idle, and synchronization overhead is abstracted away. Textbooks that list only three read–compute–write phases include the same synchronization implicitly.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=5|slide 5]].

### AAPP-01-029

Which of the assumptions of the PRAM model simplifies the communication between the processor and the memory? (1)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1B · p. 2]]

^aapp-01-029

**My answer**

I already answered this multiple times. It is about the unit time simultaneous access from all processors.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct central idea; make the answer self-contained.** “Unit-time simultaneous access” identifies the relevant assumption. In an exam, state what it guarantees directly; a reference to previous answers does not provide the requested explanation.
>
> **Suggested exam answer:** The simplifying assumption is that every processor can access any shared-memory cell in unit time, and all processors can perform permitted accesses in parallel. The model therefore ignores extra costs from network distance, cache behavior, or limited aggregate memory bandwidth. Same-cell accesses still obey EREW/CREW/CRCW rules.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]].

> [!success]- Model answer
> **Suggested exam answer:** The simplifying assumption is that every processor can access any shared-memory cell in unit time, and all processors can perform permitted accesses in parallel. The model therefore ignores extra costs from network distance, cache behavior, or limited aggregate memory bandwidth. Same-cell accesses still obey EREW/CREW/CRCW rules.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slide 4]].

### AAPP-01-030

Complete the following sentence and explain what it means: “A write conflict occurs when… (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=2|2025-11-06-1st · Exercise 1A · p. 2]]

^aapp-01-030

**My answer**

The PRAM model is Write Exclusive and 2 different processors try to write to the same memory unit in the same cycle.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct for exclusive-write PRAM, but too restrictive as a general definition.** You correctly identify the same address and simultaneous writes. Competing writes can also occur on CRCW, where the write rule specifies how they are handled. Equal proposed values still violate exclusive write.
>
> **Suggested exam answer:** “A write conflict occurs when two or more processors attempt to write to the same shared-memory cell in the same write phase.” On EREW or CREW, this is illegal even when their proposed values coincide. On CRCW, the specified rule applies: common CW requires agreement, while priority or arbitrary CW selects a winning writer. Writes to different cells, or to the same cell in different rounds, do not create this simultaneous-write conflict.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].

> [!success]- Model answer
> **Suggested exam answer:** “A write conflict occurs when two or more processors attempt to write to the same shared-memory cell in the same write phase.” On EREW or CREW, this is illegal even when their proposed values coincide. On CRCW, the specified rule applies: common CW requires agreement, while priority or arbitrary CW selects a winning writer. Writes to different cells, or to the same cell in different rounds, do not create this simultaneous-write conflict.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=6|slides 6–7]].

### AAPP-01-031

If the PRAM model is a theoretical model, why does it matter in real problem analysis? (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=2|2026-1-22-1st · Exercise 1B · p. 2]]

^aapp-01-031

**My answer**

Because we can create and optimize one algorithm that takes advantage of it and then it can allow multiple real architectures to use the ideal version by tuning it specifically for it instead of creating it from scratch. Furthermore the ideal PRAM model makes the initial algorithm design easier.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct; connect portability to analysis of parallelism.** Your explanation of easier initial design and adapting an abstract algorithm to architectures is sound. Add what can actually be measured and what the model cannot predict by itself.
>
> **Suggested exam answer:** PRAM provides a simple, machine-independent framework for designing parallel algorithms and analyzing their parallel time, work, dependencies, and memory conflicts. It helps identify available parallelism and compare algorithms before hardware details obscure the analysis. It also provides an optimistic benchmark: real implementations must add communication, bandwidth, cache, and synchronization costs. A PRAM algorithm is therefore a useful starting point for implementation, while a fast PRAM bound alone does not guarantee good real performance.
>
> **Study:** [[PRAM#Overview]]; [[lecture4-PRAM.pdf#page=3|slide 3]]; [[lecture4-PRAM.pdf#page=24|slide 24]].

> [!success]- Model answer
> **Suggested exam answer:** PRAM provides a simple, machine-independent framework for designing parallel algorithms and analyzing their parallel time, work, dependencies, and memory conflicts. It helps identify available parallelism and compare algorithms before hardware details obscure the analysis. It also provides an optimistic benchmark: real implementations must add communication, bandwidth, cache, and synchronization costs. A PRAM algorithm is therefore a useful starting point for implementation, while a fast PRAM bound alone does not guarantee good real performance.
>
> **Study:** [[PRAM#Overview]]; [[lecture4-PRAM.pdf#page=3|slide 3]]; [[lecture4-PRAM.pdf#page=24|slide 24]].

### AAPP-01-032

A programmer claims: “If my algorithm runs on EREW, it will also run on CREW and CRCW without changes.” Is this always true? Explain. (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=2|2026-2-09-1st · Exercise 1B · p. 2]]

^aapp-01-032

**My answer**

No it is definitely not true. Since it has Both exclusive read and write, changing either to concurrent could create errors in the execution in the algorithm. It is possible that such algorithm exists but it is not a guarantee. 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: incorrect; the intended answer is True.** You have reversed the direction of the model hierarchy. A more permissive machine allows additional access patterns; it does not force the program to make additional simultaneous accesses.
>
> **Suggested exam answer:** Yes, assuming the same processors, instruction set, memory, and synchronous execution semantics. A valid EREW algorithm never has simultaneous readers or writers to one cell. Every access it makes is therefore also legal on CREW and on CRCW. Running the unchanged program preserves its access pattern and result; the CRCW write-resolution rule is never needed to choose between competing writers. Thus EREW algorithms run unchanged on these more permissive models.
>
> **Direction matters:** A CREW algorithm that has several processors read the same cell in one phase is not automatically legal on EREW. That reverse direction may require copying or extra rounds.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#Deciding legality from addresses]]; [[lecture4-PRAM.pdf#page=6|slide 6]]. The access restrictions are also defined by [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

> [!success]- Model answer
> **Suggested exam answer:** Yes, assuming the same processors, instruction set, memory, and synchronous execution semantics. A valid EREW algorithm never has simultaneous readers or writers to one cell. Every access it makes is therefore also legal on CREW and on CRCW. Running the unchanged program preserves its access pattern and result; the CRCW write-resolution rule is never needed to choose between competing writers. Thus EREW algorithms run unchanged on these more permissive models.
>
> **Direction matters:** A CREW algorithm that has several processors read the same cell in one phase is not automatically legal on EREW. That reverse direction may require copying or extra rounds.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#Deciding legality from addresses]]; [[lecture4-PRAM.pdf#page=6|slide 6]]. The access restrictions are also defined by [Karp and Ramachandran, §2.1](https://www.cs.cmu.edu/~guyb/paralg/papers/KarpRamachandran90.pdf#page=4).

### AAPP-01-033

Suppose you have a PRAM algorithm that heavily relies on random access to many distinct shared cells per step. Based on the lemma about the scaling of the performance of a PRAM with reduced memory footprint, would you expect it to degrade more (or less) than an algorithm that mostly reuses a small working set? Motivate the answer. (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=2|2026-2-09-1st · Exercise 1C · p. 2]]

^aapp-01-033

**My answer**

It would degrade more, because the lemma for memory limit says that the real memory takes on the work of multiple ideal memory cells, by a factor of p/p' by serializing access. The algorithm that uses a small working set mean that the factor p/p' is smaller and thus less memory operations are needed.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: plausible conclusion, but correct the ratio and qualify what the lemma proves.** The memory ratio is $m/m'$, with $m$ simulated shared cells and $m'$ available shared cells. $p/p'$ is the processor ratio. For fixed $m,m'$, the stated ratio is unchanged by access order; a small working set can help only if the simulation exploits it.
>
> **Suggested exam answer:** I would generally expect more degradation when accesses are spread over many simulated memory segments, because more serialized segment visits may be needed. A small working set that fits in the available shared memory may permit reuse and fewer visits. The slide's general simulation bound is $O(t\lceil m/m'\rceil)$ time, using $\max(p,m')$ processors. This is an upper bound, rather than an exact slowdown or a proof that one access pattern is always slower. The locality advantage is an inference about a simulation that exploits the working set. In the original ideal PRAM, random versus nearby addresses alone has no extra access cost.
>
> **Storage assumption:** Reducing shared memory does not remove the simulated state. A standard proof retains the virtual cells in processor-local memory and uses the smaller shared memory for transfers; it does not store arbitrary $m$ words in $m'$ words of total storage. See [Tvrdík, “Simulation of large PRAMs on small PRAMs,” second lemma and proof](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slides 25–26]].

> [!success]- Model answer
> **Suggested exam answer:** I would generally expect more degradation when accesses are spread over many simulated memory segments, because more serialized segment visits may be needed. A small working set that fits in the available shared memory may permit reuse and fewer visits. The slide's general simulation bound is $O(t\lceil m/m'\rceil)$ time, using $\max(p,m')$ processors. This is an upper bound, rather than an exact slowdown or a proof that one access pattern is always slower. The locality advantage is an inference about a simulation that exploits the working set. In the original ideal PRAM, random versus nearby addresses alone has no extra access cost.
>
> **Storage assumption:** Reducing shared memory does not remove the simulated state. A standard proof retains the virtual cells in processor-local memory and uses the smaller shared memory for transfers; it does not store arbitrary $m$ words in $m'$ words of total storage. See [Tvrdík, “Simulation of large PRAMs on small PRAMs,” second lemma and proof](https://pages.cs.wisc.edu/~tvrdik/2/html/Section2.html).
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slides 25–26]].

### AAPP-01-034

Describe the execution model of a PRAM computation. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=2|2026-6-11-1st · Exercise 1A · p. 2]]

^aapp-01-034

**My answer**

A RRAM i am assuming refers to everything and not only the compute phase. So it is divided in three phases: Read, Compute, Write. Every processor executes the same phase at the same time and they are repeated in a cycle. The computations are unitary time and the memory access is unbounded and unit time as well.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct; make synchronization and the amount of work per round explicit.** Your phase order and unit-cost idea are right. Three read–compute–write phases with implicit synchronization describe the same ordering as the course's four-phase presentation. Use “PRAM” rather than “RRAM.” Unbounded memory capacity does not allow one processor to access arbitrarily many cells in one step.
>
> **Suggested exam answer:** A PRAM consists of processors with private registers that communicate through globally addressable shared memory. They execute synchronous rounds: read a shared value into local state, perform a basic local computation, write a result, and synchronize before the next round. Each processor performs only a constant amount of primitive work per round and may be idle. Permitted memory accesses and basic operations have unit cost. Simultaneous accesses must obey the chosen EREW/CREW/CRCW policy.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–6]].

> [!success]- Model answer
> **Suggested exam answer:** A PRAM consists of processors with private registers that communicate through globally addressable shared memory. They execute synchronous rounds: read a shared value into local state, perform a basic local computation, write a result, and synchronize before the next round. Each processor performs only a constant amount of primitive work per round and may be idle. Permitted memory accesses and basic operations have unit cost. Simultaneous accesses must obey the chosen EREW/CREW/CRCW policy.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[lecture4-PRAM.pdf#page=4|slides 4–6]].

### AAPP-01-035

Discuss the possible conflicts that may arise during memory access in the PRAM model. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=2|2026-6-11-1st · Exercise 1B · p. 2]]

^aapp-01-035

**My answer**

The possible conflict that may arise during memory access have to do with the exclusive policy, either for read or for write. If 2 separate processor try to access the same memory resource using the same operation, read or write, during the same cycle and the model is exclusive that would generate a conflict.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct for exclusive access; add CRCW and the phase distinction.** You correctly identify same-cell access by multiple processors under an exclusive policy. The answer should also explain how concurrent writes are handled, including illegal disagreement under common CW. Two reads do not corrupt a value, but they still violate an exclusive-read rule.
>
> **Suggested exam answer:** Simultaneous accesses to the same shared cell can produce read/read or write/write conflicts. On EREW, both are forbidden. On CREW, concurrent reads are allowed but concurrent writes are forbidden. On CRCW, concurrent writes follow a specified rule: common requires identical proposed values, priority selects the highest-priority writer, and arbitrary selects an unspecified contender. Different values violate common CW. Read and write phases are separated, so they do not overlap within a round. Accesses to distinct cells remain legal in parallel.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=5|slides 5–7]].

> [!success]- Model answer
> **Suggested exam answer:** Simultaneous accesses to the same shared cell can produce read/read or write/write conflicts. On EREW, both are forbidden. On CREW, concurrent reads are allowed but concurrent writes are forbidden. On CRCW, concurrent writes follow a specified rule: common requires identical proposed values, priority selects the highest-priority writer, and arbitrary selects an unspecified contender. Different values violate common CW. Read and write phases are separated, so they do not overlap within a round. Accesses to distinct cells remain legal in parallel.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#CRCW write rules]]; [[lecture4-PRAM.pdf#page=5|slides 5–7]].

### AAPP-01-036

Explain how shared memory is modeled in PRAM and how this affects complexity analysis. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=2|2026-6-11-1st · Exercise 1C · p. 2]]

^aapp-01-036

**My answer**

As i said multiple times the memory has unit time unlimited simultaneous accesses. This makes it so that the memory phases are unit time and can be considered a fixed constant operation in complexity analysis. Add to that the fact that instruction for the processors are also considered unit time, a full cycle can be considered like a time unit.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct; complete the shared-memory description and qualify “unlimited simultaneous accesses.”** Your main complexity argument is right: a round contains a constant number of unit-cost phases. The model lets all available processors access memory in parallel, subject to the access policy, rather than letting one processor perform an unbounded number of accesses in a round.
>
> **Suggested exam answer:** Shared memory is a globally addressable array of cells through which processors communicate. In the ideal model its capacity is unbounded, and each permitted access costs one time unit independently of address or processor. All processors can make permitted accesses in parallel, subject to EREW/CREW/CRCW rules, without extra cache, network, bandwidth, or synchronization costs. Consequently, for a stated processor count $p$, parallel time $T_p(n)$ counts synchronous constant-time rounds. Operations performed concurrently do not add to elapsed time, although they do add to total work $W(n)$. Dependencies and repeated accesses across rounds still contribute to time.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Performance quantities]]; [[lecture4-PRAM.pdf#page=4|slides 4–6]].

> [!success]- Model answer
> **Suggested exam answer:** Shared memory is a globally addressable array of cells through which processors communicate. In the ideal model its capacity is unbounded, and each permitted access costs one time unit independently of address or processor. All processors can make permitted accesses in parallel, subject to EREW/CREW/CRCW rules, without extra cache, network, bandwidth, or synchronization costs. Consequently, for a stated processor count $p$, parallel time $T_p(n)$ counts synchronous constant-time rounds. Operations performed concurrently do not add to elapsed time, although they do add to total work $W(n)$. Dependencies and repeated accesses across rounds still contribute to time.
>
> **Study:** [[PRAM#RAM and PRAM execution]]; [[PRAM#Performance quantities]]; [[lecture4-PRAM.pdf#page=4|slides 4–6]].

## Parallel performance and scaling

Related notes: [[PRAM]].

### AAPP-02-001

Define the speedup when a sequential code is accelerated with p processors. (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=2|2022-11-08-1st · Exercise 1B · p. 2]]

^aapp-02-001

**My answer**

This is speedup is described by ahmdal's law. Which is $S = \frac{1}{(1-f)+\frac t p}$ where p is the number of processors and t is the fraction of operations that can be parallelized. So the speed up is 1 divided by a non changable fraction plus a fraction, the sum is less then 1 if at least some part can be parallelized and so the speedup is higher than 1. The higher the parallel fraction or the number of processor is the higher the speedup.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: partly correct, but you give a prediction law instead of the general definition.** You recognize how parallelizable work and processor count affect ideal speedup. However, your formula mixes an undefined $f$ with $t$. Use one symbol consistently, and define the fraction in terms of sequential execution time. Amdahl's law applies under additional assumptions; it is not the definition of speedup.
>
> **Suggested exam answer:** Speedup is the ratio of the sequential execution time to the parallel execution time for the same problem and input: $S_p(n)=T_{\mathrm{seq}}(n)/T_p(n)$. With the course's best sequential baseline, write $S_p(n)=T^*(n)/T_p(n)$. A speedup of 4 means the parallel run takes one quarter of the sequential time.
>
> **Your Amdahl formula, corrected:** If $f$ is the parallelizable fraction of the fixed-size sequential runtime, then ideal speedup is $S_p=1/((1-f)+f/p)$. This assumes ideal division of that parallel part and no additional overhead. It gives $S_p>1$ when $f>0$ and $p>1$; $p=1$ or $f=0$ gives 1. Measured speedup can be below 1 if a parallel implementation is slower.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=11|slide 11]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Speedup is the ratio of the sequential execution time to the parallel execution time for the same problem and input: $S_p(n)=T_{\mathrm{seq}}(n)/T_p(n)$. With the course's best sequential baseline, write $S_p(n)=T^*(n)/T_p(n)$. A speedup of 4 means the parallel run takes one quarter of the sequential time.
>
> **Your Amdahl formula, corrected:** If $f$ is the parallelizable fraction of the fixed-size sequential runtime, then ideal speedup is $S_p=1/((1-f)+f/p)$. This assumes ideal division of that parallel part and no additional overhead. It gives $S_p>1$ when $f>0$ and $p>1$; $p=1$ or $f=0$ gives 1. Measured speedup can be below 1 if a parallel implementation is slower.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=11|slide 11]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-002

Please describe the differences between the Amdahl and the Gustafson laws. (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=2|2022-11-08-1st · Exercise 1C · p. 2]]

^aapp-02-002

**My answer**

The main difference is that amdahl law calculates the speedup on a task that is initally sequential and it can be parallelized in part, that speedup can be read as a percentage. Gustafson law, instead calculates the speedup as the time it would take for an already parallelized program to be run sequentially, so the higher the more time it is saved. They can be compared with strong and weak scaling respectively. Strong scaling has the workload remain the same while the time dimishes, weak scaling instead increases the workload while keep the time the same.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct intuition; specify what remains fixed and how the fractions are measured.** You correctly connect Amdahl to strong scaling and Gustafson to scaled workloads. Both laws compare a sequential time with a parallel time; the distinction is not whether the program was initially sequential or already parallelized. Speedup is a dimensionless factor, usually expressed as “times faster,” rather than a percentage.
>
> **Suggested exam answer:** Amdahl considers a **fixed-size problem**. If $s_A$ is the serial fraction of its sequential runtime, ideal speedup on $p$ processors is $S_A(p)=1/(s_A+(1-s_A)/p)$, with a ceiling of $1/s_A$ when $s_A>0$. Gustafson considers a **scaled problem at fixed parallel runtime**. If $s_G$ is the serial fraction of that parallel run, its scaled speedup is $S_G(p)=s_G+(1-s_G)p$. Its sequential comparison executes that same scaled workload. The two serial fractions use different runtime baselines. Both ideal formulas omit additional parallel overhead.
>
> **Scaling qualification:** Strong scaling fixes total problem size. Weak scaling fixes work per processor while total work grows with $p$; approximately constant runtime is the desired outcome, rather than a guarantee. Gustafson's fixed-time viewpoint explains the benefit of growing the parallel workload.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Amdahl considers a **fixed-size problem**. If $s_A$ is the serial fraction of its sequential runtime, ideal speedup on $p$ processors is $S_A(p)=1/(s_A+(1-s_A)/p)$, with a ceiling of $1/s_A$ when $s_A>0$. Gustafson considers a **scaled problem at fixed parallel runtime**. If $s_G$ is the serial fraction of that parallel run, its scaled speedup is $S_G(p)=s_G+(1-s_G)p$. Its sequential comparison executes that same scaled workload. The two serial fractions use different runtime baselines. Both ideal formulas omit additional parallel overhead.
>
> **Scaling qualification:** Strong scaling fixes total problem size. Weak scaling fixes work per processor while total work grows with $p$; approximately constant runtime is the desired outcome, rather than a guarantee. Gustafson's fixed-time viewpoint explains the benefit of growing the parallel workload.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-003

Gustafson says that the Amdahl law is wrong. True/False? Why? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1D · p. 2]]

^aapp-02-003

**My answer**

False, each law right in its own way, amdahl is based on a fraction while gustafson on a multiplication of the parallel work by p cores.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct True/False choice, but the explanation is insufficient.** False is the intended answer. Saying that one formula uses a fraction and the other a multiplication describes their algebra, not why they are compatible. Both formulas contain a serial fraction and processor count.
>
> **Suggested exam answer:** False. Gustafson challenges applying a fixed-problem-size assumption to workloads that grow with the available processors; he does not invalidate Amdahl's calculation under its assumptions. Amdahl holds problem size fixed, whereas Gustafson considers scaling the parallel workload within a fixed runtime. Their serial fractions are measured relative to the sequential and parallel runtimes respectively. For the same execution, using the corresponding fractions gives the same speedup. See [Gustafson, *Reevaluating Amdahl's Law*, fixed-size and scaled-size models](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).
>
> **Example:** A sequential run takes 100 seconds: 20 serial and 80 parallelizable. With four ideal processors it takes $20+80/4=40$ seconds, so speedup is $2.5$. Amdahl uses $s_A=20/100=0.2$ and gives $1/(0.2+0.8/4)=2.5$. Gustafson uses $s_G=20/40=0.5$ and gives $0.5+0.5\cdot4=2.5$. Substituting the same numerical fraction into both formulas would describe different assumptions.
>
> **Study:** [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** False. Gustafson challenges applying a fixed-problem-size assumption to workloads that grow with the available processors; he does not invalidate Amdahl's calculation under its assumptions. Amdahl holds problem size fixed, whereas Gustafson considers scaling the parallel workload within a fixed runtime. Their serial fractions are measured relative to the sequential and parallel runtimes respectively. For the same execution, using the corresponding fractions gives the same speedup. See [Gustafson, *Reevaluating Amdahl's Law*, fixed-size and scaled-size models](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).
>
> **Example:** A sequential run takes 100 seconds: 20 serial and 80 parallelizable. With four ideal processors it takes $20+80/4=40$ seconds, so speedup is $2.5$. Amdahl uses $s_A=20/100=0.2$ and gives $1/(0.2+0.8/4)=2.5$. Gustafson uses $s_G=20/40=0.5$ and gives $0.5+0.5\cdot4=2.5$. Substituting the same numerical fraction into both formulas would describe different assumptions.
>
> **Study:** [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-004

Please define the speed-up of a parallel algorithm according to the PRAM model (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1C · p. 2]]

^aapp-02-004

**My answer**

The speedup using p processors is $S_{p}=\frac{T^*}{T_{p}}$ where T* is the time taken using the best comparable senquential algorithm, while the Tp is the time taken in PRAM using p processors in parallel.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct.** You give the course's formula and correctly identify the best sequential baseline. State that both times refer to the same problem and input size. $T^*$ need not equal $T_1$, the time of the parallel algorithm run on one processor.
>
> **Suggested exam answer:** The speedup of a PRAM algorithm on $p$ processors is $S_p(n)=T^*(n)/T_p(n)$, where $T^*(n)$ is the execution time of the best sequential algorithm used as the baseline and $T_p(n)$ is the parallel execution time on $p$ processors for the same problem and input. It measures the factor by which parallel execution reduces runtime.
>
> **Study:** [[PRAM#Performance quantities]]; [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=11|slide 11]].

> [!success]- Model answer
> **Suggested exam answer:** The speedup of a PRAM algorithm on $p$ processors is $S_p(n)=T^*(n)/T_p(n)$, where $T^*(n)$ is the execution time of the best sequential algorithm used as the baseline and $T_p(n)$ is the parallel execution time on $p$ processors for the same problem and input. It measures the factor by which parallel execution reduces runtime.
>
> **Study:** [[PRAM#Performance quantities]]; [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=11|slide 11]].

### AAPP-02-005

Please describe how Gustafson defines the speed-up. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1D · p. 2]]

^aapp-02-005

**My answer**

I already answered this pretty much. 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: no self-contained answer supplied.** Your earlier explanation contains the main idea, but “I already answered this” does not supply the requested definition. Write the formula and specify what its serial fraction measures.
>
> **Suggested exam answer:** Gustafson defines scaled speedup by comparing the runtime of a scaled problem on $p$ processors with the time a sequential processor would need for that same scaled problem. Normalize the parallel runtime to 1, and let $s_G$ be its serial fraction. The serial part still takes $s_G$ sequentially, while the parallel part would take $p(1-s_G)$. Therefore $S_G(p)=s_G+p(1-s_G)=p-(p-1)s_G$. The model scales the parallel workload to use additional processors while keeping parallel runtime fixed. This is the [scaled-size construction in Gustafson's original paper](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).
>
> **Example:** If a four-processor run takes 10 seconds, with 2 serial seconds and 8 parallel seconds, the corresponding sequential time is $2+4\cdot8=34$ seconds. Thus $s_G=0.2$ and $S_G=34/10=0.2+4\cdot0.8=3.4$.
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Gustafson defines scaled speedup by comparing the runtime of a scaled problem on $p$ processors with the time a sequential processor would need for that same scaled problem. Normalize the parallel runtime to 1, and let $s_G$ be its serial fraction. The serial part still takes $s_G$ sequentially, while the parallel part would take $p(1-s_G)$. Therefore $S_G(p)=s_G+p(1-s_G)=p-(p-1)s_G$. The model scales the parallel workload to use additional processors while keeping parallel runtime fixed. This is the [scaled-size construction in Gustafson's original paper](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).
>
> **Example:** If a four-processor run takes 10 seconds, with 2 serial seconds and 8 parallel seconds, the corresponding sequential time is $2+4\cdot8=34$ seconds. Thus $s_G=0.2$ and $S_G=34/10=0.2+4\cdot0.8=3.4$.
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-006

Please define the efficiency of a parallel algorithm according to the PRAM model (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1C · p. 2]]

^aapp-02-006

**My answer**

Efficiency of PRAM means how well the algorithm uses multiple p processors. It is $E_{p}=\frac{T_{1}}{pT_{p}}$ so it is comparing running the PRAM algorithm on one processor to the total use of the algorithm using p processors. So if it is inefficient there is a lot of idling so the fraction is well below 1. 

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: correct; refine the interpretation of inefficiency.** Your formula and distinction between one-processor runtime and allocated processor-time are correct. Idling is an important cause of low efficiency, but additional communication, scheduling, or synchronization overhead can also reduce efficiency on real systems. $pT_p$ measures allocated processor-time, including idle capacity, rather than only the operations actually performed.
>
> **Suggested exam answer:** According to the course convention, efficiency is $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1(n)$ is the time of the same parallel algorithm on one processor and $T_p(n)$ is its time on $p$ processors. It compares the one-processor runtime with the total allocated processor-time. Under ideal linear scaling, $T_p=T_1/p$ and $E_p=1$; a lower value indicates less effective use of the allocated processors relative to this baseline.
>
> **Baseline caution:** The course defines speedup using $T^*$, so $E_p=S_p/p$ only when $T_1=T^*$. In general, $E_p=(T_1/T^*)\,S_p/p$. Keep this distinction, which you already handled correctly in question 004.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** According to the course convention, efficiency is $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1(n)$ is the time of the same parallel algorithm on one processor and $T_p(n)$ is its time on $p$ processors. It compares the one-processor runtime with the total allocated processor-time. Under ideal linear scaling, $T_p=T_1/p$ and $E_p=1$; a lower value indicates less effective use of the allocated processors relative to this baseline.
>
> **Baseline caution:** The course defines speedup using $T^*$, so $E_p=S_p/p$ only when $T_1=T^*$. In general, $E_p=(T_1/T^*)\,S_p/p$. Keep this distinction, which you already handled correctly in question 004.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-007

Please compare the assumptions behind the Gustafson and the Amdahl laws. (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1D · p. 2]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1D · p. 2]]

^aapp-02-007

**My answer**

Amdahl assumes there is a task and a portion of this taks can be parallelized and another called s not. So using p processors the total task becomes s+(1-s)/p so the parallel part is split among the p processor. For the Gustafson law the task is already run in parallel, at least a fraction and we try to find how long it would take sequentially by multipling the parallel part by the number of processors, s+(1-s)p.

> [!note]- Feedback
> **Reviewed: 2026-10-30.**
>
> **Assessment: mostly correct; add the fixed-size/fixed-time assumptions and distinguish the fractions.** Your two runtime constructions are right. In Amdahl's model, $s+(1-s)/p$ is the normalized **parallel runtime**; speedup is its reciprocal. In Gustafson's model, $s+(1-s)p$ is the normalized **sequential runtime** of the scaled problem, and also its speedup because parallel runtime is normalized to 1. The two occurrences of $s$ therefore have different denominators.
>
> **Suggested exam answer:** Amdahl assumes a fixed problem size with an unchanged serial component. Normalize its sequential runtime to 1; if the serial fraction is $s_A$, then ideal parallel runtime is $s_A+(1-s_A)/p$ and speedup is its reciprocal. Gustafson assumes that the parallel workload grows with processor count while parallel runtime remains fixed and the serial component does not grow in the ideal model. Normalize that parallel runtime to 1; with serial fraction $s_G$, the same scaled work would take $s_G+p(1-s_G)$ sequentially. Both models assume ideal distribution of the parallel part over comparable processors and omit additional parallel overhead. Their different workload assumptions explain why they do not contradict each other.
>
> **Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Amdahl assumes a fixed problem size with an unchanged serial component. Normalize its sequential runtime to 1; if the serial fraction is $s_A$, then ideal parallel runtime is $s_A+(1-s_A)/p$ and speedup is its reciprocal. Gustafson assumes that the parallel workload grows with processor count while parallel runtime remains fixed and the serial component does not grow in the ideal model. Normalize that parallel runtime to 1; with serial fraction $s_G$, the same scaled work would take $s_G+p(1-s_G)$ sequentially. Both models assume ideal distribution of the parallel part over comparable processors and omit additional parallel overhead. Their different workload assumptions explain why they do not contradict each other.
>
> **Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-008

Define the “work” in a PRAM model. (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1D · p. 2]]

^aapp-02-008

**My answer**

Work i a pram model is the number of operation executed across all processors. So every addition for example counts as 1, while the processor idling is not counted.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct.** You correctly count executed operations across all processors and exclude idle slots. Count all basic operations required by the algorithm, including extra bookkeeping, rather than only useful arithmetic.
>
> **Suggested exam answer:** Work $W(n)$ is the total number of basic operations actually executed by all processors during a PRAM computation. If $a_r$ operations execute in round $r$, then $W=\sum_r a_r$. Simultaneous operations count separately; idle processors contribute no operations. Allocated cost is instead $C_p=pT_p$, so $W\le C_p$ under the unit-operation convention.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]].

> [!success]- Model answer
> **Suggested exam answer:** Work $W(n)$ is the total number of basic operations actually executed by all processors during a PRAM computation. If $a_r$ operations execute in round $r$, then $W=\sum_r a_r$. Simultaneous operations count separately; idle processors contribute no operations. Allocated cost is instead $C_p=pT_p$, so $W\le C_p$ under the unit-operation convention.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]].

### AAPP-02-009

Define the “cost” in a PRAM model. (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1D · p. 2]]

^aapp-02-009

**My answer**

Cost in PRAM is the total CPU time used. So i counts the time for the total execution times the number of processors pT_p. This is also counting unused processors in certain round, even if they are idle they are still considered a cost.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct; use “allocated processor-time” for precision.** Your formula and inclusion of idle processors are right. Cost does not count every processor physically present in a machine: it counts the $p$ processors allocated to this computation for its duration.
>
> **Suggested exam answer:** PRAM cost is $C_p(n)=pT_p(n)$, the number of allocated processors multiplied by the parallel execution time. It includes idle processor-time within that allocation. Work counts actual operations and can be smaller. For example, four processors reserved for three rounds cost 12 processor-rounds even if only seven operations execute.
>
> **Study:** [[PRAM#Work versus cost]]; [[PRAM#Reading a processor-time diagram]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** PRAM cost is $C_p(n)=pT_p(n)$, the number of allocated processors multiplied by the parallel execution time. It includes idle processor-time within that allocation. Work counts actual operations and can be smaller. For example, four processors reserved for three rounds cost 12 processor-rounds even if only seven operations execute.
>
> **Study:** [[PRAM#Work versus cost]]; [[PRAM#Reading a processor-time diagram]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-010

Define the cost C when a sequential code is accelerated with p processors. (1)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=2|2023-11-09-1st · Exercise 1B · p. 2]]

^aapp-02-010

**My answer**

Look at the answer above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct by reference to 009; supply the formula directly in an exam.** Your preceding definition applies here. The sequential baseline is needed to assess cost optimality, rather than to define cost itself.
>
> **Suggested exam answer:** If execution on $p$ processors takes $T_p(n)$ time, its cost is $C_p(n)=pT_p(n)$. This is allocated processor-time, including idle time. Relative to the best sequential baseline $T^*(n)$, the implementation is cost-optimal when $C_p(n)=\Theta(T^*(n))$.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** If execution on $p$ processors takes $T_p(n)$ time, its cost is $C_p(n)=pT_p(n)$. This is allocated processor-time, including idle time. Relative to the best sequential baseline $T^*(n)$, the implementation is cost-optimal when $C_p(n)=\Theta(T^*(n))$.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-011

What is it meant with a fixed time model? Is it referring to Gustafson or Amdahl’s law? (1)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=2|2023-11-09-1st · Exercise 1C · p. 2]]

^aapp-02-011

**My answer**

Fixed time model is referring to gustafson law. The time for a parallel execution is fixed to one and it is compared to the same program but run sequentially. Eventually the law can increase the workload but the time remains fixed.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; distinguish the fixed budget from normalization.** You correctly identify Gustafson and the sequential comparison. The runtime is kept at a chosen budget, such as 10 seconds; writing it as 1 simply chooses normalized units. Growing the parallel workload as processors increase is the defining experiment.
>
> **Suggested exam answer:** A fixed-time model keeps the parallel runtime approximately constant while increasing the amount of work with the number of processors. This is Gustafson's viewpoint. If $s_G$ is the serial fraction of the parallel runtime, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. It compares the time of the same scaled workload on one processor with its time on $p$ processors, assuming ideal parallel execution and unchanged serial work.
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** A fixed-time model keeps the parallel runtime approximately constant while increasing the amount of work with the number of processors. This is Gustafson's viewpoint. If $s_G$ is the serial fraction of the parallel runtime, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. It compares the time of the same scaled workload on one processor with its time on $p$ processors, assuming ideal parallel execution and unchanged serial work.
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-012

Please define what is meant by “Efficiency” in a PRAM application. (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1B · p. 2]]

^aapp-02-012

**My answer**

Efficiency in PRAM is how well the algorithm utilizes all processors in parallel. To compute it we compare the time it would take to execute the program on one processor to the total CPU time used on p processors $E=\frac{T_{1}}{pT_{p}}$. If all parallel cores are used perfectly with no wasted idling the efficiency is one, otherwise it is lower. The higher the better.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct formula and main interpretation; qualify the “no idling” explanation.** Efficiency compares runtimes and allocated cost. On real systems, overhead can lower efficiency even when processors are active. Keeping processors busy with duplicated or unnecessary work also does not establish efficiency relative to the best sequential algorithm.
>
> **Suggested exam answer:** The course defines $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1$ is the runtime of the parallel algorithm on one processor and $T_p$ its runtime on $p$ processors. Ideal linear scaling gives $T_p=T_1/p$ and $E_p=1$. Lower efficiency indicates that the allocated processor-time exceeds the one-processor baseline, for example through idle capacity or additional overhead. $T_1$ need not equal the best sequential time $T^*$.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** The course defines $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1$ is the runtime of the parallel algorithm on one processor and $T_p$ its runtime on $p$ processors. Ideal linear scaling gives $T_p=T_1/p$ and $E_p=1$. Lower efficiency indicates that the allocated processor-time exceeds the one-processor baseline, for example through idle capacity or additional overhead. $T_1$ need not equal the best sequential time $T^*$.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-013

Please relate the strong scaling vs the weak scaling to the Amdahl vs Gustafson laws. (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1D · p. 2]]

^aapp-02-013

**My answer**

Ok the stong scaling is related to the amdahl law because it is the principle of having a fixed workload and we want to test how much faster it can complete by adding compute, the speedup of amdahl law tells us exacltly that. For the weak scaling instead, the workload can vary but the compute time is fixed. We want to test how much work can be completed in the same time. Gustafson law fixes the parallel execution for for any workload to 1 and compares it with the sequential time.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; define weak scaling through fixed work per processor.** Your association of strong scaling with Amdahl and scaled workloads with Gustafson is right. In a weak-scaling measurement, constant runtime is the desired result; the experiment fixes work per processor and measures whether runtime stays constant. Normalizing time to 1 does not make arbitrary workloads finish in the same time.
>
> **Suggested exam answer:** Strong scaling fixes total workload and increases processor count to reduce runtime; Amdahl models this with $S_A(p)=1/(s_A+(1-s_A)/p)$ for serial fraction $s_A$ of sequential runtime. Weak scaling increases total workload in proportion to processor count, keeping work per processor fixed; good weak scaling keeps runtime approximately constant. Gustafson's fixed-time model explains the benefit of growing the parallel workload, with $S_G(p)=s_G+p(1-s_G)$, where $s_G$ is measured in the parallel run. Both ideal laws omit additional overhead.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Strong scaling fixes total workload and increases processor count to reduce runtime; Amdahl models this with $S_A(p)=1/(s_A+(1-s_A)/p)$ for serial fraction $s_A$ of sequential runtime. Weak scaling increases total workload in proportion to processor count, keeping work per processor fixed; good weak scaling keeps runtime approximately constant. Gustafson's fixed-time model explains the benefit of growing the parallel workload, with $S_G(p)=s_G+p(1-s_G)$, where $s_G$ is measured in the parallel run. Both ideal laws omit additional overhead.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-014

Please define what is meant by “Speed up” in a PRAM application. (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1B · p. 2]]

^aapp-02-014

**My answer**

In a PRAM application Speedup means how much faster a problem can be solved by exploiting parallel execution, compared to a normal sequential execution. The formula is     $S_{p}=\frac{T^*}{T_{p}}$ , where T* is the time for the best sequential alogrithm and Tp is the time taken why the parallel algorithm using a PRAM model with p processors.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct.** Your formula and definitions match the course. State explicitly that both runtimes solve the same problem on the same input.
>
> **Suggested exam answer:** Speedup on $p$ processors is $S_p(n)=T^*(n)/T_p(n)$, where $T^*$ is the best sequential runtime used as the baseline and $T_p$ is the PRAM runtime on $p$ processors for the same problem and input. A speedup of 4 means parallel execution takes one quarter of the sequential time. The best sequential baseline $T^*$ can differ from $T_1$ for the parallel algorithm.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=11|slide 11]].

> [!success]- Model answer
> **Suggested exam answer:** Speedup on $p$ processors is $S_p(n)=T^*(n)/T_p(n)$, where $T^*$ is the best sequential runtime used as the baseline and $T_p$ is the PRAM runtime on $p$ processors for the same problem and input. A speedup of 4 means parallel execution takes one quarter of the sequential time. The best sequential baseline $T^*$ can differ from $T_1$ for the parallel algorithm.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=11|slide 11]].

### AAPP-02-015

Is the Amdahl law a fixed-time model? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1D · p. 2]]

^aapp-02-015

**My answer**

No amdahl law is not fixed time. What is fixed is the workload and it tries to find how much faster that same workload can be executed by exploiting parallel computation.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct.** You identify the fixed workload and the changing runtime. Add the ideal formula if space permits.
>
> **Suggested exam answer:** No. Amdahl uses a fixed-size problem: its workload remains the same as processors are added. If $s_A$ is the serial fraction of the sequential runtime, ideal speedup is $S_A(p)=1/(s_A+(1-s_A)/p)$. When $s_A>0$, speedup approaches $1/s_A$ as $p$ grows. Gustafson is associated with a fixed-time, scaled-workload model.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** No. Amdahl uses a fixed-size problem: its workload remains the same as processors are added. If $s_A$ is the serial fraction of the sequential runtime, ideal speedup is $S_A(p)=1/(s_A+(1-s_A)/p)$. When $s_A>0$, speedup approaches $1/s_A$ as $p$ grows. Gustafson is associated with a fixed-time, scaled-workload model.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-016

Please define what is meant by “Work” in a PRAM application. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1B · p. 2]]
Source: [[Tema Esame 2026-6-29-1st.pdf#page=2|2026-6-29-1st · Exercise 1B · p. 2]]

^aapp-02-016

**My answer**

Already answered this question above.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 008; that definition is correct.** Write a self-contained definition when answering an individual exam question.
>
> **Suggested exam answer:** Work $W(n)$ is the total number of basic operations actually executed across all processors. Equivalently, sum the number of executed operations over all rounds. Concurrent operations count separately and idle processor slots do not count. For a reduction of eight inputs, counting additions only, $W=4+2+1=7$ even though the parallel execution has three addition rounds.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]].

> [!success]- Model answer
> **Suggested exam answer:** Work $W(n)$ is the total number of basic operations actually executed across all processors. Equivalently, sum the number of executed operations over all rounds. Concurrent operations count separately and idle processor slots do not count. For a reduction of eight inputs, counting additions only, $W=4+2+1=7$ even though the parallel execution has three addition rounds.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]].

### AAPP-02-017

Please define what “Cost” means in a PRAM application. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1B · p. 2]]

^aapp-02-017

**My answer**

Already answered this question above.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 009; that definition is correct.** Include the formula and the treatment of idle processors directly in an exam answer.
>
> **Suggested exam answer:** Cost is $C_p(n)=pT_p(n)$, the total processor-time allocated to the PRAM application. All $p$ allocated processors count for the full runtime, including rounds in which some are idle. Thus cost can exceed work, which counts only executed operations. For four processors over three rounds, cost is 12 processor-rounds.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** Cost is $C_p(n)=pT_p(n)$, the total processor-time allocated to the PRAM application. All $p$ allocated processors count for the full runtime, including rounds in which some are idle. Thus cost can exceed work, which counts only executed operations. For four processors over three rounds, cost is 12 processor-rounds.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-018

In a PRAM, 𝑝𝐸𝑝(𝑛) is equal to the application speed-up? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=2|2024-09-05-1st · Exercise 1A · p. 2]]

^aapp-02-018

**My answer**

No $pE_{p}(n)=\frac{T_{1}}{T_{p}}$ but $S_{p}=\frac{T^*}{T_{p}}$. So the T1 is the parallel algorithm executed on a single processor, while T* is the best sequential algorithm that solves the same problem. It can happen that T1=T* and in that case it holds that pEp=Sp, it just means that the parallel algorithm on one processor is also the best sequential algorithm.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct.** You correctly distinguish the two baselines and give the condition for equality. Phrase the initial answer as “not necessarily,” since equality does hold when $T_1=T^*$.
>
> **Suggested exam answer:** Not necessarily. Under the course definitions, $pE_p(n)=T_1(n)/T_p(n)$ while $S_p(n)=T^*(n)/T_p(n)$. Consequently, $pE_p=S_p$ exactly when the two sequential baselines agree, $T_1=T^*$. In general, $pE_p=(T_1/T^*)S_p$. Running a parallel algorithm on one processor can require more work than the best sequential algorithm.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** Not necessarily. Under the course definitions, $pE_p(n)=T_1(n)/T_p(n)$ while $S_p(n)=T^*(n)/T_p(n)$. Consequently, $pE_p=S_p$ exactly when the two sequential baselines agree, $T_1=T^*$. In general, $pE_p=(T_1/T^*)S_p$. Running a parallel algorithm on one processor can require more work than the best sequential algorithm.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-019

What happens to the PRAM model if we have a bounded number of processors smaller than the one required by the theoretical model? What happens to the speed-up if the application is a do-all kind of application and we have a bounded number of processors? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=2|2024-09-05-1st · Exercise 1B · p. 2]]

^aapp-02-019

**My answer**

If the number of processor is bounded and lower than the required number, we can use enough virtual processor, and the real ones will share the workload of more than one virtual processor. More precisely with p virtual processors and p' physical ones, each one shares the load of p/p' virtual processors, thus the complexity of the problem is also increased by that factor. The speedup will just consider the real processor p' and not the virtual ones.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct simulation argument; quantify the do-all speedup.** Your virtual-processor explanation is sound. The simulation gives a bound on runtime, rather than an exact slowdown for every algorithm. Saying that speedup uses the physical processor count does not yet describe its behavior for independent iterations.
>
> **Suggested exam answer:** If $p$ virtual processors require $t$ rounds, $p'<p$ physical processors can simulate them by batching, in $O(t\lceil p/p'\rceil)$ time with the same shared memory. Save virtual local states and preserve the original read–compute–write ordering and access policy. For a do-all computation of $n$ independent, equal-cost iterations, $p'$ processors need $\lceil n/p'\rceil$ iteration rounds. Relative to $n$ sequential rounds, ideal speedup is $n/\lceil n/p'\rceil$, approximately $p'$ for enough evenly divisible work. Extra virtual processors do not provide extra physical throughput.
>
> **Example:** Eight independent unit-time iterations on three processors take three rounds, so speedup is $8/3$, below 3 because the last batch is incomplete. Fixed setup or other serial work can reduce speedup further.
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slide 25]].

> [!success]- Model answer
> **Suggested exam answer:** If $p$ virtual processors require $t$ rounds, $p'<p$ physical processors can simulate them by batching, in $O(t\lceil p/p'\rceil)$ time with the same shared memory. Save virtual local states and preserve the original read–compute–write ordering and access policy. For a do-all computation of $n$ independent, equal-cost iterations, $p'$ processors need $\lceil n/p'\rceil$ iteration rounds. Relative to $n$ sequential rounds, ideal speedup is $n/\lceil n/p'\rceil$, approximately $p'$ for enough evenly divisible work. Extra virtual processors do not provide extra physical throughput.
>
> **Example:** Eight independent unit-time iterations on three processors take three rounds, so speedup is $8/3$, below 3 because the last batch is incomplete. Fixed setup or other serial work can reduce speedup further.
>
> **Study:** [[PRAM#Simulating limited resources]]; [[PRAM#Why processor batching must preserve phases]]; [[lecture4-PRAM.pdf#page=25|slide 25]].

### AAPP-02-020

Could you please discuss the following sentence? “Amdahl's law presupposes that the computing requirements will stay the same, given increased processing power. In other words, an analysis of the same data will take less time given more computing power“. Is it true or false? What does it mean? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=2|2024-09-05-1st · Exercise 1C · p. 2]]

^aapp-02-020

**My answer**

It is true, the explanation was reported in other questions multiple times.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct True/False choice; include the explanation locally.** The statement describes Amdahl's fixed-workload assumption. Runtime improvement is an ideal prediction when some work is parallelizable, rather than a guarantee on real hardware.
>
> **Suggested exam answer:** True as a description of Amdahl's model. The input and total computational task stay fixed when processor count increases. The serial part retains its duration, while the parallelizable part is ideally divided among $p$ processors. For serial fraction $s_A$ of the sequential runtime, $T_p/T_{\mathrm{seq}}=s_A+(1-s_A)/p$. Its reciprocal is speedup. The same data is processed sooner when parallelism is available; communication or scheduling overhead can limit real gains.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** True as a description of Amdahl's model. The input and total computational task stay fixed when processor count increases. The serial part retains its duration, while the parallelizable part is ideally divided among $p$ processors. For serial fraction $s_A$ of the sequential runtime, $T_p/T_{\mathrm{seq}}=s_A+(1-s_A)/p$. Its reciprocal is speedup. The same data is processed sooner when parallelism is available; communication or scheduling overhead can limit real gains.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-021

Please show the formula defining the “Efficiency” in a PRAM model. (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1B · p. 2]]

^aapp-02-021

**My answer**

You can find the same answer above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 006; the earlier formula is correct.** This question explicitly asks for the formula, so write it directly.
>
> **Suggested exam answer:** $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1$ is the parallel algorithm's runtime on one processor and $T_p$ is its runtime on $p$ processors. The denominator is allocated processor-time. Ideal linear scaling gives efficiency 1. Since the course defines speedup using $T^*$, the identity $E_p=S_p/p$ additionally requires $T_1=T^*$.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** $E_p(n)=T_1(n)/(pT_p(n))$, where $T_1$ is the parallel algorithm's runtime on one processor and $T_p$ is its runtime on $p$ processors. The denominator is allocated processor-time. Ideal linear scaling gives efficiency 1. Since the course defines speedup using $T^*$, the identity $E_p=S_p/p$ additionally requires $T_1=T^*$.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-022

Can you provide an example where the “work” done by a parallel PRAM program exceeds that of the sequential version of the same algorithm? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1C · p. 2]]

^aapp-02-022

**My answer**

If the problem requires reductions, those could add more operations to the base ones already executed like in the sequential algorithm. I don't have a good real example.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: plausible idea, but incomplete without actual operation counts.** A reduction does not automatically do extra arithmetic: an ordinary binary-tree sum and an optimal sequential sum both use $n-1$ additions. Specify which parallelization operations add work. Idle processors increase cost, not work.
>
> **Suggested exam answer:** Parallelizing a sum can introduce extra accumulator and merge operations. For example, a sequential loop that initializes one accumulator to 0 and adds eight inputs performs eight additions. In a parallel version, four processors each initialize an accumulator to 0 and add two inputs: eight additions in total. Combining the four partial sums needs three further additions, giving 11 additions versus eight sequentially. The extra work comes from the chosen partial-sum implementation. These counts isolate additions and consistently omit loads, stores, and initialization instructions.
>
> **Qualification:** This overhead is implementation-dependent. Seeding each partial sum with its first input can avoid the redundant additions to zero. Extra work must be demonstrated, rather than inferred from the presence of a reduction.
>
> **Study:** [[PRAM#Work versus cost]]; [[PRAM#Reduction]]; [[PRAM#Chunk first, then reduce]]; [[lecture4-PRAM.pdf#page=15|slide 15]].

> [!success]- Model answer
> **Suggested exam answer:** Parallelizing a sum can introduce extra accumulator and merge operations. For example, a sequential loop that initializes one accumulator to 0 and adds eight inputs performs eight additions. In a parallel version, four processors each initialize an accumulator to 0 and add two inputs: eight additions in total. Combining the four partial sums needs three further additions, giving 11 additions versus eight sequentially. The extra work comes from the chosen partial-sum implementation. These counts isolate additions and consistently omit loads, stores, and initialization instructions.
>
> **Qualification:** This overhead is implementation-dependent. Seeding each partial sum with its first input can avoid the redundant additions to zero. Extra work must be demonstrated, rather than inferred from the presence of a reduction.
>
> **Study:** [[PRAM#Work versus cost]]; [[PRAM#Reduction]]; [[PRAM#Chunk first, then reduce]]; [[lecture4-PRAM.pdf#page=15|slide 15]].

### AAPP-02-023

What does it mean fixed-size model? Does it refer to Gustafson or Amdahl’s law? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1D · p. 2]]

^aapp-02-023

**My answer**

That would be amdahl law like i have already explained above.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct identification; state what “fixed-size” means.** Referring to earlier explanations is sufficient for your revision shorthand, but an exam answer needs the defining assumption.
>
> **Suggested exam answer:** A fixed-size model holds the input and computational workload constant while increasing the number of processors. It asks how much the same problem's runtime can decrease. This is Amdahl's viewpoint: with sequential serial fraction $s_A$, $S_A(p)=1/(s_A+(1-s_A)/p)$.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** A fixed-size model holds the input and computational workload constant while increasing the number of processors. It asks how much the same problem's runtime can decrease. This is Amdahl's viewpoint: with sequential serial fraction $s_A$, $S_A(p)=1/(s_A+(1-s_A)/p)$.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-024

Could you please elaborate on the conditions under which the following formula holds as an equality and when it holds as an inequality: SUp ≤ p?"

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1B · p. 2]]

^aapp-02-024

**My answer**

No idea

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: no solution supplied; the key condition is perfect linear speedup.** The question concerns the course's ideal comparison for the same problem and input, with compatible unit-cost operations and a best sequential baseline.
>
> **Suggested exam answer:** Since $S_p=T^*/T_p$, equality $S_p=p$ holds when $T_p=T^*/p$, equivalently when allocated cost $pT_p$ exactly matches the sequential baseline $T^*$. This is ideal linear speedup: the baseline work is perfectly distributed with no lost processor-time or additional overhead. Strict inequality $S_p<p$ holds when $T_p>T^*/p$, for example because of serial dependencies, load imbalance, idle slots, or extra executed operations. Keeping every processor busy is insufficient if the parallel implementation does more work than the sequential baseline.
>
> **Amdahl illustration:** With $T^*=T_{\mathrm{seq}}$ and the ideal fixed-size formula, $S_p=1/(s_A+(1-s_A)/p)$. For $p>1$, $s_A=0$ gives $S_p=p$, while $s_A>0$ gives $S_p<p$. Even with $s_A=0$, real overhead can prevent equality. The bound $S_p\le p$ assumes the stated ideal comparison; changing the baseline, workload, or machine cost assumptions changes that comparison.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=11|slide 11]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Since $S_p=T^*/T_p$, equality $S_p=p$ holds when $T_p=T^*/p$, equivalently when allocated cost $pT_p$ exactly matches the sequential baseline $T^*$. This is ideal linear speedup: the baseline work is perfectly distributed with no lost processor-time or additional overhead. Strict inequality $S_p<p$ holds when $T_p>T^*/p$, for example because of serial dependencies, load imbalance, idle slots, or extra executed operations. Keeping every processor busy is insufficient if the parallel implementation does more work than the sequential baseline.
>
> **Amdahl illustration:** With $T^*=T_{\mathrm{seq}}$ and the ideal fixed-size formula, $S_p=1/(s_A+(1-s_A)/p)$. For $p>1$, $s_A=0$ gives $S_p=p$, while $s_A>0$ gives $S_p<p$. Even with $s_A=0$, real overhead can prevent equality. The bound $S_p\le p$ assumes the stated ideal comparison; changing the baseline, workload, or machine cost assumptions changes that comparison.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=11|slide 11]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-025

Could you please elaborate on what “weak scaling” means? To which law we have seen during the lectures is referring to? (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1C · p. 2]]

^aapp-02-025

**My answer**

I already answered that.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; refine the earlier weak-scaling definition.** Keep work per processor fixed. Approximately constant runtime is the desired scaling behavior, rather than a condition automatically satisfied by an implementation.
>
> **Suggested exam answer:** Weak scaling increases total workload proportionally to the number of processors, holding work per processor fixed. For a baseline workload $n_0$ per processor, compare $T_1(n_0)$ with $T_p(pn_0)$ when workload is proportional to $n$. Good weak scaling keeps those runtimes approximately equal. It is associated with Gustafson's scaled-workload, fixed-time viewpoint. Gustafson's scaled speedup compares sequential and parallel execution of the same larger workload; that ratio differs from the weak-scaling efficiency measurement.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

> [!success]- Model answer
> **Suggested exam answer:** Weak scaling increases total workload proportionally to the number of processors, holding work per processor fixed. For a baseline workload $n_0$ per processor, compare $T_1(n_0)$ with $T_p(pn_0)$ when workload is proportional to $n$. Good weak scaling keeps those runtimes approximately equal. It is associated with Gustafson's scaled-workload, fixed-time viewpoint. Gustafson's scaled speedup compares sequential and parallel execution of the same larger workload; that ratio differs from the weak-scaling efficiency measurement.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

### AAPP-02-026

Please describe the speed-up when a fixed-size model is considered. (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1D · p. 2]]

^aapp-02-026

**My answer**

That is amdahl law as i have already explained

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct law identified; give its speedup and limiting behavior.** Referring to Amdahl alone does not supply the requested discussion.
>
> **Suggested exam answer:** For a fixed-size workload with serial fraction $s_A$ measured in sequential runtime, ideal speedup is $S_A(p)=1/(s_A+(1-s_A)/p)$. Only the parallel part is divided by $p$; the serial duration stays fixed. If $s_A>0$, increasing processor count gives diminishing gains and speedup approaches $1/s_A$. If $s_A=0$, the ideal formula gives $S_A=p$. The formula assumes perfect distribution of parallel work and no additional overhead.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** For a fixed-size workload with serial fraction $s_A$ measured in sequential runtime, ideal speedup is $S_A(p)=1/(s_A+(1-s_A)/p)$. Only the parallel part is divided by $p$; the serial duration stays fixed. If $s_A>0$, increasing processor count gives diminishing gains and speedup approaches $1/s_A$. If $s_A=0$, the ideal formula gives $S_A=p$. The formula assumes perfect distribution of parallel work and no additional overhead.
>
> **Study:** [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-027

Could you please discuss the differences between “weak scaling” and “strong scaling”? To which laws we have seen during the lectures are referring to? (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1C · p. 2]]

^aapp-02-027

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; make the two experiments explicit.** Your earlier distinction is useful, with the correction that weak scaling fixes work per processor and measures the resulting runtime.
>
> **Suggested exam answer:** Strong scaling holds total workload fixed and adds processors to reduce runtime; Amdahl's law describes the ideal fixed-size speedup and its serial bottleneck. Weak scaling holds work per processor fixed, so total work grows with processor count; good behavior is approximately constant runtime. Gustafson's law describes the benefit of scaling the parallel workload within a fixed time budget. The serial fractions in the two laws refer to sequential and parallel runtime respectively.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Strong scaling holds total workload fixed and adds processors to reduce runtime; Amdahl's law describes the ideal fixed-size speedup and its serial bottleneck. Weak scaling holds work per processor fixed, so total work grows with processor count; good behavior is approximately constant runtime. Gustafson's law describes the benefit of scaling the parallel workload within a fixed time budget. The serial fractions in the two laws refer to sequential and parallel runtime respectively.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=28|slide 28]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-028

Please define and discuss the speed-up when Gustafson’s law is considered. (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1D · p. 2]]

^aapp-02-028

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; use the precise interpretation established in our discussion.** Gustafson reconstructs the sequential time of the same scaled workload. Multiplication by $p$ accounts for the work performed concurrently by all processors.
>
> **Suggested exam answer:** With parallel runtime normalized to 1 and its serial fraction denoted by $s_G$, Gustafson's scaled speedup is $S_G(p)=s_G+p(1-s_G)$. A sequential processor executes the serial part once and takes $p$ times as long for the work completed during the parallel phase. Thus $S_G$ is the factor by which sequential execution of that same scaled workload would take longer. The model grows parallel work with processor count while holding the parallel time budget fixed. For fixed $s_G<1$, scaled speedup grows linearly with $p$ under the ideal assumptions.
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** With parallel runtime normalized to 1 and its serial fraction denoted by $s_G$, Gustafson's scaled speedup is $S_G(p)=s_G+p(1-s_G)$. A sequential processor executes the serial part once and takes $p$ times as long for the work completed during the parallel phase. Thus $S_G$ is the factor by which sequential execution of that same scaled workload would take longer. The model grows parallel work with processor count while holding the parallel time budget fixed. For fixed $s_G<1$, scaled speedup grows linearly with $p$ under the ideal assumptions.
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-029

How does the matrix-vector multiplication example illustrate strong scaling, and what would change in a weak scaling scenario? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1C · p. 2]]

^aapp-02-029

**My answer**

Strong scaling is trying to measure how much faster a fixed workload can be completed by adding more computing resources. In a matrix multiplication of fixed sized there are a lot of row columns multiplications that can be executed in parallel as they are not dependent on each other.  If i add more processors i can reduce the compute time. Matrix multiplication has a good strong scaling. While in a weak scaling scenario it tries to measure how much workload can be finished in the same fixed time by having more compute.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct strong-scaling idea; use matrix-vector multiplication and specify how the weak-scaling input grows.** The supplied example computes each matrix row dotted with one shared vector. Different output rows are independent. “Good strong scaling” is possible in the ideal model within the available row parallelism; it is not guaranteed for arbitrary processor counts or real memory systems.
>
> **Suggested exam answer:** In $y=Ax$, separate processors can compute independent output rows. For a fixed $r\times c$ matrix and vector of length $c$, a row-based PRAM schedule takes $\Theta(c\lceil r/p\rceil)$ time, so increasing $p\le r$ reduces runtime while input size remains fixed: strong scaling. For weak scaling, one concrete choice is to grow the number of rows proportionally to $p$ while keeping $c$ and rows per processor fixed. Each processor then performs the same number of dot-product operations, so ideal runtime stays approximately constant while the total matrix grows. Real bandwidth, communication, and imbalance can limit either scaling behavior.
>
> **Study:** [[PRAM#Map: matrix-vector multiplication]]; [[PRAM#Worked row decomposition]]; [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=20|slide 20]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

> [!success]- Model answer
> **Suggested exam answer:** In $y=Ax$, separate processors can compute independent output rows. For a fixed $r\times c$ matrix and vector of length $c$, a row-based PRAM schedule takes $\Theta(c\lceil r/p\rceil)$ time, so increasing $p\le r$ reduces runtime while input size remains fixed: strong scaling. For weak scaling, one concrete choice is to grow the number of rows proportionally to $p$ while keeping $c$ and rows per processor fixed. Each processor then performs the same number of dot-product operations, so ideal runtime stays approximately constant while the total matrix grows. Real bandwidth, communication, and imbalance can limit either scaling behavior.
>
> **Study:** [[PRAM#Map: matrix-vector multiplication]]; [[PRAM#Worked row decomposition]]; [[PRAM#Strong and weak scaling]]; [[lecture4-PRAM.pdf#page=20|slide 20]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

### AAPP-02-030

Why does Amdahl’s Law suggest diminishing returns with increasing processors, and how does Gustafson’s Law counter this? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1D · p. 2]]

^aapp-02-030

**My answer**

Amdal law has the number of processor as fraction. So as it increases the parallelizable part of the program is less and less up to infinite p where the speedup caps at 1/s, where s is the serial part. Gustafson law instead does not have this limit as if we have an infinite number of processor the speedup would also be infinite.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: partly correct; explain the unchanged serial time and the growing workload.** You correctly identify Amdahl's ceiling when the serial fraction is positive. The parallelizable fraction of the original sequential workload remains fixed; its elapsed parallel execution time decreases. Gustafson's growth describes larger workloads and assumes a parallel-time serial fraction below 1.
>
> **Suggested exam answer:** Amdahl fixes problem size. As $p$ increases, $(1-s_A)/p$ shrinks while serial time $s_A$ remains, so $S_A(p)=1/(s_A+(1-s_A)/p)$ approaches $1/s_A$ for $s_A>0$. Gustafson changes the experiment by increasing parallel work within a fixed runtime: $S_G(p)=s_G+p(1-s_G)$. For fixed $s_G<1$, scaled speedup grows linearly with processor count. This explains why many processors can remain useful for larger problems; it does not eliminate the serial bottleneck for a fixed problem. Both laws use ideal assumptions and different serial-fraction baselines.
>
> **Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Amdahl fixes problem size. As $p$ increases, $(1-s_A)/p$ shrinks while serial time $s_A$ remains, so $S_A(p)=1/(s_A+(1-s_A)/p)$ approaches $1/s_A$ for $s_A>0$. Gustafson changes the experiment by increasing parallel work within a fixed runtime: $S_G(p)=s_G+p(1-s_G)$. For fixed $s_G<1$, scaled speedup grows linearly with processor count. This explains why many processors can remain useful for larger problems; it does not eliminate the serial bottleneck for a fixed problem. Both laws use ideal assumptions and different serial-fraction baselines.
>
> **Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-031

Given an algorithm with $T_1(n)=n^3$ and $T_p(n)=n^3/p$, analyze the speedup and efficiency. What can you conclude? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1B · p. 2]]

^aapp-02-031

**My answer**

speedup is 1/p while efficiency is 1 it also means that T1 is the best sequential algorithm and no processor idle.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: speedup is inverted; efficiency is correct; optimality does not follow.** $(n^3)/(n^3/p)=p$, rather than $1/p$. Also, being given $T_1=n^3$ does not establish that no better sequential algorithm exists.
>
> **Suggested exam answer:** The speedup relative to the one-processor execution is $T_1/T_p=n^3/(n^3/p)=p$, and efficiency is $E_p=T_1/(pT_p)=1$. Thus the formulas describe ideal linear scaling relative to $T_1$ in the processor range where the stated runtime model applies. With the course's definition $S_p=T^*/T_p$, the exact expression is $S_p=pT^*(n)/n^3$. If the intended additional assumption is $T^*=T_1=n^3$, then $S_p=p$ and the cost $pT_p=n^3$ matches that sequential baseline. The supplied runtimes alone do not prove $T_1=T^*$ or establish a detailed processor schedule.
>
> **Study:** [[PRAM#Performance quantities]]; [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** The speedup relative to the one-processor execution is $T_1/T_p=n^3/(n^3/p)=p$, and efficiency is $E_p=T_1/(pT_p)=1$. Thus the formulas describe ideal linear scaling relative to $T_1$ in the processor range where the stated runtime model applies. With the course's definition $S_p=T^*/T_p$, the exact expression is $S_p=pT^*(n)/n^3$. If the intended additional assumption is $T^*=T_1=n^3$, then $S_p=p$ and the cost $pT_p=n^3$ matches that sequential baseline. The supplied runtimes alone do not prove $T_1=T^*$ or establish a detailed processor schedule.
>
> **Study:** [[PRAM#Performance quantities]]; [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-032

How does Gustafson’s Law support the concept of weak scaling, and what is its implication for massively parallel systems? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1D · p. 2]]

^aapp-02-032

**My answer**

Not sure about the implication for massive parallel, but for weak scaling i already answered a lot.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: incomplete; explain why a large processor count can still be useful.** The implication for massively parallel systems follows from growing the amount of parallel work, rather than repeatedly accelerating a fixed small problem.
>
> **Suggested exam answer:** Weak scaling keeps work per processor fixed as processors and total work increase. Gustafson's fixed-time model expresses the associated opportunity: for parallel-run serial fraction $s_G$, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. If $s_G$ remains small, it is close to $p$, so a massively parallel system can solve a proportionally larger problem within roughly the same time budget. This requires sufficient independent work and controlled serial, communication, and synchronization costs. The law supports this possibility; it does not guarantee that every growing application scales well.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Weak scaling keeps work per processor fixed as processors and total work increase. Gustafson's fixed-time model expresses the associated opportunity: for parallel-run serial fraction $s_G$, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. If $s_G$ remains small, it is close to $p$, so a massively parallel system can solve a proportionally larger problem within roughly the same time budget. This requires sufficient independent work and controlled serial, communication, and synchronization costs. The law supports this possibility; it does not guarantee that every growing application scales well.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-033

Assuming $T^*(n)=T_1(n)$, what kind of relation do you have between the efficiency and the speedup of a PRAM-based application? (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=2|2025-11-06-1st · Exercise 1B · p. 2]]

^aapp-02-033

**My answer**

the speedup S=pE

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct; add a one-line derivation.** The prompt explicitly supplies the baseline equality needed for your identity.
>
> **Suggested exam answer:** Since $T^*(n)=T_1(n)$, $S_p(n)=T_1(n)/T_p(n)$ and $E_p(n)=T_1(n)/(pT_p(n))$. Therefore $S_p(n)=pE_p(n)$, equivalently $E_p=S_p/p$. With these matching baselines, ideal speedup $S_p=p$ gives efficiency 1.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

> [!success]- Model answer
> **Suggested exam answer:** Since $T^*(n)=T_1(n)$, $S_p(n)=T_1(n)/T_p(n)$ and $E_p(n)=T_1(n)/(pT_p(n))$. Therefore $S_p(n)=pE_p(n)$, equivalently $E_p=S_p/p$. With these matching baselines, ideal speedup $S_p=p$ gives efficiency 1.
>
> **Study:** [[PRAM#Speedup and efficiency]]; [[lecture4-PRAM.pdf#page=8|slide 8]].

### AAPP-02-034

Please outline the key aspects of strong scalability (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=2|2025-11-06-1st · Exercise 1D · p. 2]]

^aapp-02-034

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; include the experiment, ideal behavior, and limitations.** These are the key aspects an exam answer should state directly.
>
> **Suggested exam answer:** Strong scalability measures how runtime changes when processor count increases for the same fixed total problem. Ideally, $T_p\approx T_1/p$ and speedup relative to $T_1$ is approximately $p$. Measure fixed-input runtimes over increasing processor counts and examine speedup and efficiency. Serial dependencies, limited parallelism, load imbalance, and real communication or synchronization overhead eventually limit gains. Amdahl's fixed-size model gives a ceiling $1/s_A$ when the sequential serial fraction $s_A$ is positive.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

> [!success]- Model answer
> **Suggested exam answer:** Strong scalability measures how runtime changes when processor count increases for the same fixed total problem. Ideally, $T_p\approx T_1/p$ and speedup relative to $T_1$ is approximately $p$. Measure fixed-input runtimes over increasing processor counts and examine speedup and efficiency. Serial dependencies, limited parallelism, load imbalance, and real communication or synchronization overhead eventually limit gains. Amdahl's fixed-size model gives a ceiling $1/s_A$ when the sequential serial fraction $s_A$ is positive.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

### AAPP-02-035

Please outline the key aspects of Gustafson's law and how it relates to scalability. (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=2|2026-1-22-1st · Exercise 1D · p. 2]]

^aapp-02-035

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; include the workload assumption and the runtime baseline of the serial fraction.** Your later explanation of sequential time for a scaled workload is the useful interpretation here.
>
> **Suggested exam answer:** Gustafson considers growing the parallel workload with processor count while keeping parallel runtime fixed. If $s_G$ is the serial fraction of that parallel run, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. It compares one-processor and $p$-processor execution of the same scaled problem. For a small, approximately constant $s_G$, scaled speedup can remain close to linear, supporting the usefulness of large systems for larger workloads. This relates to weak scaling; it assumes enough parallel work and manageable serial and communication costs. See also [Gustafson's fixed-size and scaled-size comparison](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Gustafson considers growing the parallel workload with processor count while keeping parallel runtime fixed. If $s_G$ is the serial fraction of that parallel run, scaled speedup is $S_G(p)=s_G+p(1-s_G)$. It compares one-processor and $p$-processor execution of the same scaled problem. For a small, approximately constant $s_G$, scaled speedup can remain close to linear, supporting the usefulness of large systems for larger workloads. This relates to weak scaling; it assumes enough parallel work and manageable serial and communication costs. See also [Gustafson's fixed-size and scaled-size comparison](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2).
>
> **Study:** [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-036

Please show an example where idling processors is unavoidable, and explain how it affects efficiency. (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=2|2026-2-09-1st · Exercise 1A · p. 2]]

^aapp-02-036

**My answer**

When for example we have a sum and the first round we use all processors. Then we reduce the results and use only half of the processors, those are idle, and the more this happens the less the efficiency is, beacase the total cpu time increases even if no work is being done. Max efficiency is 1.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct example and effect; make the cost calculation explicit.** In a fixed tree-reduction schedule, later levels have fewer independent operations, so the allocated processors cannot all stay busy. Idle slots contribute to allocated cost without adding work. They do not necessarily make elapsed runtime increase when more processors are added.
>
> **Suggested exam answer:** Consider summing eight inputs by a binary tree on four allocated processors. Counting addition rounds only, the three levels execute 4, 2, and 1 additions. Thus $W=7$, $T_4=3$, and $C_4=4\cdot3=12$. The last two levels have insufficient independent additions to occupy every processor, leaving five idle slots. A one-processor execution needs seven additions, so $E_4=7/12\approx0.583$. The dependencies impose this loss of utilization for the stated schedule. Efficiency 1 is the ideal upper value for this fixed-computation PRAM comparison.
>
> **Study:** [[PRAM#Reading a processor-time diagram]]; [[PRAM#Reduction]]; [[lecture4-PRAM.pdf#page=21|slide 21]].

> [!success]- Model answer
> **Suggested exam answer:** Consider summing eight inputs by a binary tree on four allocated processors. Counting addition rounds only, the three levels execute 4, 2, and 1 additions. Thus $W=7$, $T_4=3$, and $C_4=4\cdot3=12$. The last two levels have insufficient independent additions to occupy every processor, leaving five idle slots. A one-processor execution needs seven additions, so $E_4=7/12\approx0.583$. The dependencies impose this loss of utilization for the stated schedule. Efficiency 1 is the ideal upper value for this fixed-computation PRAM comparison.
>
> **Study:** [[PRAM#Reading a processor-time diagram]]; [[PRAM#Reduction]]; [[lecture4-PRAM.pdf#page=21|slide 21]].

### AAPP-02-037

You observe near-linear speedup when increasing processors. Is this evidence supporting Amdahl’s model or Gustafson’s model? Explain why. (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=2|2026-2-09-1st · Exercise 1D · p. 2]]

^aapp-02-037

**My answer**

most probably gustafson, Amdahl law has diminishing return and caps at 1/s

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: not justified; near-linear speedup alone does not distinguish the models.** Amdahl can predict nearly linear speedup over the measured processor range if its serial fraction is sufficiently small. Its eventual ceiling does not imply visibly diminishing returns at every processor count.
>
> **Suggested exam answer:** More information about the experiment is needed. If the workload is fixed, near-linear speedup is compatible with Amdahl when the sequential serial fraction is small; with $s_A=0$, its ideal formula gives exactly $S_A=p$. If the workload grows with processor count at approximately fixed runtime, near-linear scaled speedup is consistent with Gustafson and a small parallel-run serial fraction $s_G$. Identify what remains fixed and how speedup is defined before selecting a model. The observed curve alone is insufficient.
>
> **Example:** Amdahl with $s_A=0.001$ and $p=8$ gives $S_A=1/(0.001+0.999/8)\approx7.94$, very close to 8 despite using a fixed-size model. This counterexample follows directly from the formula; it is not a claim about which experiment the question omitted.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** More information about the experiment is needed. If the workload is fixed, near-linear speedup is compatible with Amdahl when the sequential serial fraction is small; with $s_A=0$, its ideal formula gives exactly $S_A=p$. If the workload grows with processor count at approximately fixed runtime, near-linear scaled speedup is consistent with Gustafson and a small parallel-run serial fraction $s_G$. Identify what remains fixed and how speedup is defined before selecting a model. The observed curve alone is insufficient.
>
> **Example:** Amdahl with $s_A=0.001$ and $p=8$ gives $S_A=1/(0.001+0.999/8)\approx7.94$, very close to 8 despite using a fixed-size model. This counterexample follows directly from the formula; it is not a claim about which experiment the question omitted.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-038

Discuss the scalability laws presented in class and their interpretation in terms of time and processors. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=2|2026-6-11-1st · Exercise 1D · p. 2]]

^aapp-02-038

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; summarize the two laws with their assumptions.** The interpretation in terms of time and processors is essential, rather than just naming the formulas.
>
> **Suggested exam answer:** Amdahl holds problem size fixed and models how adding processors reduces runtime: $S_A(p)=1/(s_A+(1-s_A)/p)$, where $s_A$ is the serial fraction of sequential runtime. For $s_A>0$, speedup approaches $1/s_A$. Gustafson keeps a parallel time budget fixed while increasing parallel workload: $S_G(p)=s_G+p(1-s_G)$, where $s_G$ is measured in the parallel run. This can give near-linear scaled speedup for small $s_G$. The laws correspond to fixed-size and scaled-size viewpoints, associated with strong and weak scaling. They are compatible; their workloads and serial-fraction baselines differ. Real overhead must be assessed separately.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Amdahl holds problem size fixed and models how adding processors reduces runtime: $S_A(p)=1/(s_A+(1-s_A)/p)$, where $s_A$ is the serial fraction of sequential runtime. For $s_A>0$, speedup approaches $1/s_A$. Gustafson keeps a parallel time budget fixed while increasing parallel workload: $S_G(p)=s_G+p(1-s_G)$, where $s_G$ is measured in the parallel run. This can give near-linear scaled speedup for small $s_G$. The laws correspond to fixed-size and scaled-size viewpoints, associated with strong and weak scaling. They are compatible; their workloads and serial-fraction baselines differ. Real overhead must be assessed separately.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-039

Please describe how Amdahl and Gustafson define the speed-up. (1)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=2|2026-6-29-1st · Exercise 1D · p. 2]]

^aapp-02-039

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; give both runtime constructions explicitly.** Both speedups compare sequential and parallel execution of the same workload within each calculation; the workload may grow across Gustafson's processor-count experiments.
>
> **Suggested exam answer:** Amdahl normalizes a fixed problem's sequential time to 1. With sequential serial fraction $s_A$, its parallel time is $s_A+(1-s_A)/p$, so speedup is $1/(s_A+(1-s_A)/p)$. Gustafson normalizes the scaled problem's parallel time to 1. With parallel-run serial fraction $s_G$, its sequential time would be $s_G+p(1-s_G)$, which is also its scaled speedup. The fractions use different denominators, and both formulas assume ideal parallelization without extra overhead.
>
> **Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

> [!success]- Model answer
> **Suggested exam answer:** Amdahl normalizes a fixed problem's sequential time to 1. With sequential serial fraction $s_A$, its parallel time is $s_A+(1-s_A)/p$, so speedup is $1/(s_A+(1-s_A)/p)$. Gustafson normalizes the scaled problem's parallel time to 1. With parallel-run serial fraction $s_G$, its sequential time would be $s_G+p(1-s_G)$, which is also its scaled speedup. The fractions use different denominators, and both formulas assume ideal parallelization without extra overhead.
>
> **Study:** [[PRAM#Amdahl's law]]; [[PRAM#Gustafson's law]]; [[PRAM#Reconciling the two serial fractions]]; [[lecture4-PRAM.pdf#page=31|slide 31]].

### AAPP-02-040

In the PRAM model, explain the meaning of work efficiency and why a parallel algorithm may perform more work than its sequential counterpart. Give one concrete example involving parallel overhead. (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=2|2026-9-10-1st · Exercise 1B · p. 2]]

^aapp-02-040

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: incomplete by reference; work efficiency and a concrete overhead example still need to be supplied.** Your earlier work definition is correct. Work efficiency is an asymptotic comparison, rather than the fraction of allocated processor-time that is busy.
>
> **Suggested exam answer:** A parallel algorithm is work-efficient if $W(n)=O(T^*(n))$: its total executed operations are within a constant factor of the best sequential baseline. Parallelization may add initialization, duplicated calculations, or bookkeeping and merging operations. For example, summing $n$ values sequentially into one accumulator initialized to 0 uses $n$ additions. With $p$ nonempty chunks, initializing each partial accumulator to 0 and adding its inputs still uses $n$ additions, then merging the $p$ partials adds $p-1$ more. The parallel implementation therefore uses $n+p-1$ additions. Counting additions only, this demonstrates extra executed work, and it remains $O(n)$ for $p\le n$: more operations do not automatically destroy work efficiency. Idle processors affect cost rather than work.
>
> **Model detail:** The example's extra additions depend on its accumulator initialization strategy and can be optimized away; it demonstrates one concrete implementation rather than a lower bound for parallel summation.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]]. The asymptotic definition is also given by [Blelloch and Maggs, §25.2.3](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=9).

> [!success]- Model answer
> **Suggested exam answer:** A parallel algorithm is work-efficient if $W(n)=O(T^*(n))$: its total executed operations are within a constant factor of the best sequential baseline. Parallelization may add initialization, duplicated calculations, or bookkeeping and merging operations. For example, summing $n$ values sequentially into one accumulator initialized to 0 uses $n$ additions. With $p$ nonempty chunks, initializing each partial accumulator to 0 and adding its inputs still uses $n$ additions, then merging the $p$ partials adds $p-1$ more. The parallel implementation therefore uses $n+p-1$ additions. Counting additions only, this demonstrates extra executed work, and it remains $O(n)$ for $p\le n$: more operations do not automatically destroy work efficiency. Idle processors affect cost rather than work.
>
> **Model detail:** The example's extra additions depend on its accumulator initialization strategy and can be optimized away; it demonstrates one concrete implementation rather than a lower bound for parallel summation.
>
> **Study:** [[PRAM#Work versus cost]]; [[lecture4-PRAM.pdf#page=15|slide 15]]. The asymptotic definition is also given by [Blelloch and Maggs, §25.2.3](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=9).

### AAPP-02-041

Please outline the key aspects of weak scalability (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=2|2026-9-10-1st · Exercise 1D · p. 2]]

^aapp-02-041

**My answer**

already done above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; use the corrected definition of weak scalability.** State what is fixed in the experiment and what successful performance looks like.
>
> **Suggested exam answer:** Weak scalability measures runtime as processors and total work increase together, keeping work per processor fixed. If one processor handles workload $n_0$ in $T_1(n_0)$, ideal weak scaling gives $T_p(pn_0)\approx T_1(n_0)$ when work grows proportionally to $n$. Weak-scaling efficiency can be reported as $E_{\mathrm{weak}}=T_1(n_0)/T_p(pn_0)$. Communication, global synchronization, serial work, or imbalance can make runtime grow. Gustafson's fixed-time, scaled-workload viewpoint explains the benefit of larger systems, while constant measured runtime remains a result to verify.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Two experiments with different meanings]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

> [!success]- Model answer
> **Suggested exam answer:** Weak scalability measures runtime as processors and total work increase together, keeping work per processor fixed. If one processor handles workload $n_0$ in $T_1(n_0)$, ideal weak scaling gives $T_p(pn_0)\approx T_1(n_0)$ when work grows proportionally to $n$. Weak-scaling efficiency can be reported as $E_{\mathrm{weak}}=T_1(n_0)/T_p(pn_0)$. Communication, global synchronization, serial work, or imbalance can make runtime grow. Gustafson's fixed-time, scaled-workload viewpoint explains the benefit of larger systems, while constant measured runtime remains a result to verify.
>
> **Study:** [[PRAM#Strong and weak scaling]]; [[PRAM#Two experiments with different meanings]]; [[lecture4-PRAM.pdf#page=28|slide 28]].

## PRAM algorithms

Related notes: [[PRAM]].

### AAPP-03-001

Please describe the matrix multiply algorithm on PRAM (Pseudo code. Complexity). (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1A · p. 2]]

^aapp-03-001

**My answer**

For matrix multiplication we have to compute a linear combination of row columns couples. We need to match all rows of the first matrix with all columns of the second. The code is:
for (int i=0; i<size; i++) {
	for (int j=0; j<size; j++) {
			result\[i]\[j] = linear_combination(A1.row(i), A2.column(j))
	}
}

where linear combinations is just the sum of multiplied element from the two vectors. All instances of for exectuion can be parallel. The complexity is given p processors. O(n(n/p)), if p=n O(n) while work is O(n^2). For the exam sake this is an old kind of question and should not appear in newer exams.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct row–column idea, but the complexity counts matrix–vector work.** An $n\times n$ matrix product has $n^2$ output entries, each requiring a dot product of length $n$. Your function `linear_combination` hides that inner loop; it is not a unit-time operation. Both output loops can run in parallel, but each dot product needs either sequential accumulation or an explicitly parallel reduction.
>
> **Suggested exam answer:** For dense square matrices, $C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$. One simple PRAM algorithm assigns output entries to processors, with a private accumulator per entry:
>
> ```text
> parallel for each pair (i, j), scheduled over p processors:
>     s = 0                         // private accumulator
>     for k = 0 to n - 1:           // sequential within this task
>         s = s + A[i,k] * B[k,j]
>     C[i,j] = s
> ```
>
> For this schedule, $W=\Theta(n^3)$ and $T_p=\Theta(n\lceil n^2/p\rceil)$ for $1\le p\le n^2$. Thus $p=n$ gives $\Theta(n^2)$ time, while $p=n^2$ gives $\Theta(n)$ time. Shared input entries may have several readers, while each output has one writer, so CREW suffices.
>
> **Further parallelism:** Parallelizing the products within each dot product and reducing them can give $O(\log n)$ time with $\Theta(n^3)$ processors and $\Theta(n^3)$ work. The processor allocation and reduction must be stated. These are classical multiplication bounds, rather than lower bounds for every multiplication algorithm. See [Blelloch and Maggs, §25.8.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=37).
>
> **Course scope:** The supplied PRAM deck illustrates matrix–vector multiplication; the construction above explicitly answers a matrix–matrix interpretation. The bank also contains a matrix–matrix prompt from July 2024 in [[#AAPP-03-005]]. The age of a question does not establish its exclusion from a future exam; no such exclusion has been verified here.
>
> **Study:** [[Divide and Conquer#Matrix multiplication]]; compare [[PRAM#Map: matrix-vector multiplication]].

> [!success]- Model answer
> **Suggested exam answer:** For dense square matrices, $C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$. One simple PRAM algorithm assigns output entries to processors, with a private accumulator per entry:
>
> ```text
> parallel for each pair (i, j), scheduled over p processors:
>     s = 0                         // private accumulator
>     for k = 0 to n - 1:           // sequential within this task
>         s = s + A[i,k] * B[k,j]
>     C[i,j] = s
> ```
>
> For this schedule, $W=\Theta(n^3)$ and $T_p=\Theta(n\lceil n^2/p\rceil)$ for $1\le p\le n^2$. Thus $p=n$ gives $\Theta(n^2)$ time, while $p=n^2$ gives $\Theta(n)$ time. Shared input entries may have several readers, while each output has one writer, so CREW suffices.
>
> **Further parallelism:** Parallelizing the products within each dot product and reducing them can give $O(\log n)$ time with $\Theta(n^3)$ processors and $\Theta(n^3)$ work. The processor allocation and reduction must be stated. These are classical multiplication bounds, rather than lower bounds for every multiplication algorithm. See [Blelloch and Maggs, §25.8.1](https://www.cs.cmu.edu/~guyb/papers/BM10.pdf#page=37).
>
> **Course scope:** The supplied PRAM deck illustrates matrix–vector multiplication; the construction above explicitly answers a matrix–matrix interpretation. The bank also contains a matrix–matrix prompt from July 2024 in [[#AAPP-03-005]]. The age of a question does not establish its exclusion from a future exam; no such exclusion has been verified here.
>
> **Study:** [[Divide and Conquer#Matrix multiplication]]; compare [[PRAM#Map: matrix-vector multiplication]].

### AAPP-03-002

The PRAM algorithm computing the prefix sum of a vector uses concurrent reads. True/False? Where? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1C · p. 2]]

^aapp-03-002

**My answer**

True, besides the first round every other one has multiple processor read the same values, and it adds different elements based on which partial sum we need to obtain. For example the value in position 2 is read by two processor that compute the partial sum of 3 and of 4 elements.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct for the broadcast scan illustrated in the lecture.** Your example matches the diagram when positions are numbered from 1. Be explicit that processors read the same intermediate cell during the same read phase; simultaneous reads of different cells do not require concurrent-read permission.
>
> **Suggested exam answer:** True for the lecture's broadcast implementation. After the first pairwise stage, cell 2 contains $a_1+a_2$. In the next stage, processors computing prefixes 3 and 4 both read that cell and add it to their respective right-half partial sums. For eight inputs, a later stage similarly broadcasts the sum in cell 4 to processors computing prefixes 5 through 8. The resulting prefix entries have distinct writers, so this implementation uses CREW. The first pairwise stage does not need this shared-prefix broadcast.
>
> **Qualification:** This describes the diagram's implementation. Prefix scan can also be implemented on EREW with a different schedule, so concurrent reads are not an unavoidable property of the prefix-sum problem itself.
>
> **Study:** [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=23|slide 23, green CR labels]]; [[PRAM#How the work-efficient tree scan works]].

> [!success]- Model answer
> **Suggested exam answer:** True for the lecture's broadcast implementation. After the first pairwise stage, cell 2 contains $a_1+a_2$. In the next stage, processors computing prefixes 3 and 4 both read that cell and add it to their respective right-half partial sums. For eight inputs, a later stage similarly broadcasts the sum in cell 4 to processors computing prefixes 5 through 8. The resulting prefix entries have distinct writers, so this implementation uses CREW. The first pairwise stage does not need this shared-prefix broadcast.
>
> **Qualification:** This describes the diagram's implementation. Prefix scan can also be implemented on EREW with a different schedule, so concurrent reads are not an unavoidable property of the prefix-sum problem itself.
>
> **Study:** [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=23|slide 23, green CR labels]]; [[PRAM#How the work-efficient tree scan works]].

### AAPP-03-003

Please describe how prefix scan works when a PRAM architecture is considered. (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1C · p. 2]]

^aapp-03-003

**My answer**

Prefix scan i am not sure it was covered in the PRAM part.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: no algorithm supplied; prefix scan is covered in the PRAM material.** “Scan” is another name for the prefix operation. The inclusive sum scan outputs $S_i=\sum_{j=1}^{i}a_j$ for every position, rather than returning only the final total.
>
> **Suggested exam answer:** In the lecture's broadcast pattern, start with blocks of one input. At each stage, combine adjacent blocks of equal size: the prefixes in the left block stay unchanged, and the total of that left block is added to every local prefix in the right block. Double the block size and synchronize before the next stage. Each stage reads the preceding stage's values; use separate input/output buffers to make that ordering explicit. After $\lceil\log_2 n\rceil$ stages, each position holds its complete prefix. Padding with zeros handles a non-power-of-two length without changing the asymptotic bounds.
>
> **Example following that pattern:** $[3,1,4,2]\rightarrow[3,4,4,6]\rightarrow[3,4,8,10]$. In the second stage, the left total 4 is read by both right-half processors.
>
> **Complexity and memory rule:** This simple broadcast implementation has $\Theta(\log n)$ time with $O(n)$ processors, $\Theta(n\log n)$ work, concurrent reads of shared block totals, and exclusive writes. A work-efficient tree scan can instead achieve $\Theta(n)$ work and logarithmic depth. The note's separate offset-doubling construction has different intermediate arrays; do not mix its trace with this broadcast trace.
>
> **Study:** [[PRAM#Prefix sum]]; [[PRAM#How the work-efficient tree scan works]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

> [!success]- Model answer
> **Suggested exam answer:** In the lecture's broadcast pattern, start with blocks of one input. At each stage, combine adjacent blocks of equal size: the prefixes in the left block stay unchanged, and the total of that left block is added to every local prefix in the right block. Double the block size and synchronize before the next stage. Each stage reads the preceding stage's values; use separate input/output buffers to make that ordering explicit. After $\lceil\log_2 n\rceil$ stages, each position holds its complete prefix. Padding with zeros handles a non-power-of-two length without changing the asymptotic bounds.
>
> **Example following that pattern:** $[3,1,4,2]\rightarrow[3,4,4,6]\rightarrow[3,4,8,10]$. In the second stage, the left total 4 is read by both right-half processors.
>
> **Complexity and memory rule:** This simple broadcast implementation has $\Theta(\log n)$ time with $O(n)$ processors, $\Theta(n\log n)$ work, concurrent reads of shared block totals, and exclusive writes. A work-efficient tree scan can instead achieve $\Theta(n)$ work and logarithmic depth. The note's separate offset-doubling construction has different intermediate arrays; do not mix its trace with this broadcast trace.
>
> **Study:** [[PRAM#Prefix sum]]; [[PRAM#How the work-efficient tree scan works]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

### AAPP-03-004

Please describe how matrix x vector works when a PRAM architecture is considered. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1C · p. 2]]

^aapp-03-004

**My answer**

For a matrix vector multiplication, we need to linearly combine the vector with every single row of the matrix. Since those results are independent we can parallelize that by using concurrent reads and exclusive rights. Each processor takes care of 1 or more, in case p < n, rows of the matrix. That reduces the complexity to O(n/p) compared to n^2.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct decomposition and CREW policy; the time bound is missing a factor of $n$.** There are $n$ independent output rows, but each row needs $n$ products and additions. Assigning $n/p$ rows to a processor therefore requires $\Theta(n^2/p)$ time in the divisible case, rather than $O(n/p)$.
>
> **Suggested exam answer:** For an $n\times n$ matrix and length-$n$ vector, compute $y_i=\sum_{j=0}^{n-1}A_{ij}x_j$. Assign independent rows to processors:
>
> ```text
> parallel for each row i, scheduled over p processors:
>     s = 0                         // private accumulator
>     for j = 0 to n - 1:
>         s = s + A[i,j] * x[j]
>     y[i] = s
> ```
>
> The row-based schedule takes $T_p=\Theta(n\lceil n/p\rceil)$ for $1\le p\le n$, with $W=\Theta(n^2)$. At $p=n$, time is $\Theta(n)$, rather than constant. Processors read distinct matrix rows, may read the same vector element simultaneously, and write distinct outputs: CREW suffices. More than $n$ processors cannot help this unchanged row-only schedule; further parallelism needs a reduction within each row.
>
> **Study:** [[PRAM#Map: matrix-vector multiplication]]; [[PRAM#Worked row decomposition]]; [[lecture4-PRAM.pdf#page=20|slide 20]].

> [!success]- Model answer
> **Suggested exam answer:** For an $n\times n$ matrix and length-$n$ vector, compute $y_i=\sum_{j=0}^{n-1}A_{ij}x_j$. Assign independent rows to processors:
>
> ```text
> parallel for each row i, scheduled over p processors:
>     s = 0                         // private accumulator
>     for j = 0 to n - 1:
>         s = s + A[i,j] * x[j]
>     y[i] = s
> ```
>
> The row-based schedule takes $T_p=\Theta(n\lceil n/p\rceil)$ for $1\le p\le n$, with $W=\Theta(n^2)$. At $p=n$, time is $\Theta(n)$, rather than constant. Processors read distinct matrix rows, may read the same vector element simultaneously, and write distinct outputs: CREW suffices. More than $n$ processors cannot help this unchanged row-only schedule; further parallelism needs a reduction within each row.
>
> **Study:** [[PRAM#Map: matrix-vector multiplication]]; [[PRAM#Worked row decomposition]]; [[lecture4-PRAM.pdf#page=20|slide 20]].

### AAPP-03-005

Please describe how matrix x matrix works when considering a PRAM architecture. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1C · p. 2]]

^aapp-03-005

**My answer**

Answered right above.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: the reference needs correcting: the immediately preceding answer describes matrix–vector multiplication.** The matrix–matrix idea is in 001, whose complexity also needs the correction given there. Matrix–matrix multiplication has $n^2$ dot products, whereas matrix–vector multiplication has $n$.
>
> **Suggested exam answer:** For two $n\times n$ matrices, each output is $C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$. Compute different output entries in parallel, with one private sequential accumulator for each entry and one final writer to $C_{ij}$. This classical method performs $\Theta(n^3)$ work. With $p\le n^2$ processors distributing the $n^2$ output tasks, its time is $\Theta(n\lceil n^2/p\rceil)$. In particular, $n^2$ processors give $\Theta(n)$ time; $n$ processors give $\Theta(n^2)$ time. Reused input entries require concurrent reads in the natural schedule, while output writes are exclusive. Parallel reductions within dot products offer another allocation/time trade-off.
>
> **Pseudocode:** See the corrected explicit algorithm in [[#AAPP-03-001]].
>
> **Study:** [[Divide and Conquer#Matrix multiplication]]; compare [[PRAM#Map: matrix-vector multiplication]].

> [!success]- Model answer
> **Suggested exam answer:** For two $n\times n$ matrices, each output is $C_{ij}=\sum_{k=0}^{n-1}A_{ik}B_{kj}$. Compute different output entries in parallel, with one private sequential accumulator for each entry and one final writer to $C_{ij}$. This classical method performs $\Theta(n^3)$ work. With $p\le n^2$ processors distributing the $n^2$ output tasks, its time is $\Theta(n\lceil n^2/p\rceil)$. In particular, $n^2$ processors give $\Theta(n)$ time; $n$ processors give $\Theta(n^2)$ time. Reused input entries require concurrent reads in the natural schedule, while output writes are exclusive. Parallel reductions within dot products offer another allocation/time trade-off.
>
> **Pseudocode:** See the corrected explicit algorithm in [[#AAPP-03-001]].
>
> **Study:** [[Divide and Conquer#Matrix multiplication]]; compare [[PRAM#Map: matrix-vector multiplication]].

### AAPP-03-006

Why is the prefix sum algorithm on PRAM more efficient than the basic sum algorithm, and what is the trade-off? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1C · p. 2]]

^aapp-03-006

**My answer**

It is more efficient because there are more intermediate operation that use the processors, and less dependency on recutions. Meanwhile with normal sum reduction is the most taxing part and every round the number of unused processors doubles.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: partly correct utilization intuition, but “more efficient” needs a metric and a named algorithm.** A scan can keep more addition tasks active across stages, but extra activity can also mean extra work. Scan computes every prefix; reduction computes one total. A standard tree reduction already has logarithmic depth. Its active processor count halves at each level; the idle count itself does not generally double.
>
> **Suggested exam answer:** Compared with sequential accumulation, a parallel scan replaces a linear dependency chain with logarithmic-depth stages and returns all prefix sums. Compared with a parallel tree reduction, a scan is not inherently faster: both can take $\Theta(\log n)$ time with enough processors, and they produce different outputs. In the lecture's simple broadcast scan, the trade-off is obtaining every prefix through more intermediate operations and concurrent reads: work is $\Theta(n\log n)$, while a tree reduction needs only $\Theta(n)$ work for one total. Better processor utilization alone does not prove lower work or cost.
>
> **Small comparison:** For four inputs, a tree reduction needs three additions. The broadcast scan in 003 needs four additions and returns four prefixes. With eight inputs, that scan performs $4\cdot3=12$ additions, while reduction performs seven.
>
> **Source qualification:** The exam does not define “basic sum” or the efficiency metric. A universal claim that scan beats reduction is therefore unsupported. The extra-work trade-off is specific to the simple scan: a work-efficient tree scan can compute all prefixes with linear work and logarithmic depth, including on EREW. See [Blelloch, *Prefix Sums and Their Applications*, §1.2](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf#page=5).
>
> **Study:** [[PRAM#Reduction]]; [[PRAM#Prefix sum]]; [[PRAM#How the work-efficient tree scan works]]; [[lecture4-PRAM.pdf#page=21|slide 21]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

> [!success]- Model answer
> **Suggested exam answer:** Compared with sequential accumulation, a parallel scan replaces a linear dependency chain with logarithmic-depth stages and returns all prefix sums. Compared with a parallel tree reduction, a scan is not inherently faster: both can take $\Theta(\log n)$ time with enough processors, and they produce different outputs. In the lecture's simple broadcast scan, the trade-off is obtaining every prefix through more intermediate operations and concurrent reads: work is $\Theta(n\log n)$, while a tree reduction needs only $\Theta(n)$ work for one total. Better processor utilization alone does not prove lower work or cost.
>
> **Small comparison:** For four inputs, a tree reduction needs three additions. The broadcast scan in 003 needs four additions and returns four prefixes. With eight inputs, that scan performs $4\cdot3=12$ additions, while reduction performs seven.
>
> **Source qualification:** The exam does not define “basic sum” or the efficiency metric. A universal claim that scan beats reduction is therefore unsupported. The extra-work trade-off is specific to the simple scan: a work-efficient tree scan can compute all prefixes with linear work and logarithmic depth, including on EREW. See [Blelloch, *Prefix Sums and Their Applications*, §1.2](https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf#page=5).
>
> **Study:** [[PRAM#Reduction]]; [[PRAM#Prefix sum]]; [[PRAM#How the work-efficient tree scan works]]; [[lecture4-PRAM.pdf#page=21|slide 21]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

### AAPP-03-007

During the lectures, we discussed how the prefix sum and PRAM memory access enable us to maintain low algorithm complexity. Please discuss what type of PRAM memory accesses are performed. (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=2|2025-11-06-1st · Exercise 1C · p. 2]]

^aapp-03-007

**My answer**

PRAM performs unit time access to any part of memory, all processors can access it at the same time with no networking or bandwidth limit. This allows to abstract away from real systems, where latency bandwidth and other factor are present and it allows to examine how the algorithm scales in a more ideal environment.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct general PRAM idealization, but the algorithm-specific access pattern is missing.** The question asks which reads and writes the prefix algorithm uses. Unit-time access explains their cost; it does not identify which accesses are legal.
>
> **Suggested exam answer:** The lecture's broadcast prefix scan uses concurrent reads and exclusive writes, so CREW suffices. Several processors may read the same left-block total during a stage; for example, the partial sum in cell 2 is read by the processors computing prefixes 3 and 4. Each processor writes its own distinct prefix/output cell. All reads use the preceding stage's values, and the synchronous stage boundary orders the writes before the next stage. Each permitted memory access has unit cost, so the constant-work stages give $\Theta(\log n)$ parallel time with enough processors. No concurrent writes are required.
>
> **Qualification:** This is the access policy of the illustrated broadcast implementation; other scan algorithms can satisfy EREW.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

> [!success]- Model answer
> **Suggested exam answer:** The lecture's broadcast prefix scan uses concurrent reads and exclusive writes, so CREW suffices. Several processors may read the same left-block total during a stage; for example, the partial sum in cell 2 is read by the processors computing prefixes 3 and 4. Each processor writes its own distinct prefix/output cell. All reads use the preceding stage's values, and the synchronous stage boundary orders the writes before the next stage. Each permitted memory access has unit cost, so the constant-work stages give $\Theta(\log n)$ parallel time with enough processors. No concurrent writes are required.
>
> **Qualification:** This is the access policy of the illustrated broadcast implementation; other scan algorithms can satisfy EREW.
>
> **Study:** [[PRAM#Memory-access rules]]; [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

### AAPP-03-008

During the lectures, we discuss how to compute the sum of a collection of integer values in a PRAM model. Could you discuss the conclusions we reached regarding the problem's complexity? (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=2|2026-1-22-1st · Exercise 1C · p. 2]]

^aapp-03-008

**My answer**

The work can be split among many processor, however the final result is still a single value so we need to take the intermidiate results and merge them togheter, that is called reduction. In a normal sum every round we can reduce the sums to half so the algorithm need logn rounds where n is the number of addends. If we don't have p > n for the first round then we need to chunk some operation first so now the complexity is logn + n/p for chunking.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; refine the processor threshold and the chunked reduction term.** Your reduction explanation and logarithmic bound are sound. The first level needs about $n/2$ addition tasks, rather than more than $n$ processors. With chunking, the final tree combines $p$ partial sums, so that phase has $\Theta(\log p)$ time. Your $O(n/p+\log n)$ remains a valid upper bound for $1\le p\le n$; $n/p+\log p$ identifies the two phases more directly.
>
> **Suggested exam answer:** Sequential summation needs $\Theta(n)$ time. A balanced binary reduction combines disjoint pairs at each level, requiring $\Theta(\log n)$ parallel time with $\Theta(n)$ processors and $n-1$ additions in total. For $n$ a power of two, $n/2$ processors suffice for the first level. With $1\le p\le n$, each processor can first sum a chunk of about $n/p$ inputs, then reduce the $p$ partial sums in a tree. This gives $T_p=\Theta(n/p+\log p)$ and $W=\Theta(n)$. If all $p$ processors remain allocated, cost is $\Theta(n+p\log p)$; it includes idle slots during the tree phase. Distinct read operands and write destinations make a properly staged tree reduction EREW.
>
> **Example, counting additions only:** For 16 values and four processors, each four-value chunk needs three additions, then the four partial sums need two tree rounds. Thus $T_4=3+2=5$ addition rounds, while total work is $4\cdot3+3=15$ additions.
>
> **Study:** [[PRAM#Reduction]]; [[PRAM#Chunk first, then reduce]]; [[PRAM#Choosing processors with an exact small model]]; [[lecture4-PRAM.pdf#page=21|slides 21–22]].

> [!success]- Model answer
> **Suggested exam answer:** Sequential summation needs $\Theta(n)$ time. A balanced binary reduction combines disjoint pairs at each level, requiring $\Theta(\log n)$ parallel time with $\Theta(n)$ processors and $n-1$ additions in total. For $n$ a power of two, $n/2$ processors suffice for the first level. With $1\le p\le n$, each processor can first sum a chunk of about $n/p$ inputs, then reduce the $p$ partial sums in a tree. This gives $T_p=\Theta(n/p+\log p)$ and $W=\Theta(n)$. If all $p$ processors remain allocated, cost is $\Theta(n+p\log p)$; it includes idle slots during the tree phase. Distinct read operands and write destinations make a properly staged tree reduction EREW.
>
> **Example, counting additions only:** For 16 values and four processors, each four-value chunk needs three additions, then the four partial sums need two tree rounds. Thus $T_4=3+2=5$ addition rounds, while total work is $4\cdot3+3=15$ additions.
>
> **Study:** [[PRAM#Reduction]]; [[PRAM#Chunk first, then reduce]]; [[PRAM#Choosing processors with an exact small model]]; [[lecture4-PRAM.pdf#page=21|slides 21–22]].

### AAPP-03-009

Please discuss what type of PRAM memory accesses are performed in the vector sum PRAM algorithm. (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=2|2026-9-10-1st · Exercise 1C · p. 2]]

^aapp-03-009

**My answer**

Already answered above.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference, but distinguish a plain vector sum from a prefix scan.** The source says “vector sum” without specifying a schedule. The CREW answer for the broadcast prefix scan should not automatically be applied to a reduction that returns one total.
>
> **Suggested exam answer, interpreting vector sum as $\sum_i a_i$:** A standard pairwise tree reduction can use EREW. At each level, processors handle disjoint pairs of input/partial-sum cells, perform their reads in a constant number of read steps, compute a sum, and write to distinct cells of the next level. No shared cell needs multiple readers or writers in the same access phase. Separate level buffers and synchronous rounds preserve the old values until all needed reads complete. Unit-cost accesses and a logarithmic number of levels give logarithmic parallel time with enough processors.
>
> **Other interpretations:** Elementwise vector addition $c_i=a_i+b_i$ is also naturally EREW with disjoint index assignments. If “vector sum” refers to the broadcast **prefix** algorithm illustrated on slide 23, use the CREW explanation in [[#AAPP-03-007]]: common block totals are read by several processors and each output has one writer. State which operation and schedule you are analyzing; the phrase alone does not determine one access policy.
>
> **Study:** [[PRAM#Reduction]]; [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=21|slide 21]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

> [!success]- Model answer
> **Suggested exam answer, interpreting vector sum as $\sum_i a_i$:** A standard pairwise tree reduction can use EREW. At each level, processors handle disjoint pairs of input/partial-sum cells, perform their reads in a constant number of read steps, compute a sum, and write to distinct cells of the next level. No shared cell needs multiple readers or writers in the same access phase. Separate level buffers and synchronous rounds preserve the old values until all needed reads complete. Unit-cost accesses and a logarithmic number of levels give logarithmic parallel time with enough processors.
>
> **Other interpretations:** Elementwise vector addition $c_i=a_i+b_i$ is also naturally EREW with disjoint index assignments. If “vector sum” refers to the broadcast **prefix** algorithm illustrated on slide 23, use the CREW explanation in [[#AAPP-03-007]]: common block totals are read by several processors and each output has one writer. State which operation and schedule you are analyzing; the phrase alone does not determine one access policy.
>
> **Study:** [[PRAM#Reduction]]; [[PRAM#Prefix sum]]; [[lecture4-PRAM.pdf#page=21|slide 21]]; [[lecture4-PRAM.pdf#page=23|slide 23]].

## Divide and conquer and recurrences

Related notes: [[Divide and Conquer]].

### AAPP-04-001

Describe how divide and conquer work with some examples and why master theorem method matter.

Source: [[Tema Esame 2022-06-09-1st.pdf#page=2|2022-06-09-1st · Exercise 1 · p. 2]]

^aapp-04-001

**My answer**

The divide and conquer is a strategy for solving certain problems. It consists of take an initial big problem and divide it in smaller subproblems, then solve those or split those as well. For example this is the principle behind binary search, start with a big list, and split it then search among those lists. But those list can also be split again. Another example can be powering a number, matrix multiplication or H tree embedding. The reason master theorem is very important is that with this divide and conquer approches we usually take an initial complexity T(n) and obtain a fraction of that for multiple subproblems, aT(n/b) plus a fixed cost operation usually. That is exactly what the master theorem is able to solve and so it provides a simple way of analyzing the complexity of the divide and conquer approach.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; add combination and refine the recurrence explanation.** Your examples and the connection to recurrences are sound. Divide and conquer also needs base cases and a rule for combining subproblem solutions. In binary search, the array must be sorted and only one of the two possible halves is searched. The nonrecursive cost $f(n)$ need not be constant: merging or adding matrix blocks can take growing time.
>
> **Suggested exam answer:** Divide and conquer divides an instance into smaller subproblems, solves them recursively until base cases are reached, and combines their solutions. Merge sort solves both halves and merges them, giving $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$. Binary search follows only one half of a sorted array, giving worst-case $T(n)=T(n/2)+\Theta(1)=\Theta(\log n)$ when using indices. Many balanced algorithms yield $T(n)=aT(n/b)+f(n)$, where $a$ counts recursive calls, $n/b$ is their size, and $f(n)$ counts work outside recursion. The Master theorem quickly solves recurrences that meet its assumptions and one of its cases; it does not apply to every divide-and-conquer algorithm.
>
> **Study:** [[Divide and Conquer#Overview]]; [[Divide and Conquer#Binary search]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=2|slide 2]].

> [!success]- Model answer
> **Suggested exam answer:** Divide and conquer divides an instance into smaller subproblems, solves them recursively until base cases are reached, and combines their solutions. Merge sort solves both halves and merges them, giving $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$. Binary search follows only one half of a sorted array, giving worst-case $T(n)=T(n/2)+\Theta(1)=\Theta(\log n)$ when using indices. Many balanced algorithms yield $T(n)=aT(n/b)+f(n)$, where $a$ counts recursive calls, $n/b$ is their size, and $f(n)$ counts work outside recursion. The Master theorem quickly solves recurrences that meet its assumptions and one of its cases; it does not apply to every divide-and-conquer algorithm.
>
> **Study:** [[Divide and Conquer#Overview]]; [[Divide and Conquer#Binary search]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=2|slide 2]].

### AAPP-04-002

Please describe how the Divide and Conquer class of algorithms works. (2)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=3|2023-02-14-1st · Exercise 2A · p. 3]]

^aapp-04-002

**My answer**

Answer above should be enough.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; the main idea in 001 is correct with the additions noted there.** A self-contained definition should state all three stages and the base case.
>
> **Suggested exam answer:** Divide and conquer has three stages: divide an instance into smaller instances of the same problem, conquer by solving them recursively, and combine their answers. Directly solve sufficiently small instances as base cases. Recursive arguments must shrink so the algorithm terminates, and the combination rule must produce a correct solution. For example, merge sort recursively sorts two halves and merges the sorted results. Splitting a problem is useful only if the resulting recursion and combination costs are favorable.
>
> **Study:** [[Divide and Conquer#Overview]]; [[Divide and Conquer#From a recursive specification to a proof]]; [[lecture3-DandC.pdf#page=2|slide 2]].

> [!success]- Model answer
> **Suggested exam answer:** Divide and conquer has three stages: divide an instance into smaller instances of the same problem, conquer by solving them recursively, and combine their answers. Directly solve sufficiently small instances as base cases. Recursive arguments must shrink so the algorithm terminates, and the combination rule must produce a correct solution. For example, merge sort recursively sorts two halves and merges the sorted results. Splitting a problem is useful only if the resulting recursion and combination costs are favorable.
>
> **Study:** [[Divide and Conquer#Overview]]; [[Divide and Conquer#From a recursive specification to a proof]]; [[lecture3-DandC.pdf#page=2|slide 2]].

### AAPP-04-003

How the complexity of a Divide and Conquer algorithm can be computed? (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=3|2023-02-14-1st · Exercise 2B · p. 3]]

^aapp-04-003

**My answer**

Answer above should be enough.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; explicitly show how the cost recurrence is built.** A recurrence describes the actual recursive calls and the nonrecursive work, rather than dividing an already-known complexity by the number of pieces.
>
> **Suggested exam answer:** Specify the input-size measure and base-case cost, count the recursive calls and their sizes, and add the divide/combine work. For $a$ equal-size calls on size $n/b$, sequential time satisfies $T(n)=aT(n/b)+f(n)$ with a constant-size base case. Identify $a,b,f(n)$, check the Master theorem's assumptions and case conditions, and solve it. If they fail, use a recursion tree, substitution, or another suitable method. For merge sort, $a=b=2$ and $f(n)=\Theta(n)$, giving $\Theta(n\log n)$. Count calls actually executed: binary search uses one half, not both.
>
> **Study:** [[Algorithm as recipes#Solving recurrences]]; [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Merge sort as the template]].

> [!success]- Model answer
> **Suggested exam answer:** Specify the input-size measure and base-case cost, count the recursive calls and their sizes, and add the divide/combine work. For $a$ equal-size calls on size $n/b$, sequential time satisfies $T(n)=aT(n/b)+f(n)$ with a constant-size base case. Identify $a,b,f(n)$, check the Master theorem's assumptions and case conditions, and solve it. If they fail, use a recursion tree, substitution, or another suitable method. For merge sort, $a=b=2$ and $f(n)=\Theta(n)$, giving $\Theta(n\log n)$. Count calls actually executed: binary search uses one half, not both.
>
> **Study:** [[Algorithm as recipes#Solving recurrences]]; [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Merge sort as the template]].

### AAPP-04-004

Please discuss the complexity of the “Powering a number” algorithm. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=3|2023-02-14-1st · Exercise 2C · p. 3]]
Source: [[Tema Esame 2026-6-29-1st.pdf#page=3|2026-6-29-1st · Exercise 2B · p. 3]]

^aapp-04-004

**My answer**

When power a number we can, instead of power of n, multiply together the two n/2 powers. By doing so since the two sides are the same number we only have to compute one and then multiply by itself. We can keep applying this for multiple levels until we reach exponent 1. The complexity is O(logn) because starting from n we halve it every time until we reach 1.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct central argument; add odd exponents, a base case, and the cost model.** You correctly explain that the equal half-power must be computed once and reused. An exponent is not always even, so halving needs a floor and sometimes one extra multiplication.
>
> **Suggested exam answer:** To compute $x^n$ for a nonnegative integer $n$, return 1 at $n=0$. Otherwise compute $y=x^{\lfloor n/2\rfloor}$ recursively once. Return $y^2$ for even $n$ and $xy^2$ for odd $n$. Thus $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ for growing positive $n$, counting arithmetic at unit cost. Repeated multiplication takes $\Theta(n)$ operations. Calling the half-power routine twice would instead give $2T(n/2)+\Theta(1)=\Theta(n)$ and lose the improvement. Exact large-integer bit complexity requires a separate analysis.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

> [!success]- Model answer
> **Suggested exam answer:** To compute $x^n$ for a nonnegative integer $n$, return 1 at $n=0$. Otherwise compute $y=x^{\lfloor n/2\rfloor}$ recursively once. Return $y^2$ for even $n$ and $xy^2$ for odd $n$. Thus $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ for growing positive $n$, counting arithmetic at unit cost. Repeated multiplication takes $\Theta(n)$ operations. Calling the half-power routine twice would instead give $2T(n/2)+\Theta(1)=\Theta(n)$ and lose the improvement. Exact large-integer bit complexity requires a separate analysis.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

### AAPP-04-005

Please describe how Strassen’s algorithm works. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=3|2023-06-19-1st · Exercise 2A · p. 3]]

^aapp-04-005

**My answer**

Strassen algorithm is a way to apply divide and conquer to matrix multiplication in order to obtain a smaller complexity. What it does is divide the starting matrices in certain block. For 2x2 matrix it reduces the recursive multiplications from 8 to 7 by performing some more blocks addition and subtraction. It need a further step to reconstruct the real output from the obtained values. The original complexity would be O(n^3) while Strassen achieves O(n^2.8), which is marginally better, but for big matrix it can matter a lot.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct mechanism; use the exact exponent and explain the recursive saving.** You correctly identify seven recursive products, additional additions/subtractions, and reconstruction. The improvement repeats at every level. Formally, $O(n^{2.8})$ is too small: $\log_2 7\approx2.8073549>2.8$. Use $\Theta(n^{\log_2 7})$, or give 2.807 as an approximate exponent.
>
> **Suggested exam answer:** Strassen is a divide-and-conquer matrix-multiplication algorithm. Partition each $n\times n$ input into four $(n/2)\times(n/2)$ blocks. Ordinary block multiplication uses eight recursive products; Strassen uses seven specially chosen products and reconstructs the four output blocks through additions and subtractions. With the lecture's block names $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ and $B=\begin{pmatrix}e&f\\g&h\end{pmatrix}$, compute
>
> $$
> \begin{aligned}
> P_1&=a(f-h),&P_2&=(a+b)h,\\
> P_3&=(c+d)e,&P_4&=d(g-e),\\
> P_5&=(a+d)(e+h),&P_6&=(b-d)(g+h),\\
> P_7&=(a-c)(e+f).
> \end{aligned}
> $$
>
> Then $C_{11}=P_5+P_4-P_2+P_6$, $C_{12}=P_1+P_2$, $C_{21}=P_3+P_4$, and $C_{22}=P_5+P_1-P_3-P_7$. Recursively apply the same method down to a small base case. The block additions cost $\Theta(n^2)$ per call, yielding $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$, compared with $\Theta(n^3)$ for the classical method. Extra constants and storage affect practical performance, so a smaller exponent does not guarantee an advantage for every matrix size.
>
> **Study:** [[Divide and Conquer#Strassen's algorithm]]; [[Divide and Conquer#Complexity]]; [[Divide and Conquer#Why saving one product compounds]]; [[lecture3-DandC.pdf#page=29|slides 29–38]].

> [!success]- Model answer
> **Suggested exam answer:** Strassen is a divide-and-conquer matrix-multiplication algorithm. Partition each $n\times n$ input into four $(n/2)\times(n/2)$ blocks. Ordinary block multiplication uses eight recursive products; Strassen uses seven specially chosen products and reconstructs the four output blocks through additions and subtractions. With the lecture's block names $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ and $B=\begin{pmatrix}e&f\\g&h\end{pmatrix}$, compute
>
> $$
> \begin{aligned}
> P_1&=a(f-h),&P_2&=(a+b)h,\\
> P_3&=(c+d)e,&P_4&=d(g-e),\\
> P_5&=(a+d)(e+h),&P_6&=(b-d)(g+h),\\
> P_7&=(a-c)(e+f).
> \end{aligned}
> $$
>
> Then $C_{11}=P_5+P_4-P_2+P_6$, $C_{12}=P_1+P_2$, $C_{21}=P_3+P_4$, and $C_{22}=P_5+P_1-P_3-P_7$. Recursively apply the same method down to a small base case. The block additions cost $\Theta(n^2)$ per call, yielding $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$, compared with $\Theta(n^3)$ for the classical method. Extra constants and storage affect practical performance, so a smaller exponent does not guarantee an advantage for every matrix size.
>
> **Study:** [[Divide and Conquer#Strassen's algorithm]]; [[Divide and Conquer#Complexity]]; [[Divide and Conquer#Why saving one product compounds]]; [[lecture3-DandC.pdf#page=29|slides 29–38]].

### AAPP-04-006

Why is the Master Theorem method frequently used to evaluate the asymptotic complexity of a Divide and Conquer algorithm can be computed? (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=3|2023-06-19-1st · Exercise 2B · p. 3]]

^aapp-04-006

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; explain the recurrence structure and the theorem's limits.** Your first answer identifies the main reason for using it, with the correction that divide/combine cost is a function $f(n)$ and can grow with $n$.
>
> **Suggested exam answer:** Many divide-and-conquer runtimes have the form $T(n)=aT(n/b)+f(n)$: $a$ recursive calls on equal reduced sizes and nonrecursive divide/combine cost $f(n)$. The Master theorem compares $f(n)$ with $n^{\log_b a}$ and gives an asymptotic bound without expanding every recursion level. It requires constants $a\ge1$, $b>1$, an eventually positive cost, suitable base cases, and one of the theorem's case conditions. Polynomial separation is required in Cases 1 and 3, and Case 3 also needs regularity. Other recurrences require another analysis method.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Algorithm as recipes#Reading a recursion tree level by level]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].

> [!success]- Model answer
> **Suggested exam answer:** Many divide-and-conquer runtimes have the form $T(n)=aT(n/b)+f(n)$: $a$ recursive calls on equal reduced sizes and nonrecursive divide/combine cost $f(n)$. The Master theorem compares $f(n)$ with $n^{\log_b a}$ and gives an asymptotic bound without expanding every recursion level. It requires constants $a\ge1$, $b>1$, an eventually positive cost, suitable base cases, and one of the theorem's case conditions. Polynomial separation is required in Cases 1 and 3, and Case 3 also needs regularity. Other recurrences require another analysis method.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Algorithm as recipes#Reading a recursion tree level by level]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].

### AAPP-04-007

Please discuss how the complexity of the powering of a number algorithm can be computed. Please report also the complexity in terms of time and space. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=3|2023-07-11-1st · Exercise 2A · p. 3]]

^aapp-04-007

**My answer**

Already answered above. For space i am not sure.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: the time argument is correct by reference to 004; space was missing.** Count the live recursion frames, not the total number of multiplications, and state whether the implementation is recursive or iterative.
>
> **Suggested exam answer:** Compute $y=x^{\lfloor n/2\rfloor}$ once, then return $y^2$ or $xy^2$ according to the parity of $n$, with $x^0=1$. The time recurrence is $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$, giving $\Theta(\log n)$ unit-cost arithmetic operations. The ordinary recursive implementation has $\Theta(\log n)$ nested calls and a constant number of words per frame, so auxiliary stack space is $\Theta(\log n)$. Equivalently, $S(n)=S(\lfloor n/2\rfloor)+\Theta(1)$. An iterative exponentiation-by-squaring implementation uses $\Theta(1)$ auxiliary words while retaining logarithmic arithmetic-operation count. These space bounds use the course's word model and exclude input/output storage; they do not assert constant-bit storage for arbitrarily large powers.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[Divide and Conquer#Following the calls and returns of POWER]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

> [!success]- Model answer
> **Suggested exam answer:** Compute $y=x^{\lfloor n/2\rfloor}$ once, then return $y^2$ or $xy^2$ according to the parity of $n$, with $x^0=1$. The time recurrence is $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$, giving $\Theta(\log n)$ unit-cost arithmetic operations. The ordinary recursive implementation has $\Theta(\log n)$ nested calls and a constant number of words per frame, so auxiliary stack space is $\Theta(\log n)$. Equivalently, $S(n)=S(\lfloor n/2\rfloor)+\Theta(1)$. An iterative exponentiation-by-squaring implementation uses $\Theta(1)$ auxiliary words while retaining logarithmic arithmetic-operation count. These space bounds use the course's word model and exclude input/output storage; they do not assert constant-bit storage for arbitrarily large powers.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[Divide and Conquer#Following the calls and returns of POWER]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

### AAPP-04-008

Please discuss the cases the master theorem solves and under which assumption the theorem holds. Apply then to the binary search algorithm. Is the master theorem of any help in case we would like to estimate the spatial complexity of an algorithm? (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=3|2023-09-11-1st · Exercise 2A · p. 3]]

^aapp-04-008

**My answer**

Master theorem solves the complexity for problems that look like this:
T(n) = aT(n/b) + f(n) where multiple sub-tasks are computed plus a fixed amount f. It compares $n^{\log_{b}a}$ to f(n) and based on 3 cases of asysntotic comparison, it directly gives a value to the complexity, which can be just f(n) or $n^{\log_{b}a}$ or $n^{\log_{b}a}(\log n)^{k+1}$.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct reference term and result shapes, but substantial parts are missing.** State the exact case conditions, apply them to binary search, and answer the space question. $f(n)$ is nonrecursive cost, which need not be fixed or constant.
>
> **Suggested exam answer — theorem:** For $T(n)=aT(n/b)+f(n)$ with constants $a\ge1$, $b>1$, constant-size base cases, and eventually positive $f(n)$, put $d=\log_b a$. In the form used in the notes:
>
> 1. If $f(n)=O(n^{d-\varepsilon})$ for some constant $\varepsilon>0$, then $T(n)=\Theta(n^d)$.
> 2. If $f(n)=\Theta(n^d\log^k n)$ for a constant $k\ge0$, then $T(n)=\Theta(n^d\log^{k+1}n)$.
> 3. If $f(n)=\Omega(n^{d+\varepsilon})$ for some constant $\varepsilon>0$ and $af(n/b)\le cf(n)$ for some constant $0<c<1$ and all sufficiently large $n$, then $T(n)=\Theta(f(n))$.
>
> The outer cases require a polynomial gap, rather than merely being smaller or larger. The recurrence has equal-size subproblems, up to standard floor/ceiling rounding. Some recurrences satisfy none of these cases. This statement matches [MIT's Master theorem sheet](https://people.csail.mit.edu/thies/6.046-web/master.pdf#page=1).
>
> **Application to binary search:** For a sorted array represented by index bounds, only one half is searched. Worst-case $T(n)=T(n/2)+\Theta(1)$ has $a=1,b=2,d=0$ and $f(n)=\Theta(1)=\Theta(n^0\log^0 n)$. Case 2 gives $\Theta(\log n)$ time. The best case is constant time if the first midpoint matches.
>
> **Space or spatial complexity:** The theorem solves suitable recurrences for other resources too, but first derive the right recurrence. Recursive index-based binary search has $S(n)=S(n/2)+\Theta(1)=\Theta(\log n)$ stack words; an iterative version needs $\Theta(1)$ auxiliary words. Sequential sibling calls can reuse storage, so peak space does not automatically add their space costs. For the lecture's geometric example, H-tree side length satisfies $L(n)=2L(n/4)+\Theta(1)=\Theta(\sqrt n)$, and its area is $L(n)^2=\Theta(n)$. The side-length result must be squared to obtain area.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Binary search]]; [[Divide and Conquer#H-tree layout]]; [[lecture3-DandC.pdf#page=5|slides 5–7]]; [[lecture3-DandC.pdf#page=46|slide 46]].

> [!success]- Model answer
> **Suggested exam answer — theorem:** For $T(n)=aT(n/b)+f(n)$ with constants $a\ge1$, $b>1$, constant-size base cases, and eventually positive $f(n)$, put $d=\log_b a$. In the form used in the notes:
>
> 1. If $f(n)=O(n^{d-\varepsilon})$ for some constant $\varepsilon>0$, then $T(n)=\Theta(n^d)$.
> 2. If $f(n)=\Theta(n^d\log^k n)$ for a constant $k\ge0$, then $T(n)=\Theta(n^d\log^{k+1}n)$.
> 3. If $f(n)=\Omega(n^{d+\varepsilon})$ for some constant $\varepsilon>0$ and $af(n/b)\le cf(n)$ for some constant $0<c<1$ and all sufficiently large $n$, then $T(n)=\Theta(f(n))$.
>
> The outer cases require a polynomial gap, rather than merely being smaller or larger. The recurrence has equal-size subproblems, up to standard floor/ceiling rounding. Some recurrences satisfy none of these cases. This statement matches [MIT's Master theorem sheet](https://people.csail.mit.edu/thies/6.046-web/master.pdf#page=1).
>
> **Application to binary search:** For a sorted array represented by index bounds, only one half is searched. Worst-case $T(n)=T(n/2)+\Theta(1)$ has $a=1,b=2,d=0$ and $f(n)=\Theta(1)=\Theta(n^0\log^0 n)$. Case 2 gives $\Theta(\log n)$ time. The best case is constant time if the first midpoint matches.
>
> **Space or spatial complexity:** The theorem solves suitable recurrences for other resources too, but first derive the right recurrence. Recursive index-based binary search has $S(n)=S(n/2)+\Theta(1)=\Theta(\log n)$ stack words; an iterative version needs $\Theta(1)$ auxiliary words. Sequential sibling calls can reuse storage, so peak space does not automatically add their space costs. For the lecture's geometric example, H-tree side length satisfies $L(n)=2L(n/4)+\Theta(1)=\Theta(\sqrt n)$, and its area is $L(n)^2=\Theta(n)$. The side-length result must be squared to obtain area.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Binary search]]; [[Divide and Conquer#H-tree layout]]; [[lecture3-DandC.pdf#page=5|slides 5–7]]; [[lecture3-DandC.pdf#page=46|slide 46]].

### AAPP-04-009

Please describe the divide and conquer powering of a number algorithm. What complexity does it have? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=3|2024-02-16-1st · Exercise 2C · p. 3]]

^aapp-04-009

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 004; include the odd case and reuse rule.** The logarithmic bound depends on making one recursive call per level.
>
> **Suggested exam answer:** To compute $x^n$, return 1 when $n=0$; otherwise recursively compute $y=x^{\lfloor n/2\rfloor}$ once and reuse it. Return $y^2$ for even $n$, or $xy^2$ for odd $n$. The exponent halves at each level and combination uses at most two multiplications, so $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ under unit-cost arithmetic. Recursively computing the two equal half-powers separately would require linear arithmetic work instead.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

> [!success]- Model answer
> **Suggested exam answer:** To compute $x^n$, return 1 when $n=0$; otherwise recursively compute $y=x^{\lfloor n/2\rfloor}$ once and reuse it. Return $y^2$ for even $n$, or $xy^2$ for odd $n$. The exponent halves at each level and combination uses at most two multiplications, so $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ under unit-cost arithmetic. Recursively computing the two equal half-powers separately would require linear arithmetic work instead.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

### AAPP-04-010

Please list the condition under which the Master Theorem can be used to compute the complexity of an algorithm. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=3|2024-06-26-1st · Exercise 2C · p. 3]]

^aapp-04-010

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference, but the earlier answer did not list the required conditions.** “It looks like $aT(n/b)+f(n)$” alone is insufficient: the constants, cost assumptions, and a valid case must also be checked.
>
> **Suggested exam answer:** Use a recurrence $T(n)=aT(n/b)+f(n)$ with fixed constants $a\ge1$ and $b>1$, eventually positive nonrecursive cost $f(n)$, and constant-size base cases. Subproblems have the same size $n/b$, allowing ordinary floor/ceiling rounding. With $d=\log_b a$, establish either a polynomially smaller $f(n)$, the boundary form $f(n)=\Theta(n^d\log^k n)$ with constant $k\ge0$, or a polynomially larger $f(n)$ satisfying regularity $af(n/b)\le cf(n)$ for some $0<c<1$ eventually. If no case applies, this version of the theorem gives no result. Unequal recursive sizes or a nonconstant $a$ do not fit this standard form directly.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; full cases in [[#AAPP-04-008]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].

> [!success]- Model answer
> **Suggested exam answer:** Use a recurrence $T(n)=aT(n/b)+f(n)$ with fixed constants $a\ge1$ and $b>1$, eventually positive nonrecursive cost $f(n)$, and constant-size base cases. Subproblems have the same size $n/b$, allowing ordinary floor/ceiling rounding. With $d=\log_b a$, establish either a polynomially smaller $f(n)$, the boundary form $f(n)=\Theta(n^d\log^k n)$ with constant $k\ge0$, or a polynomially larger $f(n)$ satisfying regularity $af(n/b)\le cf(n)$ for some $0<c<1$ eventually. If no case applies, this version of the theorem gives no result. Unequal recursive sizes or a nonconstant $a$ do not fit this standard form directly.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; full cases in [[#AAPP-04-008]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].

### AAPP-04-011

Please discuss the cases the master theorem solves and under which assumption the theorem holds. Apply then to the powering algorithm. Is the master theorem of any help if we would like to estimate the spatial complexity of an algorithm? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=3|2024-07-24-1st · Exercise 2A · p. 3]]

^aapp-04-011

**My answer**

Already answered above. For the powering, we start from a^n, then we divide in $a^{n/2}\cdot a^{n/2}$ if even or $a^{n-1/2}\cdot a^{n-1/2} \cdot a$  if odd. The complexity for a normal powering is O(n) while now T(n) = 1T(n/2) + O(1) so a=1 and b=2. We compare n^0 to 1 which is the same so we take the complexity O(n^0logn) = O(logn).

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct recurrence and Case 2 application; fix the odd exponent and complete the theorem/space discussion.** For odd $n$, use $(n-1)/2$, not $n-1/2$. Those expressions differ: with $n=5$, the former is 2 and the latter 4.5. Compute the half-power once. Your $a=1$, $b=2$ analysis correctly counts that single recursive call.
>
> **Suggested exam answer:** The Master theorem uses $T(n)=aT(n/b)+f(n)$ with constants $a\ge1,b>1$, eventually positive $f(n)$, and suitable constant-size base cases. Put $d=\log_b a$. Case 1 requires $f(n)=O(n^{d-\varepsilon})$ and gives $\Theta(n^d)$. Case 2 has $f(n)=\Theta(n^d\log^k n)$, $k\ge0$, and gives $\Theta(n^d\log^{k+1}n)$. Case 3 requires $f(n)=\Omega(n^{d+\varepsilon})$ and regularity $af(n/b)\le cf(n)$ eventually, for constants $\varepsilon>0$ and $0<c<1$; it gives $\Theta(f(n))$.
>
> **Powering:** Use $x^0=1$ and $x^n=(x^{n/2})^2$ for even $n$, or $x^n=x(x^{(n-1)/2})^2$ for odd $n$. Reusing the recursive result gives $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. Here $d=\log_2 1=0$, so Case 2 with $k=0$ gives $\Theta(\log n)$ unit-cost time.
>
> **Space:** Yes, the theorem can help when a correctly derived space recurrence has the required form. Ordinary recursive powering has $S(n)=S(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ auxiliary stack words. The iterative version uses $\Theta(1)$ auxiliary words. This must be analyzed separately from time. For geometric spatial complexity, the lecture's H-tree similarly uses $L(n)=2L(n/4)+\Theta(1)$ for side length and then squares the result to get linear area.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Exponentiation by squaring]]; [[Divide and Conquer#H-tree layout]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

> [!success]- Model answer
> **Suggested exam answer:** The Master theorem uses $T(n)=aT(n/b)+f(n)$ with constants $a\ge1,b>1$, eventually positive $f(n)$, and suitable constant-size base cases. Put $d=\log_b a$. Case 1 requires $f(n)=O(n^{d-\varepsilon})$ and gives $\Theta(n^d)$. Case 2 has $f(n)=\Theta(n^d\log^k n)$, $k\ge0$, and gives $\Theta(n^d\log^{k+1}n)$. Case 3 requires $f(n)=\Omega(n^{d+\varepsilon})$ and regularity $af(n/b)\le cf(n)$ eventually, for constants $\varepsilon>0$ and $0<c<1$; it gives $\Theta(f(n))$.
>
> **Powering:** Use $x^0=1$ and $x^n=(x^{n/2})^2$ for even $n$, or $x^n=x(x^{(n-1)/2})^2$ for odd $n$. Reusing the recursive result gives $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. Here $d=\log_2 1=0$, so Case 2 with $k=0$ gives $\Theta(\log n)$ unit-cost time.
>
> **Space:** Yes, the theorem can help when a correctly derived space recurrence has the required form. Ordinary recursive powering has $S(n)=S(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ auxiliary stack words. The iterative version uses $\Theta(1)$ auxiliary words. This must be analyzed separately from time. For geometric spatial complexity, the lecture's H-tree similarly uses $L(n)=2L(n/4)+\Theta(1)$ for side length and then squares the result to get linear area.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Exponentiation by squaring]]; [[Divide and Conquer#H-tree layout]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

### AAPP-04-012

Please discuss the types of problems that the master theorem can solve and the assumptions under which the theorem holds. Apply the theorem to the matrix multiplication algorithm and explain why Strassen’s version is more efficient. (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=3|2024-09-05-1st · Exercise 2A · p. 3]]

^aapp-04-012

**My answer**

Already answered above. For the matrix multiplication the result is the same as the naive version

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct for ordinary block multiplication, but the Strassen comparison and recurrence analysis are missing.** Ordinary divide-and-conquer multiplication has the same cubic order as the triple loop. Strassen changes the number of recursive products, so its asymptotic bound differs.
>
> **Suggested exam answer:** The Master theorem applies to balanced recurrences $T(n)=aT(n/b)+f(n)$ with constant $a\ge1,b>1$, positive nonrecursive cost, appropriate base cases, and one of its valid case conditions. Ordinary multiplication partitions each matrix into four quadrants, but each output block needs two products: eight recursive multiplications overall. Thus $T(n)=8T(n/2)+\Theta(n^2)$. Since $d=\log_2 8=3$ and $f(n)=\Theta(n^2)$ is polynomially smaller, Case 1 gives $\Theta(n^3)$.
>
> Strassen uses seven recursive products and extra block additions/subtractions, giving $T(n)=7T(n/2)+\Theta(n^2)$. Now $d=\log_2 7\approx2.807>2$, so Case 1 gives $\Theta(n^{\log_2 7})$. The saving compounds across recursion levels. These are arithmetic-operation bounds; merely partitioning into quadrants does not produce the improved exponent.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Ordinary block recursion]]; [[Divide and Conquer#Complexity]]; [[lecture3-DandC.pdf#page=23|slide 23]]; [[lecture3-DandC.pdf#page=38|slide 38]].

> [!success]- Model answer
> **Suggested exam answer:** The Master theorem applies to balanced recurrences $T(n)=aT(n/b)+f(n)$ with constant $a\ge1,b>1$, positive nonrecursive cost, appropriate base cases, and one of its valid case conditions. Ordinary multiplication partitions each matrix into four quadrants, but each output block needs two products: eight recursive multiplications overall. Thus $T(n)=8T(n/2)+\Theta(n^2)$. Since $d=\log_2 8=3$ and $f(n)=\Theta(n^2)$ is polynomially smaller, Case 1 gives $\Theta(n^3)$.
>
> Strassen uses seven recursive products and extra block additions/subtractions, giving $T(n)=7T(n/2)+\Theta(n^2)$. Now $d=\log_2 7\approx2.807>2$, so Case 1 gives $\Theta(n^{\log_2 7})$. The saving compounds across recursion levels. These are arithmetic-operation bounds; merely partitioning into quadrants does not produce the improved exponent.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[Divide and Conquer#Ordinary block recursion]]; [[Divide and Conquer#Complexity]]; [[lecture3-DandC.pdf#page=23|slide 23]]; [[lecture3-DandC.pdf#page=38|slide 38]].

### AAPP-04-013

Master Theorem method is an important tool for the Divide and Conquer class of algorithms. Why and under which assumptions the theorem could be applied? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=3|2024-11-12-1st · Exercise 2B · p. 3]]

^aapp-04-013

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; give both the usefulness and the assumptions explicitly.** The principle in 001 is sound, but the restrictions should be stated.
>
> **Suggested exam answer:** Divide-and-conquer algorithms often generate $T(n)=aT(n/b)+f(n)$, with a fixed number of equal-size smaller calls plus divide/combine work. The Master theorem compares $f(n)$ with $n^{\log_b a}$ and quickly yields an asymptotic bound when a case applies. It assumes constant $a\ge1,b>1$, eventually positive cost, and suitable base cases. Cases 1 and 3 require polynomial separation; Case 3 additionally requires $af(n/b)\le cf(n)$ for some $c<1$ eventually. The boundary case covers $f(n)=\Theta(n^{\log_b a}\log^k n)$ for $k\ge0$. Other recurrences need another method.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].

> [!success]- Model answer
> **Suggested exam answer:** Divide-and-conquer algorithms often generate $T(n)=aT(n/b)+f(n)$, with a fixed number of equal-size smaller calls plus divide/combine work. The Master theorem compares $f(n)$ with $n^{\log_b a}$ and quickly yields an asymptotic bound when a case applies. It assumes constant $a\ge1,b>1$, eventually positive cost, and suitable base cases. Cases 1 and 3 require polynomial separation; Case 3 additionally requires $af(n/b)\le cf(n)$ for some $c<1$ eventually. The boundary case covers $f(n)=\Theta(n^{\log_b a}\log^k n)$ for $k\ge0$. Other recurrences need another method.
>
> **Study:** [[Algorithm as recipes#Master theorem]]; [[lecture2-AlgorithmAsRecipe.pdf#page=18|slides 18–21]].

### AAPP-04-014

Could you please describe how the Strassen algorithm improves matrix multiplication? Additionally, which class of algorithms does the Strassen approach belong to? (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=3|2025-01-24-1st · Exercise 2A · p. 3]]

^aapp-04-014

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 005; the class is divide and conquer.** Use the corrected exponent and identify how the seven-product saving is repeated recursively.
>
> **Suggested exam answer:** Strassen belongs to divide and conquer. It splits two square matrices into quadrants, recursively computes seven products of chosen sums/differences of those blocks, and combines the products to reconstruct the output quadrants. Ordinary block multiplication uses eight recursive products. The extra additions and subtractions still cost $\Theta(n^2)$ per call, giving $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$, compared with classical $\Theta(n^3)$ time. Its smaller exponent provides an asymptotic improvement, while practical crossover depends on implementation costs.
>
> **Study:** [[Divide and Conquer#Strassen's algorithm]]; [[Divide and Conquer#Complexity]]; product formulas in [[#AAPP-04-005]]; [[lecture3-DandC.pdf#page=29|slides 29–38]].

> [!success]- Model answer
> **Suggested exam answer:** Strassen belongs to divide and conquer. It splits two square matrices into quadrants, recursively computes seven products of chosen sums/differences of those blocks, and combines the products to reconstruct the output quadrants. Ordinary block multiplication uses eight recursive products. The extra additions and subtractions still cost $\Theta(n^2)$ per call, giving $T(n)=7T(n/2)+\Theta(n^2)=\Theta(n^{\log_2 7})$, compared with classical $\Theta(n^3)$ time. Its smaller exponent provides an asymptotic improvement, while practical crossover depends on implementation costs.
>
> **Study:** [[Divide and Conquer#Strassen's algorithm]]; [[Divide and Conquer#Complexity]]; product formulas in [[#AAPP-04-005]]; [[lecture3-DandC.pdf#page=29|slides 29–38]].

### AAPP-04-015

Could you please describe how the powering algorithm works? Additionally, which class of algorithms does it belong to? (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=3|2025-02-14-1st · Exercise 2A · p. 3]]

^aapp-04-015

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 004; explicitly name divide and conquer and handle both parities.** One recursive subproblem still fits the course's divide-and-conquer classification.
>
> **Suggested exam answer:** Exponentiation by squaring is a divide-and-conquer algorithm. For $x^n$, stop at $n=0$ with result 1. Compute the smaller power $y=x^{\lfloor n/2\rfloor}$ once, then combine it as $y^2$ for even $n$ or $xy^2$ for odd $n$. The recursive exponent halves and combination takes constant arithmetic work, so $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ under the unit-cost model. Reusing $y$ is essential; the repeated equal factor is not a second required recursive call.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

> [!success]- Model answer
> **Suggested exam answer:** Exponentiation by squaring is a divide-and-conquer algorithm. For $x^n$, stop at $n=0$ with result 1. Compute the smaller power $y=x^{\lfloor n/2\rfloor}$ once, then combine it as $y^2$ for even $n$ or $xy^2$ for odd $n$. The recursive exponent halves and combination takes constant arithmetic work, so $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)=\Theta(\log n)$ under the unit-cost model. Reusing $y$ is essential; the repeated equal factor is not a second required recursive call.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[lecture3-DandC.pdf#page=17|slides 17–19]].

### AAPP-04-016

Please describe how the Divide and Conquer class of algorithms works by using one of the algorithms presented in class. (2)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=3|2025-09-05-1st · Exercise 2A · p. 3]]

^aapp-04-016

**My answer**

Already answered above. To provide a different example we can talk about merge sort. Instead of sorting the whole array, we split it in half and merge the two halves then merge them together in the order. We can also recursively split the sub array until we reach a single element array and merge from that point on.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; say “recursively sort” before merging.** Your final description of splitting to single elements and merging upward gives the right structure. A merge relies on both input halves already being sorted; splitting an unsorted array and immediately merging its unsorted halves does not implement merge sort.
>
> **Suggested exam answer:** Merge sort illustrates divide and conquer. Divide the array into two nearly equal halves. Conquer by recursively sorting both halves, stopping at arrays of size zero or one, which are already sorted. Combine by repeatedly taking the smaller next element from the two sorted halves. This linear-time merge produces the sorted full array. Its sequential recurrence is $T(n)=2T(n/2)+\Theta(n)$, with constant base-case cost, giving $\Theta(n\log n)$ time by Master Case 2.
>
> **Study:** [[Divide and Conquer#Merge sort as the template]]; [[Algorithm as recipes#Looking inside the merge]]; [[lecture3-DandC.pdf#page=4|slide 4]].

> [!success]- Model answer
> **Suggested exam answer:** Merge sort illustrates divide and conquer. Divide the array into two nearly equal halves. Conquer by recursively sorting both halves, stopping at arrays of size zero or one, which are already sorted. Combine by repeatedly taking the smaller next element from the two sorted halves. This linear-time merge produces the sorted full array. Its sequential recurrence is $T(n)=2T(n/2)+\Theta(n)$, with constant base-case cost, giving $\Theta(n\log n)$ time by Master Case 2.
>
> **Study:** [[Divide and Conquer#Merge sort as the template]]; [[Algorithm as recipes#Looking inside the merge]]; [[lecture3-DandC.pdf#page=4|slide 4]].

### AAPP-04-017

Please explain how powering of a number works and how, with the Master Theorem method, you can compute its asymptotic complexity. (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=3|2025-11-06-1st · Exercise 2B · p. 3]]

^aapp-04-017

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; state the one-call recurrence and the exact Master case.** The idea in 004 is correct, with the odd-exponent correction explained in 011.
>
> **Suggested exam answer:** Compute $x^{\lfloor n/2\rfloor}$ once and square the result; multiply by $x$ once more if $n$ is odd. Stop at $n=0$ with result 1. This gives $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. For the Master theorem, $a=1,b=2$ and $n^{\log_2 1}=1$. The nonrecursive cost is $\Theta(1)$, so Case 2 with $k=0$ gives $\Theta(\log n)$ unit-cost arithmetic time. Computing the same half-power twice would change the recurrence and result in linear work.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=19|slide 19]].

> [!success]- Model answer
> **Suggested exam answer:** Compute $x^{\lfloor n/2\rfloor}$ once and square the result; multiply by $x$ once more if $n$ is odd. Stop at $n=0$ with result 1. This gives $T(n)=T(\lfloor n/2\rfloor)+\Theta(1)$. For the Master theorem, $a=1,b=2$ and $n^{\log_2 1}=1$. The nonrecursive cost is $\Theta(1)$, so Case 2 with $k=0$ gives $\Theta(\log n)$ unit-cost arithmetic time. Computing the same half-power twice would change the recurrence and result in linear work.
>
> **Study:** [[Divide and Conquer#Exponentiation by squaring]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=19|slide 19]].

### AAPP-04-018

Discuss Strassen’s matrix multiplication algorithm and compare its complexity with the standard matrix multiplication algorithm. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=5|2026-6-11-1st · Exercise 3B · p. 5]]

^aapp-04-018

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference to 005; replace the rounded $O(n^{2.8})$ claim with the exact bound.** For this comparison, the recurrences show why the exponent changes.
>
> **Suggested exam answer:** Classical matrix multiplication takes $\Theta(n^3)$ time; its ordinary block-recursive form uses eight half-size products and has $T(n)=8T(n/2)+\Theta(n^2)$. Strassen uses seven half-size products of block sums/differences and reconstructs the result through additional additions/subtractions. Its recurrence is $T(n)=7T(n/2)+\Theta(n^2)$, giving $\Theta(n^{\log_2 7})$ arithmetic operations, with exponent approximately 2.807. This is asymptotically smaller than cubic time. The reduction from eight to seven occurs at every recursive level, though extra overhead can outweigh the saving for small matrices.
>
> **Study:** [[Divide and Conquer#Ordinary block recursion]]; [[Divide and Conquer#Complexity]]; [[Divide and Conquer#Why saving one product compounds]]; [[lecture3-DandC.pdf#page=38|slide 38]].

> [!success]- Model answer
> **Suggested exam answer:** Classical matrix multiplication takes $\Theta(n^3)$ time; its ordinary block-recursive form uses eight half-size products and has $T(n)=8T(n/2)+\Theta(n^2)$. Strassen uses seven half-size products of block sums/differences and reconstructs the result through additional additions/subtractions. Its recurrence is $T(n)=7T(n/2)+\Theta(n^2)$, giving $\Theta(n^{\log_2 7})$ arithmetic operations, with exponent approximately 2.807. This is asymptotically smaller than cubic time. The reduction from eight to seven occurs at every recursive level, though extra overhead can outweigh the saving for small matrices.
>
> **Study:** [[Divide and Conquer#Ordinary block recursion]]; [[Divide and Conquer#Complexity]]; [[Divide and Conquer#Why saving one product compounds]]; [[lecture3-DandC.pdf#page=38|slide 38]].

### AAPP-04-019

Describe one Divide and Conquer example discussed during the lectures and explain why the Master Theorem is useful for analyzing this class of algorithms. (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=3|2026-9-10-1st · Exercise 2B · p. 3]]

^aapp-04-019

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; one concrete example and its recurrence make a complete answer.** Merge sort, already discussed in 016 and in the lecture, gives a direct illustration.
>
> **Suggested exam answer:** Merge sort divides an array into two halves, recursively sorts each half, and merges the sorted results in linear time, stopping at constant-size arrays. Its recurrence is $T(n)=2T(n/2)+\Theta(n)$. The Master theorem has $a=2,b=2$, so $n^{\log_b a}=n$ matches the nonrecursive cost. Case 2 gives $T(n)=\Theta(n\log n)$. The theorem is useful because many balanced divide-and-conquer algorithms have this fixed-number, fixed-ratio structure, allowing their bounds to be derived by checking standard cases. Its assumptions must be verified rather than applied to every recursive algorithm.
>
> **Study:** [[Divide and Conquer#Merge sort as the template]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=4|slides 4–7]].

> [!success]- Model answer
> **Suggested exam answer:** Merge sort divides an array into two halves, recursively sorts each half, and merges the sorted results in linear time, stopping at constant-size arrays. Its recurrence is $T(n)=2T(n/2)+\Theta(n)$. The Master theorem has $a=2,b=2$, so $n^{\log_b a}=n$ matches the nonrecursive cost. Case 2 gives $T(n)=\Theta(n\log n)$. The theorem is useful because many balanced divide-and-conquer algorithms have this fixed-number, fixed-ratio structure, allowing their bounds to be derived by checking standard cases. Its assumptions must be verified rather than applied to every recursive algorithm.
>
> **Study:** [[Divide and Conquer#Merge sort as the template]]; [[Algorithm as recipes#Master theorem]]; [[lecture3-DandC.pdf#page=4|slides 4–7]].

## Randomized algorithm classes

Related notes: [[Randomized Algorithms]].

### AAPP-05-001

Explain the difference between Monte Carlo and Las Vegas Randomized based algorithms.

Source: [[Tema Esame 2022-01-14-1st.pdf#page=4|2022-01-14-1st · Exercise 3 · p. 4]]

^aapp-05-001

**My answer**

They are both randomized algorithm, meaning they have some functioning that is random and so is some aspect of the result and complexity. Monte Carlo algorithms have a fixed maximum time under which they are guaranteed to finish, but it does not guarantee that the result is correct. Las Vegas is the opposite, the time to finish is random but it always find the result. 

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; make the guarantees precise.** You correctly distinguish bounded-time possible error from zero-error random runtime. A randomized algorithm need not have both a random answer and a random runtime. Also, a Monte Carlo time bound is a function of input size and the chosen parameters, rather than one fixed constant for every input.
>
> **Suggested exam answer:** A Las Vegas algorithm never returns an incorrect solution; randomness affects its execution time. Under the usual finite-expected-time guarantee it terminates with probability one, although some algorithms allow arbitrarily long runs. A Monte Carlo algorithm has a stated worst-case runtime bound and may return an incorrect answer or fail to find the requested solution with a specified probability. Its error guarantee must be stated. Independent repetition can often reduce that probability. Las Vegas does not necessarily have an unbounded worst-case runtime: randomized quicksort is always correct and still has a finite quadratic worst case.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Sorting#Randomized quicksort]]; [[lecture5-Randomization.pdf#page=21|slides 21–24]].

> [!success]- Model answer
> **Suggested exam answer:** A Las Vegas algorithm never returns an incorrect solution; randomness affects its execution time. Under the usual finite-expected-time guarantee it terminates with probability one, although some algorithms allow arbitrarily long runs. A Monte Carlo algorithm has a stated worst-case runtime bound and may return an incorrect answer or fail to find the requested solution with a specified probability. Its error guarantee must be stated. Independent repetition can often reduce that probability. Las Vegas does not necessarily have an unbounded worst-case runtime: randomized quicksort is always correct and still has a finite quadratic worst case.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Sorting#Randomized quicksort]]; [[lecture5-Randomization.pdf#page=21|slides 21–24]].

### AAPP-05-002

Please define when Las Vegas and Monte Carlo algorithms are defined as efficient algorithms. (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=3|2024-02-16-1st · Exercise 2A · p. 3]]

^aapp-05-002

**My answer**

For Las Vegas it is efficient when the expected time is bounded by a polynomial of the input size, for Monte Carlo the worst case has to be bounded to that same amount.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: correct runtime criteria; add what is being averaged and the Monte Carlo error guarantee.** Your expected-polynomial versus worst-case-polynomial distinction matches the lecture. The Las Vegas expectation is over internal random choices for each fixed input, rather than over a favorable distribution of inputs.
>
> **Suggested exam answer:** An efficient Las Vegas algorithm is zero-error and has expected runtime bounded by a polynomial in input size on every valid input. In symbols, for some polynomial $P$, $\mathbb E_R[T(x,R)]\le P(|x|)$ for each input $x$. An efficient Monte Carlo algorithm has polynomial worst-case runtime on every valid input, together with a specified useful error bound. For a standard bounded-error decision algorithm, one can require error at most $1/3$ on each input; the particular constant is conventional and can often be improved by independent repetition. The repetition needed to achieve the required guarantee must also fit the polynomial budget.
>
> **Course wording:** Slide 24 states the runtime criteria; slide 23 explicitly adds bounded error for Monte Carlo. Read those statements together.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Randomized Algorithms#Fixing the input before taking an expectation]]; [[lecture5-Randomization.pdf#page=23|slides 23–24]].

> [!success]- Model answer
> **Suggested exam answer:** An efficient Las Vegas algorithm is zero-error and has expected runtime bounded by a polynomial in input size on every valid input. In symbols, for some polynomial $P$, $\mathbb E_R[T(x,R)]\le P(|x|)$ for each input $x$. An efficient Monte Carlo algorithm has polynomial worst-case runtime on every valid input, together with a specified useful error bound. For a standard bounded-error decision algorithm, one can require error at most $1/3$ on each input; the particular constant is conventional and can often be improved by independent repetition. The repetition needed to achieve the required guarantee must also fit the polynomial budget.
>
> **Course wording:** Slide 24 states the runtime criteria; slide 23 explicitly adds bounded error for Monte Carlo. Read those statements together.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Randomized Algorithms#Fixing the input before taking an expectation]]; [[lecture5-Randomization.pdf#page=23|slides 23–24]].

### AAPP-05-003

Please list the main differences between the Las Vegas and Monte Carlo algorithms. (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=3|2024-06-26-1st · Exercise 2A · p. 3]]

^aapp-05-003

**My answer**

Already answered.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; your main distinction in 001 is correct with the qualifications there.** Give the guarantees directly when answering an individual exam question.
>
> **Suggested exam answer:** Las Vegas algorithms preserve correctness: any returned solution is correct, while runtime depends on the random choices and is usually analyzed in expectation. Monte Carlo algorithms have a stated worst-case runtime bound while allowing a quantified probability of error or failure. Efficient Las Vegas algorithms have polynomial expected time for each input; efficient Monte Carlo algorithms have polynomial worst-case time with a controlled error guarantee. Randomized quicksort illustrates zero-error random runtime, while the lecture's bounded random search illustrates bounded time with possible failure.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Randomized Algorithms#Example: finding an a]]; [[lecture5-Randomization.pdf#page=21|slides 21–27]].

> [!success]- Model answer
> **Suggested exam answer:** Las Vegas algorithms preserve correctness: any returned solution is correct, while runtime depends on the random choices and is usually analyzed in expectation. Monte Carlo algorithms have a stated worst-case runtime bound while allowing a quantified probability of error or failure. Efficient Las Vegas algorithms have polynomial expected time for each input; efficient Monte Carlo algorithms have polynomial worst-case time with a controlled error guarantee. Randomized quicksort illustrates zero-error random runtime, while the lecture's bounded random search illustrates bounded time with possible failure.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[Randomized Algorithms#Example: finding an a]]; [[lecture5-Randomization.pdf#page=21|slides 21–27]].

### AAPP-05-004

Please describe the differences between Las Vegas and Monte Carlo algorithms, even considering time complexity issues. (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=4|2024-11-12-1st · Exercise 3A · p. 4]]

^aapp-05-004

**My answer**

Already answered above. For time complexity Las Vegas has an expected time but worst case could be infinite, Monte Carlo instead is bound.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: mostly correct; distinguish an unbounded worst case from a positive probability of never finishing.** A Las Vegas algorithm can have arbitrarily long executions, but this is not required of every Las Vegas algorithm. A finite expected runtime implies termination with probability one; it does not provide a deterministic deadline.
>
> **Suggested exam answer:** Las Vegas algorithms are zero-error and are efficient when expected runtime is polynomial on every input. In the lecture's repeat-until-hit example, no finite deterministic trial bound exists, yet termination has probability one and the expectation is finite under the promised target fraction. Other Las Vegas algorithms have finite worst-case bounds: standard randomized quicksort on distinct keys has expected $\Theta(n\log n)$ time and worst-case $\Theta(n^2)$ time. Monte Carlo algorithms instead have a stated worst-case time bound and permit controlled error or failure; efficient versions use polynomial time with a suitable error guarantee. A polynomial expectation and a polynomial worst-case bound are different guarantees.
>
> **Study:** [[Randomized Algorithms#Las Vegas version]]; [[Randomized Algorithms#Probability of stopping now versus still waiting]]; [[Sorting#Randomized quicksort]]; [[lecture5-Randomization.pdf#page=26|slides 26–27]].

> [!success]- Model answer
> **Suggested exam answer:** Las Vegas algorithms are zero-error and are efficient when expected runtime is polynomial on every input. In the lecture's repeat-until-hit example, no finite deterministic trial bound exists, yet termination has probability one and the expectation is finite under the promised target fraction. Other Las Vegas algorithms have finite worst-case bounds: standard randomized quicksort on distinct keys has expected $\Theta(n\log n)$ time and worst-case $\Theta(n^2)$ time. Monte Carlo algorithms instead have a stated worst-case time bound and permit controlled error or failure; efficient versions use polynomial time with a suitable error guarantee. A polynomial expectation and a polynomial worst-case bound are different guarantees.
>
> **Study:** [[Randomized Algorithms#Las Vegas version]]; [[Randomized Algorithms#Probability of stopping now versus still waiting]]; [[Sorting#Randomized quicksort]]; [[lecture5-Randomization.pdf#page=26|slides 26–27]].

### AAPP-05-005

Please list the main differences, including the efficiency, between the Las Vegas and Monte Carlo algorithms. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=3|2025-07-04-1st · Exercise 2B · p. 3]]

^aapp-05-005

**My answer**

Already answered above.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; combine the classification with the efficiency criteria.** Your answer in 002 supplies the correct runtime distinction. Include the correctness/error requirements as well.
>
> **Suggested exam answer:** A Las Vegas algorithm gives a correct answer whenever it terminates; an efficient version has polynomial expected runtime for every fixed valid input, averaging over its own random choices. Under that guarantee termination occurs with probability one. A Monte Carlo algorithm has a bounded worst-case runtime and a specified probability of error or failure. An efficient version has polynomial worst-case runtime and meets the required error guarantee, including any repetitions used to improve reliability. A Las Vegas run need not finish within its expected time, and bounded time alone does not make an unreliable Monte Carlo solver adequate.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[lecture5-Randomization.pdf#page=23|slides 23–24]].

> [!success]- Model answer
> **Suggested exam answer:** A Las Vegas algorithm gives a correct answer whenever it terminates; an efficient version has polynomial expected runtime for every fixed valid input, averaging over its own random choices. Under that guarantee termination occurs with probability one. A Monte Carlo algorithm has a bounded worst-case runtime and a specified probability of error or failure. An efficient version has polynomial worst-case runtime and meets the required error guarantee, including any repetitions used to improve reliability. A Las Vegas run need not finish within its expected time, and bounded time alone does not make an unreliable Monte Carlo solver adequate.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[lecture5-Randomization.pdf#page=23|slides 23–24]].

### AAPP-05-006

Could you outline the main differences between Las Vegas and Monte Carlo algorithms, especially in terms of efficiency, and give examples of each? (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=5|2026-1-22-1st · Exercise 3A · p. 5]]

^aapp-05-006

**My answer**

Already answered above. An example can be made from find a in a list of elements. Las Vegas is look a random element until a is found, always finds a but time is not bound. Monte Carlo says look for a randomly 20 times, a might not be found but time is bound to 20 executions.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: good examples; add the input promise, sampling model, and probabilities.** Your repeat-until-found versus 20-trial distinction matches the lecture. “Always finds a” needs the promise that an `a` exists and should be expressed as termination with probability one. If no `a` exists, the unbounded loop never succeeds. Twenty trials alone do not establish a useful success probability for an arbitrary array.
>
> **Suggested exam answer:** Las Vegas is zero-error with runtime analyzed in expectation; efficient versions have polynomial expected time on each input. Monte Carlo has a stated worst-case time bound with controlled error or failure; efficient versions meet the required error guarantee in polynomial worst-case time. For the lecture's example, assume an array with half its entries equal to `a`, and take independent uniform samples with replacement. The Las Vegas version samples until it reads an `a` and returns that index. Every returned index is valid, expected trial count is $1/(1/2)=2$, and termination has probability one, with no finite deterministic trial limit. The Monte Carlo version samples at most 20 times, returning a valid index if found and `FAIL` otherwise. It uses at most 20 samples, and $\Pr(\mathrm{FAIL})=(1/2)^{20}=2^{-20}\approx9.54\times10^{-7}$.
>
> **Error interpretation:** `FAIL` means that the bounded search did not find a witness. It does not establish that the array contains no `a`. If failure is reported as a membership answer NO, an existing `a` can be missed: a false negative. This is the bounded-sampling example used in the lecture's Monte Carlo discussion.
>
> **Why the promise matters:** With target fraction $q>0$, the expected repeat-until-hit count is $1/q$ and the 20-trial failure probability is $(1-q)^{20}$. If there is only one `a` among $n$ entries, the latter is $(1-1/n)^{20}$ and approaches 1 as $n$ grows. Thus 20 trials are not uniformly reliable without a lower bound on the target fraction. These sample-time bounds assume unit-cost random indexing and lookup.
>
> **Study:** [[Randomized Algorithms#Example: finding an a]]; [[Randomized Algorithms#Generalizing the success probability]]; [[Randomized Algorithms#Interpreting the error direction]]; [[lecture5-Randomization.pdf#page=25|slides 25–27]].

> [!success]- Model answer
> **Suggested exam answer:** Las Vegas is zero-error with runtime analyzed in expectation; efficient versions have polynomial expected time on each input. Monte Carlo has a stated worst-case time bound with controlled error or failure; efficient versions meet the required error guarantee in polynomial worst-case time. For the lecture's example, assume an array with half its entries equal to `a`, and take independent uniform samples with replacement. The Las Vegas version samples until it reads an `a` and returns that index. Every returned index is valid, expected trial count is $1/(1/2)=2$, and termination has probability one, with no finite deterministic trial limit. The Monte Carlo version samples at most 20 times, returning a valid index if found and `FAIL` otherwise. It uses at most 20 samples, and $\Pr(\mathrm{FAIL})=(1/2)^{20}=2^{-20}\approx9.54\times10^{-7}$.
>
> **Error interpretation:** `FAIL` means that the bounded search did not find a witness. It does not establish that the array contains no `a`. If failure is reported as a membership answer NO, an existing `a` can be missed: a false negative. This is the bounded-sampling example used in the lecture's Monte Carlo discussion.
>
> **Why the promise matters:** With target fraction $q>0$, the expected repeat-until-hit count is $1/q$ and the 20-trial failure probability is $(1-q)^{20}$. If there is only one `a` among $n$ entries, the latter is $(1-1/n)^{20}$ and approaches 1 as $n$ grows. Thus 20 trials are not uniformly reliable without a lower bound on the target fraction. These sample-time bounds assume unit-cost random indexing and lookup.
>
> **Study:** [[Randomized Algorithms#Example: finding an a]]; [[Randomized Algorithms#Generalizing the success probability]]; [[Randomized Algorithms#Interpreting the error direction]]; [[lecture5-Randomization.pdf#page=25|slides 25–27]].

### AAPP-05-007

Please list the main differences between the Las Vegas and Monte Carlo algorithms. What about the efficiency? (1)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=4|2026-6-29-1st · Exercise 2C · p. 4]]

^aapp-05-007

**My answer**

Already answered above

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: revision cross-reference; the earlier classification and runtime criteria are mostly correct.** State both guarantees explicitly and identify the source of the expectation.
>
> **Suggested exam answer:** In a Las Vegas algorithm, randomness affects performance while correctness is preserved; finite expected time gives termination with probability one. It is efficient when, for every valid input, expected runtime over internal random choices is polynomial in input size. A Monte Carlo algorithm has a stated worst-case runtime bound and a quantified probability of error or failure. Efficient versions have polynomial worst-case time and meet an appropriate error guarantee, often improved through independent repetition. Some Las Vegas algorithms have finite worst-case bounds, so “Las Vegas always has an infinite worst case” is not a defining distinction.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[lecture5-Randomization.pdf#page=21|slides 21–24]].

> [!success]- Model answer
> **Suggested exam answer:** In a Las Vegas algorithm, randomness affects performance while correctness is preserved; finite expected time gives termination with probability one. It is efficient when, for every valid input, expected runtime over internal random choices is polynomial in input size. A Monte Carlo algorithm has a stated worst-case runtime bound and a quantified probability of error or failure. Efficient versions have polynomial worst-case time and meet an appropriate error guarantee, often improved through independent repetition. Some Las Vegas algorithms have finite worst-case bounds, so “Las Vegas always has an infinite worst case” is not a defining distinction.
>
> **Study:** [[Randomized Algorithms#Las Vegas and Monte Carlo]]; [[lecture5-Randomization.pdf#page=21|slides 21–24]].

### AAPP-05-008

Why can randomization be useful in a data structure even when the required answer must always be correct? Give one example. (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=5|2026-9-10-1st · Exercise 3A · p. 5]]

^aapp-05-008

**My answer**

Yes of coure. Mainly Las Vegas, because Monte Carlo can be erroneous. To see if it is useful we need to analyze the problem and the efficiency of Las Vegas in that problem. If the expected time for success is bounded by a polynomial of the input size than it is efficient. Then we can compare it to a deterministic method and see which is better. 

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: relevant zero-error intuition, but the data-structure mechanism and example are missing.** The question asks how randomness can improve structure or operation costs while searches remain exact. A general polynomial-time comparison does not explain that benefit.
>
> **Suggested exam answer:** Random choices can determine a data structure's shape while its invariants guarantee correct answers. For example, a treap stores keys in binary-search-tree order and gives each node an independent random priority, maintaining a heap order on priorities. Rotations preserve key order while restoring the priority invariant, so searches and updates remain correct for every valid priority assignment. Under the standard model of independent distinct priorities and a fixed operation sequence independent of those priorities, search, insertion, and deletion take $O(\log n)$ expected time, although a worst-case chain can take $O(n)$. Thus randomness supplies favorable expected structure without requiring the keys to arrive in random order. Expected performance does not imply perfect balance on every run.
>
> **Study:** [[Randomized Data Structures#Overview]]; [[Randomized Data Structures#Treaps: a search tree and a priority heap]]; [[Randomized Data Structures#Search and harmonic path lengths]]; [[Randomized Data Structures#Rotations and updates]]; [[lecture11RandomDataStructures.pdf#page=9|slides 9–17]].

> [!success]- Model answer
> **Suggested exam answer:** Random choices can determine a data structure's shape while its invariants guarantee correct answers. For example, a treap stores keys in binary-search-tree order and gives each node an independent random priority, maintaining a heap order on priorities. Rotations preserve key order while restoring the priority invariant, so searches and updates remain correct for every valid priority assignment. Under the standard model of independent distinct priorities and a fixed operation sequence independent of those priorities, search, insertion, and deletion take $O(\log n)$ expected time, although a worst-case chain can take $O(n)$. Thus randomness supplies favorable expected structure without requiring the keys to arrive in random order. Expected performance does not imply perfect balance on every run.
>
> **Study:** [[Randomized Data Structures#Overview]]; [[Randomized Data Structures#Treaps: a search tree and a priority heap]]; [[Randomized Data Structures#Search and harmonic path lengths]]; [[Randomized Data Structures#Rotations and updates]]; [[lecture11RandomDataStructures.pdf#page=9|slides 9–17]].

### AAPP-05-009

Randomization can simplify balancing and give good expected performance while preserving correctness. True/False? Example? (2)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=6|2026-9-10-1st · Exercise 3C · p. 6]]

^aapp-05-009

**My answer**

Not sure what this means.

> [!note]- Feedback
> **Reviewed: 2026-11-01.**
>
> **Assessment: no answer supplied; the statement is True under the usual randomized-data-structure assumptions.** Randomization can choose the shape, while deterministic structural invariants preserve the meaning of every operation.
>
> **Suggested exam answer:** True. A treap maintains binary-search-tree order on keys and heap order on independent random priorities. Rotations preserve key order and restore the priority invariant, avoiding the need for deterministic balance factors or coloring rules. Search, insertion, and deletion remain exact and have $O(\log n)$ expected cost for fixed operation sequences independent of the sampled priorities. A possible worst-case chain still costs $O(n)$ per operation. The expectation concerns the priorities, rather than random user inputs. See [Aspnes, randomized search trees, §§6.3–6.3.1](https://www.cs.yale.edu/~aspnes/classes/469/notes.pdf#page=139).
>
> **Concrete example:** Insert keys $1,2,3$ in that order. An ordinary unbalanced BST forms a rightward chain. Assign treap priorities $(3,1,2)$ to those keys and use the lecture's min-heap convention. Inserting key 2 rotates it above key 1; inserting key 3 gives a tree with root 2, left child 1, and right child 3. Searches are still ordinary exact BST comparisons. This example illustrates how priorities change shape; the logarithmic expected bound comes from analysis over all independent priority choices, rather than from this one balanced instance.
>
> **Study:** [[Randomized Data Structures#Treaps: a search tree and a priority heap]]; [[Randomized Data Structures#Why a rotation preserves search order]]; [[Randomized Data Structures#Insertion: search down, rotate up]]; [[lecture11RandomDataStructures.pdf#page=9|slides 9–20]].

> [!success]- Model answer
> **Suggested exam answer:** True. A treap maintains binary-search-tree order on keys and heap order on independent random priorities. Rotations preserve key order and restore the priority invariant, avoiding the need for deterministic balance factors or coloring rules. Search, insertion, and deletion remain exact and have $O(\log n)$ expected cost for fixed operation sequences independent of the sampled priorities. A possible worst-case chain still costs $O(n)$ per operation. The expectation concerns the priorities, rather than random user inputs. See [Aspnes, randomized search trees, §§6.3–6.3.1](https://www.cs.yale.edu/~aspnes/classes/469/notes.pdf#page=139).
>
> **Concrete example:** Insert keys $1,2,3$ in that order. An ordinary unbalanced BST forms a rightward chain. Assign treap priorities $(3,1,2)$ to those keys and use the lecture's min-heap convention. Inserting key 2 rotates it above key 1; inserting key 3 gives a tree with root 2, left child 1, and right child 3. Searches are still ordinary exact BST comparisons. This example illustrates how priorities change shape; the logarithmic expected bound comes from analysis over all independent priority choices, rather than from this one balanced instance.
>
> **Study:** [[Randomized Data Structures#Treaps: a search tree and a priority heap]]; [[Randomized Data Structures#Why a rotation preserves search order]]; [[Randomized Data Structures#Insertion: search down, rotate up]]; [[lecture11RandomDataStructures.pdf#page=9|slides 9–20]].

## Minimum cut

Related notes: [[Minimum Cut]].

### AAPP-06-001

Describe how Karger and Stein algorithm works. Discuss and compare the two algorithms’ complexity.

Source: [[Tema Esame 2022-01-14-1st.pdf#page=3|2022-01-14-1st · Exercise 2 · p. 3]]

^aapp-06-001

**My answer**

Krager algorithm by itself is used to find the minimum cut of a graph. In order to do so an edge is picked at random and the 2 nodes it connect are merged, repeat that until only 2 nodes remain and all the edges between those represents a cut, the change to be the minumum is 2/(n(n-1)) so we repeat the algorithm n(n-1)/2 times clogn and take the smallest cut found, that still does not guarantee success. With a O(n^2) time to execute it once, the total is O(n^4logn). Stein imporved the algorithm by reducing the complexity. To do so it avoids doing more branching reductions at the beginning since the chance of hitting the wrong edge is low, so it finds 2 reduction with  1+n/radix(2) nodes. After that it behaves like the normal Krager algorithm so the complexity is reduced.

> [!note]- Feedback
> **Reviewed: 2026-11-02.**
>
> **Assessment: mostly correct basic Karger analysis; the Karger–Stein description and comparison are incomplete.** Your contraction idea, repetition order, and $O(n^4\log n)$ amplified bound match the course model. Three details matter: $2/[n(n-1)]$ is a lower bound on success, rather than necessarily its exact probability; contraction must preserve parallel-edge multiplicities and remove self-loops; and both Karger–Stein branches recurse using Karger–Stein, rather than simply finishing with one ordinary Karger path each.
>
> **Suggested exam answer — Karger:** For a connected undirected unweighted graph with $n\ge2$ vertices, repeatedly choose a uniformly random remaining edge copy and merge its endpoints. Retain parallel edges, remove self-loops, and record which original vertices each supernode contains. After $n-2$ contractions, return the cut between the two supernodes. A chosen minimum cut survives whenever none of its edges is contracted; its survival probability is at least $p_0=2/[n(n-1)]$. Repeat from fresh copies of the original graph with independent random choices and retain the smallest returned cut. With $R$ runs, failure probability is at most $(1-p_0)^R\le e^{-p_0R}$. Thus your budget, written precisely as $R=\lceil c\,n(n-1)\ln n/2\rceil$, suffices for failure at most $n^{-c}$, for fixed $c>0$. At $O(n^2)$ time per run, total time is $O(n^4\log n)$.
>
> **Suggested exam answer — Karger–Stein:** At a recursive call with $n>6$ supernodes, make two fresh copies and independently contract each to $t=\lceil1+n/\sqrt2\rceil$ supernodes. Recursively run Karger–Stein on both resulting multigraphs, and return the smaller lifted cut. For $n\le6$, find the minimum cut exactly by enumerating the nontrivial partitions. This branching is repeated at every recursive level. The threshold is a number of supernodes to leave, rather than a number of contractions to perform. It preserves a chosen minimum cut in a partial contraction with probability at least $1/2$, but the recursive call must still find that cut. One full recursive run has success probability $\Omega(1/\log n)$.
>
> **Complexity comparison:** Under the lecture's quadratic contraction/copying model, one recursive run satisfies $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Exploring that recursion tree is one run. Repeating whole independent runs $O(\log^2 n)$ times gives inverse-polynomial failure probability and total $O(n^2\log^3 n)$ time.
>
> | Algorithm | Time for one full run | Success guarantee per run | Total time for failure at most $n^{-c}$ |
> |---|---|---|---|
> | Karger | $O(n^2)$ | At least $2/[n(n-1)]$ | $O(n^4\log n)$ |
> | Karger–Stein | $O(n^2\log n)$ | $\Omega(1/\log n)$ | $O(n^2\log^3 n)$ |
>
> Karger–Stein improves the success-versus-time trade-off: its single recursive run costs more, but far fewer independent runs are needed. Both are Monte Carlo algorithms. For a fixed constant error target, the corresponding totals are $O(n^4)$ and $O(n^2\log^2 n)$; the extra logarithm in the table comes from requiring failure at most $n^{-c}$. The distinction between single-run and amplified bounds is also derived in [Vigoda's notes, §1.3.2](https://sites.cs.ucsb.edu/~vigoda/6550/Notes/Lec1.pdf#page=4).
>
> **Base-case detail:** With the stated ceiling, $t=6$ when $n=6$. Use the exact base case $n\le6$ so recursion shrinks; the supplied slide's strict $n<6$ condition needs this correction.
>
> **Study:** [[Minimum Cut#Contraction and the invariant]]; [[Minimum Cut#Repetition and running time]]; [[Minimum Cut#Stop early and branch]]; [[Minimum Cut#Partial survival and recursive success]]; [[Minimum Cut#Time for one run versus amplified time]]; [[lecture6-MinCut.pdf#page=16|slides 16–21]].

> [!success]- Model answer
> **Suggested exam answer — Karger:** For a connected undirected unweighted graph with $n\ge2$ vertices, repeatedly choose a uniformly random remaining edge copy and merge its endpoints. Retain parallel edges, remove self-loops, and record which original vertices each supernode contains. After $n-2$ contractions, return the cut between the two supernodes. A chosen minimum cut survives whenever none of its edges is contracted; its survival probability is at least $p_0=2/[n(n-1)]$. Repeat from fresh copies of the original graph with independent random choices and retain the smallest returned cut. With $R$ runs, failure probability is at most $(1-p_0)^R\le e^{-p_0R}$. Thus your budget, written precisely as $R=\lceil c\,n(n-1)\ln n/2\rceil$, suffices for failure at most $n^{-c}$, for fixed $c>0$. At $O(n^2)$ time per run, total time is $O(n^4\log n)$.
>
> **Suggested exam answer — Karger–Stein:** At a recursive call with $n>6$ supernodes, make two fresh copies and independently contract each to $t=\lceil1+n/\sqrt2\rceil$ supernodes. Recursively run Karger–Stein on both resulting multigraphs, and return the smaller lifted cut. For $n\le6$, find the minimum cut exactly by enumerating the nontrivial partitions. This branching is repeated at every recursive level. The threshold is a number of supernodes to leave, rather than a number of contractions to perform. It preserves a chosen minimum cut in a partial contraction with probability at least $1/2$, but the recursive call must still find that cut. One full recursive run has success probability $\Omega(1/\log n)$.
>
> **Complexity comparison:** Under the lecture's quadratic contraction/copying model, one recursive run satisfies $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Exploring that recursion tree is one run. Repeating whole independent runs $O(\log^2 n)$ times gives inverse-polynomial failure probability and total $O(n^2\log^3 n)$ time.
>
> | Algorithm | Time for one full run | Success guarantee per run | Total time for failure at most $n^{-c}$ |
> |---|---|---|---|
> | Karger | $O(n^2)$ | At least $2/[n(n-1)]$ | $O(n^4\log n)$ |
> | Karger–Stein | $O(n^2\log n)$ | $\Omega(1/\log n)$ | $O(n^2\log^3 n)$ |
>
> Karger–Stein improves the success-versus-time trade-off: its single recursive run costs more, but far fewer independent runs are needed. Both are Monte Carlo algorithms. For a fixed constant error target, the corresponding totals are $O(n^4)$ and $O(n^2\log^2 n)$; the extra logarithm in the table comes from requiring failure at most $n^{-c}$. The distinction between single-run and amplified bounds is also derived in [Vigoda's notes, §1.3.2](https://sites.cs.ucsb.edu/~vigoda/6550/Notes/Lec1.pdf#page=4).
>
> **Base-case detail:** With the stated ceiling, $t=6$ when $n=6$. Use the exact base case $n\le6$ so recursion shrinks; the supplied slide's strict $n<6$ condition needs this correction.
>
> **Study:** [[Minimum Cut#Contraction and the invariant]]; [[Minimum Cut#Repetition and running time]]; [[Minimum Cut#Stop early and branch]]; [[Minimum Cut#Partial survival and recursive success]]; [[Minimum Cut#Time for one run versus amplified time]]; [[lecture6-MinCut.pdf#page=16|slides 16–21]].

### AAPP-06-002

Describe the Karger’s Min-Cut Algorithm. Is the Karger’s Min-Cut Algorithm a Monte Carlo randomization- based algorithm?

Source: [[Tema Esame 2022-02-11-1st.pdf#page=3|2022-02-11-1st · Exercise 2 · p. 3]]

^aapp-06-002

**My answer**

Yes beacause the number of runs is limited, but it does not guarantee to find the min cut. It does find a resulting cut altought it might not be minimal

> [!note]- Feedback
> **Reviewed: 2026-11-02.**
>
> **Assessment: correct classification and outcome distinction; the contraction algorithm is missing.** You correctly say that the output is a valid cut and may fail to be minimum. A limited run count alone does not establish Monte Carlo classification: the relevant combination is bounded runtime and possible error about optimality.
>
> **Suggested exam answer:** Yes. On a connected undirected graph, Karger's algorithm repeatedly samples a uniformly random edge copy and contracts its endpoints until two supernodes remain. Preserve parallel-edge multiplicities, delete self-loops, and track original vertex memberships. The final partition defines a valid cut of the original graph, but an unlucky contraction can destroy the minimum cut being preserved. A basic run succeeds with probability at least $2/[n(n-1)]$ and takes $O(n^2)$ time in the course implementation model. Fresh independent repetitions improve reliability by keeping the smallest returned cut; $O(n^2\log n)$ runs suffice for inverse-polynomial failure, giving $O(n^4\log n)$ total time.
>
> It is Monte Carlo because the runtime budget is bounded while the answer may be non-optimal. Verifying that the returned partition is a valid cut does not certify that it is minimum, so this check alone does not turn the algorithm into Las Vegas. Finite repetition gives a probability guarantee, rather than a universal zero-error guarantee.
>
> **Study:** [[Minimum Cut#Contraction and the invariant]]; [[Minimum Cut#Success probability]]; [[Minimum Cut#Repetition and running time]]; [[Randomized Algorithms#Interpreting the error direction]]; [[lecture6-MinCut.pdf#page=9|slides 9–16]].

> [!success]- Model answer
> **Suggested exam answer:** Yes. On a connected undirected graph, Karger's algorithm repeatedly samples a uniformly random edge copy and contracts its endpoints until two supernodes remain. Preserve parallel-edge multiplicities, delete self-loops, and track original vertex memberships. The final partition defines a valid cut of the original graph, but an unlucky contraction can destroy the minimum cut being preserved. A basic run succeeds with probability at least $2/[n(n-1)]$ and takes $O(n^2)$ time in the course implementation model. Fresh independent repetitions improve reliability by keeping the smallest returned cut; $O(n^2\log n)$ runs suffice for inverse-polynomial failure, giving $O(n^4\log n)$ total time.
>
> It is Monte Carlo because the runtime budget is bounded while the answer may be non-optimal. Verifying that the returned partition is a valid cut does not certify that it is minimum, so this check alone does not turn the algorithm into Las Vegas. Finite repetition gives a probability guarantee, rather than a universal zero-error guarantee.
>
> **Study:** [[Minimum Cut#Contraction and the invariant]]; [[Minimum Cut#Success probability]]; [[Minimum Cut#Repetition and running time]]; [[Randomized Algorithms#Interpreting the error direction]]; [[lecture6-MinCut.pdf#page=9|slides 9–16]].

### AAPP-06-003

Describe the Karger and Stein Min-Cut Algorithm. How is the complexity of this algorithm computed? Which is the randomization class the algorithm belongs to?

Source: [[Tema Esame 2022-09-07-1st.pdf#page=2|2022-09-07-1st · Exercise 1 · p. 2]]

^aapp-06-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-004

Describe the Karger and Stein algorithm and its complexity. (2)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=4|2023-01-17-1st · Exercise 3B · p. 4]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=4|2025-09-05-1st · Exercise 3B · p. 4]]

^aapp-06-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-005

What are the key differences between Karger vs Karger&Steing algorithms? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=5|2024-02-16-1st · Exercise 4A · p. 5]]

^aapp-06-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-006

Please describe the key properties of the Karger & Stein algorithm. (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=4|2024-06-26-1st · Exercise 3B · p. 4]]

^aapp-06-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-007

Please describe the ideas used to improve the Karger approach to solving the min-cut problem. What changed with respect to the asymptotic complexity with respect to the initial approach? (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=3|2024-11-12-1st · Exercise 2A · p. 3]]

^aapp-06-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-008

What are the key ideas of the basic Karger approach compared to previous approaches? Does it affect the worst-case complexity?" (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=4|2025-01-24-1st · Exercise 3A · p. 4]]

^aapp-06-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Basic Karger replaces deterministic global-cut approaches based on repeated s–t min-cut/max-flow computations with random edge contraction. Repeatedly merge uniformly chosen edge copies until two supernodes remain; preserve multiplicities and remove loops. The remaining crossing edges define a valid cut, but it may not be minimum. A run costs $O(n^2)$ in the lecture model; success is at least $2/[n(n-1)]$. Independent repetition and choosing the smallest output give $O(n^4\log n)$ bounded total time for inverse-polynomial error. Randomness affects optimality, not whether the prescribed operation budget exists. A historical comparison does not establish superiority over every modern deterministic algorithm.
>
> Study: [[Minimum Cut#Global cuts and s-t cuts]]; [[Minimum Cut#Repetition and running time]].

### AAPP-06-009

In class, we studied two algorithms for minimum cut in a graph. Describe the behavior of both algorithms, including their algorithmic class and complexity. Based on the discussion held in class, explain why one might be preferable over the other. (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=3|2025-06-05-1st · Exercise 2A · p. 3]]

^aapp-06-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-010

What is the main improvement of the Karger–Stein minimum cut algorithm over Karger’s original algorithm, and how does the complexity of one run compare to the overall complexity required to obtain the minimum cut with high probability in both cases? (2)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=7|2025-11-06-1st · Exercise 4A · p. 7]]

^aapp-06-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

### AAPP-06-011

Karger’s min-cut algorithm contracts uniformly random edges until only two supernodes remain and outputs the cut defined by them. In a few sentences, explain (i) what can cause a single run to return a non-minimum cut, and (ii) why and how running the same algorithm many times changes the reliability of the result. (2)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=6|2026-2-09-1st · Exercise 3C · p. 6]]

^aapp-06-011

**My answer**

i: Considering a graph with n edges, a subset of these should be part of the min cut. If the algorithm that selects an edge at every step and reduces it to a single node, at any point, selects an edge that is part of the min cut, then it is impossible to obtain a full reduction that still contains all the min cut edges. ii: If we run the algorithm once, we have at least a (n 2)^-1 chance of obtaining the min cut, so by repeating multiple runs multiple times we can minimize the chance of error, since only one run needs to be successful and we can also bound the failure probability.

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Fix a minimum cut. Contracting one of its crossing edges merges vertices that this cut must separate, destroying that particular optimum; other minimum cuts may still survive. If all contractions avoid a fixed minimum cut, the final two supernodes return it. A run succeeds with probability at least $p_0=2/[n(n-1)]$. Run fresh independent trials from the original graph and retain the smallest cut. Since no valid cut beats the true optimum, any successful trial makes the combined result correct. After $R$ trials, failure is at most $(1-p_0)^R\le e^{-p_0R}$; $R\ge\ln(1/\delta)/p_0$ suffices. Reusing identical random choices gives no such amplification, and observing repeated cut values does not certify optimality.
>
> Study: [[Minimum Cut#Success probability]]; [[Minimum Cut#Why taking the best of repeated runs works]].

### AAPP-06-012

Please describe the key properties of the Karger & Stein algorithm. How is the complexity analyzed? (2)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=3|2026-6-29-1st · Exercise 2A · p. 3]]

^aapp-06-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Karger–Stein is a Monte Carlo divide-and-conquer contraction algorithm. On two independent copies, contract uniformly sampled edge copies down to $t=\lceil1+n/\sqrt2\rceil$ supernodes, preserve multiplicities, remove loops, recursively solve both smaller multigraphs, and retain the smaller lifted cut. Enumerate cuts exactly for $n\le6$; with this rounding, a strict $n<6$ base case would fail to shrink at 6. Branching recurs at every level, concentrating alternatives on the dangerous later contractions.
>
> With quadratic contraction/copying cost, one recursive run costs $T(n)=2T(n/\sqrt2+O(1))+O(n^2)=O(n^2\log n)$. Its success is $\Omega(1/\log n)$, so $O(\log n\log(1/\delta))$ independent complete runs give failure at most $\delta$, with total $O(n^2\log^2 n\log(1/\delta))$. For $\delta=n^{-c}$ this is $O(n^2\log^3 n)$. Basic Karger costs $O(n^2)$ per run, succeeds with probability at least $2/[n(n-1)]$, and needs $O(n^2\log n)$ runs for that confidence: $O(n^4\log n)$ overall. Compare equal confidence targets; the improvement is not a cheaper single run.
>
> Study: [[Minimum Cut#Karger–Stein]]; [[Minimum Cut#Time for one run versus amplified time]].

## Sorting and partitioning

Related notes: [[Sorting]].

### AAPP-07-001

Discuss counting sort complexity. Why does counting sort matter in radix sort?

Source: [[Tema Esame 2022-02-11-1st.pdf#page=4|2022-02-11-1st · Exercise 3 · p. 4]]

^aapp-07-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-002

The best worst-case running time that we have seen for comparison sorting is O(nlg n). Can you explain why? (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=3|2023-07-11-1st · Exercise 2B · p. 3]]

^aapp-07-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.
>
> Study: [[Sorting]].

### AAPP-07-003

Please explain following theorem and why does not hold for the counting sort algorithm: Theorem: “Any decision tree that can sort n elements must have height W(nlg n)” (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=3|2023-09-11-1st · Exercise 2B · p. 3]]

^aapp-07-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.
>
> Study: [[Sorting]].

### AAPP-07-004

Please explain the following theorem and why does not hold for the counting sort algorithm: Theorem: “Any decision tree that can sort n elements must have a height of W(nlog n)” (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=5|2023-11-09-1st · Exercise 4A · p. 5]]

^aapp-07-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.
>
> Study: [[Sorting]].

### AAPP-07-005

What are the key properties that the auxiliary sorting algorithm used by the radix sort must have to achieve efficient and correct sorting? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=3|2024-02-16-1st · Exercise 2B · p. 3]]

^aapp-07-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-006

What are the key properties of the counting sort algorithm? (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=3|2024-06-26-1st · Exercise 2B · p. 3]]

^aapp-07-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-007

Please describe the partitioning algorithm used by the quick sort and its key properties. How is it randomized? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=3|2024-09-05-1st · Exercise 2B · p. 3]]
Source: [[Tema Esame 2025-07-04-1st.pdf#page=5|2025-07-04-1st · Exercise 4A · p. 5]]

^aapp-07-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> One valid variant is Lomuto partition (inclusive bounds):
> ```text
> PARTITION(A,l,r):
>     x=A[r]; i=l
>     for j=l..r-1:
>         if A[j] <= x: swap(A[i],A[j]); i++
>     swap(A[i],A[r]); return i
> ```
> The invariant has keys $\le x$ before $i$, keys $>x$ in the examined middle region, and unexamined keys ahead of $j$. The returned pivot is in its final rank position. A partition takes $\Theta(r-l+1)$ time and $O(1)$ auxiliary space; it is normally unstable. Randomize by choosing a uniform pivot index and swapping it into $r$ before partitioning. Hoare partition returns a split boundary rather than necessarily a final pivot index; recursion bounds must match it. Three-way partition groups $<x,=x,>x$ and handles many duplicates well. Partition is also used by Quickselect.
>
> Study: [[Sorting]].

### AAPP-07-008

Please explain what “Lower bound for comparison sorting” means and its implications. (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=5|2024-11-12-1st · Exercise 4A · p. 5]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=5|2025-09-05-1st · Exercise 4C · p. 5]]
Source: [[Tema Esame 2026-6-11-1st.pdf#page=4|2026-6-11-1st · Exercise 2C · p. 4]]

^aapp-07-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.
>
> Study: [[Sorting]].

### AAPP-07-009

Please show the pseudo-code of the partitioning algorithm used by Quicksort and report its variants, complexity, and usage in other algorithms. (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=5|2024-11-12-1st · Exercise 4B · p. 5]]

^aapp-07-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> One valid variant is Lomuto partition (inclusive bounds):
> ```text
> PARTITION(A,l,r):
>     x=A[r]; i=l
>     for j=l..r-1:
>         if A[j] <= x: swap(A[i],A[j]); i++
>     swap(A[i],A[r]); return i
> ```
> The invariant has keys $\le x$ before $i$, keys $>x$ in the examined middle region, and unexamined keys ahead of $j$. The returned pivot is in its final rank position. A partition takes $\Theta(r-l+1)$ time and $O(1)$ auxiliary space; it is normally unstable. Randomize by choosing a uniform pivot index and swapping it into $r$ before partitioning. Hoare partition returns a split boundary rather than necessarily a final pivot index; recursion bounds must match it. Three-way partition groups $<x,=x,>x$ and handles many duplicates well. Partition is also used by Quickselect.
>
> Study: [[Sorting]].

### AAPP-07-010

Why is the Counting sort used as the auxiliary algorithm of the Radix sort? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=5|2024-11-12-1st · Exercise 4C · p. 5]]

^aapp-07-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-011

Please discuss the complexity of the partitioning algorithm used by the quick sort. (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=5|2025-01-24-1st · Exercise 4A · p. 5]]

^aapp-07-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> One valid variant is Lomuto partition (inclusive bounds):
> ```text
> PARTITION(A,l,r):
>     x=A[r]; i=l
>     for j=l..r-1:
>         if A[j] <= x: swap(A[i],A[j]); i++
>     swap(A[i],A[r]); return i
> ```
> The invariant has keys $\le x$ before $i$, keys $>x$ in the examined middle region, and unexamined keys ahead of $j$. The returned pivot is in its final rank position. A partition takes $\Theta(r-l+1)$ time and $O(1)$ auxiliary space; it is normally unstable. Randomize by choosing a uniform pivot index and swapping it into $r$ before partitioning. Hoare partition returns a split boundary rather than necessarily a final pivot index; recursion bounds must match it. Three-way partition groups $<x,=x,>x$ and handles many duplicates well. Partition is also used by Quickselect.
>
> Study: [[Sorting]].

### AAPP-07-012

Please discuss the lower bound of the comparison-based sort algorithms. (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=5|2025-02-14-1st · Exercise 4A · p. 5]]

^aapp-07-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.
>
> Study: [[Sorting]].

### AAPP-07-013

Could you please list the characteristics of the counting sort algorithm that make it suitable for use in radix sort? (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=5|2025-02-14-1st · Exercise 4C · p. 5]]

^aapp-07-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-014

Why does quicksort perform poorly in the worst case, and how can this be mitigated? Report the class of algorithms to which it belongs and its average-case complexity. According to the definition, is it an efficient algorithm? (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=4|2025-06-05-1st · Exercise 3A · p. 4]]

^aapp-07-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Quicksort is divide and conquer: partition around a pivot and recursively sort both remaining parts. Consistently extreme pivots give $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$; balanced splits give $\Theta(n\log n)$. Uniform independent random pivots give expected $\Theta(n\log n)$ time for each fixed distinct-key input while retaining the quadratic worst case. This randomized version is Las Vegas: sorting correctness is exact and expected runtime is polynomial, so it is efficient in that theoretical sense. Randomization mitigates input-order sensitivity; three-way partition handles duplicates, and an introspective switch to heapsort can enforce $O(n\log n)$ worst-case time.
>
> Study: [[Sorting#Randomized quicksort]].

### AAPP-07-015

Please discuss why, for many algorithms we have discussed during the lectures, the complexity of the best sorting algorithm is bounded by $O(n\lg n)$. (2)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=3|2026-1-22-1st · Exercise 2A · p. 3]]

^aapp-07-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For distinct keys, a comparison decision tree needs at least $n!$ distinguishable leaves, one for each possible relative order. A binary tree of height $h$ has at most $2^h$ leaves, hence $h\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$. This is a worst-case comparison lower bound, attained asymptotically by merge sort or heapsort. It does not require every input to take that long. Counting sort escapes the comparison-only model by using bounded integer keys as array indices; $\Theta(n+k)$ can be linear when key-range size $k=O(n)$. The printed W is the intended $\Omega$ symbol.
>
> Study: [[Sorting]].

### AAPP-07-016

Please explain why counting sort matters with the radix sort algorithm. (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=3|2026-1-22-1st · Exercise 2B · p. 3]]

^aapp-07-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-017

Explain when the quick sort algorithm falls in the best case or in the worst case recurrence. (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=3|2026-2-09-1st · Exercise 2B · p. 3]]

^aapp-07-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Balanced pivot ranks give $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$; any fixed nontrivial constant-ratio split also has logarithmic height and this order. Repeated smallest/largest pivots give $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$. This concerns the recursion tree over the whole run, not just one good or bad pivot. Equal keys require attention to the partition variant: a two-way implementation can produce extreme splits even after randomization.
>
> Study: [[Sorting#Recursion shape and running time]].

### AAPP-07-018

Explain the role of Counting Sort inside Radix Sort. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=3|2026-6-11-1st · Exercise 2B · p. 3]]

^aapp-07-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

### AAPP-07-019

For randomized Quicksort, explain how the expected running time is obtained from the recurrence induced by a random pivot. Discuss why the worst case remains quadratic. (2)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=3|2026-9-10-1st · Exercise 2A · p. 3]]

^aapp-07-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> With a uniform pivot and distinct keys, its rank $k+1$ is uniform over $k=0,\ldots,n-1$. Both resulting sorts execute, giving $E_n=\frac1n\sum_{k=0}^{n-1}(E_k+E_{n-1-k})+\Theta(n)=\frac2n\sum_{k=0}^{n-1}E_k+\Theta(n)$. Solving by substitution or the comparison-count recurrence gives expected $\Theta(n\log n)$; in particular expected pivot comparisons are $2(n+1)H_n-4n$. Random choices can still repeatedly pick an extreme pivot, so a quadratic execution remains possible. Expectation is over fresh internal randomness for each fixed input, not an assumption that user inputs are uniform.
>
> Study: [[Sorting#Expected-time recurrence]]; [[Sorting#Supplementary exact comparison count]].

### AAPP-07-020

What does it mean for a sorting algorithm to be stable, and why is stability important in Radix Sort? (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=5|2026-9-10-1st · Exercise 3B · p. 5]]

^aapp-07-020

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Counting sort counts keys in a bounded integer range, prefix-sums the frequencies into output positions, and places records into an auxiliary array. Time is $\Theta(n+k)$ and auxiliary storage $\Theta(n+k)$ for $n$ records and $k$ possible keys. Stable placement preserves the relative order of equal-key records (for cumulative end positions, scan input right-to-left). It is not comparison sorting. As a digit pass in LSD radix sort it preserves the ordering established by lower digits; with $d$ digits total time is $\Theta(d(n+k))$. Stability and a modest digit range, rather than merely being a sorting algorithm, make it suitable.
>
> Study: [[Sorting]].

## Selection and order statistics

Related notes: [[Selection and Order Statistics]].

### AAPP-08-001

Describe how the randomized select-ith method work. Is it a Monte Carlo randomization-based algorithm?

Source: [[Tema Esame 2022-06-09-1st.pdf#page=3|2022-06-09-1st · Exercise 2 · p. 3]]

^aapp-08-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> Study: [[Selection and Order Statistics#Randomized selection]].

### AAPP-08-002

Describe the algorithm selecting the ith smallest of n elements (Pseudo code, complexity). (2)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=3|2023-01-17-1st · Exercise 2A · p. 3]]

^aapp-08-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> Study: [[Selection and Order Statistics#Randomized selection]].

### AAPP-08-003

Is there a Select ith smallest of n elements algorithm that runs in linear time in the worst case? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=3|2023-01-17-1st · Exercise 2B · p. 3]]

^aapp-08-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics#Deterministic selection with median of medians]].

### AAPP-08-004

Context: Exercise 2A asks for the algorithm selecting the ith smallest of n elements (pseudocode and complexity). In which class of randomized algorithms could the algorithm described in A be inserted? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=3|2023-01-17-1st · Exercise 2C · p. 3]]

^aapp-08-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> Study: [[Selection and Order Statistics#Randomized selection]].

### AAPP-08-005

Please describe how the partitioning work in the “Select the ith smallest of n elements” algorithm. How is it randomized? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=3|2024-01-26-1st · Exercise 2A · p. 3]]

^aapp-08-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> Study: [[Selection and Order Statistics#Randomized selection]].

### AAPP-08-006

Please describe the “Select the i th smallest of n elements” algorithm and its key properties. How is it randomized? (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=3|2024-07-24-1st · Exercise 2B · p. 3]]

^aapp-08-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> Study: [[Selection and Order Statistics#Randomized selection]].

### AAPP-08-007

Please discuss the different variants of the Select-ith algorithm. (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=5|2025-01-24-1st · Exercise 4B · p. 5]]

^aapp-08-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> For deterministic pivot_rule, use the following construction.
>
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics]].

### AAPP-08-008

Describe the Select-ith deterministic algorithm and its complexity. Why is dividing into groups of 5 critical for the deterministic Select-ith algorithm’s performance? (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=5|2025-06-05-1st · Exercise 4B · p. 5]]

^aapp-08-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics#Deterministic selection with median of medians]].

### AAPP-08-009

What are the differences between the randomized and deterministic algorithms for solving the Select-ith problem? (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=5|2025-07-04-1st · Exercise 4B · p. 5]]

^aapp-08-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> For deterministic pivot_rule, use the following construction.
>
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics]].

### AAPP-08-010

Please explain how the “Select the i th smallest of n elements” can be solved (pseudo code required) and what kind of complexity we may expect from the reported solutions. (2)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=3|2025-11-06-1st · Exercise 2A · p. 3]]

^aapp-08-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> For deterministic pivot_rule, use the following construction.
>
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics]].

### AAPP-08-011

Both RAND-SELECT and SELECT find the i-th order statistic, but only SELECT guarantees worst-case time complexity. What specific pivot-selection mechanism does SELECT use to limit the size of the largest recursive subproblem, and how does that guarantee lead to the worst-case bound (i.e., what fraction of elements is discarded each step)? (2)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=3|2026-2-09-1st · Exercise 2A · p. 3]]

^aapp-08-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics#Deterministic selection with median of medians]].

### AAPP-08-012

What are the differences between the randomized and deterministic algorithms for solving the Select-ith problem (pseudo code required)? (1)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=5|2026-6-29-1st · Exercise 3B · p. 5]]

^aapp-08-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a 1-based desired rank $i$ and partition into three groups, which also handles duplicate keys:
> ```text
> SELECT(A,i,pivot_rule):
>     if |A| <= constant: sort A; return A[i]
>     x = pivot_rule(A)
>     partition A into L (<x), E (=x), G (>x)
>     if i <= |L|: return SELECT(L,i,pivot_rule)
>     if i <= |L|+|E|: return x
>     return SELECT(G,i-|L|-|E|,pivot_rule)
> ```
> Randomized Quickselect chooses $x$ uniformly from the current interval. Partition is linear; only the side containing the requested rank is recursively solved. Expected time is $\Theta(n)$, worst-case $\Theta(n^2)$, and correctness is exact: Las Vegas, not Monte Carlo. In-place partition avoids copying the subarrays; an iterative outer selection loop can avoid a linear recursion stack.
>
> For deterministic pivot_rule, use the following construction.
>
> Deterministic SELECT uses median of medians: split into full groups of five, find each group's median in constant time, recursively select the median of those medians, then partition the entire input and recurse only on the desired rank's side. Retain leftover elements for partitioning. At least $3n/10-O(1)$ elements are certified on either inclusive side, so the larger recursive partition has at most $7n/10+O(1)$ elements. Thus $T(n)\le T(n/5)+T(7n/10+O(1))+O(n)=O(n)$; the fractions sum to less than one, leaving linear slack. The lecture's looser $3n/4$ side bound also proves linearity. Groups of three give no such slack in the simple proof; five is sufficient, not the only possible group size.
>
> Study: [[Selection and Order Statistics]].

## Primality testing

Related notes: [[Primality Testing and Cryptosystems]].

### AAPP-09-001

Which is the type/class of randomized algorithms used by the primality testing algorithms presented during the lectures? (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=3|2024-01-26-1st · Exercise 2C · p. 3]]

^aapp-09-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

### AAPP-09-002

Describe the ideas behind the primality test algorithm presented during the lectures. Which class of randomized approach does it belong to? (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=5|2025-01-24-1st · Exercise 4C · p. 5]]

^aapp-09-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

### AAPP-09-003

Could you explain which aspects of primality testing use randomization and how that process works? Additionally, would you classify it as a Las Vegas randomized algorithm? (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=4|2025-02-14-1st · Exercise 3A · p. 4]]
Source: [[Tema Esame 2026-6-29-1st.pdf#page=7|2026-6-29-1st · Exercise 4B · p. 7]]

^aapp-09-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

### AAPP-09-004

Please describe how the primality test, presented during the lectures, works, and specify which class of randomization it belongs to. (2)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=7|2025-11-06-1st · Exercise 4B · p. 7]]

^aapp-09-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

### AAPP-09-005

Could you explain which aspects of primality testing we have seen during the lectures that use randomization? Additionally, would you classify it as a Monte Carlo or Las Vegas randomized algorithm? (2)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=7|2026-1-22-1st · Exercise 4A · p. 7]]

^aapp-09-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

### AAPP-09-006

Describe the randomized primality testing algorithm presented in class, including its randomized-algorithm classification. (2)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=6|2026-6-11-1st · Exercise 3C · p. 6]]

^aapp-09-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

### AAPP-09-007

Describe the ideas behind the primality test algorithm presented during the lectures. Which class of randomized approach does it belong to? (2)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=7|2026-9-10-1st · Exercise 4A · p. 7]]

^aapp-09-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture uses random modular witnesses: choose fresh uniform bases, compute powers modulo the candidate by repeated squaring, and reject when Fermat's congruence fails or a nontrivial square root of 1 is found. Handle $n<2$, small primes, and even candidates separately. In standard Miller–Rabin form, write $n-1=2^sd$ with odd $d$; calculate $a^d\bmod n$ and repeatedly square. A round passes if the initial residue is 1 or some tested residue is $-1\bmod n$; otherwise it certifies COMPOSITE.
>
> This is one-sided Monte Carlo, not Las Vegas: a prime always passes, whereas a composite may be reported POSSIBLY-PRIME. For an odd composite, independent uniform bases in the standard domain $[2,n-2]$ give error at most $4^{-k}$ after $k$ rounds. COMPOSITE is certain; a pass is not a proof. This probability is conditional on a fixed composite input, not a posterior probability about an arbitrary passing candidate. Each round uses $O(\log n)$ modular multiplications; bit complexity is polynomial in the bit length, with multiplication cost included. The notes qualify the slide's printed base-count/domain claim; use the standard domain and error statement.
>
> Study: [[Primality Testing and Cryptosystems#Modular exponentiation with a witness check]]; [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].

## Dynamic programming and LCS

Related notes: [[Dynamic Programming and LCS]].

### AAPP-10-001

Discuss why dynamic programming matter for Longest common subsequence algorithm.

Source: [[Tema Esame 2022-01-14-1st.pdf#page=2|2022-01-14-1st · Exercise 1 · p. 2]]

^aapp-10-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-002

Discuss an example of dynamic programming based algorithm. Which are the key features of an algorithm for being classified as a dynamic programming algorithm?

Source: [[Tema Esame 2022-09-07-1st.pdf#page=3|2022-09-07-1st · Exercise 2 · p. 3]]

^aapp-10-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-003

Describe the Longest Common Subsequence (LCS) algorithm. (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=3|2022-11-08-1st · Exercise 2A · p. 3]]

^aapp-10-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-004

What kind of temporal or spatial complexity has LCS? (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=3|2022-11-08-1st · Exercise 2B · p. 3]]

^aapp-10-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> For the standard full-table LCS algorithm on lengths $m,n$, auxiliary space is $\Theta(mn)$, with at most $O(m+n)$ traceback/recursive-stack cost. If only the length is needed, two rows (or a careful one-row update) reduce auxiliary space to $O(\min(m,n))$, keeping $\Theta(mn)$ time. The ordinary traceback cannot be used after discarding its table. A witness in linear auxiliary space requires a separate reconstruction method such as Hirschberg, not just deletion of old rows. State whether the task asks for a length or an actual subsequence.
>
> Study: [[Dynamic Programming and LCS#Reducing space and preserving the right claim]].

### AAPP-10-005

LCS is classified as a dynamic programming algorithm. Why? (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=3|2022-11-08-1st · Exercise 2C · p. 3]]

^aapp-10-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-006

Please explain why an algorithm could be classified as a Dynamic programming algorithm. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=4|2023-06-19-1st · Exercise 3A · p. 4]]

^aapp-10-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.
>
> For a concrete repeated state, with both final symbols unequal, branches $(m-1,n)$ and $(m,n-1)$ can both request $(m-1,n-1)$. Cache by the complete state pair. An UNSEEN marker must differ from 0, which is a valid LCS length.
>
> Study: [[Dynamic Programming and LCS#Memoization: solve each requested state once]].

### AAPP-10-007

Detail the Longest Common Subsequence algorithm: pseudo code and space and temporal complexity. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=5|2023-07-11-1st · Exercise 4A · p. 5]]

^aapp-10-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-008

What kind of spatial complexity has the longest common subsequence problem? (1).

Source: [[Tema Esame 2023-11-09-1st.pdf#page=3|2023-11-09-1st · Exercise 2B · p. 3]]

^aapp-10-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For the standard full-table LCS algorithm on lengths $m,n$, auxiliary space is $\Theta(mn)$, with at most $O(m+n)$ traceback/recursive-stack cost. If only the length is needed, two rows (or a careful one-row update) reduce auxiliary space to $O(\min(m,n))$, keeping $\Theta(mn)$ time. The ordinary traceback cannot be used after discarding its table. A witness in linear auxiliary space requires a separate reconstruction method such as Hirschberg, not just deletion of old rows. State whether the task asks for a length or an actual subsequence.
>
> Study: [[Dynamic Programming and LCS#Reducing space and preserving the right claim]].

### AAPP-10-009

Why does spatial complexity matter for all dynamic programming algorithms? (1)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=3|2023-11-09-1st · Exercise 2C · p. 3]]

^aapp-10-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming saves repeated computation by retaining state results, so storage can determine feasibility: a polynomial-time table may still be too large, while memoizing an exponential state space does not make it small. Count the states, information per state and recursion stack, and retain only live dependencies where possible. LCS illustrates the tradeoff.
>
> For the standard full-table LCS algorithm on lengths $m,n$, auxiliary space is $\Theta(mn)$, with at most $O(m+n)$ traceback/recursive-stack cost. If only the length is needed, two rows (or a careful one-row update) reduce auxiliary space to $O(\min(m,n))$, keeping $\Theta(mn)$ time. The ordinary traceback cannot be used after discarding its table. A witness in linear auxiliary space requires a separate reconstruction method such as Hirschberg, not just deletion of old rows. State whether the task asks for a length or an actual subsequence.
>
> Study: [[Dynamic Programming and LCS#Reducing space and preserving the right claim]].

### AAPP-10-010

What kind of time complexity has the longest common subsequence problem (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=3|2024-01-26-1st · Exercise 2B · p. 3]]

^aapp-10-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The standard dynamic-programming LCS table takes $\Theta(mn)$ time for sequence lengths $m,n$, since it evaluates $mn$ constant-cost states. This is $\Theta(n^2)$ when both lengths are $n$. Naive uncached recursion can be exponential; a memoized algorithm evaluates only reached states, but a fully allocated/initialized dense table still has $\Theta(mn)$ overhead.
>
> Study: [[Dynamic Programming and LCS#Bottom-up tabulation]].

### AAPP-10-011

Please discuss how the longest common subsequence works. What about its complexity? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=4|2024-02-16-1st · Exercise 3A · p. 4]]

^aapp-10-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-012

Please discuss the key property of the longest common subsequence. In which class of algorithm can be inserted? Why? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=5|2024-07-24-1st · Exercise 4A · p. 5]]

^aapp-10-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-013

To which class does the Longest Common Subsequence Algorithm belong? How is its complexity evaluated? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=3|2024-09-05-1st · Exercise 2C · p. 3]]

^aapp-10-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-014

In class, we studied an algorithm that shows the main hallmarks of dynamic programming. Describe the algorithm and its complexity, and why it is classified as a good dynamic programming example. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=3|2025-07-04-1st · Exercise 2A · p. 3]]

^aapp-10-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-015

What properties and algorithmic steps are required to convert a divide-and-conquer solution into a dynamic programming solution? (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=6|2025-11-06-1st · Exercise 3C · p. 6]]

^aapp-10-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.
>
> For a concrete repeated state, with both final symbols unequal, branches $(m-1,n)$ and $(m,n-1)$ can both request $(m-1,n-1)$. Cache by the complete state pair. An UNSEEN marker must differ from 0, which is a valid LCS length.
>
> Study: [[Dynamic Programming and LCS#Memoization: solve each requested state once]].

### AAPP-10-016

Please describe a problem that is typically solved by a divide‑and‑conquer strategy, yet also admits a dynamic‑programming formulation. In your explanation, highlight how memoization is employed. (2)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=6|2026-1-22-1st · Exercise 3C · p. 6]]

^aapp-10-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.
>
> For a concrete repeated state, with both final symbols unequal, branches $(m-1,n)$ and $(m,n-1)$ can both request $(m-1,n-1)$. Cache by the complete state pair. An UNSEEN marker must differ from 0, which is a valid LCS length.
>
> Study: [[Dynamic Programming and LCS#Memoization: solve each requested state once]].

### AAPP-10-017

What kind of spatial complexity does the longest common subsequence problem have? (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=5|2026-2-09-1st · Exercise 3A · p. 5]]

^aapp-10-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For the standard full-table LCS algorithm on lengths $m,n$, auxiliary space is $\Theta(mn)$, with at most $O(m+n)$ traceback/recursive-stack cost. If only the length is needed, two rows (or a careful one-row update) reduce auxiliary space to $O(\min(m,n))$, keeping $\Theta(mn)$ time. The ordinary traceback cannot be used after discarding its table. A witness in linear auxiliary space requires a separate reconstruction method such as Hirschberg, not just deletion of old rows. State whether the task asks for a length or an actual subsequence.
>
> Study: [[Dynamic Programming and LCS#Reducing space and preserving the right claim]].

### AAPP-10-018

Detail the Longest Common Subsequence algorithm: pseudo code, space, and temporal complexity. (2)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=7|2026-6-11-1st · Exercise 4A · p. 7]]

^aapp-10-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For sequences $X[1..m],Y[1..n]$, let $C[i,j]$ be the LCS length of their prefixes. Set $C[i,0]=C[0,j]=0$. If $X[i]=Y[j]$, use $C[i,j]=1+C[i-1,j-1]$; otherwise use $\max(C[i-1,j],C[i,j-1])$. Fill the table in increasing prefix lengths:
> ```text
> for i=1..m:
>     for j=1..n:
>         if X[i]==Y[j]: C[i,j]=C[i-1,j-1]+1
>         else: C[i,j]=max(C[i-1,j],C[i,j-1])
> return C[m,n]
> ```
> The $mn$ states each require constant work: $\Theta(mn)$ time and table space. Trace backward through matches and maximizing predecessors to reconstruct a subsequence in $O(m+n)$ additional time. Dynamic programming is appropriate because optimal prefix solutions combine correctly and the naive recursion repeatedly requests the same prefix pairs. Memoization or tabulation evaluates each state once.
>
> Study: [[Dynamic Programming and LCS]].

### AAPP-10-019

What is memoization, and why is it useful in Dynamic Programming? Give an example of a repeated subproblem for which memoization avoids recomputation. (1)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=4|2026-9-10-1st · Exercise 2C · p. 4]]

^aapp-10-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.
>
> For a concrete repeated state, with both final symbols unequal, branches $(m-1,n)$ and $(m,n-1)$ can both request $(m-1,n-1)$. Cache by the complete state pair. An UNSEEN marker must differ from 0, which is a valid LCS length.
>
> Study: [[Dynamic Programming and LCS#Memoization: solve each requested state once]].

## BDDs and memoization

Related notes: [[Binary Decision Diagrams]], [[Dynamic Programming and LCS#Memoization: solve each requested state once|LCS memoization]].

### AAPP-11-001

Please explain what the memoization technique is meant for and where it matters. (2)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=4|2023-02-14-1st · Exercise 3A · p. 4]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=4|2025-09-05-1st · Exercise 3A · p. 4]]

^aapp-11-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.
>
> BDD operations cache tuples of operand handles in the computed table; a node unique table provides structural sharing, which is a separate job.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

### AAPP-11-002

Why the BDD data structure can be classified as an example of dynamic programming. (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=3|2023-11-09-1st · Exercise 2A · p. 3]]

^aapp-11-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Memoization is top-down dynamic programming on operand states. For ITE, choose the earliest variable among the three arguments, recursively compute its two cofactor results, and construct one reduced node:
> ```text
> ITE(f,g,h):
>     if f==1: return g
>     if f==0: return h
>     if g==h: return g
>     if cache contains (f,g,h): return cache[(f,g,h)]
>     v=earliest top variable of f,g,h
>     hi=ITE(f|v=1,g|v=1,h|v=1)
>     lo=ITE(f|v=0,g|v=0,h|v=0)
>     r=MAKE_UNIQUE(v,hi,lo)
>     cache[(f,g,h)]=r; return r
> ```
> An operand that does not depend on $v$ is unchanged by either cofactor. With ideal retention and expected constant-time hashing, there are at most $N_fN_gN_h$ operand triples, so time is $O(N_fN_gN_h)$; binary Apply has an $O(N_fN_g)$ bound. Without the computed table, reconvergent assignment paths can repeatedly expand the same state exponentially in variable count even while the unique table keeps the result compact. Neither result size alone nor a finite lossy cache guarantees the ideal once-per-state bound.
>
> Study: [[Binary Decision Diagrams#What memoization does to complexity]].

### AAPP-11-003

Please explain the differences between “Computed table” and “Unique table” with BDDs. Why are they used? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=5|2024-01-26-1st · Exercise 4B · p. 5]]

^aapp-11-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

### AAPP-11-004

What is the Unique Table, and what is it used for in ROBDDs? Does it also have to do with the canonicity of ROBDD? (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=5|2024-06-26-1st · Exercise 4A · p. 5]]

^aapp-11-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

### AAPP-11-005

What is the Computed Table, and what is it used for in ROBDDs? Does it also have to do with the canonicity of ROBDD? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=5|2024-09-05-1st · Exercise 4B · p. 5]]

^aapp-11-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

### AAPP-11-006

What is meant by the memoization technique, and in which class of algorithm does it matter? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=3|2024-11-12-1st · Exercise 2C · p. 3]]

^aapp-11-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Dynamic programming defines a finite set of states with reusable overlapping subproblems and a dependency order. For optimization, establish optimal substructure, derive base cases and a correct recurrence, then memoize recursive results or tabulate in a topological order. Time is the number of reached states plus transitions, rather than the size of the expanded recursion tree. Acyclic dependencies or another well-founded solution method are required. LCS is an example: prefix pairs $(i,j)$ repeat, so storing each result turns exponential naive branching into $\Theta(mn)$ worst-case table evaluation. Independent divide-and-conquer subproblems do not benefit merely from adding a cache.
>
> BDD operations cache tuples of operand handles in the computed table; a node unique table provides structural sharing, which is a separate job.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

### AAPP-11-007

"Why can BDD be considered an example of a data structure that exploits dynamic programming? How does asymptotic complexity change with memoization?" (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=3|2025-01-24-1st · Exercise 2B · p. 3]]

^aapp-11-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Memoization is top-down dynamic programming on operand states. For ITE, choose the earliest variable among the three arguments, recursively compute its two cofactor results, and construct one reduced node:
> ```text
> ITE(f,g,h):
>     if f==1: return g
>     if f==0: return h
>     if g==h: return g
>     if cache contains (f,g,h): return cache[(f,g,h)]
>     v=earliest top variable of f,g,h
>     hi=ITE(f|v=1,g|v=1,h|v=1)
>     lo=ITE(f|v=0,g|v=0,h|v=0)
>     r=MAKE_UNIQUE(v,hi,lo)
>     cache[(f,g,h)]=r; return r
> ```
> An operand that does not depend on $v$ is unchanged by either cofactor. With ideal retention and expected constant-time hashing, there are at most $N_fN_gN_h$ operand triples, so time is $O(N_fN_gN_h)$; binary Apply has an $O(N_fN_g)$ bound. Without the computed table, reconvergent assignment paths can repeatedly expand the same state exponentially in variable count even while the unique table keeps the result compact. Neither result size alone nor a finite lossy cache guarantees the ideal once-per-state bound.
>
> Study: [[Binary Decision Diagrams#What memoization does to complexity]].

### AAPP-11-008

Please discuss the role of the computed table on BDD ITE operation. How does the ITE asymptotic complexity change with this table?" (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=3|2025-02-14-1st · Exercise 2B · p. 3]]

^aapp-11-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Memoization is top-down dynamic programming on operand states. For ITE, choose the earliest variable among the three arguments, recursively compute its two cofactor results, and construct one reduced node:
> ```text
> ITE(f,g,h):
>     if f==1: return g
>     if f==0: return h
>     if g==h: return g
>     if cache contains (f,g,h): return cache[(f,g,h)]
>     v=earliest top variable of f,g,h
>     hi=ITE(f|v=1,g|v=1,h|v=1)
>     lo=ITE(f|v=0,g|v=0,h|v=0)
>     r=MAKE_UNIQUE(v,hi,lo)
>     cache[(f,g,h)]=r; return r
> ```
> An operand that does not depend on $v$ is unchanged by either cofactor. With ideal retention and expected constant-time hashing, there are at most $N_fN_gN_h$ operand triples, so time is $O(N_fN_gN_h)$; binary Apply has an $O(N_fN_g)$ bound. Without the computed table, reconvergent assignment paths can repeatedly expand the same state exponentially in variable count even while the unique table keeps the result compact. Neither result size alone nor a finite lossy cache guarantees the ideal once-per-state bound.
>
> Study: [[Binary Decision Diagrams#What memoization does to complexity]].

### AAPP-11-009

How do the unique table and computed table contribute to the efficiency and canonicity of BDDs?" (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=3|2025-06-05-1st · Exercise 2B · p. 3]]

^aapp-11-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

### AAPP-11-010

Why do we mention the BDD computed tables as an example of Dynamic programming? Please provide a pseudo-code example of its usage. (2)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=5|2025-11-06-1st · Exercise 3A · p. 5]]

^aapp-11-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Memoization is top-down dynamic programming on operand states. For ITE, choose the earliest variable among the three arguments, recursively compute its two cofactor results, and construct one reduced node:
> ```text
> ITE(f,g,h):
>     if f==1: return g
>     if f==0: return h
>     if g==h: return g
>     if cache contains (f,g,h): return cache[(f,g,h)]
>     v=earliest top variable of f,g,h
>     hi=ITE(f|v=1,g|v=1,h|v=1)
>     lo=ITE(f|v=0,g|v=0,h|v=0)
>     r=MAKE_UNIQUE(v,hi,lo)
>     cache[(f,g,h)]=r; return r
> ```
> An operand that does not depend on $v$ is unchanged by either cofactor. With ideal retention and expected constant-time hashing, there are at most $N_fN_gN_h$ operand triples, so time is $O(N_fN_gN_h)$; binary Apply has an $O(N_fN_g)$ bound. Without the computed table, reconvergent assignment paths can repeatedly expand the same state exponentially in variable count even while the unique table keeps the result compact. Neither result size alone nor a finite lossy cache guarantees the ideal once-per-state bound.
>
> Study: [[Binary Decision Diagrams#What memoization does to complexity]].

### AAPP-11-011

Explain the different roles of the unique table and the computed table. Give a scenario where the unique table alone is insufficient to avoid exponential time, and the computed table fixes it. (2)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=7|2026-2-09-1st · Exercise 4A · p. 7]]

^aapp-11-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Memoization is top-down dynamic programming on operand states. For ITE, choose the earliest variable among the three arguments, recursively compute its two cofactor results, and construct one reduced node:
> ```text
> ITE(f,g,h):
>     if f==1: return g
>     if f==0: return h
>     if g==h: return g
>     if cache contains (f,g,h): return cache[(f,g,h)]
>     v=earliest top variable of f,g,h
>     hi=ITE(f|v=1,g|v=1,h|v=1)
>     lo=ITE(f|v=0,g|v=0,h|v=0)
>     r=MAKE_UNIQUE(v,hi,lo)
>     cache[(f,g,h)]=r; return r
> ```
> An operand that does not depend on $v$ is unchanged by either cofactor. With ideal retention and expected constant-time hashing, there are at most $N_fN_gN_h$ operand triples, so time is $O(N_fN_gN_h)$; binary Apply has an $O(N_fN_g)$ bound. Without the computed table, reconvergent assignment paths can repeatedly expand the same state exponentially in variable count even while the unique table keeps the result compact. Neither result size alone nor a finite lossy cache guarantees the ideal once-per-state bound.
>
> Study: [[Binary Decision Diagrams#What memoization does to complexity]].

### AAPP-11-012

Please explain the differences between the computed table and the unique table in the context of BDDs. Which one is more closely related to dynamic programming algorithms? (2)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=7|2026-6-29-1st · Exercise 4A · p. 7]]

^aapp-11-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The unique table interns node triples $(variable,high,low)$; if children coincide, eliminate the test, otherwise reuse the existing node or allocate one. Together with a fixed variable order and reduction rules, this maintains canonical ROBDD representation. The computed table caches operation states, for example $(ITE,f,g,h)\mapsto result$, to avoid repeating recursion on shared subgraphs. It improves runtime rather than defining canonicity; eviction may cause recomputation without changing answers. Interning an output node does not avoid the work already spent recomputing its operands. Hash tables must compare full keys, including after collisions.
>
> Study: [[Binary Decision Diagrams#Unique table and computed table]].

## Treaps

Related notes: [[Randomized Data Structures#Treaps: a search tree and a priority heap|Randomized Data Structures — treaps]].

### AAPP-12-001

Describe how treap Union works.

Source: [[Tema Esame 2022-02-11-1st.pdf#page=2|2022-02-11-1st · Exercise 1 · p. 2]]

^aapp-12-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-002

Describe how Treap split/union works.

Source: [[Tema Esame 2022-09-07-1st.pdf#page=4|2022-09-07-1st · Exercise 3 · p. 4]]

^aapp-12-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-003

Describe how Treap split/union works.? (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=4|2022-11-08-1st · Exercise 3B · p. 4]]

^aapp-12-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-004

Describe the treap data structure, how the search is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=4|2023-06-19-1st · Exercise 3B · p. 4]]

^aapp-12-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a BST on keys and, in the lecture, a min-heap on distinct independent random priorities. Comparisons search as in a BST, so correctness holds for every valid shape. The priority order randomizes shape independently of key arrival order. Under the standard fixed-operation-sequence model, searches and updates cost $O(\log n)$ expected, but a chain gives $O(n)$ worst case. Searches do not perform rotations. Updating heap order uses rotations that preserve BST order; fewer than two expected rotations per ordinary insertion/deletion does not make the preceding search constant time.
>
> Study: [[Randomized Data Structures#Search and harmonic path lengths]].

### AAPP-12-005

Describe the treap data structure and how the split is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=4|2023-09-11-1st · Exercise 3B · p. 4]]

^aapp-12-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-006

Please provide the implementation of the split operation for Treaps. What is the operation complexity? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=4|2024-01-26-1st · Exercise 3B · p. 4]]

^aapp-12-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-007

Please provide the implementation of the union operation for Treaps. What is the operation complexity? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=4|2024-02-16-1st · Exercise 3B · p. 4]]

^aapp-12-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-008

Please discuss the key properties of a Treap and of its search function. (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=4|2024-06-26-1st · Exercise 3A · p. 4]]

^aapp-12-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a BST on keys and, in the lecture, a min-heap on distinct independent random priorities. Comparisons search as in a BST, so correctness holds for every valid shape. The priority order randomizes shape independently of key arrival order. Under the standard fixed-operation-sequence model, searches and updates cost $O(\log n)$ expected, but a chain gives $O(n)$ worst case. Searches do not perform rotations. Updating heap order uses rotations that preserve BST order; fewer than two expected rotations per ordinary insertion/deletion does not make the preceding search constant time.
>
> Study: [[Randomized Data Structures#Search and harmonic path lengths]].

### AAPP-12-009

Please discuss how a Union is implemented in a Treap Data-Structure. How does the number of rotations impact the search for an element in a Treap? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=4|2024-07-24-1st · Exercise 3A · p. 4]]

^aapp-12-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> A treap is a BST on keys and, in the lecture, a min-heap on distinct independent random priorities. Comparisons search as in a BST, so correctness holds for every valid shape. The priority order randomizes shape independently of key arrival order. Under the standard fixed-operation-sequence model, searches and updates cost $O(\log n)$ expected, but a chain gives $O(n)$ worst case. Searches do not perform rotations. Updating heap order uses rotations that preserve BST order; fewer than two expected rotations per ordinary insertion/deletion does not make the preceding search constant time.
>
> Study: [[Randomized Data Structures]].

### AAPP-12-010

Why does randomized Treap structure have a complexity on average similar to a balanced binary tree? Treap required all priorities to be pairwise distinct. How can this property be satisfied? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=4|2024-09-05-1st · Exercise 3A · p. 4]]

^aapp-12-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a BST on keys and, in the lecture, a min-heap on distinct independent random priorities. Comparisons search as in a BST, so correctness holds for every valid shape. The priority order randomizes shape independently of key arrival order. Under the standard fixed-operation-sequence model, searches and updates cost $O(\log n)$ expected, but a chain gives $O(n)$ worst case. Searches do not perform rotations. Updating heap order uses rotations that preserve BST order; fewer than two expected rotations per ordinary insertion/deletion does not make the preceding search constant time.
>
> Independent continuous random priorities are distinct with probability one. For finite random bit strings, collisions are possible: the lecture extends and stores additional random bits when priorities cannot yet be distinguished. Keep each node's resulting priority stable across comparisons. A sufficiently wide finite random priority with explicit tie-breaking is another implementation convention, but exact distributional claims must match it. Independent random priority order gives the same shape distribution as a random-order BST, hence logarithmic expected search paths; it does not guarantee a deterministically balanced tree.
>
> Study: [[Randomized Data Structures#Sampling priorities and handling ties]].

### AAPP-12-011

Please discuss how a Split is implemented in a Treap Data-Structure. What happen in case the k element is in the initial Treap? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=4|2024-09-05-1st · Exercise 3B · p. 4]]

^aapp-12-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-012

Describe how the split for Treaps data structure works and discuss its complexity. (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=4|2024-11-12-1st · Exercise 3B · p. 4]]

^aapp-12-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-013

Describe how the split and the union work in a treap and discuss their complexity. (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=4|2025-02-14-1st · Exercise 3B · p. 4]]

^aapp-12-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-014

Describe how the union and the split work in a treap and discuss its complexity. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=4|2025-07-04-1st · Exercise 3B · p. 4]]

^aapp-12-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-015

Describe how the union for Treaps data structure works and discuss its complexity. (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=4|2025-11-06-1st · Exercise 2C · p. 4]]

^aapp-12-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-016

Describe how the split for Treaps data structure works and discuss its complexity. (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=4|2026-1-22-1st · Exercise 2C · p. 4]]

^aapp-12-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-017

Treap required all priorities to be pairwise distinct. How can this property be satisfied? (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=5|2026-2-09-1st · Exercise 3B · p. 5]]

^aapp-12-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Independent continuous random priorities are distinct with probability one. For finite random bit strings, collisions are possible: the lecture extends and stores additional random bits when priorities cannot yet be distinguished. Keep each node's resulting priority stable across comparisons. A sufficiently wide finite random priority with explicit tie-breaking is another implementation convention, but exact distributional claims must match it. Independent random priority order gives the same shape distribution as a random-order BST, hence logarithmic expected search paths; it does not guarantee a deterministically balanced tree.
>
> Study: [[Randomized Data Structures#Sampling priorities and handling ties]].

### AAPP-12-018

Please describe how the treap split works. (1)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=5|2026-6-11-1st · Exercise 3A · p. 5]]

^aapp-12-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> Split returns keys $\le k$ and keys $>k$, including an existing key $k$ in the first output:
> ```text
> SPLIT(T,k):
>     if T==NIL: return (NIL,NIL)
>     if T.key<=k:
>         (L,R)=SPLIT(T.right,k); T.right=L; return (T,R)
>     (L,R)=SPLIT(T.left,k); T.left=R; return (L,T)
> ```
> Only a search path changes. Expected time is $O(\log n)$, worst case $O(n)$. The lecture's equivalent dummy-root method inserts a separator with priority $-\infty$, rotates it to the root, then detaches/discards it rather than joining the children back together. If $k$ already exists, remove its record before dummy insertion and reinsert it, with its data/priority, in the $\le k$ output. Direct recursion above avoids needing an artificial separator key.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

### AAPP-12-019

Please describe how the treap union works. (1)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=5|2026-6-29-1st · Exercise 3A · p. 5]]

^aapp-12-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A treap is a binary search tree on keys and a min-heap on distinct random priorities.
>
> The lecture's Union is ordered join: **every key of L is smaller than every key of R**. It is not unrestricted overlapping set union.
> ```text
> JOIN(L,R):
>     if L==NIL: return R
>     if R==NIL: return L
>     if L.priority<R.priority:
>         L.right=JOIN(L.right,R); return L
>     R.left=JOIN(L,R.left); return R
> ```
> Choose the smaller-priority root and recursively join the one boundary subtree; both invariants are preserved. Expected cost is $O(\log(n_L+n_R))$, worst case linear. The lecture also creates a dummy root between the two key ranges, attaches both trees, then deletes that root through rotations. An ordered universe may lack an intermediate representable key, so the direct routine is more general. The constant expected rotation bound for an ordinary random-priority insertion does not apply to a forced-priority dummy.
>
> Study: [[Randomized Data Structures#Split and the restricted Union]].

## Skip lists

Related notes: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list|Randomized Data Structures — skip lists]].

### AAPP-13-001

Discuss how skip list insertion work? What about its worst vs average case complexity?

Source: [[Tema Esame 2022-06-09-1st.pdf#page=4|2022-06-09-1st · Exercise 3 · p. 4]]

^aapp-13-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Find the insertion position and record each level's predecessor. Sample a new tower height by independent coin flips, insert the node in the bottom list, and splice its forward pointers at each level it occupies; extend the header if needed. Preserve sorted order and the fact that higher levels are subsets of lower ones. Expected search-plus-update time is $O(\log n)$ and expected new pointers are constant for promotion probability $1/2$. Worst-case search can cost $O(n)$ with a customary bounded height; in an uncapped model state the bound in terms of the realized height as well. Searches and deletion do not resample stored heights.
>
> Study: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].

### AAPP-13-002

Describe the skip-list data structure, how the search is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=4|2023-02-14-1st · Exercise 3B · p. 4]]

^aapp-13-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Study: [[Randomized Data Structures#Search: right while safe, otherwise down]].

### AAPP-13-003

Describe the skip list data structure and how the union is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=4|2023-07-11-1st · Exercise 3B · p. 4]]

^aapp-13-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> A general correct union construction merges the two sorted bottom lists, resolves duplicate-key records under an explicit policy, then rebuilds a skip list on the merged keys using independent geometric heights. This takes $O(n+m)$ expected time and storage, including expected pointer creation. Ordered concatenation can instead reconnect boundary pointers, but needs the precondition that all keys in the first list precede all keys in the second. The supplied deck does not specify one unique skip-list union algorithm; this is an explicit construction, not a claim about an unseen marking scheme.
>
> Study: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].

### AAPP-13-004

Describe how the search for skip-list data structure works. (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=4|2023-11-09-1st · Exercise 3B · p. 4]]

^aapp-13-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Study: [[Randomized Data Structures#Search: right while safe, otherwise down]].

### AAPP-13-005

Describe how the insertion for skip-list data structure works. What about its complexity? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=4|2024-07-24-1st · Exercise 3B · p. 4]]

^aapp-13-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Find the insertion position and record each level's predecessor. Sample a new tower height by independent coin flips, insert the node in the bottom list, and splice its forward pointers at each level it occupies; extend the header if needed. Preserve sorted order and the fact that higher levels are subsets of lower ones. Expected search-plus-update time is $O(\log n)$ and expected new pointers are constant for promotion probability $1/2$. Worst-case search can cost $O(n)$ with a customary bounded height; in an uncapped model state the bound in terms of the realized height as well. Searches and deletion do not resample stored heights.
>
> Study: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].

### AAPP-13-006

Describe how the search for Skip-list data structure works and discuss its complexity. (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=4|2025-01-24-1st · Exercise 3B · p. 4]]

^aapp-13-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Study: [[Randomized Data Structures#Search: right while safe, otherwise down]].

### AAPP-13-007

Describe how the insert for the Skip-list data structure works and discuss its complexity. (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=4|2025-06-05-1st · Exercise 3B · p. 4]]

^aapp-13-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Find the insertion position and record each level's predecessor. Sample a new tower height by independent coin flips, insert the node in the bottom list, and splice its forward pointers at each level it occupies; extend the header if needed. Preserve sorted order and the fact that higher levels are subsets of lower ones. Expected search-plus-update time is $O(\log n)$ and expected new pointers are constant for promotion probability $1/2$. Worst-case search can cost $O(n)$ with a customary bounded height; in an uncapped model state the bound in terms of the realized height as well. Searches and deletion do not resample stored heights.
>
> Study: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].

### AAPP-13-008

Describe the skip list data structure and how the search is performed, and what the complexity is. (2)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=5|2025-09-05-1st · Exercise 4B · p. 5]]

^aapp-13-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Study: [[Randomized Data Structures#Search: right while safe, otherwise down]].

### AAPP-13-009

Describe how the insert for the skip-list data structure works and discuss its complexity. (1)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=4|2026-2-09-1st · Exercise 2C · p. 4]]

^aapp-13-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A skip list has a sorted bottom list containing every key, and progressively sparser upper levels of forward shortcuts. Search starts at the highest header, advances while the next key is smaller than the target, then descends; check equality at the bottom. The sorted-list invariant makes the answer exact. Independent geometric heights (promotion probability $1/2$) give $O(\log n)$ expected search/update time and $O(n)$ expected pointer storage. A particular search can be linear. More precisely worst-case path cost includes the actual height $H$; with customary $O(\log n)$ level limits this is $O(n)$, while an ideal uncapped geometric height has no finite deterministic bound solely in $n$.
>
> Find the insertion position and record each level's predecessor. Sample a new tower height by independent coin flips, insert the node in the bottom list, and splice its forward pointers at each level it occupies; extend the header if needed. Preserve sorted order and the fact that higher levels are subsets of lower ones. Expected search-plus-update time is $O(\log n)$ and expected new pointers are constant for promotion probability $1/2$. Worst-case search can cost $O(n)$ with a customary bounded height; in an uncapped model state the bound in terms of the realized height as well. Searches and deletion do not resample stored heights.
>
> Study: [[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].

## Disjoint sets

*No dedicated study note is currently available for this topic.*

### AAPP-14-001

Please explain how the disjoint set data structure works and which optimizations have been considered to reduce the complexity of the operations. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=4|2023-07-11-1st · Exercise 3A · p. 4]]

^aapp-14-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Maintain disjoint sets as rooted parent forests. MAKE-SET(x) initializes parent[x]=x and rank/size metadata; FIND(x) returns the root; UNION(x,y) links the representatives unless already equal. Union by rank or size attaches the shallower/smaller tree below the other. Path compression redirects visited FIND nodes toward the root. Together they give inverse-Ackermann amortized cost: $O((n+m)\alpha(n))$ for initialization and $m$ operations, with $O(n)$ storage. This is a sequence guarantee, not a claim that every individual call takes constant worst-case time. With rank/size alone tree height is $O(\log n)$. Representative identities may change; membership equivalence is preserved.
>
> Reference: [Princeton union-find implementation and bounds](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/UF.html).

### AAPP-14-002

Please explain which optimizations have been considered to reduce the complexity of the disjoint-set operations. (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=4|2023-09-11-1st · Exercise 3A · p. 4]]

^aapp-14-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Maintain disjoint sets as rooted parent forests. MAKE-SET(x) initializes parent[x]=x and rank/size metadata; FIND(x) returns the root; UNION(x,y) links the representatives unless already equal. Union by rank or size attaches the shallower/smaller tree below the other. Path compression redirects visited FIND nodes toward the root. Together they give inverse-Ackermann amortized cost: $O((n+m)\alpha(n))$ for initialization and $m$ operations, with $O(n)$ storage. This is a sequence guarantee, not a claim that every individual call takes constant worst-case time. With rank/size alone tree height is $O(\log n)$. Representative identities may change; membership equivalence is preserved.
>
> Reference: [Princeton union-find implementation and bounds](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/UF.html).

## Amortized analysis

Related notes: [[Amortized Analysis]].

### AAPP-15-001

Consider a k-bit binary counter counting upwards from 0 using the INCREMENT procedure, implemented according to the following pseudocode:

```text
INCREMENT(A, k)
1 i = 0
2 while i < k and A[i] == 1
3   A[i] = 0
4   i = i + 1
5 if i < k
6   A[i] = 1
```

Provide a pseudocode implementation for the RESET procedure that returns the counter to its original state (all bits set to 0). Compute the amortized cost for both procedures for a sequence of n operations starting with n-1 INCREMENTs and ending with one RESET using one of the amortized analysis methods seen at lecture. You are allowed to modify the increment procedure and add additional variables to improve the amortized cost of the RESET procedure.

Source: [[Tema Esame 2022-11-08-1st.pdf#page=5|2022-11-08-1st · Exercise 4 · p. 5]]

^aapp-15-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A naive RESET scans all $k$ bits and costs $\Theta(k)$ even if almost none have been touched. Maintain h, the highest bit written since the last reset (initially -1), in addition to the given counter:
> ```text
> INCREMENT(A,k):
>     i=0
>     while i<k and A[i]==1: A[i]=0; i++
>     if i<k: A[i]=1; h=max(h,i)
> RESET(A):
>     for i=0..h: A[i]=0
>     h=-1
> ```
> For the specified $n-1$ increments from zero, bit j flips at most $\lfloor(n-1)/2^j\rfloor$ times, so fewer than $2(n-1)$ bit flips occur. RESET visits at most $\min(k,1+\lfloor\log_2(n-1)\rfloor)$ touched positions for $n>1$ (zero for $n=1$). Total is $O(n)$ and each operation has $O(1)$ amortized cost, although an individual increment or reset can be more expensive. Counter initialization is a separate $O(k)$ cost if it is charged.
>
> Study: [[Amortized Analysis#Aggregate method]].

### AAPP-15-002

Consider a stack data structure storing elements of a given type, which can be assumed to be empty at the start time. Users can push one element on top of the stack using a PUSH operation, which has a constant cost of 1 and remove the top with a POP operation, which has a constant cost of 1. Compute the real cost of the MULTIPOP(k) operation that removes min{k,s} elements from the top of the stack where s is the number of elements in the stack. Determine the worst possible sequence of n operations on this stack and compute the amortized cost for the operations contained in the sequence using one of the methods seen during the course.

Source: [[Tema Esame 2023-01-17-1st.pdf#page=5|2023-01-17-1st · Exercise 4 · p. 5]]

^aapp-15-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MULTIPOP(k) performs $t=\min(k,s)$ pops, costing $\Theta(1+t)$ including loop overhead. It can be linear in current stack size, but every item can be popped only after being pushed. Over n operations from empty, total successful pops are at most total pushes, hence total cost is $O(n)$ and amortized cost is $O(1)$ per operation. A sequence of n-1 pushes followed by MULTIPOP(n-1) exhibits an expensive final operation but only linear total cost. Using potential $\Phi=s$, PUSH has amortized cost 2, POP cost 0, and MULTIPOP's t pop-cost is canceled by a potential drop t, leaving at most constant loop overhead.
>
> Study: [[Amortized Analysis#Potential method]].

### AAPP-15-003

Consider a dynamic table data structure for storing a variable number of elements in memory. When created, the table has space for storing only one element, and pushing one element in the table has a constant cost. If the table is full, twice the size of the original table is allocated to a new table and all elements of the original table are copied in the new table. The cost for allocating one unit of memory is constant. Compute the real cost for inserting n elements into a new-allocated table (having an initial capacity for storing only one element) and determine the amortized cost for the allocating the same number of elements using one of the methods seen during the course.

Source: [[Tema Esame 2023-02-14-1st.pdf#page=5|2023-02-14-1st · Exercise 4 · p. 5]]

^aapp-15-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Charge one per allocated slot, copied element, and inserted element, as the question specifies. A resize from full capacity m costs $2m+m+1=3m+1$; a nonresize insertion costs 1. Let $M=2^{\lceil\log_2 n\rceil}$ be final capacity. Including the initial one-slot allocation, n insertions cost $n+3M-2<7n$; if that initial allocation was prepaid, subtract 1. Thus total cost is $\Theta(n)$ and amortized insertion cost $\Theta(1)$, despite a $\Theta(n)$ single resize. This follows by geometric summation of allocation and copy sizes. Alternatively use potential $6s-3m$ for nonempty states and zero initially: ordinary and resize charges are 7, and the first allocation/insertion has charge 5. The familiar charge 3 omits allocation-per-slot cost and is not the same exact model.
>
> Study: [[Amortized Analysis#Charging allocation per slot]].

### AAPP-15-004

Please explain what aggregate amortized analysis is. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=5|2023-06-19-1st · Exercise 4A · p. 5]]

^aapp-15-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-005

What is meant by “accounting method”? At which class of algorithms could be applied? (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=5|2023-07-11-1st · Exercise 4B · p. 5]]

^aapp-15-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The accounting method overcharges cheap operations and stores credits to pay for later expensive operations, maintaining a nonnegative total credit balance. For a doubling dynamic array, charging a constant per insertion pays for its own write and saves enough to copy elements at the next expansion. With copies/write cost only the standard charge is at most 3 per insertion, treating initialization separately. If allocation is charged per slot as in question 003, a larger constant charge is needed. The method proves worst-case total sequence bounds for stateful data structures; it is not an average over random executions.
>
> Study: [[Amortized Analysis#Accounting method]].

### AAPP-15-006

What is meant by “potential method”? At which class of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=5|2023-09-11-1st · Exercise 4B · p. 5]]

^aapp-15-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Choose a potential $\Phi(D)$ representing stored credit; require it to be bounded below relative to its initial value (usually $\Phi_0=0$ and $\Phi_i\ge0$). Define $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$. Then $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$, so nonnegative final potential bounds actual total by amortized total. A negative change releases earlier credit, and is compatible with a nonnegative potential. For a nonempty doubling array of size $s$ and capacity $m$, $\Phi=2s-m$ gives constant amortized insertion cost when charging copies and the inserted element; use a separate initial empty-state convention. Allocation-per-slot charges need adjusted constants.
>
> Study: [[Amortized Analysis#Potential method]].

### AAPP-15-007

What is meant by “potential method”? To which class of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=5|2023-11-09-1st · Exercise 4B · p. 5]]

^aapp-15-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Choose a potential $\Phi(D)$ representing stored credit; require it to be bounded below relative to its initial value (usually $\Phi_0=0$ and $\Phi_i\ge0$). Define $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$. Then $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$, so nonnegative final potential bounds actual total by amortized total. A negative change releases earlier credit, and is compatible with a nonnegative potential. For a nonempty doubling array of size $s$ and capacity $m$, $\Phi=2s-m$ gives constant amortized insertion cost when charging copies and the inserted element; use a separate initial empty-state convention. Allocation-per-slot charges need adjusted constants.
>
> Study: [[Amortized Analysis#Potential method]].

### AAPP-15-008

Please discuss the amortized analysis. For which class of algorithm does it matter? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=4|2024-01-26-1st · Exercise 3A · p. 4]]

^aapp-15-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-009

What is meant by “accounting method”? To which class of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=5|2024-02-16-1st · Exercise 4B · p. 5]]

^aapp-15-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The accounting method overcharges cheap operations and stores credits to pay for later expensive operations, maintaining a nonnegative total credit balance. For a doubling dynamic array, charging a constant per insertion pays for its own write and saves enough to copy elements at the next expansion. With copies/write cost only the standard charge is at most 3 per insertion, treating initialization separately. If allocation is charged per slot as in question 003, a larger constant charge is needed. The method proves worst-case total sequence bounds for stateful data structures; it is not an average over random executions.
>
> Study: [[Amortized Analysis#Accounting method]].

### AAPP-15-010

What is meant by “amortized analysis”? To which type of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=5|2024-07-24-1st · Exercise 4B · p. 5]]

^aapp-15-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-011

Please discuss the different variants of the amortized analysis. For what class of problems are they used? (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=5|2025-02-14-1st · Exercise 4B · p. 5]]

^aapp-15-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-012

Why is amortized analysis useful in algorithm design, especially for data structures? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=5|2025-06-05-1st · Exercise 4A · p. 5]]

^aapp-15-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-013

What does it mean if the potential difference ΔΦ is negative in the potential method? What about the sign of Φ. (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=5|2025-06-05-1st · Exercise 4C · p. 5]]

^aapp-15-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Choose a potential $\Phi(D)$ representing stored credit; require it to be bounded below relative to its initial value (usually $\Phi_0=0$ and $\Phi_i\ge0$). Define $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$. Then $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$, so nonnegative final potential bounds actual total by amortized total. A negative change releases earlier credit, and is compatible with a nonnegative potential. For a nonempty doubling array of size $s$ and capacity $m$, $\Phi=2s-m$ gives constant amortized insertion cost when charging copies and the inserted element; use a separate initial empty-state convention. Allocation-per-slot charges need adjusted constants.
>
> Study: [[Amortized Analysis#Potential method]].

### AAPP-15-014

Describe an algorithm seen during the course lectures where the potential method has been used. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=4|2025-07-04-1st · Exercise 3A · p. 4]]

^aapp-15-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Choose a potential $\Phi(D)$ representing stored credit; require it to be bounded below relative to its initial value (usually $\Phi_0=0$ and $\Phi_i\ge0$). Define $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$. Then $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$, so nonnegative final potential bounds actual total by amortized total. A negative change releases earlier credit, and is compatible with a nonnegative potential. For a nonempty doubling array of size $s$ and capacity $m$, $\Phi=2s-m$ gives constant amortized insertion cost when charging copies and the inserted element; use a separate initial empty-state convention. Allocation-per-slot charges need adjusted constants.
>
> Study: [[Amortized Analysis#Potential method]].

### AAPP-15-015

What are the characteristics of an algorithm that require the amortized analysis methods? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=5|2025-07-04-1st · Exercise 4C · p. 5]]

^aapp-15-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-016

What is meant by “accounting method”? To which class of algorithms could be applied? Examples? (1)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=5|2025-09-05-1st · Exercise 4A · p. 5]]

^aapp-15-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The accounting method overcharges cheap operations and stores credits to pay for later expensive operations, maintaining a nonnegative total credit balance. For a doubling dynamic array, charging a constant per insertion pays for its own write and saves enough to copy elements at the next expansion. With copies/write cost only the standard charge is at most 3 per insertion, treating initialization separately. If allocation is charged per slot as in question 003, a larger constant charge is needed. The method proves worst-case total sequence bounds for stateful data structures; it is not an average over random executions.
>
> Study: [[Amortized Analysis#Accounting method]].

### AAPP-15-017

Explain the various forms of amortized analysis. What characteristics of a problem make amortized analysis the appropriate analytical technique? (2)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=7|2026-1-22-1st · Exercise 4B · p. 7]]

^aapp-15-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-018

Describe amortized analysis and discuss one algorithm or data structure where this analysis is appropriate. (2)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=3|2026-6-11-1st · Exercise 2A · p. 3]]

^aapp-15-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Amortized analysis bounds the total actual cost of an arbitrary operation sequence from a stated initial state; no random-input assumption is needed. A rare expensive operation can be paid for by many cheap ones. Aggregate analysis bounds total $C(m)$ and divides by $m$. Accounting assigns charges and stores nonnegative credits. Potential analysis chooses a state function and uses $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$; if $\Phi_m\ge\Phi_0$, telescoping makes total amortized charge an upper bound on total actual cost. This suits dynamic arrays, stack MULTIPOP, counters, and union-find. It is a method for sequences, not a requirement that the algorithm belong to one design paradigm.
>
> Study: [[Amortized Analysis]].

### AAPP-15-019

Describe the potential method of amortized analysis and apply it conceptually to a dynamic array that doubles when full. (2)

Source: [[Tema Esame 2026-9-10-1st.pdf#page=7|2026-9-10-1st · Exercise 4B · p. 7]]

^aapp-15-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Choose a potential $\Phi(D)$ representing stored credit; require it to be bounded below relative to its initial value (usually $\Phi_0=0$ and $\Phi_i\ge0$). Define $\widehat c_i=c_i+\Phi_i-\Phi_{i-1}$. Then $\sum c_i=\sum\widehat c_i+\Phi_0-\Phi_m$, so nonnegative final potential bounds actual total by amortized total. A negative change releases earlier credit, and is compatible with a nonnegative potential. For a nonempty doubling array of size $s$ and capacity $m$, $\Phi=2s-m$ gives constant amortized insertion cost when charging copies and the inserted element; use a separate initial empty-state convention. Allocation-per-slot charges need adjusted constants.
>
> Study: [[Amortized Analysis#Potential method]].

## Online algorithms and competitive analysis

Related study note: [[Competitive Analysis]] — online/offline models, move-to-front and its potential proof, and LRU versus MIN paging. The paid/free cost distinction matters for the competitive factor.

### AAPP-16-001

Please discuss the difference between Online and Offline algorithms. (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=4|2022-11-08-1st · Exercise 3A · p. 4]]

^aapp-16-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.
>
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis]].

### AAPP-16-002

Please explain what the competitive analysis is meant for. (2)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=4|2023-01-17-1st · Exercise 3A · p. 4]]

^aapp-16-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.
>
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis]].

### AAPP-16-003

Please explain why the amortized analysis matters for the analysis of the complexity of the Move to Front algorithm. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=5|2023-06-19-1st · Exercise 4B · p. 5]]

^aapp-16-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-004

Detail the Move to Front algorithm. What approach is followed to estimate the temporal complexity of this class of algorithms? Which class of algorithms does it belongs to? (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=5|2023-09-11-1st · Exercise 4A · p. 5]]

^aapp-16-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-005

Please discuss the competitive analysis. For which class of algorithm does it matter? (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=4|2023-11-09-1st · Exercise 3A · p. 4]]

^aapp-16-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.
>
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis]].

### AAPP-16-006

Please describe the difference between on-line and off-line algorithms. How is their complexity analyzed? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=5|2024-01-26-1st · Exercise 4A · p. 5]]

^aapp-16-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.
>
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis]].

### AAPP-16-007

Please describe the “move to front” heuristic (complexity included). Why did we use amortized analysis instead of the worst-case? (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=5|2024-06-26-1st · Exercise 4B · p. 5]]

^aapp-16-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-008

To which class does the Move-To-Front Algorithm belong? How is its complexity evaluated? (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=3|2024-07-24-1st · Exercise 2C · p. 3]]

^aapp-16-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-009

Please discuss the competitive analysis. In which class of algorithm is used? Amortized analysis could be of some use; why? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=5|2024-09-05-1st · Exercise 4A · p. 5]]

^aapp-16-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.
>
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis]].

### AAPP-16-010

Please explain what the competitive analysis is meant for by using one of the examples presented during the course lectures. (2)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=3|2025-09-05-1st · Exercise 2B · p. 3]]

^aapp-16-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-011

Please describe what is peculiar to the self-organizing list problem, how this problem can be solved, and how its complexity could be analyzed. (1)

Source: [[Tema Esame 2025-11-06-1st.pdf#page=5|2025-11-06-1st · Exercise 3B · p. 5]]

^aapp-16-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-012

Please describe an example of an online problem and how its complexity could be analyzed. (1)

Source: [[Tema Esame 2026-1-22-1st.pdf#page=5|2026-1-22-1st · Exercise 3B · p. 5]]

^aapp-16-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-013

Explain why the self-organizing list problem is naturally online, and give a concrete access sequence where having future knowledge (offline) allows strictly lower cost than any online strategy. (2)

Source: [[Tema Esame 2026-2-09-1st.pdf#page=7|2026-2-09-1st · Exercise 4B · p. 7]]

^aapp-16-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Requests must be served before future requests are known, so reordering trades current cost against unknown future benefits. In the lecture's paid-swap model, start at [A,B,C] and request C,A,A. MTF pays 5,3,1 (search plus forward swaps), totaling 9; an offline strategy that leaves the list unchanged pays 3,1,1=5. Thus future knowledge can help against a specified online heuristic. However, the wording “one fixed sequence cheaper than any online strategy” is too strong: an online strategy can happen to make the offline-optimal decisions on that sequence. The valid adversarial quantifier is: for each fixed deterministic online strategy, a suitable bad sequence can be chosen; it need not be the same sequence for all strategies.
>
> Study: [[Competitive Analysis#Online, offline, and the role of the adversary]].

### AAPP-16-014

Discuss self-organizing lists, including one heuristic presented in class and the method used to analyze its performance. (2)

Source: [[Tema Esame 2026-6-11-1st.pdf#page=7|2026-6-11-1st · Exercise 4B · p. 7]]

^aapp-16-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis#Move-to-front: algorithm and exact costs]]; [[Competitive Analysis#Competitive guarantees and the additive constant]].

### AAPP-16-015

Please describe the difference between online and offline algorithms. How is their complexity analyzed? (2)

Source: [[Tema Esame 2026-6-29-1st.pdf#page=6|2026-6-29-1st · Exercise 3C · p. 6]]

^aapp-16-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An online algorithm must serve the current request without knowing the future suffix; an offline algorithm can plan using the full sequence. Analyze absolute time as usual, but compare solution/sequence quality by competitive analysis: $C_A(\sigma)\le\alpha C_{OPT}(\sigma)+\beta$ for every sequence, with a sequence-independent startup constant. Both costs use the same sequence, cost model and initial conditions. An adversarial worst-case request sequence is not a probability distribution, and the offline optimum need not be strictly cheaper on every input.
>
> Move-to-front is an online self-organizing-list heuristic: search for the requested item, then move it to the head while preserving other items' relative order. In the lecture's paid-adjacent-swap model, rank r costs r for search plus r-1 swaps, hence $2r-1$ and $\Theta(n)$ worst case per request. Compare whole-sequence cost with offline OPT rather than relying on that uninformative single-operation bound. Using twice the number of order inversions between MTF and OPT as potential proves $C_{MTF}\le4C_{OPT}+\Phi_0$. With identical starting lists $\Phi_0=0$. In the different free-forward-move model MTF is 2-competitive. Amortization is the proof technique; competitiveness is the comparison guarantee.
>
> Study: [[Competitive Analysis]].

## Parallel design and architectures

Related notes: [[Course Introduction]].

### AAPP-17-001

List and describe the different kinds of parallelism according to the Flynn taxonomy, together with architectures implementing them when possible.

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=3|2022-02-11-2nd-a · Exercise 2A · p. 3]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=3|2022-02-11-2nd-b · Exercise 2A · p. 3]]

^aapp-17-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Flynn classifies architectures by instruction and data streams: **SISD** executes one instruction stream on one data stream (a conventional sequential core); **SIMD** applies one instruction to multiple data elements (CPU vector units); **MISD** applies multiple instruction streams to the same data stream (rare; specialized redundant processing is a possible interpretation); **MIMD** executes independent instruction streams on different data (multicore CPUs and clusters). GPUs expose SIMT, closely related to SIMD within a warp, while independently scheduled groups provide additional parallelism.

### AAPP-17-002

It is not recommendable to mix parallelism technologies since doing so increases the complexity of the compiled binaries: true or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=3|2022-02-11-2nd-a · Exercise 2B · p. 3]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=3|2022-02-11-2nd-b · Exercise 2B · p. 3]]

^aapp-17-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Mixing models is possible and often useful. For example, MPI distributes a simulation across cluster nodes, OpenMP uses the cores within each node, and CUDA offloads suitable kernels to GPUs. The relevant costs are coordination, data movement, oversubscription and programming complexity; increased binary complexity is not a general reason to reject hybrid programming. Match each model to the hardware level and give each level a clear responsibility.

### AAPP-17-003

Is it possible to obtain the same low level implementation starting from different parallel programming models descriptions of the same parallel pattern?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=3|2022-06-09-2nd-a · Exercise 2A · p. 3]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=3|2022-06-09-2nd-b · Exercise 2A · p. 3]]

^aapp-17-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes. Different models can express the same decomposition and ultimately generate similar machine operations: for example, an OpenMP parallel loop and a Pthreads worker pool can both divide an array into blocks processed by CPU threads. The models differ in how much scheduling and synchronization the programmer specifies. Identical low-level code is possible, but is not guaranteed by equivalent high-level behavior.

### AAPP-17-004

Parallel programming models using threads spawn a single process, therefore the program I/O correctness is always guaranteed: true or false?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=3|2022-06-09-2nd-a · Exercise 2B · p. 3]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=3|2022-06-09-2nd-b · Exercise 2B · p. 3]]

^aapp-17-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> False. Threads share the process address space and usually its I/O resources, so concurrent output can interleave and concurrent operations can require synchronization. Even when an individual library call is internally thread-safe, a sequence of calls is not automatically one atomic record, and output order is unspecified. Use a lock around a complete logical output operation or collect results and print them in a controlled order.

### AAPP-17-005

Is it possible to use multiple parallelization models in the same program? Would it benefit some hardware architectures in particular?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=3|2022-09-07-2nd-b · Exercise 2A · p. 3]]

^aapp-17-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Mixing models is possible and often useful. For example, MPI distributes a simulation across cluster nodes, OpenMP uses the cores within each node, and CUDA offloads suitable kernels to GPUs. The relevant costs are coordination, data movement, oversubscription and programming complexity; increased binary complexity is not a general reason to reject hybrid programming. Match each model to the hardware level and give each level a clear responsibility.

### AAPP-17-006

Which are the main differences between parallel programming models based on threads and those based on processes in terms of low-level information management and architectures that can benefit from them?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=3|2022-09-07-2nd-b · Exercise 2C · p. 3]]

^aapp-17-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Threads within a process share its address space and resources; each has its own execution state and stack. They communicate through shared data and need synchronization to prevent races. Separate processes normally have separate address spaces and exchange data explicitly, for example with MPI messages. Thread models naturally fit a shared-memory node; message passing also spans distributed-memory machines. Process-based communication can run within one node too, and hybrid programs combine the two.

### AAPP-17-007

Could you please summarize why manual parallelization is preferred to automatic parallelization? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1A · p. 2]]
Source: [[Tema Esame 2025-09-05-2nd.pdf#page=1|2025-09-05-2nd · Exercise 1A · p. 1]]

^aapp-17-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Manual parallelization can exploit domain knowledge that a compiler cannot safely infer: independence despite pointer aliasing, suitable data decomposition, algorithm changes, acceptable reductions, granularity and placement. Automatic parallelization remains useful where independence can be established, particularly regular loops and vectorization. Manual parallelization is therefore often needed for larger structural changes, rather than being universally preferable for every loop.

### AAPP-17-008

Designing a «good» parallel algorithm by extracting all the available parallelism is not enough. True/False? Why?(1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1B · p. 2]]

^aapp-17-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> True. Exposing many concurrent operations is only one requirement. A useful algorithm must also keep total work close to the best sequential algorithm, limit communication and synchronization, provide enough work per task, balance the load and use memory efficiently. Creating millions of tiny tasks can expose more parallelism yet run slower because management overhead dominates. Judge both work/span and the costs of mapping the computation onto the target hardware.

### AAPP-17-009

Please comment this sentence: “Design a «good» parallel algorithm by extracting all the available parallelism is not enough.” (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=2|2024-07-24-2nd · Exercise 1A · p. 2]]

^aapp-17-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> True. Exposing many concurrent operations is only one requirement. A useful algorithm must also keep total work close to the best sequential algorithm, limit communication and synchronization, provide enough work per task, balance the load and use memory efficiently. Creating millions of tiny tasks can expose more parallelism yet run slower because management overhead dominates. Judge both work/span and the costs of mapping the computation onto the target hardware.

### AAPP-17-010

Please comment on this sentence: “Automatic parallelization cannot be used because it produces wrong solutions.”. True/false, partially true? (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=2|2024-09-05-2nd · Exercise 1A · p. 2]]

^aapp-17-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> False as a general claim. A correct automatic parallelizer preserves the specified semantics and refuses or guards transformations when it cannot establish safety. Its main limitations are incomplete knowledge, conservative dependence analysis and restricted transformations, so it may miss profitable parallelism. Incorrect directives supplied by a programmer or assumptions that explicitly permit changed floating-point behavior are separate issues.

### AAPP-17-011

“A single instruction can manipulate different data at a time”. Please comment on the sentence and discuss which kind of parallelism it is referring to. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=2|2024-09-05-2nd · Exercise 1B · p. 2]]

^aapp-17-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> This describes **SIMD**, single instruction, multiple data. A vector instruction applies the same operation to several lanes, such as adding eight 32-bit floats in a 256-bit vector. It exploits data parallelism within a core. It differs from MIMD threading, in which cores can execute different instruction streams.

### AAPP-17-012

What does PCAM Design Methodology mean? (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=1|2025-01-24-2nd · Exercise 1B · p. 1]]

^aapp-17-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **PCAM** means **Partitioning, Communication, Agglomeration, Mapping**. First divide computation/data into fine-grained tasks; then identify their required communication and dependencies. Combine tasks to obtain useful granularity and locality, and finally assign them to processors to balance the load and control communication. These stages guide exploration and may be revisited as costs become clearer.
>
> **Reference:** [Foster, PCAM methodology](https://www.mcs.anl.gov/~itf/dbpp/text/node15.html).

### AAPP-17-013

Could you please explain what PCAM design methodology is? (1)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=1|2025-12-18-2nd · Exercise 1B · p. 1]]

^aapp-17-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **PCAM** means **Partitioning, Communication, Agglomeration, Mapping**. First divide computation/data into fine-grained tasks; then identify their required communication and dependencies. Combine tasks to obtain useful granularity and locality, and finally assign them to processors to balance the load and control communication. These stages guide exploration and may be revisited as costs become clearer.
>
> **Reference:** [Foster, PCAM methodology](https://www.mcs.anl.gov/~itf/dbpp/text/node15.html).

### AAPP-17-014

Could you please explain what the aim of agglomeration is in the PCAM design methodology? (1)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=1|2026-1-22-2nd · Exercise 1B · p. 1]]

^aapp-17-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Agglomeration combines fine-grained tasks and data into larger units. It reduces task-management and communication overhead and improves locality, while retaining enough tasks to balance the processors. For example, combine individual image pixels into tiles. Excessive agglomeration reduces concurrency, so the aim is an efficient granularity rather than the fewest possible tasks.
>
> **Reference:** [Foster, PCAM methodology](https://www.mcs.anl.gov/~itf/dbpp/text/node15.html).

### AAPP-17-015

Please explain what is meant by AoS and SoA, and in which cases you would use one or the other. (1)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=1|2026-2-09-2nd · Exercise 1B · p. 1]]

^aapp-17-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **AoS**, array of structures, stores complete records together, for example `p[i].x, p[i].y, p[i].z`. It is useful when an operation consumes most fields of each object. **SoA**, structure of arrays, stores one array per field, for example `x[i], y[i], z[i]`. It gives contiguous access when processing one field across many objects and often helps SIMD vectorization and GPU memory coalescing. The best layout depends on the actual access pattern; blocked mixtures are also possible.

### AAPP-17-016

Based on the architecture illustrated in the figure below, describe how you would exploit the different levels of parallelism to accelerate the execution of an application. (1)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=4|2026-6-11-2nd · Exercise 3A · p. 4]]

![[2026-6-11-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2026-6-11-2nd.pdf#page=4|PDF page 4]].*

^aapp-17-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The figure shows two CPU sockets, multiple cores per socket, and 256-bit vector units within each core, connected to shared RAM. Use OpenMP threads across cores and SIMD within each core, for example `parallel for simd` on a large independent loop. A 256-bit vector holds eight 32-bit floats or four 64-bit values. Bind threads and place data to preserve locality; shared addressability does not imply uniform access costs. MPI between sockets is optional here, while MPI between separate nodes would add another level.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

## Dependences and loop parallelization

*No dedicated study note is currently available for this topic.*

### AAPP-18-001

Loop-carried dependences prevent loop parallelization. True/False? Why?(1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1C · p. 2]]

^aapp-18-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> No. A loop-carried dependence prevents an unrestricted DOALL execution when iterations need values produced by others, but may still allow independent chains, pipelining, wavefront scheduling or a specialized transformation such as an associative scan. Anti- and output dependences can often be removed by renaming storage. Determine the precise accesses and required ordering before choosing a transformation.

### AAPP-18-002

Is an output dependence a true dependence? True/False? Why? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1D · p. 2]]

^aapp-18-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An output dependence is **WAW**, write after write. It is a storage or false dependence: two operations write the same location, so their order determines the final value. It does not transmit a value between operations as RAW does. Separate temporary locations can remove the conflict, provided the final store preserves the value of the original last writer.

### AAPP-18-003

What is meant by DOALL loop? Example? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=2|2023-01-17-2nd · Exercise 1A · p. 2]]

^aapp-18-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A DOALL loop has independent iterations and can execute them in any order, for example `for (i=0; i<n; ++i) y[i]=f(x[i]);` with separate arrays and a pure `f`. An OpenMP `parallel for` distributes the iterations. With equal constant-cost iterations, ideal time is $\Theta(n/p)$ plus startup/scheduling costs. Near-linear speedup additionally requires enough work, adequate memory bandwidth, balanced execution and negligible serial overhead; independence alone does not guarantee it.

### AAPP-18-004

Is the following code parallelizable? (1)

```c
           for (i=10; i<100; i++)
             a[i-10] = a[i] + 100;
```

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=2|2023-01-17-2nd · Exercise 1B · p. 2]]

^aapp-18-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The loop has a **WAR anti-dependence of distance 10**: iteration $i$ reads `a[i]`, and later iteration $i+10$ overwrites that location as its destination. The ascending sequential loop reads the original source values. Running iterations concurrently in place can overwrite a value too early. First copy the read range into immutable `old`, then run `a[i-10]=old[i]+100` in parallel. This removes the storage conflict without changing which values are read.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-005

Please describe the differences between flow, output and anti-dependencies. (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=2|2023-01-17-2nd · Exercise 1C · p. 2]]

^aapp-18-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **RAW (flow/true):** a write must precede a read of its result, e.g. `x=...; y=x+1`. **WAR (anti):** a read must precede a later overwrite, e.g. `y=x+1; x=...`. **WAW (output):** writes to the same location must preserve their order to retain the correct final value. These can be within one iteration or carried between iterations. WAR and WAW are often removable by renaming; RAW generally requires preserving the producer-to-consumer computation.

### AAPP-18-006

“Parallel execution must address control, data, and system dependences”. What is meant by “dependency” in this context? (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=2|2023-02-14-2nd · Exercise 1A · p. 2]]

^aapp-18-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A dependence is an ordering constraint needed to preserve program behavior. Data dependences arise from accesses to the same location with at least one write (RAW, WAR, WAW); control dependences arise because a branch determines whether an operation executes. I/O, synchronization and other observable side effects can impose additional order. Parallelize operations whose required predecessor operations have completed, rather than merely operations written in different loop iterations.

### AAPP-18-007

Is the following code parallelizable? Are there better parallelizable solutions? (2)

```c
           for (j=1; j<100; j++)
                     for (i=0; i<100; i++)
                           a[i][j] = f(a[i][j-1]);
```

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=2|2023-02-14-2nd · Exercise 1B · p. 2]]

^aapp-18-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Each row is a chain along `j`: `a[i][j-1]` produces the next column, a RAW dependence of vector $(0,1)$ in `(i,j)` coordinates. Different rows are independent. Interchange the loops and parallelize the outer `i` loop, keeping `j=1..99` sequential within each row. Alternatively, retain the original column order and parallelize the inner row loop with a barrier between columns, at greater synchronization cost.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-008

Please explain the differences between “loop-carried“ and “loop-independent”.(1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=2|2023-02-14-2nd · Exercise 1C · p. 2]]

^aapp-18-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A **loop-independent** dependence connects accesses in the same iteration, such as assigning a temporary and then reading it. A **loop-carried** dependence connects different iterations, such as `a[i]=a[i-1]+1`. The latter can constrain iteration order; the former normally requires only the original statement order within each iteration. For nested loops, specify which level carries the dependence and its direction/distance.

### AAPP-18-009

Is it possible to eliminate a flow dependency by modifying the program and ensuring that the program remains equivalent? (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=2|2023-06-19-2nd · Exercise 1A · p. 2]]

^aapp-18-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Not in general. A RAW dependence carries a computed value from a producer to a consumer; merely renaming the location does not create that value sooner. Keep its order, or reformulate the algorithm when its algebra permits it. For example, an associative accumulation can become a parallel scan. An arbitrary recurrence involving an unknown `f` cannot automatically receive that transformation.

### AAPP-18-010

Is the following code parallelizable? Are there better parallelizable solutions? (2)

```c
           for (i=0; i<100; i++)
                      for (j=1; j<100; j++)
                            a[i][j] = f(a[i][j-1]);
```

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=2|2023-06-19-2nd · Exercise 1B · p. 2]]

^aapp-18-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> There is a RAW dependence along columns: `(i,j-1)` must finish before `(i,j)`. Parallelize different rows with `#pragma omp parallel for` on `i`, and execute each inner `j` loop sequentially. An unrestricted parallel loop over `j`, or `collapse(2)`, would break the recurrence.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-011

DOALL loops have linear speedup even using the Amdahl law. Could you please write a short pseudo code showing an example of a DOALL loop? (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=2|2023-07-11-2nd · Exercise 1A · p. 2]]

^aapp-18-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A DOALL loop has independent iterations and can execute them in any order, for example `for (i=0; i<n; ++i) y[i]=f(x[i]);` with separate arrays and a pure `f`. An OpenMP `parallel for` distributes the iterations. With equal constant-cost iterations, ideal time is $\Theta(n/p)$ plus startup/scheduling costs. Near-linear speedup additionally requires enough work, adequate memory bandwidth, balanced execution and negligible serial overhead; independence alone does not guarantee it.

### AAPP-18-012

Is the following code parallelizable? Are there better parallelizable solutions? (2)

```c
           for (i=0; i<100; i++)
                     for (j=0; j<91; j++)
                        a[i][j+9] = f(a[i][j]);
```

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=2|2023-07-11-2nd · Exercise 1B · p. 2]]

^aapp-18-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The write is nine columns ahead of the read: iteration `j` produces `a[i][j+9]`, read by iteration `j+9`. This is a RAW dependence of distance 9. Parallelize rows, and optionally the nine chains identified by `j % 9`; within each chain process `j` in increasing steps of 9. Do not run all columns unordered, since later iterations require the newly computed values.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-013

Could you please describe the statement/operation dependency and how and when it can be removed? (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=2|2023-09-11-2nd · Exercise 1A · p. 2]]

^aapp-18-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A statement/operation dependence is a required ordering between operations, for example `x=f(); y=g(x);`: `g` needs the result of `f` (RAW). Renaming cannot remove that value dependence. Dependences caused solely by storage reuse, such as reading `x` before an unrelated overwrite (WAR), or two writes to `x` (WAW), can often be removed with separate temporaries while preserving the observed reads and final value. A true dependence may disappear after an algebraically valid reformulation, but not for arbitrary functions.

### AAPP-18-014

Under which condition the following code is parallelizable? In case the conditions hold, are there better parallelizable solutions? (2)

```c
           for (i=0; i<100; i++)
                     for (j=0; j<10; j++)
                           a[i][j] = f(a[i][j]);
```

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=2|2023-09-11-2nd · Exercise 1B · p. 2]]

^aapp-18-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Each iteration reads and updates only its own `a[i][j]`, so the nests are DOALL when `f` has no shared side effects. Parallelize outer rows, or use `collapse(2)` for more tasks. In C row-major storage keep `j` as the fast-moving index for contiguous access. There is a dependence within each iteration between its read and write, but none between distinct cells.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-015

Could you please write a short pseudo code showing an example of a DOALL loop in C? Which parallel pattern is directly connected to the DOALL loop? (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=2|2023-12-21-2nd · Exercise 1A · p. 2]]

^aapp-18-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A DOALL loop has independent iterations and can execute them in any order, for example `for (i=0; i<n; ++i) y[i]=f(x[i]);` with separate arrays and a pure `f`. An OpenMP `parallel for` distributes the iterations. With equal constant-cost iterations, ideal time is $\Theta(n/p)$ plus startup/scheduling costs. Near-linear speedup additionally requires enough work, adequate memory bandwidth, balanced execution and negligible serial overhead; independence alone does not guarantee it.
>
> The directly related parallel pattern is **Map**: apply the same independent operation to each element.

### AAPP-18-016

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=0; j<10; j++)
                            a[i][j] = f(a[j][i-1]);
```

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=2|2023-12-21-2nd · Exercise 1B · p. 2]]

^aapp-18-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The transposed in-place access `a[i][j]=f(a[j][i-1])` creates RAW and WAR dependences in the small leading block; it is not a simple row-independent recurrence. For example, for $1\le i\le9$, iteration `(i,i)` reads `a[i][i-1]` just written by the preceding inner iteration. Reads of earlier rows may also see values updated by earlier outer iterations. Therefore neither `collapse(2)` nor replacing every read by an original-array snapshot preserves the printed sequential semantics. One safe partial strategy is to execute outer rows `i=1..10` in original order, then parallelize all iterations with `i>=11`: their reads use columns `i-1>=10`, which this loop never writes. More aggressive scheduling must respect the exact dependence graph.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-017

Is it possible to eliminate a flow dependency by modifying the program and ensuring that the program remains equivalent? Is it the same with output dependency? Please show an example of what can be done. (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=2|2024-01-26-2nd · Exercise 1A · p. 2]]

^aapp-18-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A **RAW** dependence reads the value a previous operation computed, so an actual producer-to-consumer relationship remains even after renaming. A **WAW** dependence exists only because writes reuse storage: compute into separate locations and retain the last writer's value afterward. For example, independent `tmp[i]=f(i)` computations followed by `x=tmp[n-1]` can replace repeated `x=f(i)` writes when intermediate values are unused and `f` has no side effects.
>
> For a special removable flow chain, the prefix-sum recurrence `s[i]=s[i-1]+x[i]` can become a parallel scan when addition is associative in the chosen arithmetic. This preserves values under that assumption; it is an algorithmic reformulation rather than storage renaming.

### AAPP-18-018

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=0; j<100; j++)
                             c[j][i] += a[i]*b[j];
```

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=2|2024-01-26-2nd · Exercise 1B · p. 2]]

^aapp-18-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Each pair `(i,j)` updates a distinct `c[j][i]`, while `a` and `b` are read-only, so iterations are independent. Use a parallel outer loop. For C row-major storage, interchange to `j` outer and `i` inner so the inner loop traverses `c[j][i]` contiguously; this also helps vectorization. Repeated reading of `a` or `b` is legal in shared-memory execution.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-019

Please describe the Parallel Data Management Patterns: Pipeline. Are flow dependencies preventing correct parallelization of pipeline parallel pattern when present? (2)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=2|2024-02-16-2nd · Exercise 1A · p. 2]]

^aapp-18-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A pipeline respects dependencies between stages for each item while allowing different items to occupy different stages concurrently. For example, read item $k+1$, transform item $k$, and write item $k-1$. This is useful for a sequence of repeated independent items, not a way to ignore a recurrence that still links successive items. Use synchronized stage queues or task dependences, retain necessary order and avoid letting a slow stage become the throughput bottleneck.

### AAPP-18-020

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=0; j<100; j++)
                            b[i][j] += f(a[i][j]);
```

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=2|2024-02-16-2nd · Exercise 1B · p. 2]]

^aapp-18-020

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `b[i][j] += f(a[i][j])` reads and writes one distinct output cell per iteration, so both loop levels are independent under the stated assumptions. Parallelize outer rows, optionally vectorize inner columns, or use `collapse(2)` when the outer iteration count is too small. If `a` and `b` overlap at different indices, re-check dependences before applying these directives.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-021

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=i; j<100; j++)
                            b[i][j] += f(a[i][j]);
```

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=2|2024-06-26-2nd · Exercise 1B · p. 2]]

^aapp-18-021

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> With triangular bounds `j=i..99`, different iterations update different cells, so outer iterations are independent but have unequal work: small `i` has more iterations. Use `#pragma omp parallel for schedule(dynamic)` or `guided` on the outer loop to improve balance, with a chunk size large enough to control scheduling overhead. A valid flattened triangular iteration space is another option. Keep contiguous inner access for locality.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-022

Is it possible to eliminate an anti-dependency by modifying the program and ensuring that the program remains equivalent? Is it the same with output-dependency? Please show an example of what can be done in both cases. (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=2|2024-07-24-2nd · Exercise 1B · p. 2]]

^aapp-18-022

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> WAR and WAW are false/storage dependences and can often be removed using private temporaries, renaming, double buffering or array expansion. Copy old data before parallel writes when sequential reads require old values, and perform the appropriate final store when only the last write should remain. These transformations must preserve observed reads and final outputs. A true RAW dependence cannot in general be removed just by giving its location another name.
>
> Example WAR: replace `y=x+1; x=f();` by `old=x;` followed by independent `y=old+1` and `x=f()`, if `f` has no conflicting side effects. Example WAW: replace independent overwritten results `x=f(); x=g();` by private `u=f(); v=g(); x=v;`, preserving the original final value.

### AAPP-18-023

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=0; i<100; i++)
                      for (j=2; j<100; j++)
                            a[i][j] = f(a[i][j]) + a[i][j-2];
```

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=2|2024-07-24-2nd · Exercise 1C · p. 2]]

^aapp-18-023

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The term `a[i][j-2]` introduces a RAW dependence of distance 2 along `j`. Different rows and the even/odd column chains of each row are independent. Parallelize rows; or schedule two tasks per row, each running one parity in increasing order. Unrestricted column parallelism would read predecessor cells before they have been updated.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-024

Which loop can be parallelized and under which conditions? Does the overhead of the runtime impact the parallelization of the loops? Which is the best way to parallelize this code on multi-core systems? (2)

```c
            for (i=0; i<1000; i++)
                      for (j=0; j<4; j++)
                            a[i][j] = f(a[i][j]) + a[i][j];
```

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=2|2024-09-05-2nd · Exercise 1C · p. 2]]

^aapp-18-024

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The 1000 row iterations are independent and provide ample parallel work; parallelize the outer `i` loop and keep the four inner iterations together. Use a private inner index, preferably declared in the loop, and optionally SIMD inside the row if profitable. Creating a nested thread team for each four-element row would add excessive overhead. Assign blocks of rows to threads to limit scheduling cost and false sharing.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-025

Please explain when a dependence can be classified as lexically forward dependence. (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=1|2025-01-24-2nd · Exercise 1A · p. 1]]

^aapp-18-025

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A dependence is lexically forward when its source operation precedes its dependent sink in the original sequential execution order. In a loop nest, compare iteration vectors lexicographically; for operations in the same iteration, compare statement order. A legal parallel schedule must keep true producer-to-consumer edges forward. A dependence pointing backward under a proposed interchange indicates that the transformation would violate the original order unless the algorithm or storage is changed.

### AAPP-18-026

Where and under what conditions can the following code be parallelized? Is there a way to write the code for better parallelization if these conditions are met? (2)

```c
            for (i=0; i<100; i++) {
                      for (j=1; j<100; j++)
                         a[i][0] += f(a[i-5][j]);
                      for (j=0; j<100; j++)
                            b[i][j] += f(b[i][j]);
          }
```

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=1|2025-01-24-2nd · Exercise 1C · p. 1]]

^aapp-18-026

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **As printed, the first five outer iterations access `a[i-5][j]` with a negative row index.** Ordinary arrays make this undefined; require an explicit halo/offset representation or start from a valid `i`. After resolving bounds, the shifted read does not itself create a cross-row dependence: the loop writes column 0 but reads columns `j=1..99`. Within each row, `a[i][0] += ...` is a sum reduction. Parallelize valid rows, keeping a private accumulator initialized from the old `a[i][0]`, and store it once. The `b[i][j]` updates are independent.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-027

What dependencies can be eliminated by renaming the variables? (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=1|2025-02-14-2nd · Exercise 1B · p. 1]]

^aapp-18-027

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> WAR and WAW are false/storage dependences and can often be removed using private temporaries, renaming, double buffering or array expansion. Copy old data before parallel writes when sequential reads require old values, and perform the appropriate final store when only the last write should remain. These transformations must preserve observed reads and final outputs. A true RAW dependence cannot in general be removed just by giving its location another name.

### AAPP-18-028

Where and under what conditions can the following code be parallelized? Is there a way to write the code for better parallelization if these conditions are met? Assume that a and b store integers. (2)

```c
            for (i=3; i<100; i++) {
                      for (j=1; j<100; j++)
                         a[i][0] *= f(a[i][j]);
                      for (j=0; j<100; j++)
                          b[i-3][j] += f(b[i][j]);
          }
```

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=1|2025-02-14-2nd · Exercise 1C · p. 1]]

^aapp-18-028

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The `a[i][0] *= f(a[i][j])` updates form a product reduction within each row. The `b[i-3][j] += f(b[i][j])` part has a WAR anti-dependence of outer distance 3: a future iteration overwrites a row that an earlier iteration must read first. To parallelize outer iterations, first snapshot the required `b` source values; all sequential source reads use these old values. Then compute `b[i-3][j] += f(old_b[i][j])` and each row's private product independently. Preserve the original initial `a[i][0]`, and ensure arithmetic is defined; signed overflow is not a valid parallelization assumption.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-029

Consider the following nested loop:

```c
        for (j = 0; j < 100; j++) {
            for (i = 1; i < 100; i++) {
                a[i][j] = f(a[i-1][j]);
            }
        }
```

Evaluate the cache-friendliness of this code. How does the memory layout of the array affect performance, and what changes could improve cache utilization? Is it still parallelizable? How? Justify your answer. (2)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=1|2025-06-05-2nd · Exercise 1C · p. 1]]

^aapp-18-029

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> There is a RAW dependence from row `i-1` to row `i` within each column. Parallelize columns `j`, keeping the `i` loop sequential within each column. With row-major arrays this is strided; alternatively keep row steps in order and parallelize the columns at each step with a barrier, or process column tiles. Do not parallelize rows unordered, since they need newly computed preceding-row values.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-030

What is the difference between a true dependence and an anti-dependence? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=1|2025-07-04-2nd · Exercise 1A · p. 1]]

^aapp-18-030

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A true/flow dependence is RAW: a later operation reads a value produced by an earlier write. An anti-dependence is WAR: an earlier read must occur before a later write overwrites that location. RAW represents a value relationship; WAR arises from storage reuse and can often be removed by reading an old copy or renaming the later destination.

### AAPP-18-031

Consider the following nested loop:

```c
        for (j = 0; j < 100; j++) {
            b[j] = f1(a[j]);
        }
        for (j = 99; j >= 0; j--) {
            a[j] = f2(b[j]);
        }
```

Which loop can be parallelized and under which conditions (j is declared as an integer)? Is there a way to improve the code? Is the OpenMP nowait clause a possible option? Justify your answers. (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=1|2025-07-04-2nd · Exercise 1C · p. 1]]

^aapp-18-031

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The first loop writes `b[j]` from `a[j]`; the second reads that `b[j]` to update the same `a[j]`. Each loop is independently parallel, but a barrier between them is needed unless correct ownership/order is proved. Their opposite directions make an unqualified `nowait` unsafe. A better option is fusion: parallelize `for (j=0;j<100;j++) { b[j]=f1(a[j]); a[j]=f2(b[j]); }`, assuming pure functions and disjoint arrays. The reverse order of independent second-loop iterations does not affect results.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-032

Please describe the differences between flow, output, and anti-dependencies. (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=1|2025-09-05-2nd · Exercise 1B · p. 1]]

^aapp-18-032

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **RAW (flow/true):** a write must precede a read of its result, e.g. `x=...; y=x+1`. **WAR (anti):** a read must precede a later overwrite, e.g. `y=x+1; x=...`. **WAW (output):** writes to the same location must preserve their order to retain the correct final value. These can be within one iteration or carried between iterations. WAR and WAW are often removable by renaming; RAW generally requires preserving the producer-to-consumer computation.

### AAPP-18-033

Consider the following nested loop:

```c
        for (i=0; i<100; i++) {
          for (j=0; j<100; j++)
            b[i][j] += f(a[i][j]);
          for (j=99; j>=0; j++)
            a[i][j] += f(b[i][j]);
        }
```

Which loop can be parallelized and under which conditions (i and j are declared as integers)? Is there a way to improve the code? Is the OpenMP nowait clause a possible option? Justify your answers. (2)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=1|2025-09-05-2nd · Exercise 1C · p. 1]]

^aapp-18-033

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **The printed second loop uses `j++` while testing `j>=0`; it runs out of bounds instead of terminating.** It cannot be assigned a valid result as written. If the intended correction is `j--`, the two phases for each row may be fused per cell when the functions are pure and arrays do not alias. Parallelize rows, preserving each cell's first update before its dependent second update. If keeping separate worksharing loops, retain synchronization wherever the second consumes the first loop's results.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.

### AAPP-18-034

Under what conditions can the following code be parallelized? Is there a way to write the code for better efficiency if these conditions are met? (2)

```c
double total_sum = 0.0;
for (i = 0; i < 100; i++)
   for (j = 2; j < 100; j += 2) {
       a[i][j] = f(a[i][j]) + b[i][j-2];
       total_sum += a[i][j];
   }
for (i = 0; i < 100; i++)
   for (j = 3; j < 100; j += 2) {
       c[i][j] = f(a[i][j]) + b[i][j-2];
       total_sum += c[i][j];
   }
```

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=2|2025-12-18-2nd · Exercise 1C · p. 2]]

^aapp-18-034

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The first phase updates even-indexed `a` values and accumulates a floating-point sum. The second reads odd-indexed `a` values and writes separate `c` cells, so it does not consume the modified even entries. Both phases update the same `total_sum`, so use a reduction for **both** phases (or one fused outer-row reduction) and independent parallel cell/row work; the phases may overlap or fuse when all accesses are disjoint as printed. Preserve the reduction's initial value and wait for its completion before using `sum`. Floating-point reassociation may change rounding.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.
>
> ```c
> #pragma omp parallel for reduction(+:total_sum)
> for (int i=0; i<100; ++i) {
>     for (int j=2; j<100; j+=2) {
>         a[i][j] = f(a[i][j]) + b[i][j-2];
>         total_sum += a[i][j];
>     }
>     for (int j=3; j<100; j+=2) {
>         c[i][j] = f(a[i][j]) + b[i][j-2];
>         total_sum += c[i][j];
>     }
> }
> ```

### AAPP-18-035

What is meant by Loop-carried dependency? Please provide an example with a short code snippet that demonstrates a loop-carried dependency that cannot be parallelized. (1)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=1|2026-1-22-2nd · Exercise 1A · p. 1]]

^aapp-18-035

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An arbitrary recurrence such as `a[i]=f(a[i-1])` contains a true loop-carried RAW dependence: iteration $i$ needs the value produced by $i-1$. Adding `parallel for` is incorrect. Independent rows/chains can still run concurrently; a special associative recurrence may be reformulated as a scan. With an arbitrary `f`, there is no general transformation that removes the producer-to-consumer chain without changing the algorithm.

### AAPP-18-036

Given the following C-based code:

```c
int acc = 0;
for (i = 0; i < 100; i++)
   for (j = 1; j < 100; j += 2) {
       a[i][j] += a[i][j-1];
       acc += a[i][j];
   }
for (i = 0; i < 100; i++)
   for (j = 2; j < 100; j += 2) {
       c[i][j] += f(a[i][j]) + b[i][j-2];
   }
```

Where both matrices a, b and c store integers and already contain actual data (e.g., are not full of zeros). How and under what conditions can the previous code be parallelized? Is there a way to write the code exploiting parallel OMP pragmas? (2)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=2|2026-1-22-2nd · Exercise 1C · p. 2]]

^aapp-18-036

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The first loop updates odd columns of `a` using even columns and adds contributions to `acc`; the second reads even columns of `a`, which the first does not modify, and updates distinct `c` entries. Thus there is no inter-phase RAW dependence through `a` as printed. Parallelize with `reduction(+:acc)` on the first phase and parallelize the second; fusion by row can reduce overhead. Keep a barrier before consuming the final `acc`, and avoid undefined signed overflow.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.
>
> ```c
> #pragma omp parallel
> {
>     #pragma omp for collapse(2) reduction(+:acc)
>     for (int i=0; i<100; ++i)
>         for (int j=1; j<100; j+=2) {
>             a[i][j] += a[i][j-1];
>             acc += a[i][j];
>         }
>     #pragma omp for collapse(2)
>     for (int i=0; i<100; ++i)
>         for (int j=2; j<100; j+=2)
>             c[i][j] += f(a[i][j]) + b[i][j-2];
> }
> ```

### AAPP-18-037

Given the following C-based code:

```c
int acc = 0;
for (i = 3; i < 100; i++)
   for (j = 1; j < 100; j ++) {
       a[i][2*j] = f(a[i-3][2*j-1]);
   }
for (i = 0; i < 100; i++)
   for (j = 0; j < 100; j ++) {
       c[i][j] += a[i][2*j+1]) + b[i][j];
   }
```

Where both matrices a, b and c store integers and already contain actual data (e.g., are not full of zeros). How and under what conditions can the previous code be parallelized? Which OMP pragmas will you use to parallelize the code? (2)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=2|2026-2-09-2nd · Exercise 1C · p. 2]]

^aapp-18-037

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **Resolve the printed extra closing parenthesis and array bounds first:** subscripts `2*j`, `2*j-1` and `2*j+1` reach 198, 197 and 199 respectively, so at least 200 columns are needed across the two printed column ranges. After those corrections, the first phase writes even columns of `a` but reads odd ones; the second also reads odd columns, including its shifted-row reads. These are not producer-to-consumer dependences on the even writes. Therefore independent output cells/rows can be parallelized, and the phases can overlap if their destinations and side effects are disjoint. The shifted row index alone does not establish a dependence.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.
>
> After explicitly removing the source's stray parenthesis and ensuring at least 200 columns in `a`:
>
> ```c
> #pragma omp parallel
> {
>     #pragma omp for collapse(2) nowait
>     for (int i=3; i<100; ++i)
>         for (int j=1; j<100; ++j)
>             a[i][2*j] = f(a[i-3][2*j-1]);
>     #pragma omp for collapse(2)
>     for (int i=0; i<100; ++i)
>         for (int j=0; j<100; ++j)
>             c[i][j] += a[i][2*j+1] + b[i][j];
> }
> ```

### AAPP-18-038

Please provide a practical example of instruction dependency that prevents parallelization and an example that does not prevent parallelization. (1)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=1|2026-6-11-2nd · Exercise 1B · p. 1]]

^aapp-18-038

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For `x=f(...); y=g(x);`, the second operation has a RAW dependence and must see the value produced by the first. Operations using unrelated inputs and outputs can execute concurrently. WAR and WAW conflicts caused only by temporary reuse can be removed by separate variables, but renaming the RAW example still leaves `g` dependent on the result of `f`. Check memory aliases and hidden state in called functions as well as visible variable names.

### AAPP-18-039

Given the following C-based code:

```c
int sum = 0;
for (i = 2; i < 100; i++) {
   for (j = 1; j < 100; j++) {
       x[i][j] = g(x[i-2][j], y[i][j-1]);
   }
}
for (i = 0; i < 100; i++) {
   for (j = 1; j < 100; j++) {
       z[i][j] = z[i][j] + x[i][j] * w[i][j];
       sum += z[i][j];
   }
}
```

where matrices x, y, z, and w store integers and already contain valid data before the execution of the code. Discuss how and under which conditions the previous code can be parallelized. In particular, identify possible loop-carried dependencies, specify which loops can be safely parallelized, and state which OpenMP pragmas you would use. Discuss how the variable sum must be handled. (2)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=2|2026-6-11-2nd · Exercise 1C · p. 2]]

^aapp-18-039

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The first nest has a RAW dependence along `i` at distance 2. Different columns, and the even/odd row chains within each column, can run concurrently, while each chain advances in increasing `i`. Finish the required `x` values before the second phase consumes them. The `z` cell updates are independent and `sum += ...` is a reduction, so use a parallel loop with `reduction(+:sum)` there. Any shared side effects in `g` would require additional analysis.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.
>
> For example, parallelize columns while retaining each column's row chains, then use a reduction after the implicit barrier:
>
> ```c
> #pragma omp parallel
> {
>     #pragma omp for
>     for (int j=1; j<100; ++j)
>         for (int i=2; i<100; ++i)
>             x[i][j] = g(x[i-2][j], y[i][j-1]);
>     #pragma omp for collapse(2) reduction(+:sum)
>     for (int i=0; i<100; ++i)
>         for (int j=1; j<100; ++j) {
>             z[i][j] += x[i][j] * w[i][j];
>             sum += z[i][j];
>         }
> }
> ```
>
> Require pure/thread-safe `g` and defined integer arithmetic. This column decomposition is correct but can be strided in row-major storage.

### AAPP-18-040

Please provide a practical example of a loop carry dependency that cannot be parallelizable. (1)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=1|2026-6-29-2nd · Exercise 1B · p. 1]]

^aapp-18-040

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An arbitrary recurrence such as `a[i]=f(a[i-1])` contains a true loop-carried RAW dependence: iteration $i$ needs the value produced by $i-1$. Adding `parallel for` is incorrect. Independent rows/chains can still run concurrently; a special associative recurrence may be reformulated as a scan. With an arbitrary `f`, there is no general transformation that removes the producer-to-consumer chain without changing the algorithm.

### AAPP-18-041

Given the following C-based code:

```c
int sum = 0;
for (i = 4; i < 100; i++) {
   for (j = 1; j < 100; j++) {
       x[i][j] = g(x[i-4][j], y[i][j-1]);
   }
}
for (i = 0; i < 100; i++) {
   for (j = 1; j < 100; j++) {
       z[i][j-1] = z[i][j-1] + x[i][j-1] * w[i][j-1];
       sum *= z[i][j-1];
   }
}
```

where matrices x, y, z, and w store integers and already contain valid data before the execution of the code. Discuss when function g prevents code parallelization (a practical example is required). Is the memory layout of x,y,z creating issues for the parallelization of the code (show an example where this is going to happen)? How and under what conditions can the previous code be parallelized? (2)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=2|2026-6-29-2nd · Exercise 1C · p. 2]]

^aapp-18-041

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The `x` recurrence has outer distance 4, so process columns and the four residue classes of `i` concurrently, preserving increasing order within each chain. Complete those producers before the `z` phase. **The printed `sum` starts at 0 and is multiplied**, so it remains 0 in defined ordinary arithmetic; the independent `z` updates must still run. Parallelize `z` and retain `sum=0`. A signed-integer product reduction can introduce overflow in nonzero private partial products even though the original accumulator stays zero, so it is not automatically equivalent. If a nonzero product was intended, state the changed initialization and suitable arithmetic assumptions. A `g` that modifies a shared static counter, for example, would race; strided layout/false sharing affects performance, while actual aliases can introduce additional dependences.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.
>
> ```c
> #pragma omp parallel
> {
>     #pragma omp for
>     for (int j=1; j<100; ++j)
>         for (int i=4; i<100; ++i)
>             x[i][j] = g(x[i-4][j], y[i][j-1]);
>     #pragma omp for collapse(2)
>     for (int i=0; i<100; ++i)
>         for (int j=1; j<100; ++j)
>             z[i][j-1] += x[i][j-1] * w[i][j-1];
> }
> /* sum retains its original zero value. */
> ```
>
> For a concrete layout cost, assigning neighboring columns to different threads can make them update distinct elements on the same cache line (false sharing), while walking a column in row-major storage causes large strides. Neither alone changes the mathematical dependence; a `g` with `static int calls; ++calls;` would instead introduce a race.

### AAPP-18-042

Given the following C-based code:

```c
for (i=1; i<n; i++)
   for (j=1; j<m; j++)
       x[i][j] = x[i-1][j] + x[i][j-1] + y[i][j]
for (i = 0; i < 100; i++) {
   for (j = 1; j < 100; j++) {
       z[i][j] = z[i][j-1] - x[i][j-1] + w[i][j-1];
   }
}
```

where matrices x, y, z, and w store integers and already contain valid data before the execution of the code. Discuss when function g prevents code parallelization (a practical example is required). Is the memory layout of x,y,z and w creating issues for the parallelization of the code (show an example where this is going to happen)? How and under what conditions can the previous code be parallelized? (2)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=2|2026-9-10-2nd · Exercise 1C · p. 2]]

^aapp-18-042

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The first nest reads the preceding row and preceding column of `x`, so its cells require a **wavefront** schedule: run cells with equal `i+j` concurrently after the previous diagonal, or create tiled tasks with dependencies on the upper and left tiles. The second nest has a left-to-right recurrence within each row of `z`; parallelize rows while retaining sequential columns. Wait for required `x` values before consuming them. **Source issues:** the first assignment lacks a semicolon, the fixed bounds require arrays large enough for the referenced cells, and the question mentions `g` although no `g` call appears in the printed snippet. Do not invent a particular side effect for that missing function.
>
> **Assumptions:** Assume valid array bounds, distinct non-aliasing arrays where applicable, and a pure, thread-safe, constant-cost `f`. Preserve the original ordering of any actual flow dependences.
>
> One direct wavefront implementation is:
>
> ```c
> #pragma omp parallel
> {
>     for (int d=2; d<=n+m-2; ++d) {
>         #pragma omp for
>         for (int i=1; i<n; ++i) {
>             int j=d-i;
>             if (j>=1 && j<m)
>                 x[i][j]=x[i-1][j]+x[i][j-1]+y[i][j];
>         } // implicit barrier before the next diagonal
>     }
>     #pragma omp for
>     for (int i=0; i<100; ++i)
>         for (int j=1; j<100; ++j)
>             z[i][j]=z[i][j-1]-x[i][j-1]+w[i][j-1];
> }
> ```
>
> Assume `n,m>=100`, compatible dimensions and defined arithmetic, or adapt the second phase's fixed bounds to the actual domain. Wavefront cells are scattered in row-major storage; tiled dependent tasks improve locality and amortize barriers. A hypothetical `g` that increments shared state would require synchronization, but no such call is present in this source.

## Parallel patterns

Related notes: [[PRAM]] (introductory patterns only).

### AAPP-19-001

Describe the map parallel pattern and at least one fusion optimization that can be applied to it.

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=3|2022-02-11-2nd-a · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=3|2022-02-11-2nd-b · Exercise 2C · p. 3]]

^aapp-19-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Map applies a function independently to each element: $y_i=f(x_i)$. Assume independent outputs and no conflicting shared side effects. For constant-cost $f$, PRAM depth is $O(1)$ with $n$ processors and work is $\Theta(n)$; with $p$ processors time is $\Theta(\lceil n/p\rceil)$ in the ideal model. Example: square each array element.
>
> ```c
> #pragma omp parallel for
> for (int i=0; i<n; ++i) y[i] = f(x[i]);
> ```
>
> Two successive maps can fuse to `y[i]=g(f(x[i]))`, eliminating a temporary array and an extra traversal, provided intermediate values are not otherwise needed.

### AAPP-19-002

Describe the scan parallel pattern. Can it be implemented using different approaches with respect to the computation of intermediate values?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=3|2022-06-09-2nd-a · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=3|2022-06-09-2nd-b · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=3|2022-09-07-2nd-b · Exercise 2B · p. 3]]

^aapp-19-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The **workpile** pattern maintains a shared collection of pending tasks, which workers repeatedly remove and execute; tasks may generate additional tasks. It suits irregular searches and graph/tree exploration where work and task count are not known in advance. A fixed Pthreads pool can use a mutex-protected queue and condition variables; OpenMP tasks provide a higher-level implementation. Protect queue operations, balance granularity, and detect termination using both pending and active tasks: an empty queue alone does not mean active workers will create no more work.

### AAPP-19-003

Describe the workpile pattern, situations where it may be applied and possible implementations.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=3|2022-06-30-2nd-a · Exercise 2A · p. 3]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=3|2022-06-30-2nd-b · Exercise 2A · p. 3]]

^aapp-19-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **Fork-join** starts concurrent branches and waits for their completion before continuing. It fits independent subproblems in divide-and-conquer, such as recursively sorting both halves. OpenMP uses `parallel` for a team and tasks within a `single` region to create recursive work, followed by `taskwait` or a `taskgroup`; Pthreads uses `pthread_create` and `pthread_join`. A task pool avoids creating an operating-system thread at every recursive call. Choose a sequential cutoff for small subproblems.

### AAPP-19-004

Is the Quicksort algorithm easy to parallelize? Propose a high-level description of a possible parallelization and analyze its potential bottlenecks.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=3|2022-06-30-2nd-a · Exercise 2B · p. 3]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=3|2022-06-30-2nd-b · Exercise 2B · p. 3]]

^aapp-19-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes, the two recursive subproblems after partitioning are independent and map naturally to tasks, but efficient scaling needs more than spawning them. With sequential partitioning, balanced quicksort has work $\Theta(n\log n)$ and span $\Theta(n)$, so average parallelism is only $\Theta(\log n)$. An imbalanced pivot can make work and span quadratic. Random pivots or robust partitioning, a task-size cutoff and load balancing help. A work-efficient parallel partition reduces partition depth to $O(\log n)$; in a balanced recursion this gives $O(\log^2 n)$ span while retaining $O(n\log n)$ work.

### AAPP-19-005

Describe how to implement a map pattern with one of the parallel programming models presented in the course.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=3|2022-06-30-2nd-a · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=3|2022-06-30-2nd-b · Exercise 2C · p. 3]]

^aapp-19-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Map applies a function independently to each element: $y_i=f(x_i)$. Assume independent outputs and no conflicting shared side effects. For constant-cost $f$, PRAM depth is $O(1)$ with $n$ processors and work is $\Theta(n)$; with $p$ processors time is $\Theta(\lceil n/p\rceil)$ in the ideal model. Example: square each array element.
>
> ```c
> #pragma omp parallel for
> for (int i=0; i<n; ++i) y[i] = f(x[i]);
> ```
>
> Two successive maps can fuse to `y[i]=g(f(x[i]))`, eliminating a temporary array and an extra traversal, provided intermediate values are not otherwise needed.

### AAPP-19-006

Please define what a parallel reduction is: assumptions, complexity, example.(1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2A · p. 3]]

^aapp-19-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Reduce combines $n$ values with an associative operator, e.g. sum, maximum or logical OR. An identity handles empty partitions; commutativity is unnecessary if the original operand order is preserved by the tree. A balanced tree has $\Theta(n)$ work and $\Theta(\log n)$ depth, versus sequential $\Theta(n)$ time and work. With $p$ processors, a work-efficient implementation takes $O(n/p+\log p)$ time. Example: sum an array, using OpenMP `reduction(+:sum)`. Floating-point addition is not exactly associative, so a parallel sum may round differently. Fuse a preceding map into the local reduction to avoid materializing all transformed values.

### AAPP-19-007

Please describe how a parallel pattern gather works. (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2B · p. 3]]

^aapp-19-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Gather uses one index per output: `y[i]=x[index[i]]`. Each processor owns a distinct output, so repeated indices cause only shared reads. Assume all indices are valid and the output does not overwrite unread input. For $m$ outputs, CREW PRAM depth is $O(1)$ with $m$ processors and work is $\Theta(m)$; EREW needs distinct input reads or explicit replication. Example: select ten entries from a hundred-element array using a ten-element index array. Gather also implements the final placement step of Unpack and Unsplit.

### AAPP-19-008

Describe all the collision rules for a scatter pattern. (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2C · p. 3]]
Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2C · p. 3]]

^aapp-19-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-009

Describe how the pack parallel pattern could be parallelly implemented. (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2D · p. 3]]

^aapp-19-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

### AAPP-19-010

Please describe the stencil pattern: assumptions, complexity, example. (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2A · p. 3]]

^aapp-19-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A stencil computes each output from a fixed neighborhood of input values, for example a 2D five-point average. Define boundary behavior and use separate input/output buffers, or otherwise preserve which time step each read sees. With a constant-size neighborhood and $n$ output cells, one step has $\Theta(n)$ work and $O(1)$ depth with $n$ processors on CREW PRAM. Overlapping neighborhoods create concurrent reads, so EREW needs replication or an appropriate schedule. Multiple time steps require dependencies between steps, often implemented using double buffering and barriers or tiled wavefronts.

### AAPP-19-011

Please describe the differences between Split and Bin parallel patterns. (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2B · p. 3]]

^aapp-19-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Split stably partitions elements into two groups according to a Boolean predicate, retaining their relative order within each group. Let group 1 precede group 0:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     pos = b[i] ? s[i] : K + (i - s[i])
>     out[pos] = x[i]
> ```
>
> The two destination ranges are disjoint and each element has a unique position. This is two complementary stable packs, implemented with one scan and one scatter. With a work-efficient scan it takes $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM. Bin generalizes classification to multiple buckets rather than just two; bucket sizes/offsets and collision-free positions must then be computed.

### AAPP-19-012

Given an input collection of 100 values and an auxiliary array of 10, which parallel pattern between the gather and the scatter is producing an output collection of 10 values? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2C · p. 3]]

^aapp-19-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **Gather**, if the ten-element auxiliary array contains the input indices to read: `out[i]=input[index[i]]` for `i=0..9`, so output length is 10. A scatter normally supplies one destination index for each input value and therefore requires 100 such indices for 100 inputs. Merely knowing array sizes is insufficient without their roles, so the interpretation of the auxiliary array as an index list is essential.

### AAPP-19-013

What is meant by separating hyperplane in a recurrence parallelization? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2D · p. 3]]

^aapp-19-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A separating hyperplane partitions an iteration/dependence space into ordered fronts so that required predecessors lie on earlier fronts, while operations on the same front are independent. For a 2D recurrence depending on the cell above and to the left, the anti-diagonals `i+j=k` are parallel fronts: compute increasing `k`, processing all cells on each front concurrently. A valid choice must orient every dependence forward; an arbitrary geometric cut is not necessarily a valid schedule.

### AAPP-19-014

Please describe the map pattern: assumptions, complexity, example. (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2A · p. 3]]

^aapp-19-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Map applies a function independently to each element: $y_i=f(x_i)$. Assume independent outputs and no conflicting shared side effects. For constant-cost $f$, PRAM depth is $O(1)$ with $n$ processors and work is $\Theta(n)$; with $p$ processors time is $\Theta(\lceil n/p\rceil)$ in the ideal model. Example: square each array element.
>
> ```c
> #pragma omp parallel for
> for (int i=0; i<n; ++i) y[i] = f(x[i]);
> ```
>
> Two successive maps can fuse to `y[i]=g(f(x[i]))`, eliminating a temporary array and an extra traversal, provided intermediate values are not otherwise needed.

### AAPP-19-015

Please describe the differences between Zip and Unzip parallel patterns. (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2B · p. 3]]

^aapp-19-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Zip combines equally indexed elements of multiple collections into tuples; Unzip separates a tuple collection into component arrays:
>
> ```text
> parallel for i = 0 .. n-1: tuples[i] = (a[i], b[i])  // zip
> parallel for i = 0 .. n-1:                         // unzip
>     a[i] = tuples[i].first
>     b[i] = tuples[i].second
> ```
>
> Assume valid equal lengths (or a specified truncation policy), distinct destinations and no harmful aliasing. Both have $\Theta(n)$ work and $O(1)$ depth with $n$ processors under unit-cost tuple access. Zip may also denote elementwise processing of several aligned inputs, e.g. `c[i]=a[i]+b[i]`; state the chosen convention.

### AAPP-19-016

What is meant by “permutation scatter”? (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2D · p. 3]]
Source: [[Tema Esame 2023-07-11-2nd.pdf#page=3|2023-07-11-2nd · Exercise 2C · p. 3]]

^aapp-19-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-017

Is it possible to implement a pipeline paradigm using OpenMP? What parallel paradigm is adopted by default in OpenMP?(2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=4|2023-02-14-2nd · Exercise 3A · p. 4]]

^aapp-19-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pipeline parallelism divides each item into ordered stages, while overlapping different items across stages. Example: read frame $k+1$, filter frame $k$, encode frame $k-1$. Use Pthreads stage workers with synchronized bounded queues, or OpenMP tasks with producer/consumer `depend` clauses and storage that remains alive until completion. OpenMP's basic execution model is fork-join; a pipeline is an additional pattern that must be expressed explicitly. Good throughput requires enough items, sufficiently large stages and a balanced bottleneck stage, with communication costs controlled. If stage times are $t_1,\ldots,t_s$, ideal steady-state time per item cannot beat $\max t_i$; startup/drain still cost roughly $\sum t_i$.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-19-018

Please describe the reduce pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=3|2023-06-19-2nd · Exercise 2A · p. 3]]
Source: [[Tema Esame 2023-09-11-2nd.pdf#page=3|2023-09-11-2nd · Exercise 2A · p. 3]]

^aapp-19-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Reduce combines $n$ values with an associative operator, e.g. sum, maximum or logical OR. An identity handles empty partitions; commutativity is unnecessary if the original operand order is preserved by the tree. A balanced tree has $\Theta(n)$ work and $\Theta(\log n)$ depth, versus sequential $\Theta(n)$ time and work. With $p$ processors, a work-efficient implementation takes $O(n/p+\log p)$ time. Example: sum an array, using OpenMP `reduction(+:sum)`. Floating-point addition is not exactly associative, so a parallel sum may round differently. Fuse a preceding map into the local reduction to avoid materializing all transformed values.

### AAPP-19-019

Please describe the differences between Gather and scatter parallel patterns. (1)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=3|2023-06-19-2nd · Exercise 2B · p. 3]]

^aapp-19-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Gather is output-driven: `out[i]=in[index[i]]`, so each output selects an input and repeated indices cause only shared reads. Scatter is input-driven: `out[index[i]]=in[i]`, so each input chooses its destination and repeated indices cause write collisions. A valid scatter must require unique destinations or define a collision-resolution rule; gather instead needs valid source indices and protection against harmful input/output aliasing.

### AAPP-19-020

What is meant by “merge scatter”? (1)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=3|2023-06-19-2nd · Exercise 2C · p. 3]]

^aapp-19-020

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-021

Please describe the stencil pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=3|2023-07-11-2nd · Exercise 2A · p. 3]]

^aapp-19-021

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A stencil computes each output from a fixed neighborhood of input values, for example a 2D five-point average. Define boundary behavior and use separate input/output buffers, or otherwise preserve which time step each read sees. With a constant-size neighborhood and $n$ output cells, one step has $\Theta(n)$ work and $O(1)$ depth with $n$ processors on CREW PRAM. Overlapping neighborhoods create concurrent reads, so EREW needs replication or an appropriate schedule. Multiple time steps require dependencies between steps, often implemented using double buffering and barriers or tiled wavefronts.

### AAPP-19-022

Please describe how the Pack parallel pattern could be implemented. (1)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=3|2023-07-11-2nd · Exercise 2B · p. 3]]

^aapp-19-022

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

### AAPP-19-023

Please describe what is meant by pipelined parallelism and how could be implemented in OpenMP?(2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=4|2023-07-11-2nd · Exercise 3A · p. 4]]

^aapp-19-023

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pipeline parallelism divides each item into ordered stages, while overlapping different items across stages. Example: read frame $k+1$, filter frame $k$, encode frame $k-1$. Use Pthreads stage workers with synchronized bounded queues, or OpenMP tasks with producer/consumer `depend` clauses and storage that remains alive until completion. OpenMP's basic execution model is fork-join; a pipeline is an additional pattern that must be expressed explicitly. Good throughput requires enough items, sufficiently large stages and a balanced bottleneck stage, with communication costs controlled. If stage times are $t_1,\ldots,t_s$, ideal steady-state time per item cannot beat $\max t_i$; startup/drain still cost roughly $\sum t_i$.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-19-024

Please describe how the Unpack parallel pattern could be implemented. (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=3|2023-09-11-2nd · Exercise 2B · p. 3]]

^aapp-19-024

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Unpack places a packed sequence into positions selected by a known mask, supplying a specified default at unselected positions. It requires the mask (or equivalent position information); it cannot recover discarded original values from the packed sequence alone.
>
> ```text
> s = exclusive_scan(mask, +, 0)
> parallel for i = 0 .. n-1:
>     out[i] = mask[i] ? packed[s[i]] : default_value
> ```
>
> Require `length(packed) == sum(mask)` and Boolean mask values. The final step is a gather with distinct selected source indices. A work-efficient scan gives $\Theta(n)$ work and $\Theta(\log n)$ depth; if the prefix positions are already supplied, placement has $O(1)$ depth with $n$ processors.

### AAPP-19-025

Please describe the scan pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=3|2023-12-21-2nd · Exercise 2A · p. 3]]

^aapp-19-025

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scan produces every prefix of a sequence under an associative operator. Inclusive scan is $y_i=x_0\circ\cdots\circ x_i$; exclusive scan is $y_0=e$ and $y_i=x_0\circ\cdots\circ x_{i-1}$, where $e$ is the identity. For `[3,1,4]`, addition gives inclusive `[3,4,8]` and exclusive `[0,3,4]`. A work-efficient tree up-sweep/down-sweep uses $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM; simple recursive doubling instead uses $\Theta(n\log n)$ work. Preserve operand order for noncommutative operators. Scan computes positions for Pack, Unpack, Split and Unsplit.

### AAPP-19-026

Please describe how the Split parallel pattern could be implemented. (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=3|2023-12-21-2nd · Exercise 2B · p. 3]]

^aapp-19-026

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Split stably partitions elements into two groups according to a Boolean predicate, retaining their relative order within each group. Let group 1 precede group 0:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     pos = b[i] ? s[i] : K + (i - s[i])
>     out[pos] = x[i]
> ```
>
> The two destination ranges are disjoint and each element has a unique position. This is two complementary stable packs, implemented with one scan and one scatter. With a work-efficient scan it takes $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM. Bin generalizes classification to multiple buckets rather than just two; bucket sizes/offsets and collision-free positions must then be computed.

### AAPP-19-027

Please describe the parallel gather pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=3|2024-01-26-2nd · Exercise 2A · p. 3]]

^aapp-19-027

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Gather uses one index per output: `y[i]=x[index[i]]`. Each processor owns a distinct output, so repeated indices cause only shared reads. Assume all indices are valid and the output does not overwrite unread input. For $m$ outputs, CREW PRAM depth is $O(1)$ with $m$ processors and work is $\Theta(m)$; EREW needs distinct input reads or explicit replication. Example: select ten entries from a hundred-element array using a ten-element index array. Gather also implements the final placement step of Unpack and Unsplit.

### AAPP-19-028

Please describe how the “Merge collision resolution” works. Is it related to the parallel gather pattern? (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=3|2024-01-26-2nd · Exercise 2B · p. 3]]

^aapp-19-028

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.
>
> Merge collision resolution belongs to **scatter**, where several inputs target one output. Ordinary gather has a unique owner per output; repeated indices only mean concurrent reads and require no merge of competing writes.

### AAPP-19-029

Please describe the parallel scatter pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=3|2024-02-16-2nd · Exercise 2A · p. 3]]

^aapp-19-029

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-030

Please describe how the Pack parallel pattern works. How is implemented? (2)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=3|2024-02-16-2nd · Exercise 2B · p. 3]]

^aapp-19-030

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

### AAPP-19-031

Please describe the parallel reduce pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=3|2024-06-26-2nd · Exercise 2A · p. 3]]
Source: [[Tema Esame 2024-09-05-2nd.pdf#page=3|2024-09-05-2nd · Exercise 2A · p. 3]]

^aapp-19-031

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Reduce combines $n$ values with an associative operator, e.g. sum, maximum or logical OR. An identity handles empty partitions; commutativity is unnecessary if the original operand order is preserved by the tree. A balanced tree has $\Theta(n)$ work and $\Theta(\log n)$ depth, versus sequential $\Theta(n)$ time and work. With $p$ processors, a work-efficient implementation takes $O(n/p+\log p)$ time. Example: sum an array, using OpenMP `reduction(+:sum)`. Floating-point addition is not exactly associative, so a parallel sum may round differently. Fuse a preceding map into the local reduction to avoid materializing all transformed values.

### AAPP-19-032

Please describe how the Split parallel pattern works. How is it implemented? (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=3|2024-06-26-2nd · Exercise 2B · p. 3]]

^aapp-19-032

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Split stably partitions elements into two groups according to a Boolean predicate, retaining their relative order within each group. Let group 1 precede group 0:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     pos = b[i] ? s[i] : K + (i - s[i])
>     out[pos] = x[i]
> ```
>
> The two destination ranges are disjoint and each element has a unique position. This is two complementary stable packs, implemented with one scan and one scatter. With a work-efficient scan it takes $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM. Bin generalizes classification to multiple buckets rather than just two; bucket sizes/offsets and collision-free positions must then be computed.

### AAPP-19-033

Please describe the parallel Split pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=3|2024-07-24-2nd · Exercise 2A · p. 3]]

^aapp-19-033

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Split stably partitions elements into two groups according to a Boolean predicate, retaining their relative order within each group. Let group 1 precede group 0:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     pos = b[i] ? s[i] : K + (i - s[i])
>     out[pos] = x[i]
> ```
>
> The two destination ranges are disjoint and each element has a unique position. This is two complementary stable packs, implemented with one scan and one scatter. With a work-efficient scan it takes $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM. Bin generalizes classification to multiple buckets rather than just two; bucket sizes/offsets and collision-free positions must then be computed.

### AAPP-19-034

Please describe how the Unzip parallel pattern works. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=3|2024-07-24-2nd · Exercise 2B · p. 3]]

^aapp-19-034

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Zip combines equally indexed elements of multiple collections into tuples; Unzip separates a tuple collection into component arrays:
>
> ```text
> parallel for i = 0 .. n-1: tuples[i] = (a[i], b[i])  // zip
> parallel for i = 0 .. n-1:                         // unzip
>     a[i] = tuples[i].first
>     b[i] = tuples[i].second
> ```
>
> Assume valid equal lengths (or a specified truncation policy), distinct destinations and no harmful aliasing. Both have $\Theta(n)$ work and $O(1)$ depth with $n$ processors under unit-cost tuple access. Zip may also denote elementwise processing of several aligned inputs, e.g. `c[i]=a[i]+b[i]`; state the chosen convention.

### AAPP-19-035

Please explain how the parallel shift pattern functions and provide its implementation (including pseudo-code). Also, please indicate its complexity. (2)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=3|2024-09-05-2nd · Exercise 2B · p. 3]]

^aapp-19-035

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Shift moves elements by a fixed displacement. Define boundaries explicitly; for a non-cyclic right shift by $d\ge0$ with padding:
>
> ```text
> parallel for i = 0 .. n-1:
>     out[i] = (i >= d) ? input[i-d] : pad
> ```
>
> Use separate input/output storage so writes cannot destroy unread values. Work is $\Theta(n)$ and PRAM depth is $O(1)$ with $n$ processors; each valid input is read at most once, so EREW suffices. A cyclic shift instead uses `input[(i-d+n)%n]` after normalizing $d$ modulo $n$; it has the same costs.

### AAPP-19-036

Please describe the parallel scan pattern, including assumptions, complexity, and examples. (2)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=2|2025-01-24-2nd · Exercise 2A · p. 2]]

^aapp-19-036

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scan produces every prefix of a sequence under an associative operator. Inclusive scan is $y_i=x_0\circ\cdots\circ x_i$; exclusive scan is $y_0=e$ and $y_i=x_0\circ\cdots\circ x_{i-1}$, where $e$ is the identity. For `[3,1,4]`, addition gives inclusive `[3,4,8]` and exclusive `[0,3,4]`. A work-efficient tree up-sweep/down-sweep uses $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM; simple recursive doubling instead uses $\Theta(n\log n)$ work. Preserve operand order for noncommutative operators. Scan computes positions for Pack, Unpack, Split and Unsplit.

### AAPP-19-037

Please discuss how the Zip parallel pattern works. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=2|2025-01-24-2nd · Exercise 2B · p. 2]]

^aapp-19-037

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Zip combines equally indexed elements of multiple collections into tuples; Unzip separates a tuple collection into component arrays:
>
> ```text
> parallel for i = 0 .. n-1: tuples[i] = (a[i], b[i])  // zip
> parallel for i = 0 .. n-1:                         // unzip
>     a[i] = tuples[i].first
>     b[i] = tuples[i].second
> ```
>
> Assume valid equal lengths (or a specified truncation policy), distinct destinations and no harmful aliasing. Both have $\Theta(n)$ work and $O(1)$ depth with $n$ processors under unit-cost tuple access. Zip may also denote elementwise processing of several aligned inputs, e.g. `c[i]=a[i]+b[i]`; state the chosen convention.

### AAPP-19-038

Please describe and show an example of Parallel Data Management Patterns: pipeline. (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=1|2025-02-14-2nd · Exercise 1A · p. 1]]

^aapp-19-038

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pipeline parallelism divides each item into ordered stages, while overlapping different items across stages. Example: read frame $k+1$, filter frame $k$, encode frame $k-1$. Use Pthreads stage workers with synchronized bounded queues, or OpenMP tasks with producer/consumer `depend` clauses and storage that remains alive until completion. OpenMP's basic execution model is fork-join; a pipeline is an additional pattern that must be expressed explicitly. Good throughput requires enough items, sufficiently large stages and a balanced bottleneck stage, with communication costs controlled. If stage times are $t_1,\ldots,t_s$, ideal steady-state time per item cannot beat $\max t_i$; startup/drain still cost roughly $\sum t_i$.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-19-039

Please describe the parallel Scatter pattern, including assumptions, PRAM-based complexity, and examples. (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=2|2025-02-14-2nd · Exercise 2A · p. 2]]

^aapp-19-039

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-040

Please discuss how the Pack parallel pattern works. How is it implemented (pseudo code required and PRAM-based complexity)? (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=2|2025-02-14-2nd · Exercise 2B · p. 2]]

^aapp-19-040

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

### AAPP-19-041

How does the Fork-Join pattern differ from a barrier in parallel programming? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=1|2025-06-05-2nd · Exercise 1A · p. 1]]

^aapp-19-041

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Fork-join creates/activates concurrent branches and later waits for their completion. A barrier is a rendezvous for an already existing group: each participant waits until all required participants arrive, then they can continue. A barrier does not itself create work or terminate threads; a join concerns completion of the joined branches/tasks. Fork-join implementations may use a barrier internally, but the abstractions describe different behavior.

### AAPP-19-042

How does the Workpile pattern differ from a standard Map pattern? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=1|2025-06-05-2nd · Exercise 1B · p. 1]]

^aapp-19-042

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Map processes a fixed input collection, with one independent application per element. Workpile processes a dynamically managed set of tasks; workers can add more tasks, and the task count and costs may be irregular. Both can use a fixed worker pool, but workpile additionally needs a safe queue, load balancing and termination detection that accounts for active task generators.

### AAPP-19-043

How can the map and reduce patterns be fused, and what is the benefit of doing so? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=2|2025-06-05-2nd · Exercise 2A · p. 2]]

^aapp-19-043

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Compute each mapped value and immediately combine it into a thread-local accumulator, then reduce the local accumulators. For example, sum squares using `sum += x[i]*x[i]` with OpenMP `reduction(+:sum)`. This preserves linear work and logarithmic ideal reduction depth while removing the intermediate array, an extra memory pass and often a synchronization point. The reduction operator must permit the chosen reassociation, and the map must have no conflicting shared effects.

### AAPP-19-044

In the context of parallel scan, what is the difference between an inclusive and an exclusive scan? What about the complexity? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=2|2025-06-05-2nd · Exercise 2B · p. 2]]

^aapp-19-044

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scan produces every prefix of a sequence under an associative operator. Inclusive scan is $y_i=x_0\circ\cdots\circ x_i$; exclusive scan is $y_0=e$ and $y_i=x_0\circ\cdots\circ x_{i-1}$, where $e$ is the identity. For `[3,1,4]`, addition gives inclusive `[3,4,8]` and exclusive `[0,3,4]`. A work-efficient tree up-sweep/down-sweep uses $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM; simple recursive doubling instead uses $\Theta(n\log n)$ work. Preserve operand order for noncommutative operators. Scan computes positions for Pack, Unpack, Split and Unsplit.

### AAPP-19-045

Please discuss how the Split parallel pattern works. How is it implemented (pseudo code required and PRAM-based complexity)? (2)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=2|2025-06-05-2nd · Exercise 2C · p. 2]]
Source: [[Tema Esame 2025-09-05-2nd.pdf#page=2|2025-09-05-2nd · Exercise 2B · p. 2]]

^aapp-19-045

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Split stably partitions elements into two groups according to a Boolean predicate, retaining their relative order within each group. Let group 1 precede group 0:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     pos = b[i] ? s[i] : K + (i - s[i])
>     out[pos] = x[i]
> ```
>
> The two destination ranges are disjoint and each element has a unique position. This is two complementary stable packs, implemented with one scan and one scatter. With a work-efficient scan it takes $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM. Bin generalizes classification to multiple buckets rather than just two; bucket sizes/offsets and collision-free positions must then be computed.

### AAPP-19-046

What are the challenges of using a shared state in a Map function? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=1|2025-07-04-2nd · Exercise 1B · p. 1]]

^aapp-19-046

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A map function should be independent across elements. Shared mutable state can cause races, order-dependent results and contention; a lock may restore correctness while serializing the hot path. Use immutable shared inputs, per-iteration/per-thread state, or an explicit reduction for a shared aggregate. For example, updating a global pseudorandom generator from every map iteration is unsafe or contentious; use independent streams or an index-based generator.

### AAPP-19-047

Please describe the parallel reduce pattern: assumptions, PRAM complexity, and example. What about the work done? Is it different from the one done by the sequential algorithm? (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=2|2025-07-04-2nd · Exercise 2A · p. 2]]

^aapp-19-047

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Reduce combines $n$ values with an associative operator, e.g. sum, maximum or logical OR. An identity handles empty partitions; commutativity is unnecessary if the original operand order is preserved by the tree. A balanced tree has $\Theta(n)$ work and $\Theta(\log n)$ depth, versus sequential $\Theta(n)$ time and work. With $p$ processors, a work-efficient implementation takes $O(n/p+\log p)$ time. Example: sum an array, using OpenMP `reduction(+:sum)`. Floating-point addition is not exactly associative, so a parallel sum may round differently. Fuse a preceding map into the local reduction to avoid materializing all transformed values.

### AAPP-19-048

Please discuss how the Unpack parallel pattern works. How is it implemented (pseudo code required and PRAM-based complexity)? (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=2|2025-07-04-2nd · Exercise 2B · p. 2]]

^aapp-19-048

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Unpack places a packed sequence into positions selected by a known mask, supplying a specified default at unselected positions. It requires the mask (or equivalent position information); it cannot recover discarded original values from the packed sequence alone.
>
> ```text
> s = exclusive_scan(mask, +, 0)
> parallel for i = 0 .. n-1:
>     out[i] = mask[i] ? packed[s[i]] : default_value
> ```
>
> Require `length(packed) == sum(mask)` and Boolean mask values. The final step is a gather with distinct selected source indices. A work-efficient scan gives $\Theta(n)$ work and $\Theta(\log n)$ depth; if the prefix positions are already supplied, placement has $O(1)$ depth with $n$ processors.

### AAPP-19-049

Please describe the parallel gather pattern, including assumptions, PRAM-based complexity, and examples. (2)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=2|2025-09-05-2nd · Exercise 2A · p. 2]]

^aapp-19-049

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Gather uses one index per output: `y[i]=x[index[i]]`. Each processor owns a distinct output, so repeated indices cause only shared reads. Assume all indices are valid and the output does not overwrite unread input. For $m$ outputs, CREW PRAM depth is $O(1)$ with $m$ processors and work is $\Theta(m)$; EREW needs distinct input reads or explicit replication. Example: select ten entries from a hundred-element array using a ten-element index array. Gather also implements the final placement step of Unpack and Unsplit.

### AAPP-19-050

What kind of problems may create a parallel scatter pattern? Please discuss and provide examples. (1)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=1|2025-12-18-2nd · Exercise 1A · p. 1]]

^aapp-19-050

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-051

Please describe the parallel gather pattern, including assumptions, complexity, and examples. (2)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=3|2025-12-18-2nd · Exercise 2A · p. 3]]

^aapp-19-051

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Gather uses one index per output: `y[i]=x[index[i]]`. Each processor owns a distinct output, so repeated indices cause only shared reads. Assume all indices are valid and the output does not overwrite unread input. For $m$ outputs, CREW PRAM depth is $O(1)$ with $m$ processors and work is $\Theta(m)$; EREW needs distinct input reads or explicit replication. Example: select ten entries from a hundred-element array using a ten-element index array. Gather also implements the final placement step of Unpack and Unsplit.

### AAPP-19-052

Please describe how the Pack parallel pattern works. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=3|2025-12-18-2nd · Exercise 2B · p. 3]]

^aapp-19-052

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

### AAPP-19-053

Please describe the parallel scan pattern, including assumptions, PRAM complexity. In which other parallel patterns discussed during the lecture have been used? (2)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=3|2026-1-22-2nd · Exercise 2A · p. 3]]

^aapp-19-053

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scan produces every prefix of a sequence under an associative operator. Inclusive scan is $y_i=x_0\circ\cdots\circ x_i$; exclusive scan is $y_0=e$ and $y_i=x_0\circ\cdots\circ x_{i-1}$, where $e$ is the identity. For `[3,1,4]`, addition gives inclusive `[3,4,8]` and exclusive `[0,3,4]`. A work-efficient tree up-sweep/down-sweep uses $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM; simple recursive doubling instead uses $\Theta(n\log n)$ work. Preserve operand order for noncommutative operators. Scan computes positions for Pack, Unpack, Split and Unsplit.

### AAPP-19-054

Please describe how the Split parallel pattern works and its performance considering a PRAM model. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=3|2026-1-22-2nd · Exercise 2B · p. 3]]

^aapp-19-054

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Split stably partitions elements into two groups according to a Boolean predicate, retaining their relative order within each group. Let group 1 precede group 0:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     pos = b[i] ? s[i] : K + (i - s[i])
>     out[pos] = x[i]
> ```
>
> The two destination ranges are disjoint and each element has a unique position. This is two complementary stable packs, implemented with one scan and one scatter. With a work-efficient scan it takes $\Theta(n)$ work and $\Theta(\log n)$ depth on EREW PRAM. Bin generalizes classification to multiple buckets rather than just two; bucket sizes/offsets and collision-free positions must then be computed.

### AAPP-19-055

Describe the map parallel pattern and at least one fusion optimization that can be applied to it. (1)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=1|2026-2-09-2nd · Exercise 1A · p. 1]]

^aapp-19-055

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Map applies a function independently to each element: $y_i=f(x_i)$. Assume independent outputs and no conflicting shared side effects. For constant-cost $f$, PRAM depth is $O(1)$ with $n$ processors and work is $\Theta(n)$; with $p$ processors time is $\Theta(\lceil n/p\rceil)$ in the ideal model. Example: square each array element.
>
> ```c
> #pragma omp parallel for
> for (int i=0; i<n; ++i) y[i] = f(x[i]);
> ```
>
> Two successive maps can fuse to `y[i]=g(f(x[i]))`, eliminating a temporary array and an extra traversal, provided intermediate values are not otherwise needed.

### AAPP-19-056

Please describe the parallel gather pattern, including assumptions, PRAM complexity. In which other parallel patterns discussed during the lecture has the gather been used? (2)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=3|2026-2-09-2nd · Exercise 2A · p. 3]]

^aapp-19-056

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Gather uses one index per output: `y[i]=x[index[i]]`. Each processor owns a distinct output, so repeated indices cause only shared reads. Assume all indices are valid and the output does not overwrite unread input. For $m$ outputs, CREW PRAM depth is $O(1)$ with $m$ processors and work is $\Theta(m)$; EREW needs distinct input reads or explicit replication. Example: select ten entries from a hundred-element array using a ten-element index array. Gather also implements the final placement step of Unpack and Unsplit.

### AAPP-19-057

Please describe how the Unsplit parallel pattern works and its performance considering a PRAM model. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=3|2026-2-09-2nd · Exercise 2B · p. 3]]

^aapp-19-057

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Unsplit reverses a stable two-way Split when the original Boolean mask and the order of the two groups are retained. If group 1 occupies `[0,K)` and group 0 occupies `[K,n)`, then:
>
> ```text
> s = exclusive_scan(mask, +, 0)
> K = sum(mask)                       // also available from the scan
> parallel for i = 0 .. n-1:
>     src = mask[i] ? s[i] : K + (i - s[i])
>     original[i] = split_array[src]
> ```
>
> This is a scan followed by a gather; source positions are unique. Work is $\Theta(n)$ and depth is $\Theta(\log n)$ on a work-efficient EREW PRAM implementation. Without the mask or equivalent permutation metadata the original interleaving cannot generally be recovered.

### AAPP-19-058

Describe the reduce parallel pattern and at least one fusion optimization that can be applied to it. (1)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=1|2026-6-11-2nd · Exercise 1A · p. 1]]

^aapp-19-058

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Reduce combines $n$ values with an associative operator, e.g. sum, maximum or logical OR. An identity handles empty partitions; commutativity is unnecessary if the original operand order is preserved by the tree. A balanced tree has $\Theta(n)$ work and $\Theta(\log n)$ depth, versus sequential $\Theta(n)$ time and work. With $p$ processors, a work-efficient implementation takes $O(n/p+\log p)$ time. Example: sum an array, using OpenMP `reduction(+:sum)`. Floating-point addition is not exactly associative, so a parallel sum may round differently. Fuse a preceding map into the local reduction to avoid materializing all transformed values.

### AAPP-19-059

Please provide a short pseudocode for the parallel scatter pattern. Discuss its assumptions and PRAM complexity. In which other parallel patterns discussed during the lecture has the scatter been used? (2)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=3|2026-6-11-2nd · Exercise 2A · p. 3]]

^aapp-19-059

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Scatter uses one destination index per input:
>
> ```text
> parallel for i = 0 .. n-1:
>     y[index[i]] = x[i]
> ```
>
> Assume valid indices, disjoint input/output storage, and specify how collisions are handled. With distinct destinations, EREW PRAM depth is $O(1)$ using $n$ processors and work is $\Theta(n)$. Repeated destinations require an explicit rule: reject them; allow only equal concurrent values; choose one winner (arbitrary or priority); or merge contributions with an associative operation. These are different semantics. A merge requires combining hardware or a reduction algorithm; an ordinary unsynchronized write does not implement a sum. Example: a permutation scatter has distinct destinations; a histogram has collisions and requires addition. Pack and Split use computed unique destinations to scatter safely.

### AAPP-19-060

Please describe how the Pack parallel pattern works and its performance considering a PRAM model. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=3|2026-6-11-2nd · Exercise 2B · p. 3]]

^aapp-19-060

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

### AAPP-19-061

Describe the map followed by a reduce parallel pattern providing PRAM complexity and show at least one example discussed during the lectures. (1)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=1|2026-6-29-2nd · Exercise 1A · p. 1]]

^aapp-19-061

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Map-Reduce first independently transforms inputs and then combines the results using an associative operator. A standard example is the sum of squares, $\sum_i x_i^2$, or the Monte Carlo $\pi$ computation in the bank: map each point to an inside-circle indicator and sum the indicators. Fuse transformation into each local reduction. For constant-cost transforms, work is $\Theta(n)$ and work-efficient PRAM depth is $\Theta(\log n)$; with $p$ processors, $O(n/p+\log p)$ time is achievable. These are standard examples; the supplied course notes do not identify which example was shown in this particular lecture.

### AAPP-19-062

Please describe how the Unpack parallel pattern works and its performance considering a PRAM model. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=3|2026-6-29-2nd · Exercise 2A · p. 3]]

^aapp-19-062

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Unpack places a packed sequence into positions selected by a known mask, supplying a specified default at unselected positions. It requires the mask (or equivalent position information); it cannot recover discarded original values from the packed sequence alone.
>
> ```text
> s = exclusive_scan(mask, +, 0)
> parallel for i = 0 .. n-1:
>     out[i] = mask[i] ? packed[s[i]] : default_value
> ```
>
> Require `length(packed) == sum(mask)` and Boolean mask values. The final step is a gather with distinct selected source indices. A work-efficient scan gives $\Theta(n)$ work and $\Theta(\log n)$ depth; if the prefix positions are already supplied, placement has $O(1)$ depth with $n$ processors.

### AAPP-19-063

Describe the scan followed by a reduce parallel pattern providing PRAM complexity and show at least one example discussed during the lectures. (1)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=1|2026-9-10-2nd · Exercise 1A · p. 1]]

^aapp-19-063

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A Scan-Reduce pipeline computes all prefixes and then reduces those prefixes. For example, scan account changes to obtain balances $b_i=\sum_{j\le i}x_j$, then reduce with maximum to obtain the largest balance. A work-efficient scan and a tree reduction each use $\Theta(n)$ work and $\Theta(\log n)$ depth, so the composition has the same asymptotic bounds. If the requested result is merely the total sum of inputs, the final prefix already contains it and an additional reduction is unnecessary. This is a standard illustrative example; the supplied notes do not establish the precise example used in the lecture.

### AAPP-19-064

Describe the parallel pipeline pattern and one condition required for good scalability. (1)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=1|2026-9-10-2nd · Exercise 1B · p. 1]]

^aapp-19-064

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pipeline parallelism divides each item into ordered stages, while overlapping different items across stages. Example: read frame $k+1$, filter frame $k$, encode frame $k-1$. Use Pthreads stage workers with synchronized bounded queues, or OpenMP tasks with producer/consumer `depend` clauses and storage that remains alive until completion. OpenMP's basic execution model is fork-join; a pipeline is an additional pattern that must be expressed explicitly. Good throughput requires enough items, sufficiently large stages and a balanced bottleneck stage, with communication costs controlled. If stage times are $t_1,\ldots,t_s$, ideal steady-state time per item cannot beat $\max t_i$; startup/drain still cost roughly $\sum t_i$.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-19-065

Describe the Pack pattern and give its PRAM work and time complexity. (2)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=3|2026-9-10-2nd · Exercise 2A · p. 3]]

^aapp-19-065

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pack is stable filtering: retain exactly the elements whose Boolean flags are 1, in original order. Compute each selected element's destination with an exclusive prefix sum, then scatter:
>
> ```text
> b[i] = predicate(x[i]) ? 1 : 0          // parallel map
> s = exclusive_scan(b, +, 0)
> K = (n == 0) ? 0 : s[n-1] + b[n-1]
> parallel for i = 0 .. n-1:
>     if b[i] == 1: out[s[i]] = x[i]
> ```
>
> Selected destinations are unique, so there are no write collisions. With constant-cost predicates and a work-efficient scan, depth is $\Theta(\log n)$ and work is $\Theta(n)$ on EREW PRAM. Example: `[a,b,c,d]` with flags `[1,0,1,0]` produces `[a,c]`.

## Task graphs and OpenMP implementations

*No dedicated study note is currently available for this topic.*

### AAPP-20-001

Given an algorithm with the following structure: And the following values of work: W(Task1) = 2, W(Task2) = 1, W(Task3) = 3, W(Task4) = 2, W(Task5) = 1, W(Task6) = 2, W(Task7) = 5, W(Task8) = 1. Compute the Work and the Makespan of the algorithm. What is the minimum number of threads required to guarantee the maximum parallelism? (1) Provide a pseudocode implementation using OpenMP (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=4|2023-01-17-2nd · Exercise 3A · p. 4]]

![[2023-01-17-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2023-01-17-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Total work is $W=17$. The critical path is $1\to3\to4\to6\to8$, of length $2+3+2+2+1=10$, so the unlimited-processor makespan/span is $D=10$ and average parallelism is $W/D=1.7$.
>
> **Three threads** are needed to attain this span with indivisible nonpreemptive tasks. A schedule is: T1 on 0–2; T2 on 2–3, T3 on 2–5, T7 on 2–7; T4 on 5–7 and T5 on 5–6; T6 on 7–9; T8 on 9–10. Two threads cannot preserve the tight critical path while fitting both T7 and the required T2/T5 work into their available slots. Thus $\lceil W/D\rceil=2$ is only a lower bound on the required thread count.
>
> ```c
> int token[9]; // dependence tokens; values are irrelevant
> #pragma omp parallel shared(token)
> {
>   #pragma omp single
>   {
>     #pragma omp taskgroup
>     {
>       #pragma omp task depend(out: token[1])
>       { Task1(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[2])
>       { Task2(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[3])
>       { Task3(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[7])
>       { Task7(); }
>       #pragma omp task depend(in: token[2], token[3]) depend(out: token[4])
>       { Task4(); }
>       #pragma omp task depend(in: token[3]) depend(out: token[5])
>       { Task5(); }
>       #pragma omp task depend(in: token[4], token[5]) depend(out: token[6])
>       { Task6(); }
>       #pragma omp task depend(in: token[6], token[7]) depend(out: token[8])
>       { Task8(); }
>     }
>   }
> }
> ```
>
> A single generator creates sibling tasks in topological order. Each `depend` represents an actual edge; the token storage remains alive through the taskgroup. Tasks may run on any team thread. The taskgroup waits for the whole graph, without a global barrier between unrelated levels. Real task bodies must also obey the depicted data dependencies.

### AAPP-20-002

Please describe what is meant by task parallelism (Parallel Task Graph) and how could be implemented in OpenMP?(2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=4|2023-09-11-2nd · Exercise 3A · p. 4]]

^aapp-20-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Task parallelism represents a computation as a DAG: nodes are work units and edges are required predecessor relationships. Independent ready nodes may run concurrently. In OpenMP create a team, use a `single` region to generate tasks, and describe data dependencies with `depend(in/out/inout: ...)`. Use a `taskgroup` to await the group and descendants, or `taskwait` for the appropriate direct children. Keep dependent storage alive and generate sibling tasks in a suitable order; tasks are work units, not newly created operating-system threads.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-20-003

Consider the following task graph: Calculate work and parallelism. Is it a good idea to use 3 threads? (1) Write a corresponding OpenMP implementation. (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=4|2023-12-21-2nd · Exercise 3B · p. 4]]

![[2023-12-21-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2023-12-21-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> $W=1000$. A critical path is $1\to2\to5\to6\to10$ (also via T3), giving $D=700$ and $W/D=10/7\approx1.43$. Three threads give no ideal makespan improvement over two: with two, run T1 0–100; T2 and T3 100–200; T5 200–300 in one thread, while the other runs T4 200–250 and T7 250–300; then T6 300–600 while the other runs T8/T9 300–400; finally T10 600–700. Thus two suffice for the span; overhead can make a third less attractive.
>
> ```c
> int token[11]; // dependence tokens; values are irrelevant
> #pragma omp parallel shared(token)
> {
>   #pragma omp single
>   {
>     #pragma omp taskgroup
>     {
>       #pragma omp task depend(out: token[1])
>       { Task1(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[2])
>       { Task2(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[3])
>       { Task3(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[4])
>       { Task4(); }
>       #pragma omp task depend(in: token[2], token[3]) depend(out: token[5])
>       { Task5(); }
>       #pragma omp task depend(in: token[4]) depend(out: token[7])
>       { Task7(); }
>       #pragma omp task depend(in: token[5]) depend(out: token[6])
>       { Task6(); }
>       #pragma omp task depend(in: token[7]) depend(out: token[8])
>       { Task8(); }
>       #pragma omp task depend(in: token[7]) depend(out: token[9])
>       { Task9(); }
>       #pragma omp task depend(in: token[6], token[8], token[9]) depend(out: token[10])
>       { Task10(); }
>     }
>   }
> }
> ```
>
> A single generator creates sibling tasks in topological order. Each `depend` represents an actual edge; the token storage remains alive through the taskgroup. Tasks may run on any team thread. The taskgroup waits for the whole graph, without a global barrier between unrelated levels. Real task bodies must also obey the depicted data dependencies.

### AAPP-20-004

Is it better to implement the program with 3 or 4 threads? (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=4|2024-07-24-2nd · Exercise 3A · p. 4]]

![[2024-07-24-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2024-07-24-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use **four threads** to minimize ideal execution time. $W=1550$ and the critical path $1\to3\to5\to7\to9$ has span $D=600$. Four threads run T2,T3,T4,T8 concurrently after T1, allowing T5 on 300–350, T7 on 350–550 and T9 on 550–600. Three threads cannot simultaneously meet the deadlines of the T8 branch and all three inputs of T5; their optimal nonpreemptive makespan is 750. The average parallelism $1550/600\approx2.58$ does not imply that three threads attain the span. This comparison ignores real thread-management overhead.

### AAPP-20-005

Write a corresponding OpenMP implementation. (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=4|2024-07-24-2nd · Exercise 3B · p. 4]]

> [!example]- Shared graph or diagram
> ![[2024-07-24-2nd-p4.png|800]]

^aapp-20-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> ```c
> int token[10]; // dependence tokens; values are irrelevant
> #pragma omp parallel shared(token)
> {
>   #pragma omp single
>   {
>     #pragma omp taskgroup
>     {
>       #pragma omp task depend(out: token[1])
>       { Task1(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[2])
>       { Task2(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[3])
>       { Task3(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[4])
>       { Task4(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[8])
>       { Task8(); }
>       #pragma omp task depend(in: token[2], token[3], token[4]) depend(out: token[5])
>       { Task5(); }
>       #pragma omp task depend(in: token[5]) depend(out: token[6])
>       { Task6(); }
>       #pragma omp task depend(in: token[5]) depend(out: token[7])
>       { Task7(); }
>       #pragma omp task depend(in: token[6], token[7], token[8]) depend(out: token[9])
>       { Task9(); }
>     }
>   }
> }
> ```
>
> A single generator creates sibling tasks in topological order. Each `depend` represents an actual edge; the token storage remains alive through the taskgroup. Tasks may run on any team thread. The taskgroup waits for the whole graph, without a global barrier between unrelated levels. Real task bodies must also obey the depicted data dependencies.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-20-006

If you could optimize one task bringing its work to 0 (maintaining the graph structure), which one would yield the best improvement in terms of parallel execution time? (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=4|2024-07-24-2nd · Exercise 3C · p. 4]]

> [!example]- Shared graph or diagram
> ![[2024-07-24-2nd-p4.png|800]]

^aapp-20-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> With enough threads, set **T3** to zero. It reduces the T5 input bottleneck from 250 to 200: the new span is $50+200+50+200+50=550$. Setting T7 to zero also gives span 550, because the T8 branch then becomes critical ($50+450+50$). Setting T1, T5 or T9 to zero gives 550 as well. Thus **T1, T3, T5, T7 and T9 tie**, each reducing span by 50; no single task eliminates both competing branches enough to do better. This is a span comparison; a fixed-thread optimum may have additional resource constraints.

### AAPP-20-007

Describe the method to qualitatively evaluate a parallel algorithm through its data flow graph. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=4|2024-09-05-2nd · Exercise 3A · p. 4]]

^aapp-20-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Assign each node its work/cost and draw every dependence edge. Total work is $W=\sum_v w_v$; span $D$ is the maximum weighted source-to-sink path, computed by $F(v)=w_v+\max_{u\to v}F(u)$. Average parallelism is $W/D$, and $T_p\ge\max(W/p,D)$. Inspect critical paths, widths, load balance, granularity and communication. These bounds do not by themselves give an attainable finite-thread schedule: precedence and indivisible tasks can require additional idle time.

### AAPP-20-008

Calculate Span and Parallelism. If Tasks 0, 2 and 10 represent the thread management overhead, what is the maximum theoretical speedup over a sequential implementation? (1)

*Shared exercise context:* Consider the task graph on the source page.

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=3|2025-01-24-2nd · Exercise 3B · p. 3]]

![[2025-01-24-2nd-p3.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-01-24-2nd.pdf#page=3|PDF page 3]].*

^aapp-20-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Including all tasks, $W=630$ and $D=270$, from $0\to3\to7\to9\to10$. Hence graph parallelism is $630/270=7/3\approx2.33$. If T0,T2,T10 are pure parallel-management overhead, a sequential implementation does useful work $W_{\rm useful}=630-30=600$. Its maximum theoretical speedup over this parallel graph is therefore $600/270=20/9\approx2.22$, not $630/270$. Keep the overhead on the parallel critical path; it disappears only from the sequential baseline.

### AAPP-20-009

Write a corresponding OpenMP implementation. (2)

*Shared exercise context:* Consider the task graph on the source page.

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=3|2025-01-24-2nd · Exercise 3C · p. 3]]

> [!example]- Shared graph or diagram
> ![[2025-01-24-2nd-p3.png|800]]

^aapp-20-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> ```c
> int token[11]; // dependence tokens; values are irrelevant
> #pragma omp parallel shared(token)
> {
>   #pragma omp single
>   {
>     #pragma omp taskgroup
>     {
>       #pragma omp task depend(out: token[0])
>       { Task0(); }
>       #pragma omp task depend(in: token[0]) depend(out: token[1])
>       { Task1(); }
>       #pragma omp task depend(in: token[0]) depend(out: token[2])
>       { Task2(); }
>       #pragma omp task depend(in: token[0]) depend(out: token[3])
>       { Task3(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[4])
>       { Task4(); }
>       #pragma omp task depend(in: token[2]) depend(out: token[5])
>       { Task5(); }
>       #pragma omp task depend(in: token[2]) depend(out: token[6])
>       { Task6(); }
>       #pragma omp task depend(in: token[3]) depend(out: token[7])
>       { Task7(); }
>       #pragma omp task depend(in: token[4]) depend(out: token[8])
>       { Task8(); }
>       #pragma omp task depend(in: token[7]) depend(out: token[9])
>       { Task9(); }
>       #pragma omp task depend(in: token[5], token[6], token[8], token[9]) depend(out: token[10])
>       { Task10(); }
>     }
>   }
> }
> ```
>
> A single generator creates sibling tasks in topological order. Each `depend` represents an actual edge; the token storage remains alive through the taskgroup. Tasks may run on any team thread. The taskgroup waits for the whole graph, without a global barrier between unrelated levels. Real task bodies must also obey the depicted data dependencies.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-20-010

Indicate the critical path in the figure, and calculate the Parallelism. (1)

*Shared exercise context:* Consider the task graph on the source page. All tasks contain the same amount of work.

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=3|2025-07-04-2nd · Exercise 3B · p. 3]]

![[2025-07-04-2nd-p3.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-07-04-2nd.pdf#page=3|PDF page 3]].*

^aapp-20-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Let each task cost one unit. There are seven tasks, so $W=7$. The longest path is $1\to3\to6\to5\to7$, with span $D=5$ and parallelism $7/5=1.4$. The edge $6\to5$ is essential: treating T5 as dependent only on T2 would underestimate the span. For equal cost $c$, work and span become $7c$ and $5c$, leaving the ratio unchanged.

### AAPP-20-011

Write a corresponding OpenMP implementation, explaining your choice of work-sharing construct. (2)

*Shared exercise context:* Consider the task graph on the source page. All tasks contain the same amount of work.

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=3|2025-07-04-2nd · Exercise 3C · p. 3]]

> [!example]- Shared graph or diagram
> ![[2025-07-04-2nd-p3.png|800]]

^aapp-20-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> ```c
> int token[8]; // dependence tokens; values are irrelevant
> #pragma omp parallel shared(token)
> {
>   #pragma omp single
>   {
>     #pragma omp taskgroup
>     {
>       #pragma omp task depend(out: token[1])
>       { Task1(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[2])
>       { Task2(); }
>       #pragma omp task depend(in: token[1]) depend(out: token[3])
>       { Task3(); }
>       #pragma omp task depend(in: token[2]) depend(out: token[4])
>       { Task4(); }
>       #pragma omp task depend(in: token[3]) depend(out: token[6])
>       { Task6(); }
>       #pragma omp task depend(in: token[2], token[6]) depend(out: token[5])
>       { Task5(); }
>       #pragma omp task depend(in: token[4], token[5], token[6]) depend(out: token[7])
>       { Task7(); }
>     }
>   }
> }
> ```
>
> A single generator creates sibling tasks in topological order. Each `depend` represents an actual edge; the token storage remains alive through the taskgroup. Tasks may run on any team thread. The taskgroup waits for the whole graph, without a global barrier between unrelated levels. Real task bodies must also obey the depicted data dependencies.
>
> Tasks with `depend` fit this nontrivial DAG better than a single `sections` block, whose sections do not by themselves express these producer/consumer edges. In particular, T5 must await both T2 and T6.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-20-012

Given the structure of the following parallel algorithm: what is the average number of processes that are not idle? Is it better to run it with 2 or 3 threads? (1)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=4|2025-12-18-2nd · Exercise 3B · p. 4]]

![[2025-12-18-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-12-18-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> $W=750$ and $D=450$ on $1\to2\to5\to7$. Over an ideal span-attaining execution, the average number of busy processors is $W/D=5/3\approx1.67$; for an arbitrary actual schedule it is $W/T_p$ instead. **Three threads are faster** despite that average being below two. They execute T2,T3,T4 concurrently on 100–200 (T2 continues to 250), T6 on 200–300, T5 on 250–350, and T7 on 350–450. With two threads the best makespan is 500: run T2 100–250 and T3 100–200, T4 200–300, T5 250–350, T6 300–400, then T7 400–500. This compares ideal task costs and ignores thread overhead.

### AAPP-20-013

Consider the following task graph: Calculate Work and Parallelism. Imagine having the possibility to optimize a task, halving its computational cost. Which one would you choose to reduce the span? (motivate) (2)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=4|2026-9-10-2nd · Exercise 3A · p. 4]]

![[2026-9-10-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2026-9-10-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> $W=200$. There are two length-100 critical paths: $1\to2\to5\to6\to11$ and $3\to7\to6\to11$, so span is 100 and parallelism is 2. Halve **T11**, from 30 to 15. Both paths shorten to 85, but $1\to2\to5\to10\to9$ then becomes critical at 90. The new span is **90**, an improvement of 10. Halving T6 only reduces span to 95; shortening a task confined to one of the two original critical paths leaves the other at 100. Thus choosing the largest task alone (T7) would not reduce span.

## OpenMP

*No dedicated study note is currently available for this topic.*

### AAPP-21-001

OpenMP is an API dedicated to the acceleration of applications in distributed-memory environments: true or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1A · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1A · p. 2]]

^aapp-21-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> False. OpenMP primarily describes shared-memory multithreading, SIMD and device offloading; a plain host OpenMP team does not communicate across independent node address spaces. MPI is normally used between distributed-memory nodes, often with OpenMP within each node. Device offload extends the set of execution/memory environments but does not make ordinary OpenMP a replacement for general cluster message passing.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-002

Describe the functionality of the private, shared, default Data Scope Attribute Clauses

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1B · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1B · p. 2]]

^aapp-21-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `shared(x)` makes threads refer to the same original object; it does not make accesses atomic. `private(x)` supplies a separate uninitialized instance (for ordinary C scalars), so it does not copy the original value. `firstprivate(x)` additionally initializes each private copy from the original value. `default(none)` requires explicit attributes for variables without predetermined rules; `default(shared)` sets the default for eligible variables. Data scope controls which object is used; synchronization controls visibility and ordering of accesses to a shared object.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-003

How can the search of an element inside an (unbalanced) binary tree be accelerated using OpenMP?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1C · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1C · p. 2]]

^aapp-21-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an unordered tree search that must explore branches, use one outer `parallel` team, a `single` generator and recursive tasks for child subtrees. Capture child pointers safely, keep the tree immutable, use a synchronized found/result state or a valid reduction, and await all generated tasks; an optional cooperative cancellation can stop unnecessary search. Irregular subtree sizes benefit from task scheduling, but an extremely unbalanced chain has little parallelism. If this is an ordered binary-search-tree lookup, the usual search follows one comparison-selected path, so blindly searching both subtrees increases work rather than accelerating that algorithm.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-004

The maximum number of threads that can be spawned in OpenMP depends on the underlying hardware architecture: true or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1D · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1D · p. 2]]

^aapp-21-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> False if it means a hard limit equal to the physical core count. OpenMP can oversubscribe hardware with more software threads than cores; actual team sizes depend on runtime limits, settings, nesting and resources. The hardware determines how many threads can execute simultaneously and strongly affects useful performance. More threads than available compute/memory capacity can slow the program.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-005

Are there any compiler-related limitations to the use of OpenMP?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1A · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1A · p. 2]]

^aapp-21-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes. The compiler and runtime must implement the needed OpenMP version/features, and OpenMP must be enabled, for example with the compiler's appropriate option. A compiler may accept only an older feature set or lack some offload targets. Without support, ordinary OpenMP pragmas may be ignored and code can run serially, while runtime API calls still need declarations/linking. Associated loops/regions must also satisfy OpenMP syntax and canonical-form restrictions.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-006

What are Work-Sharing constructs in OpenMP? Describe their use and the conditions required for them to effectively parallelize a task.

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1B · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1B · p. 2]]

^aapp-21-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Worksharing divides work among an existing team: `for`/Fortran `do` distributes loop iterations, `sections` distributes explicitly listed blocks, and `single` selects one team thread for a block; Fortran also has `workshare`. These constructs do not themselves create a team. Participants must encounter the required constructs in a consistent order and obey nesting/loop rules. Ensure iterations/blocks are independent or use reductions/synchronization for their dependencies, and provide enough coarse work to offset overhead. Most have an implicit end barrier unless an allowed `nowait` removes it.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-007

Describe how to parallelize the search of an element inside a list of unknown length using OpenMP.

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1C · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1C · p. 2]]

^aapp-21-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A pointer-linked list of unknown length is not directly an indexed canonical `omp for`. One `single` thread can traverse links and create a task per node (or per batch), capturing the node pointer with `firstprivate`; tasks search immutable node contents and publish a result safely. Pointer chasing/task creation remains a serial producer bottleneck, so batch sufficiently expensive work. Alternatively first collect node pointers into an indexed array and parallelize that search, accounting for the preprocessing cost. A mutable list needs additional synchronization.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-008

Is it possible to express nested parallelism in OpenMP? Is it generally a good practice?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1D · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1D · p. 2]]

^aapp-21-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes: a `parallel` region can be encountered inside another, creating nested teams when enabled and permitted by the active-level settings, for example `omp_set_max_active_levels`. Inner regions may otherwise be serialized. Nested teams can be useful for genuinely hierarchical work, but often cause oversubscription and repeated team overhead. Prefer one team with tasks or a suitably collapsed/distributed loop when that expresses the decomposition efficiently.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-009

Describe the multithreading paradigm used in OpenMP and the lifespan of threads with respect to tasks.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1A · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1A · p. 2]]

^aapp-21-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> OpenMP uses fork-join: the encountering thread forms a team at a parallel region, threads execute implicit tasks, and the team synchronizes at the end. A runtime commonly keeps operating-system threads in a reusable pool, so the logical join need not destroy them. Explicit tasks are work items created within that execution; they may be deferred and run by available team threads. Creating an explicit task does not mean creating a new operating-system thread.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-010

How is variables visibility managed in OpenMP?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1B · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1B · p. 2]]

^aapp-21-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `shared(x)` makes threads refer to the same original object; it does not make accesses atomic. `private(x)` supplies a separate uninitialized instance (for ordinary C scalars), so it does not copy the original value. `firstprivate(x)` additionally initializes each private copy from the original value. `default(none)` requires explicit attributes for variables without predetermined rules; `default(shared)` sets the default for eligible variables. Data scope controls which object is used; synchronization controls visibility and ordering of accesses to a shared object.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-011

What is the “omp sections” directive used for?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1C · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1C · p. 2]]

^aapp-21-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `sections` distributes a fixed set of `section` structured blocks among the current team. Each section executes once, assigned to some team thread, and a thread may execute multiple sections. There is an implicit end barrier unless `nowait` is specified. It suits a small known set of independent operations, not an unknown recursive number of tasks. Enclose it in `parallel` or use `parallel sections` to create a team.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-012

Is it possible and/or mandatory to define barriers in OpenMP?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1D · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1D · p. 2]]

^aapp-21-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Explicit `#pragma omp barrier` is available inside a valid team context, but is not always needed. Worksharing constructs commonly already supply an implicit end barrier; `nowait` removes one where permitted. Keep a barrier when subsequent work needs all previous results; omit redundant barriers only after checking dependencies and memory visibility. All required team participants must encounter a barrier consistently, so placing it in an incompatible conditional/worksharing region can deadlock or violate the standard.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-013

What are the static and dynamic extents of the omp parallel directive?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1A · p. 2]]

^aapp-21-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> The **static/lexical extent** is the source-code structured block associated with the `parallel` directive. Its **dynamic extent** also includes routines called while executing that block, transitively. A function need not be textually inside the parallel block to execute concurrently when team threads call it. Therefore shared state and thread safety of called routines matter, not just the visible statements in the lexical block.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-014

Is it possible for the programmer to control the distribution of parallel loop iterations across threads when using an omp for directive?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1B · p. 2]]

^aapp-21-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-015

What is the functionality of the omp_set_num_threads function? Are there other ways for achieving the same result?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1C · p. 2]]

^aapp-21-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `num_threads(k)` on a parallel region, `omp_set_num_threads(k)` for subsequent relevant regions, or the `OMP_NUM_THREADS` environment variable. `omp_set_num_threads` updates the calling task's control state; it does not resize a team already executing. The actual team also depends on dynamic adjustment, active nesting limits, thread limits and available runtime resources. Query it inside the region with `omp_get_num_threads()`. Hardware affects performance and resources, but the number is not simply capped at the number of physical cores.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-016

Is it possible to perform a reduction over a single variable using OpenMP?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1D · p. 2]]

^aapp-21-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A `reduction(+:sum)` creates private partial sums initialized with the operator identity (0 for addition), then combines them with the original `sum` when the reduction completes. With `parallel for`, a team is created and loop iterations are distributed among its threads. This avoids a race on a shared accumulator and usually avoids the contention of an atomic update per iteration. Initialize the original value as intended and wait for completion before reading the result. Floating-point reassociation may change rounding; signed integer overflow must remain absent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-017

What’s the use of the omp single directive? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=4|2022-12-22-2nd · Exercise 3B · p. 4]]

^aapp-21-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `single` executes its structured block once, by one arbitrary thread of the current team. Other threads skip the block and normally wait at its implicit end barrier, unless `nowait` is specified. Use it for one-time actions such as generating tasks or initializing shared data within a parallel region. It does not necessarily choose the primary thread and does not itself create a new team.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-018

How can we control the number of threads spawned by the omp parallel pragma? (2)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=4|2022-12-22-2nd · Exercise 3C · p. 4]]

^aapp-21-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `num_threads(k)` on a parallel region, `omp_set_num_threads(k)` for subsequent relevant regions, or the `OMP_NUM_THREADS` environment variable. `omp_set_num_threads` updates the calling task's control state; it does not resize a team already executing. The actual team also depends on dynamic adjustment, active nesting limits, thread limits and available runtime resources. Query it inside the region with `omp_get_num_threads()`. Hardware affects performance and resources, but the number is not simply capped at the number of physical cores.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-019

What’s the use of the omp critical directive? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=4|2023-01-17-2nd · Exercise 3B · p. 4]]

^aapp-21-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `critical` gives mutual exclusion: at most one thread at a time executes critical regions with the same name (unnamed critical regions share a common name). It protects compound accesses to shared state, such as updating a shared container. All competing accesses must use compatible synchronization. It is not a barrier: other threads need not arrive before a thread proceeds, and excessive use can serialize a hot path.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-020

Is it possible to control the visibility of variables between different threads in OpenMP? In which ways? (2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=4|2023-02-14-2nd · Exercise 3B · p. 4]]

^aapp-21-020

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `shared(x)` makes threads refer to the same original object; it does not make accesses atomic. `private(x)` supplies a separate uninitialized instance (for ordinary C scalars), so it does not copy the original value. `firstprivate(x)` additionally initializes each private copy from the original value. `default(none)` requires explicit attributes for variables without predetermined rules; `default(shared)` sets the default for eligible variables. Data scope controls which object is used; synchronization controls visibility and ordering of accesses to a shared object.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-021

Please describe what is meant by nested parallelism and how could be implemented in OpenMP?(2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=4|2023-06-19-2nd · Exercise 3A · p. 4]]

^aapp-21-021

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes: a `parallel` region can be encountered inside another, creating nested teams when enabled and permitted by the active-level settings, for example `omp_set_max_active_levels`. Inner regions may otherwise be serialized. Nested teams can be useful for genuinely hierarchical work, but often cause oversubscription and repeated team overhead. Prefer one team with tasks or a suitably collapsed/distributed loop when that expresses the decomposition efficiently.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-022

What is the difference between static and dynamic schedule clauses of OpenMP? In which OpenMP directive is it used? (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=4|2023-06-19-2nd · Exercise 3B · p. 4]]

^aapp-21-022

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-023

Please describe the work-sharing constructs in OpenMP. (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=4|2023-07-11-2nd · Exercise 3B · p. 4]]

^aapp-21-023

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Worksharing divides work among an existing team: `for`/Fortran `do` distributes loop iterations, `sections` distributes explicitly listed blocks, and `single` selects one team thread for a block; Fortran also has `workshare`. These constructs do not themselves create a team. Participants must encounter the required constructs in a consistent order and obey nesting/loop rules. Ensure iterations/blocks are independent or use reductions/synchronization for their dependencies, and provide enough coarse work to offset overhead. Most have an implicit end barrier unless an allowed `nowait` removes it.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-024

Please describe the simd directive in OpenMP. (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=4|2023-09-11-2nd · Exercise 3B · p. 4]]

^aapp-21-024

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `#pragma omp simd` permits concurrent execution of suitable loop iterations in SIMD lanes, typically using vector instructions within a core. It does not by itself create a team of operating-system threads. The loop must obey its dependence and data-sharing requirements; reductions and appropriate SIMD clauses express supported dependencies. Combine it with `parallel for` to distribute chunks across cores and vectorize within each chunk.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-025

Describe how each thread in the following diagram behaves at runtime as it encounters points marked with 1, representing pragma omp cancel, and with 2, representing pragma omp cancellation point. (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=4|2024-01-26-2nd · Exercise 3C · p. 4]]

![[2024-01-26-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2024-01-26-2nd.pdf#page=4|PDF page 4]].*

^aapp-21-025

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Assume cancellation is enabled and all numbered directives target the same valid enclosing cancellable region. **Thread 1** reaches the earliest point 1, activates cancellation and exits the canceled region immediately; it never reaches its later point 2. **Thread 3** exits when it reaches its point 1; it also never reaches its later point 2. **Threads 2 and 4** reach their point 2 after cancellation is active, detect it and exit there, without reaching their later point 1. Each transfers control to the appropriate end of the canceled region, with the required completion synchronization. If cancellation is disabled, these directives have no cancellation effect and the threads continue normally.
>
> **Reference:** [OpenMP cancellation](https://openmp.org/spec-html/5.2/openmpse99.html).

### AAPP-21-026

Why is synchronization necessary when programming with the shared memory model? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3A · p. 4]]

^aapp-21-026

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Threads can access the same memory concurrently, so conflicting unsynchronized accesses can race and violate the program's required value/order relationships. Synchronization provides mutual exclusion, atomic updates and/or producer-to-consumer visibility. Use reductions for aggregates, locks/critical regions for compound state, atomic operations for supported individual accesses, and barriers/task dependencies for phase ordering. A `shared` declaration alone supplies none of these protections.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-027

What is the difference between static and dynamic schedule of OpenMP for loops? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3C · p. 4]]

^aapp-21-027

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-028

Please write a short pseudo-code showing how the map parallel pattern could be implemented in OpenMP. (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=2|2024-06-26-2nd · Exercise 1A · p. 2]]

^aapp-21-028

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For a pure function and separate valid arrays, each map iteration owns one output:
>
> ```c
> #pragma omp parallel for
> for (int i=0; i<n; ++i) {
>     y[i] = f(x[i]);
> }
> ```
>
> The iteration variable is private by the loop rules. Shared input reads are safe; `f` must not introduce conflicting hidden shared-state accesses. Chunking and a sufficiently large `n` help amortize startup costs.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-029

What happens when a variable is declared as firstprivate in an OpenMP pragma? (1)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=4|2024-06-26-2nd · Exercise 3B · p. 4]]
Source: [[Tema Esame 2025-09-05-2nd.pdf#page=3|2025-09-05-2nd · Exercise 3B · p. 3]]

^aapp-21-029

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `firstprivate(x)` creates a private instance initialized from the value of `x` at the specified construct encounter. Later updates to that private copy do not update the original or the other threads' copies. This differs from `private`, whose ordinary C scalar copy is uninitialized. Copies are initialized according to the construct/task rules, not freshly from the original before every loop iteration. Capture a loop-generated task's index/pointer with `firstprivate` when it must retain that encounter's value.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-030

Why is cancellation in OpenMP described as “best effort” cancellation? (1.5)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=4|2024-06-26-2nd · Exercise 3C · p. 4]]

^aapp-21-030

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Cancellation is cooperative and must be enabled. `cancel` requests cancellation of a supported enclosing construct; other executing tasks/threads notice it only at applicable cancellation points, so work between those points can continue. It is not asynchronous preemption or rollback, and already performed side effects remain. Explicit `cancellation point` directives improve responsiveness where appropriate. Code must still avoid leaving locks/resources or synchronization in an invalid state.
>
> **Reference:** [OpenMP cancellation](https://openmp.org/spec-html/5.2/openmpse99.html).

### AAPP-21-031

Describe what is the effect of the following OpenMP directive: (2)

```c
     #pragma omp for simd schedule(simd:static, 5)
```

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=4|2024-09-05-2nd · Exercise 3B · p. 4]]

^aapp-21-031

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `for simd` distributes a loop over an already existing team and allows SIMD execution within each assigned chunk. `static,5` requests static round-robin chunks; the `simd` schedule modifier adjusts interior chunk sizes to $\lceil5/w\rceil w$, where $w$ is an implementation-defined SIMD width. The first and last chunks have the specified permitted exceptions, so this does not guarantee five iterations per chunk or a particular vector instruction width. The loop still must satisfy dependence and SIMD restrictions. No new team is created by this directive alone.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-032

List similarities and differences between a single and a master region in OpenMP. (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=3|2025-02-14-2nd · Exercise 3A · p. 3]]

^aapp-21-032

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Both run a block once within a team. `single` chooses an arbitrary team thread and has an implicit end barrier unless `nowait` is used. Legacy `master` runs only on the primary thread (thread number 0) and has no implicit barrier. Thus replacing one with the other can change both thread identity and synchronization. Modern OpenMP provides `masked` for primary/selected-thread execution; the exam's `master` terminology describes the older construct.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-033

Describe how each thread in the following diagram behaves at runtime as it encounters points marked with 1, representing pragma omp cancel, and with 2, representing pragma omp cancellation point. (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=3|2025-02-14-2nd · Exercise 3C · p. 3]]

![[2025-02-14-2nd-p3.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-02-14-2nd.pdf#page=3|PDF page 3]].*

^aapp-21-033

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Assume enabled cancellation of the same valid enclosing construct. **Thread 2** and **Thread 4** first pass point 2 before any cancellation request, so they continue. **Thread 1** then reaches point 1, activates cancellation and exits the region. Threads 2 and 4 later reach their own point 1 and exit there. **Thread 3** reaches its point 2 after cancellation is active and exits there. Cancellation is not retroactive: passing an earlier cancellation point does not stop a thread from doing work before its next applicable point. With cancellation disabled, all threads continue normally.
>
> **Reference:** [OpenMP cancellation](https://openmp.org/spec-html/5.2/openmpse99.html).

### AAPP-21-034

It is always necessary to place an explicit barrier at the end of an OpenMP work sharing construct. Is this statement true or false? Explain. (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=3|2025-06-05-2nd · Exercise 3A · p. 3]]

^aapp-21-034

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Explicit `#pragma omp barrier` is available inside a valid team context, but is not always needed. Worksharing constructs commonly already supply an implicit end barrier; `nowait` removes one where permitted. Keep a barrier when subsequent work needs all previous results; omit redundant barriers only after checking dependencies and memory visibility. All required team participants must encounter a barrier consistently, so placing it in an incompatible conditional/worksharing region can deadlock or violate the standard.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-035

List the factors that determine the number of threads in an OpenMP parallel region. (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=3|2025-06-05-2nd · Exercise 3B · p. 3]]

^aapp-21-035

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `num_threads(k)` on a parallel region, `omp_set_num_threads(k)` for subsequent relevant regions, or the `OMP_NUM_THREADS` environment variable. `omp_set_num_threads` updates the calling task's control state; it does not resize a team already executing. The actual team also depends on dynamic adjustment, active nesting limits, thread limits and available runtime resources. Query it inside the region with `omp_get_num_threads()`. Hardware affects performance and resources, but the number is not simply capped at the number of physical cores.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-036

Describe the effects of the following pragma. (2)

```c
#pragma omp task depend(in: status[i])
```

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=3|2025-06-05-2nd · Exercise 3C · p. 3]]

^aapp-21-036

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> This generates an explicit task with an `in` dependence on the storage location `status[i]`. It waits for previously generated sibling tasks whose matching dependence is `out`/`inout` (or another applicable conflicting dependence type) on that location. It does not wait for the numeric value of `status[i]` to become nonzero. A matching preceding producer must be generated in the same relevant task-dependence scope; arbitrary unrelated tasks are not linked automatically. Keep the storage alive and capture `i` appropriately when the task body uses its encounter-time value.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-037

What is the difference between a static and a dynamic schedule in the OpenMP for construct? (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=3|2025-09-05-2nd · Exercise 3A · p. 3]]

^aapp-21-037

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-038

Describe in detail the effects of the following OpenMP pragma. (2)

```c
#pragma omp parallel for reduction(+:sum)
```

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=3|2025-09-05-2nd · Exercise 3C · p. 3]]

^aapp-21-038

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A `reduction(+:sum)` creates private partial sums initialized with the operator identity (0 for addition), then combines them with the original `sum` when the reduction completes. With `parallel for`, a team is created and loop iterations are distributed among its threads. This avoids a race on a shared accumulator and usually avoids the contention of an atomic update per iteration. Initialize the original value as intended and wait for completion before reading the result. Floating-point reassociation may change rounding; signed integer overflow must remain absent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-039

Provide an example of how OpenMP can hinge on both the parallelism across different CPU cores and data parallelism within each one? (1)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=4|2025-12-18-2nd · Exercise 3A · p. 4]]

^aapp-21-039

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `parallel for simd`: threads execute chunks on different cores, and SIMD lanes process elements within each core. For example, `#pragma omp parallel for simd reduction(+:sum)` followed by a loop accumulating `a[i]*a[i]`. The reduction avoids races on `sum`; the independent element operations support vectorization. Useful scaling still requires sufficient work and memory bandwidth, and the compiler determines the actual vector instructions.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-040

When should you use `#pragma omp cancel <construct>`? Why do you also need `#pragma omp cancellation point`? (2)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=4|2025-12-18-2nd · Exercise 3C · p. 4]]

^aapp-21-040

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `cancel` when remaining work in a cancellable region is no longer needed, for example after a search finds an acceptable answer. Enable cancellation (normally with `OMP_CANCELLATION=true`) and target the correct enclosing `parallel`, `for`, `sections` or `taskgroup` region. Other threads need applicable cancellation points to notice the request; explicit points can avoid long delays. Protect publication of the found result separately. Cancellation is cooperative and does not undo work already performed.
>
> **Reference:** [OpenMP cancellation](https://openmp.org/spec-html/5.2/openmpse99.html).

### AAPP-21-041

When should you use the OpenMP task construct? Is it possible to replace this construct with the section construct? (If you say no, provide an example as justification) (1)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=4|2026-1-22-2nd · Exercise 3A · p. 4]]

^aapp-21-041

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Tasks suit dynamically generated, irregular or recursive work, such as recursively exploring a tree whose shape is unknown. Existing team threads schedule ready tasks. `sections` lists a fixed set of blocks in source and is useful for a few known operations. A fixed `sections` block is not a direct replacement for an arbitrary recursive task graph. It is possible to parallelize a few recursion levels with additional parallel sections, but this changes team creation/nesting and is often much less efficient than tasks in one team.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-042

What is the tradeoff between using static and dynamic scheduling policies in a #pragma omp for worksharing construct? (1)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=4|2026-1-22-2nd · Exercise 3B · p. 4]]

^aapp-21-042

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-043

What is the parallelization issue within the following code fragment that aims to parallelize the pi computation using a Monte Carlo approach? (2)

```c
float pi = 0;
#pragma omp parallel default(shared) {
 unsigned int seed = 0;
#pragma omp for firstprivate(seed) reduction(+:pi) {
for(int i = 0; i < 100; ++i) {
    const float x = (rand_r(&seed)) / (float) RAND_MAX;
    const float y = (rand_r(&seed)) / (float) RAND_MAX;
    if (x*x + y*y) pi += 1;
}}
pi = 4 * pi / 100;
```

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=4|2026-1-22-2nd · Exercise 3C · p. 4]]

^aapp-21-043

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> There are several defects. The printed pragma/braces must first be formatted as valid OpenMP/C. `seed` is already private because it is declared inside the parallel block; putting it in `firstprivate` on the binding worksharing loop violates the scoping restriction. Giving every worker the same initial seed also repeats/correlates random streams. Finally, `if (x*x+y*y)` tests nonzero rather than membership in the unit circle; use `<=1`.
>
> One corrected outline is:
>
> ```c
> int hits = 0;
> #pragma omp parallel reduction(+:hits)
> {
>     unsigned int seed = make_distinct_seed(omp_get_thread_num());
>     #pragma omp for
>     for (int i=0; i<100; ++i) {
>         float x = rand_r(&seed) / (float)RAND_MAX;
>         float y = rand_r(&seed) / (float)RAND_MAX;
>         if (x*x + y*y <= 1.0f) ++hits;
>     }
> }
> float pi = 4.0f * hits / 100.0f;
> ```
>
> `make_distinct_seed` denotes an appropriate seeding scheme; a quality stream-splitting or counter-based generator is preferable for serious Monte Carlo work. The reduction completes before estimating pi. `rand_r` is the POSIX routine used by the question, not portable ISO C.
>
> **Reference:** [OpenMP firstprivate restrictions](https://openmp.org/spec-html/5.2/openmpsu38.html).

### AAPP-21-044

If you need to parallelize a breadth-first search in a graph using OpenMP, which worksharing construct would you use? (Explain the reason) (1)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=4|2026-2-09-2nd · Exercise 3A · p. 4]]

^aapp-21-044

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Process one BFS frontier at a time using `omp for` (often dynamic/guided scheduling) over the current frontier's vertices, or tasks if per-vertex work is very irregular. Claim each newly visited vertex atomically or with suitable locking, and collect the next frontier in safe local/shared buffers. Finish the level before processing the next to preserve BFS shortest-distance semantics. A naive recursive task traversal without frontier ordering is generally a parallel search/DFS, not a correct level-synchronous BFS.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-045

What does it mean that OpenMP has a relaxed memory model? (1)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=4|2026-2-09-2nd · Exercise 3B · p. 4]]

^aapp-21-045

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> OpenMP does not promise that every unsynchronized shared-memory access participates in one globally sequential order. Threads/compiler transformations may retain temporary views, so the program must establish the required ordering and visibility using the memory-model rules and synchronization, such as barriers, locks, atomics or task dependencies. A data race is not repaired by declaring data `shared`, nor by adding an arbitrary `flush` while retaining conflicting accesses. Properly synchronized accesses have the required happens-before relationships.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-046

What is the parallelization issue within the following code fragment that aims to parallelize a simple loop that initializes an array? (Explain the reason) (2)

```c
int offset = 5;
int result[N];
#pragma omp parallel for default(shared) private(offset)
for (int i = 0; i < N; i++) {
  result[i] = i + offset;
}
```

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=4|2026-2-09-2nd · Exercise 3C · p. 4]]

^aapp-21-046

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `private(offset)` creates an uninitialized private scalar, so iterations do not reliably see the original 5. Use `firstprivate(offset)` to copy 5, or omit the clause and keep `offset` shared/read-only. For example:
>
> ```c
> #pragma omp parallel for firstprivate(offset)
> for (int i=0; i<N; ++i) result[i] = i + offset;
> ```
>
> Each iteration owns one result element, so no other synchronization is required.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-047

When is it useful to use the OpenMP sections construct instead of tasking? Provide an explanation to support your answer. (1)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=4|2026-6-11-2nd · Exercise 3B · p. 4]]

^aapp-21-047

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `sections` for a small fixed list of independent coarse operations, such as loading three independent datasets or invoking three independent processing stages once. Each block executes once and the implicit end barrier waits for the phase. It is concise and avoids describing a task graph unnecessarily. Tasks are more flexible when the number of jobs is dynamic/recursive or when dependencies and irregular load balancing matter.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-048

Based on the architecture illustrated in point A, how would you parallelize the following code snippet using OpenMP pragmas? (2)

```c
float a[N], b[N]; // initialization of a and b is omitted
float c = 0.0f;
for (int i = 0; i < N; i++) {
        c += (a[i] + b[i]) * (a[i] + b[i]) + a[i] * 3.0f;
}
```

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=4|2026-6-11-2nd · Exercise 3C · p. 4]]

![[2026-6-11-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2026-6-11-2nd.pdf#page=4|PDF page 4]].*

^aapp-21-048

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Distribute iterations over cores and vectorize within each core, while reducing the scalar:
>
> ```c
> #pragma omp parallel for simd reduction(+:c) schedule(static)
> for (int i=0; i<N; ++i) {
>     float t = a[i] + b[i];
>     c += t*t + a[i]*3.0f;
> }
> ```
>
> Each iteration only reads its own input elements, and the reduction prevents conflicting updates to `c`. The 256-bit units shown can operate on eight 32-bit floats per vector, subject to compiler code generation. Parallel reassociation can change the final floating-point rounding.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-049

A program processes a large array in two phases. In the first phase, the same independent operation is applied to every element. In the second phase, all processed values are combined into a single scalar result. How would you structure this computation in OpenMP, and what correctness or performance problems could arise from an implementation using atomic primitives? (2)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=3|2026-6-29-2nd · Exercise 2B · p. 3]]

^aapp-21-049

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Fuse the map into a `parallel for reduction` when intermediate values are not otherwise needed: `sum += f(a[i])`. Each thread accumulates locally and the runtime combines partial results, reducing memory traffic and synchronization. If keeping two phases, ensure mapped outputs are ready before the reduction consumes them. An `atomic update` on a shared sum prevents lost updates but can serialize on a cache line; atomics do not automatically protect hidden state inside `f` or provide a complete phase barrier. Floating-point reduction/atomic order can also change rounding.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-050

For all the points in this exercise, consider the following C snippet of code that prints all the elements in a tree (the order of lines in the output does not matter):

```c
typedef struct node {
 int value;
 struct node *left;
 struct node *right;
} node;

void dfs(node *root) {
 if (root == NULL)
   return;

    printf("%d\n", root->value);

    dfs(root->left);
    dfs(root->right);
}

Int main() {
  node root;
  // initialize the tree (code omitted)
  dfs(&root);
}
```

Why can't we use the OpenMP sections construct to parallelize the code? (1)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=4|2026-6-29-2nd · Exercise 3A · p. 4]]

^aapp-21-050

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A single `sections` construct contains a fixed set of source blocks and cannot by itself generate the unknown number of recursive subtree jobs. Reusing the same worksharing sections arbitrarily inside recursive tasks also violates nesting/encounter requirements. The intended solution is tasks in one team. It is possible to create nested `parallel sections` for selected forks, so “cannot” is too absolute; that alternative creates additional teams and can oversubscribe or add substantial overhead.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-051

For all the points in this exercise, consider the following C snippet of code that prints all the elements in a tree (the order of lines in the output does not matter):

```c
typedef struct node {
 int value;
 struct node *left;
 struct node *right;
} node;

void dfs(node *root) {
 if (root == NULL)
   return;

    printf("%d\n", root->value);

    dfs(root->left);
    dfs(root->right);
}

Int main() {
  node root;
  // initialize the tree (code omitted)
  dfs(&root);
}
```

Which is a suitable OpenMP worksharing construct to use for parallelizing the code? (1)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=4|2026-6-29-2nd · Exercise 3B · p. 4]]

^aapp-21-051

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use explicit **OpenMP tasks** for the child subtrees, inside one outer `parallel` region with a `single` initial call. Tasks fit the unknown, irregular recursive work and can be scheduled on idle team threads. Technically `task` is a task-generating construct, rather than an ordinary worksharing loop/sections construct. A sequential cutoff helps small subtrees.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-052

For all the points in this exercise, consider the following C snippet of code that prints all the elements in a tree (the order of lines in the output does not matter):

```c
typedef struct node {
 int value;
 struct node *left;
 struct node *right;
} node;

void dfs(node *root) {
 if (root == NULL)
   return;

    printf("%d\n", root->value);

    dfs(root->left);
    dfs(root->right);
}

Int main() {
  node root;
  // initialize the tree (code omitted)
  dfs(&root);
}
```

Describe exactly which OpenMP pragma you would use to make the code parallel. You can either decorate the code or write here what pragma you use and where to put them (2)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=4|2026-6-29-2nd · Exercise 3C · p. 4]]

^aapp-21-052

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Create one team, let one thread initiate traversal, and spawn child work as tasks:
>
> ```c
> void dfs(node *root) {
>     if (!root) return;
>     printf("%d\n", root->value);
>     #pragma omp task firstprivate(root)
>     { dfs(root->left); }
>     #pragma omp task firstprivate(root)
>     { dfs(root->right); }
>     #pragma omp taskwait
> }
>
> int main(void) {
>     node root; /* initialize complete tree */
>     #pragma omp parallel
>     {
>         #pragma omp single
>         {
>             #pragma omp taskgroup
>             { dfs(&root); }
>         }
>     }
> }
> ```
>
> The tree must remain alive and immutable; child tasks retain their pointer value. Recursive `taskwait` and the outer taskgroup ensure completion. Output line order is arbitrary as permitted; if the I/O implementation cannot emit each record safely, guard `printf` with a named critical region. Fix the source's `Int` typo to `int` and avoid tasks below a useful size threshold.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-053

A program has three independent, known-at-compile-time stages, followed by a recursive computation that creates an unknown number of irregular subproblems. For each phase, choose between OpenMP sections and tasks, and justify the choice in terms of scheduling, load balancing, and synchronization. Mention the OpenMP construct needed to ensure that all generated work is complete before the program continues. (2)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=3|2026-9-10-2nd · Exercise 2B · p. 3]]

^aapp-21-053

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For the three fixed independent operations, use `sections` inside a team: each listed section runs once, and its default end barrier completes that phase. For recursive irregular subproblems, use tasks generated by one initial call; ready tasks can be balanced across the existing team as the graph grows. Enclose the recursive generation in a **taskgroup** to wait for the whole generated group including descendants. `taskwait` waits for the relevant direct child tasks, so it covers an entire recursive tree only when the recursive structure itself supplies the required waits.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-054

Within a parallel OpenMP section, there is only a plain for loop. What would happen if we didn’t use the OpenMP for construct? (1)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=4|2026-9-10-2nd · Exercise 3B · p. 4]]

^aapp-21-054

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> If “section” means the body of a `parallel` region, a plain `for` is executed independently by every thread: the work is duplicated, and shared writes can race. `omp for` distributes the iterations once among the team. If the wording literally means one `omp section` block, that block is assigned to one thread, so its ordinary loop stays serial; an `omp for` cannot simply be closely nested there. In either interpretation, ordinary C loop syntax does not automatically share the work.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-21-055

State the pros and cons of dynamic and static schedules in OpenMP when applied to the for worksharing construct. (1)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=4|2026-9-10-2nd · Exercise 3C · p. 4]]

^aapp-21-055

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the `schedule` clause on `omp for` (or `parallel for`). `static` assigns chunks in advance, with low runtime overhead and predictable ownership/locality; it suits uniform iteration costs. With an explicit chunk size, chunks are assigned round-robin. `dynamic` hands out chunks as workers finish, improving balance for irregular work but adding coordination overhead and potentially poorer locality. Larger chunks reduce scheduling cost but may worsen balance; `guided` decreases chunk sizes over time. Scheduling does not make dependent iterations independent.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

## Pthreads and shared-memory synchronization

*No dedicated study note is currently available for this topic.*

### AAPP-22-001

How can a thread communicate the result of its computation after completing its routine?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=5|2022-02-11-2nd-a · Exercise 4A · p. 5]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=5|2022-02-11-2nd-b · Exercise 4A · p. 5]]

^aapp-22-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A joinable worker returns a `void *` from its start routine or calls `pthread_exit(value)`. Another thread obtains it through `pthread_join(thread, &result)`. The pointed-to result must outlive the worker: allocate it on the heap or use caller-owned storage, never return a pointer into the terminated worker's stack. A worker can also write caller-provided shared output, with a join or other synchronization establishing completion. Detached threads cannot be joined, so shared output needs another completion/lifetime protocol.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-002

Can PThread be used to implement a fixed-depth parallel pipeline? How should the pipeline stages synchronize their execution?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=5|2022-02-11-2nd-a · Exercise 4B · p. 5]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=5|2022-02-11-2nd-b · Exercise 4B · p. 5]]

^aapp-22-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes. Assign one or more worker threads to each fixed stage and connect consecutive stages with bounded queues. Protect each queue with a mutex; use condition variables to wait while empty/full, checking predicates in `while` loops. A producer signals available data and a consumer signals free capacity. Propagate an end-of-stream marker or explicit completion state so stages terminate safely. Different items overlap across stages, but each item retains its required stage order; the slowest stage limits throughput.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-003

Does PThread use an explicit or implicit synchronization model? Describe common approaches to manage the access to critical sections.

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=5|2022-06-09-2nd-a · Exercise 4A · p. 5]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=5|2022-06-09-2nd-b · Exercise 4A · p. 5]]

^aapp-22-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pthreads synchronization is explicit: the programmer selects where mutex locks/unlocks, condition waits/signals, barriers and joins are needed. Protect a critical section with the same mutex for all conflicting accesses, or use a read-write lock for suitable read-heavy state. Atomics can serve supported individual operations. Creating threads does not automatically synchronize shared state, and `volatile` is not a replacement for a synchronization protocol.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-004

What are the possible approaches for managing the execution flow of different threads using PThreads?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=5|2022-06-09-2nd-a · Exercise 4B · p. 5]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=5|2022-06-09-2nd-b · Exercise 4B · p. 5]]

^aapp-22-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use `pthread_create` to start workers, `pthread_join` to await joinable completion, barriers for phase rendezvous, mutexes/read-write locks for protected state, and condition variables for predicate-based waiting such as queues. Thread attributes control properties such as detachment. A fixed pool with a synchronized task queue separates work scheduling from thread creation. Choose the construct according to the required relationship; mutual exclusion, completion and a rendezvous are different requirements.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-005

When a new thread is spawned and assigned a routine, is it possible to automatically pass some arguments to that routine?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=5|2022-06-30-2nd-a · Exercise 4A · p. 5]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=5|2022-06-30-2nd-b · Exercise 4A · p. 5]]

^aapp-22-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `pthread_create` passes exactly the supplied `void *arg` to a start routine with type `void *routine(void *)`. Package multiple arguments in a struct and pass its address, then cast inside the routine. The programmer explicitly supplies this argument; arbitrary local variables are not automatically captured. The struct must remain alive until consumed, and use a distinct per-thread struct or safe immutable storage rather than a shared changing loop variable.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-006

What is the difference between joinable and detached threads?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=5|2022-06-30-2nd-a · Exercise 4B · p. 5]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=5|2022-06-30-2nd-b · Exercise 4B · p. 5]]

^aapp-22-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A joinable thread retains the information/resources needed for `pthread_join`, which waits for its termination and can retrieve its return value. A detached thread releases termination resources automatically and cannot be joined. Detachment does not prevent ordinary synchronization: detached threads may still use mutexes, condition variables, barriers or shared completion flags with proper synchronization. Arrange data lifetime and completion explicitly; “detached” does not mean independent of the process lifetime.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-007

What is the use of condition variables in PThreads?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=5|2022-09-07-2nd-b · Exercise 4A · p. 5]]

^aapp-22-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A condition variable lets threads sleep until a predicate over shared state may have changed. Protect that predicate with a mutex and check it in a loop:
>
> ```c
> pthread_mutex_lock(&m);
> while (!ready) pthread_cond_wait(&cv, &m);
> /* predicate is true; use/update protected state */
> pthread_mutex_unlock(&m);
> ```
>
> `pthread_cond_wait` atomically releases the mutex while blocking and reacquires it before return. A producer changes the predicate under the mutex and calls `pthread_cond_signal` or `pthread_cond_broadcast`. Recheck because wakeups can be spurious or another consumer can use the resource first. Notifications are not a queue of saved events; the predicate is the source of truth.
>
> **Reference:** [POSIX condition wait](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3p.html).

### AAPP-22-008

Is it possible to share work over a fixed size thread pool that is spawned once at the beginning of the program execution? What kind of parallel pattern can be implemented in this way?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=5|2022-09-07-2nd-b · Exercise 4B · p. 5]]

^aapp-22-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes. Create a fixed worker pool once, give it a synchronized queue of task descriptors, and have workers repeatedly remove and execute tasks. This implements **workpile** and can also implement map or task-parallel patterns. Use mutexes/condition variables for queue access and sleeping, and choose a task granularity that amortizes queue overhead. For dynamically generated work, terminate only when no queued or active task can produce more jobs, not simply when the queue happens to be empty.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-009

Using Pthreads, is it possible to synchronize the execution flow of multiple threads so that they will progress beyond a given point only after all threads have reached it? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=4|2022-12-22-2nd · Exercise 3A · p. 4]]

^aapp-22-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A POSIX barrier is initialized for a participant count. Each `pthread_barrier_wait` waits until that many threads have arrived, then the participating threads are released and the barrier can be reused for another round. One returns `PTHREAD_BARRIER_SERIAL_THREAD`, the others return 0; that special return is not an error. A join instead waits for one target thread to terminate, so it cannot provide a reusable mid-computation rendezvous among continuing workers. Use the correct participant count and ensure every participant reaches each round.
>
> **Reference:** [POSIX barrier wait](https://man7.org/linux/man-pages/man3/pthread_barrier_wait.3p.html).

### AAPP-22-010

What are PThread condition variables and what is their use? (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=5|2023-01-17-2nd · Exercise 4B · p. 5]]

^aapp-22-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A condition variable lets threads sleep until a predicate over shared state may have changed. Protect that predicate with a mutex and check it in a loop:
>
> ```c
> pthread_mutex_lock(&m);
> while (!ready) pthread_cond_wait(&cv, &m);
> /* predicate is true; use/update protected state */
> pthread_mutex_unlock(&m);
> ```
>
> `pthread_cond_wait` atomically releases the mutex while blocking and reacquires it before return. A producer changes the predicate under the mutex and calls `pthread_cond_signal` or `pthread_cond_broadcast`. Recheck because wakeups can be spurious or another consumer can use the resource first. Notifications are not a queue of saved events; the predicate is the source of truth.
>
> **Reference:** [POSIX condition wait](https://man7.org/linux/man-pages/man3/pthread_cond_wait.3p.html).

### AAPP-22-011

What is the difference between joinable and detached threads in PThread? Can detached threads’ execution be synchronized with other threads? (2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=5|2023-02-14-2nd · Exercise 4B · p. 5]]

^aapp-22-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A joinable thread retains the information/resources needed for `pthread_join`, which waits for its termination and can retrieve its return value. A detached thread releases termination resources automatically and cannot be joined. Detachment does not prevent ordinary synchronization: detached threads may still use mutexes, condition variables, barriers or shared completion flags with proper synchronization. Arrange data lifetime and completion explicitly; “detached” does not mean independent of the process lifetime.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-012

What is it meant for the procedure pthread_barrier_wait? (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=5|2023-06-19-2nd · Exercise 4B · p. 5]]

^aapp-22-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A POSIX barrier is initialized for a participant count. Each `pthread_barrier_wait` waits until that many threads have arrived, then the participating threads are released and the barrier can be reused for another round. One returns `PTHREAD_BARRIER_SERIAL_THREAD`, the others return 0; that special return is not an error. A join instead waits for one target thread to terminate, so it cannot provide a reusable mid-computation rendezvous among continuing workers. Use the correct participant count and ensure every participant reaches each round.
>
> **Reference:** [POSIX barrier wait](https://man7.org/linux/man-pages/man3/pthread_barrier_wait.3p.html).

### AAPP-22-013

Describe the main advantages of OpenMP over Pthreads. (1)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=4|2023-12-21-2nd · Exercise 3A · p. 4]]

^aapp-22-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pthreads exposes low-level thread creation, argument passing, joining and synchronization. OpenMP adds compiler/runtime support for teams, loop worksharing, tasks, data scoping and reductions, so common parallel structures require less manual scheduling and bookkeeping. Both support shared-memory programming and still require correct handling of dependencies and shared state. Pthreads gives explicit control and does not require OpenMP directives; OpenMP needs a supporting compiler/runtime and its construct rules must be respected.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-22-014

What is the difference between joinable and detached threads in Pthreads? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=4|2024-01-26-2nd · Exercise 3A · p. 4]]

^aapp-22-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A joinable thread retains the information/resources needed for `pthread_join`, which waits for its termination and can retrieve its return value. A detached thread releases termination resources automatically and cannot be joined. Detachment does not prevent ordinary synchronization: detached threads may still use mutexes, condition variables, barriers or shared completion flags with proper synchronization. Arrange data lifetime and completion explicitly; “detached” does not mean independent of the process lifetime.
>
> **Reference:** [Linux man-pages: POSIX threads overview](https://man7.org/linux/man-pages/man7/pthreads.7.html).

### AAPP-22-015

What is the difference between joining and waiting on a barrier in Pthreads? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=4|2024-01-26-2nd · Exercise 3B · p. 4]]

^aapp-22-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A POSIX barrier is initialized for a participant count. Each `pthread_barrier_wait` waits until that many threads have arrived, then the participating threads are released and the barrier can be reused for another round. One returns `PTHREAD_BARRIER_SERIAL_THREAD`, the others return 0; that special return is not an error. A join instead waits for one target thread to terminate, so it cannot provide a reusable mid-computation rendezvous among continuing workers. Use the correct participant count and ensure every participant reaches each round.
>
> **Reference:** [POSIX barrier wait](https://man7.org/linux/man-pages/man3/pthread_barrier_wait.3p.html).

### AAPP-22-016

Which Pthreads API call is needed to ensure that spawned threads can finish their execution after main() returns? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3B · p. 4]]

^aapp-22-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A normal return from the initial thread's `main` terminates the process, including other threads. To terminate only that initial thread while allowing workers to continue, call **`pthread_exit(NULL)` instead of returning from `main`**. Alternatively, join all joinable workers before returning. There is no call that makes ordinary Pthreads continue after the process itself has exited; the wording “after main returns” is therefore imprecise.
>
> **Reference:** [POSIX thread exit](https://man7.org/linux/man-pages/man3/pthread_exit.3p.html).

### AAPP-22-017

What are the main differences between Pthreads and OpenMP? (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=3|2025-01-24-2nd · Exercise 3A · p. 3]]

^aapp-22-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Pthreads exposes low-level thread creation, argument passing, joining and synchronization. OpenMP adds compiler/runtime support for teams, loop worksharing, tasks, data scoping and reductions, so common parallel structures require less manual scheduling and bookkeeping. Both support shared-memory programming and still require correct handling of dependencies and shared state. Pthreads gives explicit control and does not require OpenMP directives; OpenMP needs a supporting compiler/runtime and its construct rules must be respected.
>
> **Reference:** [OpenMP 5.2 specification](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf).

### AAPP-22-018

What happens when threads encounter a barrier in Pthreads? Is the same behavior achievable through joining? (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=3|2025-02-14-2nd · Exercise 3B · p. 3]]

^aapp-22-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A POSIX barrier is initialized for a participant count. Each `pthread_barrier_wait` waits until that many threads have arrived, then the participating threads are released and the barrier can be reused for another round. One returns `PTHREAD_BARRIER_SERIAL_THREAD`, the others return 0; that special return is not an error. A join instead waits for one target thread to terminate, so it cannot provide a reusable mid-computation rendezvous among continuing workers. Use the correct participant count and ensure every participant reaches each round.
>
> **Reference:** [POSIX barrier wait](https://man7.org/linux/man-pages/man3/pthread_barrier_wait.3p.html).

## MPI

*No dedicated study note is currently available for this topic.*

### AAPP-23-001

Is the synchronization between processes explicit or implicit?

Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=4|2022-02-11-2nd-b · Exercise 3A · p. 4]]

^aapp-23-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI normally uses **explicit synchronization** through the communication and completion operations selected by the programmer. A blocking receive waits for its matching message; a blocking send returns when its send buffer is reusable, which need not mean the receiver has completed. `MPI_Barrier` is an explicit rendezvous. Nonblocking calls initiate work and require completion with `MPI_Wait`/`MPI_Test` or their variants. Collectives require matching participation/order, but a data-moving collective is not automatically a barrier. Separate address spaces remove ordinary shared-variable races, not communication-order deadlocks.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-002

Describe the behavior of MPI_Bcast.

Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=4|2022-02-11-2nd-b · Exercise 3B · p. 4]]

^aapp-23-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Bcast(buffer,count,datatype,root,comm)` copies the root's data to every member of `comm`, including the root itself. All members call it with the same root/communicator and compatible type signatures. `buffer` is the source at the root and destination elsewhere; `count` is the number of datatype entries, `datatype` describes their layout/type, and `root` is a rank in that communicator. Allocate valid buffers before calling. Blocking return makes the local buffer usable; it does not promise that all other processes have returned, so broadcast is not a general barrier.
>
> **Reference:** [MPI broadcast](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node120.htm).

### AAPP-23-003

What are communicators? What is the advantage of defining multiple communicators in an MPI program?

Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=4|2022-02-11-2nd-b · Exercise 3C · p. 4]]

^aapp-23-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An MPI intracommunicator combines a group of processes, ranked locally, with an isolated communication context. The context prevents matching messages from unrelated communications even when ranks/tags coincide. Create communicators at runtime with operations such as `MPI_Comm_split` or duplicate one with `MPI_Comm_dup`. For example, in a 2D distributed matrix, create one communicator per process row and one per process column, then broadcast row/column blocks independently within those groups. Collective calls involve the specified group, not automatically every process in the application. Free custom communicators when finished.
>
> **Reference:** [MPI intracommunicators](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node180.htm).

### AAPP-23-004

Which memory architectures are supported by MPI? Are there any differences with the other parallel programming models presented?

Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=4|2022-06-09-2nd-b · Exercise 3A · p. 4]]

^aapp-23-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI describes cooperating **processes**, normally with separate address spaces and explicit communication. It supports distributed-memory clusters as well as shared-memory nodes; an implementation may use shared memory internally for local communication, and MPI also provides shared-memory window facilities. Pthreads and ordinary host OpenMP primarily use threads and directly shared memory within a node. MPI ranks are processes, not individually addressable threads, although each process can itself be multithreaded. Hybrid MPI+OpenMP uses message passing across nodes and threads within nodes.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-005

Describe the behavior of MPI_Gather.

Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=4|2022-06-09-2nd-b · Exercise 3B · p. 4]]

^aapp-23-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Gather(sendbuf,sendcount,sendtype,recvbuf,recvcount,recvtype,root,comm)` collects one equally sized contribution from every rank, including root, and stores them at root in rank order. `sendcount` describes the local contribution; **`recvcount` is the count per rank, not the total**. For $p$ ranks sending $k$ ordinary elements each, root needs space for $pk$ elements. Receive-buffer arguments matter only at root; send and receive type signatures must match pairwise. Use `MPI_Gatherv` for variable contribution sizes. All ranks participate; completion is not a general barrier.
>
> **Reference:** [MPI gather](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node122.htm).

### AAPP-23-006

Describe how to spread data across processes according to a user-defined distribution using MPI.

Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=4|2022-06-09-2nd-b · Exercise 3C · p. 4]]

^aapp-23-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For variable contiguous blocks from a root, compute `sendcounts[r]` and `displs[r]`, communicate each rank's local count, allocate its buffer, then call `MPI_Scatterv`. Each rank receives its own count; displacements at root are in units of the send datatype's extent. For irregular noncontiguous layouts, use suitable derived datatypes or pack buffers, and point-to-point or all-to-all variants when the required distribution is not a root scatter. Keep pairwise type signatures compatible and avoid overlapping root reads where prohibited.
>
> **Reference:** [MPI scatter and scatterv](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node124.htm).

### AAPP-23-007

Does MPI parallelize over thread or processes? What are the main differences between the two approaches?

Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=4|2022-06-30-2nd-b · Exercise 3A · p. 4]]

^aapp-23-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI describes cooperating **processes**, normally with separate address spaces and explicit communication. It supports distributed-memory clusters as well as shared-memory nodes; an implementation may use shared memory internally for local communication, and MPI also provides shared-memory window facilities. Pthreads and ordinary host OpenMP primarily use threads and directly shared memory within a node. MPI ranks are processes, not individually addressable threads, although each process can itself be multithreaded. Hybrid MPI+OpenMP uses message passing across nodes and threads within nodes.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-008

Describe the behavior of the MPI_Reduce routine.

Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=4|2022-06-30-2nd-b · Exercise 3B · p. 4]]

^aapp-23-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `MPI_Reduce(sendbuf,recvbuf,count,datatype,op,root,comm)` combines corresponding entries from all processes and returns the result at root. With `count=1` it reduces one scalar per process; with `count=k` it produces **k reduced elements**, where output position $j$ combines position $j$ across ranks. It does not reduce all positions into one scalar. The operation must meet MPI's associativity rules and be valid for the datatype; examples are `MPI_SUM` and `MPI_MAX`. All members supply compatible arguments. Use `MPI_Allreduce` when every rank needs the result; floating-point reassociation can alter rounding.
>
> **Reference:** [MPI reduce](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node130.htm).

### AAPP-23-009

Are there any restrictions on the use of communication routines in MPI, particularly related to the use of other routines?

Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=4|2022-06-30-2nd-b · Exercise 3C · p. 4]]

^aapp-23-009

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes. In the world model, initialize MPI before ordinary communication and finish requests before finalization. Match point-to-point source/tag/communicator and type signatures; allocate sufficient buffers. All members of a collective must make compatible collective calls in the same required order. Do not access active nonblocking receive buffers or modify active send buffers until completion. With threads, request/check an appropriate MPI thread-support level and obey it. These restrictions concern the protocol, not a general ban on mixing blocking/nonblocking calls or MPI with OpenMP.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-010

Describe the processes synchronization model used by MPI.

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=4|2022-09-07-2nd-b · Exercise 3A · p. 4]]

^aapp-23-010

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI normally uses **explicit synchronization** through the communication and completion operations selected by the programmer. A blocking receive waits for its matching message; a blocking send returns when its send buffer is reusable, which need not mean the receiver has completed. `MPI_Barrier` is an explicit rendezvous. Nonblocking calls initiate work and require completion with `MPI_Wait`/`MPI_Test` or their variants. Collectives require matching participation/order, but a data-moving collective is not automatically a barrier. Separate address spaces remove ordinary shared-variable races, not communication-order deadlocks.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-011

Describe the behavior of the MPI_Bcast routine.

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=4|2022-09-07-2nd-b · Exercise 3B · p. 4]]

^aapp-23-011

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Bcast(buffer,count,datatype,root,comm)` copies the root's data to every member of `comm`, including the root itself. All members call it with the same root/communicator and compatible type signatures. `buffer` is the source at the root and destination elsewhere; `count` is the number of datatype entries, `datatype` describes their layout/type, and `root` is a rank in that communicator. Allocate valid buffers before calling. Blocking return makes the local buffer usable; it does not promise that all other processes have returned, so broadcast is not a general barrier.
>
> **Reference:** [MPI broadcast](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node120.htm).

### AAPP-23-012

Describe the use of communicators in MPI and the advantages of defining multiple communicators in a program.

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=4|2022-09-07-2nd-b · Exercise 3C · p. 4]]

^aapp-23-012

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An MPI intracommunicator combines a group of processes, ranked locally, with an isolated communication context. The context prevents matching messages from unrelated communications even when ranks/tags coincide. Create communicators at runtime with operations such as `MPI_Comm_split` or duplicate one with `MPI_Comm_dup`. For example, in a 2D distributed matrix, create one communicator per process row and one per process column, then broadcast row/column blocks independently within those groups. Collective calls involve the specified group, not automatically every process in the application. Free custom communicators when finished.
>
> **Reference:** [MPI intracommunicators](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node180.htm).

### AAPP-23-013

Describe the functionality of the MPI_Gather subroutine (2)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=5|2022-12-22-2nd · Exercise 4A · p. 5]]

^aapp-23-013

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Gather(sendbuf,sendcount,sendtype,recvbuf,recvcount,recvtype,root,comm)` collects one equally sized contribution from every rank, including root, and stores them at root in rank order. `sendcount` describes the local contribution; **`recvcount` is the count per rank, not the total**. For $p$ ranks sending $k$ ordinary elements each, root needs space for $pk$ elements. Receive-buffer arguments matter only at root; send and receive type signatures must match pairwise. Use `MPI_Gatherv` for variable contribution sizes. All ranks participate; completion is not a general barrier.
>
> **Reference:** [MPI gather](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node122.htm).

### AAPP-23-014

How does MPI differ from Pthreads and OpenMP? (2)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=5|2022-12-22-2nd · Exercise 4B · p. 5]]

^aapp-23-014

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI describes cooperating **processes**, normally with separate address spaces and explicit communication. It supports distributed-memory clusters as well as shared-memory nodes; an implementation may use shared memory internally for local communication, and MPI also provides shared-memory window facilities. Pthreads and ordinary host OpenMP primarily use threads and directly shared memory within a node. MPI ranks are processes, not individually addressable threads, although each process can itself be multithreaded. Hybrid MPI+OpenMP uses message passing across nodes and threads within nodes.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-015

What are Communicators in MPI? Describe if it is possible to define custom communicators in a program at runtime, and why doing so would be useful. (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=5|2023-01-17-2nd · Exercise 4A · p. 5]]

^aapp-23-015

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An MPI intracommunicator combines a group of processes, ranked locally, with an isolated communication context. The context prevents matching messages from unrelated communications even when ranks/tags coincide. Create communicators at runtime with operations such as `MPI_Comm_split` or duplicate one with `MPI_Comm_dup`. For example, in a 2D distributed matrix, create one communicator per process row and one per process column, then broadcast row/column blocks independently within those groups. Collective calls involve the specified group, not automatically every process in the application. Free custom communicators when finished.
>
> **Reference:** [MPI intracommunicators](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node180.htm).

### AAPP-23-016

Describe the functionality of the MPI_Reduce subroutine (2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=5|2023-02-14-2nd · Exercise 4A · p. 5]]

^aapp-23-016

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `MPI_Reduce(sendbuf,recvbuf,count,datatype,op,root,comm)` combines corresponding entries from all processes and returns the result at root. With `count=1` it reduces one scalar per process; with `count=k` it produces **k reduced elements**, where output position $j$ combines position $j$ across ranks. It does not reduce all positions into one scalar. The operation must meet MPI's associativity rules and be valid for the datatype; examples are `MPI_SUM` and `MPI_MAX`. All members supply compatible arguments. Use `MPI_Allreduce` when every rank needs the result; floating-point reassociation can alter rounding.
>
> **Reference:** [MPI reduce](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node130.htm).

### AAPP-23-017

Describe the procedure MPI_Send (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=5|2023-06-19-2nd · Exercise 4A · p. 5]]

^aapp-23-017

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `MPI_Send(buf,count,datatype,dest,tag,comm)` performs a standard-mode blocking send. The buffer contains `count` datatype entries, addressed to rank `dest` in `comm` with message label `tag`. It returns when the sender may safely reuse the buffer. Depending on buffering/message protocol it may wait for a matching receive, so return does not necessarily mean the receiver has completed, and the call is not guaranteed to complete independently of the receiver. Arrange matching receives without a cyclic wait.
>
> **Reference:** [MPI communication modes](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node67.htm).

### AAPP-23-018

Describe the functionality and the parameters meaning of the function MPI_Bcast (You can skip this question if you completed the second challenge) (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=5|2023-07-11-2nd · Exercise 4A · p. 5]]

^aapp-23-018

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Bcast(buffer,count,datatype,root,comm)` copies the root's data to every member of `comm`, including the root itself. All members call it with the same root/communicator and compatible type signatures. `buffer` is the source at the root and destination elsewhere; `count` is the number of datatype entries, `datatype` describes their layout/type, and `root` is a rank in that communicator. Allocate valid buffers before calling. Blocking return makes the local buffer usable; it does not promise that all other processes have returned, so broadcast is not a general barrier.
>
> **Reference:** [MPI broadcast](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node120.htm).

### AAPP-23-019

Describe the functionality and the parameters meaning of the function MPI_Gather(You can skip this question if you completed the second challenge) (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=5|2023-09-11-2nd · Exercise 4A · p. 5]]

^aapp-23-019

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Gather(sendbuf,sendcount,sendtype,recvbuf,recvcount,recvtype,root,comm)` collects one equally sized contribution from every rank, including root, and stores them at root in rank order. `sendcount` describes the local contribution; **`recvcount` is the count per rank, not the total**. For $p$ ranks sending $k$ ordinary elements each, root needs space for $pk$ elements. Receive-buffer arguments matter only at root; send and receive type signatures must match pairwise. Use `MPI_Gatherv` for variable contribution sizes. All ranks participate; completion is not a general barrier.
>
> **Reference:** [MPI gather](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node122.htm).

### AAPP-23-020

Most of the point-to-point communication functions have a parameter named “tag”. Please, state its type, explain its usage and why we might need to use the “MPI_ANY_TAG” value. (1)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=5|2023-12-21-2nd · Exercise 4A · p. 5]]

^aapp-23-020

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> In the C binding the tag is an integer message label. Matching uses the communicator/context, source rank and tag. Sends use a valid nonnegative tag (bounded by `MPI_TAG_UB`); receives/probes can use `MPI_ANY_TAG` to accept any tag and inspect `status.MPI_TAG`. Example: worker rank 3 sends array lengths with `LENGTH_TAG=10` and numeric payloads with `DATA_TAG=11`; the receiver requests the corresponding tag so a length is not confused with data. A dispatcher may probe any tag, then branch on WORK/RESULT/STOP and receive the identified source/tag.
>
> **Reference:** [MPI message envelope](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node58.htm).

### AAPP-23-021

Explain when the MPI usage overlaps with OpenMP and when OpenMP cannot replace MPI. (3)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=5|2023-12-21-2nd · Exercise 4B · p. 5]]

^aapp-23-021

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI describes cooperating **processes**, normally with separate address spaces and explicit communication. It supports distributed-memory clusters as well as shared-memory nodes; an implementation may use shared memory internally for local communication, and MPI also provides shared-memory window facilities. Pthreads and ordinary host OpenMP primarily use threads and directly shared memory within a node. MPI ranks are processes, not individually addressable threads, although each process can itself be multithreaded. Hybrid MPI+OpenMP uses message passing across nodes and threads within nodes.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-022

What are the approaches that the receiver in point-to-point communications can use to allocate a suitable receiving buffer, i.e. allocate a suitable number of elements? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=5|2024-01-26-2nd · Exercise 4A · p. 5]]

^aapp-23-022

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Two common strategies are: **(1)** know the size from the protocol (a fixed size, a safe upper bound, or an initial size/header message), allocate that capacity, then receive; **(2)** use `MPI_Probe` plus `MPI_Get_count`, allocate for the reported number of datatype entries, then receive the probed source/tag. The receive count is capacity and can exceed the actual message length; use the returned status to inspect what arrived. For multithreaded competing receives, matched probing avoids the probe/receive race.
>
> **Reference:** [MPI probe](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node79.htm).

### AAPP-23-023

Why are there multiple MPI implementations? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=5|2024-01-26-2nd · Exercise 4B · p. 5]]

^aapp-23-023

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-024

What are the main differences between collective and point-to-point functions when we focus on data exchange functions? (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=5|2024-01-26-2nd · Exercise 4C · p. 5]]

^aapp-23-024

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Point-to-point operations communicate between a sender and a matching receiver, identifying peers/tags within a communicator. Collective operations specify group-wide behavior, such as one-to-all broadcast, all-to-one gather, or reduction, and all relevant members must call compatible operations in the required order. A collective may use optimized trees/topology-aware algorithms internally. Blocking completion concerns local buffer safety and is not, in general, a full group barrier. Collectives do not use application tags to match the operation.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-025

When is it possible that at least two MPI processes are stuck waiting for each other, without the possibility of continuing their execution? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=5|2024-02-16-2nd · Exercise 4A · p. 5]]

^aapp-23-025

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes: communication dependencies can form a cycle even without shared memory. For example, ranks 0 and 1 both execute a blocking receive from the other before either sends; neither matching send will ever be posted. Likewise, both doing a standard blocking `MPI_Send` before receive can deadlock when buffering is unavailable. Fix a pairwise exchange with `MPI_Sendrecv`, a correct complementary send/receive order, or post `MPI_Irecv` and `MPI_Isend` before waiting for both. Never rely on eager buffering observed for small test messages.
>
> **Reference:** [MPI point-to-point semantics](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node68.htm).

### AAPP-23-026

When in doubt about the behavior of an MPI function, why is it important to rely on the MPI standard instead of just trying how it works with your MPI implementation? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=5|2024-02-16-2nd · Exercise 4B · p. 5]]

^aapp-23-026

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-027

What is the relationship between i) MPI functions with blocking semantics, ii) MPI functions without blocking semantics, and iii) MPI + multithreading? (2) ù

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=5|2024-02-16-2nd · Exercise 4C · p. 5]]

^aapp-23-027

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> To overlap communication with independent computation, initiate `MPI_Irecv`/`MPI_Isend`, compute without touching active communication buffers, and periodically call `MPI_Test` or finish with `MPI_Wait`. Progress/overlap depends on the implementation and how MPI is driven; initiation alone does not promise background transfer throughout arbitrary computation. Alternatively use one communication thread while other OpenMP threads compute. Call `MPI_Init_thread`, check the provided level, and keep MPI calls within that level: `FUNNELED` permits only the initializing/main thread, `SERIALIZED` permits nonconcurrent calls by threads, and `MULTIPLE` permits concurrent calls.
>
> **Reference:** [MPI nonblocking communication](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm).

### AAPP-23-028

What error will arise compiling the following code snippet? (1.5)

```c
#pragma omp parallel for private(x) reduction(+:sum) default(none)
for (i=1;i<= num_steps; i++)
{
```

x = (i-0.5)*step; sum = sum + 4.0/(1.0+x*x);

```c
}
```

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=4|2024-06-26-2nd · Exercise 3A · p. 4]]

^aapp-23-028

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> With `default(none)`, `num_steps` and `step` need explicit data-sharing attributes if they are ordinary surrounding variables. `x` is covered by `private`, `sum` by the reduction, and the associated loop index `i` is predetermined private. A corrected directive is:
>
> ```c
> #pragma omp parallel for private(x) reduction(+:sum) \
>     default(none) shared(num_steps, step)
> ```
>
> This assumes those variables are declared and initialized appropriately; constants with predetermined rules may differ. Also reconstruct the extracted body as normal valid C. The issue is OpenMP scoping, despite this entry being grouped under MPI.

### AAPP-23-029

Why should I use the MPI_Probe function? (1)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=5|2024-06-26-2nd · Exercise 4A · p. 5]]

^aapp-23-029

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a probe when the next message's size or kind is not known. For example, workers send variable-length search results; the coordinator probes a ready result, allocates exactly enough storage, and receives the same message:
>
> ```c
> MPI_Status st;
> MPI_Probe(MPI_ANY_SOURCE, RESULT_TAG, comm, &st);
> int n;
> MPI_Get_count(&st, MPI_DOUBLE, &n);
> double *buf = malloc((size_t)n * sizeof *buf);
> MPI_Recv(buf, n, MPI_DOUBLE, st.MPI_SOURCE, st.MPI_TAG,
>          comm, MPI_STATUS_IGNORE);
> ```
>
> Assume valid homogeneous double messages, representable counts, successful allocation and no competing receive that can steal the probed message. For concurrent receivers use matched probing (`MPI_Mprobe`/`MPI_Mrecv`) or serialize access. A probe inspects, not consumes, a message. Sending a size header first is an alternative, so probe is required by this particular protocol, not by every possible implementation of variable-size messaging.
>
> **Reference:** [MPI probe](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node79.htm).

### AAPP-23-030

Provide an example(s) of how the MPI tag and rank can be used in a program (1)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=5|2024-06-26-2nd · Exercise 4B · p. 5]]

^aapp-23-030

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> In the C binding the tag is an integer message label. Matching uses the communicator/context, source rank and tag. Sends use a valid nonnegative tag (bounded by `MPI_TAG_UB`); receives/probes can use `MPI_ANY_TAG` to accept any tag and inspect `status.MPI_TAG`. Example: worker rank 3 sends array lengths with `LENGTH_TAG=10` and numeric payloads with `DATA_TAG=11`; the receiver requests the corresponding tag so a length is not confused with data. A dispatcher may probe any tag, then branch on WORK/RESULT/STOP and receive the identified source/tag.
>
> **Reference:** [MPI message envelope](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node58.htm).

### AAPP-23-031

What are communicators in MPI? Why should I use more than one? (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=5|2024-06-26-2nd · Exercise 4C · p. 5]]

^aapp-23-031

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An MPI intracommunicator combines a group of processes, ranked locally, with an isolated communication context. The context prevents matching messages from unrelated communications even when ranks/tags coincide. Create communicators at runtime with operations such as `MPI_Comm_split` or duplicate one with `MPI_Comm_dup`. For example, in a 2D distributed matrix, create one communicator per process row and one per process column, then broadcast row/column blocks independently within those groups. Collective calls involve the specified group, not automatically every process in the application. Free custom communicators when finished.
>
> **Reference:** [MPI intracommunicators](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node180.htm).

### AAPP-23-032

Why should I use mpirun to execute my MPI application? (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=5|2024-07-24-2nd · Exercise 4A · p. 5]]

^aapp-23-032

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `mpirun -np p program` (or the implementation/scheduler equivalent) launches and connects the requested MPI processes, possibly on multiple nodes, establishing the runtime environment in which MPI initialization forms the job. Running an executable directly may work as a singleton in some implementations, so `mpirun` is not universally the only valid launch method; scheduler commands such as `srun` can serve that role. Ordinary direct execution does not by itself request a distributed p-process run.
>
> **Reference:** [MPI process startup](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node280.htm).

### AAPP-23-033

Explain what the MPI_Comm_split function does and give an example of its usage, without implementation details such as the function signature. (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=5|2024-07-24-2nd · Exercise 4B · p. 5]]

^aapp-23-033

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For a 2D matrix distributed over a grid of ranks, split the world communicator by process-row number, ordering members by column number. Each resulting row communicator broadcasts a matrix block only along that row, with local ranks and an independent context. Create column communicators similarly for column broadcasts. `MPI_Comm_split` collectively groups processes with the same color and orders each group by key (ties by original rank); `MPI_UNDEFINED` excludes a process. This avoids forcing unrelated rows to participate in every row operation.
>
> **Reference:** [MPI communicator constructors](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node188.htm).

### AAPP-23-034

Explain the blocking semantics in point-to-point communications and the problems it introduces in the program. (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=5|2024-07-24-2nd · Exercise 4C · p. 5]]

^aapp-23-034

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A blocking point-to-point call returns only after its local completion condition: a receive has placed its matched message in the receive buffer; a standard send has made the send buffer reusable. A send may rely on a matching receive rather than buffering, so two send-first peers can deadlock, and blocking also prevents the calling thread from doing independent work while waiting. Use a safe communication order, `MPI_Sendrecv`, or post nonblocking operations before their completion waits. A blocking call does not automatically stop all processes.
>
> **Reference:** [MPI communication modes](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node67.htm).

### AAPP-23-035

Provide an example of when it is useful to use the MPI_Barrier function. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=5|2024-09-05-2nd · Exercise 4A · p. 5]]

^aapp-23-035

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an SPMD benchmark, call `MPI_Barrier(comm)` before starting a timed phase so no process enters that phase until every group member has reached the barrier. For completion time, measure local elapsed time and reduce with maximum as appropriate. The barrier synchronizes control flow; it neither exchanges the benchmark data nor guarantees synchronized clocks or automatically completes unrelated outstanding nonblocking requests.
>
> **Reference:** [MPI barrier](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node119.htm).

### AAPP-23-036

What is the main difference between MPI and OpenMPI? (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=5|2024-09-05-2nd · Exercise 4B · p. 5]]

^aapp-23-036

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-037

Since each MPI process has a different memory address space, how is it possible to have a deadlock? Also, make an example to explain how we can solve it. (2)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=5|2024-09-05-2nd · Exercise 4C · p. 5]]

^aapp-23-037

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes: communication dependencies can form a cycle even without shared memory. For example, ranks 0 and 1 both execute a blocking receive from the other before either sends; neither matching send will ever be posted. Likewise, both doing a standard blocking `MPI_Send` before receive can deadlock when buffering is unavailable. Fix a pairwise exchange with `MPI_Sendrecv`, a correct complementary send/receive order, or post `MPI_Irecv` and `MPI_Isend` before waiting for both. Never rely on eager buffering observed for small test messages.
>
> **Reference:** [MPI point-to-point semantics](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node68.htm).

### AAPP-23-038

What is the role of the root parameter in the MPI_Gather function? How does it relate to the sending and receiving buffers? (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=4|2025-01-24-2nd · Exercise 4A · p. 4]]

^aapp-23-038

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an intracommunicator, `MPI_Gather(sendbuf,sendcount,sendtype,recvbuf,recvcount,recvtype,root,comm)` collects one equally sized contribution from every rank, including root, and stores them at root in rank order. `sendcount` describes the local contribution; **`recvcount` is the count per rank, not the total**. For $p$ ranks sending $k$ ordinary elements each, root needs space for $pk$ elements. Receive-buffer arguments matter only at root; send and receive type signatures must match pairwise. Use `MPI_Gatherv` for variable contribution sizes. All ranks participate; completion is not a general barrier.
>
> **Reference:** [MPI gather](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node122.htm).

### AAPP-23-039

When two MPI processes are running on two different computers, e.g. on two HPC nodes, is it possible that they could end up in a deadlock? (explain the answer) (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=4|2025-01-24-2nd · Exercise 4B · p. 4]]

^aapp-23-039

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Yes: communication dependencies can form a cycle even without shared memory. For example, ranks 0 and 1 both execute a blocking receive from the other before either sends; neither matching send will ever be posted. Likewise, both doing a standard blocking `MPI_Send` before receive can deadlock when buffering is unavailable. Fix a pairwise exchange with `MPI_Sendrecv`, a correct complementary send/receive order, or post `MPI_Irecv` and `MPI_Isend` before waiting for both. Never rely on eager buffering observed for small test messages.
>
> **Reference:** [MPI point-to-point semantics](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node68.htm).

### AAPP-23-040

What is an MPI communicator? How and why should I manipulate communicators? Please also provide an example where it is useful. (2)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=4|2025-01-24-2nd · Exercise 4C · p. 4]]

^aapp-23-040

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An MPI intracommunicator combines a group of processes, ranked locally, with an isolated communication context. The context prevents matching messages from unrelated communications even when ranks/tags coincide. Create communicators at runtime with operations such as `MPI_Comm_split` or duplicate one with `MPI_Comm_dup`. For example, in a 2D distributed matrix, create one communicator per process row and one per process column, then broadcast row/column blocks independently within those groups. Collective calls involve the specified group, not automatically every process in the application. Free custom communicators when finished.
>
> **Reference:** [MPI intracommunicators](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node180.htm).

### AAPP-23-041

What do I get from an MPI implementation, e.g. from OpenMPI? (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=4|2025-02-14-2nd · Exercise 4A · p. 4]]

^aapp-23-041

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-042

Make an example where non-blocking semantics does not help with solving an MPI deadlock. (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=4|2025-02-14-2nd · Exercise 4B · p. 4]]

^aapp-23-042

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Nonblocking initiation does not fix an incorrect dependency order. For example, both ranks do `MPI_Irecv(...from_other...,&r); MPI_Wait(&r,...); MPI_Isend(...to_other...,&s);`. Each wait still prevents the matching send from being posted, so they deadlock. Post all required matching receives/sends before waits, or use `MPI_Sendrecv`. Wrong peers/tags or mismatched collective order can also prevent completion regardless of whether calls are nonblocking.
>
> **Reference:** [MPI nonblocking semantics](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node75.htm).

### AAPP-23-043

How MPI_Reduce work when the send and receive data are buffers with a single element? What happens when the buffers have more than one element? Describe how the result is computed. (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=4|2025-02-14-2nd · Exercise 4C · p. 4]]

^aapp-23-043

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `MPI_Reduce(sendbuf,recvbuf,count,datatype,op,root,comm)` combines corresponding entries from all processes and returns the result at root. With `count=1` it reduces one scalar per process; with `count=k` it produces **k reduced elements**, where output position $j$ combines position $j$ across ranks. It does not reduce all positions into one scalar. The operation must meet MPI's associativity rules and be valid for the datatype; examples are `MPI_SUM` and `MPI_MAX`. All members supply compatible arguments. Use `MPI_Allreduce` when every rank needs the result; floating-point reassociation can alter rounding.
>
> **Reference:** [MPI reduce](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node130.htm).

### AAPP-23-044

Modern HPC systems feature cores in the order of millions. Why can MPi help my application to use more cores than a plain OpenMP application?(1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=4|2025-06-05-2nd · Exercise 4A · p. 4]]

^aapp-23-044

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI describes cooperating **processes**, normally with separate address spaces and explicit communication. It supports distributed-memory clusters as well as shared-memory nodes; an implementation may use shared memory internally for local communication, and MPI also provides shared-memory window facilities. Pthreads and ordinary host OpenMP primarily use threads and directly shared memory within a node. MPI ranks are processes, not individually addressable threads, although each process can itself be multithreaded. Hybrid MPI+OpenMP uses message passing across nodes and threads within nodes.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-045

Make an example where the program’s correct execution requires MPI_probe (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=4|2025-06-05-2nd · Exercise 4B · p. 4]]

^aapp-23-045

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use a probe when the next message's size or kind is not known. For example, workers send variable-length search results; the coordinator probes a ready result, allocates exactly enough storage, and receives the same message:
>
> ```c
> MPI_Status st;
> MPI_Probe(MPI_ANY_SOURCE, RESULT_TAG, comm, &st);
> int n;
> MPI_Get_count(&st, MPI_DOUBLE, &n);
> double *buf = malloc((size_t)n * sizeof *buf);
> MPI_Recv(buf, n, MPI_DOUBLE, st.MPI_SOURCE, st.MPI_TAG,
>          comm, MPI_STATUS_IGNORE);
> ```
>
> Assume valid homogeneous double messages, representable counts, successful allocation and no competing receive that can steal the probed message. For concurrent receivers use matched probing (`MPI_Mprobe`/`MPI_Mrecv`) or serialize access. A probe inspects, not consumes, a message. Sending a size header first is an alternative, so probe is required by this particular protocol, not by every possible implementation of variable-size messaging.
>
> **Reference:** [MPI probe](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node79.htm).

### AAPP-23-046

MPI functions with non-blocking semantics, e.g. MPI_Irecv, and multi-threading programming, e.g. OpenMP, can be used to solve the same problem. What is the problem and how can the two approaches be used to solve it? (2)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=4|2025-06-05-2nd · Exercise 4C · p. 4]]

^aapp-23-046

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> To overlap communication with independent computation, initiate `MPI_Irecv`/`MPI_Isend`, compute without touching active communication buffers, and periodically call `MPI_Test` or finish with `MPI_Wait`. Progress/overlap depends on the implementation and how MPI is driven; initiation alone does not promise background transfer throughout arbitrary computation. Alternatively use one communication thread while other OpenMP threads compute. Call `MPI_Init_thread`, check the provided level, and keep MPI calls within that level: `FUNNELED` permits only the initializing/main thread, `SERIALIZED` permits nonconcurrent calls by threads, and `MULTIPLE` permits concurrent calls.
>
> **Reference:** [MPI nonblocking communication](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm).

### AAPP-23-047

Which software components do I get from an MPI implementation? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=4|2025-07-04-2nd · Exercise 4A · p. 4]]

^aapp-23-047

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-048

The following is the MPI_Recv signature:

```c
      int MPI_Recv(void *buf, int count, MPI_Datatype datatype,
                   int source, int tag, MPI_Comm comm, MPI_Status *status)
```

What value should I provide to the count parameter? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=4|2025-07-04-2nd · Exercise 4B · p. 4]]

^aapp-23-048

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `count` is the maximum number of entries of `datatype` that the receiving buffer can hold, not the number of bytes unless the datatype is `MPI_BYTE`. Allocate storage covering that datatype/count layout. The actual message may contain fewer entries; a larger incompatible message causes truncation/error. Determine a sufficient capacity from the protocol or probing, and use `MPI_Get_count` on the returned status to obtain the actual number when applicable.
>
> **Reference:** [MPI receive](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node59.htm).

### AAPP-23-049

Make an example where MPI_Comm_split is useful. Do not describe what the function does. Describe a scenario where it makes sense to use it, how you use it, and the reason you use it. (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=4|2025-07-04-2nd · Exercise 4C · p. 4]]

^aapp-23-049

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For a 2D matrix distributed over a grid of ranks, split the world communicator by process-row number, ordering members by column number. Each resulting row communicator broadcasts a matrix block only along that row, with local ranks and an independent context. Create column communicators similarly for column broadcasts. `MPI_Comm_split` collectively groups processes with the same color and orders each group by key (ties by original rank); `MPI_UNDEFINED` excludes a process. This avoids forcing unrelated rows to participate in every row operation.
>
> **Reference:** [MPI communicator constructors](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node188.htm).

### AAPP-23-050

Why does MPI enable the usage of distributed architectures? (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=4|2025-09-05-2nd · Exercise 4A · p. 4]]

^aapp-23-050

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI describes cooperating **processes**, normally with separate address spaces and explicit communication. It supports distributed-memory clusters as well as shared-memory nodes; an implementation may use shared memory internally for local communication, and MPI also provides shared-memory window facilities. Pthreads and ordinary host OpenMP primarily use threads and directly shared memory within a node. MPI ranks are processes, not individually addressable threads, although each process can itself be multithreaded. Hybrid MPI+OpenMP uses message passing across nodes and threads within nodes.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-051

In which scenario does it make sense to use MPI_ANY_TAG in MPI_Probe? (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=4|2025-09-05-2nd · Exercise 4B · p. 4]]

^aapp-23-051

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> In the C binding the tag is an integer message label. Matching uses the communicator/context, source rank and tag. Sends use a valid nonnegative tag (bounded by `MPI_TAG_UB`); receives/probes can use `MPI_ANY_TAG` to accept any tag and inspect `status.MPI_TAG`. Example: worker rank 3 sends array lengths with `LENGTH_TAG=10` and numeric payloads with `DATA_TAG=11`; the receiver requests the corresponding tag so a length is not confused with data. A dispatcher may probe any tag, then branch on WORK/RESULT/STOP and receive the identified source/tag.
>
> **Reference:** [MPI message envelope](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node58.htm).

### AAPP-23-052

What is the purpose of the function MPI_Reduce? When the input buffer in each MPI process has more than one value, what is the size and content of the output buffer? (2)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=4|2025-09-05-2nd · Exercise 4C · p. 4]]

^aapp-23-052

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `MPI_Reduce(sendbuf,recvbuf,count,datatype,op,root,comm)` combines corresponding entries from all processes and returns the result at root. With `count=1` it reduces one scalar per process; with `count=k` it produces **k reduced elements**, where output position $j$ combines position $j$ across ranks. It does not reduce all positions into one scalar. The operation must meet MPI's associativity rules and be valid for the datatype; examples are `MPI_SUM` and `MPI_MAX`. All members supply compatible arguments. Use `MPI_Allreduce` when every rank needs the result; floating-point reassociation can alter rounding.
>
> **Reference:** [MPI reduce](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node130.htm).

### AAPP-23-053

Why is it important to ensure to write standard-compliant MPI code, besides checking if it works on the target testbed? (1)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=5|2025-12-18-2nd · Exercise 4A · p. 5]]

^aapp-23-053

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-054

What is an MPI communicator? Provide an example where it makes sense to create multiple communicators. (Generic or vague examples do not count) (1)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=5|2025-12-18-2nd · Exercise 4B · p. 5]]

^aapp-23-054

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> An MPI intracommunicator combines a group of processes, ranked locally, with an isolated communication context. The context prevents matching messages from unrelated communications even when ranks/tags coincide. Create communicators at runtime with operations such as `MPI_Comm_split` or duplicate one with `MPI_Comm_dup`. For example, in a 2D distributed matrix, create one communicator per process row and one per process column, then broadcast row/column blocks independently within those groups. Collective calls involve the specified group, not automatically every process in the application. Free custom communicators when finished.
>
> **Reference:** [MPI intracommunicators](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node180.htm).

### AAPP-23-055

Provide an example where MPI non-blocking functions do not solve a deadlock. When you want to overlap communication with computation, what are the alternatives that you have, including both MPI and/or OpenMP? (2)

Source: [[Tema Esame 2025-12-18-2nd.pdf#page=5|2025-12-18-2nd · Exercise 4C · p. 5]]

^aapp-23-055

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Nonblocking initiation does not fix an incorrect dependency order. For example, both ranks do `MPI_Irecv(...from_other...,&r); MPI_Wait(&r,...); MPI_Isend(...to_other...,&s);`. Each wait still prevents the matching send from being posted, so they deadlock. Post all required matching receives/sends before waits, or use `MPI_Sendrecv`. Wrong peers/tags or mismatched collective order can also prevent completion regardless of whether calls are nonblocking.
>
> To overlap communication with independent computation, initiate `MPI_Irecv`/`MPI_Isend`, compute without touching active communication buffers, and periodically call `MPI_Test` or finish with `MPI_Wait`. Progress/overlap depends on the implementation and how MPI is driven; initiation alone does not promise background transfer throughout arbitrary computation. Alternatively use one communication thread while other OpenMP threads compute. Call `MPI_Init_thread`, check the provided level, and keep MPI calls within that level: `FUNNELED` permits only the initializing/main thread, `SERIALIZED` permits nonconcurrent calls by threads, and `MULTIPLE` permits concurrent calls.
>
> **Reference:** [MPI nonblocking communication](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm).

### AAPP-23-056

Given the following signature of the MPI scatter function, why are sendcount and recvcount scalar? What if one or more processes need to compute leftovers? (1)

```c
int MPI_Scatter(const void *sendbuf, int sendcount, MPI_Datatype
sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, int
root, MPI_Comm comm)
```

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=5|2026-1-22-2nd · Exercise 4A · p. 5]]

^aapp-23-056

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Ordinary `MPI_Scatter` sends the same count from root to each rank, and each process receives one block; therefore these are scalar per-block counts. At root, `sendcount` is not the total number of elements. If $N$ is not divisible by $p$, use `MPI_Scatterv` with `counts[r]=N/p+(r<N%p)` and prefix-sum displacements, or scatter equal blocks and handle leftovers explicitly. With `Scatterv`, each rank passes its own scalar receive count matching its particular contribution.
>
> **Reference:** [MPI scatter](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node124.htm).

### AAPP-23-057

Why do you need mpirun to execute a valid MPI application? (1)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=5|2026-1-22-2nd · Exercise 4B · p. 5]]

^aapp-23-057

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `mpirun -np p program` (or the implementation/scheduler equivalent) launches and connects the requested MPI processes, possibly on multiple nodes, establishing the runtime environment in which MPI initialization forms the job. Running an executable directly may work as a singleton in some implementations, so `mpirun` is not universally the only valid launch method; scheduler commands such as `srun` can serve that role. Ordinary direct execution does not by itself request a distributed p-process run.
>
> **Reference:** [MPI process startup](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node280.htm).

### AAPP-23-058

What are the two main strategies that I have to allocate a receiving buffer from point-to-point communication? (2)

Source: [[Tema Esame 2026-1-22-2nd.pdf#page=5|2026-1-22-2nd · Exercise 4C · p. 5]]

^aapp-23-058

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Two common strategies are: **(1)** know the size from the protocol (a fixed size, a safe upper bound, or an initial size/header message), allocate that capacity, then receive; **(2)** use `MPI_Probe` plus `MPI_Get_count`, allocate for the reported number of datatype entries, then receive the probed source/tag. The receive count is capacity and can exceed the actual message length; use the returned status to inspect what arrived. For multithreaded competing receives, matched probing avoids the probe/receive race.
>
> **Reference:** [MPI probe](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node79.htm).

### AAPP-23-059

Make an example where the usage of the tag parameter matters (no point for vague or generic examples) (1)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=5|2026-2-09-2nd · Exercise 4A · p. 5]]

^aapp-23-059

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> In the C binding the tag is an integer message label. Matching uses the communicator/context, source rank and tag. Sends use a valid nonnegative tag (bounded by `MPI_TAG_UB`); receives/probes can use `MPI_ANY_TAG` to accept any tag and inspect `status.MPI_TAG`. Example: worker rank 3 sends array lengths with `LENGTH_TAG=10` and numeric payloads with `DATA_TAG=11`; the receiver requests the corresponding tag so a length is not confused with data. A dispatcher may probe any tag, then branch on WORK/RESULT/STOP and receive the identified source/tag.
>
> **Reference:** [MPI message envelope](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node58.htm).

### AAPP-23-060

What is the difference between MPI, Open MPI, and MPICH? (1)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=5|2026-2-09-2nd · Exercise 4B · p. 5]]

^aapp-23-060

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> MPI is a **standard/API specification**; **Open MPI** and **MPICH** are independent implementations of it. An implementation provides headers/modules, communication/runtime libraries, compiler wrapper commands such as `mpicc`, launch/integration tools and supporting components. It can select network transports, local shared-memory paths and collective algorithms for the target machine. Several implementations exist because hardware integration, optimization and development choices differ. Conforming programs should rely on standard guarantees, not an implementation's incidental buffering or timing.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-061

Write a meta code that shows how you can implement a scatter operation using MPI point-to-point operations on the root and non-root processes (2)

Source: [[Tema Esame 2026-2-09-2nd.pdf#page=5|2026-2-09-2nd · Exercise 4C · p. 5]]

^aapp-23-061

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For ordinary contiguous blocks of `k` elements of type `T`, root sends rank $r$ the slice beginning at `r*k`. Root copies its own slice locally, avoiding a blocking send to itself:
>
> ```text
> if rank == root:
>     copy sendbuf[root*k : (root+1)*k] into recvbuf
>     for r = 0 .. p-1:
>         if r != root:
>             MPI_Send(sendbuf + r*k, k, T, r, SCATTER_TAG, comm)
> else:
>     MPI_Recv(recvbuf, k, T, root, SCATTER_TAG, comm, status)
> ```
>
> All ranks agree on `k`, root and tag; allocate valid nonoverlapping buffers. This is a correct simple linear scatter for these types, though an MPI collective can use a faster tree algorithm. Derived datatype extents require corresponding address calculations.
>
> **Reference:** [MPI scatter](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node124.htm).

### AAPP-23-062

Assuming that echo is a serial executable that prints its command-line arguments to standard output, what would be the output of the following command? mpirun –np 4 echo hello world? (1)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=5|2026-6-11-2nd · Exercise 4A · p. 5]]

^aapp-23-062

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Four processes run `echo hello world`, so the usual output consists of **four lines `hello world`**. Their order is unspecified, and launcher/output forwarding can affect presentation. `mpirun` can launch a non-MPI executable; `echo` does not itself need to initialize MPI to print its arguments. Interpret the printed long dash as the intended command option `-np 4`.

### AAPP-23-063

If I were to look inside MPI, what would I expect to read? Can you give some examples? (1)

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=5|2026-6-11-2nd · Exercise 4B · p. 5]]

^aapp-23-063

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> If “inside MPI” means the **standard**, expect definitions of the API and semantics: message matching, communicators, datatypes, collective behavior, completion/progress, thread support and language bindings. For example, it specifies what `MPI_Send` completion means and how `MPI_Gather` orders contributions. If it means an implementation's source, expect transport protocols, buffering, shared-memory/network paths, collective algorithms and runtime integration. MPI does not prescribe one universal source implementation.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-064

Describe how you could use OpenMP to parallelize the snippet of pseudocode written below that uses non-blocking semantics to overlap communication with computation (2)

```c
MPI_Irecv_c(/* parameter recv 1 */, &request);
int request_is_complete = 0;
while(request_is_complete == 0) {
 do_work(); // this function perform the computation
  MPI_Test(&request, &request_is_complete, /* the status of recv */)
}
```

Source: [[Tema Esame 2026-6-11-2nd.pdf#page=5|2026-6-11-2nd · Exercise 4C · p. 5]]

^aapp-23-064

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Use the initializing/main thread for communication and other threads for independent computation. Request and check `MPI_THREAD_FUNNELED`; then `master` in this outer team keeps calls on the initializing thread:
>
> ```c
> /* MPI_Init_thread(..., MPI_THREAD_FUNNELED, &provided); check provided */
> #pragma omp parallel shared(request)
> {
>     #pragma omp master
>     {
>         MPI_Irecv_c(/* receive arguments */, &request);
>         MPI_Wait(&request, MPI_STATUS_IGNORE);
>     }
>     if (omp_get_thread_num() != 0) {
>         do_independent_work_for_this_thread();
>     }
> } /* completion before consumers use the receive buffer */
> ```
>
> This is an outline: divide work without duplication and do not access the receive buffer during the outstanding operation. A blocking `MPI_Recv` in the communication thread can serve the same overlap purpose. The printed `MPI_Test` is also missing a semicolon. If communication may occur on another thread, request `SERIALIZED` or `MULTIPLE` as required; arbitrary `single` is not sufficient for FUNNELED.
>
> **Reference:** [MPI and threads](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node281.htm).

### AAPP-23-065

Make an application example where the usage of the tag parameter in MPI_Recv matters. (1)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=5|2026-6-29-2nd · Exercise 4A · p. 5]]

^aapp-23-065

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> In the C binding the tag is an integer message label. Matching uses the communicator/context, source rank and tag. Sends use a valid nonnegative tag (bounded by `MPI_TAG_UB`); receives/probes can use `MPI_ANY_TAG` to accept any tag and inspect `status.MPI_TAG`. Example: worker rank 3 sends array lengths with `LENGTH_TAG=10` and numeric payloads with `DATA_TAG=11`; the receiver requests the corresponding tag so a length is not confused with data. A dispatcher may probe any tag, then branch on WORK/RESULT/STOP and receive the identified source/tag.
>
> **Reference:** [MPI message envelope](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node58.htm).

### AAPP-23-066

In an application that uses only MPI to parallelize the computation, it would make sense to use a mutex? Explain the reason. (1)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=5|2026-6-29-2nd · Exercise 4B · p. 5]]

^aapp-23-066

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For an ordinary single-threaded MPI program with private process memory and only message passing, a normal thread mutex is not needed to protect local data from other ranks: they cannot directly access it. MPI deadlocks still need a correct communication protocol; a mutex does not solve mismatched messages. This answer changes if the program uses MPI shared-memory windows, other shared resources or actual threads: then an appropriate interprocess/thread synchronization mechanism may be needed.
>
> **Reference:** [MPI standard, version 4.1](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/mpi41-report.htm).

### AAPP-23-067

How can I use OpenMP, or multithreading in general, to work synergistically with MPI? If we decide to use only MPI, what features of the standard should I use to overlap computation with communication within a single MPI Process? Please explain also the reasons (2)

Source: [[Tema Esame 2026-6-29-2nd.pdf#page=5|2026-6-29-2nd · Exercise 4C · p. 5]]

^aapp-23-067

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> To overlap communication with independent computation, initiate `MPI_Irecv`/`MPI_Isend`, compute without touching active communication buffers, and periodically call `MPI_Test` or finish with `MPI_Wait`. Progress/overlap depends on the implementation and how MPI is driven; initiation alone does not promise background transfer throughout arbitrary computation. Alternatively use one communication thread while other OpenMP threads compute. Call `MPI_Init_thread`, check the provided level, and keep MPI calls within that level: `FUNNELED` permits only the initializing/main thread, `SERIALIZED` permits nonconcurrent calls by threads, and `MULTIPLE` permits concurrent calls.
>
> **Reference:** [MPI nonblocking communication](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm).

### AAPP-23-068

Consider the following snippet of code of an MPI program with three processes:

```c
int x = 10;
if (rank == 0) {
      MPI_Recv(&x, 1, MPI_INT, 2, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Recv(&x, 1, MPI_INT, 1, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
} else if (rank == 1) { MPI_Send(&x, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
} else if (rank == 2) { MPI_Send(&x, 1, MPI_INT, 0, 2, MPI_COMM_WORLD); }
```

Is it possible that it leads to a deadlock? (Explain) (1) note: in both MPI functions, the 4th parameter is the rank, while the 5th is the tag)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=5|2026-9-10-2nd · Exercise 4A · p. 5]]

^aapp-23-068

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **No deadlock arises from this snippet**, assuming exactly these operations, valid initialization and no external interference. Rank 0 first receives rank 2's tag-2 message, for which rank 2 has already posted (or will post) its send. It then receives rank 1's tag-1 message. Rank 1 may wait while rank 0 handles rank 2, but there is no cycle: rank 2 does not wait for rank 1. Standard-send buffering is unnecessary for this order. Each receive stores 10 into `x`, so rank 0 ends with `x==10`.
>
> **Reference:** [MPI point-to-point semantics](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node68.htm).

### AAPP-23-069

Which is a scenario where it is useful to use non-blocking semantics? (1)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=5|2026-9-10-2nd · Exercise 4B · p. 5]]

^aapp-23-069

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A stencil halo exchange can overlap communication and useful computation: post nonblocking receives/sends for neighbor boundaries, compute interior cells that do not depend on incoming halos, wait for completion, then compute boundary cells. Do not modify active send buffers or read active receive buffers prematurely. This can reduce exposed communication latency when enough independent interior work exists and the implementation makes progress.
>
> **Reference:** [MPI nonblocking communication](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node71.htm).

### AAPP-23-070

What MPI_Comm_split does? Describe an application scenario where its usage is useful (2)

Source: [[Tema Esame 2026-9-10-2nd.pdf#page=5|2026-9-10-2nd · Exercise 4C · p. 5]]

^aapp-23-070

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> For a 2D matrix distributed over a grid of ranks, split the world communicator by process-row number, ordering members by column number. Each resulting row communicator broadcasts a matrix block only along that row, with local ranks and an independent context. Create column communicators similarly for column broadcasts. `MPI_Comm_split` collectively groups processes with the same color and orders each group by key (ties by original rank); `MPI_UNDEFINED` excludes a process. This avoids forcing unrelated rows to participate in every row operation.
>
> **Reference:** [MPI communicator constructors](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node188.htm).

## CUDA

*No dedicated study note is currently available for this topic.*

### AAPP-24-001

Briefly describe the hierarchy of memories of CUDA programming model

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=4|2022-02-11-2nd-a · Exercise 3A · p. 4]]

^aapp-24-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> CUDA memory spaces include **registers** private to a thread; **local memory**, logically per-thread but normally backed by device memory when registers spill; **shared memory**, cooperatively used by a block; and **global device memory**, visible across kernels/threads with the required synchronization. Constant and texture/read-only access paths provide cached read-oriented spaces. Hardware caches (L1/L2) support these accesses but differ from programmer-managed shared memory. Host memory is another domain; explicit transfers or supported unified/system-memory mechanisms make data available. Scope, lifetime and access cost differ, so local memory is not automatically fast merely because it is thread-private.
>
> **Reference:** [NVIDIA CUDA kernel/memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

### AAPP-24-002

Briefly describe which are the main issues in implementing a parallel application with CUDA.

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=4|2022-02-11-2nd-a · Exercise 3B · p. 4]]
Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=4|2022-06-09-2nd-a · Exercise 3B · p. 4]]

^aapp-24-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> CUDA requires enough independent work and a suitable kernel decomposition. Manage host/device data placement and transfers, use coalesced accesses, control register/shared-memory usage and occupancy, and avoid excessive branch divergence within warps. Synchronize only with valid scope: an ordinary block barrier does not synchronize all blocks. Small kernels, launch overhead and transfer cost can erase acceleration. Compared with a simple host OpenMP loop, CUDA often requires more explicit device-specific indexing, memory/lifetime management and tuning, although OpenMP offload also has data-transfer and device concerns. CUDA portability is tied to its supported NVIDIA platform.
>
> **Reference:** [NVIDIA CUDA kernel/memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

### AAPP-24-003

Concurrent CUDA Streams: operations within a given stream occur in order. True or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=4|2022-02-11-2nd-a · Exercise 3C · p. 4]]

^aapp-24-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **True** for ordinary operations enqueued in one stream: they execute in issue order, giving the required ordering of earlier operations before later dependent ones. Host submission can be asynchronous; operations in different streams may overlap when dependencies and hardware allow, but concurrency is not guaranteed. Default-stream synchronization behavior depends on its mode, so do not infer complete independence just from using different stream handles.
>
> **Reference:** [NVIDIA CUDA asynchronous execution](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/asynchronous-execution.html).

### AAPP-24-004

Describe what is CUDA

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=4|2022-06-09-2nd-a · Exercise 3A · p. 4]]

^aapp-24-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> CUDA is NVIDIA's parallel-computing platform and programming model. A host program launches kernels executed by many GPU threads, organized into blocks and grids, and coordinates memory movement and synchronization. CUDA provides programming-language support, runtime/driver APIs and libraries for general-purpose GPU computation. It is particularly effective for sufficiently large computations with substantial data parallelism and suitable memory behavior.
>
> **Reference:** [NVIDIA CUDA programming model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html).

### AAPP-24-005

How parallel threads are identified in a CUDA kernel?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=4|2022-06-09-2nd-a · Exercise 3C · p. 4]]

^aapp-24-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A kernel identifies its position using `threadIdx` within a block, `blockIdx` within a grid, and the dimensions `blockDim` and `gridDim`. For a 1D launch, the global element index is `i=blockIdx.x*blockDim.x+threadIdx.x`; guard with `if (i<n)` before accessing element `i`. Blocks and grids may have multiple dimensions; flatten them using the corresponding dimensions as needed. These are logical identifiers, not fixed physical core numbers.
>
> **Reference:** [NVIDIA CUDA kernel/memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

### AAPP-24-006

Briefly describe which are the main disadvanteges in implementing a parallel application with CUDA with respect to OpenMP.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=4|2022-06-30-2nd-a · Exercise 3A · p. 4]]

^aapp-24-006

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> CUDA requires enough independent work and a suitable kernel decomposition. Manage host/device data placement and transfers, use coalesced accesses, control register/shared-memory usage and occupancy, and avoid excessive branch divergence within warps. Synchronize only with valid scope: an ordinary block barrier does not synchronize all blocks. Small kernels, launch overhead and transfer cost can erase acceleration. Compared with a simple host OpenMP loop, CUDA often requires more explicit device-specific indexing, memory/lifetime management and tuning, although OpenMP offload also has data-transfer and device concerns. CUDA portability is tied to its supported NVIDIA platform.
>
> **Reference:** [NVIDIA CUDA kernel/memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

### AAPP-24-007

Briefly describe the hierarchy of memories of CUDA programming model.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=4|2022-06-30-2nd-a · Exercise 3B · p. 4]]

^aapp-24-007

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> CUDA memory spaces include **registers** private to a thread; **local memory**, logically per-thread but normally backed by device memory when registers spill; **shared memory**, cooperatively used by a block; and **global device memory**, visible across kernels/threads with the required synchronization. Constant and texture/read-only access paths provide cached read-oriented spaces. Hardware caches (L1/L2) support these accesses but differ from programmer-managed shared memory. Host memory is another domain; explicit transfers or supported unified/system-memory mechanisms make data available. Scope, lifetime and access cost differ, so local memory is not automatically fast merely because it is thread-private.
>
> **Reference:** [NVIDIA CUDA kernel/memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

### AAPP-24-008

Briefly describe how threads are grouped in CUDA.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=4|2022-06-30-2nd-a · Exercise 3C · p. 4]]

^aapp-24-008

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Threads are grouped into **blocks**, and blocks form a **grid** for a kernel launch. Threads in one block can cooperate using block-scoped shared memory and barriers. Hardware executes threads in **warps** (32 threads on NVIDIA GPUs), with divergence affecting execution efficiency. Blocks are scheduled onto streaming multiprocessors; ordinary blocks must not depend on a particular inter-block execution order, since some may execute later. A grid does not imply that all its threads are simultaneously resident.
>
> **Reference:** [NVIDIA CUDA kernel/memory model](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html).

## Halide and high-level synthesis

*No dedicated study note is currently available for this topic.*

### AAPP-25-001

Please shortly describe the main characteristic of the domain-specific language Halide. (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=5|2023-07-11-2nd · Exercise 4B · p. 5]]

^aapp-25-001

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> Halide is a domain-specific language embedded in C++ for image processing and related array pipelines. It separates the **algorithm**, which defines the values of functions over coordinates, from the **schedule**, which describes how those values are computed and stored. The same algorithm can therefore be tiled, fused, vectorized, threaded or mapped to a GPU without rewriting its mathematical definition. The compiler produces optimized code for the selected target.
>
> **Reference:** [Halide scheduling tutorial](https://halide-lang.org/docs/tutorial/lesson_05_scheduling_1.html).

### AAPP-25-002

Please briefly discuss what the term “schedule” means in the domain-specific language Halide. (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=5|2023-09-11-2nd · Exercise 4B · p. 5]]

^aapp-25-002

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> A Halide schedule controls evaluation and storage: loop order, splitting/tiling, vectorization, unrolling, parallel execution and where intermediate stages are computed/stored (`compute_at`, `compute_root`, etc.). It chooses how to realize the algorithm efficiently on a target while respecting its dependencies. Different schedules trade recomputation against memory traffic and locality; scheduling is separate from defining the function's values.
>
> **Reference:** [Halide multi-stage scheduling](https://halide-lang.org/docs/tutorial/lesson_08_scheduling_2.html).

### AAPP-25-003

Describe what is the effect of the following Halide schedule: (1)

```c
gradient.split(x, x_outer, x_inner, 4);
gradient.vectorize(x_inner);
```

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3D · p. 4]]

^aapp-25-003

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> `split(x,x_outer,x_inner,4)` replaces the x traversal by an outer loop over groups of four and an inner loop over positions in a group, conceptually `x=x_min+4*x_outer+x_inner`. `vectorize(x_inner)` evaluates that inner dimension with SIMD lanes, nominally four x positions at once. The compiler handles any non-multiple-of-four tail according to the applicable tail strategy; this does not by itself create CPU threads.
>
> **Reference:** [Halide split and vectorize](https://halide-lang.org/docs/tutorial/lesson_05_scheduling_1.html).

### AAPP-25-004

In Halide, it is good practice to schedule pipeline stages from the output to the input. Is this statement true or false? Explain. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=4|2024-09-05-2nd · Exercise 3C · p. 4]]

^aapp-25-004

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **True as a useful scheduling heuristic**, not a required execution order or a guarantee of optimality. Start from the output/consumer loops, then decide where to compute and store the producer stages relative to those loops. The consumer's tiling and traversal determine producer regions and reuse, so this order makes locality/recomputation choices clearer. Runtime evaluation still respects producer-to-consumer dependencies, and schedules may be revised iteratively.
>
> **Reference:** [Halide producer/consumer scheduling](https://halide-lang.org/docs/tutorial/lesson_08_scheduling_2.html).

### AAPP-25-005

The input to a High-Level Synthesis tool is a Register-Transfer Level description of an accelerator. Is this statement true or false? Explain. (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=3|2025-07-04-2nd · Exercise 3A · p. 3]]

^aapp-25-005

**My answer**

*Write your answer here.*

> [!note]- Feedback
> Not reviewed yet.

> [!success]- Model answer
> **False.** High-level synthesis takes a higher-level behavioral/algorithmic description, commonly a supported subset of C/C++, together with constraints/directives, and produces a hardware implementation such as RTL. RTL instead describes registers, combinational logic and clocked transfers; it is a typical output of HLS and input to subsequent logic synthesis. Thus the statement reverses the relevant abstraction levels.
>
> **Reference:** [AMD Vitis HLS introduction](https://docs.amd.com/r/en-US/ug1399-vitis-hls/Introduction).

## Source register

58 distinct exam papers contribute 602 exercise/subquestion occurrences, represented above by 552 entries after exact-wording consolidation. All supplied exam papers are included; the register lets you reconstruct a particular session.

| Exam paper | Question IDs |
|---|---|
| [[Tema Esame 2022-01-14-1st.pdf\|2022-01-14-1st]] | [[#AAPP-05-001\|AAPP-05-001]], [[#AAPP-06-001\|AAPP-06-001]], [[#AAPP-10-001\|AAPP-10-001]] |
| [[Tema Esame 2022-02-11-1st.pdf\|2022-02-11-1st]] | [[#AAPP-06-002\|AAPP-06-002]], [[#AAPP-07-001\|AAPP-07-001]], [[#AAPP-12-001\|AAPP-12-001]] |
| [[Tema Esame 2022-02-11-2nd-a.pdf\|2022-02-11-2nd-a]] | [[#AAPP-17-001\|AAPP-17-001]], [[#AAPP-17-002\|AAPP-17-002]], [[#AAPP-19-001\|AAPP-19-001]], [[#AAPP-21-001\|AAPP-21-001]], [[#AAPP-21-002\|AAPP-21-002]], [[#AAPP-21-003\|AAPP-21-003]], [[#AAPP-21-004\|AAPP-21-004]], [[#AAPP-22-001\|AAPP-22-001]], [[#AAPP-22-002\|AAPP-22-002]], [[#AAPP-24-001\|AAPP-24-001]], [[#AAPP-24-002\|AAPP-24-002]], [[#AAPP-24-003\|AAPP-24-003]] |
| [[Tema Esame 2022-02-11-2nd-b.pdf\|2022-02-11-2nd-b]] | [[#AAPP-17-001\|AAPP-17-001]], [[#AAPP-17-002\|AAPP-17-002]], [[#AAPP-19-001\|AAPP-19-001]], [[#AAPP-21-001\|AAPP-21-001]], [[#AAPP-21-002\|AAPP-21-002]], [[#AAPP-21-003\|AAPP-21-003]], [[#AAPP-21-004\|AAPP-21-004]], [[#AAPP-22-001\|AAPP-22-001]], [[#AAPP-22-002\|AAPP-22-002]], [[#AAPP-23-001\|AAPP-23-001]], [[#AAPP-23-002\|AAPP-23-002]], [[#AAPP-23-003\|AAPP-23-003]] |
| [[Tema Esame 2022-06-09-1st.pdf\|2022-06-09-1st]] | [[#AAPP-04-001\|AAPP-04-001]], [[#AAPP-08-001\|AAPP-08-001]], [[#AAPP-13-001\|AAPP-13-001]] |
| [[Tema Esame 2022-06-09-2nd-a.pdf\|2022-06-09-2nd-a]] | [[#AAPP-17-003\|AAPP-17-003]], [[#AAPP-17-004\|AAPP-17-004]], [[#AAPP-19-002\|AAPP-19-002]], [[#AAPP-21-005\|AAPP-21-005]], [[#AAPP-21-006\|AAPP-21-006]], [[#AAPP-21-007\|AAPP-21-007]], [[#AAPP-21-008\|AAPP-21-008]], [[#AAPP-22-003\|AAPP-22-003]], [[#AAPP-22-004\|AAPP-22-004]], [[#AAPP-24-002\|AAPP-24-002]], [[#AAPP-24-004\|AAPP-24-004]], [[#AAPP-24-005\|AAPP-24-005]] |
| [[Tema Esame 2022-06-09-2nd-b.pdf\|2022-06-09-2nd-b]] | [[#AAPP-17-003\|AAPP-17-003]], [[#AAPP-17-004\|AAPP-17-004]], [[#AAPP-19-002\|AAPP-19-002]], [[#AAPP-21-005\|AAPP-21-005]], [[#AAPP-21-006\|AAPP-21-006]], [[#AAPP-21-007\|AAPP-21-007]], [[#AAPP-21-008\|AAPP-21-008]], [[#AAPP-22-003\|AAPP-22-003]], [[#AAPP-22-004\|AAPP-22-004]], [[#AAPP-23-004\|AAPP-23-004]], [[#AAPP-23-005\|AAPP-23-005]], [[#AAPP-23-006\|AAPP-23-006]] |
| [[Tema Esame 2022-06-30-2nd-a.pdf\|2022-06-30-2nd-a]] | [[#AAPP-19-003\|AAPP-19-003]], [[#AAPP-19-004\|AAPP-19-004]], [[#AAPP-19-005\|AAPP-19-005]], [[#AAPP-21-009\|AAPP-21-009]], [[#AAPP-21-010\|AAPP-21-010]], [[#AAPP-21-011\|AAPP-21-011]], [[#AAPP-21-012\|AAPP-21-012]], [[#AAPP-22-005\|AAPP-22-005]], [[#AAPP-22-006\|AAPP-22-006]], [[#AAPP-24-006\|AAPP-24-006]], [[#AAPP-24-007\|AAPP-24-007]], [[#AAPP-24-008\|AAPP-24-008]] |
| [[Tema Esame 2022-06-30-2nd-b.pdf\|2022-06-30-2nd-b]] | [[#AAPP-19-003\|AAPP-19-003]], [[#AAPP-19-004\|AAPP-19-004]], [[#AAPP-19-005\|AAPP-19-005]], [[#AAPP-21-009\|AAPP-21-009]], [[#AAPP-21-010\|AAPP-21-010]], [[#AAPP-21-011\|AAPP-21-011]], [[#AAPP-21-012\|AAPP-21-012]], [[#AAPP-22-005\|AAPP-22-005]], [[#AAPP-22-006\|AAPP-22-006]], [[#AAPP-23-007\|AAPP-23-007]], [[#AAPP-23-008\|AAPP-23-008]], [[#AAPP-23-009\|AAPP-23-009]] |
| [[Tema Esame 2022-09-07-1st.pdf\|2022-09-07-1st]] | [[#AAPP-06-003\|AAPP-06-003]], [[#AAPP-10-002\|AAPP-10-002]], [[#AAPP-12-002\|AAPP-12-002]] |
| [[Tema Esame 2022-09-07-2nd-b.pdf\|2022-09-07-2nd-b]] | [[#AAPP-17-005\|AAPP-17-005]], [[#AAPP-17-006\|AAPP-17-006]], [[#AAPP-19-002\|AAPP-19-002]], [[#AAPP-21-013\|AAPP-21-013]], [[#AAPP-21-014\|AAPP-21-014]], [[#AAPP-21-015\|AAPP-21-015]], [[#AAPP-21-016\|AAPP-21-016]], [[#AAPP-22-007\|AAPP-22-007]], [[#AAPP-22-008\|AAPP-22-008]], [[#AAPP-23-010\|AAPP-23-010]], [[#AAPP-23-011\|AAPP-23-011]], [[#AAPP-23-012\|AAPP-23-012]] |
| [[Tema Esame 2022-11-08-1st.pdf\|2022-11-08-1st]] | [[#AAPP-01-001\|AAPP-01-001]], [[#AAPP-02-001\|AAPP-02-001]], [[#AAPP-02-002\|AAPP-02-002]], [[#AAPP-10-003\|AAPP-10-003]], [[#AAPP-10-004\|AAPP-10-004]], [[#AAPP-10-005\|AAPP-10-005]], [[#AAPP-12-003\|AAPP-12-003]], [[#AAPP-15-001\|AAPP-15-001]], [[#AAPP-16-001\|AAPP-16-001]] |
| [[Tema Esame 2022-12-22-2nd.pdf\|2022-12-22-2nd]] | [[#AAPP-17-007\|AAPP-17-007]], [[#AAPP-17-008\|AAPP-17-008]], [[#AAPP-18-001\|AAPP-18-001]], [[#AAPP-18-002\|AAPP-18-002]], [[#AAPP-19-006\|AAPP-19-006]], [[#AAPP-19-007\|AAPP-19-007]], [[#AAPP-19-008\|AAPP-19-008]], [[#AAPP-19-009\|AAPP-19-009]], [[#AAPP-21-017\|AAPP-21-017]], [[#AAPP-21-018\|AAPP-21-018]], [[#AAPP-22-009\|AAPP-22-009]], [[#AAPP-23-013\|AAPP-23-013]], [[#AAPP-23-014\|AAPP-23-014]] |
| [[Tema Esame 2023-01-17-1st.pdf\|2023-01-17-1st]] | [[#AAPP-01-002\|AAPP-01-002]], [[#AAPP-02-003\|AAPP-02-003]], [[#AAPP-03-001\|AAPP-03-001]], [[#AAPP-03-002\|AAPP-03-002]], [[#AAPP-06-004\|AAPP-06-004]], [[#AAPP-08-002\|AAPP-08-002]], [[#AAPP-08-003\|AAPP-08-003]], [[#AAPP-08-004\|AAPP-08-004]], [[#AAPP-15-002\|AAPP-15-002]], [[#AAPP-16-002\|AAPP-16-002]] |
| [[Tema Esame 2023-01-17-2nd.pdf\|2023-01-17-2nd]] | [[#AAPP-18-003\|AAPP-18-003]], [[#AAPP-18-004\|AAPP-18-004]], [[#AAPP-18-005\|AAPP-18-005]], [[#AAPP-19-010\|AAPP-19-010]], [[#AAPP-19-011\|AAPP-19-011]], [[#AAPP-19-012\|AAPP-19-012]], [[#AAPP-19-013\|AAPP-19-013]], [[#AAPP-20-001\|AAPP-20-001]], [[#AAPP-21-019\|AAPP-21-019]], [[#AAPP-22-010\|AAPP-22-010]], [[#AAPP-23-015\|AAPP-23-015]] |
| [[Tema Esame 2023-02-14-1st.pdf\|2023-02-14-1st]] | [[#AAPP-01-003\|AAPP-01-003]], [[#AAPP-01-004\|AAPP-01-004]], [[#AAPP-02-004\|AAPP-02-004]], [[#AAPP-02-005\|AAPP-02-005]], [[#AAPP-04-002\|AAPP-04-002]], [[#AAPP-04-003\|AAPP-04-003]], [[#AAPP-04-004\|AAPP-04-004]], [[#AAPP-11-001\|AAPP-11-001]], [[#AAPP-13-002\|AAPP-13-002]], [[#AAPP-15-003\|AAPP-15-003]] |
| [[Tema Esame 2023-02-14-2nd.pdf\|2023-02-14-2nd]] | [[#AAPP-18-006\|AAPP-18-006]], [[#AAPP-18-007\|AAPP-18-007]], [[#AAPP-18-008\|AAPP-18-008]], [[#AAPP-19-008\|AAPP-19-008]], [[#AAPP-19-014\|AAPP-19-014]], [[#AAPP-19-015\|AAPP-19-015]], [[#AAPP-19-016\|AAPP-19-016]], [[#AAPP-19-017\|AAPP-19-017]], [[#AAPP-21-020\|AAPP-21-020]], [[#AAPP-22-011\|AAPP-22-011]], [[#AAPP-23-016\|AAPP-23-016]] |
| [[Tema Esame 2023-06-19-1st.pdf\|2023-06-19-1st]] | [[#AAPP-01-005\|AAPP-01-005]], [[#AAPP-01-006\|AAPP-01-006]], [[#AAPP-02-006\|AAPP-02-006]], [[#AAPP-02-007\|AAPP-02-007]], [[#AAPP-04-005\|AAPP-04-005]], [[#AAPP-04-006\|AAPP-04-006]], [[#AAPP-10-006\|AAPP-10-006]], [[#AAPP-12-004\|AAPP-12-004]], [[#AAPP-15-004\|AAPP-15-004]], [[#AAPP-16-003\|AAPP-16-003]] |
| [[Tema Esame 2023-06-19-2nd.pdf\|2023-06-19-2nd]] | [[#AAPP-18-009\|AAPP-18-009]], [[#AAPP-18-010\|AAPP-18-010]], [[#AAPP-19-018\|AAPP-19-018]], [[#AAPP-19-019\|AAPP-19-019]], [[#AAPP-19-020\|AAPP-19-020]], [[#AAPP-21-021\|AAPP-21-021]], [[#AAPP-21-022\|AAPP-21-022]], [[#AAPP-22-012\|AAPP-22-012]], [[#AAPP-23-017\|AAPP-23-017]] |
| [[Tema Esame 2023-07-11-1st.pdf\|2023-07-11-1st]] | [[#AAPP-01-007\|AAPP-01-007]], [[#AAPP-01-008\|AAPP-01-008]], [[#AAPP-01-009\|AAPP-01-009]], [[#AAPP-02-008\|AAPP-02-008]], [[#AAPP-04-007\|AAPP-04-007]], [[#AAPP-07-002\|AAPP-07-002]], [[#AAPP-10-007\|AAPP-10-007]], [[#AAPP-13-003\|AAPP-13-003]], [[#AAPP-14-001\|AAPP-14-001]], [[#AAPP-15-005\|AAPP-15-005]] |
| [[Tema Esame 2023-07-11-2nd.pdf\|2023-07-11-2nd]] | [[#AAPP-18-011\|AAPP-18-011]], [[#AAPP-18-012\|AAPP-18-012]], [[#AAPP-19-016\|AAPP-19-016]], [[#AAPP-19-021\|AAPP-19-021]], [[#AAPP-19-022\|AAPP-19-022]], [[#AAPP-19-023\|AAPP-19-023]], [[#AAPP-21-023\|AAPP-21-023]], [[#AAPP-23-018\|AAPP-23-018]], [[#AAPP-25-001\|AAPP-25-001]] |
| [[Tema Esame 2023-09-11-1st.pdf\|2023-09-11-1st]] | [[#AAPP-01-010\|AAPP-01-010]], [[#AAPP-01-011\|AAPP-01-011]], [[#AAPP-01-012\|AAPP-01-012]], [[#AAPP-02-009\|AAPP-02-009]], [[#AAPP-04-008\|AAPP-04-008]], [[#AAPP-07-003\|AAPP-07-003]], [[#AAPP-12-005\|AAPP-12-005]], [[#AAPP-14-002\|AAPP-14-002]], [[#AAPP-15-006\|AAPP-15-006]], [[#AAPP-16-004\|AAPP-16-004]] |
| [[Tema Esame 2023-09-11-2nd.pdf\|2023-09-11-2nd]] | [[#AAPP-18-013\|AAPP-18-013]], [[#AAPP-18-014\|AAPP-18-014]], [[#AAPP-19-018\|AAPP-19-018]], [[#AAPP-19-024\|AAPP-19-024]], [[#AAPP-20-002\|AAPP-20-002]], [[#AAPP-21-024\|AAPP-21-024]], [[#AAPP-23-019\|AAPP-23-019]], [[#AAPP-25-002\|AAPP-25-002]] |
| [[Tema Esame 2023-11-09-1st.pdf\|2023-11-09-1st]] | [[#AAPP-01-013\|AAPP-01-013]], [[#AAPP-02-010\|AAPP-02-010]], [[#AAPP-02-011\|AAPP-02-011]], [[#AAPP-07-004\|AAPP-07-004]], [[#AAPP-10-008\|AAPP-10-008]], [[#AAPP-10-009\|AAPP-10-009]], [[#AAPP-11-002\|AAPP-11-002]], [[#AAPP-13-004\|AAPP-13-004]], [[#AAPP-15-007\|AAPP-15-007]], [[#AAPP-16-005\|AAPP-16-005]] |
| [[Tema Esame 2023-12-21-2nd.pdf\|2023-12-21-2nd]] | [[#AAPP-18-015\|AAPP-18-015]], [[#AAPP-18-016\|AAPP-18-016]], [[#AAPP-19-025\|AAPP-19-025]], [[#AAPP-19-026\|AAPP-19-026]], [[#AAPP-20-003\|AAPP-20-003]], [[#AAPP-22-013\|AAPP-22-013]], [[#AAPP-23-020\|AAPP-23-020]], [[#AAPP-23-021\|AAPP-23-021]] |
| [[Tema Esame 2024-01-26-1st.pdf\|2024-01-26-1st]] | [[#AAPP-01-014\|AAPP-01-014]], [[#AAPP-01-015\|AAPP-01-015]], [[#AAPP-02-012\|AAPP-02-012]], [[#AAPP-02-013\|AAPP-02-013]], [[#AAPP-08-005\|AAPP-08-005]], [[#AAPP-09-001\|AAPP-09-001]], [[#AAPP-10-010\|AAPP-10-010]], [[#AAPP-11-003\|AAPP-11-003]], [[#AAPP-12-006\|AAPP-12-006]], [[#AAPP-15-008\|AAPP-15-008]], [[#AAPP-16-006\|AAPP-16-006]] |
| [[Tema Esame 2024-01-26-2nd.pdf\|2024-01-26-2nd]] | [[#AAPP-18-017\|AAPP-18-017]], [[#AAPP-18-018\|AAPP-18-018]], [[#AAPP-19-027\|AAPP-19-027]], [[#AAPP-19-028\|AAPP-19-028]], [[#AAPP-21-025\|AAPP-21-025]], [[#AAPP-22-014\|AAPP-22-014]], [[#AAPP-22-015\|AAPP-22-015]], [[#AAPP-23-022\|AAPP-23-022]], [[#AAPP-23-023\|AAPP-23-023]], [[#AAPP-23-024\|AAPP-23-024]] |
| [[Tema Esame 2024-02-16-1st.pdf\|2024-02-16-1st]] | [[#AAPP-01-016\|AAPP-01-016]], [[#AAPP-02-014\|AAPP-02-014]], [[#AAPP-02-015\|AAPP-02-015]], [[#AAPP-03-003\|AAPP-03-003]], [[#AAPP-04-009\|AAPP-04-009]], [[#AAPP-05-002\|AAPP-05-002]], [[#AAPP-06-005\|AAPP-06-005]], [[#AAPP-07-005\|AAPP-07-005]], [[#AAPP-10-011\|AAPP-10-011]], [[#AAPP-12-007\|AAPP-12-007]], [[#AAPP-15-009\|AAPP-15-009]] |
| [[Tema Esame 2024-02-16-2nd.pdf\|2024-02-16-2nd]] | [[#AAPP-18-019\|AAPP-18-019]], [[#AAPP-18-020\|AAPP-18-020]], [[#AAPP-19-029\|AAPP-19-029]], [[#AAPP-19-030\|AAPP-19-030]], [[#AAPP-21-026\|AAPP-21-026]], [[#AAPP-21-027\|AAPP-21-027]], [[#AAPP-22-016\|AAPP-22-016]], [[#AAPP-23-025\|AAPP-23-025]], [[#AAPP-23-026\|AAPP-23-026]], [[#AAPP-23-027\|AAPP-23-027]], [[#AAPP-25-003\|AAPP-25-003]] |
| [[Tema Esame 2024-06-26-1st.pdf\|2024-06-26-1st]] | [[#AAPP-01-017\|AAPP-01-017]], [[#AAPP-01-018\|AAPP-01-018]], [[#AAPP-02-016\|AAPP-02-016]], [[#AAPP-03-004\|AAPP-03-004]], [[#AAPP-04-010\|AAPP-04-010]], [[#AAPP-05-003\|AAPP-05-003]], [[#AAPP-06-006\|AAPP-06-006]], [[#AAPP-07-006\|AAPP-07-006]], [[#AAPP-11-004\|AAPP-11-004]], [[#AAPP-12-008\|AAPP-12-008]], [[#AAPP-16-007\|AAPP-16-007]] |
| [[Tema Esame 2024-06-26-2nd.pdf\|2024-06-26-2nd]] | [[#AAPP-18-021\|AAPP-18-021]], [[#AAPP-19-031\|AAPP-19-031]], [[#AAPP-19-032\|AAPP-19-032]], [[#AAPP-21-028\|AAPP-21-028]], [[#AAPP-21-029\|AAPP-21-029]], [[#AAPP-21-030\|AAPP-21-030]], [[#AAPP-23-028\|AAPP-23-028]], [[#AAPP-23-029\|AAPP-23-029]], [[#AAPP-23-030\|AAPP-23-030]], [[#AAPP-23-031\|AAPP-23-031]] |
| [[Tema Esame 2024-07-24-1st.pdf\|2024-07-24-1st]] | [[#AAPP-01-019\|AAPP-01-019]], [[#AAPP-01-020\|AAPP-01-020]], [[#AAPP-02-017\|AAPP-02-017]], [[#AAPP-03-005\|AAPP-03-005]], [[#AAPP-04-011\|AAPP-04-011]], [[#AAPP-08-006\|AAPP-08-006]], [[#AAPP-10-012\|AAPP-10-012]], [[#AAPP-12-009\|AAPP-12-009]], [[#AAPP-13-005\|AAPP-13-005]], [[#AAPP-15-010\|AAPP-15-010]], [[#AAPP-16-008\|AAPP-16-008]] |
| [[Tema Esame 2024-07-24-2nd.pdf\|2024-07-24-2nd]] | [[#AAPP-17-009\|AAPP-17-009]], [[#AAPP-18-022\|AAPP-18-022]], [[#AAPP-18-023\|AAPP-18-023]], [[#AAPP-19-033\|AAPP-19-033]], [[#AAPP-19-034\|AAPP-19-034]], [[#AAPP-20-004\|AAPP-20-004]], [[#AAPP-20-005\|AAPP-20-005]], [[#AAPP-20-006\|AAPP-20-006]], [[#AAPP-23-032\|AAPP-23-032]], [[#AAPP-23-033\|AAPP-23-033]], [[#AAPP-23-034\|AAPP-23-034]] |
| [[Tema Esame 2024-09-05-1st.pdf\|2024-09-05-1st]] | [[#AAPP-02-018\|AAPP-02-018]], [[#AAPP-02-019\|AAPP-02-019]], [[#AAPP-02-020\|AAPP-02-020]], [[#AAPP-04-012\|AAPP-04-012]], [[#AAPP-07-007\|AAPP-07-007]], [[#AAPP-10-013\|AAPP-10-013]], [[#AAPP-11-005\|AAPP-11-005]], [[#AAPP-12-010\|AAPP-12-010]], [[#AAPP-12-011\|AAPP-12-011]], [[#AAPP-16-009\|AAPP-16-009]] |
| [[Tema Esame 2024-09-05-2nd.pdf\|2024-09-05-2nd]] | [[#AAPP-17-010\|AAPP-17-010]], [[#AAPP-17-011\|AAPP-17-011]], [[#AAPP-18-024\|AAPP-18-024]], [[#AAPP-19-031\|AAPP-19-031]], [[#AAPP-19-035\|AAPP-19-035]], [[#AAPP-20-007\|AAPP-20-007]], [[#AAPP-21-031\|AAPP-21-031]], [[#AAPP-23-035\|AAPP-23-035]], [[#AAPP-23-036\|AAPP-23-036]], [[#AAPP-23-037\|AAPP-23-037]], [[#AAPP-25-004\|AAPP-25-004]] |
| [[Tema Esame 2024-11-12-1st.pdf\|2024-11-12-1st]] | [[#AAPP-01-021\|AAPP-01-021]], [[#AAPP-02-021\|AAPP-02-021]], [[#AAPP-02-022\|AAPP-02-022]], [[#AAPP-02-023\|AAPP-02-023]], [[#AAPP-04-013\|AAPP-04-013]], [[#AAPP-05-004\|AAPP-05-004]], [[#AAPP-06-007\|AAPP-06-007]], [[#AAPP-07-008\|AAPP-07-008]], [[#AAPP-07-009\|AAPP-07-009]], [[#AAPP-07-010\|AAPP-07-010]], [[#AAPP-11-006\|AAPP-11-006]], [[#AAPP-12-012\|AAPP-12-012]] |
| [[Tema Esame 2025-01-24-1st.pdf\|2025-01-24-1st]] | [[#AAPP-01-022\|AAPP-01-022]], [[#AAPP-02-024\|AAPP-02-024]], [[#AAPP-02-025\|AAPP-02-025]], [[#AAPP-02-026\|AAPP-02-026]], [[#AAPP-04-014\|AAPP-04-014]], [[#AAPP-06-008\|AAPP-06-008]], [[#AAPP-07-011\|AAPP-07-011]], [[#AAPP-08-007\|AAPP-08-007]], [[#AAPP-09-002\|AAPP-09-002]], [[#AAPP-11-007\|AAPP-11-007]], [[#AAPP-13-006\|AAPP-13-006]] |
| [[Tema Esame 2025-01-24-2nd.pdf\|2025-01-24-2nd]] | [[#AAPP-17-012\|AAPP-17-012]], [[#AAPP-18-025\|AAPP-18-025]], [[#AAPP-18-026\|AAPP-18-026]], [[#AAPP-19-036\|AAPP-19-036]], [[#AAPP-19-037\|AAPP-19-037]], [[#AAPP-20-008\|AAPP-20-008]], [[#AAPP-20-009\|AAPP-20-009]], [[#AAPP-22-017\|AAPP-22-017]], [[#AAPP-23-038\|AAPP-23-038]], [[#AAPP-23-039\|AAPP-23-039]], [[#AAPP-23-040\|AAPP-23-040]] |
| [[Tema Esame 2025-02-14-1st.pdf\|2025-02-14-1st]] | [[#AAPP-01-023\|AAPP-01-023]], [[#AAPP-01-024\|AAPP-01-024]], [[#AAPP-02-027\|AAPP-02-027]], [[#AAPP-02-028\|AAPP-02-028]], [[#AAPP-04-015\|AAPP-04-015]], [[#AAPP-07-012\|AAPP-07-012]], [[#AAPP-07-013\|AAPP-07-013]], [[#AAPP-09-003\|AAPP-09-003]], [[#AAPP-11-008\|AAPP-11-008]], [[#AAPP-12-013\|AAPP-12-013]], [[#AAPP-15-011\|AAPP-15-011]] |
| [[Tema Esame 2025-02-14-2nd.pdf\|2025-02-14-2nd]] | [[#AAPP-18-027\|AAPP-18-027]], [[#AAPP-18-028\|AAPP-18-028]], [[#AAPP-19-038\|AAPP-19-038]], [[#AAPP-19-039\|AAPP-19-039]], [[#AAPP-19-040\|AAPP-19-040]], [[#AAPP-21-032\|AAPP-21-032]], [[#AAPP-21-033\|AAPP-21-033]], [[#AAPP-22-018\|AAPP-22-018]], [[#AAPP-23-041\|AAPP-23-041]], [[#AAPP-23-042\|AAPP-23-042]], [[#AAPP-23-043\|AAPP-23-043]] |
| [[Tema Esame 2025-06-05-1st.pdf\|2025-06-05-1st]] | [[#AAPP-01-025\|AAPP-01-025]], [[#AAPP-01-026\|AAPP-01-026]], [[#AAPP-02-029\|AAPP-02-029]], [[#AAPP-02-030\|AAPP-02-030]], [[#AAPP-06-009\|AAPP-06-009]], [[#AAPP-07-014\|AAPP-07-014]], [[#AAPP-08-008\|AAPP-08-008]], [[#AAPP-11-009\|AAPP-11-009]], [[#AAPP-13-007\|AAPP-13-007]], [[#AAPP-15-012\|AAPP-15-012]], [[#AAPP-15-013\|AAPP-15-013]] |
| [[Tema Esame 2025-06-05-2nd.pdf\|2025-06-05-2nd]] | [[#AAPP-18-029\|AAPP-18-029]], [[#AAPP-19-041\|AAPP-19-041]], [[#AAPP-19-042\|AAPP-19-042]], [[#AAPP-19-043\|AAPP-19-043]], [[#AAPP-19-044\|AAPP-19-044]], [[#AAPP-19-045\|AAPP-19-045]], [[#AAPP-21-034\|AAPP-21-034]], [[#AAPP-21-035\|AAPP-21-035]], [[#AAPP-21-036\|AAPP-21-036]], [[#AAPP-23-044\|AAPP-23-044]], [[#AAPP-23-045\|AAPP-23-045]], [[#AAPP-23-046\|AAPP-23-046]] |
| [[Tema Esame 2025-07-04-1st.pdf\|2025-07-04-1st]] | [[#AAPP-01-027\|AAPP-01-027]], [[#AAPP-02-031\|AAPP-02-031]], [[#AAPP-02-032\|AAPP-02-032]], [[#AAPP-03-006\|AAPP-03-006]], [[#AAPP-05-005\|AAPP-05-005]], [[#AAPP-07-007\|AAPP-07-007]], [[#AAPP-08-009\|AAPP-08-009]], [[#AAPP-10-014\|AAPP-10-014]], [[#AAPP-12-014\|AAPP-12-014]], [[#AAPP-15-014\|AAPP-15-014]], [[#AAPP-15-015\|AAPP-15-015]] |
| [[Tema Esame 2025-07-04-2nd.pdf\|2025-07-04-2nd]] | [[#AAPP-18-030\|AAPP-18-030]], [[#AAPP-18-031\|AAPP-18-031]], [[#AAPP-19-046\|AAPP-19-046]], [[#AAPP-19-047\|AAPP-19-047]], [[#AAPP-19-048\|AAPP-19-048]], [[#AAPP-20-010\|AAPP-20-010]], [[#AAPP-20-011\|AAPP-20-011]], [[#AAPP-23-047\|AAPP-23-047]], [[#AAPP-23-048\|AAPP-23-048]], [[#AAPP-23-049\|AAPP-23-049]], [[#AAPP-25-005\|AAPP-25-005]] |
| [[Tema Esame 2025-09-05-1st.pdf\|2025-09-05-1st]] | [[#AAPP-01-009\|AAPP-01-009]], [[#AAPP-01-028\|AAPP-01-028]], [[#AAPP-01-029\|AAPP-01-029]], [[#AAPP-02-007\|AAPP-02-007]], [[#AAPP-04-016\|AAPP-04-016]], [[#AAPP-06-004\|AAPP-06-004]], [[#AAPP-07-008\|AAPP-07-008]], [[#AAPP-11-001\|AAPP-11-001]], [[#AAPP-13-008\|AAPP-13-008]], [[#AAPP-15-016\|AAPP-15-016]], [[#AAPP-16-010\|AAPP-16-010]] |
| [[Tema Esame 2025-09-05-2nd.pdf\|2025-09-05-2nd]] | [[#AAPP-17-007\|AAPP-17-007]], [[#AAPP-18-032\|AAPP-18-032]], [[#AAPP-18-033\|AAPP-18-033]], [[#AAPP-19-045\|AAPP-19-045]], [[#AAPP-19-049\|AAPP-19-049]], [[#AAPP-21-029\|AAPP-21-029]], [[#AAPP-21-037\|AAPP-21-037]], [[#AAPP-21-038\|AAPP-21-038]], [[#AAPP-23-050\|AAPP-23-050]], [[#AAPP-23-051\|AAPP-23-051]], [[#AAPP-23-052\|AAPP-23-052]] |
| [[Tema Esame 2025-11-06-1st.pdf\|2025-11-06-1st]] | [[#AAPP-01-030\|AAPP-01-030]], [[#AAPP-02-033\|AAPP-02-033]], [[#AAPP-02-034\|AAPP-02-034]], [[#AAPP-03-007\|AAPP-03-007]], [[#AAPP-04-017\|AAPP-04-017]], [[#AAPP-06-010\|AAPP-06-010]], [[#AAPP-08-010\|AAPP-08-010]], [[#AAPP-09-004\|AAPP-09-004]], [[#AAPP-10-015\|AAPP-10-015]], [[#AAPP-11-010\|AAPP-11-010]], [[#AAPP-12-015\|AAPP-12-015]], [[#AAPP-16-011\|AAPP-16-011]] |
| [[Tema Esame 2025-12-18-2nd.pdf\|2025-12-18-2nd]] | [[#AAPP-17-013\|AAPP-17-013]], [[#AAPP-18-034\|AAPP-18-034]], [[#AAPP-19-050\|AAPP-19-050]], [[#AAPP-19-051\|AAPP-19-051]], [[#AAPP-19-052\|AAPP-19-052]], [[#AAPP-20-012\|AAPP-20-012]], [[#AAPP-21-039\|AAPP-21-039]], [[#AAPP-21-040\|AAPP-21-040]], [[#AAPP-23-053\|AAPP-23-053]], [[#AAPP-23-054\|AAPP-23-054]], [[#AAPP-23-055\|AAPP-23-055]] |
| [[Tema Esame 2026-1-22-1st.pdf\|2026-1-22-1st]] | [[#AAPP-01-028\|AAPP-01-028]], [[#AAPP-01-031\|AAPP-01-031]], [[#AAPP-02-035\|AAPP-02-035]], [[#AAPP-03-008\|AAPP-03-008]], [[#AAPP-05-006\|AAPP-05-006]], [[#AAPP-07-015\|AAPP-07-015]], [[#AAPP-07-016\|AAPP-07-016]], [[#AAPP-09-005\|AAPP-09-005]], [[#AAPP-10-016\|AAPP-10-016]], [[#AAPP-12-016\|AAPP-12-016]], [[#AAPP-15-017\|AAPP-15-017]], [[#AAPP-16-012\|AAPP-16-012]] |
| [[Tema Esame 2026-1-22-2nd.pdf\|2026-1-22-2nd]] | [[#AAPP-17-014\|AAPP-17-014]], [[#AAPP-18-035\|AAPP-18-035]], [[#AAPP-18-036\|AAPP-18-036]], [[#AAPP-19-053\|AAPP-19-053]], [[#AAPP-19-054\|AAPP-19-054]], [[#AAPP-21-041\|AAPP-21-041]], [[#AAPP-21-042\|AAPP-21-042]], [[#AAPP-21-043\|AAPP-21-043]], [[#AAPP-23-056\|AAPP-23-056]], [[#AAPP-23-057\|AAPP-23-057]], [[#AAPP-23-058\|AAPP-23-058]] |
| [[Tema Esame 2026-2-09-1st.pdf\|2026-2-09-1st]] | [[#AAPP-01-032\|AAPP-01-032]], [[#AAPP-01-033\|AAPP-01-033]], [[#AAPP-02-036\|AAPP-02-036]], [[#AAPP-02-037\|AAPP-02-037]], [[#AAPP-06-011\|AAPP-06-011]], [[#AAPP-07-017\|AAPP-07-017]], [[#AAPP-08-011\|AAPP-08-011]], [[#AAPP-10-017\|AAPP-10-017]], [[#AAPP-11-011\|AAPP-11-011]], [[#AAPP-12-017\|AAPP-12-017]], [[#AAPP-13-009\|AAPP-13-009]], [[#AAPP-16-013\|AAPP-16-013]] |
| [[Tema Esame 2026-2-09-2nd.pdf\|2026-2-09-2nd]] | [[#AAPP-17-015\|AAPP-17-015]], [[#AAPP-18-037\|AAPP-18-037]], [[#AAPP-19-055\|AAPP-19-055]], [[#AAPP-19-056\|AAPP-19-056]], [[#AAPP-19-057\|AAPP-19-057]], [[#AAPP-21-044\|AAPP-21-044]], [[#AAPP-21-045\|AAPP-21-045]], [[#AAPP-21-046\|AAPP-21-046]], [[#AAPP-23-059\|AAPP-23-059]], [[#AAPP-23-060\|AAPP-23-060]], [[#AAPP-23-061\|AAPP-23-061]] |
| [[Tema Esame 2026-6-11-1st.pdf\|2026-6-11-1st]] | [[#AAPP-01-034\|AAPP-01-034]], [[#AAPP-01-035\|AAPP-01-035]], [[#AAPP-01-036\|AAPP-01-036]], [[#AAPP-02-038\|AAPP-02-038]], [[#AAPP-04-018\|AAPP-04-018]], [[#AAPP-07-008\|AAPP-07-008]], [[#AAPP-07-018\|AAPP-07-018]], [[#AAPP-09-006\|AAPP-09-006]], [[#AAPP-10-018\|AAPP-10-018]], [[#AAPP-12-018\|AAPP-12-018]], [[#AAPP-15-018\|AAPP-15-018]], [[#AAPP-16-014\|AAPP-16-014]] |
| [[Tema Esame 2026-6-11-2nd.pdf\|2026-6-11-2nd]] | [[#AAPP-17-016\|AAPP-17-016]], [[#AAPP-18-038\|AAPP-18-038]], [[#AAPP-18-039\|AAPP-18-039]], [[#AAPP-19-058\|AAPP-19-058]], [[#AAPP-19-059\|AAPP-19-059]], [[#AAPP-19-060\|AAPP-19-060]], [[#AAPP-21-047\|AAPP-21-047]], [[#AAPP-21-048\|AAPP-21-048]], [[#AAPP-23-062\|AAPP-23-062]], [[#AAPP-23-063\|AAPP-23-063]], [[#AAPP-23-064\|AAPP-23-064]] |
| [[Tema Esame 2026-6-29-1st.pdf\|2026-6-29-1st]] | [[#AAPP-01-023\|AAPP-01-023]], [[#AAPP-01-026\|AAPP-01-026]], [[#AAPP-02-016\|AAPP-02-016]], [[#AAPP-02-039\|AAPP-02-039]], [[#AAPP-04-004\|AAPP-04-004]], [[#AAPP-05-007\|AAPP-05-007]], [[#AAPP-06-012\|AAPP-06-012]], [[#AAPP-08-012\|AAPP-08-012]], [[#AAPP-09-003\|AAPP-09-003]], [[#AAPP-11-012\|AAPP-11-012]], [[#AAPP-12-019\|AAPP-12-019]], [[#AAPP-16-015\|AAPP-16-015]] |
| [[Tema Esame 2026-6-29-2nd.pdf\|2026-6-29-2nd]] | [[#AAPP-18-040\|AAPP-18-040]], [[#AAPP-18-041\|AAPP-18-041]], [[#AAPP-19-061\|AAPP-19-061]], [[#AAPP-19-062\|AAPP-19-062]], [[#AAPP-21-049\|AAPP-21-049]], [[#AAPP-21-050\|AAPP-21-050]], [[#AAPP-21-051\|AAPP-21-051]], [[#AAPP-21-052\|AAPP-21-052]], [[#AAPP-23-065\|AAPP-23-065]], [[#AAPP-23-066\|AAPP-23-066]], [[#AAPP-23-067\|AAPP-23-067]] |
| [[Tema Esame 2026-9-10-1st.pdf\|2026-9-10-1st]] | [[#AAPP-01-027\|AAPP-01-027]], [[#AAPP-02-040\|AAPP-02-040]], [[#AAPP-02-041\|AAPP-02-041]], [[#AAPP-03-009\|AAPP-03-009]], [[#AAPP-04-019\|AAPP-04-019]], [[#AAPP-05-008\|AAPP-05-008]], [[#AAPP-05-009\|AAPP-05-009]], [[#AAPP-07-019\|AAPP-07-019]], [[#AAPP-07-020\|AAPP-07-020]], [[#AAPP-09-007\|AAPP-09-007]], [[#AAPP-10-019\|AAPP-10-019]], [[#AAPP-15-019\|AAPP-15-019]] |
| [[Tema Esame 2026-9-10-2nd.pdf\|2026-9-10-2nd]] | [[#AAPP-18-042\|AAPP-18-042]], [[#AAPP-19-063\|AAPP-19-063]], [[#AAPP-19-064\|AAPP-19-064]], [[#AAPP-19-065\|AAPP-19-065]], [[#AAPP-20-013\|AAPP-20-013]], [[#AAPP-21-053\|AAPP-21-053]], [[#AAPP-21-054\|AAPP-21-054]], [[#AAPP-21-055\|AAPP-21-055]], [[#AAPP-23-068\|AAPP-23-068]], [[#AAPP-23-069\|AAPP-23-069]], [[#AAPP-23-070\|AAPP-23-070]] |
