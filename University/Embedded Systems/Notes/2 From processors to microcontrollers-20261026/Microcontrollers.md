---
course: Embedded Systems
source: '[[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf]]'
source_pages: 80
annotation_style: slide-by-slide, concise English comments
---

# Microcontrollers

Original deck: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf|Microcontrollers.pdf]]

Topic: MCU organization, clock trees, memory maps, GPIO, analog peripherals, timers, and SPI/UART/I2C.

[[University/Embedded Systems/Embedded Systems|Course index]]

## Slide 1 — Embedded Systems — Microcontrollers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-001.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=1|PDF page 1]]

## Slide 2 — Microprocessors

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-002.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=2|PDF page 2]]

## Slide 3 — Microprocessors

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-003.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=3|PDF page 3]]

## Slide 4 — Microcontroller

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-004.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=4|PDF page 4]]

> [!note] Comment
> The numeric ranges on this and page 2 characterize the lecture’s 2020–2021 examples. The architectural distinction being illustrated is integration: an MCU combines its processing core, small memories, and peripherals on one chip, as the next diagram shows. Do not use these ranges as universal selection limits.

## Slide 5 — Microcontrollers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-005.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=5|PDF page 5]]

## Slide 6 — Example of common microcontrollers

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-006.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=6|PDF page 6]]

## Slide 7 — Example: NXP HCS08

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-007.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=7|PDF page 7]]

## Slide 8 — Example: NXP LPC111x – Cortex M0

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-008.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=8|PDF page 8]]

## Slide 9 — Example: Infineon XMC1000 – Cortex M0

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-009.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=9|PDF page 9]]

## Slide 10 — Example : STM STM32F0 – Cortex M0

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-010.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=10|PDF page 10]]

## Slide 11 — Example: Infineon XMC4700 – Cortex M4

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-011.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=11|PDF page 11]]

## Slide 12 — Microcontroller subsystems — Clock

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-012.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=12|PDF page 12]]

## Slide 13 — Clocks

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-013.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=13|PDF page 13]]

> [!note] Comment
> The RTC frequency is convenient because $32768=2^{15}$: fifteen divide-by-two stages yield a 1 Hz tick. A separate slow clock can maintain time while the faster core clock is stopped, provided the RTC clock domain remains powered.

## Slide 14 — Clocks

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-014.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=14|PDF page 14]]

## Slide 15 — Clocks

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-015.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=15|PDF page 15]]

## Slide 16 — Clocks

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-016.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=16|PDF page 16]]

> [!note] Comment
> “ppm” means parts per million of fractional frequency error. A constant error of 20 ppm gives approximately $20\times10^{-6}\times86400=1.728$ seconds of time error per day. The same percentage error can be acceptable for a timeout and unacceptable for long-term calendar timekeeping.

## Slide 17 — Clock distribution: NXP HCS08

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-017.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=17|PDF page 17]]

## Slide 18 — Clock distribution: NXP LPC111x

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-018.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=18|PDF page 18]]

> [!note] Comment
> Read the clock tree from left to right. Multiplexers select a source; the PLL changes frequency; dividers reduce it; enable-controlled gates stop clock delivery to individual blocks. Selecting a working source and enabling a peripheral’s gate are separate configuration steps.

## Slide 19 — Clock distribution: STM STM32F0

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-019.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=19|PDF page 19]]

## Slide 20 — Microcontroller subsystems — Memory

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-020.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=20|PDF page 20]]

## Slide 21 — Memory

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-021.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=21|PDF page 21]]

## Slide 22 — Memory

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-022.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=22|PDF page 22]]

## Slide 23 — Memory map: NXP HCS08

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-023.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=23|PDF page 23]]

## Slide 24 — Memory map: STM STM32F0

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-024.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=24|PDF page 24]]

> [!note] Comment
> The left column is an address-space map, not a picture of the amount of memory physically installed. The expanded views identify implemented regions and reserved holes. Notice the flash region at `0x08000000` and the boot-dependent mapping at zero; these help interpret the address ambiguity in [[University/Embedded Systems/Notes/2 From processors to microcontrollers-20261026/Boot of a system#Slide 9 — Microcontroller boot sequence|Boot, page 9]].

## Slide 25 — Banked memory

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-025.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=25|PDF page 25]]

## Slide 26 — Banked memory: HCS12X

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-026.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=26|PDF page 26]]

## Slide 27 — Banked memory: HCS12X

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-027.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=27|PDF page 27]]

## Slide 28 — Banked memory: HCS12X

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-028.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=28|PDF page 28]]

> [!note] Comment
> PPAGE selects which part of global flash appears in the fixed 16 KB local window. The same local address inside that window can therefore refer to different physical bytes after PPAGE changes. The unpaged regions stay directly accessible, which is useful for code that must remain reachable while a bank is switched.

## Slide 29 — Microcontroller subsystems — GPIO

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-029.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=29|PDF page 29]]

## Slide 30 — GPIO

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-030.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=30|PDF page 30]]

## Slide 31 — GPIO: Analog Input

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-031.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=31|PDF page 31]]

> [!note] Comment
> The blue overlay marks the active path for this configuration; the other wires show alternative uses of the same pin. Across pages 31–35, follow that overlay to distinguish analog routing, a sampled digital input, software-driven output, and output driven directly by a peripheral.

## Slide 32 — GPIO: Digital Input

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-032.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=32|PDF page 32]]

## Slide 33 — GPIO: Digital input to alternate function

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-033.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=33|PDF page 33]]

## Slide 34 — GPIO: Digital Output

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-034.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=34|PDF page 34]]

## Slide 35 — GPIO: Digital output from alternate function

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-035.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=35|PDF page 35]]

## Slide 36 — GPIO: Functionalities overview

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-036.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=36|PDF page 36]]

## Slide 37 — Microcontroller subsystems — Analog comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-037.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=37|PDF page 37]]

## Slide 38 — Comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-038.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=38|PDF page 38]]

## Slide 39 — Comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-039.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=39|PDF page 39]]

## Slide 40 — Comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-040.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=40|PDF page 40]]

## Slide 41 — Comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-041.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=41|PDF page 41]]

## Slide 42 — Comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-042.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=42|PDF page 42]]

## Slide 43 — Comparators

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-043.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=43|PDF page 43]]

> [!note] Comment
> “Front” means an edge of the digital comparator output. Counting measures how many such edges occur; capture latches the timer count at an edge. If two captures differ by $\Delta C$ ticks at timer frequency $f_t$, the interval is $\Delta t=\Delta C/f_t$, with overflow accounting when needed.

## Slide 44 — Microcontroller subsystems — Analog to Digital Converter

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-044.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=44|PDF page 44]]

## Slide 45 — ADC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-045.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=45|PDF page 45]]

## Slide 46 — ADC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-046.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=46|PDF page 46]]

> [!note] Comment
> Terminology ambiguity: a fixed reference and a ratiometric measurement are different ways to manage supply dependence. In a ratiometric arrangement the sensor excitation and ADC reference track the same supply, so their ratio stays stable. A fixed reference instead anchors the conversion scale independently. See [Analog Devices’ ratiometric measurement explanation](https://www.analog.com/en/resources/analog-dialogue/articles/2021/05/21/14/24/how-to-select-and-design-the-best-rtd-temperature-sensing-system.html).

## Slide 47 — ADC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-047.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=47|PDF page 47]]

## Slide 48 — ADC: NXP HCS08

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-048.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=48|PDF page 48]]

## Slide 49 — ADC: STM STM32F0

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-049.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=49|PDF page 49]]

## Slide 50 — ADC: Infineon XMC4700

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-050.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=50|PDF page 50]]

## Slide 51 — Microcontroller subsystems — Real Time Clock

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-051.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=51|PDF page 51]]

## Slide 52 — RTC

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-052.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=52|PDF page 52]]

> [!note] Comment
> The annual drift follows directly from fractional frequency error: $5\times10^{-6}\times365\times24\times3600=157.68$ seconds. This assumes a constant 5 ppm offset; temperature-dependent changes can alter both the magnitude and direction of the actual accumulated error.

## Slide 53 — RTC: Infineon XMC4700

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-053.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=53|PDF page 53]]

## Slide 54 — Timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-054.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=54|PDF page 54]]

## Slide 55 — Timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-055.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=55|PDF page 55]]

## Slide 56 — Timer

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-056.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=56|PDF page 56]]

> [!note] Comment
> Apparent label mismatch: the right-hand picture is captioned “Single shot,” but its internal labels show two capture events and a time difference, matching page 55’s capture diagram. Use the picture for interval capture; it does not illustrate a one-shot timer stopping at a programmed terminal count.

## Slide 57 — Watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-057.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=57|PDF page 57]]

## Slide 58 — Watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-058.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=58|PDF page 58]]

## Slide 59 — Watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-059.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=59|PDF page 59]]

## Slide 60 — Watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-060.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=60|PDF page 60]]

## Slide 61 — Watchdog

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-061.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=61|PDF page 61]]

## Slide 62 — Communication — SPI Bus

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-062.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=62|PDF page 62]]

## Slide 63 — SPI

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-063.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=63|PDF page 63]]

## Slide 64 — SPI

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-064.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=64|PDF page 64]]

## Slide 65 — SPI

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-065.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=65|PDF page 65]]

> [!note] Comment
> CPOL determines the idle level of SCK; the two panels illustrate different sampling phases. Data changes on one clock edge and is sampled on the other. Both devices must agree on the mode, otherwise one may sample during a transition rather than after the bit has settled.

## Slide 66 — SPI Operation

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-066.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=66|PDF page 66]]

## Slide 67 — SPI Operation

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-067.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=67|PDF page 67]]

## Slide 68 — Communication — UART

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-068.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=68|PDF page 68]]

## Slide 69 — UART

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-069.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=69|PDF page 69]]

## Slide 70 — UART

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-070.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=70|PDF page 70]]

## Slide 71 — UART

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-071.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=71|PDF page 71]]

> [!note] Comment
> 8N1 carries eight payload bits in ten transmitted bit-times: one start, eight data, one stop. Thus at 115200 bit/s, the ideal continuous payload rate is $115200/10=11520$ bytes/s before higher-level protocol overhead. The start edge lets the receiver align its local sampling clock for each frame.

## Slide 72 — UART Operation

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-072.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=72|PDF page 72]]

## Slide 73 — Communication — I2C

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-073.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=73|PDF page 73]]

## Slide 74 — I2C

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-074.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=74|PDF page 74]]

## Slide 75 — I2C

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-075.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=75|PDF page 75]]

## Slide 76 — I2C Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-076.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=76|PDF page 76]]

## Slide 77 — I2C Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-077.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=77|PDF page 77]]

## Slide 78 — I2C Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-078.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=78|PDF page 78]]

## Slide 79 — I2C Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-079.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=79|PDF page 79]]

> [!note] Comment
> Apparent wording error: during a read, the master is the receiver and sends ACK after bytes it wants to continue receiving; it sends NACK after the final byte. The bullet assigning the final non-acknowledgment to the slave reverses that role. See [NXP’s I2C specification, §3.1.6](https://www.nxp.com/docs/en/user-guide/UM10204.pdf).

## Slide 80 — I2C Protocol

![[University/Embedded Systems/Attachments/2 From processors to microcontrollers-20261026/Microcontrollers/slide-080.png]]

Source: [[University/Embedded Systems/Slides/2 From processors to microcontrollers-20261026/Microcontrollers.pdf#page=80|PDF page 80]]

> [!note] Comment
> A common use of the write phase is to select a device register, then read its value after the repeated START. The bus remains occupied across the direction change. The final read-byte NACK is generated by the master, as explained on page 79; the same wording issue occurs here.
