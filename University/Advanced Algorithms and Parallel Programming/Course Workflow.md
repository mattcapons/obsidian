---
tags:
  - aapp
  - workflow
---
# Course Workflow

[[AAPP Index|Course index]] · Last collection review: 2026-10-12

## Location and conventions

- Vault: `/home/matteo/Documents/obsidian` (lowercase). The uppercase `/home/matteo/Documents/Obsidian` path in the reusable prompt does not exist in this environment.
- Course: `University/Advanced Algorithms and Parallel Programming/`; source PDFs in `Slides/`, one substantive note per deck in `Notes/`, selected slide renders in `Attachments/<note topic>/`.
- English, explained exam-preparation notes. Preserve filenames, frontmatter, annotations, existing images, and useful explanations. Minimal lecture properties are `tags: [aapp, lecture]`, a quoted `lecture`, and a quoted source wikilink.
- Follow lecture order 1, 2, 3, 4, 4b, 5, 6, 7. Include index/previous/next navigation where applicable, concept cross-links, assumptions, correctness and cost arguments, worked examples, takeaways, original exam practice with collapsed worked solutions, and revision questions with answers.
- Use wikilinks for notes and PDF pages, LaTeX for mathematics, fenced pseudocode, local Obsidian image embeds with captions and page attribution, and Markdown links for external sources. Escape alias pipes in tables. PDF references use physical PDF page numbers, not inferred labels.
- Consolidate repeated animation slides without omitting their final algorithm or proof. Inspect rendered pages when extraction misses diagrams or mathematical grouping. Label supplementary explanations and apparent slide errors. Keep the lecturer's terminology while stating necessary qualifications.
- Follow [[Study Note Prompts#Continue when new slides arrive]]; this note records the course-specific state.

## Explanation depth for future updates

The user requested a substantially more detailed treatment while keeping the established style and structure (2026-10-12). Topic coverage alone is not sufficient. Explain why each algorithmic step is valid, what each symbol represents, how an invariant is preserved, and how the intermediate calculations lead to the stated bound. Follow a short definition with intuition and a concrete example where possible. Do not leave a difficult concept as a one-sentence reference to a theorem or technique.

Keep existing top-level organization, filenames, properties, callouts, navigation, images, and user annotations. Expand within the relevant section and add focused subheadings where needed; avoid appending a disconnected second textbook at the end. Distinguish illustrative assumptions, exact counts, asymptotic bounds, and actual measured timings. Use examples small enough to trace fully, and add original practice to test the newly explained reasoning.

Prefer useful supplied diagrams, original exact explanatory diagrams, and selected attributed figures from authoritative external sources. Every image needs a local embed and an explanatory caption. External reproductions must identify author, work, figure/page, and source URL; original figures must be labeled as such. These notes are study aids, not a claim that new supplementary examples were assigned by the lecturer.

## Source mapping and revision baseline

No earlier Course Workflow or source fingerprint record was present. Lectures 6 and 7 were new to the note collection (no corresponding notes or index entries); their filesystem arrival dates are not asserted. The six existing notes were compared with current deck topics and page references, and no additional substantive coverage gap was identified in that comparison. Historical revision status of those PDFs cannot be established from a missing earlier workflow baseline. The hashes below establish a baseline for future comparisons, not evidence that older PDFs never changed.

| Source | Pages | Note | Coverage |
|---|---|---|---|
| [[lecture1-Intro-Course2026-2027.pdf]] | 12 | [[Course Introduction]] | 1–12: objectives, syllabus, prerequisites, assessment and contacts |
| [[lecture2-AlgorithmAsRecipe.pdf]] | 23 | [[Algorithm as recipes]] | 1–23: complexity, sorting, recurrences, mini-lab fragments |
| [[lecture3-DandC.pdf]] | 47 | [[Divide and Conquer]] | 1–47: recursive design, search, powering, matrices, VLSI layouts and conclusion |
| [[lecture4-PRAM.pdf]] | 36 | [[PRAM]] | 1–36: models, metrics, patterns, resource simulation, scaling and lab overview |
| [[lecture4b-ISPC.pdf]] | 45 | [[ISPC]] | 1–45: compilation, gangs, masks, reductions, tasks, matrix multiplication and Mandelbrot |
| [[lecture5-Randomization.pdf]] | 27 | [[Randomized Algorithms]] | 1–27: probability models, hiring, Las Vegas/Monte Carlo and sampling |
| [[lecture6-MinCut.pdf]] | 24 | [[Minimum Cut]] | 1–24: contraction, proof, repetition, Karger–Stein, counting corollary and references |
| [[lecture7-Sort.pdf]] | 96 | [[Sorting]] | 1–96: quicksort (4–49), lower bounds (51–59), counting (60–79), radix (80–88), historical appendix (89–96) |

SHA-256 of the full source PDF bytes, recorded 2026-10-12:

```text
cbc5b0e85419a296ed8f541b15efdc10a4fbbf872158fb76c169500aa0d7a4db  lecture1-Intro-Course2026-2027.pdf
fdffc1b9019ed970eadda01f2fa79757105317400beb6115a3217a146747e35b  lecture2-AlgorithmAsRecipe.pdf
cd5d3c5a5355456236397fde05e0b97e49923b2d2de24482f918103c98ebff3e  lecture3-DandC.pdf
487c574dfa68dbf84b8282086c1ce2be827f9b3066ff780020d36ca99181399b  lecture4-PRAM.pdf
bb8174f6cef2edf0d9c03739cbef1b0cf210ab88223ac2cf5dbe3f701064b0b4  lecture4b-ISPC.pdf
616d6de645ad213ee44a40a0029342e760b6b9e7e852aebc043283dd1b385665  lecture5-Randomization.pdf
ca12b64251a6de0e63669432feb8d0cf05a3a1bb8eadd1fc9c3db0911f11f23a  lecture6-MinCut.pdf
c9c24973d1304f754ee850d59623fb1c0e3895908da1773938bec62f241dbc11  lecture7-Sort.pdf
```

For future updates, compare these hashes and the page mapping before editing. A changed hash signals that inspection is required; it does not by itself establish a substantive content change. Preserve user additions and document meaningful differences here rather than rewriting whole older notes. Add a row and fingerprint for each new source deck.

## Changes in this review

- Created [[Minimum Cut]] and [[Sorting]], covering both new decks with explanations, derivations, traces, original practice and solutions. Added six selected local slide images with source captions.
- Added the lectures to [[AAPP Index]], reading routes and practice links. Updated [[Course Introduction]] to eight supplied decks and linked the new applications from [[Randomized Algorithms]], [[Divide and Conquer]], and [[PRAM]]. Existing properties and images were preserved.
- Minimum-cut qualifications: nontrivial cuts, connected inputs, multiplicity-weighted edge sampling, conditional survival, single-run versus amplified work, exact small-graph base case. Corrected the apparent `n < 6` stopping error for the supplied ceiling formula and the “upper bound” wording on page 13.
- Sorting qualifications: distinctness for quicksort's expectation, recursion stack versus partition storage, stable placement, integer-key model, digit ceilings and the 2000-key pass example. Verified the parentheses in page 47's proof visually: there is no sign error. Corrected the historical company chronology on page 90 with a Census Bureau citation.
- Supplementary checks used Aspnes's Yale randomized-algorithm notes, Vigoda's min-cut lecture notes hosted at UCSB, MIT 6.006 sorting notes, and US Census Bureau history. Citations appear beside the relevant additions. The Georgia Tech URL for Vigoda returned HTTP 403; the UCSB copy was accessible. No external visuals were needed because the supplied diagrams suffice.

## Outstanding gaps and scope

- No newly supplied technical deck remains without a substantive note. Lecture 7's historical appendix is summarized for its relation to stable digit sorting; it is not transcribed verbatim, and its incidental anecdotes were not all independently verified.
- The eight decks do not establish full exam coverage. No additional explicit topic exclusions were found. Assessment statements remain attributed to the uploaded 2026–2027 introduction, not independently verified against later announcements or WeBeep.
- Still awaiting dedicated material for selection/order statistics, primality testing/cryptosystems, skip lists/treaps, dynamic programming, amortized/approximation/competitive methods, and further parallel tools and patterns announced by the introduction. Do not mark randomized selection covered simply because quicksort is now covered.
- Separate Colab notebooks mentioned by the review/PRAM slides were not supplied in the course folder. Existing notes explain the visible fragments and proposed experiments; they do not verify unavailable notebook contents or reproduce benchmark measurements.
- Source labels differ: introduction and min-cut are 2026–2027, the recipe review is 2023–2024, and sorting is 2021–2022. Preserve these provenance distinctions.

## Verification

Review checks include resolving course wikilinks and heading anchors, checking PDF page bounds, opening embedded image files, checking Markdown table separators and property syntax, and recalculating the new worked examples. Source PDFs and pre-existing images are retained unchanged. A source fingerprint allows later verification of that statement and reliable revision detection.

Results for this review: 294 internal references resolved (including heading anchors and PDF page checks), 31 image references opened successfully, all 10 Markdown files had valid YAML properties, and table column checks passed. Recalculated new probability budgets, exact quicksort comparison counts, partition/counting/radix traces and digit-cost examples; checked the stated quicksort sum inequality and Karger–Stein contraction progress on representative integer ranges. These arithmetic checks supplement the derivations; finite checks are not proofs.

## Detailed explanation pass — 2026-10-12

All eight lecture notes and their corresponding PDFs were reviewed again, using extracted text and rendered pages. The source decks and source mapping remain the same; this pass expands the explanations rather than adding a new lecture. The earlier statement of substantive topic coverage should not be read as a claim that the earlier explanatory depth was sufficient.

| Note | Main expansions |
|---|---|
| [[Course Introduction]] | Meaning of design/analysis/assessment; distinctions between syllabus methods; decomposition and communication vocabulary; worked study approach; assessment-threshold reasoning |
| [[Algorithm as recipes]] | Input/cost models, explicit asymptotic constants, comparison counts, full merge trace, recursion-tree totals, Dijkstra trace, distinction between evaluating a recurrence and implementing its recursion tree |
| [[Divide and Conquer]] | Recursive proof obligations, unsuccessful binary search, power call/return trace, matrix-block reasoning, all Strassen cancellations, compounded savings, geometric interpretation of layout recurrences |
| [[PRAM]] | Synchronous semantics, address-by-address legality, EREW broadcast, CRCW OR, work/cost picture, work/depth lower bounds, row map, reduction correctness, allocation table, complete scan traces, resource simulation, scaling and serial-fraction reconciliation |
| [[ISPC]] | Scalar/SIMD distinction, interfaces, values versus addresses, mask trace, partial gangs, Taylor update derivation, local counting, exact shuffle states, task granularity, row access patterns, complex arithmetic and divergence |
| [[Randomized Algorithms]] | Sample spaces, order of quantifiers, indicator construction, all six three-applicant orders, harmonic-growth intuition, shuffle proof, error direction, stopping versus waiting, independent versus dependent sampling |
| [[Minimum Cut]] | Cut partitions, lifting and multiplicities, bridge diagram, conditional probability factors, amplification algebra, threshold intuition, independent graph copies, recursive-success interpretation, per-level work |
| [[Sorting]] | Partition-swap reasoning, recursion-tree counts, four-rank expectation, induction slack, full telescoping algebra, decision-tree leaves, output blocks, stability counterexample, digit extraction and key-range reasoning |

Added 14 local visuals: eight original explanatory diagrams, five additional slide-page images, and the diagram panel of Blelloch's Figure 1.4(a), attributed beside the embed. Existing images were retained. Added eight original practice problems across the seven technical notes (two in PRAM, one in each other technical note). Corrected a malformed PRAM title line and a newly added external anchor during verification; preserved the remaining pre-existing note text and metadata.

External checks focused on the ISPC user/performance guides, Blelloch's scan chapter, Blelloch and Maggs on work/depth, Aspnes on probability, Vigoda on min-cut, and MIT's integer-sorting notes. Added worked examples and original diagrams were independently calculated. The ISPC code remains explanatory: no compiler/benchmark run is claimed. Previously recorded gaps—unsupplied notebooks, unverified later course announcements, and broader syllabus material—remain.

Verification for the detailed explanation pass: all 338 internal references resolved, including heading anchors and PDF page bounds; all 45 image references opened successfully. YAML properties and Markdown table columns passed checks. All eight source PDF hashes match the recorded baseline (310 pages total). The pre-pass note text remains in order, with only the malformed PRAM title corrected; pre-existing frontmatter is unchanged. New worked traces were recalculated, including insertion comparison counts, scan stages, processor allocation, row products, scaling fractions, ISPC shuffle states, hiring permutations, min-cut contraction thresholds, and quicksort telescoping counts. Visuals were inspected for readable labels and correct correspondence with the prose. Arithmetic checks support the explanations and do not replace their proofs.

## Completion check — 2026-10-13

After the interrupted chat, a fresh check confirmed that all eight expanded lecture notes are present and correspond to the eight source decks (310 pages). All 345 internal references across the collection and Study Note Prompts resolved, and all 45 image embeds opened successfully. Note properties, heading targets, PDF page bounds, table columns, and code-fence balance passed validation; source hashes still match the baseline. Key new worked calculations were independently repeated successfully. This confirms completion and file integrity; it does not claim unavailable notebooks were tested or later exam announcements verified.

Added a standalone note-question tutoring prompt to Study Note Prompts, including step-by-step explanations, small worked examples, prerequisite/source checks, and optional comprehension practice. Corrected that prompt note's example course paths to the existing lowercase vault path.
