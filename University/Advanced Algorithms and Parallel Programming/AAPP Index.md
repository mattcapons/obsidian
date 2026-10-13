---
tags:
  - aapp
  - index
---
# Advanced Algorithms and Parallel Programming

Study collection for the eight currently available slide decks. Read the notes in lecture order; follow the cross-links when a later lecture reuses an earlier idea.

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

## Study routes

- **Analyze a sequential algorithm:** [[Algorithm as recipes#Asymptotic notation]] → [[Algorithm as recipes#Solving recurrences]] → [[Divide and Conquer#Comparison table]].
- **Understand parallel performance:** [[PRAM#Performance quantities]] → [[PRAM#Reduction]] → [[PRAM#Strong and weak scaling]] → [[ISPC#Two levels of parallelism]].
- **Analyze randomness:** [[Randomized Algorithms#Where randomness comes from]] → [[Randomized Algorithms#Indicator variables]] → [[Randomized Algorithms#The hiring problem]] → [[Randomized Algorithms#Las Vegas and Monte Carlo]].
- **Apply randomized analysis:** [[Randomized Algorithms#Las Vegas and Monte Carlo]] → [[Minimum Cut#Success probability]] → [[Minimum Cut#Karger–Stein]] → [[Sorting#Randomized quicksort]].
- **Understand sorting guarantees:** [[Algorithm as recipes#Sorting and correctness]] → [[Sorting#Quicksort and partitioning]] → [[Sorting#Comparison-sorting lower bound]] → [[Sorting#Counting sort]] → [[Sorting#Radix sort]].

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

The worked problems are original practice, not retrieved past-paper questions. The eight decks establish the current collection's boundaries; they do not establish that every announced exam topic has already been supplied.

## Topics announced but not yet supplied

The introduction also announces selection/order statistics, primality testing, cryptosystems, skip lists and treaps, dynamic programming, amortized and approximation methods, competitive analysis, and further parallel programming tools and patterns. These need additional decks before lecture-specific notes can be added. Randomized quicksort and Karger/Karger–Stein min-cut are now covered by lectures 7 and 6 respectively; lecture 7 does not supply a selection algorithm.
