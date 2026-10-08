---
tags:
  - aapp
  - lecture
lecture: "1"
source: "[[lecture1-Intro-Course2026-2027.pdf]]"
---
# Course Introduction

[[AAPP Index|Course index]] · Next: [[Algorithm as recipes]]

## Overview

**Advanced Algorithms and Parallel Programming**, course code **095946**, combines algorithm design and analysis with the practical challenges of parallel implementation. The introduction is labeled academic year **2026–2027**.

The central skill is to move from a problem to an algorithm, establish its correctness and cost, and understand what changes when it runs on real hardware. A theoretically parallel algorithm can still be limited by communication, dependencies, memory access, or the tools used to implement it.

Source: [[lecture1-Intro-Course2026-2027.pdf#page=2|Objectives and learning outcomes, pp. 2–3]].

## Part I: advanced algorithms

The announced syllabus groups several ways to design and assess algorithms:

| Topic | Main question |
|---|---|
| Randomization | Can random choices improve expected behavior or control failure probability? |
| Dynamic programming | Can overlapping subproblems be solved once and reused? |
| Amortized analysis | What is the total cost of a sequence of operations? |
| Approximation | Can we obtain a provably good solution when exact optimization is expensive? |
| Competitive analysis | How well does an online algorithm compare with an offline solution? |

The decks supplied so far cover review material in [[Algorithm as recipes]], the design paradigm in [[Divide and Conquer]], and the foundations in [[Randomized Algorithms]].

The introduction additionally lists the hiring problem, random permutations, randomized quicksort, order statistics, primality tests and fast exponentiation, cryptosystems, Karger and Karger–Stein min-cut, skip lists, treaps, memoization, string matching, BDDs, dynamic tables, and move-to-front lists. These are syllabus items, not all content of the six supplied decks.

Source: [[lecture1-Intro-Course2026-2027.pdf#page=4|Algorithm syllabus, pp. 4–5]].

![[aapp-lecture1-algorithm-roadmap.png|720]]

*A visual roadmap of the first algorithm topics announced in the course introduction.* [[lecture1-Intro-Course2026-2027.pdf#page=4|Source slide 4]].

## Part II: parallel programming

The parallel part connects an abstract machine model to practical languages and libraries:

- Parallel algorithm design and machine models: introduced in [[PRAM]].
- Patterns such as reduce, prefix sum, split, compaction/expansion, segmented scan, sorting, map-reduce, and kernel fusion.
- Domain decomposition versus functional decomposition.
- Communication costs: latency, bandwidth, visibility, and synchronization.
- Data dependencies and automatic versus manual parallelization.
- Tools including POSIX threads, OpenMP, MPI, and Halide; the supplied [[ISPC]] deck provides an implementation example using SIMD and tasks.

The introduction states that CUDA is no longer part of this course syllabus.

Source: [[lecture1-Intro-Course2026-2027.pdf#page=6|Parallel syllabus]].

## Prerequisites and study approach

The stated prerequisites are operations research, basic data structures, and computational complexity; C/C++ knowledge is helpful.

![[aapp-lecture1-prerequisites.png|720]]

*The background knowledge the course expects you to bring to the algorithm and programming material.* [[lecture1-Intro-Course2026-2027.pdf#page=7|Source slide 7]].

For a technical topic, prepare to answer four questions:

1. **Problem:** What is the input and what output is required?
2. **Correctness:** Why does the procedure produce that output?
3. **Analysis:** Which operations are counted, and how does their count grow?
4. **Implementation:** Which assumptions break on a real machine?

This question sequence is a supplementary study aid, based on the course objectives.

## Study priorities for the supplied decks

This checklist defines the scope of this note collection, based on the six PDFs currently supplied. It is a study guide, not confirmation that these PDFs cover the entire exam.

| Note | What to be able to do without looking |
|---|---|
| [[Algorithm as recipes]] | Trace sorting, distinguish bounds from input cases, derive and solve recurrences |
| [[Divide and Conquer]] | Identify recursive calls, verify Strassen's products, analyze tree-layout dimensions |
| [[PRAM]] | Check access legality, calculate time/work/cost, interpret scaling experiments |
| [[ISPC]] | Identify uniform/varying data, trace masks and local counts, explain gang versus task parallelism |
| [[Randomized Algorithms]] | State the probability space, use indicators, derive expected hires and sampling failure |

For a written answer, state the assumptions, explain the algorithm, justify correctness, and show the calculation. For an open question, connect the definition to one of the lecture examples. The technical notes now include **Exam practice** sections with original problems and worked solutions based on these topics.

External material in the notes supplies explanations for these same concepts. The broader syllabus announced in the introduction remains a roadmap until its decks or exercises are supplied. Dates and grading rules continue to come from the uploaded introduction rather than unrelated external courses.

## Teaching material

The deck lists these books:

- Cormen, Leiserson, Rivest, Stein — *Introduction to Algorithms*, 3rd edition, 2009.
- Motwani, Raghavan — *Randomized Algorithms*, 1995.
- McCool, Reinders, Robison — *Structured Parallel Programming: Patterns for Efficient Computation*, 2012.
- Pacheco — *An Introduction to Parallel Programming*, 2011.

Additional course material is provided through [WeBeep](https://webeep.polimi.it), with access restricted to course participants. This link is a resource listed by the slides; its contents were not used to write these notes.

Source: [[lecture1-Intro-Course2026-2027.pdf#page=8|Teaching material]].

## Assessment as described in the deck

> [!info] Source and date
> The information below comes from the uploaded 2026–2027 introduction, pp. 9–11. It has not been independently checked against later course announcements.

Evaluation is based on a written exam containing practical problems and open questions about course concepts and techniques. The teacher may complement a written test with an oral examination.

The slides describe two intermediate tests, **November 5** and **December 17**, each contributing up to **16 points**. Admission to the second test does not depend on passing the first.

For partial scores $g_1,g_2$, the stated passing requirements are:

$$
g_1\ge 7,\qquad g_2\ge 7,\qquad g_1+g_2\ge18.
$$

The slide states that a sum greater than 30 receives *30 cum laude*. Partial results remain valid until the end of the academic year or until the student requests to repeat that part. A valid partial result can be retained for a later exam, with a customized paper for the missing part.

Examples applying the stated rule: $7+11$ passes; $6+16$ does not, despite the total; $8+8$ does not meet the total requirement.

Participation in innovative-learning classroom activities may contribute to assessment and allow some written-exam questions to be skipped when the corresponding grades are valid.

Source: [[lecture1-Intro-Course2026-2027.pdf#page=9|Exam format]] · [[lecture1-Intro-Course2026-2027.pdf#page=10|Intermediate tests]] · [[lecture1-Intro-Course2026-2027.pdf#page=11|Classroom activities]].

## Lecturers

The final slide names **Fabrizio Ferrandi** and **Davide Gadioli**, both associated with DEIB. Refer to [[lecture1-Intro-Course2026-2027.pdf#page=12|the original contact slide]] for the listed contact details.

## Takeaways and revision prompts

- The course combines theoretical guarantees with practical implementation constraints.
- Sequential complexity alone does not explain parallel performance.
- The announced syllabus is broader than the six decks currently available.

Try explaining why a theoretically efficient algorithm might perform poorly in practice, and identify which prerequisite topics you need to review before studying [[PRAM]] and [[Randomized Algorithms]].
