---
id: s31
type: research_evidence
duration_min: 1
assertion: "The instruction file is loaded at the start of every session automatically, while `DECISIONS.md` is an ordinary repository file that the agent reads only on its own initiative or on an explicit pointer; the presence paradox carries over to it in a conditional but all-or-nothing form"
learning_goal: "The evidence for case 2.1 (it is given AFTER the question) — separate the two different loading mechanisms and honestly carry the presence paradox over to a file that does not load itself"
visual:
  pattern: research_evidence
  primary: "On the left — the two loading mechanisms side by side, so they do not get mixed up: the documented auto-loading of the instruction file (worked through in case 1.3) versus an ordinary file in the repository. On the right — exactly what of the presence paradox carries over to DECISIONS.md, and in what form. At the bottom — two honest caveats: there is no direct measurement on decision logs; the final CLAUDE.md of case 1.2 has no pointer to DECISIONS.md."
---

# What loads itself, and what does not

## Assertion

The instruction file is loaded at the start of every session automatically, while `DECISIONS.md` is an ordinary repository file that the agent reads only on its own initiative or on an explicit pointer; the presence paradox carries over to it in a conditional but all-or-nothing form.

## Visual

On the left, the two mechanisms side by side:

> **Loads itself.** The official Claude Code documentation: the root `CLAUDE.md` and all parent ones are loaded automatically when the session starts. Nested ones — on demand, only once a file from that folder is actually read (case 1.3).
>
> **Does not load itself.** `DECISIONS.md` does not fall under that rule. It is an ordinary file in the repository, just like `src/main.js`: no tool feeds it into the context at the start of a session. The agent opens it if it decided to on its own — or if it was pointed to explicitly: in the request, or by a pointer line in the instruction file.

On the right, the transfer of the presence paradox — in conditional form:

> From case 1.1: the presence of text in the context costs +20–23% regardless of whether it helps solve the task. For `DECISIONS.md` this holds conditionally — the cost arises not in every session, but in every session where the file was read. And it is read in full: nobody reads a file for one relevant line. Thirty entries about deployment, validation and UI trivia are paid for in full at the moment one of them is needed.

At the bottom, two caveats in italics:

> "No direct measurement of the presence paradox on append-only decision logs specifically has been carried out — this is a transfer of an already established mechanism to a new object, not a separate new study."
>
> "The flip side of the same mechanics: an entry the agent did not open costs nothing — and gives nothing. In the final `CLAUDE.md` of case 1.2, fifteen lines, there is no pointer to `DECISIONS.md`: a guaranteed path from the auto-loaded layer to the decision log does not currently exist for us. This is an open question, not a solved one."

## Speaker notes

"Before we go through the answers — one mechanical thing that is easy to mix up, and expensive to mix up. In case 1.3 we worked through auto-loading from the official documentation: the root instruction file and all parent ones are loaded by themselves when the session starts, nested ones — only once a file from that folder is read.

`DECISIONS.md` does not fall under that rule at all. It is an ordinary repository file, no different from `src/main.js`: no tool feeds it into the context automatically. The agent opens it if it decided to open it — or if you pointed it there.

Hence a correction to the presence paradox. In case 1.1 a controlled experiment showed: the mere fact that text is present in the context costs plus twenty to twenty-three percent, regardless of whether the text helps solve the task. For a decision log this holds conditionally: the cost arises not in every session, but in every session where the file was read. But it is read in full — nobody reads a file for the one entry they need. Thirty entries on different topics are paid for in full for the sake of the one that is relevant today.

No separate measurement on decision logs specifically has been carried out — this is a transfer of a mechanism to a new object, not new proof, and that is how it is presented.

And the flip side, which is more honest to name right away: an entry the agent did not open costs nothing and gives nothing. In our final instruction file — the fifteen lines from case 1.2 — there is no pointer to `DECISIONS.md`. Which means we currently have no guaranteed path from the auto-loaded layer to the decision log. That is an open question, not a closed one."
