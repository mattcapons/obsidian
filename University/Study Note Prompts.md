---
tags:
  - study
  - prompts
aliases:
  - Course slide prompts
  - Slides to Obsidian
---
# Study Note Prompts

Reusable prompts for turning course slides into Obsidian study notes, annotating slides in their original order, keeping notes updated throughout the semester, and asking for explanations of material you do not yet understand.

## Quick access

- [[#Annotate slides one at a time|Keep the slides and add brief comments]]
- [[#Build and enhance a course collection|Start a new course collection]]
- [[#Continue when new slides arrive|Update an existing collection]]
- [[#Ask questions about a study note|Understand a note in a standalone chat]]
- [[#How to use these prompts|Setup and placeholders]]

## How to use these prompts

Use one project per course and start separate chats for new slide batches or major reviews. Include the actual course folder in the project's context. The course index, notes, and **Course Workflow.md** should provide continuity between chats; do not rely exclusively on conversation history. A single chat is sufficient for a one-off deck. See [OpenAI's projects and chats guidance](https://learn.chatgpt.com/docs/projects).

Copy the appropriate prompt below and replace these placeholders:

| Placeholder | Replace with |
|---|---|
| COURSE_NAME | Full course name |
| EXACT_COURSE_FOLDER_PATH | Absolute path of the course folder in the vault |
| EXACT_SLIDES_FOLDER_PATH | Absolute path of its Slides folder |

For AAPP:

```text
COURSE_NAME:
Advanced Algorithms and Parallel Programming

EXACT_COURSE_FOLDER_PATH:
/home/matteo/Documents/obsidian/University/Advanced Algorithms and Parallel Programming

EXACT_SLIDES_FOLDER_PATH:
/home/matteo/Documents/obsidian/University/Advanced Algorithms and Parallel Programming/Slides
```

Change the language or note depth when needed. If a course has explicit exam boundaries, add them to the prompt or supply the relevant syllabus and exam guidance.

To reference these prompts in a future conversation, attach this note or mention [[Study Note Prompts]] and specify which workflow to use. An Obsidian heading link can also point directly to the relevant prompt.

## Annotate slides one at a time

Use this when the slides are already fairly complete and you want to study them directly, with brief explanations underneath. Each slide appears in full, in its original order. “One at a time” means processing and annotating each slide separately within the note; the agent should complete the deck without waiting for approval after each slide.

```text
Create Obsidian notes containing my original course slides, one slide at a time, with concise comments where they help me understand the material.

Course: COURSE_NAME
Course folder in my vault: EXACT_COURSE_FOLDER_PATH
Slides folder: EXACT_SLIDES_FOLDER_PATH
Language for annotations: English
Style: The slides are the main study material; annotations fill specific gaps.

Work directly in the specified course folder. Inspect the available decks, existing notes, and Course Workflow.md if present. Read existing notes before editing them and preserve my annotations, corrections, properties, and filenames. Follow any explicit syllabus or exam boundaries.

1. Prepare one note per deck
- Follow existing naming conventions and use the Notes folder. If no convention exists, use Notes/<deck title>.md.
- At the top, link to the original deck and briefly identify the lecture topic.
- Render every slide as a readable local PNG image, preserving the whole slide, its aspect ratio, equations, code, and diagrams. Store images in Attachments/<deck name>/ with stable, zero-padded names such as slide-001.png.
- Embed the actual slide image in the note with Obsidian syntax. A link to the deck alone is insufficient.
- If image rendering is unavailable, use PDF page embeds as a fallback and report that limitation. Never claim that images were generated if they were not.

2. Process the deck slide by slide
- Inspect each slide visually, using extracted text as an aid. Do not rely only on text extraction.
- Include every slide exactly once in its original order, including title slides, exercises, references, and repeated slides. Do not merge slides into concept summaries or silently omit them.
- Give each slide a heading with its physical PDF page number and title, for example: "## Slide 3 — Parallel computation". If the printed slide number differs, record it separately.
- Place the slide image immediately below its heading and link to the corresponding source PDF page.
- Put any annotation immediately below that slide, before the next heading.

3. Add only useful annotations
- Treat complete, clear slides as sufficient on their own. Leave them without commentary when nothing useful needs adding.
- Usually add one short paragraph or a few bullets, roughly 30–100 words per slide that needs explanation. Use more only when a difficult step requires it.
- Explain what the slide leaves implicit: intuition, an undefined symbol, an assumption, why a step follows, how to read a diagram, or a likely source of confusion.
- For an algorithm or formula, add a small example, intermediate step, or complexity explanation only when it resolves a gap in that slide.
- Do not transcribe the slide, paraphrase every bullet, repeat earlier annotations, or add generic filler such as "this slide introduces...".
- Preserve the lecturer's terminology. Place your additions in a callout titled "Comment" so they are distinct from the original material.
- Link to another slide or existing note when that avoids repeating an explanation.
- For exercise slides, keep the problem visible; if adding a solution, put it in a separate collapsed "Worked solution" callout.
- Do not add mandatory summaries, quizzes, exam-style exercises, or extended textbook sections.

4. Handle uncertainties and sources
- Check annotations against the slide and surrounding slides first.
- Consult authoritative external sources only when needed to resolve a gap or verify a claim. Cite external explanations beside the relevant annotation.
- Flag an apparent error or ambiguity explicitly, explaining the evidence rather than silently correcting the slide.
- Identify unreadable content and incomplete processing honestly. Do not invent missing text, lecturer remarks, or exam requirements.

5. Use this layout for each slide

## Slide 3 — Slide title

![[Attachments/DECK_NAME/slide-003.png]]

Source: [[Slides/DECK_NAME.pdf#page=3|PDF page 3]]

> [!note] Comment
> A brief explanation of a specific point that benefits from clarification.

Omit the Comment callout entirely when the slide is self-explanatory. Adapt link paths to the actual vault location and use unambiguous targets. For the fallback, replace the image with ![[Slides/DECK_NAME.pdf#page=3]]. Use LaTeX for mathematics in annotations.

6. Verify and maintain
- Check that the number and order of slide sections match the source page count, all image files exist, and source page links match their slide sections.
- Check image quality and ensure the smallest text remains readable. Do not crop out slide content.
- Link completed notes from the existing course index, or create a minimal index if needed.
- Record the source deck, note path, image folder, annotation style, and outstanding issues in Course Workflow.md so later chats can continue this workflow.
- On later runs, process new decks in the same style. For revised decks, compare against the prior source mapping, preserve my comments, and flag annotations whose source slide changed or disappeared. Do not attach old comments to different slides merely because page numbers shifted.
- Keep this annotation workflow separate from existing expanded study notes; do not overwrite those notes to change their format unless I request it.

Complete the file edits for the available decks without pausing after each slide. Briefly report the notes created or updated, slide coverage, and anything incomplete.
```

## Build and enhance a course collection

```text
Turn my course slides into an organized Obsidian study collection.

Course: COURSE_NAME
Course folder in my vault: EXACT_COURSE_FOLDER_PATH
Slides folder: EXACT_SLIDES_FOLDER_PATH
Language: English
Depth: Explained study notes suitable for exam preparation.

Work directly in the specified course folder. First inspect the available slides, existing notes, and any syllabus or exam guidance. Read existing notes before editing them, and preserve my corrections, annotations, properties, and useful images.

Complete the following workflow:

1. Organize the collection
- Create a course index in the course folder.
- Maintain one Markdown note per slide deck in its Notes folder.
- Use meaningful titles and preserve established filenames.
- Link the index to every note and source deck, in lecture order.
- Add links between related concepts and prerequisite lectures.

2. Write substantive study notes
- Read every deck, including diagrams, equations, and code that text extraction may miss.
- Organize explanations by concept, consolidating repeated slides.
- Explain definitions, intuition, assumptions, and important reasoning steps.
- Include worked examples and derivations where they help understanding.
- For algorithms, explain inputs, outputs, correctness, pseudocode, and relevant time/space complexity.
- For other subjects, adapt the structure to the material rather than forcing an algorithm template.
- Finish technical notes with key takeaways, revision questions, and a few original exam-style problems with collapsible worked solutions.
- Identify practice questions as original exercises, not past exam questions.

3. Improve the reading experience
- Add selected diagrams and images beside the explanations they support.
- Prefer useful visuals from the supplied slides.
- Use external images when they clarify something the slides do not illustrate well.
- Save images locally in an organized Attachments folder and embed them with Obsidian syntax.
- Include explanatory captions, source links, and attribution for external images.
- Avoid adding images merely as decoration.

4. Review and enhance
- Check explanations and calculations against the slides.
- Consult authoritative outside sources: textbooks, university materials, original papers, and official documentation.
- Use outside information to clarify the supplied topics and fill necessary explanatory gaps.
- Keep additions within the supplied material and any explicit exam scope.
- Clearly label supplementary explanations and apparent slide errors.
- Cite external claims beside the relevant explanation.
- Preserve the lecturer's terminology, while explaining conflicts or ambiguities.
- Report inaccessible sources or unreadable material honestly.

5. Use correct Obsidian formatting
- Use wikilinks for vault notes and PDF page references.
- Use LaTeX for mathematics, fenced blocks for code, and callouts where useful.
- Escape alias separators inside Markdown tables as \| so links do not split columns.
- Preserve existing properties and use a consistent, minimal metadata structure.

6. Verify and document
- Check links, headings, image embeds, PDF page references, table structure, and mathematical examples.
- Confirm that every deck has substantive coverage.
- Create or update a Course Workflow.md note recording the folder paths, note conventions, deck-to-note mapping, and any incomplete material.
- Briefly report the files changed, important corrections, and remaining uncertainties.

Create and edit the files, rather than only proposing a plan. Use reasonable judgment for routine organizational choices.
```

## Continue when new slides arrive

```text
Update my existing Obsidian study collection with newly added or revised course material.

Course: COURSE_NAME
Course folder in my vault: EXACT_COURSE_FOLDER_PATH
Slides folder: EXACT_SLIDES_FOLDER_PATH

Read Course Workflow.md, the course index, and relevant existing notes first. If Course Workflow.md does not yet exist, infer the established conventions from the index and notes, then create it. Inspect the slides folder and identify decks that are new, revised, or incompletely covered. Use the existing notes and source mapping rather than relying on conversation memory.

Continue the established workflow:

- Create one substantive Markdown note for each new deck.
- For revised decks, update the corresponding note and explain significant changes.
- Preserve my edits, annotations, filenames, properties, and useful images.
- Match the existing language, depth, organization, and Obsidian formatting.
- Include explanations, assumptions, worked examples, relevant derivations, and original exam-style practice with solutions.
- Add useful local slide images and, where needed, attributed external visuals.
- Enhance the new material using authoritative outside sources, while staying within the supplied topics and explicit exam scope.
- Label supplementary material and apparent slide errors, and cite external explanations.
- Integrate new lectures into the index, reading order, and cross-links.
- Update older notes only where the new material creates a relevant connection, resolves an uncertainty, or requires a correction.
- Update Course Workflow.md with the current source mapping and outstanding gaps.
- Verify links, tables, image embeds, PDF references, and worked calculations.

Complete the file edits and briefly summarize what was added or changed, including anything that remains incomplete.
```

## Ask questions about a study note

Start a separate chat, attach the note you want to study (for example, [[PRAM]]), and paste the prompt below. Replace `NOTE_TITLE` and `MY_QUESTION`; you can name a heading, paste a formula, or describe the step that confuses you. Attach the source slides too if the chat cannot access your vault. You do not need the earlier note-creation conversation.

```text
Act as my patient study tutor. Help me understand a specific Obsidian study note and answer follow-up questions in this standalone chat.

First read the actual attached note or resolve and read it in my vault. Read the surrounding section, not just the sentence I quote. Do not infer its contents from its title or rely on previous conversations. If the note or a required source is inaccessible, tell me what you could not read and ask for the relevant passage.

Explain in the language I use for my question, keeping the note's technical terminology and defining unfamiliar words. Match the note's clear study style: connected explanations, LaTeX mathematics, focused examples, and useful tables or diagrams.

For each question:
- Start with a direct answer and the intuition behind it.
- Break down the reasoning into small steps. Explain why each step follows; do not skip an important step by saying it is obvious or simply citing a theorem.
- Define every new symbol and state the assumptions, indexing conventions, and cost model where relevant.
- Work through a small concrete example completely. For an algorithm, trace the changing state, explain correctness, and derive time/space complexity when those are part of my question.
- For a formula or derivation, show intermediate algebra and explain what the result means. Distinguish exact values, asymptotic bounds, expected values, and worst-case guarantees.
- Address the particular misunderstanding in my question. Use a counterexample or analogy when it helps, then connect it back to the formal explanation.
- Use a diagram when relationships, dependencies, memory accesses, recursion, or parallel execution are easier to see than to describe. Explain how to read it.

Use the corresponding slide pages and relevant prerequisite notes when they are available and help answer the question. For course context, consult the course index and Course Workflow.md if needed. Stay focused on my question and the supplied topics; label supplementary explanations and do not invent exam requirements.

If a claim is uncertain, ambiguous, or apparently wrong in the note or slides, identify the issue and explain the correction with evidence. For external clarification, use authoritative sources such as university materials, textbooks, original papers, and official documentation, and cite them beside the explanation. Do not treat the existing note as automatically correct.

After the explanation, give one short optional check-your-understanding question. If you include its answer, put it in a collapsible worked-solution callout. If I am still confused, try a different example or level of explanation instead of repeating the same wording.

Answer in the chat. Edit my vault notes only if I explicitly ask you to save or integrate an explanation; then preserve the existing filenames, properties, structure, annotations, and useful images.
```

Example starting question: “In [[PRAM#Prefix sum]], why does the doubling scan need a snapshot, and why is its work greater than its depth? Please trace four values.”
