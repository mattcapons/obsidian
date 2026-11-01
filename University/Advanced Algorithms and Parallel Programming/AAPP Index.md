---
tags:
  - aapp
  - index
---
# Advanced Algorithms and Parallel Programming

Study collection for the fifteen currently available slide decks (577 PDF pages). Read the notes in lecture order; follow the cross-links when a later lecture reuses an earlier idea. No deck numbered 9 is supplied, so navigation continues from lecture 8 to lecture 10.

## Lectures

| Lecture | Study note | Main topics | Slides |
|---|---|---|---|
| 1 | [[Course Introduction]] | Objectives, syllabus, prerequisites, assessment | [[lecture1-Intro-Course2026-2027.pdf\|Introduction]] |
| 2 | [[Algorithm as recipes]] | Complexity, sorting, asymptotic notation, recurrences | [[lecture2-AlgorithmAsRecipe.pdf\|Algorithms as Recipes]] |
| 3 | [[Divide and Conquer]] | Binary search, exponentiation, matrix multiplication, Strassen, tree layouts | [[lecture3-DandC.pdf\|Divide and Conquer]] |
| 4 | [[PRAM]] | Memory rules, work, cost, speedup, parallel patterns, scaling | [[lecture4-PRAM.pdf\|PRAM]] |
| 4b | [[ISPC]] | SIMD, gangs, uniform/varying data, reductions, tasks | [[lecture4b-ISPC.pdf\|ISPC]] |
| 5 | [[Randomized Algorithms]] | Indicators, hiring problem, Las Vegas, Monte Carlo | [[lecture5-Randomization.pdf\|Randomization]] |
| 6 | [[Minimum Cut]] | Contraction, survival probabilities, amplification, Karger–Stein | [[lecture6-MinCut.pdf\|Minimum cut]] |
| 7 | [[Sorting]] | Randomized quicksort, comparison lower bounds, counting and radix sort | [[lecture7-Sort.pdf\|Sorting]] |
| 8 | [[Selection and Order Statistics]] | Paired extrema, randomized selection, median of medians | [[lecture8-Select-ith.pdf\|Selection]] |
| 10 | [[Primality Testing and Cryptosystems]] | Fermat, strong primality tests, modular powering, RSA, extended Euclid | [[lecture10PrimalityTest.pdf\|Primality and cryptosystems]] |
| 11 | [[Randomized Data Structures]] | Treaps, rotations, split/join, skip lists, probability guarantees | [[lecture11RandomDataStructures.pdf\|Randomized data structures]] |
| 12 | [[Dynamic Programming and LCS]] | Optimal substructure, memoization, LCS tables and reconstruction | [[lezione12DynamicProgramming.pdf\|Dynamic programming and LCS]] |
| 13 | [[Binary Decision Diagrams]] | ROBDDs, unique/computed tables, ITE, ordering, ZBDDs | [[lezione13Dynamic ProgrammingBDD.pdf\|BDDs]] |
| 14 | [[Amortized Analysis]] | Dynamic tables, aggregate, accounting and potential methods | [[lezione14AmortizedAnalysis.pdf\|Amortized analysis]] |
| 15 | [[Competitive Analysis]] | Online/offline models, MTF and inversion potentials, LRU versus MIN paging | [[lezione15CompetitiveAnalysis.pdf\|Competitive analysis]] |

## Study routes

- **Analyze a sequential algorithm:** [[Algorithm as recipes#Asymptotic notation]] → [[Algorithm as recipes#Solving recurrences]] → [[Divide and Conquer#Comparison table]].
- **Understand parallel performance:** [[PRAM#Performance quantities]] → [[PRAM#Reduction]] → [[PRAM#Strong and weak scaling]] → [[ISPC#Two levels of parallelism]].
- **Analyze randomness:** [[Randomized Algorithms#Where randomness comes from]] → [[Randomized Algorithms#Indicator variables]] → [[Randomized Algorithms#The hiring problem]] → [[Randomized Algorithms#Las Vegas and Monte Carlo]].
- **Apply randomized analysis:** [[Randomized Algorithms#Las Vegas and Monte Carlo]] → [[Minimum Cut#Success probability]] → [[Minimum Cut#Karger–Stein]] → [[Sorting#Randomized quicksort]].
- **Understand sorting guarantees:** [[Algorithm as recipes#Sorting and correctness]] → [[Sorting#Quicksort and partitioning]] → [[Sorting#Comparison-sorting lower bound]] → [[Sorting#Counting sort]] → [[Sorting#Radix sort]].
- **Find one rank without sorting:** [[Sorting#Quicksort and partitioning]] → [[Selection and Order Statistics#Randomized selection]] → [[Selection and Order Statistics#Why expected selection time is linear]] → [[Selection and Order Statistics#Deterministic selection with median of medians]].
- **Recognize one-sided error:** [[Randomized Algorithms#One-sided and two-sided error]] → [[Primality Testing and Cryptosystems#Fermat's theorem and pseudoprimes]] → [[Primality Testing and Cryptosystems#Miller–Rabin form and one-sided error]].
- **Maintain an ordered dictionary:** [[Randomized Data Structures#Treaps: a search tree and a priority heap]] → [[Randomized Data Structures#Split and the restricted Union]] → [[Randomized Data Structures#Skip lists: fast lanes over a sorted list]].
- **Reuse overlapping states:** [[Dynamic Programming and LCS#State definition and recurrence]] → [[Dynamic Programming and LCS#Memoization: solve each requested state once]] → [[Binary Decision Diagrams#Unique table and computed table]] → [[Binary Decision Diagrams#The if-then-else operation]].
- **Separate expected and amortized costs:** [[Randomized Data Structures#Comparing guarantees]] → [[Amortized Analysis#Worst-case per operation versus worst-case sequence]] → [[Amortized Analysis#Aggregate method]] → [[Amortized Analysis#Potential method]].
- **Compare an online strategy with offline OPT:** [[Amortized Analysis#Potential method]] → [[Competitive Analysis#Competitive guarantees and the additive constant]] → [[Competitive Analysis#The inversion potential]] → [[Competitive Analysis#Proving paid-model MTF is 4-competitive]] → [[Competitive Analysis#LRU's competitive guarantee]].

## How to use these notes

Course-specific source mapping, conventions, and outstanding gaps: [[University/Advanced Algorithms and Parallel Programming/Course Workflow|Course Workflow]].

Reusable workflows: [[Study Note Prompts#Build and enhance a course collection|build notes for another course]] · [[Study Note Prompts#Continue when new slides arrive|add new slide material]].

1. Read an explanation and reproduce its worked example without looking.
2. For each algorithm, identify the input, correctness argument, cost model, and complexity.
3. Use the revision questions to test whether you can explain the result, rather than only recall its formula.
4. Open the linked PDF pages for the original diagrams and code.

The explanations now include intermediate reasoning, round-by-round and lane-by-lane traces, and additional local diagrams. In particular, [[PRAM#Tracing the doubling scan]], [[ISPC#What the manual shuffle reduction actually changes]], and [[Sorting#Expanding the expected recurrence for four keys]] unpack steps that were previously compressed.

The notes consolidate repeated slides. Supplementary explanations and apparent slide errors are labeled explicitly. Revision questions include short answers at the end of each technical note.

## Exam practice and review

The notes have been reviewed against the supplied slides and checked with selected university materials and official documentation. Added explanations remain tied to the existing deck topics; citations appear beside the claims they support. Course administration still follows the uploaded introduction.

- [[Algorithm as recipes#Exam practice]] — sorting traces and recurrence-case selection.
- [[Divide and Conquer#Exam practice]] — recursion reuse and H-tree dimensions.
- [[PRAM#Exam practice]] — operation counts and sequential-baseline choices.
- [[ISPC#Exam practice]] — active-lane reductions and gang/task distinctions.
- [[Randomized Algorithms#Exam practice]] — expected hiring cost and sampling budgets.
- [[Minimum Cut#Exam practice]] — edge sampling, amplification budgets, recursion termination.
- [[Sorting#Exam practice]] — partition traces, expected comparisons, stability, radix cost models.
- [[Selection and Order Statistics#Exam practice]] — local ranks, exact comparison counts and two selection guarantees.
- [[Primality Testing and Cryptosystems#Exam practice]] — witnesses, error budgets, input length and modular inverses.
- [[Randomized Data Structures#Exam practice]] — treap construction, rotations, join and promotion probabilities.
- [[Dynamic Programming and LCS#Exam practice]] — tables, reconstruction, memoized states and space claims.
- [[Binary Decision Diagrams#Exam practice]] — reduction, caching, ordered composition and ZDD semantics.
- [[Amortized Analysis#Exam practice]] — exact prefix costs, potentials and allocation models.
- [[Competitive Analysis#Exam practice]] — list-update cost models, inversion accounting, startup terms, paging traces and online decisions.

The worked problems are original practice, not retrieved past-paper questions. The fifteen decks establish the current slide collection's boundaries; they do not establish that every announced exam topic has already been supplied. The introduction explicitly excludes CUDA from the current syllabus even though historical CUDA questions remain in the bank.

## Topics announced but not yet supplied

Selection, primality/cryptosystems, treaps/skip lists, LCS, BDDs, dynamic-table amortization, and competitive/online methods now have dedicated notes. [[Competitive Analysis]] covers move-to-front and LRU versus offline MIN, including the paid/free list models and the distinct paging guarantee. Still awaiting lecture-specific decks for approximation, further string-matching topics, and the broader parallel tools and patterns announced by the introduction. The bank also contains disjoint-set and other questions beyond the currently supplied slide topics. A related note link does not certify complete coverage of every historical question.

## Local notebooks

Five notebook files are present: [[lecture3-DandC-profiling.ipynb]], [[01_pram_reduction_prefix_sum.ipynb]], [[02_amdahl_gustafson_scaling.ipynb]], [[03_strong_weak_scaling.ipynb]], and [[04_ispc.ipynb]]. They have not been executed in this slide-note update; see [[Course Workflow#Current gaps and scope — 2026-11-01|current verification limits]].

## Past exams

[[Past Exam Question Bank]] — 552 questions from 58 distinct 2022–2026 exam papers, grouped by topic, with original exam references, code, and diagrams. The bank's current entries and IDs are preserved; new lecture links provide study context.

[[Exam Recap]] — a growing revision companion with the same 25 topic sections as the bank. Sections 1–5 currently consolidate 114 reviewed questions on PRAM, parallel performance and scaling, divide and conquer/recurrences, and randomized algorithm classes, with short reminders emphasizing corrected mistakes and recent exams; the remaining sections are ready for later expansion.
