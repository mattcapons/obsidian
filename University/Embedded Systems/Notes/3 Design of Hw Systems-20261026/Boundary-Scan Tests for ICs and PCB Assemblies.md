---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf]]'
source_pages: 9
annotation_style: slide-by-slide, concise English comments
---

# Boundary-Scan Tests for ICs and PCB Assemblies

Original deck: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf|Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf]]

Topic: Supplied nine-page article printout on JTAG boundary-scan architecture, test chains, and PCB test coverage.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Boundary-Scan Tests for ICs and PCB Assemblies

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-001.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=1|PDF page 1]]

## Slide 2 — Boundary-scan motivation and limits of physical probing

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-002.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=2|PDF page 2]]

> [!note] Comment
> Source limitation: the repeated Medium cookie notice obscures content at the top of pages 2–9, including part of the diagram on page 6. Those regions are already covered in the supplied PDF. The page images preserve the original printout; the hidden text and diagram details have not been reconstructed.

## Slide 3 — Test coverage and boundary-scan architecture

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-003.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=3|PDF page 3]]

## Slide 4 — Boundary-scan register and TAP controller

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-004.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=4|PDF page 4]]

## Slide 5 — TAP signals and boundary-scan testing

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-005.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=5|PDF page 5]]

> [!note] Comment
> For the external-interconnect test drawn here, the serial path runs through boundary-scan cells around the core logic. The test drives selected pins and captures connected inputs; the ordinary processor core need not execute the shifted bits. Compare the register-selection explanation in [[University/Embedded Systems/Notes/3 Design of Hw Systems-20261026/SOC, Distributes ESs, Prototyping platforms#Slide 19 — System-on-Chip|SoC and testability, page 19]].

## Slide 6 — Interconnect test example and PCB design for test

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-006.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=6|PDF page 6]]

> [!note] Comment
> Read each binary string as a sequence of test values for a pin, rather than one parallel word traveling on one wire. Compare the driven sequence at the left with the captured sequence at the right. The red mismatches indicate how an unintended short or open changes the observed response; the top of this source diagram is partly obscured.

## Slide 7 — Multiple-device chains and test benefits

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-007.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=7|PDF page 7]]

## Slide 8 — Drawbacks, tools, and conclusion

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-008.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=8|PDF page 8]]

## Slide 9 — Conclusion — continuation and article footer

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium/slide-009.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/Boundary-Scan Tests for ICs and PCB Assemblies _ by Amos Kingatua _ Supplyframe _ Medium.pdf#page=9|PDF page 9]]
