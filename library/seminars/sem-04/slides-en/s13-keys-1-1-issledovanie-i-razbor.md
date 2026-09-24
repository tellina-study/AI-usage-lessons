---
id: s13
type: research_evidence
duration_min: 5
assertion: "A repository overview measurably does not raise the success rate and costs context — while a structured description, if it is needed, lives in README.md and is not duplicated in CLAUDE.md"
learning_goal: "The evidence + breakdown of case 1.1, merged into one pass after the vote — four sources, an honest gap, a breakdown table of the five positions, the target answer and a README plate at the level of the target answer"
visual:
  pattern: research_and_answer_combined
  primary: "A table of four sources (source · claim · strength of evidence), the first row highlighted in gold, below it the definition of the presence paradox and an honest gap with an unmeasured case from practice. Then the breakdown table of the five option cards, the 'nothing yet' row highlighted in gold. At the bottom — a prominent gold README plate at the level of the target answer: a structured description must exist, but in README.md, not duplicated in CLAUDE.md/AGENTS.md."
---

# What four sources say — and the breakdown

## Assertion

A repository overview measurably does not raise the success rate and costs context — while a structured description, if it is needed, lives in `README.md` and is not duplicated in `CLAUDE.md`.

## Visual

**The evidence.**

| Source | Claim | Strength of evidence |
|---|---|---|
| **Gloaguen et al., arXiv:2602.11988** | "Repository overviews… are not helpful" — "steps to the first relevant file" does not drop; cost +20–23% with no gain in success | Strong: a controlled experiment with an honest third arm, "no file at all" |
| The same work, ablation | They removed the existing documentation (README) from the repository — and the LLM-generated overview became useful (+2.7%) | Confirms the mechanism: an overview is harmful not in itself, but because it duplicates what is already available another way |
| Lulla et al., arXiv:2601.20404 | `AGENTS.md` focused on non-discoverable conventions: −28.6% runtime, −16.6% tokens (124 PRs) | Moderately strong "for" the file — but this is NOT about a general description of the structure |
| Shepard & Albrecht, arXiv:2606.20512 | Static written-once guidance (28.3% resolve) is worse than dynamically verified guidance (33.0%, p<0.001) | Indirect |

The term: "Cost goes up and success does not, simply because the text is present in the context — that is the **presence paradox**. The term is used from here on without being explained again."

An honest gap: "No direct experiments with a deliberately stale repository overview were found. The failure mode known from practice — the description survived a refactoring and stayed in the file, so the agent edits according to it rather than according to the code — is plausible, but unmeasured."

**The breakdown of the room's five cards:**

| Option | Where it works | Why it is too early here — and what instead |
|---|---|---|
| "A detailed description of the repository structure" | Almost nowhere, for an agent | The agent will work out the structure itself in seconds; the description will go stale at the first refactoring. +20–23% cost, with no gain in success |
| "A list of technologies and dependencies" | When the versions are critical and not visible from package.json | Usually derivable in seconds as well |
| "An instruction on where the form lives" | Almost nowhere on a repository this small | Six files, the whole structure fits on one screen |
| "A non-obvious convention" | When the convention really exists and cannot be derived | At this step there is no such convention yet |
| **"Nothing yet — until the first signal"** | **Here and now** | **The target answer** |

**README, not AGENTS.md — a gold plate at the level of the target answer:**

> "A structured description of the repository must exist — this case does not cancel the need for one, it names the place. It lives in `README.md`, rather than being duplicated in `CLAUDE.md`/`AGENTS.md`. We set up `README.md` in the first commit — that is exactly the need for a structured description it covers, and that is precisely why a separate "Repository overview" in the instruction file is not needed: the description already exists, just in a different file."

## Speaker notes

"The controlled experiment by Gloaguen et al. was the first to compare against a third arm — no file at all. The result for a repository overview, verbatim: "are not helpful". Cost goes up by twenty to twenty-three percent, the success rate does not. The only confirmed exception is repositories with no other documentation at all.

The phenomenon has a name: presence paradox. The presence of text in the context costs money regardless of whether it helped solve the task. We will need the term twice more: in cases 1.2 and 1.3, and later in the section on memory.

Briefly on the remaining sources: the ablation confirms the mechanism — they removed the README and the overview became useful. Lulla et al. is a strong argument for the file, but about non-discoverable conventions, not about a general description. Shepard & Albrecht — static, unverified guidance is worse than dynamically verified guidance.

On the gap, honestly: there are no direct experiments with a deliberately stale overview. The failure mode you do see in practice — the description survived a refactoring and the agent edits the file according to it rather than according to the code — is plausible, but unmeasured, and we are not going to pass it off as proven.

Now the breakdown. For our repository the target answer is "nothing yet": the agent sees the six-file structure itself, and the description of the project is already in the README. A structured description must exist, but not duplicated in the instruction file. The answer at this step is not "what text to write", it is "none for now"."
