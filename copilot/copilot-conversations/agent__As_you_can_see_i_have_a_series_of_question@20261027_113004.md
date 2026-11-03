---
epoch: 1793097004660
mode: agent
backendId: codex
sessionId: "01a18a1e-746e-7833-8593-25301f6d23af"
agentLabel: "As you can see i have a series of question from old exams, i…"
lastAccessedAt: 1793731270891
usage: '{"usedTokens":175489,"contextWindow":828400,"updatedAt":1793731746199}'
tags:
  - copilot-conversation
---

**user**: As you can see i have a series of question from old exams, is there a way you can set up each question so i can answer it under it and i will later ask you to correct the result?
[Timestamp: 2026/10/27 11:30:04]

**ai**: I’ll read the question bank and add a clear answer area beneath each question, so you can fill it in and ask me to review it later.I’m using the Obsidian Markdown skill to keep the note’s formatting and links intact. Each question will get a “My answer” area and a collapsed “Feedback” area for later corrections.Done — all **552 questions** in [[Past Exam Question Bank]] now have:

- A **My answer** area for your response, calculations, or code.
- A collapsed **Feedback** area for later corrections.

Replace “Write your answer here” with your attempt. Then ask, for example: **“Correct my answer to AAPP-01-001”** or **“Review my completed PRAM answers.”**

I’ll preserve your original attempt and put corrections in the feedback area.
[Timestamp: 2026/10/27 11:30:04]

**user**: Ok i answered a few questions so please go back to the related notes and also look for other sources online to answer them.
[Timestamp: 2026/10/27 12:57:08]

**user**: Ok i answered a few questions so please go back to the related notes and also look for other sources online to answer them.
[Timestamp: Unknown time]

**ai**: I’ll find the answers you’ve filled in, check them against the related course notes and online sources, and add corrections in the feedback areas while keeping your attempts intact.I found 12 attempted questions, all on PRAM. Your phase descriptions are mostly sound; the main corrections concern how parallel time is counted, what “arbitrary” writes mean, and when a write conflict occurs. The lecture slides also group arbitrary and random writes together, so I’ll explain that distinction in the feedback.The source check confirms two useful points: common CRCW requires the algorithm to ensure that simultaneous writes agree, and arbitrary CRCW must remain correct whichever writer wins. I also found a university lecture page with the exact claim in question 009; I’ll give its intended answer and explain the assumptions behind it.Reviewed **AAPP-01-001 through AAPP-01-012** in [[Past Exam Question Bank]], using [[PRAM]], the lecture slides, and academic sources online.

Each **Feedback** callout now contains an assessment, explanations of mistakes, a suggested exam answer, and source links. Your original attempts are preserved.

Focus your revision on counting parallel time, shared-memory assumptions, and CRCW write rules. Questions marked “I don’t know” also have explained answers.
[Timestamp: Unknown time]

**user**: Ok i answered a few more questions correct those as well
[Timestamp: 2026/10/28 11:39:24]

**ai**: I’ll find the new attempts, check them against the course notes and relevant sources, and add feedback beneath each one while preserving your answers.I found eight new attempts, **AAPP-01-013–020**. Your answers on timing, private registers, and synchronization are mostly sound. I’ll explain implicit synchronization more fully, separate space complexity from memory-access time, and give you a different common-CRCW example as requested.The feedback is ready. I used an array-sortedness test for the second common-CRCW example. For the questions asking for assumptions “in order of priority,” I’ve marked the ordering as a reasoned suggestion—the available slides give no official ranking. I’m checking that the edits preserve your answers and earlier feedback.Corrected **AAPP-01-013–020** in [[Past Exam Question Bank]].

Each **Feedback** callout now includes an assessment, suggested exam answer, and references. I also explained implicit synchronization and added a different common-CRCW example: checking whether an array is sorted.

Your original attempts and previous feedback are unchanged. The main areas to revisit are space complexity and the common-CW security example.
[Timestamp: 2026/10/28 11:39:24]

**user**: I answered to all question for the first PRAM section please correct them. it should be APP 01 from 021 to 036
[Timestamp: 2026/10/30 02:01:57]

**ai**: I’ll find APP 01 questions 021–036, check your answers, and add corrections in the note.
I’m using the Obsidian Markdown skill to preserve the note’s formatting and links while reviewing your answers.
The main corrections are that unit-time memory access still takes one model step, and an EREW algorithm can run unchanged on CREW or CRCW. I’m also checking the bounded-processor and reduced-memory questions, where the assumptions affect the answer.
Your explanation of synchronization is mostly sound. The recurring gaps are the memory-access rules and complexity claims: shared memory still has access restrictions, and the reduced-memory lemma gives an upper bound rather than an exact slowdown. I’ll preserve your attempts and put each assessment and corrected answer in its existing collapsed Feedback callout.
All 16 Feedback callouts are now filled in, with your original answers preserved. I’m checking the study links and confirming that the edits are limited to questions 021–036.
Reviewed **AAPP-01-021–036** in [[Past Exam Question Bank]]. All 16 **Feedback** callouts now contain an assessment, corrected exam answer, and study references. Your original answers are preserved.

Focus your revision on **023, 026, 032, and 033**. Another recurring correction: unit-time memory access takes **one model step**, not zero time.
[Timestamp: 2026/10/30 02:01:57]

**user**: Ok i moved to section 2 and i aswered up to question 8 correct them please
[Timestamp: 2026/10/30 20:23:42]

**ai**: I’ll review AAPP-02-001–008 and add feedback beneath each answer, preserving your attempts.
Question 008 still contains the answer placeholder, so I’ll leave it unreviewed. For 001–007, the main corrections concern the difference between defining speedup and predicting it, and the runtime used to measure the serial fraction in each scaling law.
Your answers to 004 and 006 are correct. Answers 002, 003, and 007 need clearer assumptions, while 001 needs the general speedup definition before Amdahl’s formula. For 005, I’ll add a self-contained answer so it can stand on its own in an exam.
Reviewed **AAPP-02-001–007** in [[Past Exam Question Bank]], adding assessments, corrected answers, and study links while preserving your attempts.

**004 and 006 are correct.** The main revisions concern speedup definitions and the assumptions behind Amdahl and Gustafson.

**008 still contains the answer placeholder**, so it remains unreviewed.
[Timestamp: 2026/10/30 20:23:42]

**user**: Ok then i don't understand what gustafson law really is
[Timestamp: 2026/10/30 22:01:09]

**ai**: I’ll use the course’s explanation and a small example to show what Gustafson’s speedup actually compares.
**Gustafson starts with a fixed time budget: use more processors to solve a larger problem within that time.**

Imagine a simulation with these ideal timings:

- Setting it up takes **2 seconds**, performed sequentially.
- Simulating **100 particles** takes **8 seconds on one processor**.

With one processor, you simulate 100 particles in $2+8=10$ seconds.

Now use **4 processors** and increase the simulation to **400 particles**. Each processor handles 100 particles, so the parallel phase still takes 8 seconds. Including setup, you still finish in **10 seconds**.

To calculate speedup, compare how long **that same 400-particle simulation** takes:

| Part | On 4 processors | On 1 processor |
|---|---:|---:|
| Setup | 2 seconds | 2 seconds |
| Simulating 400 particles | 8 seconds | 32 seconds |
| **Total** | **10 seconds** | **34 seconds** |

Therefore:

$$
S=\frac{34}{10}=3.4
$$

The extra processors let you complete a larger simulation within your original time budget.

Gustafson’s formula expresses this calculation generally. Let $s$ be the fraction of the **parallel run’s elapsed time** spent on sequential work. Here:

$$
s=\frac{2}{10}=0.2
$$

The sequential part runs once. The work completed by $p$ processors during the parallel part would take $p$ times as long on one processor. Thus:

$$
S_G=s+p(1-s)
$$

For the example:

$$
S_G=0.2+4(0.8)=3.4
$$

This assumes ideal distribution of the parallel work, unchanged serial work, and no additional overhead. [Gustafson’s original paper](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf#page=2)

The distinction from Amdahl is what you hold fixed:

- **Amdahl:** keep the particle count fixed and calculate how runtime decreases.
- **Gustafson:** keep the time budget fixed and increase the particle count as processors are added.
[Timestamp: 2026/10/30 22:01:09]

**user**: But why multiple by p, it just increases the workload
[Timestamp: 2026/10/30 22:03:53]

**ai**: We multiply by $p$ because we are calculating **how long one processor would need to do the work completed by all $p$ processors**.

Suppose 4 processors work simultaneously for 8 seconds:

- Each performs 8 seconds’ worth of work.
- Together they perform $4\times8=32$ processor-seconds of work.
- One processor would need **32 seconds** to perform those four pieces sequentially.

The parallel execution still takes **8 seconds**. Multiplication reconstructs the sequential comparison time.

Including the 2-second setup:

$$
S=\frac{\text{one processor doing all that work}}{\text{four processors doing all that work}}
=\frac{2+4\times8}{2+8}=3.4
$$

**Your observation is right: the workload increases.** Gustafson quantifies the benefit of completing that larger workload within the same time budget. Both sides of the speedup ratio execute that same larger workload.
[Timestamp: 2026/10/30 22:03:53]

**user**: ok so it right to say that gustafson is calculating the factor by which the parallel alogrithm is longer, if executed sequentially?
[Timestamp: 2026/10/30 22:06:49]

**ai**: Yes—**“longer” means execution time**. You can say:

> Gustafson’s speedup tells us how many times longer the same scaled workload would take to execute sequentially than on $p$ processors.

For example, $S_G=3.4$ means sequential execution would take **3.4 times as long**.

What makes it specifically Gustafson’s viewpoint is that **the workload grows with processor count while the parallel execution time stays fixed**.
[Timestamp: 2026/10/30 22:06:49]

**user**: Ok i completed the second section please correct that
[Timestamp: 2026/11/01 00:49:38]

**ai**: I’ll check the completed second section and add feedback to the remaining answers. I’ll also check whether any previously reviewed answers have changed.
Questions 001–007 are unchanged, and I found answers for all of 008–041. The main issues so far are a reversed speedup ratio in 031, weak scaling’s fixed work per processor, and the conclusion in 037: near-linear speedup alone does not identify which scaling model applies.
The corrections are drafted. I’ve treated “already answered above” entries as revision cross-references and supplied concise answers that can stand on their own in an exam. The feedback also includes worked examples for extra work, idle processor cost, and speedup.
All **41 questions in section 2** are now reviewed in [[Past Exam Question Bank]]. I added feedback to **008–041**, preserving your answers and earlier reviews.

Main points to revisit:

- **031:** the one-processor speedup ratio is $p$; efficiency 1 does not prove sequential optimality.
- **037:** near-linear speedup can fit either scaling model.
- **Weak scaling:** work per processor stays fixed; constant runtime is the desired result.
- **022/040:** distinguish extra executed work from idle processor cost.
[Timestamp: 2026/11/01 00:49:38]

**user**: Ok i completed section 3
[Timestamp: 2026/11/01 19:08:22]

**ai**: I’ll review section 3 and add corrections beneath your answers, preserving your attempts.
The main corrections concern matrix complexity and the comparison between scan and reduction. Your matrix–matrix answers use matrix–vector work bounds. Also, scan computes every prefix while reduction computes one total, so keeping more processors busy does not by itself make scan more efficient.
Your concurrent-read example matches the lecture diagram: after the first pairwise sums, the value at position 2 is read by the processors computing prefixes 3 and 4. I’m keeping that broadcast scan separate from other scan implementations, since their intermediate values and work counts can differ.
I’ve also qualified two prompts where the wording matters: 006 does not specify the efficiency metric, and “vector sum” in 009 could mean a reduction, elementwise addition, or a prefix scan. The feedback states the algorithm and assumptions for each answer.
Reviewed **AAPP-03-001–009** in [[Past Exam Question Bank]], preserving your answers and adding corrected explanations, pseudocode, and study references.

Main corrections:

- **001/005:** classical matrix–matrix multiplication performs $\Theta(n^3)$ work.
- **004:** the matrix–vector time bound was missing a factor of $n$.
- **003/006:** scan computes every prefix; greater processor activity does not automatically mean greater efficiency.

Your concurrent-read example in **002 is correct** for the lecture’s broadcast scan.
[Timestamp: 2026/11/01 19:08:22]

**user**: I completed section 5
[Timestamp: 2026/11/01 20:38:10]

**ai**: I’ll review section 5 and add feedback beneath your answers, preserving your attempts.
[Timestamp: 2026/11/01 20:38:10]

**user**: Sorry i mean i completed section 4
[Timestamp: 2026/11/01 20:38:23]

**ai**: I’ll review section 4, “Divide and conquer and recurrences,” and add feedback beneath your answers.
Your powering explanation has the right central idea: compute the half-power once and reuse it. The main gaps are the Master theorem’s conditions and the space analyses. There are also two formula corrections: the odd exponent needs parentheses around $(n-1)/2$, and Strassen’s exponent is $\log_2 7\approx2.807$, so $O(n^{2.8})$ is not a valid exact bound.
The exam prompts explicitly ask about space in 007, 008, and 011, so I’ll cover those parts too. Recursive powering uses $\Theta(\log n)$ stack space under the course’s word-cost model. I’ll also explain when the Master theorem can help analyze space or layout area.
The feedback for all 19 questions is ready. I’ve kept your “already answered above” entries and added self-contained exam answers beneath them. The review also distinguishes ordinary block multiplication, which remains cubic, from Strassen’s seven-product recursion.
Reviewed **AAPP-04-001–019** in [[Past Exam Question Bank]], preserving your answers and adding corrections and study references.

Main points to revisit:

- **008/010/011:** Master theorem assumptions, polynomial gaps, and regularity.
- **007/011:** recursive powering uses $\Theta(\log n)$ stack space.
- **005/012:** Strassen achieves $\Theta(n^{\log_2 7})$; ordinary block multiplication remains cubic.
- **011:** the odd exponent is $(n-1)/2$.
[Timestamp: 2026/11/01 20:38:23]

**user**: I completed section 5
[Timestamp: 2026/11/01 23:12:23]

**ai**: I’ll review section 5 and add feedback beneath your answers, preserving your attempts.
Your distinction between Las Vegas and Monte Carlo is mostly correct. I’ll clarify the runtime guarantees and the assumptions in your sampling example. Questions 008 and 009 also need a concrete data-structure example; a treap shows how randomization can improve expected performance while preserving exact answers.
Your sampling example works under the lecture’s assumptions: independent uniform samples, with half the entries equal to `a`. Then Las Vegas needs 2 samples on average, and 20 Monte Carlo samples have failure probability $2^{-20}$. I’ll make those assumptions explicit and explain what changes if `a` is rare or absent.
The nine feedback entries are ready, including a treap example for 008 and 009. I’ve also clarified that a Las Vegas algorithm can have a finite worst-case bound; an unbounded worst case is possible, but it is not part of the definition.
Reviewed **AAPP-05-001–009** in [[Past Exam Question Bank]], preserving your answers and adding corrections and study links.

Your main classification is mostly correct. Key clarifications:

- Las Vegas algorithms can have finite worst-case bounds.
- Monte Carlo efficiency also needs an error guarantee.
- Your sampling example needs assumptions about target frequency.

I added concrete **treap examples for 008 and 009** to explain randomized balancing with exact answers.
[Timestamp: 2026/11/01 23:12:23]

**user**: i did a few from section 6
[Timestamp: 2026/11/02 16:08:21]

**ai**: I’ll find the answers you’ve filled in under section 6 and add feedback, leaving unanswered questions blank.
I found answers for **AAPP-06-001 and 002**. Your basic Karger description is mostly correct. The main correction is that Karger–Stein recursively branches at every level; its advantage comes from needing far fewer repetitions, even though one recursive run costs more than one basic Karger run.
Your $O(n^4\log n)$ amplified bound for basic Karger is correct under the course’s implementation model. I’ve clarified that $2/[n(n-1)]$ is a success lower bound, and added separate single-run and amplified bounds for Karger–Stein.
Reviewed **AAPP-06-001 and 002** in [[Past Exam Question Bank]], preserving your attempts and leaving unanswered questions blank.

The main correction is that **Karger–Stein recursively solves both branches at every level**. I added a table separating single-run cost from amplified cost.

Your Monte Carlo classification is correct. I also clarified that $2/[n(n-1)]$ is a **success lower bound**, not necessarily the exact probability.
[Timestamp: 2026/11/02 16:08:21]

**user**: Actually there are too many questions, can you go ahead and answer to all question even if incomplete, later i might ask you to check my answer but i can't do all of them
[Timestamp: 2026/11/02 18:50:16]

**ai**: I’ll add model answers throughout the question bank, including unanswered and incomplete entries, while preserving your attempts and existing feedback. I’ll check the course material for each topic and flag answers that need assumptions or lack course-specific support.
The bank has **552 entries**, and 116 already contain reviewed reference answers. I’m using the Obsidian Markdown skill to add a separate collapsed **Model answer** to each entry, so you can still write your own attempt and ask for feedback later.
I’ve mapped the remaining topics. Later sections include code defects, synchronization cases, and questions that depend on diagrams, so I’m checking those individually. I also found your newer competitive-analysis notes, which distinguish the paid-swap and free-move models for move-to-front.
The diagram questions need more than a work/span calculation: some graphs need extra threads to reach the span because several tasks must overlap. I’m checking actual schedules and marking defects in the printed code so the model answers explain them explicitly.
The answers through section 19 are drafted, including the code corrections and the PRAM time/work bounds. I’m now filling in the OpenMP, Pthreads, MPI, CUDA and Halide sections, using the official specifications where the course notes don’t cover a detail.
Every question now has a draft answer. I’m checking the full set for missing subparts, math formatting and links, and verifying that your original attempts and feedback stay intact. Where a question asks for an example “from the lecture” that the supplied material doesn’t identify, I’ve labelled the standard example I used.
I noticed you added an answer to AAPP-06-011 while I was working. I’ll preserve that newer text too. The checks confirm coverage for all 552 entries and valid links to the referenced vault notes.
Added answers to **all 552 questions** in [[Past Exam Question Bank]], each under a collapsed **Model answer** callout.

Your attempts and existing feedback are preserved, including your newest answer. I’ve flagged source errors and necessary assumptions. You can still write under **My answer** and ask me to check it later.
[Timestamp: 2026/11/02 18:50:16]

**user**: i have a doubt about select ith algorithms. If the random quick select is is O(n) expected and worst case O(n^2) and the deterministic is O(n) worst case why would i not use it every time
[Timestamp: 2026/11/03 19:42:17]

**ai**: I’ll check how your notes compare the two, especially the extra work needed to choose the deterministic pivot.
Because **deterministic SELECT does extra work to guarantee a good pivot**, and Big-O hides that overhead.

- **Randomized Quickselect:** pick a random element cheaply, partition, and recurse into the needed side.
- **Median-of-medians SELECT:** find the median of every group of five, recursively select the median of those medians, then partition and recurse into the needed side.

That extra pivot construction guarantees progress, but costs more work. Both can be linear while having different constants: hypothetically, $5n$ expected operations versus $20n$ guaranteed operations. Those numbers are illustrative, but both are $O(n)$.

So the tradeoff is:

| Algorithm | What you gain | What you pay |
|---|---|---|
| Randomized Quickselect | Simple pivot choice, often lower overhead | An unlucky execution can take $\Theta(n^2)$ |
| Deterministic SELECT | Guaranteed $\Theta(n)$ worst-case time | More expensive pivot construction |

**A better worst-case bound does not necessarily mean a faster algorithm on typical executions.** Deterministic SELECT buys predictability; randomized Quickselect avoids paying for that guarantee every time.
[Timestamp: 2026/11/03 19:42:17]

**user**: I still don't understand how the deterministic having a max partition of 7/10 make the worst case linear
[Timestamp: 2026/11/03 19:43:58]

**ai**: Because **the work gets smaller at every recursive step**. You don’t process all $n$ elements again each time.

Suppose you start with **1,000 elements**. After partitioning, you only search the side containing the requested rank. Its size is at most:

$$
1000 \;\to\; 700 \;\to\; 490 \;\to\; 343 \;\to\;\cdots
$$

Each partition costs time proportional to its current size. So, temporarily ignoring pivot construction, the total work is bounded by:

$$
n+0.7n+0.7^2n+\cdots
=\frac{n}{1-0.7}
=\frac{10}{3}n.
$$

That is **a constant times $n$**, hence linear.

Now include the work of finding the deterministic pivot. There are **two recursive calls**:

- One on $n/5$ elements to find the median of the group medians.
- One on at most $7n/10$ elements to find your requested element.

Therefore, ignoring rounding:

$$
T(n)\le T(0.2n)+T(0.7n)+cn.
$$

The crucial observation is **$0.2+0.7=0.9<1$**. Across the entire recursion tree, the combined problem sizes shrink:

| Recursion level | Total size of all subproblems |
|---|---:|
| 0 | $n$ |
| 1 | At most $0.9n$ |
| 2 | At most $0.81n$ |
| 3 | At most $0.729n$ |

Thus the total work is bounded by:

$$
cn+0.9cn+0.9^2cn+\cdots
=\frac{cn}{1-0.9}
=10cn
=O(n).
$$

There are many recursive calls, but **their combined work forms a shrinking geometric sum**.
[Timestamp: 2026/11/03 19:43:58]

**user**: Ok but in the exam how should i answer about the time guarantee. Like i know how to get to that 7/10 but then how do i describe the next step in a simple way. Or i should just skip the implication
[Timestamp: 2026/11/03 19:46:10]

**ai**: **Include the implication; a short explanation is enough.** You can write:

> Finding the pivot requires a recursive call on $n/5$ elements, and selecting the desired element requires a call on at most $7n/10$ elements. Grouping and partitioning take $O(n)$ time. Therefore, ignoring rounding:
>
> $T(n)\le T(n/5)+T(7n/10)+O(n)$.
>
> Since $1/5+7/10=9/10<1$, the total size of the subproblems decreases geometrically across recursion levels. Summing their work gives **$O(n)$ worst-case time**.

The essential phrase is **“the fractions sum to less than one, so the total work decreases geometrically.”** You can omit the full geometric-series calculation unless a detailed proof is requested.
[Timestamp: 2026/11/03 19:46:10]

**user**: what is the n/5
[Timestamp: 2026/11/03 19:47:05]

**ai**: The **$n/5$ is the number of group medians used to choose the pivot**.

For example, with **100 elements**:

1. Divide them into **20 groups of 5**.
2. Find each group’s median → you now have **20 medians**.
3. Recursively run SELECT on those **20 medians** to find their median. That value becomes your pivot.

Since $20=100/5$, this recursive call costs **$T(n/5)$**.

So the recurrence includes two jobs:

- **$T(n/5)$:** find a good pivot.
- **$T(7n/10)$:** after partitioning, search for your requested element in the remaining side.

Grouping and partitioning supply the additional $O(n)$ work.
[Timestamp: 2026/11/03 19:47:05]

**user**: and how is this different from the quickselect O(n^2)
[Timestamp: 2026/11/03 19:48:36]

**ai**: The difference is **how much smaller the remaining problem is guaranteed to become**.

With **randomized Quickselect**, suppose you want the maximum and keep randomly choosing the minimum as pivot. You discard only **one element** each time:

$$
n,\;n-1,\;n-2,\;\ldots
$$

Each partition scans the remaining elements, so:

$$
T(n)=T(n-1)+O(n)
\quad\Rightarrow\quad
n+(n-1)+(n-2)+\cdots=\Theta(n^2).
$$

With **deterministic SELECT**, the extra $T(n/5)$ work constructs a pivot that guarantees you discard roughly **30%**. The side searched is therefore at most:

$$
n,\;0.7n,\;0.49n,\;\ldots
$$

Including pivot construction, the recurrence is:

$$
T(n)\le T(0.2n)+T(0.7n)+O(n).
$$

Since $0.2+0.7=0.9<1$, the combined work shrinks geometrically, giving **$O(n)$ worst-case time**.

So **the $T(n/5)$ is extra work you pay to guarantee good progress**. Randomized Quickselect chooses its pivot cheaply and achieves linear time in expectation, but permits the unlucky quadratic execution.
[Timestamp: 2026/11/03 19:48:36]