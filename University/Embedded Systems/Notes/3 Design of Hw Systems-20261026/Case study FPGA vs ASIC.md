---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf]]'
source_pages: 36
annotation_style: slide-by-slide, concise English comments
---

# Case study FPGA vs ASIC

Original deck: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf|Case study FPGA vs ASIC.pdf]]

Topic: Feasibility study for replacing an FPGA-based UMTS subsystem with a mixed-signal ASIC, including area, packaging, NRE, and volume economics.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Re-engineering of an Embedded System: A Case Study

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-001.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=1|PDF page 1]]

## Slide 2 — Project goal: feasibility analysis for a reengineering

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-002.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=2|PDF page 2]]

## Slide 3 — Structure of the study

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-003.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=3|PDF page 3]]

## Slide 4 — The application

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-004.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=4|PDF page 4]]

## Slide 5 — The Application

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-005.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=5|PDF page 5]]

## Slide 6 — The Application

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-006.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=6|PDF page 6]]

> [!note] Comment
> Apparent conversion inconsistencies: using $1\ \mathrm{KiB}=1024$ bytes, $1290752$ ROM bits give $157.5625$ KiB, rather than the stated 179.5 Kbyte. Likewise, $16\times1024$ FIFO bits give 2 KiB, rather than 2.5. The RAM figure, $61440/8/1024=7.5$ KiB, is consistent. The slide alone does not establish whether the bit totals or the converted totals were intended.

## Slide 7 — Current implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-007.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=7|PDF page 7]]

## Slide 8 — Current Implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-008.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=8|PDF page 8]]

> [!note] Comment
> Equivalent gate count is an estimate of the implemented logic, not a direct count of FPGA configuration bits or an assurance of equal performance. The study explicitly reduces the estimated ASIC count from the FPGA equivalent. The later technology-density calculation uses the 2.5-million-gate ASIC estimate, while memory and analog area are budgeted separately.

## Slide 9 — Problem: High Pinout

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-009.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=9|PDF page 9]]

## Slide 10 — Proposed implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-010.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=10|PDF page 10]]

## Slide 11 — Implementation: details omitted

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-011.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=11|PDF page 11]]

## Slide 12 — Implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-012.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=12|PDF page 12]]

> [!note] Comment
> The axes compare sample rate with resolution. The power curves show the tradeoff at approximately constant dissipation: higher speed at the same resolution, or higher resolution at the same speed, generally moves toward a higher-power region of this chart. Use the required operating point to narrow candidates; the chart is not one ADC’s transfer characteristic.

## Slide 13 — Implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-013.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=13|PDF page 13]]

## Slide 14 — Implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-014.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=14|PDF page 14]]

## Slide 15 — Pinout and packaging

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-015.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=15|PDF page 15]]

> [!note] Comment
> The package budget includes power, ground, clocks, test access, and probes as well as functional signals. The listed groups sum to 210 connections, so a nominal 256-pin package leaves room beyond that estimate. This is why counting only the 104 digital signals would underestimate the required package.

## Slide 16 — Main goals of the implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-016.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=16|PDF page 16]]

## Slide 17 — Design Flow

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-017.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=17|PDF page 17]]

## Slide 18 — Design activities of the front-end

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-018.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=18|PDF page 18]]

## Slide 19 — Which silicon technology?

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-019.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=19|PDF page 19]]

## Slide 20 — Estimated size

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-020.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=20|PDF page 20]]

> [!note] Comment
> For the 0.18 µm estimate, $2.5\times10^6/(70\times10^3)\approx35.7\ \mathrm{mm}^2$ gives the digital-logic area, matching the rounded 36 in the table. Analog and RAM areas are then added. The resulting die area therefore cannot be inferred from digital gate density alone.

## Slide 21 — Other Steps/Cost to achieve a running prototype

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-021.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=21|PDF page 21]]

## Slide 22 — Foundry selection

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-022.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=22|PDF page 22]]

## Slide 23 — Foundry selection

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-023.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=23|PDF page 23]]

## Slide 24 — Proposed design plan

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-024.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=24|PDF page 24]]

## Slide 25 — Proposed design plan

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-025.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=25|PDF page 25]]

## Slide 26 — Selection of candidate foundries

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-026.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=26|PDF page 26]]

## Slide 27 — Cost analysis: COTS + FPGA (current)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-027.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=27|PDF page 27]]

## Slide 28 — Cost analysis: Single CHIP implementation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-028.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=28|PDF page 28]]

> [!note] Comment
> Cost-boundary ambiguity: page 27 retains a 36 USD PCB contribution and estimates about 12 USD savings from reducing the layer count. Here the wording appears to remove the full additional 36 USD. Keep those two assumptions separate when reproducing the comparison; the slides do not reconcile them.

## Slide 29 — Cost-Volume analysis

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-029.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=29|PDF page 29]]

> [!note] Comment
> Apparent unit error: the text says a die area of $60\ \mathrm{cm}^2$, while the preceding estimate is roughly $8\times7\ \mathrm{mm}^2$. The table is consistent with about $60\ \mathrm{mm}^2=0.6\ \mathrm{cm}^2$: at $30\ \mathrm{USD}/\mathrm{cm}^2$, 30,000 dies cost 540,000 USD, and adding about 759,000 USD NRE gives the displayed 1.30 million USD. Read the printed area unit with this qualification.

## Slide 30 — Foundry A - Breakeven

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-030.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=30|PDF page 30]]

> [!note] Comment
> With a fixed development cost $C_0$ and per-unit costs $c_{\mathrm{COTS}}$ and $c_{\mathrm{ASIC}}$, break-even satisfies $C_0+Nc_{\mathrm{ASIC}}=Nc_{\mathrm{COTS}}$. Thus $N=C_0/(c_{\mathrm{COTS}}-c_{\mathrm{ASIC}})$. For the study’s 759,000 USD NRE, 230 USD COTS cost, and 18 USD ASIC unit cost, this is about 3,580 units. The result changes with the PCB-cost assumption flagged on page 28.

## Slide 31 — ASIC vs COTS+FPGA savings

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-031.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=31|PDF page 31]]

## Slide 32 — Summary of Results

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-032.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=32|PDF page 32]]

## Slide 33 — Summary of results

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-033.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=33|PDF page 33]]

## Slide 34 — Towards a refined feasibility study

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-034.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=34|PDF page 34]]

## Slide 35 — Some issues for the refined analysis

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-035.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=35|PDF page 35]]

## Slide 36 — Concluding Remarks

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC/slide-036.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Case study FPGA vs ASIC.pdf#page=36|PDF page 36]]
