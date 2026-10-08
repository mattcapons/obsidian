---
tags:
  - study
  - prompts
aliases:
  - Course slide prompts
  - Slides to Obsidian
---
# Study Note Prompts

Reusable prompts for turning course slides into Obsidian study notes and keeping them updated throughout the semester.

## Quick access

- [[#Build and enhance a course collection|Start a new course collection]]
- [[#Continue when new slides arrive|Update an existing collection]]
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
/home/matteo/Documents/Obsidian/University/Advanced Algorithms and Parallel Programming

EXACT_SLIDES_FOLDER_PATH:
/home/matteo/Documents/Obsidian/University/Advanced Algorithms and Parallel Programming/Slides
```

Change the language or note depth when needed. If a course has explicit exam boundaries, add them to the prompt or supply the relevant syllabus and exam guidance.

To reference these prompts in a future conversation, attach this note or mention [[Study Note Prompts]] and specify which workflow to use. An Obsidian heading link can also point directly to the relevant prompt.

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
