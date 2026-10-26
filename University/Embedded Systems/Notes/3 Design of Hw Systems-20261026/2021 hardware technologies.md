---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf]]'
source_pages: 63
annotation_style: slide-by-slide, concise English comments
---

# 2021 hardware technologies

Original deck: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf|2021 hardware technologies.pdf]]

Topic: IC fabrication and packaging, custom design, programmable logic families, and FPGA structure and implementation.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Embedded Systems — Hardware Technologies for ICs

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-001.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=1|PDF page 1]]

## Slide 2 — Outline

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-002.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=2|PDF page 2]]

## Slide 3 — Hardware Technologies for ICs

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-003.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=3|PDF page 3]]

## Slide 4 — Hardware

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-004.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=4|PDF page 4]]

## Slide 5 — (AS) ICs

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-005.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=5|PDF page 5]]

## Slide 6 — (AS)IC – a pill of history

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-006.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=6|PDF page 6]]

> [!note] Comment
> Apparent corporate-history error: “Fairchild Semiconductor, today ST” conflates different company histories. Fairchild was acquired by ON Semiconductor in 2016; ST was formed by combining SGS and Thomson semiconductor businesses in 1987. See [onsemi’s acquisition letter](https://www.onsemi.com/site/pdf/Fairchild-Customer-Letter.pdf) and [ST’s history](https://investors.st.com/resources/faqs).

## Slide 7 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-007.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=7|PDF page 7]]

## Slide 8 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-008.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=8|PDF page 8]]

## Slide 9 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-009.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=9|PDF page 9]]

## Slide 10 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-010.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=10|PDF page 10]]

> [!note] Comment
> The cross-sections show selective processing: the mask defines which regions are exposed, so later removal or modification acts only where intended. Read pages 10–12 as successive stages of one example, not as unrelated completed devices. Page 13 explicitly identifies this example as bipolar-transistor fabrication rather than a complete CMOS process.

## Slide 11 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-011.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=11|PDF page 11]]

## Slide 12 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-012.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=12|PDF page 12]]

## Slide 13 — (AS)IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-013.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=13|PDF page 13]]

## Slide 14 — Complete view of the chain to produce a die

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-014.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=14|PDF page 14]]

## Slide 15 — Bonding and packaging

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-015.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=15|PDF page 15]]

## Slide 16 — Most ICs are bonded to small IC packages

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-016.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=16|PDF page 16]]

## Slide 17 — Never-ending evolution of IC packages

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-017.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=17|PDF page 17]]

## Slide 18 — Full custom design of IC

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-018.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=18|PDF page 18]]

## Slide 19 — Use of regular structures

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-019.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=19|PDF page 19]]

## Slide 20 — Standard cells: higher abstraction of the design

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-020.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=20|PDF page 20]]

> [!note] Comment
> A standard cell is already characterized and laid out for a particular fabrication technology. The designer combines these cells instead of drawing every transistor. A common cell height permits rows; routing then connects pins across those rows. “Manhattan geometry” refers to horizontal and vertical routing directions.

## Slide 21 — Standard cells

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-021.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=21|PDF page 21]]

## Slide 22 — Use of regular structures

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-022.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=22|PDF page 22]]

## Slide 23 — Programmable and Reprogrammable Technologies

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-023.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=23|PDF page 23]]

## Slide 24 — Programmable logic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-024.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=24|PDF page 24]]

## Slide 25 — Programmable logic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-025.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=25|PDF page 25]]

## Slide 26 — Programming

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-026.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=26|PDF page 26]]

## Slide 27 — Programming

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-027.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=27|PDF page 27]]

## Slide 28 — Programming modes

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-028.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=28|PDF page 28]]

## Slide 29 — Programming modes

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-029.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=29|PDF page 29]]

> [!note] Comment
> The stored SRAM bit controls a physical switch between wires. Loading configuration bits therefore changes the circuit’s connectivity; it is different from sending ordinary program instructions to a fixed CPU. Since SRAM is volatile, this configuration must be restored after power loss unless another mechanism stores it persistently.

## Slide 30 — Programming modes

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-030.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=30|PDF page 30]]

## Slide 31 — Connections

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-031.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=31|PDF page 31]]

## Slide 32 — Connections

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-032.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=32|PDF page 32]]

## Slide 33 — Connections

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-033.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=33|PDF page 33]]

## Slide 34 — Connections

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-034.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=34|PDF page 34]]

> [!note] Comment
> Apparent acronym swap: the expansions of PAL and PLA are reversed in this list. Pages 37, 39, and 40 consistently give PLA = Programmable Logic Array, and PAL = Programmable Array Logic. Use those later diagrams to distinguish which AND/OR planes are programmable.

## Slide 35 — 2-level programmable logic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-035.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=35|PDF page 35]]

## Slide 36 — General structure

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-036.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=36|PDF page 36]]

## Slide 37 — Main types

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-037.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=37|PDF page 37]]

## Slide 38 — Read-Only Memory (ROM/PROM)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-038.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=38|PDF page 38]]

> [!note] Comment
> With $n$ input bits, the decoder generates $2^n$ possible minterms, one per address. Each of the $m$ output bits selects the minterms for which it should be 1. A ROM implementing a three-input, four-output truth table therefore stores $2^3\times4=32$ bits.

## Slide 39 — Programmable Logic Array (PLA)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-039.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=39|PDF page 39]]

> [!note] Comment
> A PLA need not generate every minterm. For $f=ab+a\bar c$, two AND terms are sufficient: connect $a,b$ to one product line and $a,\bar c$ to another, then connect both products to the output OR. Unlike a full minterm, a product term can omit an input.

## Slide 40 — Programmable Array Logic (PAL)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-040.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=40|PDF page 40]]

## Slide 41 — Multi-level programmable logic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-041.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=41|PDF page 41]]

## Slide 42 — Multi-level logic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-042.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=42|PDF page 42]]

## Slide 43 — Advanced PLA and PAL

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-043.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=43|PDF page 43]]

> [!note] Comment
> The output-select multiplexer can choose a combinational result or the stored flip-flop value. Feeding a registered output back into the logic supplies the current state for a finite-state machine. The clock advances that state; the combinational AND/OR network computes outputs and next-state values between clock edges.

## Slide 44 — Generic Array Logic (GAL)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-044.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=44|PDF page 44]]

## Slide 45 — Complex Programmable Logic Devices

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-045.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=45|PDF page 45]]

## Slide 46 — Complex Programmable Logic Devices

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-046.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=46|PDF page 46]]

## Slide 47 — Complex Programmable Logic Devices

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-047.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=47|PDF page 47]]

## Slide 48 — Field Programmable Gate Arrays

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-048.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=48|PDF page 48]]

## Slide 49 — FPGA

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-049.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=49|PDF page 49]]

## Slide 50 — FPGA – main aspects

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-050.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=50|PDF page 50]]

## Slide 51 — FPGA – other aspects

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-051.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=51|PDF page 51]]

## Slide 52 — Comparisons

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-052.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=52|PDF page 52]]

## Slide 53 — FPGA

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-053.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=53|PDF page 53]]

> [!note] Comment
> A LUT4 stores the truth table of a four-input Boolean function: $2^4=16$ configuration bits. The input pattern selects one stored result. The surrounding multiplexers choose signal paths and whether an output bypasses the flip-flop or is registered, so a logic block supports both combinational and sequential circuits.

## Slide 54 — FPGA – Design flow

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-054.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=54|PDF page 54]]

## Slide 55 — FPGA – Design flow, typical split

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-055.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=55|PDF page 55]]

> [!note] Comment
> Synthesis converts HDL behavior into a network of logic resources. Place-and-route assigns those resources to actual FPGA locations and wires; the bitstream encodes the resulting configuration. Functional simulation checks behavior, while timing analysis checks whether signal paths satisfy constraints such as the requested clock period.

## Slide 56 — VIVADO integrated support of the design phases

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-056.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=56|PDF page 56]]

## Slide 57 — CLB in Xilinx 7 Series - example

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-057.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=57|PDF page 57]]

> [!note] Comment
> The RAM and shift-register uses are alternative configurations of a SLICEM LUT, rather than extra resources simultaneously available beside that same LUT’s full logic function. Resource totals in the next tables must therefore be read with the chosen configuration in mind.

## Slide 58 — 7 Series CLB main features

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-058.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=58|PDF page 58]]

## Slide 59 — Artix and Spartan, the popular ones

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-059.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=59|PDF page 59]]

## Slide 60 — No compromise: Virtex-7

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-060.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=60|PDF page 60]]

## Slide 61 — ASMBL architecture

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-061.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=61|PDF page 61]]

## Slide 62 — Simplified view of Virtex 7 series FPGA slice cell

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-062.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=62|PDF page 62]]

## Slide 63 — “Simplified” Virtex 7 series FPGA slice cells

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/2021 hardware technologies/slide-063.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/2021 hardware technologies.pdf#page=63|PDF page 63]]
