---
tags:
  - aapp
  - exam-practice
  - question-bank
status: unanswered
created: 2026-10-15
---
# AAPP — Past Exam Question Bank

[[AAPP Index|Course index]]

Questions collected from the supplied 2022–2025 exams, grouped by subject for revision and future reference answers. **No answers or newly generated questions are included.**

> [!info] How to use this bank
> Each entry has a stable question ID and an original exam/page reference. Answer with reasoning: the exams repeatedly state that an unsupported answer is invalid. Keep the ID when adding a future answer or requesting similar practice. Points in parentheses are the original marks where available.

## Contents

- [[#PRAM model and memory rules]] — 29 questions
- [[#Parallel performance and scaling]] — 32 questions
- [[#PRAM algorithms]] — 6 questions
- [[#Divide and conquer and recurrences]] — 16 questions
- [[#Randomized algorithm classes]] — 5 questions
- [[#Minimum cut]] — 9 questions
- [[#Sorting and partitioning]] — 14 questions
- [[#Selection and order statistics]] — 9 questions
- [[#Primality testing]] — 3 questions
- [[#Dynamic programming and LCS]] — 14 questions
- [[#BDDs and memoization]] — 9 questions
- [[#Treaps]] — 14 questions
- [[#Skip lists]] — 8 questions
- [[#Disjoint sets]] — 2 questions
- [[#Amortized analysis]] — 16 questions
- [[#Online algorithms and competitive analysis]] — 10 questions
- [[#Parallel design and architectures]] — 12 questions
- [[#Dependences and loop parallelization]] — 33 questions
- [[#Parallel patterns]] — 49 questions
- [[#Task graphs and OpenMP implementations]] — 11 questions
- [[#OpenMP]] — 38 questions
- [[#Pthreads and shared-memory synchronization]] — 18 questions
- [[#MPI]] — 52 questions
- [[#CUDA]] — 8 questions
- [[#Halide and high-level synthesis]] — 5 questions

## Editorial conventions

- Repeated questions with identical extracted wording are listed once with all their sources; distinct wording and technical variants are retained. Questions in the 2022 A/B papers are therefore combined only when their wording matches.
- Original exercise/subquestion labels, requirements, numerical values, and code are preserved. Blank answer lines, cover instructions, and challenge-based exemptions are omitted. A multi-part prompt without separate letter labels remains one entry.
- Page links use physical PDF pages. Embedded source pages retain task graphs, task weights, and cancellation timelines that plain text cannot capture. Some diagrams are shared by several entries.
- Source filenames identify exam sessions. Some PDFs contain copied footers with a different date; follow the linked source rather than treating a footer as a separate exam.
- Wording, claims to discuss, and apparent source errors are left as questions, not corrected into answers. In particular, check the bounds and increment in the September 2025 loop exactly as printed.
- Links to existing notes indicate related study material, not a guarantee that every question is already covered. Topics without a dedicated note remain included.

> [!warning] Future answer pass
> Use the course notes and source PDFs to answer each ID when requested. Preserve assumptions and distinguish expected, worst-case, and amortized bounds. Where material is still missing, mark the answer as pending rather than inventing a course-specific explanation.

## PRAM model and memory rules

Related notes: [[PRAM]].

### AAPP-01-001

Describe the main characteristics of a PRAM model. (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=2|2022-11-08-1st · Exercise 1A · p. 2]]

^aapp-01-001

### AAPP-01-002

Please describe the type of Read/Write abilities a PRAM may have. (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1B · p. 2]]

^aapp-01-002

### AAPP-01-003

Please define a PRAM. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1A · p. 2]]

^aapp-01-003

### AAPP-01-004

Please describe what “Common CRCW” means. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1B · p. 2]]

^aapp-01-004

### AAPP-01-005

Please define the different phases followed in a PRAM computation. (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1A · p. 2]]

^aapp-01-005

### AAPP-01-006

Please describe what “Arbitrary CW” means. (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1B · p. 2]]

^aapp-01-006

### AAPP-01-007

How the time complexity in a PRAM model is computed? (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1A · p. 2]]

^aapp-01-007

### AAPP-01-008

How is the communication via shared memory performed in a PRAM model? (latency vs parallel accesses) (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1B · p. 2]]

^aapp-01-008

### AAPP-01-009

Discuss the following sentence: “If a problem has no feasible/efficient solution on PRAM, it has no feasible/efficient solution for any parallel machine.” True or False? (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1C · p. 2]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1C · p. 2]]

^aapp-01-009

### AAPP-01-010

Which of the PRAM model’s assumptions help to compute the time complexity? (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1A · p. 2]]

^aapp-01-010

### AAPP-01-011

Which of the assumptions of the PRAM model simplifies the communication between processor and memory? (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1B · p. 2]]

^aapp-01-011

### AAPP-01-012

Please define when a write conflict occurs in a PRAM model. (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1C · p. 2]]

^aapp-01-012

### AAPP-01-013

Explain why, in the PRAM model, the number of instructions executed is used as time complexity. (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=2|2023-11-09-1st · Exercise 1A · p. 2]]

^aapp-01-013

### AAPP-01-014

Please discuss the following sentence: “In a PRAM model, processors do not have private local memories”. True/False? (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1A · p. 2]]

^aapp-01-014

### AAPP-01-015

Please provide an example of a PRAM application relying on a Common CW policy. (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1C · p. 2]]

^aapp-01-015

### AAPP-01-016

Are PRAM architectures using explicit or implicit synchronizations? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1A · p. 2]]

^aapp-01-016

### AAPP-01-017

Explain the factors that simplify the computation of space complexity in a PRAM application, giving them in order of priority. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1A · p. 2]]

^aapp-01-017

### AAPP-01-018

Please describe an example of Common CRCW with a PRAM model. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1D · p. 2]]

^aapp-01-018

### AAPP-01-019

Explain the factors that simplify the computation of time complexity in a PRAM application, giving them in order of priority. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1A · p. 2]]

^aapp-01-019

### AAPP-01-020

Please describe what happens in a PRAM model when the number of threads exceeds the number of processors. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1D · p. 2]]

^aapp-01-020

### AAPP-01-021

“In a PRAM model, synchronization primitives are not required when data is exchanged through the shared memory.” True/False? Why? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1A · p. 2]]

^aapp-01-021

### AAPP-01-022

In a PRAM model, “all processors can access all memory cells in unit time. Could you please provide a detailed explanation of the implications of this assumption? (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1A · p. 2]]

^aapp-01-022

### AAPP-01-023

What can be said about the time complexity of a PRAM-based application when the PRAM model has a bounded number of processors? (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1A · p. 2]]

^aapp-01-023

### AAPP-01-024

How is the communication via shared memory performed in a PRAM model? (latency vs parallel accesses)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1B · p. 2]]

^aapp-01-024

### AAPP-01-025

How does the PRAM model abstract away synchronization and communication, and what are the implications for algorithm design? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1A · p. 2]]

^aapp-01-025

### AAPP-01-026

How do the different types of concurrent write (CW) models affect algorithm design in PRAM? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1B · p. 2]]

^aapp-01-026

### AAPP-01-027

What does it imply that each memory cell can hold an integer of unbounded size in a PRAM? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1A · p. 2]]

^aapp-01-027

### AAPP-01-028

What kind of synchronization does PRAM use? (1)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1A · p. 2]]

^aapp-01-028

### AAPP-01-029

Which of the assumptions of the PRAM model simplifies the communication between the processor and the memory? (1)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1B · p. 2]]

^aapp-01-029

## Parallel performance and scaling

Related notes: [[PRAM]].

### AAPP-02-001

Define the speedup when a sequential code is accelerated with p processors. (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=2|2022-11-08-1st · Exercise 1B · p. 2]]

^aapp-02-001

### AAPP-02-002

Please describe the differences between the Amdahl and the Gustafson laws. (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=2|2022-11-08-1st · Exercise 1C · p. 2]]

^aapp-02-002

### AAPP-02-003

Gustafson says that the Amdahl law is wrong. True/False? Why? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1D · p. 2]]

^aapp-02-003

### AAPP-02-004

Please define the speed-up of a parallel algorithm according to the PRAM model (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1C · p. 2]]

^aapp-02-004

### AAPP-02-005

Please describe how Gustafson defines the speed-up. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=2|2023-02-14-1st · Exercise 1D · p. 2]]

^aapp-02-005

### AAPP-02-006

Please define the efficiency of a parallel algorithm according to the PRAM model (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1C · p. 2]]

^aapp-02-006

### AAPP-02-007

Please compare the assumptions behind the Gustafson and the Amdahl laws. (1)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=2|2023-06-19-1st · Exercise 1D · p. 2]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=2|2025-09-05-1st · Exercise 1D · p. 2]]

^aapp-02-007

### AAPP-02-008

Define the “work” in a PRAM model. (1)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=2|2023-07-11-1st · Exercise 1D · p. 2]]

^aapp-02-008

### AAPP-02-009

Define the “cost” in a PRAM model. (1)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=2|2023-09-11-1st · Exercise 1D · p. 2]]

^aapp-02-009

### AAPP-02-010

Define the cost C when a sequential code is accelerated with p processors. (1)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=2|2023-11-09-1st · Exercise 1B · p. 2]]

^aapp-02-010

### AAPP-02-011

What is it meant with a fixed time model? Is it referring to Gustafson or Amdahl’s law? (1)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=2|2023-11-09-1st · Exercise 1C · p. 2]]

^aapp-02-011

### AAPP-02-012

Please define what is meant by “Efficiency” in a PRAM application. (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1B · p. 2]]

^aapp-02-012

### AAPP-02-013

Please relate the strong scaling vs the weak scaling to the Amdahl vs Gustafson laws. (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=2|2024-01-26-1st · Exercise 1D · p. 2]]

^aapp-02-013

### AAPP-02-014

Please define what is meant by “Speed up” in a PRAM application. (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1B · p. 2]]

^aapp-02-014

### AAPP-02-015

Is the Amdahl law a fixed-time model? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1D · p. 2]]

^aapp-02-015

### AAPP-02-016

Please define what is meant by “Work” in a PRAM application. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1B · p. 2]]

^aapp-02-016

### AAPP-02-017

Please define what “Cost” means in a PRAM application. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1B · p. 2]]

^aapp-02-017

### AAPP-02-018

In a PRAM, 𝑝𝐸𝑝(𝑛) is equal to the application speed-up? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=2|2024-09-05-1st · Exercise 1A · p. 2]]

^aapp-02-018

### AAPP-02-019

What happens to the PRAM model if we have a bounded number of processors smaller than the one required by the theoretical model? What happens to the speed-up if the application is a do-all kind of application and we have a bounded number of processors? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=2|2024-09-05-1st · Exercise 1B · p. 2]]

^aapp-02-019

### AAPP-02-020

Could you please discuss the following sentence? “Amdahl's law presupposes that the computing requirements will stay the same, given increased processing power. In other words, an analysis of the same data will take less time given more computing power“. Is it true or false? What does it mean? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=2|2024-09-05-1st · Exercise 1C · p. 2]]

^aapp-02-020

### AAPP-02-021

Please show the formula defining the “Efficiency” in a PRAM model. (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1B · p. 2]]

^aapp-02-021

### AAPP-02-022

Can you provide an example where the “work” done by a parallel PRAM program exceeds that of the sequential version of the same algorithm? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1C · p. 2]]

^aapp-02-022

### AAPP-02-023

What does it mean fixed-size model? Does it refer to Gustafson or Amdahl’s law? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=2|2024-11-12-1st · Exercise 1D · p. 2]]

^aapp-02-023

### AAPP-02-024

Could you please elaborate on the conditions under which the following formula holds as an equality and when it holds as an inequality: SUp ≤ p?"

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1B · p. 2]]

^aapp-02-024

### AAPP-02-025

Could you please elaborate on what “weak scaling” means? To which law we have seen during the lectures is referring to? (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1C · p. 2]]

^aapp-02-025

### AAPP-02-026

Please describe the speed-up when a fixed-size model is considered. (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=2|2025-01-24-1st · Exercise 1D · p. 2]]

^aapp-02-026

### AAPP-02-027

Could you please discuss the differences between “weak scaling” and “strong scaling”? To which laws we have seen during the lectures are referring to? (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1C · p. 2]]

^aapp-02-027

### AAPP-02-028

Please define and discuss the speed-up when Gustafson’s law is considered. (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=2|2025-02-14-1st · Exercise 1D · p. 2]]

^aapp-02-028

### AAPP-02-029

How does the matrix-vector multiplication example illustrate strong scaling, and what would change in a weak scaling scenario? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1C · p. 2]]

^aapp-02-029

### AAPP-02-030

Why does Amdahl’s Law suggest diminishing returns with increasing processors, and how does Gustafson’s Law counter this? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=2|2025-06-05-1st · Exercise 1D · p. 2]]

^aapp-02-030

### AAPP-02-031

Given an algorithm with $T_1(n)=n^3$ and $T_p(n)=n^3/p$, analyze the speedup and efficiency. What can you conclude? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1B · p. 2]]

^aapp-02-031

### AAPP-02-032

How does Gustafson’s Law support the concept of weak scaling, and what is its implication for massively parallel systems? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1D · p. 2]]

^aapp-02-032

## PRAM algorithms

Related notes: [[PRAM]].

### AAPP-03-001

Please describe the matrix multiply algorithm on PRAM (Pseudo code. Complexity). (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1A · p. 2]]

^aapp-03-001

### AAPP-03-002

The PRAM algorithm computing the prefix sum of a vector uses concurrent reads. True/False? Where? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=2|2023-01-17-1st · Exercise 1C · p. 2]]

^aapp-03-002

### AAPP-03-003

Please describe how prefix scan works when a PRAM architecture is considered. (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=2|2024-02-16-1st · Exercise 1C · p. 2]]

^aapp-03-003

### AAPP-03-004

Please describe how matrix x vector works when a PRAM architecture is considered. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=2|2024-06-26-1st · Exercise 1C · p. 2]]

^aapp-03-004

### AAPP-03-005

Please describe how matrix x matrix works when considering a PRAM architecture. (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=2|2024-07-24-1st · Exercise 1C · p. 2]]

^aapp-03-005

### AAPP-03-006

Why is the prefix sum algorithm on PRAM more efficient than the basic sum algorithm, and what is the trade-off? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=2|2025-07-04-1st · Exercise 1C · p. 2]]

^aapp-03-006

## Divide and conquer and recurrences

Related notes: [[Divide and Conquer]].

### AAPP-04-001

Describe how divide and conquer work with some examples and why master theorem method matter.

Source: [[Tema Esame 2022-06-09-1st.pdf#page=2|2022-06-09-1st · Exercise 1 · p. 2]]

^aapp-04-001

### AAPP-04-002

Please describe how the Divide and Conquer class of algorithms works. (2)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=3|2023-02-14-1st · Exercise 2A · p. 3]]

^aapp-04-002

### AAPP-04-003

How the complexity of a Divide and Conquer algorithm can be computed? (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=3|2023-02-14-1st · Exercise 2B · p. 3]]

^aapp-04-003

### AAPP-04-004

Please discuss the complexity of the “Powering a number” algorithm. (1)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=3|2023-02-14-1st · Exercise 2C · p. 3]]

^aapp-04-004

### AAPP-04-005

Please describe how Strassen’s algorithm works. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=3|2023-06-19-1st · Exercise 2A · p. 3]]

^aapp-04-005

### AAPP-04-006

Why is the Master Theorem method frequently used to evaluate the asymptotic complexity of a Divide and Conquer algorithm can be computed? (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=3|2023-06-19-1st · Exercise 2B · p. 3]]

^aapp-04-006

### AAPP-04-007

Please discuss how the complexity of the powering of a number algorithm can be computed. Please report also the complexity in terms of time and space. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=3|2023-07-11-1st · Exercise 2A · p. 3]]

^aapp-04-007

### AAPP-04-008

Please discuss the cases the master theorem solves and under which assumption the theorem holds. Apply then to the binary search algorithm. Is the master theorem of any help in case we would like to estimate the spatial complexity of an algorithm? (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=3|2023-09-11-1st · Exercise 2A · p. 3]]

^aapp-04-008

### AAPP-04-009

Please describe the divide and conquer powering of a number algorithm. What complexity does it have? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=3|2024-02-16-1st · Exercise 2C · p. 3]]

^aapp-04-009

### AAPP-04-010

Please list the condition under which the Master Theorem can be used to compute the complexity of an algorithm. (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=3|2024-06-26-1st · Exercise 2C · p. 3]]

^aapp-04-010

### AAPP-04-011

Please discuss the cases the master theorem solves and under which assumption the theorem holds. Apply then to the powering algorithm. Is the master theorem of any help if we would like to estimate the spatial complexity of an algorithm? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=3|2024-07-24-1st · Exercise 2A · p. 3]]

^aapp-04-011

### AAPP-04-012

Please discuss the types of problems that the master theorem can solve and the assumptions under which the theorem holds. Apply the theorem to the matrix multiplication algorithm and explain why Strassen’s version is more efficient. (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=3|2024-09-05-1st · Exercise 2A · p. 3]]

^aapp-04-012

### AAPP-04-013

Master Theorem method is an important tool for the Divide and Conquer class of algorithms. Why and under which assumptions the theorem could be applied? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=3|2024-11-12-1st · Exercise 2B · p. 3]]

^aapp-04-013

### AAPP-04-014

Could you please describe how the Strassen algorithm improves matrix multiplication? Additionally, which class of algorithms does the Strassen approach belong to? (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=3|2025-01-24-1st · Exercise 2A · p. 3]]

^aapp-04-014

### AAPP-04-015

Could you please describe how the powering algorithm works? Additionally, which class of algorithms does it belong to? (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=3|2025-02-14-1st · Exercise 2A · p. 3]]

^aapp-04-015

### AAPP-04-016

Please describe how the Divide and Conquer class of algorithms works by using one of the algorithms presented in class. (2)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=3|2025-09-05-1st · Exercise 2A · p. 3]]

^aapp-04-016

## Randomized algorithm classes

Related notes: [[Randomized Algorithms]].

### AAPP-05-001

Explain the difference between Monte Carlo and Las Vegas Randomized based algorithms.

Source: [[Tema Esame 2022-01-14-1st.pdf#page=4|2022-01-14-1st · Exercise 3 · p. 4]]

^aapp-05-001

### AAPP-05-002

Please define when Las Vegas and Monte Carlo algorithms are defined as efficient algorithms. (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=3|2024-02-16-1st · Exercise 2A · p. 3]]

^aapp-05-002

### AAPP-05-003

Please list the main differences between the Las Vegas and Monte Carlo algorithms. (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=3|2024-06-26-1st · Exercise 2A · p. 3]]

^aapp-05-003

### AAPP-05-004

Please describe the differences between Las Vegas and Monte Carlo algorithms, even considering time complexity issues. (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=4|2024-11-12-1st · Exercise 3A · p. 4]]

^aapp-05-004

### AAPP-05-005

Please list the main differences, including the efficiency, between the Las Vegas and Monte Carlo algorithms. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=3|2025-07-04-1st · Exercise 2B · p. 3]]

^aapp-05-005

## Minimum cut

Related notes: [[Minimum Cut]].

### AAPP-06-001

Describe how Karger and Stein algorithm works. Discuss and compare the two algorithms’ complexity.

Source: [[Tema Esame 2022-01-14-1st.pdf#page=3|2022-01-14-1st · Exercise 2 · p. 3]]

^aapp-06-001

### AAPP-06-002

Describe the Karger’s Min-Cut Algorithm. Is the Karger’s Min-Cut Algorithm a Monte Carlo randomization- based algorithm?

Source: [[Tema Esame 2022-02-11-1st.pdf#page=3|2022-02-11-1st · Exercise 2 · p. 3]]

^aapp-06-002

### AAPP-06-003

Describe the Karger and Stein Min-Cut Algorithm. How is the complexity of this algorithm computed? Which is the randomization class the algorithm belongs to?

Source: [[Tema Esame 2022-09-07-1st.pdf#page=2|2022-09-07-1st · Exercise 1 · p. 2]]

^aapp-06-003

### AAPP-06-004

Describe the Karger and Stein algorithm and its complexity. (2)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=4|2023-01-17-1st · Exercise 3B · p. 4]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=4|2025-09-05-1st · Exercise 3B · p. 4]]

^aapp-06-004

### AAPP-06-005

What are the key differences between Karger vs Karger&Steing algorithms? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=5|2024-02-16-1st · Exercise 4A · p. 5]]

^aapp-06-005

### AAPP-06-006

Please describe the key properties of the Karger & Stein algorithm. (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=4|2024-06-26-1st · Exercise 3B · p. 4]]

^aapp-06-006

### AAPP-06-007

Please describe the ideas used to improve the Karger approach to solving the min-cut problem. What changed with respect to the asymptotic complexity with respect to the initial approach? (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=3|2024-11-12-1st · Exercise 2A · p. 3]]

^aapp-06-007

### AAPP-06-008

What are the key ideas of the basic Karger approach compared to previous approaches? Does it affect the worst-case complexity?" (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=4|2025-01-24-1st · Exercise 3A · p. 4]]

^aapp-06-008

### AAPP-06-009

In class, we studied two algorithms for minimum cut in a graph. Describe the behavior of both algorithms, including their algorithmic class and complexity. Based on the discussion held in class, explain why one might be preferable over the other. (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=3|2025-06-05-1st · Exercise 2A · p. 3]]

^aapp-06-009

## Sorting and partitioning

Related notes: [[Sorting]].

### AAPP-07-001

Discuss counting sort complexity. Why does counting sort matter in radix sort?

Source: [[Tema Esame 2022-02-11-1st.pdf#page=4|2022-02-11-1st · Exercise 3 · p. 4]]

^aapp-07-001

### AAPP-07-002

The best worst-case running time that we have seen for comparison sorting is O(nlg n). Can you explain why? (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=3|2023-07-11-1st · Exercise 2B · p. 3]]

^aapp-07-002

### AAPP-07-003

Please explain following theorem and why does not hold for the counting sort algorithm: Theorem: “Any decision tree that can sort n elements must have height W(nlg n)” (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=3|2023-09-11-1st · Exercise 2B · p. 3]]

^aapp-07-003

### AAPP-07-004

Please explain the following theorem and why does not hold for the counting sort algorithm: Theorem: “Any decision tree that can sort n elements must have a height of W(nlog n)” (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=5|2023-11-09-1st · Exercise 4A · p. 5]]

^aapp-07-004

### AAPP-07-005

What are the key properties that the auxiliary sorting algorithm used by the radix sort must have to achieve efficient and correct sorting? (1)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=3|2024-02-16-1st · Exercise 2B · p. 3]]

^aapp-07-005

### AAPP-07-006

What are the key properties of the counting sort algorithm? (1)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=3|2024-06-26-1st · Exercise 2B · p. 3]]

^aapp-07-006

### AAPP-07-007

Please describe the partitioning algorithm used by the quick sort and its key properties. How is it randomized? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=3|2024-09-05-1st · Exercise 2B · p. 3]]
Source: [[Tema Esame 2025-07-04-1st.pdf#page=5|2025-07-04-1st · Exercise 4A · p. 5]]

^aapp-07-007

### AAPP-07-008

Please explain what “Lower bound for comparison sorting” means and its implications. (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=5|2024-11-12-1st · Exercise 4A · p. 5]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=5|2025-09-05-1st · Exercise 4C · p. 5]]

^aapp-07-008

### AAPP-07-009

Please show the pseudo-code of the partitioning algorithm used by Quicksort and report its variants, complexity, and usage in other algorithms. (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=5|2024-11-12-1st · Exercise 4B · p. 5]]

^aapp-07-009

### AAPP-07-010

Why is the Counting sort used as the auxiliary algorithm of the Radix sort? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=5|2024-11-12-1st · Exercise 4C · p. 5]]

^aapp-07-010

### AAPP-07-011

Please discuss the complexity of the partitioning algorithm used by the quick sort. (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=5|2025-01-24-1st · Exercise 4A · p. 5]]

^aapp-07-011

### AAPP-07-012

Please discuss the lower bound of the comparison-based sort algorithms. (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=5|2025-02-14-1st · Exercise 4A · p. 5]]

^aapp-07-012

### AAPP-07-013

Could you please list the characteristics of the counting sort algorithm that make it suitable for use in radix sort? (1)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=5|2025-02-14-1st · Exercise 4C · p. 5]]

^aapp-07-013

### AAPP-07-014

Why does quicksort perform poorly in the worst case, and how can this be mitigated? Report the class of algorithms to which it belongs and its average-case complexity. According to the definition, is it an efficient algorithm? (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=4|2025-06-05-1st · Exercise 3A · p. 4]]

^aapp-07-014

## Selection and order statistics

*No dedicated study note is currently available for this topic.*

### AAPP-08-001

Describe how the randomized select-ith method work. Is it a Monte Carlo randomization-based algorithm?

Source: [[Tema Esame 2022-06-09-1st.pdf#page=3|2022-06-09-1st · Exercise 2 · p. 3]]

^aapp-08-001

### AAPP-08-002

Describe the algorithm selecting the ith smallest of n elements (Pseudo code, complexity). (2)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=3|2023-01-17-1st · Exercise 2A · p. 3]]

^aapp-08-002

### AAPP-08-003

Is there a Select ith smallest of n elements algorithm that runs in linear time in the worst case? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=3|2023-01-17-1st · Exercise 2B · p. 3]]

^aapp-08-003

### AAPP-08-004

Context: Exercise 2A asks for the algorithm selecting the ith smallest of n elements (pseudocode and complexity). In which class of randomized algorithms could the algorithm described in A be inserted? (1)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=3|2023-01-17-1st · Exercise 2C · p. 3]]

^aapp-08-004

### AAPP-08-005

Please describe how the partitioning work in the “Select the ith smallest of n elements” algorithm. How is it randomized? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=3|2024-01-26-1st · Exercise 2A · p. 3]]

^aapp-08-005

### AAPP-08-006

Please describe the “Select the i th smallest of n elements” algorithm and its key properties. How is it randomized? (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=3|2024-07-24-1st · Exercise 2B · p. 3]]

^aapp-08-006

### AAPP-08-007

Please discuss the different variants of the Select-ith algorithm. (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=5|2025-01-24-1st · Exercise 4B · p. 5]]

^aapp-08-007

### AAPP-08-008

Describe the Select-ith deterministic algorithm and its complexity. Why is dividing into groups of 5 critical for the deterministic Select-ith algorithm’s performance? (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=5|2025-06-05-1st · Exercise 4B · p. 5]]

^aapp-08-008

### AAPP-08-009

What are the differences between the randomized and deterministic algorithms for solving the Select-ith problem? (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=5|2025-07-04-1st · Exercise 4B · p. 5]]

^aapp-08-009

## Primality testing

*No dedicated study note is currently available for this topic.*

### AAPP-09-001

Which is the type/class of randomized algorithms used by the primality testing algorithms presented during the lectures? (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=3|2024-01-26-1st · Exercise 2C · p. 3]]

^aapp-09-001

### AAPP-09-002

Describe the ideas behind the primality test algorithm presented during the lectures. Which class of randomized approach does it belong to? (1)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=5|2025-01-24-1st · Exercise 4C · p. 5]]

^aapp-09-002

### AAPP-09-003

Could you explain which aspects of primality testing use randomization and how that process works? Additionally, would you classify it as a Las Vegas randomized algorithm? (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=4|2025-02-14-1st · Exercise 3A · p. 4]]

^aapp-09-003

## Dynamic programming and LCS

*No dedicated study note is currently available for this topic.*

### AAPP-10-001

Discuss why dynamic programming matter for Longest common subsequence algorithm.

Source: [[Tema Esame 2022-01-14-1st.pdf#page=2|2022-01-14-1st · Exercise 1 · p. 2]]

^aapp-10-001

### AAPP-10-002

Discuss an example of dynamic programming based algorithm. Which are the key features of an algorithm for being classified as a dynamic programming algorithm?

Source: [[Tema Esame 2022-09-07-1st.pdf#page=3|2022-09-07-1st · Exercise 2 · p. 3]]

^aapp-10-002

### AAPP-10-003

Describe the Longest Common Subsequence (LCS) algorithm. (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=3|2022-11-08-1st · Exercise 2A · p. 3]]

^aapp-10-003

### AAPP-10-004

What kind of temporal or spatial complexity has LCS? (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=3|2022-11-08-1st · Exercise 2B · p. 3]]

^aapp-10-004

### AAPP-10-005

LCS is classified as a dynamic programming algorithm. Why? (1)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=3|2022-11-08-1st · Exercise 2C · p. 3]]

^aapp-10-005

### AAPP-10-006

Please explain why an algorithm could be classified as a Dynamic programming algorithm. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=4|2023-06-19-1st · Exercise 3A · p. 4]]

^aapp-10-006

### AAPP-10-007

Detail the Longest Common Subsequence algorithm: pseudo code and space and temporal complexity. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=5|2023-07-11-1st · Exercise 4A · p. 5]]

^aapp-10-007

### AAPP-10-008

What kind of spatial complexity has the longest common subsequence problem? (1).

Source: [[Tema Esame 2023-11-09-1st.pdf#page=3|2023-11-09-1st · Exercise 2B · p. 3]]

^aapp-10-008

### AAPP-10-009

Why does spatial complexity matter for all dynamic programming algorithms? (1)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=3|2023-11-09-1st · Exercise 2C · p. 3]]

^aapp-10-009

### AAPP-10-010

What kind of time complexity has the longest common subsequence problem (1)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=3|2024-01-26-1st · Exercise 2B · p. 3]]

^aapp-10-010

### AAPP-10-011

Please discuss how the longest common subsequence works. What about its complexity? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=4|2024-02-16-1st · Exercise 3A · p. 4]]

^aapp-10-011

### AAPP-10-012

Please discuss the key property of the longest common subsequence. In which class of algorithm can be inserted? Why? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=5|2024-07-24-1st · Exercise 4A · p. 5]]

^aapp-10-012

### AAPP-10-013

To which class does the Longest Common Subsequence Algorithm belong? How is its complexity evaluated? (1)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=3|2024-09-05-1st · Exercise 2C · p. 3]]

^aapp-10-013

### AAPP-10-014

In class, we studied an algorithm that shows the main hallmarks of dynamic programming. Describe the algorithm and its complexity, and why it is classified as a good dynamic programming example. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=3|2025-07-04-1st · Exercise 2A · p. 3]]

^aapp-10-014

## BDDs and memoization

*No dedicated study note is currently available for this topic.*

### AAPP-11-001

Please explain what the memoization technique is meant for and where it matters. (2)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=4|2023-02-14-1st · Exercise 3A · p. 4]]
Source: [[Tema Esame 2025-09-05-1st.pdf#page=4|2025-09-05-1st · Exercise 3A · p. 4]]

^aapp-11-001

### AAPP-11-002

Why the BDD data structure can be classified as an example of dynamic programming. (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=3|2023-11-09-1st · Exercise 2A · p. 3]]

^aapp-11-002

### AAPP-11-003

Please explain the differences between “Computed table” and “Unique table” with BDDs. Why are they used? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=5|2024-01-26-1st · Exercise 4B · p. 5]]

^aapp-11-003

### AAPP-11-004

What is the Unique Table, and what is it used for in ROBDDs? Does it also have to do with the canonicity of ROBDD? (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=5|2024-06-26-1st · Exercise 4A · p. 5]]

^aapp-11-004

### AAPP-11-005

What is the Computed Table, and what is it used for in ROBDDs? Does it also have to do with the canonicity of ROBDD? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=5|2024-09-05-1st · Exercise 4B · p. 5]]

^aapp-11-005

### AAPP-11-006

What is meant by the memoization technique, and in which class of algorithm does it matter? (1)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=3|2024-11-12-1st · Exercise 2C · p. 3]]

^aapp-11-006

### AAPP-11-007

"Why can BDD be considered an example of a data structure that exploits dynamic programming? How does asymptotic complexity change with memoization?" (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=3|2025-01-24-1st · Exercise 2B · p. 3]]

^aapp-11-007

### AAPP-11-008

Please discuss the role of the computed table on BDD ITE operation. How does the ITE asymptotic complexity change with this table?" (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=3|2025-02-14-1st · Exercise 2B · p. 3]]

^aapp-11-008

### AAPP-11-009

How do the unique table and computed table contribute to the efficiency and canonicity of BDDs?" (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=3|2025-06-05-1st · Exercise 2B · p. 3]]

^aapp-11-009

## Treaps

*No dedicated study note is currently available for this topic.*

### AAPP-12-001

Describe how treap Union works.

Source: [[Tema Esame 2022-02-11-1st.pdf#page=2|2022-02-11-1st · Exercise 1 · p. 2]]

^aapp-12-001

### AAPP-12-002

Describe how Treap split/union works.

Source: [[Tema Esame 2022-09-07-1st.pdf#page=4|2022-09-07-1st · Exercise 3 · p. 4]]

^aapp-12-002

### AAPP-12-003

Describe how Treap split/union works.? (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=4|2022-11-08-1st · Exercise 3B · p. 4]]

^aapp-12-003

### AAPP-12-004

Describe the treap data structure, how the search is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=4|2023-06-19-1st · Exercise 3B · p. 4]]

^aapp-12-004

### AAPP-12-005

Describe the treap data structure and how the split is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=4|2023-09-11-1st · Exercise 3B · p. 4]]

^aapp-12-005

### AAPP-12-006

Please provide the implementation of the split operation for Treaps. What is the operation complexity? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=4|2024-01-26-1st · Exercise 3B · p. 4]]

^aapp-12-006

### AAPP-12-007

Please provide the implementation of the union operation for Treaps. What is the operation complexity? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=4|2024-02-16-1st · Exercise 3B · p. 4]]

^aapp-12-007

### AAPP-12-008

Please discuss the key properties of a Treap and of its search function. (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=4|2024-06-26-1st · Exercise 3A · p. 4]]

^aapp-12-008

### AAPP-12-009

Please discuss how a Union is implemented in a Treap Data-Structure. How does the number of rotations impact the search for an element in a Treap? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=4|2024-07-24-1st · Exercise 3A · p. 4]]

^aapp-12-009

### AAPP-12-010

Why does randomized Treap structure have a complexity on average similar to a balanced binary tree? Treap required all priorities to be pairwise distinct. How can this property be satisfied? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=4|2024-09-05-1st · Exercise 3A · p. 4]]

^aapp-12-010

### AAPP-12-011

Please discuss how a Split is implemented in a Treap Data-Structure. What happen in case the k element is in the initial Treap? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=4|2024-09-05-1st · Exercise 3B · p. 4]]

^aapp-12-011

### AAPP-12-012

Describe how the split for Treaps data structure works and discuss its complexity. (2)

Source: [[Tema Esame 2024-11-12-1st.pdf#page=4|2024-11-12-1st · Exercise 3B · p. 4]]

^aapp-12-012

### AAPP-12-013

Describe how the split and the union work in a treap and discuss their complexity. (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=4|2025-02-14-1st · Exercise 3B · p. 4]]

^aapp-12-013

### AAPP-12-014

Describe how the union and the split work in a treap and discuss its complexity. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=4|2025-07-04-1st · Exercise 3B · p. 4]]

^aapp-12-014

## Skip lists

*No dedicated study note is currently available for this topic.*

### AAPP-13-001

Discuss how skip list insertion work? What about its worst vs average case complexity?

Source: [[Tema Esame 2022-06-09-1st.pdf#page=4|2022-06-09-1st · Exercise 3 · p. 4]]

^aapp-13-001

### AAPP-13-002

Describe the skip-list data structure, how the search is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-02-14-1st.pdf#page=4|2023-02-14-1st · Exercise 3B · p. 4]]

^aapp-13-002

### AAPP-13-003

Describe the skip list data structure and how the union is performed, and which complexity has. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=4|2023-07-11-1st · Exercise 3B · p. 4]]

^aapp-13-003

### AAPP-13-004

Describe how the search for skip-list data structure works. (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=4|2023-11-09-1st · Exercise 3B · p. 4]]

^aapp-13-004

### AAPP-13-005

Describe how the insertion for skip-list data structure works. What about its complexity? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=4|2024-07-24-1st · Exercise 3B · p. 4]]

^aapp-13-005

### AAPP-13-006

Describe how the search for Skip-list data structure works and discuss its complexity. (2)

Source: [[Tema Esame 2025-01-24-1st.pdf#page=4|2025-01-24-1st · Exercise 3B · p. 4]]

^aapp-13-006

### AAPP-13-007

Describe how the insert for the Skip-list data structure works and discuss its complexity. (2)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=4|2025-06-05-1st · Exercise 3B · p. 4]]

^aapp-13-007

### AAPP-13-008

Describe the skip list data structure and how the search is performed, and what the complexity is. (2)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=5|2025-09-05-1st · Exercise 4B · p. 5]]

^aapp-13-008

## Disjoint sets

*No dedicated study note is currently available for this topic.*

### AAPP-14-001

Please explain how the disjoint set data structure works and which optimizations have been considered to reduce the complexity of the operations. (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=4|2023-07-11-1st · Exercise 3A · p. 4]]

^aapp-14-001

### AAPP-14-002

Please explain which optimizations have been considered to reduce the complexity of the disjoint-set operations. (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=4|2023-09-11-1st · Exercise 3A · p. 4]]

^aapp-14-002

## Amortized analysis

*No dedicated study note is currently available for this topic.*

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

### AAPP-15-002

Consider a stack data structure storing elements of a given type, which can be assumed to be empty at the start time. Users can push one element on top of the stack using a PUSH operation, which has a constant cost of 1 and remove the top with a POP operation, which has a constant cost of 1. Compute the real cost of the MULTIPOP(k) operation that removes min{k,s} elements from the top of the stack where s is the number of elements in the stack. Determine the worst possible sequence of n operations on this stack and compute the amortized cost for the operations contained in the sequence using one of the methods seen during the course.

Source: [[Tema Esame 2023-01-17-1st.pdf#page=5|2023-01-17-1st · Exercise 4 · p. 5]]

^aapp-15-002

### AAPP-15-003

Consider a dynamic table data structure for storing a variable number of elements in memory. When created, the table has space for storing only one element, and pushing one element in the table has a constant cost. If the table is full, twice the size of the original table is allocated to a new table and all elements of the original table are copied in the new table. The cost for allocating one unit of memory is constant. Compute the real cost for inserting n elements into a new-allocated table (having an initial capacity for storing only one element) and determine the amortized cost for the allocating the same number of elements using one of the methods seen during the course.

Source: [[Tema Esame 2023-02-14-1st.pdf#page=5|2023-02-14-1st · Exercise 4 · p. 5]]

^aapp-15-003

### AAPP-15-004

Please explain what aggregate amortized analysis is. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=5|2023-06-19-1st · Exercise 4A · p. 5]]

^aapp-15-004

### AAPP-15-005

What is meant by “accounting method”? At which class of algorithms could be applied? (2)

Source: [[Tema Esame 2023-07-11-1st.pdf#page=5|2023-07-11-1st · Exercise 4B · p. 5]]

^aapp-15-005

### AAPP-15-006

What is meant by “potential method”? At which class of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=5|2023-09-11-1st · Exercise 4B · p. 5]]

^aapp-15-006

### AAPP-15-007

What is meant by “potential method”? To which class of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=5|2023-11-09-1st · Exercise 4B · p. 5]]

^aapp-15-007

### AAPP-15-008

Please discuss the amortized analysis. For which class of algorithm does it matter? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=4|2024-01-26-1st · Exercise 3A · p. 4]]

^aapp-15-008

### AAPP-15-009

What is meant by “accounting method”? To which class of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2024-02-16-1st.pdf#page=5|2024-02-16-1st · Exercise 4B · p. 5]]

^aapp-15-009

### AAPP-15-010

What is meant by “amortized analysis”? To which type of algorithms could be applied? Examples? (2)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=5|2024-07-24-1st · Exercise 4B · p. 5]]

^aapp-15-010

### AAPP-15-011

Please discuss the different variants of the amortized analysis. For what class of problems are they used? (2)

Source: [[Tema Esame 2025-02-14-1st.pdf#page=5|2025-02-14-1st · Exercise 4B · p. 5]]

^aapp-15-011

### AAPP-15-012

Why is amortized analysis useful in algorithm design, especially for data structures? (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=5|2025-06-05-1st · Exercise 4A · p. 5]]

^aapp-15-012

### AAPP-15-013

What does it mean if the potential difference ΔΦ is negative in the potential method? What about the sign of Φ. (1)

Source: [[Tema Esame 2025-06-05-1st.pdf#page=5|2025-06-05-1st · Exercise 4C · p. 5]]

^aapp-15-013

### AAPP-15-014

Describe an algorithm seen during the course lectures where the potential method has been used. (2)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=4|2025-07-04-1st · Exercise 3A · p. 4]]

^aapp-15-014

### AAPP-15-015

What are the characteristics of an algorithm that require the amortized analysis methods? (1)

Source: [[Tema Esame 2025-07-04-1st.pdf#page=5|2025-07-04-1st · Exercise 4C · p. 5]]

^aapp-15-015

### AAPP-15-016

What is meant by “accounting method”? To which class of algorithms could be applied? Examples? (1)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=5|2025-09-05-1st · Exercise 4A · p. 5]]

^aapp-15-016

## Online algorithms and competitive analysis

*No dedicated study note is currently available for this topic.*

### AAPP-16-001

Please discuss the difference between Online and Offline algorithms. (2)

Source: [[Tema Esame 2022-11-08-1st.pdf#page=4|2022-11-08-1st · Exercise 3A · p. 4]]

^aapp-16-001

### AAPP-16-002

Please explain what the competitive analysis is meant for. (2)

Source: [[Tema Esame 2023-01-17-1st.pdf#page=4|2023-01-17-1st · Exercise 3A · p. 4]]

^aapp-16-002

### AAPP-16-003

Please explain why the amortized analysis matters for the analysis of the complexity of the Move to Front algorithm. (2)

Source: [[Tema Esame 2023-06-19-1st.pdf#page=5|2023-06-19-1st · Exercise 4B · p. 5]]

^aapp-16-003

### AAPP-16-004

Detail the Move to Front algorithm. What approach is followed to estimate the temporal complexity of this class of algorithms? Which class of algorithms does it belongs to? (2)

Source: [[Tema Esame 2023-09-11-1st.pdf#page=5|2023-09-11-1st · Exercise 4A · p. 5]]

^aapp-16-004

### AAPP-16-005

Please discuss the competitive analysis. For which class of algorithm does it matter? (2)

Source: [[Tema Esame 2023-11-09-1st.pdf#page=4|2023-11-09-1st · Exercise 3A · p. 4]]

^aapp-16-005

### AAPP-16-006

Please describe the difference between on-line and off-line algorithms. How is their complexity analyzed? (2)

Source: [[Tema Esame 2024-01-26-1st.pdf#page=5|2024-01-26-1st · Exercise 4A · p. 5]]

^aapp-16-006

### AAPP-16-007

Please describe the “move to front” heuristic (complexity included). Why did we use amortized analysis instead of the worst-case? (2)

Source: [[Tema Esame 2024-06-26-1st.pdf#page=5|2024-06-26-1st · Exercise 4B · p. 5]]

^aapp-16-007

### AAPP-16-008

To which class does the Move-To-Front Algorithm belong? How is its complexity evaluated? (1)

Source: [[Tema Esame 2024-07-24-1st.pdf#page=3|2024-07-24-1st · Exercise 2C · p. 3]]

^aapp-16-008

### AAPP-16-009

Please discuss the competitive analysis. In which class of algorithm is used? Amortized analysis could be of some use; why? (2)

Source: [[Tema Esame 2024-09-05-1st.pdf#page=5|2024-09-05-1st · Exercise 4A · p. 5]]

^aapp-16-009

### AAPP-16-010

Please explain what the competitive analysis is meant for by using one of the examples presented during the course lectures. (2)

Source: [[Tema Esame 2025-09-05-1st.pdf#page=3|2025-09-05-1st · Exercise 2B · p. 3]]

^aapp-16-010

## Parallel design and architectures

Related notes: [[Course Introduction]].

### AAPP-17-001

List and describe the different kinds of parallelism according to the Flynn taxonomy, together with architectures implementing them when possible.

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=3|2022-02-11-2nd-a · Exercise 2A · p. 3]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=3|2022-02-11-2nd-b · Exercise 2A · p. 3]]

^aapp-17-001

### AAPP-17-002

It is not recommendable to mix parallelism technologies since doing so increases the complexity of the compiled binaries: true or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=3|2022-02-11-2nd-a · Exercise 2B · p. 3]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=3|2022-02-11-2nd-b · Exercise 2B · p. 3]]

^aapp-17-002

### AAPP-17-003

Is it possible to obtain the same low level implementation starting from different parallel programming models descriptions of the same parallel pattern?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=3|2022-06-09-2nd-a · Exercise 2A · p. 3]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=3|2022-06-09-2nd-b · Exercise 2A · p. 3]]

^aapp-17-003

### AAPP-17-004

Parallel programming models using threads spawn a single process, therefore the program I/O correctness is always guaranteed: true or false?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=3|2022-06-09-2nd-a · Exercise 2B · p. 3]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=3|2022-06-09-2nd-b · Exercise 2B · p. 3]]

^aapp-17-004

### AAPP-17-005

Is it possible to use multiple parallelization models in the same program? Would it benefit some hardware architectures in particular?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=3|2022-09-07-2nd-b · Exercise 2A · p. 3]]

^aapp-17-005

### AAPP-17-006

Which are the main differences between parallel programming models based on threads and those based on processes in terms of low-level information management and architectures that can benefit from them?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=3|2022-09-07-2nd-b · Exercise 2C · p. 3]]

^aapp-17-006

### AAPP-17-007

Could you please summarize why manual parallelization is preferred to automatic parallelization? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1A · p. 2]]
Source: [[Tema Esame 2025-09-05-2nd.pdf#page=1|2025-09-05-2nd · Exercise 1A · p. 1]]

^aapp-17-007

### AAPP-17-008

Designing a «good» parallel algorithm by extracting all the available parallelism is not enough. True/False? Why?(1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1B · p. 2]]

^aapp-17-008

### AAPP-17-009

Please comment this sentence: “Design a «good» parallel algorithm by extracting all the available parallelism is not enough.” (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=2|2024-07-24-2nd · Exercise 1A · p. 2]]

^aapp-17-009

### AAPP-17-010

Please comment on this sentence: “Automatic parallelization cannot be used because it produces wrong solutions.”. True/false, partially true? (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=2|2024-09-05-2nd · Exercise 1A · p. 2]]

^aapp-17-010

### AAPP-17-011

“A single instruction can manipulate different data at a time”. Please comment on the sentence and discuss which kind of parallelism it is referring to. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=2|2024-09-05-2nd · Exercise 1B · p. 2]]

^aapp-17-011

### AAPP-17-012

What does PCAM Design Methodology mean? (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=1|2025-01-24-2nd · Exercise 1B · p. 1]]

^aapp-17-012

## Dependences and loop parallelization

*No dedicated study note is currently available for this topic.*

### AAPP-18-001

Loop-carried dependences prevent loop parallelization. True/False? Why?(1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1C · p. 2]]

^aapp-18-001

### AAPP-18-002

Is an output dependence a true dependence? True/False? Why? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=2|2022-12-22-2nd · Exercise 1D · p. 2]]

^aapp-18-002

### AAPP-18-003

What is meant by DOALL loop? Example? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=2|2023-01-17-2nd · Exercise 1A · p. 2]]

^aapp-18-003

### AAPP-18-004

Is the following code parallelizable? (1)

```c
           for (i=10; i<100; i++)
             a[i-10] = a[i] + 100;
```

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=2|2023-01-17-2nd · Exercise 1B · p. 2]]

^aapp-18-004

### AAPP-18-005

Please describe the differences between flow, output and anti-dependencies. (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=2|2023-01-17-2nd · Exercise 1C · p. 2]]

^aapp-18-005

### AAPP-18-006

“Parallel execution must address control, data, and system dependences”. What is meant by “dependency” in this context? (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=2|2023-02-14-2nd · Exercise 1A · p. 2]]

^aapp-18-006

### AAPP-18-007

Is the following code parallelizable? Are there better parallelizable solutions? (2)

```c
           for (j=1; j<100; j++)
                     for (i=0; i<100; i++)
                           a[i][j] = f(a[i][j-1]);
```

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=2|2023-02-14-2nd · Exercise 1B · p. 2]]

^aapp-18-007

### AAPP-18-008

Please explain the differences between “loop-carried“ and “loop-independent”.(1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=2|2023-02-14-2nd · Exercise 1C · p. 2]]

^aapp-18-008

### AAPP-18-009

Is it possible to eliminate a flow dependency by modifying the program and ensuring that the program remains equivalent? (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=2|2023-06-19-2nd · Exercise 1A · p. 2]]

^aapp-18-009

### AAPP-18-010

Is the following code parallelizable? Are there better parallelizable solutions? (2)

```c
           for (i=0; i<100; i++)
                      for (j=1; j<100; j++)
                            a[i][j] = f(a[i][j-1]);
```

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=2|2023-06-19-2nd · Exercise 1B · p. 2]]

^aapp-18-010

### AAPP-18-011

DOALL loops have linear speedup even using the Amdahl law. Could you please write a short pseudo code showing an example of a DOALL loop? (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=2|2023-07-11-2nd · Exercise 1A · p. 2]]

^aapp-18-011

### AAPP-18-012

Is the following code parallelizable? Are there better parallelizable solutions? (2)

```c
           for (i=0; i<100; i++)
                     for (j=0; j<91; j++)
                        a[i][j+9] = f(a[i][j]);
```

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=2|2023-07-11-2nd · Exercise 1B · p. 2]]

^aapp-18-012

### AAPP-18-013

Could you please describe the statement/operation dependency and how and when it can be removed? (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=2|2023-09-11-2nd · Exercise 1A · p. 2]]

^aapp-18-013

### AAPP-18-014

Under which condition the following code is parallelizable? In case the conditions hold, are there better parallelizable solutions? (2)

```c
           for (i=0; i<100; i++)
                     for (j=0; j<10; j++)
                           a[i][j] = f(a[i][j]);
```

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=2|2023-09-11-2nd · Exercise 1B · p. 2]]

^aapp-18-014

### AAPP-18-015

Could you please write a short pseudo code showing an example of a DOALL loop in C? Which parallel pattern is directly connected to the DOALL loop? (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=2|2023-12-21-2nd · Exercise 1A · p. 2]]

^aapp-18-015

### AAPP-18-016

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=0; j<10; j++)
                            a[i][j] = f(a[j][i-1]);
```

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=2|2023-12-21-2nd · Exercise 1B · p. 2]]

^aapp-18-016

### AAPP-18-017

Is it possible to eliminate a flow dependency by modifying the program and ensuring that the program remains equivalent? Is it the same with output dependency? Please show an example of what can be done. (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=2|2024-01-26-2nd · Exercise 1A · p. 2]]

^aapp-18-017

### AAPP-18-018

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=0; j<100; j++)
                             c[j][i] += a[i]*b[j];
```

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=2|2024-01-26-2nd · Exercise 1B · p. 2]]

^aapp-18-018

### AAPP-18-019

Please describe the Parallel Data Management Patterns: Pipeline. Are flow dependencies preventing correct parallelization of pipeline parallel pattern when present? (2)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=2|2024-02-16-2nd · Exercise 1A · p. 2]]

^aapp-18-019

### AAPP-18-020

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=0; j<100; j++)
                            b[i][j] += f(a[i][j]);
```

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=2|2024-02-16-2nd · Exercise 1B · p. 2]]

^aapp-18-020

### AAPP-18-021

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=1; i<100; i++)
                      for (j=i; j<100; j++)
                            b[i][j] += f(a[i][j]);
```

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=2|2024-06-26-2nd · Exercise 1B · p. 2]]

^aapp-18-021

### AAPP-18-022

Is it possible to eliminate an anti-dependency by modifying the program and ensuring that the program remains equivalent? Is it the same with output-dependency? Please show an example of what can be done in both cases. (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=2|2024-07-24-2nd · Exercise 1B · p. 2]]

^aapp-18-022

### AAPP-18-023

Under what conditions can the following code be parallelized? If these conditions are met, is there a way to write the code for better parallelization? (2)

```c
            for (i=0; i<100; i++)
                      for (j=2; j<100; j++)
                            a[i][j] = f(a[i][j]) + a[i][j-2];
```

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=2|2024-07-24-2nd · Exercise 1C · p. 2]]

^aapp-18-023

### AAPP-18-024

Which loop can be parallelized and under which conditions? Does the overhead of the runtime impact the parallelization of the loops? Which is the best way to parallelize this code on multi-core systems? (2)

```c
            for (i=0; i<1000; i++)
                      for (j=0; j<4; j++)
                            a[i][j] = f(a[i][j]) + a[i][j];
```

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=2|2024-09-05-2nd · Exercise 1C · p. 2]]

^aapp-18-024

### AAPP-18-025

Please explain when a dependence can be classified as lexically forward dependence. (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=1|2025-01-24-2nd · Exercise 1A · p. 1]]

^aapp-18-025

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

### AAPP-18-027

What dependencies can be eliminated by renaming the variables? (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=1|2025-02-14-2nd · Exercise 1B · p. 1]]

^aapp-18-027

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

### AAPP-18-030

What is the difference between a true dependence and an anti-dependence? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=1|2025-07-04-2nd · Exercise 1A · p. 1]]

^aapp-18-030

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

### AAPP-18-032

Please describe the differences between flow, output, and anti-dependencies. (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=1|2025-09-05-2nd · Exercise 1B · p. 1]]

^aapp-18-032

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

## Parallel patterns

Related notes: [[PRAM]] (introductory patterns only).

### AAPP-19-001

Describe the map parallel pattern and at least one fusion optimization that can be applied to it.

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=3|2022-02-11-2nd-a · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=3|2022-02-11-2nd-b · Exercise 2C · p. 3]]

^aapp-19-001

### AAPP-19-002

Describe the scan parallel pattern. Can it be implemented using different approaches with respect to the computation of intermediate values?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=3|2022-06-09-2nd-a · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=3|2022-06-09-2nd-b · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=3|2022-09-07-2nd-b · Exercise 2B · p. 3]]

^aapp-19-002

### AAPP-19-003

Describe the workpile pattern, situations where it may be applied and possible implementations.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=3|2022-06-30-2nd-a · Exercise 2A · p. 3]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=3|2022-06-30-2nd-b · Exercise 2A · p. 3]]

^aapp-19-003

### AAPP-19-004

Is the Quicksort algorithm easy to parallelize? Propose a high-level description of a possible parallelization and analyze its potential bottlenecks.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=3|2022-06-30-2nd-a · Exercise 2B · p. 3]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=3|2022-06-30-2nd-b · Exercise 2B · p. 3]]

^aapp-19-004

### AAPP-19-005

Describe how to implement a map pattern with one of the parallel programming models presented in the course.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=3|2022-06-30-2nd-a · Exercise 2C · p. 3]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=3|2022-06-30-2nd-b · Exercise 2C · p. 3]]

^aapp-19-005

### AAPP-19-006

Please define what a parallel reduction is: assumptions, complexity, example.(1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2A · p. 3]]

^aapp-19-006

### AAPP-19-007

Please describe how a parallel pattern gather works. (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2B · p. 3]]

^aapp-19-007

### AAPP-19-008

Describe all the collision rules for a scatter pattern. (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2C · p. 3]]
Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2C · p. 3]]

^aapp-19-008

### AAPP-19-009

Describe how the pack parallel pattern could be parallelly implemented. (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=3|2022-12-22-2nd · Exercise 2D · p. 3]]

^aapp-19-009

### AAPP-19-010

Please describe the stencil pattern: assumptions, complexity, example. (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2A · p. 3]]

^aapp-19-010

### AAPP-19-011

Please describe the differences between Split and Bin parallel patterns. (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2B · p. 3]]

^aapp-19-011

### AAPP-19-012

Given an input collection of 100 values and an auxiliary array of 10, which parallel pattern between the gather and the scatter is producing an output collection of 10 values? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2C · p. 3]]

^aapp-19-012

### AAPP-19-013

What is meant by separating hyperplane in a recurrence parallelization? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=3|2023-01-17-2nd · Exercise 2D · p. 3]]

^aapp-19-013

### AAPP-19-014

Please describe the map pattern: assumptions, complexity, example. (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2A · p. 3]]

^aapp-19-014

### AAPP-19-015

Please describe the differences between Zip and Unzip parallel patterns. (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2B · p. 3]]

^aapp-19-015

### AAPP-19-016

What is meant by “permutation scatter”? (1)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=3|2023-02-14-2nd · Exercise 2D · p. 3]]
Source: [[Tema Esame 2023-07-11-2nd.pdf#page=3|2023-07-11-2nd · Exercise 2C · p. 3]]

^aapp-19-016

### AAPP-19-017

Is it possible to implement a pipeline paradigm using OpenMP? What parallel paradigm is adopted by default in OpenMP?(2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=4|2023-02-14-2nd · Exercise 3A · p. 4]]

^aapp-19-017

### AAPP-19-018

Please describe the reduce pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=3|2023-06-19-2nd · Exercise 2A · p. 3]]
Source: [[Tema Esame 2023-09-11-2nd.pdf#page=3|2023-09-11-2nd · Exercise 2A · p. 3]]

^aapp-19-018

### AAPP-19-019

Please describe the differences between Gather and scatter parallel patterns. (1)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=3|2023-06-19-2nd · Exercise 2B · p. 3]]

^aapp-19-019

### AAPP-19-020

What is meant by “merge scatter”? (1)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=3|2023-06-19-2nd · Exercise 2C · p. 3]]

^aapp-19-020

### AAPP-19-021

Please describe the stencil pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=3|2023-07-11-2nd · Exercise 2A · p. 3]]

^aapp-19-021

### AAPP-19-022

Please describe how the Pack parallel pattern could be implemented. (1)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=3|2023-07-11-2nd · Exercise 2B · p. 3]]

^aapp-19-022

### AAPP-19-023

Please describe what is meant by pipelined parallelism and how could be implemented in OpenMP?(2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=4|2023-07-11-2nd · Exercise 3A · p. 4]]

^aapp-19-023

### AAPP-19-024

Please describe how the Unpack parallel pattern could be implemented. (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=3|2023-09-11-2nd · Exercise 2B · p. 3]]

^aapp-19-024

### AAPP-19-025

Please describe the scan pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=3|2023-12-21-2nd · Exercise 2A · p. 3]]

^aapp-19-025

### AAPP-19-026

Please describe how the Split parallel pattern could be implemented. (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=3|2023-12-21-2nd · Exercise 2B · p. 3]]

^aapp-19-026

### AAPP-19-027

Please describe the parallel gather pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=3|2024-01-26-2nd · Exercise 2A · p. 3]]

^aapp-19-027

### AAPP-19-028

Please describe how the “Merge collision resolution” works. Is it related to the parallel gather pattern? (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=3|2024-01-26-2nd · Exercise 2B · p. 3]]

^aapp-19-028

### AAPP-19-029

Please describe the parallel scatter pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=3|2024-02-16-2nd · Exercise 2A · p. 3]]

^aapp-19-029

### AAPP-19-030

Please describe how the Pack parallel pattern works. How is implemented? (2)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=3|2024-02-16-2nd · Exercise 2B · p. 3]]

^aapp-19-030

### AAPP-19-031

Please describe the parallel reduce pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=3|2024-06-26-2nd · Exercise 2A · p. 3]]
Source: [[Tema Esame 2024-09-05-2nd.pdf#page=3|2024-09-05-2nd · Exercise 2A · p. 3]]

^aapp-19-031

### AAPP-19-032

Please describe how the Split parallel pattern works. How is it implemented? (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=3|2024-06-26-2nd · Exercise 2B · p. 3]]

^aapp-19-032

### AAPP-19-033

Please describe the parallel Split pattern: assumptions, complexity, and example. (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=3|2024-07-24-2nd · Exercise 2A · p. 3]]

^aapp-19-033

### AAPP-19-034

Please describe how the Unzip parallel pattern works. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=3|2024-07-24-2nd · Exercise 2B · p. 3]]

^aapp-19-034

### AAPP-19-035

Please explain how the parallel shift pattern functions and provide its implementation (including pseudo-code). Also, please indicate its complexity. (2)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=3|2024-09-05-2nd · Exercise 2B · p. 3]]

^aapp-19-035

### AAPP-19-036

Please describe the parallel scan pattern, including assumptions, complexity, and examples. (2)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=2|2025-01-24-2nd · Exercise 2A · p. 2]]

^aapp-19-036

### AAPP-19-037

Please discuss how the Zip parallel pattern works. How is it implemented (pseudo code required)? (2)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=2|2025-01-24-2nd · Exercise 2B · p. 2]]

^aapp-19-037

### AAPP-19-038

Please describe and show an example of Parallel Data Management Patterns: pipeline. (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=1|2025-02-14-2nd · Exercise 1A · p. 1]]

^aapp-19-038

### AAPP-19-039

Please describe the parallel Scatter pattern, including assumptions, PRAM-based complexity, and examples. (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=2|2025-02-14-2nd · Exercise 2A · p. 2]]

^aapp-19-039

### AAPP-19-040

Please discuss how the Pack parallel pattern works. How is it implemented (pseudo code required and PRAM-based complexity)? (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=2|2025-02-14-2nd · Exercise 2B · p. 2]]

^aapp-19-040

### AAPP-19-041

How does the Fork-Join pattern differ from a barrier in parallel programming? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=1|2025-06-05-2nd · Exercise 1A · p. 1]]

^aapp-19-041

### AAPP-19-042

How does the Workpile pattern differ from a standard Map pattern? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=1|2025-06-05-2nd · Exercise 1B · p. 1]]

^aapp-19-042

### AAPP-19-043

How can the map and reduce patterns be fused, and what is the benefit of doing so? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=2|2025-06-05-2nd · Exercise 2A · p. 2]]

^aapp-19-043

### AAPP-19-044

In the context of parallel scan, what is the difference between an inclusive and an exclusive scan? What about the complexity? (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=2|2025-06-05-2nd · Exercise 2B · p. 2]]

^aapp-19-044

### AAPP-19-045

Please discuss how the Split parallel pattern works. How is it implemented (pseudo code required and PRAM-based complexity)? (2)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=2|2025-06-05-2nd · Exercise 2C · p. 2]]
Source: [[Tema Esame 2025-09-05-2nd.pdf#page=2|2025-09-05-2nd · Exercise 2B · p. 2]]

^aapp-19-045

### AAPP-19-046

What are the challenges of using a shared state in a Map function? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=1|2025-07-04-2nd · Exercise 1B · p. 1]]

^aapp-19-046

### AAPP-19-047

Please describe the parallel reduce pattern: assumptions, PRAM complexity, and example. What about the work done? Is it different from the one done by the sequential algorithm? (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=2|2025-07-04-2nd · Exercise 2A · p. 2]]

^aapp-19-047

### AAPP-19-048

Please discuss how the Unpack parallel pattern works. How is it implemented (pseudo code required and PRAM-based complexity)? (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=2|2025-07-04-2nd · Exercise 2B · p. 2]]

^aapp-19-048

### AAPP-19-049

Please describe the parallel gather pattern, including assumptions, PRAM-based complexity, and examples. (2)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=2|2025-09-05-2nd · Exercise 2A · p. 2]]

^aapp-19-049

## Task graphs and OpenMP implementations

*No dedicated study note is currently available for this topic.*

### AAPP-20-001

Given an algorithm with the following structure: And the following values of work: W(Task1) = 2, W(Task2) = 1, W(Task3) = 3, W(Task4) = 2, W(Task5) = 1, W(Task6) = 2, W(Task7) = 5, W(Task8) = 1. Compute the Work and the Makespan of the algorithm. What is the minimum number of threads required to guarantee the maximum parallelism? (1) Provide a pseudocode implementation using OpenMP (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=4|2023-01-17-2nd · Exercise 3A · p. 4]]

![[2023-01-17-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2023-01-17-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-001

### AAPP-20-002

Please describe what is meant by task parallelism (Parallel Task Graph) and how could be implemented in OpenMP?(2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=4|2023-09-11-2nd · Exercise 3A · p. 4]]

^aapp-20-002

### AAPP-20-003

Consider the following task graph: Calculate work and parallelism. Is it a good idea to use 3 threads? (1) Write a corresponding OpenMP implementation. (2)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=4|2023-12-21-2nd · Exercise 3B · p. 4]]

![[2023-12-21-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2023-12-21-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-003

### AAPP-20-004

Is it better to implement the program with 3 or 4 threads? (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=4|2024-07-24-2nd · Exercise 3A · p. 4]]

![[2024-07-24-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2024-07-24-2nd.pdf#page=4|PDF page 4]].*

^aapp-20-004

### AAPP-20-005

Write a corresponding OpenMP implementation. (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=4|2024-07-24-2nd · Exercise 3B · p. 4]]

> [!example]- Shared graph or diagram
> ![[2024-07-24-2nd-p4.png|800]]

^aapp-20-005

### AAPP-20-006

If you could optimize one task bringing its work to 0 (maintaining the graph structure), which one would yield the best improvement in terms of parallel execution time? (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=4|2024-07-24-2nd · Exercise 3C · p. 4]]

> [!example]- Shared graph or diagram
> ![[2024-07-24-2nd-p4.png|800]]

^aapp-20-006

### AAPP-20-007

Describe the method to qualitatively evaluate a parallel algorithm through its data flow graph. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=4|2024-09-05-2nd · Exercise 3A · p. 4]]

^aapp-20-007

### AAPP-20-008

Calculate Span and Parallelism. If Tasks 0, 2 and 10 represent the thread management overhead, what is the maximum theoretical speedup over a sequential implementation? (1)

*Shared exercise context:* Consider the task graph on the source page.

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=3|2025-01-24-2nd · Exercise 3B · p. 3]]

![[2025-01-24-2nd-p3.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-01-24-2nd.pdf#page=3|PDF page 3]].*

^aapp-20-008

### AAPP-20-009

Write a corresponding OpenMP implementation. (2)

*Shared exercise context:* Consider the task graph on the source page.

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=3|2025-01-24-2nd · Exercise 3C · p. 3]]

> [!example]- Shared graph or diagram
> ![[2025-01-24-2nd-p3.png|800]]

^aapp-20-009

### AAPP-20-010

Indicate the critical path in the figure, and calculate the Parallelism. (1)

*Shared exercise context:* Consider the task graph on the source page. All tasks contain the same amount of work.

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=3|2025-07-04-2nd · Exercise 3B · p. 3]]

![[2025-07-04-2nd-p3.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-07-04-2nd.pdf#page=3|PDF page 3]].*

^aapp-20-010

### AAPP-20-011

Write a corresponding OpenMP implementation, explaining your choice of work-sharing construct. (2)

*Shared exercise context:* Consider the task graph on the source page. All tasks contain the same amount of work.

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=3|2025-07-04-2nd · Exercise 3C · p. 3]]

> [!example]- Shared graph or diagram
> ![[2025-07-04-2nd-p3.png|800]]

^aapp-20-011

## OpenMP

*No dedicated study note is currently available for this topic.*

### AAPP-21-001

OpenMP is an API dedicated to the acceleration of applications in distributed-memory environments: true or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1A · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1A · p. 2]]

^aapp-21-001

### AAPP-21-002

Describe the functionality of the private, shared, default Data Scope Attribute Clauses

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1B · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1B · p. 2]]

^aapp-21-002

### AAPP-21-003

How can the search of an element inside an (unbalanced) binary tree be accelerated using OpenMP?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1C · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1C · p. 2]]

^aapp-21-003

### AAPP-21-004

The maximum number of threads that can be spawned in OpenMP depends on the underlying hardware architecture: true or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=2|2022-02-11-2nd-a · Exercise 1D · p. 2]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=2|2022-02-11-2nd-b · Exercise 1D · p. 2]]

^aapp-21-004

### AAPP-21-005

Are there any compiler-related limitations to the use of OpenMP?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1A · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1A · p. 2]]

^aapp-21-005

### AAPP-21-006

What are Work-Sharing constructs in OpenMP? Describe their use and the conditions required for them to effectively parallelize a task.

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1B · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1B · p. 2]]

^aapp-21-006

### AAPP-21-007

Describe how to parallelize the search of an element inside a list of unknown length using OpenMP.

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1C · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1C · p. 2]]

^aapp-21-007

### AAPP-21-008

Is it possible to express nested parallelism in OpenMP? Is it generally a good practice?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=2|2022-06-09-2nd-a · Exercise 1D · p. 2]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=2|2022-06-09-2nd-b · Exercise 1D · p. 2]]

^aapp-21-008

### AAPP-21-009

Describe the multithreading paradigm used in OpenMP and the lifespan of threads with respect to tasks.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1A · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1A · p. 2]]

^aapp-21-009

### AAPP-21-010

How is variables visibility managed in OpenMP?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1B · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1B · p. 2]]

^aapp-21-010

### AAPP-21-011

What is the “omp sections” directive used for?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1C · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1C · p. 2]]

^aapp-21-011

### AAPP-21-012

Is it possible and/or mandatory to define barriers in OpenMP?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=2|2022-06-30-2nd-a · Exercise 1D · p. 2]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=2|2022-06-30-2nd-b · Exercise 1D · p. 2]]

^aapp-21-012

### AAPP-21-013

What are the static and dynamic extents of the omp parallel directive?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1A · p. 2]]

^aapp-21-013

### AAPP-21-014

Is it possible for the programmer to control the distribution of parallel loop iterations across threads when using an omp for directive?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1B · p. 2]]

^aapp-21-014

### AAPP-21-015

What is the functionality of the omp_set_num_threads function? Are there other ways for achieving the same result?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1C · p. 2]]

^aapp-21-015

### AAPP-21-016

Is it possible to perform a reduction over a single variable using OpenMP?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=2|2022-09-07-2nd-b · Exercise 1D · p. 2]]

^aapp-21-016

### AAPP-21-017

What’s the use of the omp single directive? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=4|2022-12-22-2nd · Exercise 3B · p. 4]]

^aapp-21-017

### AAPP-21-018

How can we control the number of threads spawned by the omp parallel pragma? (2)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=4|2022-12-22-2nd · Exercise 3C · p. 4]]

^aapp-21-018

### AAPP-21-019

What’s the use of the omp critical directive? (1)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=4|2023-01-17-2nd · Exercise 3B · p. 4]]

^aapp-21-019

### AAPP-21-020

Is it possible to control the visibility of variables between different threads in OpenMP? In which ways? (2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=4|2023-02-14-2nd · Exercise 3B · p. 4]]

^aapp-21-020

### AAPP-21-021

Please describe what is meant by nested parallelism and how could be implemented in OpenMP?(2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=4|2023-06-19-2nd · Exercise 3A · p. 4]]

^aapp-21-021

### AAPP-21-022

What is the difference between static and dynamic schedule clauses of OpenMP? In which OpenMP directive is it used? (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=4|2023-06-19-2nd · Exercise 3B · p. 4]]

^aapp-21-022

### AAPP-21-023

Please describe the work-sharing constructs in OpenMP. (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=4|2023-07-11-2nd · Exercise 3B · p. 4]]

^aapp-21-023

### AAPP-21-024

Please describe the simd directive in OpenMP. (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=4|2023-09-11-2nd · Exercise 3B · p. 4]]

^aapp-21-024

### AAPP-21-025

Describe how each thread in the following diagram behaves at runtime as it encounters points marked with 1, representing pragma omp cancel, and with 2, representing pragma omp cancellation point. (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=4|2024-01-26-2nd · Exercise 3C · p. 4]]

![[2024-01-26-2nd-p4.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2024-01-26-2nd.pdf#page=4|PDF page 4]].*

^aapp-21-025

### AAPP-21-026

Why is synchronization necessary when programming with the shared memory model? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3A · p. 4]]

^aapp-21-026

### AAPP-21-027

What is the difference between static and dynamic schedule of OpenMP for loops? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3C · p. 4]]

^aapp-21-027

### AAPP-21-028

Please write a short pseudo-code showing how the map parallel pattern could be implemented in OpenMP. (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=2|2024-06-26-2nd · Exercise 1A · p. 2]]

^aapp-21-028

### AAPP-21-029

What happens when a variable is declared as firstprivate in an OpenMP pragma? (1)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=4|2024-06-26-2nd · Exercise 3B · p. 4]]
Source: [[Tema Esame 2025-09-05-2nd.pdf#page=3|2025-09-05-2nd · Exercise 3B · p. 3]]

^aapp-21-029

### AAPP-21-030

Why is cancellation in OpenMP described as “best effort” cancellation? (1.5)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=4|2024-06-26-2nd · Exercise 3C · p. 4]]

^aapp-21-030

### AAPP-21-031

Describe what is the effect of the following OpenMP directive: (2)

```c
     #pragma omp for simd schedule(simd:static, 5)
```

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=4|2024-09-05-2nd · Exercise 3B · p. 4]]

^aapp-21-031

### AAPP-21-032

List similarities and differences between a single and a master region in OpenMP. (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=3|2025-02-14-2nd · Exercise 3A · p. 3]]

^aapp-21-032

### AAPP-21-033

Describe how each thread in the following diagram behaves at runtime as it encounters points marked with 1, representing pragma omp cancel, and with 2, representing pragma omp cancellation point. (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=3|2025-02-14-2nd · Exercise 3C · p. 3]]

![[2025-02-14-2nd-p3.png|800]]

*Original source page for the graph or diagram. [[Tema Esame 2025-02-14-2nd.pdf#page=3|PDF page 3]].*

^aapp-21-033

### AAPP-21-034

It is always necessary to place an explicit barrier at the end of an OpenMP work sharing construct. Is this statement true or false? Explain. (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=3|2025-06-05-2nd · Exercise 3A · p. 3]]

^aapp-21-034

### AAPP-21-035

List the factors that determine the number of threads in an OpenMP parallel region. (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=3|2025-06-05-2nd · Exercise 3B · p. 3]]

^aapp-21-035

### AAPP-21-036

Describe the effects of the following pragma. (2)

```c
#pragma omp task depend(in: status[i])
```

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=3|2025-06-05-2nd · Exercise 3C · p. 3]]

^aapp-21-036

### AAPP-21-037

What is the difference between a static and a dynamic schedule in the OpenMP for construct? (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=3|2025-09-05-2nd · Exercise 3A · p. 3]]

^aapp-21-037

### AAPP-21-038

Describe in detail the effects of the following OpenMP pragma. (2)

```c
#pragma omp parallel for reduction(+:sum)
```

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=3|2025-09-05-2nd · Exercise 3C · p. 3]]

^aapp-21-038

## Pthreads and shared-memory synchronization

*No dedicated study note is currently available for this topic.*

### AAPP-22-001

How can a thread communicate the result of its computation after completing its routine?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=5|2022-02-11-2nd-a · Exercise 4A · p. 5]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=5|2022-02-11-2nd-b · Exercise 4A · p. 5]]

^aapp-22-001

### AAPP-22-002

Can PThread be used to implement a fixed-depth parallel pipeline? How should the pipeline stages synchronize their execution?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=5|2022-02-11-2nd-a · Exercise 4B · p. 5]]
Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=5|2022-02-11-2nd-b · Exercise 4B · p. 5]]

^aapp-22-002

### AAPP-22-003

Does PThread use an explicit or implicit synchronization model? Describe common approaches to manage the access to critical sections.

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=5|2022-06-09-2nd-a · Exercise 4A · p. 5]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=5|2022-06-09-2nd-b · Exercise 4A · p. 5]]

^aapp-22-003

### AAPP-22-004

What are the possible approaches for managing the execution flow of different threads using PThreads?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=5|2022-06-09-2nd-a · Exercise 4B · p. 5]]
Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=5|2022-06-09-2nd-b · Exercise 4B · p. 5]]

^aapp-22-004

### AAPP-22-005

When a new thread is spawned and assigned a routine, is it possible to automatically pass some arguments to that routine?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=5|2022-06-30-2nd-a · Exercise 4A · p. 5]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=5|2022-06-30-2nd-b · Exercise 4A · p. 5]]

^aapp-22-005

### AAPP-22-006

What is the difference between joinable and detached threads?

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=5|2022-06-30-2nd-a · Exercise 4B · p. 5]]
Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=5|2022-06-30-2nd-b · Exercise 4B · p. 5]]

^aapp-22-006

### AAPP-22-007

What is the use of condition variables in PThreads?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=5|2022-09-07-2nd-b · Exercise 4A · p. 5]]

^aapp-22-007

### AAPP-22-008

Is it possible to share work over a fixed size thread pool that is spawned once at the beginning of the program execution? What kind of parallel pattern can be implemented in this way?

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=5|2022-09-07-2nd-b · Exercise 4B · p. 5]]

^aapp-22-008

### AAPP-22-009

Using Pthreads, is it possible to synchronize the execution flow of multiple threads so that they will progress beyond a given point only after all threads have reached it? (1)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=4|2022-12-22-2nd · Exercise 3A · p. 4]]

^aapp-22-009

### AAPP-22-010

What are PThread condition variables and what is their use? (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=5|2023-01-17-2nd · Exercise 4B · p. 5]]

^aapp-22-010

### AAPP-22-011

What is the difference between joinable and detached threads in PThread? Can detached threads’ execution be synchronized with other threads? (2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=5|2023-02-14-2nd · Exercise 4B · p. 5]]

^aapp-22-011

### AAPP-22-012

What is it meant for the procedure pthread_barrier_wait? (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=5|2023-06-19-2nd · Exercise 4B · p. 5]]

^aapp-22-012

### AAPP-22-013

Describe the main advantages of OpenMP over Pthreads. (1)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=4|2023-12-21-2nd · Exercise 3A · p. 4]]

^aapp-22-013

### AAPP-22-014

What is the difference between joinable and detached threads in Pthreads? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=4|2024-01-26-2nd · Exercise 3A · p. 4]]

^aapp-22-014

### AAPP-22-015

What is the difference between joining and waiting on a barrier in Pthreads? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=4|2024-01-26-2nd · Exercise 3B · p. 4]]

^aapp-22-015

### AAPP-22-016

Which Pthreads API call is needed to ensure that spawned threads can finish their execution after main() returns? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3B · p. 4]]

^aapp-22-016

### AAPP-22-017

What are the main differences between Pthreads and OpenMP? (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=3|2025-01-24-2nd · Exercise 3A · p. 3]]

^aapp-22-017

### AAPP-22-018

What happens when threads encounter a barrier in Pthreads? Is the same behavior achievable through joining? (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=3|2025-02-14-2nd · Exercise 3B · p. 3]]

^aapp-22-018

## MPI

*No dedicated study note is currently available for this topic.*

### AAPP-23-001

Is the synchronization between processes explicit or implicit?

Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=4|2022-02-11-2nd-b · Exercise 3A · p. 4]]

^aapp-23-001

### AAPP-23-002

Describe the behavior of MPI_Bcast.

Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=4|2022-02-11-2nd-b · Exercise 3B · p. 4]]

^aapp-23-002

### AAPP-23-003

What are communicators? What is the advantage of defining multiple communicators in an MPI program?

Source: [[Tema Esame 2022-02-11-2nd-b.pdf#page=4|2022-02-11-2nd-b · Exercise 3C · p. 4]]

^aapp-23-003

### AAPP-23-004

Which memory architectures are supported by MPI? Are there any differences with the other parallel programming models presented?

Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=4|2022-06-09-2nd-b · Exercise 3A · p. 4]]

^aapp-23-004

### AAPP-23-005

Describe the behavior of MPI_Gather.

Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=4|2022-06-09-2nd-b · Exercise 3B · p. 4]]

^aapp-23-005

### AAPP-23-006

Describe how to spread data across processes according to a user-defined distribution using MPI.

Source: [[Tema Esame 2022-06-09-2nd-b.pdf#page=4|2022-06-09-2nd-b · Exercise 3C · p. 4]]

^aapp-23-006

### AAPP-23-007

Does MPI parallelize over thread or processes? What are the main differences between the two approaches?

Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=4|2022-06-30-2nd-b · Exercise 3A · p. 4]]

^aapp-23-007

### AAPP-23-008

Describe the behavior of the MPI_Reduce routine.

Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=4|2022-06-30-2nd-b · Exercise 3B · p. 4]]

^aapp-23-008

### AAPP-23-009

Are there any restrictions on the use of communication routines in MPI, particularly related to the use of other routines?

Source: [[Tema Esame 2022-06-30-2nd-b.pdf#page=4|2022-06-30-2nd-b · Exercise 3C · p. 4]]

^aapp-23-009

### AAPP-23-010

Describe the processes synchronization model used by MPI.

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=4|2022-09-07-2nd-b · Exercise 3A · p. 4]]

^aapp-23-010

### AAPP-23-011

Describe the behavior of the MPI_Bcast routine.

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=4|2022-09-07-2nd-b · Exercise 3B · p. 4]]

^aapp-23-011

### AAPP-23-012

Describe the use of communicators in MPI and the advantages of defining multiple communicators in a program.

Source: [[Tema Esame 2022-09-07-2nd-b.pdf#page=4|2022-09-07-2nd-b · Exercise 3C · p. 4]]

^aapp-23-012

### AAPP-23-013

Describe the functionality of the MPI_Gather subroutine (2)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=5|2022-12-22-2nd · Exercise 4A · p. 5]]

^aapp-23-013

### AAPP-23-014

How does MPI differ from Pthreads and OpenMP? (2)

Source: [[Tema Esame 2022-12-22-2nd.pdf#page=5|2022-12-22-2nd · Exercise 4B · p. 5]]

^aapp-23-014

### AAPP-23-015

What are Communicators in MPI? Describe if it is possible to define custom communicators in a program at runtime, and why doing so would be useful. (2)

Source: [[Tema Esame 2023-01-17-2nd.pdf#page=5|2023-01-17-2nd · Exercise 4A · p. 5]]

^aapp-23-015

### AAPP-23-016

Describe the functionality of the MPI_Reduce subroutine (2)

Source: [[Tema Esame 2023-02-14-2nd.pdf#page=5|2023-02-14-2nd · Exercise 4A · p. 5]]

^aapp-23-016

### AAPP-23-017

Describe the procedure MPI_Send (2)

Source: [[Tema Esame 2023-06-19-2nd.pdf#page=5|2023-06-19-2nd · Exercise 4A · p. 5]]

^aapp-23-017

### AAPP-23-018

Describe the functionality and the parameters meaning of the function MPI_Bcast (You can skip this question if you completed the second challenge) (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=5|2023-07-11-2nd · Exercise 4A · p. 5]]

^aapp-23-018

### AAPP-23-019

Describe the functionality and the parameters meaning of the function MPI_Gather(You can skip this question if you completed the second challenge) (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=5|2023-09-11-2nd · Exercise 4A · p. 5]]

^aapp-23-019

### AAPP-23-020

Most of the point-to-point communication functions have a parameter named “tag”. Please, state its type, explain its usage and why we might need to use the “MPI_ANY_TAG” value. (1)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=5|2023-12-21-2nd · Exercise 4A · p. 5]]

^aapp-23-020

### AAPP-23-021

Explain when the MPI usage overlaps with OpenMP and when OpenMP cannot replace MPI. (3)

Source: [[Tema Esame 2023-12-21-2nd.pdf#page=5|2023-12-21-2nd · Exercise 4B · p. 5]]

^aapp-23-021

### AAPP-23-022

What are the approaches that the receiver in point-to-point communications can use to allocate a suitable receiving buffer, i.e. allocate a suitable number of elements? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=5|2024-01-26-2nd · Exercise 4A · p. 5]]

^aapp-23-022

### AAPP-23-023

Why are there multiple MPI implementations? (1)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=5|2024-01-26-2nd · Exercise 4B · p. 5]]

^aapp-23-023

### AAPP-23-024

What are the main differences between collective and point-to-point functions when we focus on data exchange functions? (2)

Source: [[Tema Esame 2024-01-26-2nd.pdf#page=5|2024-01-26-2nd · Exercise 4C · p. 5]]

^aapp-23-024

### AAPP-23-025

When is it possible that at least two MPI processes are stuck waiting for each other, without the possibility of continuing their execution? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=5|2024-02-16-2nd · Exercise 4A · p. 5]]

^aapp-23-025

### AAPP-23-026

When in doubt about the behavior of an MPI function, why is it important to rely on the MPI standard instead of just trying how it works with your MPI implementation? (1)

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=5|2024-02-16-2nd · Exercise 4B · p. 5]]

^aapp-23-026

### AAPP-23-027

What is the relationship between i) MPI functions with blocking semantics, ii) MPI functions without blocking semantics, and iii) MPI + multithreading? (2) ù

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=5|2024-02-16-2nd · Exercise 4C · p. 5]]

^aapp-23-027

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

### AAPP-23-029

Why should I use the MPI_Probe function? (1)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=5|2024-06-26-2nd · Exercise 4A · p. 5]]

^aapp-23-029

### AAPP-23-030

Provide an example(s) of how the MPI tag and rank can be used in a program (1)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=5|2024-06-26-2nd · Exercise 4B · p. 5]]

^aapp-23-030

### AAPP-23-031

What are communicators in MPI? Why should I use more than one? (2)

Source: [[Tema Esame 2024-06-26-2nd.pdf#page=5|2024-06-26-2nd · Exercise 4C · p. 5]]

^aapp-23-031

### AAPP-23-032

Why should I use mpirun to execute my MPI application? (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=5|2024-07-24-2nd · Exercise 4A · p. 5]]

^aapp-23-032

### AAPP-23-033

Explain what the MPI_Comm_split function does and give an example of its usage, without implementation details such as the function signature. (1)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=5|2024-07-24-2nd · Exercise 4B · p. 5]]

^aapp-23-033

### AAPP-23-034

Explain the blocking semantics in point-to-point communications and the problems it introduces in the program. (2)

Source: [[Tema Esame 2024-07-24-2nd.pdf#page=5|2024-07-24-2nd · Exercise 4C · p. 5]]

^aapp-23-034

### AAPP-23-035

Provide an example of when it is useful to use the MPI_Barrier function. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=5|2024-09-05-2nd · Exercise 4A · p. 5]]

^aapp-23-035

### AAPP-23-036

What is the main difference between MPI and OpenMPI? (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=5|2024-09-05-2nd · Exercise 4B · p. 5]]

^aapp-23-036

### AAPP-23-037

Since each MPI process has a different memory address space, how is it possible to have a deadlock? Also, make an example to explain how we can solve it. (2)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=5|2024-09-05-2nd · Exercise 4C · p. 5]]

^aapp-23-037

### AAPP-23-038

What is the role of the root parameter in the MPI_Gather function? How does it relate to the sending and receiving buffers? (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=4|2025-01-24-2nd · Exercise 4A · p. 4]]

^aapp-23-038

### AAPP-23-039

When two MPI processes are running on two different computers, e.g. on two HPC nodes, is it possible that they could end up in a deadlock? (explain the answer) (1)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=4|2025-01-24-2nd · Exercise 4B · p. 4]]

^aapp-23-039

### AAPP-23-040

What is an MPI communicator? How and why should I manipulate communicators? Please also provide an example where it is useful. (2)

Source: [[Tema Esame 2025-01-24-2nd.pdf#page=4|2025-01-24-2nd · Exercise 4C · p. 4]]

^aapp-23-040

### AAPP-23-041

What do I get from an MPI implementation, e.g. from OpenMPI? (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=4|2025-02-14-2nd · Exercise 4A · p. 4]]

^aapp-23-041

### AAPP-23-042

Make an example where non-blocking semantics does not help with solving an MPI deadlock. (1)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=4|2025-02-14-2nd · Exercise 4B · p. 4]]

^aapp-23-042

### AAPP-23-043

How MPI_Reduce work when the send and receive data are buffers with a single element? What happens when the buffers have more than one element? Describe how the result is computed. (2)

Source: [[Tema Esame 2025-02-14-2nd.pdf#page=4|2025-02-14-2nd · Exercise 4C · p. 4]]

^aapp-23-043

### AAPP-23-044

Modern HPC systems feature cores in the order of millions. Why can MPi help my application to use more cores than a plain OpenMP application?(1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=4|2025-06-05-2nd · Exercise 4A · p. 4]]

^aapp-23-044

### AAPP-23-045

Make an example where the program’s correct execution requires MPI_probe (1)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=4|2025-06-05-2nd · Exercise 4B · p. 4]]

^aapp-23-045

### AAPP-23-046

MPI functions with non-blocking semantics, e.g. MPI_Irecv, and multi-threading programming, e.g. OpenMP, can be used to solve the same problem. What is the problem and how can the two approaches be used to solve it? (2)

Source: [[Tema Esame 2025-06-05-2nd.pdf#page=4|2025-06-05-2nd · Exercise 4C · p. 4]]

^aapp-23-046

### AAPP-23-047

Which software components do I get from an MPI implementation? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=4|2025-07-04-2nd · Exercise 4A · p. 4]]

^aapp-23-047

### AAPP-23-048

The following is the MPI_Recv signature:

```c
      int MPI_Recv(void *buf, int count, MPI_Datatype datatype,
                   int source, int tag, MPI_Comm comm, MPI_Status *status)
```

What value should I provide to the count parameter? (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=4|2025-07-04-2nd · Exercise 4B · p. 4]]

^aapp-23-048

### AAPP-23-049

Make an example where MPI_Comm_split is useful. Do not describe what the function does. Describe a scenario where it makes sense to use it, how you use it, and the reason you use it. (2)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=4|2025-07-04-2nd · Exercise 4C · p. 4]]

^aapp-23-049

### AAPP-23-050

Why does MPI enable the usage of distributed architectures? (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=4|2025-09-05-2nd · Exercise 4A · p. 4]]

^aapp-23-050

### AAPP-23-051

In which scenario does it make sense to use MPI_ANY_TAG in MPI_Probe? (1)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=4|2025-09-05-2nd · Exercise 4B · p. 4]]

^aapp-23-051

### AAPP-23-052

What is the purpose of the function MPI_Reduce? When the input buffer in each MPI process has more than one value, what is the size and content of the output buffer? (2)

Source: [[Tema Esame 2025-09-05-2nd.pdf#page=4|2025-09-05-2nd · Exercise 4C · p. 4]]

^aapp-23-052

## CUDA

*No dedicated study note is currently available for this topic.*

### AAPP-24-001

Briefly describe the hierarchy of memories of CUDA programming model

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=4|2022-02-11-2nd-a · Exercise 3A · p. 4]]

^aapp-24-001

### AAPP-24-002

Briefly describe which are the main issues in implementing a parallel application with CUDA.

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=4|2022-02-11-2nd-a · Exercise 3B · p. 4]]
Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=4|2022-06-09-2nd-a · Exercise 3B · p. 4]]

^aapp-24-002

### AAPP-24-003

Concurrent CUDA Streams: operations within a given stream occur in order. True or false?

Source: [[Tema Esame 2022-02-11-2nd-a.pdf#page=4|2022-02-11-2nd-a · Exercise 3C · p. 4]]

^aapp-24-003

### AAPP-24-004

Describe what is CUDA

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=4|2022-06-09-2nd-a · Exercise 3A · p. 4]]

^aapp-24-004

### AAPP-24-005

How parallel threads are identified in a CUDA kernel?

Source: [[Tema Esame 2022-06-09-2nd-a.pdf#page=4|2022-06-09-2nd-a · Exercise 3C · p. 4]]

^aapp-24-005

### AAPP-24-006

Briefly describe which are the main disadvanteges in implementing a parallel application with CUDA with respect to OpenMP.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=4|2022-06-30-2nd-a · Exercise 3A · p. 4]]

^aapp-24-006

### AAPP-24-007

Briefly describe the hierarchy of memories of CUDA programming model.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=4|2022-06-30-2nd-a · Exercise 3B · p. 4]]

^aapp-24-007

### AAPP-24-008

Briefly describe how threads are grouped in CUDA.

Source: [[Tema Esame 2022-06-30-2nd-a.pdf#page=4|2022-06-30-2nd-a · Exercise 3C · p. 4]]

^aapp-24-008

## Halide and high-level synthesis

*No dedicated study note is currently available for this topic.*

### AAPP-25-001

Please shortly describe the main characteristic of the domain-specific language Halide. (2)

Source: [[Tema Esame 2023-07-11-2nd.pdf#page=5|2023-07-11-2nd · Exercise 4B · p. 5]]

^aapp-25-001

### AAPP-25-002

Please briefly discuss what the term “schedule” means in the domain-specific language Halide. (2)

Source: [[Tema Esame 2023-09-11-2nd.pdf#page=5|2023-09-11-2nd · Exercise 4B · p. 5]]

^aapp-25-002

### AAPP-25-003

Describe what is the effect of the following Halide schedule: (1)

```c
gradient.split(x, x_outer, x_inner, 4);
gradient.vectorize(x_inner);
```

Source: [[Tema Esame 2024-02-16-2nd.pdf#page=4|2024-02-16-2nd · Exercise 3D · p. 4]]

^aapp-25-003

### AAPP-25-004

In Halide, it is good practice to schedule pipeline stages from the output to the input. Is this statement true or false? Explain. (1)

Source: [[Tema Esame 2024-09-05-2nd.pdf#page=4|2024-09-05-2nd · Exercise 3C · p. 4]]

^aapp-25-004

### AAPP-25-005

The input to a High-Level Synthesis tool is a Register-Transfer Level description of an accelerator. Is this statement true or false? Explain. (1)

Source: [[Tema Esame 2025-07-04-2nd.pdf#page=3|2025-07-04-2nd · Exercise 3A · p. 3]]

^aapp-25-005

## Source register

46 distinct exam papers contribute 464 exercise/subquestion occurrences, represented above by 422 entries after exact-wording consolidation. All supplied exam papers are included; the register lets you reconstruct a particular session.

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

### Duplicate PDF uploads

The following pairs are byte-identical; each exam is represented once. The original files are unchanged.

- [[Tema Esame 2024-02-16-2nd-1.pdf]] duplicates [[Tema Esame 2024-02-16-2nd.pdf]].
- [[Tema Esame 2024-06-26-1st-1.pdf]] duplicates [[Tema Esame 2024-06-26-1st.pdf]].

### Files containing results rather than questions

The following three PDFs contain marks/results tables and contribute no questions:

- [[AAPP-2nd-midterm.pdf]]
- [[AAPP-Sep-10th.pdf]]
- [[elenco-AAPP-25-26.pdf]]
