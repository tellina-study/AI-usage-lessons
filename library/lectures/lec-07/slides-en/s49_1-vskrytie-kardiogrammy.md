---
# НОВЫЙ КАДР — ВСКРЫТИЕ ИГРЫ-ПРЕДСКАЗАНИЯ, прожарка сторителлинга #293, Этап C (П3, раздел 3).
#   Вторая половина разрезанного `s49`: там постановка, база и вопрос, здесь ответ. Разрез
#   нужен затем, что на одном кадре вопрос и ответ стояли рядом и предсказывать было нечего.
# НОМЕР `s49_1` — подномер между `s49` и `s49a` (`deckkit/slidefile.py::order_key`). Буквенный
#   хвост `s49a` занят обзорным разбором ста шести опытов; переименовать его значило бы двигать
#   ссылки на него в `s49d`, `s99` и реестре.
# ВСЁ, ЧТО ЗДЕСЬ СТОИТ, СТОЯЛО НА ПРЕЖНЕМ `s49`: матрица двух групп, обе плашки потерь и строка
#   про якорение. Ни одно число не заведено этим этапом, ни одно не потеряно — разведены
#   вопрос и ответ, не содержание.
# ПЕРВАЯ СТРОКА — МОСТ С ВОПРОСА (§5.22) и одновременно ответ на его вторую половину: зал
#   предсказывал, кто упадёт глубже, и первым делом получает именно это.
id: s49_1
local_id: s3-12_1
section: "3. Постановка диагноза"
type: case
title: "The reveal: both groups fall by half, the less expert one falls deeper"
assertion: "Ответ на предсказание предыдущего кадра: на неверной машинной расшифровке точность заключения падает у обеих групп вдвое — 84,86 до 41,66 и 86,38 до 27,43 из ста, — и у менее экспертной группы падение глубже на 15,75 пункта; этот вывод авторы высказывают сами и дважды, а второй признак той же оси — согласие с неверной расшифровкой, 30,77 против 42,31 из ста по медианам"
source: "Bond et al., Journal of Electrocardiology 2018 — https://pubmed.ncbi.nlm.nih.gov/30122457/ · Buçinca et al., CSCW 2021 — https://arxiv.org/abs/2102.09692 · Yu et al., Nature Medicine 2024 — https://doi.org/10.1038/s41591-024-02850-w"
media: ""
media_needed: ""
media_note: "иллюстрация не нужна: кадр держат матрица на две группы и две плашки потерь, и они же и есть содержание вскрытия"
# СХЕМА ЭТОГО РАЗБОРА СТОИТ НА `s49` — первой половине того же разреза (#293, Этап E).
#   Там схема порядка чтения кардиограммы и постановка опыта, здесь ответ на предсказание.
#   Ставить её сюда дублем запрещено §5.12 (два написания одного содержания на соседних
#   кадрах), поэтому сторож `[схема]` ПЕРЕАДРЕСОВАН, а не отменён: `build_lec07.
#   check_scheme_refs` принимает ссылку только если названный кадр есть и несёт свою схему,
#   иначе печатает то же блокирующее `[схема]` с уточнением, чем ref битый.
scheme_ref: s49
blocks:
  - {label: "Accuracy lost on an incorrect machine readout: cardiology trainees → other specialties", value: "−43.20 → −58.95 points", note: "the difference is robust in both groups; the less expert group loses 15.75 points more — the authors' own conclusion, stated twice", key: true}
  - {label: "Agreed with the incorrect readout", value: "30.77 versus 42.31 out of a hundred", note: "medians for the same two groups, in the same order: the less expert group agrees more often", key: true}
pol_slov: 120   # ОБЪЯВЛЕН ПОД ВТОРУЮ ПОЛОВИНУ РАЗРЕЗАННОГО `s49` (#293, Этап C): матрица на две группы, две плашки потерь, строка про якорение. Переобъявляется по собранному PDF этапа — мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 0.55
in_bucket: true
method_steps: ["упоминание"]
form: ["сетка", "[VFY]"]
vfy: true
status: собран
---

## Visible slide text
**The ones who fell deeper were trainees from other specialties — those with less training in this kind of reading.**

| report accuracy, out of a hundred | correct | incorrect |
|---|---|---|
| cardiology trainees | 84.86 | **41.66** |
| other specialties | 86.38 | **27.43** |

**Anchoring, the first of the six input distortions.** Specialty protects, but it doesn't save you: both groups fall, and both by half.

## Speaker notes

First, the answer to both halves of the question, in the order they were asked. Depth: the fall isn't five points, or fifteen — it's by half. For cardiology trainees, accuracy falls from eighty-four and eighty-six hundredths to forty-one and sixty-six hundredths out of a hundred — forty-three and twenty hundredths points. For trainees in other specialties, from eighty-six and thirty-eight hundredths to twenty-seven and forty-three hundredths — fifty-eight and ninety-five hundredths points. Both drops are significant, p less than one thousandth. Who falls deeper: the less expert group, and the room usually guesses this correctly.

The authors state the load-bearing conclusion of this study themselves, and they state it twice: less expert readers are affected MORE STRONGLY. The gap between the losses is fifteen and seventy-five hundredths points in favor of the expert group, and that group agrees with the incorrect readout less often: thirty and seventy-seven hundredths versus forty-two and thirty-one hundredths out of a hundred, by median. In other words, specialty protects, and protects measurably — it just doesn't save you: both groups fall, and both by half. This has to be said in exactly this order, because the reverse order gives the reverse conclusion, and that's exactly the mistake this slide carried before the fix: a caption reading "specialty tells them apart" erased the expertise axis the authors themselves call load-bearing.

Let me name what's happening to the person here: it's a cognitive bias. The first of the six presented at the opening of the evening, and it's called anchoring — the report shifts toward the suggestion, even one that's knowingly wrong. The opening slide showed it on chest X-rays: twenty-three and six tenths versus ninety-two and eight tenths out of a hundred across two hundred twenty readers; here the same mechanism is captured on an EKG.

Alongside this, not instead of it: the link between a reader's confidence and being right weakens for both groups. You can get out of a fall in accuracy through a recheck procedure; you can't get out of broken calibration, because the person doesn't know which cases to send for a recheck. This shouldn't be ranked above the between-group difference: calibration is the study's second finding, not its first.

What does NOT save you. One hundred forty radiologists, fifteen chest X-ray tasks: experience, subspecialty, and familiarity with the tools don't predict who the model's help will benefit and who it will hurt; the common assumption that weaker readers come out ahead is refuted. What does predict it is the presence of model errors. There's deliberately no figure for this quantity: its whole content is the absence of a link. But that study measured what predicts the BENEFIT from a suggestion, while the EKG study measured the DEPTH OF THE FAILURE on an error — these are two different questions, and there's no conflict between the two sources. Collapsing them into one conclusion, "experience doesn't help," would give exactly the opposite conclusion from the one the EKG study's authors actually print.

Where's the ceiling, if someone asks "can this be fixed by changing how it's presented." One hundred ninety-nine crowd-platform participants, a nutrition-composition task — non-clinical and with no stakes; the suggestion's accuracy was simulated at a seventy-five percent level, no model was trained. Forced presentation techniques — not showing the suggestion until requested; the person's own decision first, suggestion second; a delay before display — cut agreement with the incorrect suggestion from sixty-four to forty-eight out of a hundred. This pair is counted on one task in the set; on the aggregate metric across all tasks the shift didn't reach significance. Both halves hold together: sixteen points is a real improvement, and even with it, close to half of the agreements remain. The cost is measured by the same study: the interfaces that cut reliance the most were rated worse by users. There's no breakdown by expertise in this study at all, so its figures don't fit under the matrix above, and they can't be placed there.

And the overall point of this pair of slides, the reason it sits right here, after three case studies on the suggestion. In all three, the person either trusted the suggestion more than they should have, or got nothing from it at all — and in none of the cases was the reason that they knew too little. Expertise does enter the picture, and measurably so: it reduces both the depth of the failure and how often people agree with an incorrect suggestion. You can't say "experience doesn't help"; the true statement is "experience isn't enough." Hence the ceiling: redesigning the presentation is possible, and it buys a significant sixteen points, but close to half of the agreements with an incorrect suggestion remain even under the strongest measure tried. So "we'll teach people not to trust blindly" isn't a process measure, it's a wish; the only thing that counts as a measure is something that changes the order of presentation and the distribution of responsibility.

**Sources.** [Bond et al., Journal of Electrocardiology 2018](https://doi.org/10.1016/j.jelectrocard.2018.08.007) · [Yu et al., Nature Medicine 2024](https://doi.org/10.1038/s41591-024-02850-w) · [Buçinca et al., To Trust or to Think, CSCW 2021](https://arxiv.org/abs/2102.09692) · [Dietvorst et al., Algorithm Aversion, 2015](https://doi.org/10.1037/xge0000033)
