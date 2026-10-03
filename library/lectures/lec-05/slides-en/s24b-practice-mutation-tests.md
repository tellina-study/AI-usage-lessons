---
id: s24b
type: schema_matrix
section: "Section 3. Build and launch"
duration_min: 2.5
assertion: "A check that has never had a defect planted in it on purpose counts as broken: the share of mutants killed carries over from code to everything the AI is constrained by"
learning_goal: "Practice 2 of the phase: mutation testing from the previous lecture applied to the checks around AI — the golden set, the agent instructions file, a rule in the pipeline"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§3.4a"
verify_day_of: false
partial_out_strict_in: true
interaction: none
protected: true
note: >
  issue #212, owner-review 2026-10-01: the practice was rebuilt from scratch. It used to be
  "the golden set" — that almost word for word repeated the eval loop from Section 4 (s31a),
  and the owner removed the duplicate. The new practice is mutation testing as applied to
  work with AI: a continuation of what the students have already heard in Lecture 4 §4.3
  (the share of mutants killed is more honest than coverage, Meta's data 32/5.3 % against
  2.4/15 %) and a development of the owner's article "AI delivery gap" (25 Sept 2026): a
  check that has never had a defect planted in it on purpose should be treated as broken.
  A step forward against both supports: in Lecture 4 it was the CODE that was mutated, to
  check the tests; here the same practice is pointed at the checks AROUND the AI — the
  golden set, the agent instructions file, a rule in the pipeline. The card form is kept:
  WHAT IT IS / HOW IT WORKS / WITH AI AND WITHOUT / WHERE IT BREAKS.
  NEEDS THE ORCHESTRATOR'S ATTENTION: chapter_ref §3.4a still describes the golden set —
  the chapter was not edited (out of scope), and the divergence between slide and chapter
  has to be closed separately.
  Correction to the owner's article: the share of defects not linked to any mutant is given
  there as 17 %; the primary source (Just et al., FSE 2014) gives 27 % — 63 out of 357. The
  slide carries the number from the primary source.
meme_or_visual: >
  schema_matrix, one practice card: WHAT IT IS · HOW IT WORKS (four numbered steps on the
  left + a labelled diagram on the right: three rows of "what we check → which defect we
  plant", one row per check) · WITH AI AND WITHOUT · WHERE IT BREAKS (gold).
source: "A continuation of Lecture 4 §4.3 (the share of mutants killed is more honest than coverage) · mutants from a model against a list of rules: 76.5% against 44.2% of real defects found on a sample of 851, arXiv 2406.09843 · Meta ACH — 10,795 Kotlin classes → 9,095 mutants → 571 tests, arXiv 2501.12862 · Just et al., FSE 2014 — 27% of real defects are not linked to any mutant (63 out of 357) · the agent instructions file: with no file the rule was followed 0 times out of 524, with the file 67.7%, arXiv 2605.10039 · tools: PIT, mutmut, Cosmic Ray, Stryker"
---

# Visible content

## Title bar
A check that has never had a defect planted in it on purpose counts as broken

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

**Mutation testing** — a small error (a "mutant") is deliberately put into the code and you watch whether any check at all fails. The share of mutants killed is what tells you whether the set of checks is capable of catching anything; coverage answers a different question — whether the line was touched by the run. In work with AI the same practice is pointed at everything the AI is constrained by: **at the golden set, at the agent instructions file, at a rule in the pipeline**.

**HOW IT WORKS**

1. Name the check you rely on, and **the class of errors it is obliged to catch**.
2. Put an error of that class in **on purpose** — one, small, in one place.
3. Run the check. **Silence means there is no check**: it does not tell the sound from the spoilt.
4. Record the share caught **as a number** and repeat the measurement after every edit to the check: checks go stale quietly.

[Labelled diagram on the right: "The same practice on three different checks" — unit tests: flip a condition · the golden set: swap the answer for a nearly right one · the agent instructions file: a task where breaking the rule is the shorter route. Caption: "silence in answer to a planted defect is exactly what having no check means"]

**WITH AI AND WITHOUT**

| WITHOUT AI — the mutants come from a list of rules | WITH AI — the model writes the mutants |
|---|---|
| Flip a condition, shift a boundary, take out a call. The run is reproducible and there are tools for every language: PIT, mutmut, Cosmic Ray, Stryker. | They sit closer to real errors: they find **76.5%** of real defects against **44.2%** for the list of rules (851 defects). The price — around a third of the generated mutants do not compile. |

[Gold callout — WHERE IT BREAKS]
Some defects the practice cannot see by construction: out of 357 real errors, **27% are not linked to any mutant** — wrong algorithms, and code that should have been deleted. And the share killed spoils the same way coverage does: put a gate on it and easily killed mutants start breeding, while detection does not grow.

## Speaker notes

Mutation testing already came up in the previous lecture: small defects — mutants — are put into the code on purpose, and you look at what share of them the tests killed. We compared that with coverage at the time and saw that coverage only tells you a line was touched by the run. Meta's data showed it as a number: test generation by a model covered thirty-two per cent of classes against five for the narrowly targeted method, and killed two and a half per cent of mutants against fifteen. More tests and higher coverage do not mean that detection got better.

Here the practice takes a step further. In the previous lecture the code was mutated in order to check the tests. In a product with AI there are more checks, and every one of them is capable of going silent: the golden set, the agent instructions file, a rule in the pipeline, an alert threshold. The rule is a hard one: a check that has never had a defect planted in it on purpose counts as broken until proven otherwise. A green build, an empty list of violations and quiet monitoring look the same whether everything is fine or the detector has died.

Here is how it is done on the agent instructions file. You take two copies of the repository, one with the file and one without, and a task in which breaking the rule is the short route. You measure the share of violations in both runs. If there are no fewer violations with the file, the rule is not working. In the published measurement, with no file the rule was followed zero times out of five hundred and twenty-four; with the file, in sixty-seven per cent of runs. Every third run breaks the rule anyway, which is why prohibitions that must not be broken are placed as an interceptor in code: text does not hold that much.

Now what the arrival of AI changed in the practice itself. The mutants are now written by a model, and they sit closer to real errors — seventy-six per cent of real defects found against forty-four for the list of rules. At Meta the same practice was pointed at one named risk, privacy: nine thousand mutants across a little over ten thousand classes produced five hundred and seventy-one tests. And two limits. The practice is expensive: a thousand mutants with a ten-second run comes to around two hours fifty minutes of machine time, so it is run over the important modules as a one-off, as a diagnostic; it is not kept in the build permanently. And twenty-seven per cent of real defects are not linked to any mutant — wrong algorithms and redundant code are invisible to the practice.
