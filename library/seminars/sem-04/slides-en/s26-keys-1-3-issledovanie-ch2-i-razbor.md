---
id: s26
type: research_evidence
duration_min: 3
assertion: "Neither of the two controlled measurements found that distributing documentation improves the result — so the channel is chosen by delivery and cost, not by a promised benefit: knowledge about a function goes into the code, knowledge about a class of files into a rule with a path pattern, knowledge about the project into the root file as pointers"
learning_goal: "The evidence for case 1.3, part 2 + the breakdown: four sources, the 'honest about the gap' block, the breakdown table of the five cards, the target answer 'the rule of three addresses'"
visual:
  pattern: research_and_answer_combined
  primary: "Top — a table of four sources (source · claim · strength of evidence), the first two rows reading 'no effect found'. Middle — an 'honest about the gap' block of four caveats, visually set apart. Below — the breakdown table of the room's five cards; two rows highlighted in gold as parts of the target answer, and the 'nested file' row flagged as the only one with no guarantee. At the bottom — a gold plate, 'the rule of three addresses', at the level of the target answer."
---

# No structure has measured a benefit — the breakdown

## Assertion

Neither of the two controlled measurements found that distributing documentation improves the result — so the channel is chosen by delivery and cost, not by a promised benefit: knowledge about a function goes into the code, knowledge about a class of files into a rule with a path pattern, knowledge about the project into the root file as pointers.

## Visual

| Source | Claim | Strength of evidence |
|---|---|---|
| McMillan, arXiv:2605.10039 — 1,650 Claude Code sessions | None of the 4 structural variables of the config file (contradictions between adjacent levels included) produced a significant effect after correcting for multiplicity; for size and for contradictions the Bayes factor is evidence for the ABSENCE of an effect | Strong and counterintuitive: the only controlled study of config-file structure as such does not confirm any benefit from splitting it up |
| Khatri, arXiv:2607.27250 — 288 runs, 2 agents, 3 repositories, hidden reference tests | Three modes: no file / the file in every turn / separate documents to be loaded on demand. Claude: 53.3 — 55.6 — 55.6%. Codex: 58.8 — 56.9 — 52.9%, that is, no file at all is better. No significance (p=1.00 and p=0.66). The tasks failed on implementation craft, not on a shortage of knowledge about the repository | Strong in design, weak in power: the authors write themselves that across 15–17 tasks the detectable effect is above 30 pp |
| Vasilopoulos, arXiv:2602.20478 — 283 sessions, one developer, 108K lines | The only work in which the corpus is built out in full: a permanently loaded core + domain specialists + 34 on-demand documents behind a search index; the infrastructure is 24.2% of the project's lines | Weak as evidence of benefit: one person, one project, no control group; the author states outright that this is not a controlled experiment |
| The same work, on the failure mode | "Agents trust documentation absolutely, and stale specifications cause silent failures." Maintaining the corpus takes 1–2 hours a week; staleness is named the main failure mode | A direct observation by the owner of the system — and the only thing we know about the cost of a corpus |

**Honest about the gap — four caveats:**

1. No measurement showed that distributing documentation improves the result. The channel is chosen not by a promised benefit but by delivery and cost.
2. "No effect found" is not "there is no effect": Khatri's power would have been enough only for an effect above 30 pp, and McMillan's Bayes factor argues for the absence of an effect for two of the four variables.
3. The guarantee for a comment in the code is derived from the mechanism, not measured: if the agent reads the file in chunks, or jumps straight to a symbol through the language server, the file header may never land in context. Hence the practical consequence — keep the comment next to the function itself, not only in the file header.
4. A rule with a path pattern is conditional loading too, not a guarantee, and the pattern itself has its own traps: a documented case — an unescaped `[` makes the pattern invalid, it matches nothing, and the rule silently fails to fire.

**The breakdown of the room's five cards:**

| Option | Where it works | Why it's too early here — and what instead |
|---|---|---|
| "A nested file in the folder itself" | Nowhere with a guarantee | The only option with no guarantee in any of the four tools. The promise comes from the standard, not from the tool |
| "A rule with a declared path pattern" | When a class of files has a convention that isn't needed in the other sessions | The right mechanism — but not on our repository: the `tests/` convention fits into two lines, and a new mechanism costs more than two lines |
| **"A comment next to the code"** | **Always — for knowledge about specific code** | **Part of the target answer.** The only channel where delivery follows from the mechanism rather than from a setting. The detail about the retried submit goes here |
| **"A separate document plus a pointer in the root file"** | **When the document already exists and there is somebody to maintain it** | **Part of the target answer — and the answer to "where the corpus lives".** The corpus is not a separate file you have to find: it is a table of contents inside the one file that loads at launch. For us there is nothing to point at yet |
| "Append it to the root file" | When the knowledge is needed in every session | For the `tests/` convention — presence paradox: the line about the page object costs context in sessions where nobody touches the tests too |

**A gold plate at the level of the target answer — the rule of three addresses:**

> "Knowledge about a single function — next to it, in the code. Knowledge about a class of files — into a rule with a declared path pattern. Knowledge about the whole project — into the root file, briefly, and as pointers rather than as content. The one place knowledge should not be put is a nested instruction file in a subfolder: it is the only one of the five channels with no guarantee in any tool."

## Speaker notes

"Now the uncomfortable part. Two controlled measurements checked whether any of this helps at all. The first — sixteen hundred and fifty sessions, four structural variables of the config file: not one of them has a significant effect. The second, more recent — two hundred and eighty-eight runs across two agents and three repositories, three modes: no file, the file in every turn, separate documents to be loaded on demand. For Claude all three land within two percentage points of each other. For Codex the 'no file' variant turned out to be the best one. There is no significance. And the failure analysis showed that the tasks fell over on implementation craft, not on a shortage of knowledge about the repository.

The authors make the caveat themselves, and we will repeat it: across fifteen tasks the detectable effect is more than thirty percentage points. An effect of ten they would not have seen. 'Not found' is not 'not there'.

What follows from this in practice. We choose the delivery channel not because somebody proved it useful — nobody proved that. We choose by the two things we know for sure: does the text arrive, and what does it cost in the sessions where it isn't needed. Hence the rule of three addresses. Knowledge about a single function — next to it, in the code: the only channel where delivery follows from the mechanism. Knowledge about a class of files — into a rule with a declared path pattern. Knowledge about the whole project — into the root file, briefly.

And the answer to the question that usually hangs in the air: where does the corpus live. The corpus is not a separate document the agent is supposed to find. The corpus is a table of contents inside the one file that loads at launch: one line per document, where it sits and when to go there. Everything else — 'we have a wiki, go take a look' — is a hope, not a delivery channel.

We know the cost of that corpus too, from the only work in which it was built out in full: an hour or two a week to keep it up, and the main failure mode is going stale. Verbatim: agents trust documentation absolutely, and stale specifications produce silent failures. That is the experience of one developer on one project, with no control group — but we have no other numbers on the cost of a corpus."
