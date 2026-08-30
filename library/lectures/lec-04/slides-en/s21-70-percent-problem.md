---
id: s20
type: case_study
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "The 70% problem: AI gets to \"almost right\" fast, but the last 30% — understanding — it does not speed up; \"almost right\" code passes a quick glance and breaks on an edge case"
learning_goal: "[SI] Failure: the 70% problem (Osmani) + \"almost right\" (SO 66%) + knowledge paradox + GitClear merge-gate"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.4 [for-slide-s18]"
references: [osmani-70-percent, stackoverflow-2025, gitclear]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — the "70% curve" in an Ocean rounded box: the first ~70% of the task AI gets done fast/cheap, the last 20-30%
  (edge cases, error handling, security, integration, behavior under load) remain just as hard →
  senior oversight; the gap is STRUCTURAL (the specifics of the system are absent from the training data = essential complexity), not temporary.
  The "two steps back" loop. A plate "almost-right code is costlier than obviously wrong" — the work shifts from writing to debugging someone else's plausible logic.
  Right — 3 numbers with a baseline: SO-2025 66% the main frustration "almost right" · GitClear 211M lines: clones 8.3%→12.3%,
  refactoring ~25%→<10%, churn 3.3%→5.7% · the knowledge paradox (seniors challenge, juniors accept).
  Gold — "AI speeds up the first 70%, but not the last 30% — understanding". Source citations — inline right next to the material itself (definition/claim/recommendation), NOT in a bottom footer; small and muted: Osmani; SO 2025; GitClear (correlation over 211M LOC, not an RCT).
interaction: none
---

# Visible content

## Title bar
The 70% problem: AI speeds up the first 70%, but not the last 30% — understanding

## Body
[Left — the 70% curve in an Ocean rounded box]

AI gets a typical task to **~70%** fast and cheap. The last **20-30%** — edge cases, error handling, security, integration, behavior under load — remain just as hard and require senior oversight.

The gap is **structural**, not temporary: the specifics of your system are absent from the training data — this is essential complexity. Hence the "two steps back" loop.

[Plate — "almost right"]
**"Almost right" code is costlier than obviously wrong**: it passes a quick glance and breaks on an edge case. The work shifts from writing to **debugging someone else's plausible logic**.

[Right — three numbers with a baseline]

**Stack Overflow 2025: 66%** of developers named as their main frustration "solutions that are almost right, but not quite."

**GitClear** (211M lines, 2020-2024): clones **8.3% → 12.3%**; refactored **~25% → <10%**; churn **3.3% → 5.7%**. *(Correlation over 211M lines, not an RCT.)*

**The knowledge paradox** (Osmani): seniors challenge AI's output, juniors accept it ("house of cards") — AI amplifies the experienced more.

[Gold callout]
The alternative — small verifiable units + harness + **read the diff before accept**; duplication and churn metrics in CI as a gate. **Merge — always a human.**

## Speaker notes

The first failure of the implementation phase was named by Addy Osmani, a Google Chrome engineer — the seventy-percent problem, updated to eighty percent in agentic coding [1]. The gist: AI gets a typical task to about seventy percent fast and cheap, and this creates the feeling that the task is almost done [1]. But the last twenty to thirty percent — edge cases, error handling, security, integration with the rest of the system, behavior under load — remain exactly as hard as they were, and require experienced oversight [1]. It is critical to understand: the gap is structural, not temporary. The specifics of your particular system are absent from the model's training data — this is essential complexity per Brooks, and it will not close with the next version of the model. Hence the familiar "two steps back" loop: you fix one thing — another breaks [1].

A particular but important case — "almost right" code is costlier than obviously wrong [1]. Obviously wrong code falls over right away, you throw it out. "Almost right" passes a quick glance, gets into the system, and breaks on an edge case in production, while the work shifts from the pleasant writing to the unpleasant debugging of someone else's plausible logic that you didn't write and don't hold in your head.

Now the measured consequence. GitClear analyzed two hundred eleven million lines over 2020-2024: the share of clones rose from eight point three to twelve point three percent, the share of refactored and reused code fell from about twenty-five to under ten percent, and churn — code rewritten within two weeks — rose from three point three to five point seven [2]. A caveat about the baseline: this is a correlation over a large corpus, not a controlled experiment, but three markers point the same way — the accumulation of tech debt [2]. And Osmani's knowledge paradox: the experienced challenge AI's output, while beginners accept it as is, building a house of cards — so AI amplifies the strong more than the weak [1]. The alternative — not "don't use AI," but the discipline of the previous slides: small verifiable units, a harness, and mandatory reading of the diff before accept, plus duplication and churn metrics in CI as a gate. And the unchanging rule: merge is always a human.
