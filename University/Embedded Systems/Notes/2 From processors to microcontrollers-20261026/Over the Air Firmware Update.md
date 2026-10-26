---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf]]'
source_pages: 38
annotation_style: slide-by-slide, concise English comments
---

# Over the Air Firmware Update

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf|Over+the+Air+Firmware+Update.pdf]]

Topic: OTA update architecture, second-stage bootloaders, memory staging, and firmware authentication.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Over the Air Firmware Update

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=1|PDF page 1]]

## Slide 2 — Introduction

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=2|PDF page 2]]

## Slide 3 — Introduction

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=3|PDF page 3]]

## Slide 4 — Introduction

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=4|PDF page 4]]

## Slide 5 — How OTA DFU works: basic steps

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=5|PDF page 5]]

## Slide 6 — Example: Nordic

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=6|PDF page 6]]

## Slide 7 — More in general…

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=7|PDF page 7]]

## Slide 8 — Server/client architecture of an emb. sys.

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=8|PDF page 8]]

## Slide 9 — Server/client architecture of an emb. sys.

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=9|PDF page 9]]

> [!note] Comment
> Separate the destination address from the bytes to store there. In the example, half of each eight-byte packet is address overhead and half is firmware data; the packet address is not itself written as an instruction. This is an illustrative packet format, not a required OTA format.

## Slide 10 — Major challenges - 1

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=10|PDF page 10]]

## Slide 11 — Major challenges - 2

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=11|PDF page 11]]

## Slide 12 — The Second-Stage Boot Loader (SSBL)

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=12|PDF page 12]]

## Slide 13 — Typical boot sequence with SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=13|PDF page 13]]

> [!note] Comment
> The upper drawing is memory organization; the lower drawing is execution flow after reset. The table of contents supplies the application choice, allowing the SSBL to remain the stable entry point while different application images occupy other regions. “User space” here labels MCU memory accessible to the application, rather than an operating-system privilege level.

## Slide 14 — Lesson Learned: Always Have an SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=14|PDF page 14]]

## Slide 15 — Lesson Learned: Always Have a SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-015.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=15|PDF page 15]]

> [!note] Comment
> The description is deliberately incomplete: branching to a reset handler does not reproduce all effects of a hardware reset. The next pages explain why the old RTOS and interrupt state matter. Compare [[University/Embedded Systems/Notes/2 From processors to microcontrollers-20261026/Boot of a system#Slide 33 — Bootloader – With IVT offset register|Boot, page 33]] for the additional vector-table, stack, and interrupt steps.

## Slide 16 — Major issues of not having a SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-016.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=16|PDF page 16]]

## Slide 17 — Major issues of not having a SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-017.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=17|PDF page 17]]

> [!note] Comment
> A fixed SSBL protects the path by which control reaches the chosen application. It does not by itself make every update step immune to power loss: application storage and the table of contents still need recoverable updates. This qualifies the broad power-cycle claim here using the failure-recovery requirement on pages 10 and 36.

## Slide 18 — Design Trade-Off: The Role of the SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-018.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=18|PDF page 18]]

## Slide 19 — Design Trade-Off: The Role of the SSBL

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-019.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=19|PDF page 19]]

## Slide 20 — Design Trade-Off: Caching and Compression

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-020.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=20|PDF page 20]]

## Slide 21 — Design Trade-Off: Caching and Compression

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-021.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=21|PDF page 21]]

## Slide 22 — 3 approaches of OTA update for caching

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-022.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=22|PDF page 22]]

## Slide 23 — 3 approaches of OTA update for caching

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-023.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=23|PDF page 23]]

> [!note] Comment
> The 2 kB SRAM block is a temporary mirror of one flash page, rather than a second complete application image. Page-based buffering reduces the amount of staging RAM, but the implementation must track which bytes of the current page have arrived before writing it and reusing the buffer.

## Slide 24 — 3 approaches of OTA update for caching

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-024.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=24|PDF page 24]]

## Slide 25 — Design Trade-Off: Software vs. Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-025.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=25|PDF page 25]]

## Slide 26 — Design Trade-Off: Software vs. Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-026.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=26|PDF page 26]]

## Slide 27 — Security challenges

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-027.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=27|PDF page 27]]

> [!note] Comment
> Two qualifications: a fixed-size hash is collision-resistant, not mathematically unique; and an unauthenticated digest can be replaced together with the data. The signatures introduced on page 29 supply the missing authenticity check. See [NIST’s hash-function properties](https://csrc.nist.gov/glossary/term/hash_function).

## Slide 28 — Security challenges - example

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-028.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=28|PDF page 28]]

## Slide 29 — Use of use asymmetric encryption

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-029.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=29|PDF page 29]]

> [!note] Comment
> The operation drawn is digital signing and verification. The private key signs, and the client uses a trusted public key to verify; this does not encrypt the payload for confidentiality. That distinction is also made by the separate signing and encryption items on page 34.

## Slide 30 — Asymmetric encryption vs microcontrollers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-030.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=30|PDF page 30]]

## Slide 31 — Security challenges

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-031.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=31|PDF page 31]]

> [!note] Comment
> Read the table’s “+” as concatenation of bytes, not numeric addition. For example, authenticate $H_0$ with the initial signature; then check $H(P_1\Vert H_1)=H_0$ before trusting $H_1$ for the next packet. The server builds the dependencies backwards from a defined final value. The terminal value is not specified here, so this is a conceptual scheme rather than a complete packet protocol.

## Slide 32 — To move deeper into the OTA world

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-032.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=32|PDF page 32]]

## Slide 33 — Summary of Best Practices

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-033.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=33|PDF page 33]]

## Slide 34 — Best practices

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-034.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=34|PDF page 34]]

## Slide 35 — Best practices

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-035.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=35|PDF page 35]]

## Slide 36 — Best practices

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-036.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=36|PDF page 36]]

> [!note] Comment
> The two rollback statements need a policy distinction. Recovery returns to an authorized known-good image after a failed installation; downgrade prevention blocks installing an older vulnerable release as an ordinary update. The recovery mechanism and version policy must be designed together so that recovery does not bypass the intended version restriction.

## Slide 37 — Best practices

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-037.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=37|PDF page 37]]

## Slide 38 — Best practices

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update/slide-038.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Over+the+Air+Firmware+Update.pdf#page=38|PDF page 38]]
