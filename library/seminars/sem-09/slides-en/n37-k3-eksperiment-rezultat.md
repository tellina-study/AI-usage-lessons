---
id: n37
type: measured_outcome_table
duration_min: 2.0
assertion: "On 20 answers that code accepted as good enough, the judge rejected 19 — and every one of those 19 rejection reasons is disproved by the answer's own text"
learning_goal: "Updated 2026-10-27 — a full 20×3 measurement instead of the original 6. A turn in the case (P1): the original ask was 'how often is the judge softer than code,' and that still isn't measured cleanly on the new sample (code didn't reject a SINGLE one of the first 20 answers) — but the opposite direction held up and got stronger: it went from 5 false rejections out of 5 measurable to 19 out of 20."
visual:
  pattern: measured_outcome_table
  primary: >
    A banner with the load-bearing number "19 of 20" and a note that the
    reverse half of the comparison isn't measured in this sample. Below it,
    a table of 7 representative rows (the full 20 are in the protocol):
    answer length, the judge's verdict, the reason, and why it's false. At
    the bottom, a verbatim quote of one answer with its verdict and a new
    error class (a legitimate number called a violation).
  backup: >
    Numbers from `stend/zamery-k1-k3/README.md`, § "Measurement 4 — Case 3,
    full 20×3 measurement," subsection "Extending judge-check to 20
    questions." Source — `raw/zamer3-judgecheck-20.json`, executions
    1034–1053, reusing the first answers from `raw/zamer3-full-20.json`
    (code's answers, not newly generated).

    WHY THE PREVIOUS VERSION'S "0 OF 6" ISN'T REPEATED LITERALLY: on the
    earlier sample, code rejected 1 of 6 answers (kb5, a grammatical case),
    which gave a measurable "the judge approved what code rejected" (= 0).
    On the new sample, code accepted ALL 20 first answers on the first
    attempt — there are no code-rejected texts to compare against. This
    isn't a weakness of the measurement — it's an honest side effect of
    code not making a single mistake on this run, and hiding that would be
    worse than stating it plainly.

    THE FULL TABLE OF ALL 20 is in the README; the frame shows 7 rows: 3
    recurring classes of false reason (length/detail/rule number) plus a
    new class (a legitimate number called a violation) plus the single
    agreement.

    A NEW ERROR CLASS (absent on the sample of 6): "the answer contains the
    number 18" — the judge rejected a legitimate number FROM THE KNOWLEDGE
    BASE ITSELF (kb3, age of majority) as "a number not in the base," even
    though code (checking against the same list of allowed numbers)
    correctly let it through.

    Run numbers do not appear on the visible layer (BRIEF §2) — they're in
    the protocol.
---

# Twenty answers, two checkers

## Assertion

Code accepted 20 of 20 answers. The judge rejected 19 of them — and every rejection reason is disproved by the text itself.

## Visual

> **The judge rejected what code accepted: 19 cases out of 20 (95%)**
> **The reverse comparison ("the judge approved what code rejected") isn't measured in this sample** — code didn't reject a single one of the first 20 answers.

| Question (short) | Answer length | Judge's reason | Why the reason is false |
|---|---|---|---|
| installment payment | 97 characters | "doesn't mention the detail 'installment'" | the detail is in the answer, literally |
| rescheduling, was sick | 169 characters | "1. No longer than 280 characters" | a rule number, not a violation — the answer is shorter than the limit |
| a refund | 213 characters | "the answer exceeds 280 characters" | literally false — 213 < 280 |
| **parental consent (age 18)** | 155 characters | **"the answer contains the number 18"** | **a new class: 18 is a legitimate number from the knowledge base itself (kb3), not a violation** |
| retake on a weekday | 125 characters | "doesn't mention 'the second Saturday'" | the detail is in the answer, literally |
| a certificate after the course | 144 characters | "doesn't mention '5 business days'" | the detail is in the answer, literally |
| certificate, where to check | 113 characters | **(agreed)** | the only match out of 20 |

> **Four recurring classes of false reason.** Length (7) · a rule number instead of an explanation (4) · a detail already in the text (7) · a legitimate number called a violation (1).

> **"Code accepted" means exactly that, and no more.** All 20 passed the same five rules — the same check the judge uses; there's no other quality measure for this task.

## Speaker notes

This sample grew from six answers to twenty — the same experiment, a wider base.

Code accepted all twenty first answers. Not a single rejection. That means one half of the original question — "will the judge approve what code itself rejected" — simply can't be measured on this run: there are no code-rejected texts to compare against. I'm saying this outright, not hiding it: the absence of a number is also an honest result, when there's no material for it.

The opposite direction, though, is measured reliably and strongly. Of the twenty answers code accepted, the judge rejected nineteen. Ninety-five percent.

Look at the reasons. "The answer exceeds two hundred eighty characters" — on a two-hundred-thirteen-character answer. "Doesn't mention the detail" — when the detail is in the text literally, in the same words. "A rule number instead of an explanation" — the same bug we saw before. And a new class, absent on the six-answer sample: the judge rejected the number eighteen as "a number not in the base," even though it's a legitimate number from the base itself — the age of majority. Code, reading the same list of allowed numbers, didn't make this mistake.

The single agreement — the answer about where to check a certificate, the judge agreed right away. One case out of twenty, five percent. This doesn't disprove the finding — it says the judge sometimes still guesses right, but you can't rely on a guess the way you rely on a check.

And one more thing worth saying outright, because otherwise it's easy to leave hanging: "code accepted" here doesn't mean some separate, deeper check of correctness. Code and judge check the same text by the same five rules, and this task simply has no third, more authoritative source of truth. When code says "good enough," that means "passed the five rules" — no more, no less. On this sample, expanded from six answers to twenty, the direction and scale of the earlier finding got stronger, not different: it was five false rejections out of five measurable, now it's nineteen out of twenty.
