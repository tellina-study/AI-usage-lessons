---
id: s18
type: assertion_visual
duration_min: 7
assertion: "True or false? Let's check your intuition about AI"
learning_goal: "A quickfire quiz on 7 statements, voting before the answer, all with icons for consistency"
learning_outcomes: []
references: []
visual:
  pattern: quiz_statement_list_progressive_reveal
  primary: "6 numbered Ocean rounded box statement rows (round-2: was 7), each with its own icon, with NO inline spoiler glosses + 'true/false' chips"
  round4_note: "comment #248 — this slide became the base (no answers) + 6 progressive-reveal copies (s18a..s18f). On copy k, the correct answers for questions 1..k are highlighted cumulatively (GOLD ✓, the incorrect chip greyed out). Correct answers: 1 false · 2 false · 3 true · 4 false · 5 false · 6 false. Round-4c (owner follow-up): the speaker notes on each copy now contain ONE detailed comment, only for the answer revealed on that slide (without repeating the discussion of previous questions); format 'question + detailed explanation + Lesson.' The memo slide s19 (five_point_memo) was removed by comment #248, then RESTORED in round-4b."
  reveal_slides: [s18a, s18b, s18c, s18d, s18e, s18f]
---

# True or false? Let's check your intuition about AI

## Assertion

True or false? Let's check your intuition about AI.

## Visual

Round-2 changes: removed the "hand+camera" voting badge (voting explained on
s05); removed 2 spoiler glosses "(tokens, not letters)" and "(the context
window)," which gave away the answer before the vote; removed the statement
"Code with no runtime errors means it's logically correct" entirely (the memo
on s19 also loses the corresponding point); the statement about the context
window was replaced with a new one about determinism/training data. In total,
a list of 6 (not 7) compact Ocean rounded box rows, each — a number + icon +
a short statement + 2 neutral chips "true" / "false" on the right, with no
glosses. 1) "AI counts the letters in a word directly, the way a human does"
(`hash` icon). 2) "AI always knows what happened in the world today"
(`calendar` icon). 3) "AI sometimes confidently says something untrue without
intending to deceive" (`brain-circuit` icon). 4) "An AI chat can see your
personal email and files by default" (`lock` icon). 5) "AI always gives an
answer consistent with the data it was fed" (`database` icon, new statement in
round-2). 6) "All AI models give the same answer to the same question"
(`shuffle` icon). At the bottom — small print "vote before the explanation."

## Speaker notes

Quickfire quiz: I read out a statement, you vote by raising a hand — true or false — before I give the answer. The explanation will be short, with a lesson, not just a bare fact.

First: AI counts the letters in a word directly, the way a human does. False — AI splits text into tokens, it doesn't read letter by letter.

Second: AI always knows what happened in the world today. False — the model is trained on data up to a certain cutoff date and, without web search, doesn't know about events after that.

Third: AI sometimes confidently and convincingly says something untrue, without even intending to deceive. True — this phenomenon is called hallucination, we already discussed it in the previous block under the name "hallucinated fact." A confident tone in an answer isn't a sign of accuracy.

Fourth: an AI chat can see your personal email and files by default. False — without an explicit connection, AI has no access to personal data.

Fifth (a new statement in round-2): AI always gives an answer consistent with the data it was fed. False — training data really does shape the model's "character" and its systematic biases, but the answer isn't derived from it rigidly and unambiguously. Because of the randomness of sampling (temperature), the same model can give different answers to the same question. The model doesn't "look up" a ready-made chunk of text in the training set — it generates a continuation based on learned statistical patterns, which is why both generalization to new cases and hallucinations are possible. On top of that, a model's behavior is heavily adjusted after pretraining — through fine-tuning and dialogue tuning (RLHF), so the final answer reflects more than just the "raw" training data.

Sixth: all AI models give the same answer to the same question. False — different models, and even the same prompt run multiple times, can produce answers that differ in substance. Cross-checking with several sources is sensible for important decisions.

On the third and fifth questions the audience usually splits almost evenly — if you see a split, ask a couple of people from each side why they voted that way before giving the answer.
