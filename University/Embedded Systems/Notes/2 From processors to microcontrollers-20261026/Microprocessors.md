---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf]]'
source_pages: 68
annotation_style: slide-by-slide, concise English comments
---

# Microprocessors

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf|Microprocessor_short_en.pdf]]

Topic: Processor selection, CISC/RISC, superscalar execution, VLIW, DSPs, network processors, and MCUs.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Embedded Systems — Microprocessors

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=1|PDF page 1]]

## Slide 2 — Outline

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=2|PDF page 2]]

## Slide 3 — Microprocessors — Introduction

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=3|PDF page 3]]

## Slide 4 — Introduction

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=4|PDF page 4]]

## Slide 5 — Not only a blue sky

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=5|PDF page 5]]

## Slide 6 — Example 1/2

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=6|PDF page 6]]

## Slide 7 — Example 2/2

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=7|PDF page 7]]

> [!note] Comment
> The discontinuity comes from crossing the processor’s native word width. A dedicated adder can be widened by one bit; software must represent and combine multiple words, including a carry between them. The quoted penalty is illustrative: it depends on the instruction set, operand representation, and the costs included in the comparison.

## Slide 8 — Introduction

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=8|PDF page 8]]

## Slide 9 — Classes of a processor

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=9|PDF page 9]]

## Slide 10 — In which form is available?

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=10|PDF page 10]]

## Slide 11 — Selection process

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=11|PDF page 11]]

## Slide 12 — Selection process

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=12|PDF page 12]]

> [!note] Comment
> IPC and CPI are reciprocals for the same execution: $\mathrm{IPC}=I/C$ and $\mathrm{CPI}=C/I$. Execution time is $t=I\,\mathrm{CPI}/f$. For one million instructions at CPI 2 and 100 MHz, $t=20$ ms. Comparing IPC alone also misses how many instructions each ISA needs for the same task.

## Slide 13 — Selection process

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=13|PDF page 13]]

> [!note] Comment
> The ratios point in opposite directions: lower mW/MHz is preferable, whereas higher MIPS/mW is preferable. Under a fixed workload, energy is $E=P\,t$; a lower-power processor can still consume more energy if it runs sufficiently longer. Frequency-normalized power is therefore a selection aid rather than a complete energy estimate.

## Slide 14 — Memory

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=14|PDF page 14]]

## Slide 15 — Peripherals

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-015.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=15|PDF page 15]]

## Slide 16 — Available Software is crucial

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-016.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=16|PDF page 16]]

## Slide 17 — Software Development

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-017.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=17|PDF page 17]]

## Slide 18 — Something more tangible

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-018.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=18|PDF page 18]]

## Slide 19 — Microprocessors — General Purpose Processors

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-019.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=19|PDF page 19]]

## Slide 20 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-020.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=20|PDF page 20]]

## Slide 21 — GPP — CISC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-021.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=21|PDF page 21]]

## Slide 22 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-022.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=22|PDF page 22]]

## Slide 23 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-023.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=23|PDF page 23]]

> [!note] Comment
> In the table, `M(a)` means the contents of memory at address `a`, while a register name denotes its current contents. Address calculation and data access are separate ideas: a base-plus-offset load computes the address from a register and an offset, then reads memory there. The final row shows `pop` despite repeating the “Push” label.

## Slide 24 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-024.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=24|PDF page 24]]

## Slide 25 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-025.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=25|PDF page 25]]

## Slide 26 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-026.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=26|PDF page 26]]

## Slide 27 — GPP - CISC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-027.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=27|PDF page 27]]

## Slide 28 — GPP — RISC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-028.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=28|PDF page 28]]

## Slide 29 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-029.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=29|PDF page 29]]

> [!note] Comment
> Terminology correction: RISC expands to “Reduced Instruction Set Computer,” rather than “Restricted.” The discussion concerns simplifying individual instructions and their implementation. See [Arm’s definition](https://www.arm.com/glossary/risc).

## Slide 30 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-030.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=30|PDF page 30]]

## Slide 31 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-031.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=31|PDF page 31]]

> [!note] Comment
> “Load/store architecture” means arithmetic operates on register values and dedicated instructions move values between memory and registers. It does not mean every arithmetic instruction reloads its operands: an intermediate result can stay in registers across many operations, reducing memory traffic.

## Slide 32 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-032.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=32|PDF page 32]]

## Slide 33 — GPP - RISC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-033.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=33|PDF page 33]]

> [!note] Comment
> The statement that RISC architectures have no hardware for pipeline conflicts is too broad. It describes a simplified implementation model, not a restriction imposed by a RISC instruction set. For a concrete counterexample, [Arm documents out-of-order scheduling in Cortex-A72](https://support.arm.com/documentation/100095/0002/introduction/product-documentation-and-design-flow/documentation). Keep ISA style separate from microarchitecture when reading this comparison.

## Slide 34 — Superscalarity

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-034.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=34|PDF page 34]]

## Slide 35 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-035.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=35|PDF page 35]]

## Slide 36 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-036.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=36|PDF page 36]]

> [!note] Comment
> Several execution units allow independent instructions to overlap. The reorder buffer and commit stage explain how results can become architecturally visible in program order even when execution finishes out of order. Dependencies still constrain which instructions may run together; extra ALUs alone do not guarantee a proportional IPC increase.

## Slide 37 — GPP – super scalar

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-037.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=37|PDF page 37]]

## Slide 38 — GPP — CISC/RISC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-038.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=38|PDF page 38]]

## Slide 39 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-039.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=39|PDF page 39]]

## Slide 40 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-040.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=40|PDF page 40]]

## Slide 41 — GPP — EPIC/VLIW

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-041.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=41|PDF page 41]]

## Slide 42 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-042.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=42|PDF page 42]]

## Slide 43 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-043.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=43|PDF page 43]]

> [!note] Comment
> The eight slots correspond to different kinds of execution resources. Independent operations can occupy different slots in the same word, but two dependent operations cannot simply be packed together. If the compiler cannot find a useful operation for a slot, that slot may be unused, so the wide word does not guarantee eight useful results.

## Slide 44 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-044.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=44|PDF page 44]]

## Slide 45 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-045.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=45|PDF page 45]]

## Slide 46 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-046.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=46|PDF page 46]]

## Slide 47 — GPP — CISC/VLIW

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-047.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=47|PDF page 47]]

## Slide 48 — GPP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-048.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=48|PDF page 48]]

## Slide 49 — GPP — Comparison

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-049.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=49|PDF page 49]]

> [!note] Comment
> Read the columns as the lecture’s simplified implementation families. Earlier slides distinguish instruction-set style (CISC/RISC), issue organization (superscalar), and compiler scheduling (VLIW); these are different design dimensions. The table’s typical IPC and power entries summarize those examples rather than defining all processors with a given ISA.

## Slide 50 — Microprocessors — Application Specific

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-050.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=50|PDF page 50]]

## Slide 51 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-051.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=51|PDF page 51]]

## Slide 52 — ASP — Digital Signal Processor

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-052.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=52|PDF page 52]]

## Slide 53 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-053.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=53|PDF page 53]]

## Slide 54 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-054.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=54|PDF page 54]]

> [!note] Comment
> For the dot product $2\cdot4+3\cdot5$, start with accumulator $z_0=0$: the first MAC gives $z_1=8$ and the second gives $z_2=23$. A MAC combines multiplication with accumulation; feeding it still requires operand bandwidth, which motivates the memory discussion on page 56.

## Slide 55 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-055.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=55|PDF page 55]]

## Slide 56 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-056.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=56|PDF page 56]]

## Slide 57 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-057.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=57|PDF page 57]]

## Slide 58 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-058.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=58|PDF page 58]]

## Slide 59 — ASP — Network Processors

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-059.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=59|PDF page 59]]

## Slide 60 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-060.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=60|PDF page 60]]

## Slide 61 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-061.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=61|PDF page 61]]

## Slide 62 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-062.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=62|PDF page 62]]

## Slide 63 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-063.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=63|PDF page 63]]

> [!note] Comment
> Follow a packet upward from a PHY through its channel processor to the shared buses and buffers. Several channels can process traffic in parallel, while the RISC core handles supervision. Shared buffers, lookup tables, and SDRAM can still become common bottlenecks even when the per-channel processing is independent.

## Slide 64 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-064.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=64|PDF page 64]]

## Slide 65 — ASP — Microcontrollers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-065.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=65|PDF page 65]]

## Slide 66 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-066.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=66|PDF page 66]]

## Slide 67 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-067.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=67|PDF page 67]]

## Slide 68 — ASP

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microprocessor_short_en/slide-068.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microprocessor_short_en.pdf#page=68|PDF page 68]]
