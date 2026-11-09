---
id: s38
local_id: s3-04
section: "3. Постановка диагноза"
type: norm
title: "Four rungs of involvement"
assertion: "Ступень называет, что человек успевает увидеть, и ступенью разборы не различаются: два разбора стоят на одной ступени с противоположными результатами, а расходится у них устройство процедуры — сохранённая независимость двух мнений и арбитраж третьим; на четвёртой ступени формальное требование выполняется за время, за которое подсказку нельзя прочесть"
source: "Qazi I. A. et al., NEJM AI 2026 — https://doi.org/10.1056/AIoa2501001 · Mozannar et al., CHI 2024 — https://arxiv.org/abs/2210.14306"
media: ""
media_needed: "собственная схема четырёх ступеней; на ней же дальше отмечаются разборы"
media_note: "—"
scheme:
  kind: lestnitsa
  axis: "human involvement"
  direction: вниз
  rows:
    - label: "Rungs"
      steps:
        - "Looks first\nsees the case"
        - "Looks second\nsees the case and the finished conclusion"
        - "Looks only at disputed cases\nsees the sample the model selected"
        - "Signs without looking\nsees only the text"
pol_slov: 136    # О13 (#229): +4 слова на описание работы — 44 врача читали по шесть клинических задач каждый (264 прочтения, не 264 случая). Без них на кадре стояло число без работы, из которой оно взялось
timing_min: 0.75
in_bucket: true
method_steps: ["заземление", "упоминание"]
form: ["[VFY]"]
vizforma: "лестница"
vfy: true
status: собран
---

## Visible slide text

**The second rung holds both the gain and three failures.** The eye-tracking study, the pathologists, the surgeons — and the Swedish trial, where the person stays the first reader and the model becomes the second: one rung, opposite outcomes. What differs between them is **the design of the procedure** — whether the independence of the two opinions is preserved, and who resolves a disagreement.

**Training doesn't move you up a rung:** 44 trained physicians read six clinical cases each — the share of correct reasoning across 264 readings **84.9 → 73.3 out of a hundred** when some of the recommendations are wrong.

**The risk of the third rung:** the person doesn't know what the model screened out. **The fourth** — the formal requirement that "a person checked it" is met in a median of **1.99 seconds**: not enough time to read the suggestion.

## Speaker notes

The four rungs of human involvement describe what a person manages to see before a decision moves on. At the fourth rung, where a person only signs off, the median review time is 1.99 seconds, and that's the time BEFORE the decision is made; the second median in the same study is 6.48 seconds.

The formula "human in the loop" answers a question nobody asked: it says the person is present, and says nothing about what they do. The four rungs separate this out by what a person manages to see. Reading first, they see the case and reach their own conclusion before learning the machine's; this is the most expensive rung in time, and it preserves independence. Reading second, they see the case together with the finished conclusion — independence is lost by construction, and there's a gain in speed. Looking only at disputed cases, they see the sample the model selected, and whatever was selected incorrectly never reaches them at all. Signing without looking, they see only the text of the report.

The fourth rung has a measured figure, and it was found outside medicine: twenty-one programmers, 1,096 processed suggestions from a code assistant, behavioral telemetry. The median time spent over a suggestion before deciding to accept it is 1.99 seconds. The same study has a second median, and the two must not be confused: if you count the review that continues after accepting the suggestion, you get 6.48 seconds — meaning more than half of all review time falls after the decision has already been made. The first figure answers the question "does a person have time to read before signing off." More important is this: a suggestion accepted without prior review later needed a fix with probability 0.53; one reviewed before acceptance, 0.18. There's no medicine in this sample, and carrying it over to a physician rests on an analogy.

The medical measurement alongside it is about training not raising you a rung. The baseline for comparison here is working with correct model recommendations; there's no condition at all without a suggestion in the trial: the same 44 physicians — twenty-two per arm, six clinical cases each, meaning 264 readings, not 264 cases — give 84.9 out of a hundred with correct model recommendations and 73.3 when some recommendations are deliberately wrong; the wrong ones were given in three of the six cases. The adjusted difference is minus 14.0 points, with an interval from −18.9 to −9.1: the point estimate's sign matches the interval's, and it has to be said out loud, or the number reads as a gain. The strength of evidence is high — a peer-reviewed randomized trial, not a preprint — the sample is small, it's a single country, and neither fact cancels the other. We leave the −18.9 to −9.1 interval as is and don't correct it: the two published versions of this work give different bounds, both centered on minus 14.0, and we have no right to change the bounds without reading the journal version. A physician who completed a twenty-hour course stayed on the rung where they started: the course doesn't turn them into a reader who can selectively disbelieve.

And one last thing about the fourth rung, without which it reads as a reproach. Signing without looking is behavior with a measured payoff, and that payoff isn't created by the interface but by the order in which a case is reviewed after the outcome. A physician who accepted a machine suggestion in favor of standard treatment is judged, on review, as more reasonable than one who rejected the suggestion; for a non-standard recommendation there's no difference. So the rung doesn't rest on laziness: disagreeing and being wrong costs more than signing off. The measurement itself and its caveats are presented in the section on licensing, oversight, and liability — where signature, procedure, and regulation are examined; it's named here so the ladder doesn't read as a scale of diligence.

And right away, a caveat without which the ladder lies. A rung names what a person manages to see, and nothing more: it can't rank case studies by quality, and it can't tell them apart either. Later in this section you'll meet two case studies on the exact same rung, "looks first," with opposite results — in one, the pair didn't outperform a human without the model and stayed below the model itself; in the other, it came out stronger than both sides. What tells them apart is the design of the procedure: whether the independence of the two opinions is preserved, and who's assigned to arbitrate a disagreement. Their rung is the same. And the case study where the pair came out below both the model and the human individually sits on a different rung — "looks second": there, the suggestion was shown before the person had formed their own opinion.

**Sources.** [Qazi I. A., Ali A., Khawaja A. U. et al., Automation Bias in Large Language Model–Assisted Diagnostic Reasoning among Physicians Trained in AI Literacy — A Randomized Clinical Trial, NEJM AI 2026;3(5), 23.04.2026, DOI 10.1056/AIoa2501001](https://doi.org/10.1056/AIoa2501001); medRxiv preprint 10.1101/2025.08.23.25334280 · [Mozannar et al., Reading Between the Lines, CHI 2024](https://arxiv.org/abs/2210.14306)
