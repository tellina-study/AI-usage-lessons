---
id: s18
type: research_evidence
duration_min: 4
assertion: "A textual gate with no tooling is not merely useless but harmful — regressions rose to almost 10%; none of the room's five options solves the problem systematically, except handing the check to a mechanism outside the text"
learning_goal: "The evidence and breakdown of case 1.2, part 1 (slide 1.2.4) — two mini source tables (gates + the improvement loop), an honest gap, a breakdown table of the five cards; the formula and the extended block on the hook are on the next slide"
visual:
  pattern: research_and_answer_combined
  primary: "Two mini source tables (gates; the \"plan → code → improvement\" loop), the first row of each highlighted in gold, an honest-gap plate. Then the breakdown table of the room's five cards, with the row \"I'll hand it to a mechanism outside the text\" marked as the right direction. The formula and the block on the hook are on the next slide, not here."
---

# What the evidence says — and the breakdown

## Assertion

A textual gate with no tooling is not merely useless but harmful — regressions rose to almost 10%; none of the room's five options solves the problem systematically, except handing the check to a mechanism outside the text.

## Visual

**The evidence — gates:**

| Source | Claim | Strength |
|---|---|---|
| SWE-Gate/SpecBench/CapCode/Verification Horizon (4 preprints, 2609–2606) | Agreement across 4+ independent 2026 preprints: agents systematically "work around" visible test gates | Strong — cross-study consensus |
| **TDAD, arXiv:2603.17973** | A purely procedural instruction to "write the tests first", with no tooling, raised regressions to 9.94% — worse than no instruction at all | Strong and counterintuitive |
| Rethinking Agent-Generated Tests, arXiv:2602.07900 | Manipulating the prompt to raise test frequency — no significant effect (6 models) | Moderate — a null result |
| Agent Scaffolding Beats Model Upgrades | Harness architecture gives +20 pp; switching the model — ~1 pp | Strong — mechanism vs. model |

**The evidence — the "improvement" loop:**

| Source | Claim | Strength |
|---|---|---|
| Self-planning, arXiv:2303.06689 | Planning before code: +25.4% pass@1 (not repo-scale) | Moderately strong, "in favor" |
| LLMs Cannot Self-Correct, ICLR'24; CRITIC 2305.11738 | Self-correction with no external signal systematically makes the result worse | Strong "against" bare self-review |
| arXiv:2604.10508 | Self-repair with an external signal: +4.9…+30 pp | Strong "in favor" — with a real check |

An honest gap: "There is no controlled experiment on an isolated gate line in `CLAUDE.md` specifically — only practitioners' best-practice observations."

**The breakdown of the room's five cards:**

| Option | Where it works | Why it is too early — and what instead |
|---|---|---|
| "In caps / harsher" | Nowhere systematically | TDAD: regressions rose to 9.94% |
| "I'll duplicate it as a second bullet" | Sometimes slightly raises the chance it gets read | Presence paradox: an extra line costs context |
| "A separate checklist file" | Helps the human, barely helps the agent | The same class of solution — text again, a request again |
| **"I'll hand it to a mechanism outside the text"** | **Works systematically: +20 pp** | **The right direction** — the mechanism itself is covered on the next slide |
| "I'll live with it, that's normal" | Acceptable for non-critical preferences | For a rule whose violation is expensive — a decision not to decide |

## Speaker notes

"Here the result is genuinely counterintuitive. The TDAD study took a purely procedural instruction, "write the tests first", without a single change to the tooling — and regressions did not fall, they rose to almost ten percent. Worse than no instruction at all. The improvement only appeared once the same requirement was wired into a skill or into the tooling rather than into text. And separately, for the "plan - code - improvement" loop: self-critique with no external signal systematically makes the result worse — ICLR confirms that firmly. Self-repair with a real test run, on the other hand, gives plus five to thirty percentage points. The difference is fundamental, not terminological: did the agent look at its own code, or did it run a real check.

There is no separate controlled experiment on an isolated gate line in an instruction file — here we have practitioners' best-practice observations, not a measurement of its own.

Now the breakdown. The option "I'll rewrite it in caps" is exactly the path TDAD tested: they strengthened the wording with text, with no tooling. Regressions rose. Caps do not turn a request into a law. "I'll duplicate it as a second bullet" — the presence paradox from the first case: an extra line costs context in every session. "A separate checklist file" — the same class of solution, text again, a request again. "I'll live with it, that's normal" — for a rule whose violation is expensive, that is a decision not to decide.

And only one option out of five — "I'll hand the check to a mechanism outside the text" — works systematically: the mechanism gives twenty percentage points where switching the model gives one. That is the right direction. The mechanism itself is on the next slide."
