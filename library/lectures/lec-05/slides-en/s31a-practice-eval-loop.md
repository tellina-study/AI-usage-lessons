---
id: s31a
type: process
section: "Section 4. Measurement"
duration_min: 2.5
assertion: "Evals are needed because the quality of answers changes with no change to the code; AI stands here in three different roles — the subject, the measuring instrument, the supplier of cases — and the loop closes when a postmortem adds a row to the golden set"
learning_goal: "A practice with AI: why evals are needed, which three roles the AI itself plays here, what the practice is run with and where an LLM-as-judge is least reliable"
learning_outcomes: [LO1, LO2]
chapter_ref: "§4.3"
verify_day_of: false
partial_out_strict_in: true
interaction: none
protected: true
note: >
  issue #212, bringing the forms together after the methodological roast of 2026-09-30: all
  twelve practice cards are brought to ONE form — WHAT IT IS (an entry point for a newcomer) /
  HOW IT WORKS (numbered steps + a labelled diagram) / WITH AI AND WITHOUT (rule R6) /
  WHERE IT BREAKS. There are no "artefact", "criterion" or "link to what has been covered"
  blocks and no questions to the room. The previous mismatched fourth blocks ("SCALE",
  "DIAGRAM", "PRACTICES 2026", "TOOLS 2026") have been removed: diagrams live inside
  HOW IT WORKS, and the current tools live in the "WITH AI" column.
  owner-review 2026-10-01: the owner did not understand what the slide was for, what the role
  of the AI was, or why development frameworks were listed. Rebuilt on all three points. WHY
  is moved into the first sentence of the WHAT IT IS block: the quality of answers changes
  with no change to the code, and the code tests say nothing about it. THE ROLE OF THE AI
  takes up the "WITH AI" column and is named as three different roles — the subject of
  evaluation, the measuring instrument (an LLM-as-judge), the supplier of cases; the decision
  on "what counts as a good answer" stays with the human. THE TOOLS have been replaced with
  tools of evaluation specifically, each with the verb it carries out for evaluation:
  promptfoo, DeepEval, Braintrust, Langfuse. LangSmith and Arize Phoenix have been removed.
  Also removed is the claim that it "raised the flow of fixes from three a day to thirty":
  there was no named baseline and no named team behind it.
source: "The three-layer framework — Hamel Husain, a machine learning engineer, author of the piece \"Your AI Product Needs Evals\" · agreement of an LLM-as-judge with a human: 80–90% where the preference is explicit, 60–65% with ties and with the order swapped · evaluation tools: promptfoo (return code 100 when the pass rate is below the threshold), DeepEval (a pytest run with a minimum score per metric), Braintrust and Langfuse (store the golden set, compare versions, block the merge when the score falls)"
meme_or_visual: >
  schema_matrix, one practice card: WHAT IT IS (with the answer to "why" in the first sentence)
  · HOW IT WORKS (four numbered steps on the left, the fourth being the evaluation tools with
  their verb; a labelled diagram on the right: a loop of four nodes, a gold closing arrow) ·
  WITH AI AND WITHOUT (in the "WITH AI" column — three roles of the AI itself) · WHERE IT
  BREAKS (gold).
---

# Visible content

## Title bar
The eval loop: see that the answers have got worse before the user does

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

**An evaluation** (an "eval", as everyone says) — a set of tasks with the desired answer written down in advance, on which a model or an agent is run. **It is needed because the quality of answers changes with no change to the code:** you switch the model version, a rule or a source — the behaviour drifts, while the code tests stay green and report nothing.

**HOW IT WORKS**

1. **Before release** — a run against the curated golden set: reproducible, catches what has broken before.
2. **After release** — evaluation on live traffic: it opens up inputs that were not in the golden set, and behaviour over a long chain of turns.
3. **Closing** — a postmortem of a production failure adds a row to the golden set, and it stays there for good.
4. **What it is run with:** promptfoo drops the build with a return code when the pass rate is below the threshold; DeepEval — through an ordinary test run with a minimum score per metric; Braintrust and Langfuse compare versions and block the merge when the score falls.

[Labelled diagram on the right: the golden set → release → live traffic → postmortem → and a gold arrow back into the golden set; caption "the gold arrow is what makes the loop a loop: a postmortem adds a row to the golden set — without that step there is no loop, only a report"]

**WITH AI AND WITHOUT**

| WITHOUT AI — a suite of code tests | WITH AI — three different roles for the AI itself |
|---|---|
| The answer is known character by character, the run is reproducible, the result is "passed" or "failed". | **The subject of evaluation** — it is the thing being checked. **The measuring instrument** — an LLM-as-judge gives a score against a written rule. **The supplier of cases** — it labels live traffic and proposes what to add to the golden set. "What counts as a good answer" is decided by a human. |

[Gold callout — WHERE IT BREAKS]
**An LLM-as-judge agrees with a human 80–90% of the time where the preference is obvious, and falls to 60–65% as soon as the answers are close or are swapped round** — it is least reliable exactly where the cost of an error is highest. The corrections: shuffle the order of the answers, take a judge from a different family. An experiment on live users costs more and is not replaced by evals.

## Speaker notes


First, why the practice exists at all, because the word "eval" has caught on while the sense behind it gets lost. An evaluation is a set of tasks with the desired answer written down in advance, on which a model or an agent is run. It is needed for a simple reason: the quality of answers changes with no change to the code. You switch the model version, rewrite a rule, update a source — the behaviour drifts, while the code tests stay green and report nothing. The evaluation is the instrument that sees that shift, and sees it before the user does.

It helps to picture evals as a closed loop, otherwise they degenerate into a report nobody reads. The first layer is a run before release against the curated golden set: reproducible, catches what has broken once already. The second is evaluation on live traffic: it opens up inputs that were not in the golden set, and behaviour visible only over a long chain of turns. The consensus among practitioners is both layers, continuously. The third element is what makes the loop a loop: every postmortem of a production failure adds a row to the golden set, so that what was caught once does not come back quietly.

Now the role of the AI, which is easy to blur. Here the AI stands in three places at once, and those are three different roles. The subject of evaluation — the thing being checked. The measuring instrument — an LLM-as-judge gives a score against a written rule in place of a human. The supplier of cases — it labels live traffic and proposes what to add to the golden set. Confusing them is dangerous: when the measuring instrument and the subject come from the same family of models, agreement between them stops being independent evidence. The decision on what counts as a good answer stays with the human in all three roles.

What this is run with. promptfoo runs the golden set on every change and drops the build with a return code when the pass rate falls below the threshold. DeepEval is shaped as an ordinary test run: a minimum score is set per metric, and the build fails by itself. Braintrust and Langfuse store the golden set, compare versions between runs and block the merge when the score falls. The measuring instrument itself gets checked separately: if the scores have hit the ceiling and stopped telling versions apart, that is a deflated golden set, and the task is still unsolved.

And the limit. An LLM-as-judge agrees with a human eighty to ninety per cent of the time where the preference is obvious, and falls to sixty as soon as the answers are close or are simply swapped round. It is least reliable exactly where the stakes are highest.
