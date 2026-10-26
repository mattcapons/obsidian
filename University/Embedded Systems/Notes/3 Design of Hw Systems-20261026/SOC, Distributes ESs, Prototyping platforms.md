---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf]]'
source_pages: 49
annotation_style: slide-by-slide, concise English comments
---

# SOC, Distributes ESs, Prototyping platforms

Original deck: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf|SOC, Distributes ESs, Prototyping platforms.pdf]]

Topic: SoC partitioning and interconnects, design for testability, distributed systems, and prototyping platforms.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Embedded Systems — Architectures and Design Styles

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-001.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=1|PDF page 1]]

## Slide 2 — Outline

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-002.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=2|PDF page 2]]

## Slide 3 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-003.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=3|PDF page 3]]

## Slide 4 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-004.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=4|PDF page 4]]

## Slide 5 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-005.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=5|PDF page 5]]

## Slide 6 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-006.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=6|PDF page 6]]

## Slide 7 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-007.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=7|PDF page 7]]

## Slide 8 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-008.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=8|PDF page 8]]

## Slide 9 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-009.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=9|PDF page 9]]

> [!note] Comment
> Putting data near each computing block reduces traffic to a shared memory, but copies or ownership then need coordination. For example, one accelerator must finish writing its result before another consumes it. Centralized memory simplifies locating shared data, while multiple simultaneous accesses can contend for the same resource.

## Slide 10 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-010.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=10|PDF page 10]]

## Slide 11 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-011.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=11|PDF page 11]]

## Slide 12 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-012.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=12|PDF page 12]]

## Slide 13 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-013.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=13|PDF page 13]]

> [!note] Comment
> Here “sw” denotes a network switch. A transfer passes from its processing element through switches and links toward the destination. Independent transfers can use different parts of the mesh concurrently, but transfers sharing a link can contend. The topology supplies possible routes; it does not by itself guarantee latency or consistency.

## Slide 14 — Racap…

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-014.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=14|PDF page 14]]

## Slide 15 — Recap…

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-015.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=15|PDF page 15]]

## Slide 16 — Recap…

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-016.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=16|PDF page 16]]

## Slide 17 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-017.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=17|PDF page 17]]

## Slide 18 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-018.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=18|PDF page 18]]

## Slide 19 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-019.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=19|PDF page 19]]

> [!note] Comment
> The instruction register selects a test operation; the selected data register then lies on the serial path from TDI to TDO. BYPASS shortens that path through an unneeded device, while EXTEST targets external interconnections. Keep the control signals TMS/TCK distinct from the serial test-data signals TDI/TDO.

## Slide 20 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-020.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=20|PDF page 20]]

## Slide 21 — System-on-Chip

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-021.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=21|PDF page 21]]

> [!note] Comment
> The TPG supplies stimuli to the unit under test (UUT); the TRE/ORA evaluates responses under the BIST controller. “Signature based” here means compacting a sequence of test responses into a value for comparison. It is a test-analysis concept, distinct from the public-key digital signatures discussed in the OTA deck.

## Slide 22 — Distributed Embedded Systems

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-022.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=22|PDF page 22]]

## Slide 23 — Distributed/Networked ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-023.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=23|PDF page 23]]

## Slide 24 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-024.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=24|PDF page 24]]

## Slide 25 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-025.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=25|PDF page 25]]

## Slide 26 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-026.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=26|PDF page 26]]

> [!note] Comment
> Apparent wording error: the example calls CAN a “wireless” connection, but the automotive discussion refers to cabling and page 27 draws nodes on a shared bus. Read this CAN example as a wired field bus; it belongs with the wired automotive category on page 24.

## Slide 27 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-027.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=27|PDF page 27]]

## Slide 28 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-028.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=28|PDF page 28]]

## Slide 29 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-029.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=29|PDF page 29]]

## Slide 30 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-030.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=30|PDF page 30]]

## Slide 31 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-031.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=31|PDF page 31]]

## Slide 32 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-032.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=32|PDF page 32]]

> [!note] Comment
> The local SPI/I2C links connect components within a sensor node, such as its MCU and radio chip. The wireless link connects separate nodes. These are different levels of communication: choosing a radio protocol does not determine how the MCU communicates with that radio inside the node.

## Slide 33 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-033.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=33|PDF page 33]]

## Slide 34 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-034.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=34|PDF page 34]]

## Slide 35 — Distributed ES

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-035.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=35|PDF page 35]]

## Slide 36 — Platforms for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-036.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=36|PDF page 36]]

## Slide 37 — Platforms and Kits for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-037.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=37|PDF page 37]]

## Slide 38 — Platforms and Kits for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-038.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=38|PDF page 38]]

## Slide 39 — Platforms and Kits for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-039.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=39|PDF page 39]]

## Slide 40 — Platforms and Kits for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-040.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=40|PDF page 40]]

> [!note] Comment
> HAL means hardware abstraction layer; BSP means board support package. They provide software support for the target hardware and board wiring so the application can use the available peripherals. Their presence reduces bring-up work, but the application still needs to be verified with the actual board configuration.

## Slide 41 — Platforms and Kits for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-041.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=41|PDF page 41]]

## Slide 42 — STM32 Nucleo Pack

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-042.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=42|PDF page 42]]

## Slide 43 — Platforms for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-043.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=43|PDF page 43]]

## Slide 44 — Platforms for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-044.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=44|PDF page 44]]

## Slide 45 — Example for development of apps on DSP (TMDXEVM6455)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-045.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=45|PDF page 45]]

> [!note] Comment
> Apparent processor-type error: the slide calls the TMS320C6455 a floating-point DSP, but TI identifies it as a fixed-point C64x+ DSP. The quoted instruction throughput should therefore not be read as floating-point operations per second. See [TI’s device description](https://www.ti.com/product/TMS320C6455).

## Slide 46 — proFPGA uno V7 Prototyping System

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-046.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=46|PDF page 46]]

## Slide 47 — proFPGA uno V7 family

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-047.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=47|PDF page 47]]

## Slide 48 — Platforms for prototyping

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-048.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=48|PDF page 48]]

> [!note] Comment
> A working prototype validates selected behavior on the chosen platform. Moving to a product can change the board, package, power distribution, timing, or available resources. The final verification step therefore concerns the product implementation as well as the prototype’s application logic.

## Slide 49 — Conclusions

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms/slide-049.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms.pdf#page=49|PDF page 49]]
