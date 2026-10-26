---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf]]'
source_pages: 23
annotation_style: slide-by-slide, concise English comments
---

# Watchdog timers general introduction

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf|Watchdog+timers+general+introduction.pdf]]

Topic: Timeout detection, recovery stages, safe outputs, independent watchdogs, and a smart-watchdog example.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Watchdog Timers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=1|PDF page 1]]

## Slide 2 — What is a watchdog timer?

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=2|PDF page 2]]

> [!note] Comment
> The timeout only tests whether the expected servicing event happened in time. A faulty program that continues kicking the watchdog can escape detection. This is why page 18 ties servicing to functional progress and page 20 adds communication monitoring instead of relying solely on a heartbeat.

## Slide 3 — Why watchdog timers are critical for the IoT?

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=3|PDF page 3]]

## Slide 4 — Basic architecture

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=4|PDF page 4]]

## Slide 5 — Operation

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=5|PDF page 5]]

## Slide 6 — … in case of problems

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=6|PDF page 6]]

## Slide 7 — Simple single stage watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=7|PDF page 7]]

## Slide 8 — Multiple-stage watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=8|PDF page 8]]

## Slide 9 — Fail-safe systems in multistage watchdogs

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=9|PDF page 9]]

## Slide 10 — Use of two sets of control states — Runmode and Safemode

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=10|PDF page 10]]

## Slide 11 — Two-stage Watchdog to recover normal operating mode

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=11|PDF page 11]]

## Slide 12 — Three-stage watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=12|PDF page 12]]

> [!note] Comment
> The stages start sequentially. If their timeout intervals are T1, T2, and T3, a persistent failure reaches system reset after approximately T1 + T2 + T3 from the last valid kick. Switching to safe outputs happens at T1, so protection of outputs does not wait for the final processor reset.

## Slide 13 — Fault detection and corrective actions

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=13|PDF page 13]]

## Slide 14 — Microchip AVR watchdog timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=14|PDF page 14]]

## Slide 15 — Microchip AVR watchdog timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-015.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=15|PDF page 15]]

> [!note] Comment
> Apparent bit-name typo: the final sentence repeats “WDTE.” The two controls named earlier on the slide are WDIE (interrupt enable) and WDE (reset enable); these are the pair relevant to the combined mode.

## Slide 16 — Microchip AVR watchdog timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-016.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=16|PDF page 16]]

## Slide 17 — Example: Texas Instr. MSP430G2210

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-017.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=17|PDF page 17]]

## Slide 18 — TIPS on watchdog timers use

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-018.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=18|PDF page 18]]

## Slide 19 — Increase robustness with external watchdogs

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-019.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=19|PDF page 19]]

> [!note] Comment
> The drawing keeps VDD connected and drives a Reset line. That connection illustrates a processor reset; it does not itself show supply power cycling. Actual power cycling would require control over the supply path. Read the power-cycle bullet as a possible system-level recovery arrangement, not a consequence of every external watchdog reset.

## Slide 20 — Designing a smart watchdog solution for IoT

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-020.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=20|PDF page 20]]

## Slide 21 — Smart watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-021.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=21|PDF page 21]]

## Slide 22 — Smart watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-022.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=22|PDF page 22]]

> [!note] Comment
> Treat this as illustrative code. `Reset=false` records a heartbeat; the foreground periodically tests it and arms the next check. The initialization configures P1.1 as an input but enables an interrupt on P2.0, so those lines do not identify the same pin. The next slide also states that servicing the external TPL5010 is still to be added.

## Slide 23 — Plenty of features that could be added to the sample code

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction/slide-023.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Watchdog+timers+general+introduction.pdf#page=23|PDF page 23]]
