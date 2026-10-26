---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/More+on+Breakpoints+and+watchpoints.pdf]]'
source_pages: 2
annotation_style: slide-by-slide, concise English comments
---

# More on Breakpoints and watchpoints

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/More+on+Breakpoints+and+watchpoints.pdf|More+on+Breakpoints+and+watchpoints.pdf]]

Topic: Two-page reading on hardware/software breakpoints and data watchpoints.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Debugging, breakpoints and watchpoints

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/More+on+Breakpoints+and+watchpoints/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/More+on+Breakpoints+and+watchpoints.pdf#page=1|PDF page 1]]

## Slide 2 — Breakpoints and watchpoints — continuation

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/More+on+Breakpoints+and+watchpoints/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/More+on+Breakpoints+and+watchpoints.pdf#page=2|PDF page 2]]

> [!note] Comment
> If a variable has an unexpected value and you do not know which instruction changed it, a write watchpoint on its memory location can stop at the modifying access. A code breakpoint is useful when you already know the instruction location to inspect. The available trigger types depend on the target’s debug hardware.
