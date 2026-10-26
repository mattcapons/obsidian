---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf]]'
source_pages: 74
annotation_style: slide-by-slide, concise English comments
---

# PCB Design with Altium - Eagle_WF_2019

Original deck: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf|PCB Design with Altium - Eagle_WF_2019.pdf]]

Topic: Historical Altium and EAGLE walkthroughs from schematic capture to PCB routing, rule checks, 3D views, and manufacturing outputs.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — PCB Design through Altium Designer & Eagle

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-001.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=1|PDF page 1]]

## Slide 2 — PCB Design Workflow

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-002.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=2|PDF page 2]]

## Slide 3 — Altium Designer PCB Design

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-003.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=3|PDF page 3]]

## Slide 4 — Altium Designer PCB Design

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-004.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=4|PDF page 4]]

## Slide 5 — The Design

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-005.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=5|PDF page 5]]

## Slide 6 — Creating a New PCB Project

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-006.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=6|PDF page 6]]

## Slide 7 — Adding a Schematic to the Project

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-007.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=7|PDF page 7]]

## Slide 8 — Setting the Document Options : Sheet Size, Snap & Visible Grid

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-008.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=8|PDF page 8]]

> [!note] Comment
> A mil is one thousandth of an inch, so the 100 mil grid corresponds to 2.54 mm. The snap grid constrains where objects can be placed; changing the visible grid alone need not change that placement constraint. Distinguish this schematic spacing from the later PCB dimensions and routing rules.

## Slide 9 — Components and Libraries in Altium Designer

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-009.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=9|PDF page 9]]

> [!note] Comment
> The library symbol supplies logical pins; the footprint supplies physical pads on the board. Their pin-to-pad mapping connects these two representations. See [[University/Embedded Systems/Notes/3 Design of Hw Systems-20261026/2021 PCB based design#Slide 25 — Footprints|PCB based design, page 25]] for why a correct symbol still needs the correct package footprint.

## Slide 10 — Accessing Components

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-010.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=10|PDF page 10]]

## Slide 11 — Making Libraries Available to Access the Components

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-011.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=11|PDF page 11]]

## Slide 12 — Finding a Component in Libraries

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-012.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=12|PDF page 12]]

## Slide 13 — Multivibrator Parts

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-013.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=13|PDF page 13]]

## Slide 14 — Placing Components on the Schematic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-014.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=14|PDF page 14]]

## Slide 15 — Placing Components on the Schematic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-015.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=15|PDF page 15]]

## Slide 16 — Wiring

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-016.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=16|PDF page 16]]

## Slide 17 — Wiring

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-017.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=17|PDF page 17]]

## Slide 18 — Nets and Net Labels

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-018.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=18|PDF page 18]]

> [!note] Comment
> A net label names an electrical connection; it does not create a voltage source or impose the displayed voltage. Labeling the supply net “12V” identifies the intended supply connection. The actual voltage comes from the circuit and the connected source.

## Slide 19 — Check For Errors

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-019.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=19|PDF page 19]]

## Slide 20 — Creating a New PCB

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-020.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=20|PDF page 20]]

## Slide 21 — Creating a New PCB

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-021.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=21|PDF page 21]]

## Slide 22 — Configuring the Board Origin

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-022.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=22|PDF page 22]]

## Slide 23 — Configuring the Board Grid

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-023.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=23|PDF page 23]]

## Slide 24 — Configuring the Board Shape

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-024.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=24|PDF page 24]]

## Slide 25 — Transferring the Design to PCB Layout

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-025.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=25|PDF page 25]]

## Slide 26 — Transferring the Design to PCB Layout

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-026.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=26|PDF page 26]]

> [!note] Comment
> The thin connection lines show required connections from the schematic before copper has been routed. They guide placement but are not conducting tracks. Compare page 37, where the routed copper paths replace those connection requirements with physical geometry.

## Slide 27 — Configuring the Layer Visibility

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-027.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=27|PDF page 27]]

## Slide 28 — Physical Layers and the Layer Stack Manager

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-028.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=28|PDF page 28]]

## Slide 29 — Routing Width Design Rules : Signal Nets

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-029.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=29|PDF page 29]]

## Slide 30 — Routing Width Design Rules : Power Nets

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-030.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=30|PDF page 30]]

## Slide 31 — Defining the Electrical Clearance Constraint

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-031.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=31|PDF page 31]]

## Slide 32 — Defining the Routing Via Style

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-032.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=32|PDF page 32]]

> [!note] Comment
> Via diameter and hole size are different dimensions. With a 1 mm outer diameter and a 0.6 mm hole, the nominal radial copper ring is $(1-0.6)/2=0.2$ mm before manufacturing tolerances. This is the copper surrounding the drilled hole, not the hole diameter itself.

## Slide 33 — Position and Placement

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-033.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=33|PDF page 33]]

## Slide 34 — Position and Placement

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-034.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=34|PDF page 34]]

## Slide 35 — Interactively Routing the Board

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-035.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=35|PDF page 35]]

## Slide 36 — Time to Route

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-036.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=36|PDF page 36]]

## Slide 37 — Time to Route

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-037.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=37|PDF page 37]]

## Slide 38 — Active Route: Automated Interactive Router

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-038.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=38|PDF page 38]]

## Slide 39 — Design Rule Check (DRC)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-039.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=39|PDF page 39]]

## Slide 40 — Configuring the Rule Checker

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-040.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=40|PDF page 40]]

> [!note] Comment
> DRC checks the layout against the enabled geometric and connectivity constraints. A clean report means those selected checks pass; it does not establish that the schematic implements the intended function. The rule scopes and limits configured on the preceding pages determine what the checker can report.

## Slide 41 — Running a Design Rule Check (DRC)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-041.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=41|PDF page 41]]

## Slide 42 — PCB in 3D

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-042.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=42|PDF page 42]]

## Slide 43 — Output Documentation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-043.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=43|PDF page 43]]

## Slide 44 — Output Documentation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-044.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=44|PDF page 44]]

## Slide 45 — Generating Output

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-045.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=45|PDF page 45]]

## Slide 46 — Generating Output: Gerber

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-046.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=46|PDF page 46]]

## Slide 47 — Configuring Gerber generation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-047.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=47|PDF page 47]]

> [!note] Comment
> In the shown millimeter format, 4:3 allocates four integer digits and three fractional digits, giving a coordinate increment of 0.001 mm. The drill and Gerber data must describe the same physical coordinates, so consistent units, format, and origin matter when the files are combined by the manufacturer.

## Slide 48 — Configuring Gerber generation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-048.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=48|PDF page 48]]

## Slide 49 — Configuring Gerber generation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-049.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=49|PDF page 49]]

## Slide 50 — PCB Design: Eagle

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-050.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=50|PDF page 50]]

## Slide 51 — What’s EAGLE?

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-051.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=51|PDF page 51]]

## Slide 52 — Overview – Control panel

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-052.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=52|PDF page 52]]

## Slide 53 — New Project

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-053.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=53|PDF page 53]]

## Slide 54 — Libraries

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-054.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=54|PDF page 54]]

## Slide 55 — Schematic

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-055.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=55|PDF page 55]]

## Slide 56 — Spice Simulation

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-056.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=56|PDF page 56]]

## Slide 57 — Hierarchy

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-057.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=57|PDF page 57]]

> [!note] Comment
> Source limitation: the screenshot overlaps part of instruction 4 in the supplied PDF. That part of the instruction is unreadable in the original page; the image preserves the overlap without inventing the missing words.

## Slide 58 — Checking the schematic and creating the board

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-058.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=58|PDF page 58]]

## Slide 59 — Design Link

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-059.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=59|PDF page 59]]

## Slide 60 — Placing and routing

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-060.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=60|PDF page 60]]

## Slide 61 — Power ang GND planes

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-061.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=61|PDF page 61]]

## Slide 62 — Layers

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-062.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=62|PDF page 62]]

## Slide 63 — Autorouting

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-063.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=63|PDF page 63]]

## Slide 64 — Autorouting

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-064.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=64|PDF page 64]]

> [!note] Comment
> The routing percentage describes how much of the required connectivity the routing attempt completed; the via count describes one aspect of its geometry. A 100% result still needs the design-rule check on the next page. Neither number alone evaluates signal behavior or whether the chosen placement is suitable.

## Slide 65 — Design Rule Check (DRC)

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-065.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=65|PDF page 65]]

## Slide 66 — Adjust Board Design

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-066.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=66|PDF page 66]]

## Slide 67 — Fusion 360

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-067.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=67|PDF page 67]]

## Slide 68 — Fusion 360

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-068.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=68|PDF page 68]]

## Slide 69 — Fusion 360

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-069.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=69|PDF page 69]]

## Slide 70 — CAM Processor

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-070.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=70|PDF page 70]]

## Slide 71 — CAM Processor

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-071.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=71|PDF page 71]]

## Slide 72 — Design Completed

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-072.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=72|PDF page 72]]

## Slide 73 — Conclusions: Altium vs Eagle

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-073.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=73|PDF page 73]]

## Slide 74 — Web-based references

![[University/Embedded Systems/Attachments/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019/slide-074.png]]

Source: [[University/Embedded Systems/Slides/3 Design of Hw Systems-20261026/PCB Design with Altium - Eagle_WF_2019.pdf#page=74|PDF page 74]]
