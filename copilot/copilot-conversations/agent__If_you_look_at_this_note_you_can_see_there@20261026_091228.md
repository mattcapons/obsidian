---
epoch: 1793002348510
mode: agent
backendId: codex
sessionId: "01a17743-1ad3-7f51-a2cf-c48467c83e14"
agentLabel: "If you look at this note you can see there are a few prompts…"
usage: '{"usedTokens":25138,"contextWindow":828400,"updatedAt":1793002450254}'
tags:
  - copilot-conversation
---

**user**: If you look at this note you can see there are a few prompts. What i want is a new way to direct an agent to use the slides and paste them in a note one at a time and add some comment or information on that slides, because most times they are quite complete by themselves.
[Timestamp: 2026/10/26 09:12:28]

**ai**: I’ll read the prompts in your note and draft one for a slide-by-slide workflow, with brief comments where they add value.The existing prompts ask for extensive rewritten notes. I’ll add a separate option that embeds every slide in order and adds short annotations only where they help explain it.I’m using the `obsidian-markdown` skill for the embeds and callouts. The new prompt will ask the agent to save each slide as a local image, place any useful commentary directly below it, and leave self-explanatory slides without extra text.Added a new prompt in [[Study Note Prompts#Annotate slides one at a time]].

It directs the agent to:

- Embed every slide as an image, in its original order.
- Add brief comments directly underneath when useful.
- Explain missing steps, symbols, assumptions, or confusing diagrams.
- Leave self-explanatory slides without extra text.
- Complete the deck without pausing after each slide.

Copy that prompt and replace the course paths using the placeholders already in the note.
[Timestamp: 2026/10/26 09:12:28]