---
# СЛИТЫЙ КАДР, прожарка сторителлинга #293, Этап A. Было три — «Две стороны приёма»
# (`s01ad`), «Влияние на врача» (`s01ae`), «Влияние на пациента» (`s01af`); стал один
# кадр-анонс. Решение прожарки: словарь выдаётся ИМЕНАМИ, замеры предъявляются там, где
# механизм встречается впервые, и там же отсчитываются сводами разделов.
#
# ПРОВЕРЕНО ГРЕПОМ ПЕРЕД СЛИЯНИЕМ (не на слово): замер каждого из шести имён уже стоит в
# своём разделе — якорение `s49_1` (84,86 против 41,66 из ста, 30 стажёров; и 23,6 против
# 92,8 у 220 читателей в его заметках) · сужение `s41` (29 → 61 из ста имевшихся раков,
# 10 радиологов) · износ `s73f` (28,4 → 22,4 из ста, 1 443 процедуры) · несогласие `s15a`
# (3 449 против 5 283 арбитражей) · поток тревог `s49f` · поправка `s63a`. Два замера
# жили ТОЛЬКО на снятом `s01ae` и перенесены в заметки своих кадров, а не потеряны:
# «отклоняется 90 из ста тревог» → `s49f`; «врач переписывает 31,3 из ста заключений
# модели, 159 630 кардиограмм» → `s63a`.
#
# СТОРОНА ПАЦИЕНТА. Пять её замеров (раскрытие · одиночество · асимметрия · цена ·
# безымянность) не предъявляются сейчас ни на одном кадре разделов — стадии «доверие и
# согласие пациента» в деке нет. Они целиком сохранены в заметках ЭТОГО кадра, с
# выборками и числами: переносить их в чужой раздел значило бы поставить замер туда, где
# он ничего не разбирает. Это открытый вопрос к владельцу, названный в журнале правок, а
# не молчаливая потеря.
#
# СХЕМА «без модели / с моделью» СНЯТА, снимки врача и пациента ОСТАВЛЕНЫ: вместе они не
# помещаются (полоса участников 3,0" плюс шесть пунктов), а владелец 2026-10-17 прямо
# требовал на этом кадре «картинки врач и пациент». Мысль схемы — модель встаёт внутри
# приёма, а не рядом — стоит первой строкой тела.
id: s01ad
local_id: В-01ad
section: "0. Вход"
type: analitika
title: "Six distortions at the front door: the names"
assertion: "Модель входит внутрь приёма и меняет работу обеих сторон; шесть механизмов этого названы именами здесь и предъявлены замером там, где каждый встречается впервые: якорение, сужение, износ навыка, поток тревог, несогласие, поправка — последнее работает в нашу пользу"
source: "Полная запись источников — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/15-rabota-vladeltsa-iskazheniya.md"
media: "rework/deck/assets/s35-vrach-chitaet-s-ekrana.jpg"
media_2: "rework/deck/assets/dve-storony-pacient-landscape.jpg"
media_label: "Physician"
media_2_label: "Patient"
media_needed: "закрыто §8 режимом участников (media_2, #262). Второй снимок — альбомный кроп s22 (не новая добыча, не правка источника — s22 используется отдельно в s22-divider-analiz-dannykh.md). Провенанс — assets/s35-vrach-chitaet-s-ekrana.url и assets/dve-storony-pacient-landscape.url"
media_note: "снимки оставлены по прямому указанию владельца 2026-10-17 («картинки врач и пациент»); схема приёма снята при слиянии — вместе со стеком имён она в кадр не входит"
timing_min: 0.8
in_bucket: true
method_steps: ["словарь"]
form: ["вопрос залу"]
vfy: false
status: собран
---

## Visible slide text

- **Anchoring.** The conclusion shifts toward the model's suggestion, even when it is plainly wrong.
- **Narrowing.** Where the model stays silent, the eye does not linger.
- **Skill decay.** Once used to the model, people find less without it.
- **Alert stream.** Alerts come one after another, and so does dismissing them, one after another.
- **Disagreement.** A mismatch with the model is now handled as a separate step, and that step is new.
- **Correction.** The one that works in our favor: the doctor catches the model's mistake and fixes its report.

## Speaker notes

The first thing worth saying, looking at the two photos: the model doesn't take a seat beside the visit, it takes a seat inside it — between the doctor and the decision — and the patient either knows that or doesn't, and their behavior changes with it either way. That is why there are two sides, and they were measured by different means: for the doctor, behavior on the task; for the patient, agreement with the decision. These two measurements cannot be added together.

This slide hands out the vocabulary that marks up the rest of the evening. There are six names, and deliberately no numbers under them yet: every number will be presented where the mechanism is first encountered, with its own sample and its own base, and tallied in the section summaries — which of the six a given section ran into. Naming them in advance is so that, by the time the mechanism is encountered, it is recognized rather than explained from scratch in the middle of a breakdown.

The frame behind these mechanisms is not ours. Three of them come from a study of distortions in human–model interaction, verified across three different fields on more than two thousand people in total, and the entire evening's medical measurements fall onto two of the three as a special case. Worth saying outright: medicine is not special here, and the objection "that's how doctors are, because it's medicine" is not knocked down by one medical measurement — it's knocked down by the fact that the same mechanisms are measured outside medicine too.

First of the three is bias amplification, and it is the only one with a control arm. People labeled facial expressions, their answers were fed to a convolutional network, it amplified the original bias, and alongside it a fresh group of people worked with the model's output: the share of biased answers rose from 49.9 to 56.3 out of a hundred. In the control arm, other people stood in for the model — there the share did not change: 50.6 against 51.5, no difference. What amplifies is not agreement with someone else's opinion in general — it is specifically the model. And the amplification grows as the work goes on: 50.7 out of a hundred in the first block, 61.4 in the last. Second is anchoring: 775 managers rated employees' work after seeing a suggestion, and their ratings pulled toward it. That study doesn't print a magnitude, and substituting a similar number from a different study is not allowed. What it does name is the move that breaks anchoring: requiring the person to consider the opposite. That is not the same as a warning: a warning is a message that gets noted and then ignored while work continues as before, while considering the opposite is an action the person is required to carry out. Third is inheritance: 666 participants took a critical-thinking test with no access to the model, and the link between how often they used it and their score turned out negative and significant.

Why this isn't visible from the inside is a question the room asks itself. In that same first study, participants were asked how much each algorithm had influenced them, and they rated the biasing one as less influential than the accurate one — exactly backwards. And with no model at all, a person corrects their own bias on their own: over the course of the trial the share of biased answers fell from 56.7 to 51.9. The capacity for self-correction is there; next to a model it stops working. And the honest other half of the same measurement: an accurate algorithm raised participants' own accuracy. The slide isn't saying the model is harmful — it's saying where to look.

Now the other side — the patient. The evening does not give these measurements a breakdown of their own, which is why they stand here. For the doctor, what was measured was behavior on the task: reads, concludes, finds or misses. For the patient, what is measured is agreement — how they respond to the bare fact that a model was involved in their case. And first: agreement is not one number. Disclosure — 1,762 adults, representative of the US population: when a patient is told the doctor uses a model, trust in the doctor falls from 0.63 to 0.30 on the scale used, and a doctor's flat refusal to use the model earns them 13 points on top of what they'd have if it were never mentioned at all. Loneliness — 518 women who came in for a breast scan: only 23 people agreed to accept the model as the sole reader, 368 of the same 518 accepted it as a second reader — a sixteenfold difference. The patient is against not the model, but its being alone. Asymmetry — 359 participants, both questions asked: a worry raised by the model, let a doctor look — 319 said yes; one raised by the doctor, let the model look — 184. Double-checking is eagerly requested upward and barely requested downward. Price — 248 adults with type 1 diabetes: removing a $50 co-payment raised the choice of a model-based exam from 43 to 81 out of a hundred, and those who chose it still wanted a specialist's double-check even more than before. Price buys agreement; it does not buy trust. Anonymity — 45 people with a cancer diagnosis rated mixed, unsigned answers: they rated the machine's answer's empathy at 4.11 out of five, the doctor's at 2.01. These five cannot be added together: the samples and the questions are different.

And the overall boundary of this whole block, better named going in than excused coming out: not one of these measurements reaches the patient's actual outcome. What was measured was the doctor's work and the patient's agreement; what happened to the person's health, none of the sources we cite measured. Separately: the effect on the doctor was almost always measured in a lab, where the share of deliberately corrupted suggestions is higher than in real life, while the effect on the patient was measured by a survey about an imagined situation. Both methods get the direction right; they overstate the magnitude.

**Six names in front of you. Which of the six, in your view, will turn out the most costly for the doctor — and which for the patient?**

**Sources.** Full record — [breakdown of the study on distortions in human–model interaction](https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/15-rabota-vladeltsa-iskazheniya.md) (the frame of three mechanisms and all 18 sources) · [compilation of medical measurements](https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/10b-ii-ispolzovanie-i-effekt.md) · [compilation on patient trust in the model](https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/16-doverie-patsienta-k-modeli.md) — which also names the two pairs deliberately not combined, and lists what simply was not found at all.
