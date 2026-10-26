---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf]]'
source_pages: 22
annotation_style: slide-by-slide, concise English comments
---

# The role of the IDE

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf|The+role+of+the+IDE.pdf]]

Topic: Cross-development, vendor IDE examples, debugging probes, trace, and virtual targets.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — How to program a microcontroller — Role of the IDE

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=1|PDF page 1]]

## Slide 2 — Needs — Rationale behind a microcontroller

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=2|PDF page 2]]

> [!note] Comment
> The host is the computer running the development tools; the target is the MCU that executes the resulting program. Cross-compilation generates instructions for the target even when the compiler runs on a different architecture. A probe or simulation model then connects the host debugger to that target.

## Slide 3 — Example of IDE - ISS

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=3|PDF page 3]]

## Slide 4 — Arm Keil MDK

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=4|PDF page 4]]

## Slide 5 — MDK-Professional

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=5|PDF page 5]]

## Slide 6 — MDK — Some of the main features

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=6|PDF page 6]]

## Slide 7 — µVision IDE

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=7|PDF page 7]]

## Slide 8 — µVision Project Manager and Run-Time Environment

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=8|PDF page 8]]

## Slide 9 — Verification tools — Parasoft C/C++test

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=9|PDF page 9]]

## Slide 10 — Verification tools — Parasoft

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=10|PDF page 10]]

## Slide 11 — ULINK Debug Adapters

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=11|PDF page 11]]

## Slide 12 — Fixed Virtual Platforms

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=12|PDF page 12]]

## Slide 13 — Code Composer Studio (CCS)

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=13|PDF page 13]]

## Slide 14 — Compiler for multi-core

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=14|PDF page 14]]

## Slide 15 — Deep analysis of execution — Trace analysis

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-015.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=15|PDF page 15]]

> [!note] Comment
> A breakpoint shows state after stopping at a chosen event. Trace instead preserves a history of execution, which helps explain the path leading to an intermittent failure. The buffer/receiver path in the slide determines how much history can be retained; it is separate from the application’s ordinary data path.

## Slide 16 — Processor Trace

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-016.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=16|PDF page 16]]

## Slide 17 — System Analyzer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-017.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=17|PDF page 17]]

## Slide 18 — Linux Development

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-018.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=18|PDF page 18]]

## Slide 19 — IAR Systems

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-019.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=19|PDF page 19]]

## Slide 20 — IAR for RISC-V — Evaluation Kit

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-020.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=20|PDF page 20]]

> [!note] Comment
> Source limitation: some text in this evaluation-kit slide is clipped at the right edge in the supplied PDF. The full PDF page is preserved in the image; words outside the source page cannot be recovered from this rendering.

## Slide 21 — Technical details of the board in the kit

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-021.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=21|PDF page 21]]

## Slide 22 — Do not forget that… — Linux

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/The+role+of+the+IDE/slide-022.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/The+role+of+the+IDE.pdf#page=22|PDF page 22]]
