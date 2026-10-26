---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf]]'
source_pages: 13
annotation_style: slide-by-slide, concise English comments
---

# PLL basics

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf|PLL+basics.pdf]]

Topic: PLL feedback, capture and lock, and programmable frequency synthesis.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Phase-Locked Loop (PLL) — basic concepts

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=1|PDF page 1]]

## Slide 2 — What is a PLL?

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=2|PDF page 2]]

## Slide 3 — Common applications of PLLs

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=3|PDF page 3]]

## Slide 4 — Basic operations

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=4|PDF page 4]]

## Slide 5 — Basic operations

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=5|PDF page 5]]

> [!note] Comment
> Equal frequencies allow a constant phase difference: $d(\phi_1-\phi_2)/dt=2\pi(f_1-f_2)=0$. That constant phase error can generate the DC control voltage needed to keep the VCO at the required frequency. Thus “locked” does not necessarily mean that the two waveforms have identical phase.

## Slide 6 — Basic operations

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=6|PDF page 6]]

## Slide 7 — PLL main applications

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=7|PDF page 7]]

## Slide 8 — Frequency synthesis

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=8|PDF page 8]]

> [!note] Comment
> The detector compares the input with the divided feedback, so lock requires $f_i=f_{\mathrm{out}}/N$. Rearranging gives $f_{\mathrm{out}}=Nf_i$: dividing inside the feedback loop produces multiplication at the VCO output. Here $f_o$ labels the feedback/input frequency; it is distinct from the free-running-frequency notation on page 6.

## Slide 9 — Frequency Synthesis

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=9|PDF page 9]]

## Slide 10 — Integer-N Synthesizer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=10|PDF page 10]]

> [!note] Comment
> At lock, $f_{\mathrm{in}}/R=f_{\mathrm{out}}/N$, hence $f_{\mathrm{out}}=f_{\mathrm{in}}N/R$. With the diagram’s 10 MHz crystal, $R=5$ and $N=24$ give 48 MHz. At fixed $R$, increasing $N$ by one changes the output by $f_{\mathrm{in}}/R$, subject to the device’s valid operating ranges.

## Slide 11 — Programmable Phase-Locked Loop Clock Generator

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=11|PDF page 11]]

## Slide 12 — What to remember for our purposes

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=12|PDF page 12]]

## Slide 13 — Integer-N Frequency Synthesizers with Prescalers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/PLL+basics/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/PLL+basics.pdf#page=13|PDF page 13]]
