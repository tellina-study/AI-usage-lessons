---
id: n25
type: criteria_checklist_and_boundary
duration_min: 2.0
assertion: "The time window, the LLM judge's own error asymmetry (measured, not assumed), and 'what counts as a duplicate' — three classes of nuance, unrelated to which tool was chosen"
learning_goal: "Three classes of nuance for Case 2, a separate slide from the criterion. The second nuance is anchored by the team's own measurement (3 false positives out of 20), not just a citation of outside work."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A list of three nuance classes; the second one carries a source link
    right on screen and ties to the team's own measurement.
  backup: >
    The three classes are from SETKA-KEYSOV-S8.md, Case 2, section
    "Nuances". The source link for the second nuance (NeurIPS 2024 Safe
    GenAI Workshop, Wataoka/Takahashi/Ri, arXiv:2410.21819) is on the
    visible layer per trebovaniya-k-soderzhaniyu-forma.md §5.12–5.22:
    links to papers belong on the slide itself, not only in the notes.
---

# Nuances of the Duplicate Check

## Assertion

Three sources of error unrelated to which tool was chosen: the window length, the LLM judge's asymmetry, and the very definition of a "duplicate".

## Visual

1. **The time window — a parameter with a cost on both sides.** Too short a window will miss a repeat spread a day or two apart. Too long a window will start confusing a person's different, consecutive requests with a repeat of one request.

2. **The LLM judge has its own error asymmetry, not zero** (Wataoka, Takahashi, Ri — NeurIPS 2024 Safe GenAI Workshop, arXiv:2410.21819, self-preference bias): a judge model is systematically non-neutral, even when formally answering "yes" or "no". Our own test confirmed this directly: 3 false positives out of 20, and not all of them come from word overlap in the questions.

3. **"What counts as a duplicate" is a product decision, not just a technical one.** Sometimes "the same question in different words" is worth treating as a new request — the person is waiting for an answer more urgently the second time. Not every technical repeat has to collapse into one in the interface.

## Speaker notes

Three nuances, and not one of them is about which scheme to pick — all three surface only after the choice has already been made and the solution already built.

First — the time window is itself a parameter with a cost. Too short a window and the check will miss a repeat the person sent a day later rather than a couple of minutes later: formally, that's already "not a recent" request. Too long a window and the check will start confusing different, but back-to-back, requests from the same person with a repeat of the same request. This number has to be tuned from reality, not guessed once and left alone.

Second — an LLM similarity check is a specific case of a more general task, where a model acts as a judge evaluating someone else's text. And it has the same error asymmetry as any model acting as an evaluator: this isn't an assumption, it's a documented result — Wataoka, Takahashi, and Ri showed at NeurIPS 2024, at the Safe GenAI workshop, that a judge model is systematically non-neutral, even when formally it's just answering "yes" or "no" to a direct question. And this isn't an abstract reference to someone else's work: we just saw exactly this on our own test — three false positives out of twenty, not zero, and at least one of them isn't explained by word overlap in the questions — the model erred on a pair with not a single word in common. The meaning check isn't perfect; it just errs differently than mechanics does.

The third nuance — what we even count as a duplicate — is a product decision, not just a technical one. Sometimes a person deliberately rephrases their question, because they need an answer more urgently the second time, and collapsing that request into "already answered" would be wrong in substance, even if technically it's the same question. Not every detected repeat has to show up as a single entry in the interface — this is a decision worth discussing with whoever works the requests every day, not guessing at in code.
