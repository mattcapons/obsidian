---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf]]'
source_pages: 34
annotation_style: slide-by-slide, concise English comments
---

# Boot of a system

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf|Boot+of+a+system.pdf]]

Topic: Reset, runtime memory initialization, vendor startup code, and bootloader handover.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Embedded Systems — Boot

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=1|PDF page 1]]

## Slide 2 — Boot

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=2|PDF page 2]]

## Slide 3 — Linux – A very complete example

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=3|PDF page 3]]

## Slide 4 — Linux – A very complete example

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=4|PDF page 4]]

## Slide 5 — Where it all begins

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=5|PDF page 5]]

> [!note] Comment
> The common idea is the transition from reset hardware to the first firmware instruction. “BIOS” names the PC example; the MCU example on the following pages instead begins at a reset handler and can run a bare-metal application without a BIOS or operating system.

## Slide 6 — Microcontroller boot sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=6|PDF page 6]]

## Slide 7 — Microcontroller boot sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=7|PDF page 7]]

> [!note] Comment
> BSS is a reservation in the runtime memory layout, rather than a block of arbitrary initial bytes that must be stored in flash. Compare pages 14–15: DATA receives initial values copied from flash, whereas BSS is created by zero-filling its RAM range. “Non-initialized” here means no explicit nonzero initializer, not an undefined initial value for static-storage objects.

## Slide 8 — Microcontroller boot sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=8|PDF page 8]]

## Slide 9 — Microcontroller boot sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=9|PDF page 9]]

> [!note] Comment
> Apparent address error: the slide gives `0x80000000` as a general Cortex-M vector base. Cortex-M0 fetches vectors at `0x00000000`; Cortex-M4 also starts there and can relocate the table using VTOR, whose offset is measured from zero. Vendor memory aliasing determines which physical memory appears there. See [Arm’s Cortex-M introduction, p. 14](https://community.arm.com/cfs-file/__key/telligent-evolution-components-attachments/01-2057-00-00-00-01-28-35/Cortex_2D00_M-for-Beginners-_2D00_-2017_5F00_EN_5F00_v2.pdf) and [M4 guide, §4.3.4](https://documentation-service.arm.com/static/5f2ac4ab60a93e65927bbdbf).

## Slide 10 — Microcontroller boot sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=10|PDF page 10]]

> [!note] Comment
> Architecture qualification: on Cortex-M, hardware already loads the initial MSP from vector entry 0 before executing the reset handler. The explicit stack-pointer assignment in the later code re-establishes that value. The stack pointers are MSP and PSP; “SSP” appears to be a terminology slip here. See [Arm’s startup-file explanation](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4).

## Slide 11 — Microcontroller boot-sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=11|PDF page 11]]

## Slide 12 — Microcontroller boot-sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=12|PDF page 12]]

## Slide 13 — Microcontroller boot-sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=13|PDF page 13]]

## Slide 14 — Microcontroller boot-sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=14|PDF page 14]]

## Slide 15 — Microcontroller boot-sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-015.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=15|PDF page 15]]

## Slide 16 — Microcontroller boot-sequence

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-016.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=16|PDF page 16]]

## Slide 17 — STMicroelectronics startup code

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-017.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=17|PDF page 17]]

## Slide 18 — Vector table

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-018.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=18|PDF page 18]]

> [!note] Comment
> This is an abbreviated vector-table illustration. Real Cortex-M tables include reserved slots at architecture-defined offsets; deleting those slots would shift every subsequent handler to the wrong exception number. Treat the displayed sequence as an explanation of the entries, rather than a complete table to copy into a project. See [Arm’s vector-table layout, §2.3.4](https://documentation-service.arm.com/static/5f2ac4ab60a93e65927bbdbf).

## Slide 19 — Reset handler

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-019.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=19|PDF page 19]]

## Slide 20 — DATA section

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-020.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=20|PDF page 20]]

> [!note] Comment
> LMA is the load-memory address of the initial bytes in flash; VMA is the address used while the program runs in RAM. With an 8-byte DATA section, the loop copies offsets 4 and then 0. The linker symbols provide addresses and bounds; they are not ordinary variables containing the application data.

## Slide 21 — DATA section

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-021.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=21|PDF page 21]]

> [!note] Comment
> Apparent heading error: although the title says “DATA section,” the symbols `__bss_start__`/`__bss_end__` and stores of zero show BSS initialization. It is the zero-fill counterpart of the copy operation on the preceding page.

## Slide 22 — Application start

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-022.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=22|PDF page 22]]

## Slide 23 — Infineon startup code

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-023.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=23|PDF page 23]]

## Slide 24 — Vector table

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-024.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=24|PDF page 24]]

## Slide 25 — Reset handler

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-025.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=25|PDF page 25]]

> [!note] Comment
> The excerpt places the default-handler definition after the `SystemInit` call. Read it as selected fragments: if execution literally fell through into `Default_Handler`, the `b .` instruction would loop forever instead of reaching the later memory-initialization code. The complete startup file must provide the intended continuation.

## Slide 26 — DATA section

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-026.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=26|PDF page 26]]

> [!note] Comment
> Each copy-table entry is three 32-bit words: flash source address, RAM destination address, and byte count. The outer loop advances by 12 bytes to the next entry; the inner loop copies that section in 4-byte units. This handles several RAM regions using linker-generated descriptors instead of one hard-coded DATA range.

## Slide 27 — BSS section

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-027.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=27|PDF page 27]]

## Slide 28 — Application start

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-028.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=28|PDF page 28]]

> [!note] Comment
> Here `blx r0` is a function call to `main`, with a return address; this differs from the blanket “jump, not a function call” wording on page 10. The following `b .` deliberately traps execution if `main` returns. The assembly shown on each page determines which transfer is actually used.

## Slide 29 — Bootloader

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-029.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=29|PDF page 29]]

## Slide 30 — Bootloader

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-030.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=30|PDF page 30]]

## Slide 31 — Bootloader

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-031.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=31|PDF page 31]]

## Slide 32 — Bootloader

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-032.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=32|PDF page 32]]

> [!note] Comment
> The final two bullets describe alternative hardware capabilities, not two simultaneous requirements. Follow page 33 when an IVT relocation register is available; follow page 34 when the device instead supports the illustrated memory-remapping mechanism.

## Slide 33 — Bootloader – With IVT offset register

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-033.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=33|PDF page 33]]

## Slide 34 — Bootloader – Without IVT offset register

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Boot+of+a+system/slide-034.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Boot+of+a+system.pdf#page=34|PDF page 34]]
