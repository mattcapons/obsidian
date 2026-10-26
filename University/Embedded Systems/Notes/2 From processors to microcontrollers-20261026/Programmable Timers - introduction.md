---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf]]'
source_pages: 14
annotation_style: slide-by-slide, concise English comments
---

# Programmable Timers - introduction

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf|Programmable+Timers+-+introduction.pdf]]

Topic: Timer/counter modes, 8051 registers, prescaling, interrupts, and hardware-triggered acquisition.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Programmable Timers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=1|PDF page 1]]

## Slide 2 — Timer vs counter

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=2|PDF page 2]]

> [!note] Comment
> The divide-by-12 and divide-by-24 limits in the comparison table belong to the classic 8051 example developed on pages 3–5. The general distinction is the source of counted events: an internal periodic clock measures elapsed time, whereas an external input counts events. Other MCU timer clocks need not use those divisors.

## Slide 3 — Ex. 8051 and associate registers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=3|PDF page 3]]

## Slide 4 — TMOD (Timer Mode) Register

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=4|PDF page 4]]

> [!note] Comment
> Apparent table-label error: the second mode-bit column is headed “M2,” while the text and TMOD layout on page 3 identify the pair as M1 and M0. Read the four rows as M1:M0 = 00, 01, 10, and 11.

## Slide 5 — TMOD (Timer Mode) Register

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=5|PDF page 5]]

## Slide 6 — Using Timers and Counters to Create Efficient MCU-based Designs

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=6|PDF page 6]]

## Slide 7 — Common features in many timers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=7|PDF page 7]]

> [!note] Comment
> Prescaling trades resolution for range. Dividing a 1 MHz clock by 1000 gives 1 ms per timer tick. For the illustrated counter that reloads after counting through zero, values $M,M-1,\ldots,0$ span $M+1$ ticks, so $T=(M+1)/f_t$. Check the particular timer’s terminal-count convention before programming a delay.

## Slide 8 — Common features in many timers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=8|PDF page 8]]

## Slide 9 — Polling and Interrupts

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=9|PDF page 9]]

## Slide 10 — Periodic Timers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=10|PDF page 10]]

## Slide 11 — Periodic Timers – ADC example

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=11|PDF page 11]]

> [!note] Comment
> The timer determines when sampling begins; DMA moves the completed conversion into RAM. Software need only handle a completed buffer instead of timing every sample or copying each value. This separates sample timing from interrupt-service delays, provided conversion and transfer finish quickly enough for the next trigger.

## Slide 12 — Delay

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=12|PDF page 12]]

## Slide 13 — STM32G0-GPTIM

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=13|PDF page 13]]

## Slide 14 — 8254 programmable interval timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Programmable+Timers+-+introduction.pdf#page=14|PDF page 14]]
