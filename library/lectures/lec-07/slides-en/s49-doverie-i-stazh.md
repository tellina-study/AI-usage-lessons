---
# РАЗРЕЗАН НАДВОЕ ПОД ИГРУ-ПРЕДСКАЗАНИЕ, прожарка сторителлинга #293, Этап C (П3, раздел 3).
#   Было: один кадр, на котором матрица сразу печатала обе колонки — и верную расшифровку, и
#   неверную. То есть вопрос и ответ стояли рядом, и предсказать зал не мог ничего: он читал
#   готовое. Прожарка дословно: «вопросы залу в деке есть (11 кадров) — но ни один не устроен
#   как игра с вскрытием».
#   Стало: ЭТОТ кадр несёт постановку, базу и вопрос; вскрытие — на `s49_1`, следующем.
# ВОПРОС — ПРЕДСКАЗАНИЕ НА МАТЕРИАЛЕ КЕЙСА, А НЕ ПРО РАБОТУ СЛУШАТЕЛЯ (решение владельца
#   2026-10-22: вопросы «у кого на работе» сняты как класс — работают в зале немногие).
#   Предсказывается то, что на следующем кадре посчитано, и предсказание проверяемо за
#   пятнадцать секунд.
# БАЗА ОСТАЁТСЯ НА ЭТОМ КАДРЕ, И ИНАЧЕ ИГРЫ НЕ ВЫХОДИТ: предсказывать падение, не видя,
#   ОТ ЧЕГО оно считается, нельзя — это была бы угадайка, а не предсказание. Поэтому колонка
#   «верная расшифровка» (84,86 и 86,38) стоит здесь, а скрыта только колонка «неверная».
#   Это же исполняет Baseline Mandate: знаменатель предъявлен прежде числа.
# СХЕМА ОСТАЛАСЬ ЗДЕСЬ, а не уехала на вскрытие: она показывает ПОРЯДОК чтения — расшифровка
#   приходит до собственного решения, — то есть ровно то, из чего зал и должен выводить своё
#   предсказание.
id: s49
local_id: s3-12
section: "3. Постановка диагноза"
type: case
title: "An EKG with a machine readout: what happens when the readout is wrong"
assertion: "Постановка опыта и его база предъявлены прежде результата: 30 стажёров двух групп читали по сто кардиограмм, и при ВЕРНОЙ машинной расшифровке обе группы читают почти одинаково — 84,86 и 86,38 из ста; зал предсказывает, что станет с этими числами на неверной расшифровке и у кого падение глубже, после чего предсказание вскрывается на следующем кадре"
source: "Bond et al., Journal of Electrocardiology 2018 — https://pubmed.ncbi.nlm.nih.gov/30122457/"
media: ""
media_needed: "рисунок первоисточника по кардиограммам — добыть и проверить права; запасной вариант — собственные три плашки разных жанров"
media_note: "иллюстрация не добыта. Снимка кардиограммы с машинной расшифровкой на кадр НЕ ставится из общего правила: картинку лучше не ставить вовсе, чем ставить слабую, а нарисованная нами «как бы кардиограмма» была бы ровно макетом, который канон запрещает"
scheme:
  caption: "The readout arrives before the trainee's own decision; the study never measured reading without it"
  arrows: true
  rows:
    - {label: "How they read", steps: ["EKG with the readout", "trainee reads", "report"]}
pol_slov: 110   # НОВОЕ ЗНАЧЕНИЕ ПОД РАЗРЕЗАННЫЙ КАДР (#293, Этап C). Прежние 147 объявлялись под кадр, который нёс И матрицу целиком, И обе плашки потерь: они уехали на `s49_1`. Здесь остались постановка опыта, колонка базы и вопрос. Переобъявляется по собранному PDF этапа — мера берётся с вывода, а не со входа
timing_min: 0.45
in_bucket: true
method_steps: ["упоминание"]
form: ["сетка", "вопрос залу", "[VFY]"]
vfy: true
status: собран
---

## Visible slide text
**30 trainees each read a hundred EKGs, each one three times:** without a readout · with a single machine readout, half of them wrong · with several candidate diagnoses. 15 per group — cardiology trainees and trainees from other specialties.

**With a CORRECT readout, both groups read almost identically:** 84.86 out of a hundred for the cardiology group, 86.38 for the other.

**Question: what happens to these two numbers when the readout is wrong — and whose drop will be deeper?**

## Speaker notes

Thirty trainees read EKGs: fifteen cardiology trainees and fifteen from other specialties. Each one went through a hundred EKGs three times: without a readout, with a single machine readout half of which were wrong, and with several candidate diagnoses. Nine thousand readings in total. The order of reading decides everything here, and it's shown in the diagram: the readout arrives BEFORE the reader's own decision, not after — meaning the reader sees someone else's answer before forming their own.

Nine thousand readings are repeated measurements on thirty readers; they aren't independent observations, and the authors themselves name this limitation. The third condition, with several candidate diagnoses, doesn't take part in the rest of the case study: the slide is carried by the first two, where there's a single suggestion that's either right or wrong.

The strong side of this design is that a reader is compared against themselves. The same thirty people, the same hundred EKGs, the only difference being what sits next to the tracing. So the result can't be explained by different training between the groups, or by different difficulty in the material: the material is the same, and the reader is the same.

And one thing this study doesn't measure, even though it looks like it does. Half of the readouts are wrong by the authors' own design — a hand-made substitution, not the behavior of a real device. So what's in front of us is a measurement of the human, not a measurement of the quality of a machine readout: the question isn't "how good is the readout" but "what does a readout the reader has come to trust do to them."

The baseline. With a correct machine readout, both groups read almost identically — eighty-four and eighty-six hundredths out of a hundred for the cardiology group, eighty-six and thirty-eight hundredths for the other. A point and a half of difference. Everything that follows is counted from this point, and it has to be read precisely: the baseline for the drop is the CORRECT readout, not reading with no suggestion at all. The study doesn't publish a "with no readout at all" column by group, there's nothing to reconstruct it from, and there's no comparison here against reading on its own. This narrows the conclusion: what's measured is what an incorrect suggestion does to a reader against a correct one, not what a suggestion does against having none.

Now the question, and it gets asked twice, because it has two halves. First: how far will these numbers fall when the readout is wrong? Name the order of magnitude — five points, fifteen, by half? Second, and this one's more interesting: whose drop will be deeper — the cardiology trainees' or the other specialties' trainees'? You can answer out loud or in one word in the chat: "cardiology" or "the others."

The common assumption here is that the suggestion's winners and losers split roughly evenly, and that if someone falls deeper, it's the person with less training; the second half of this assumption happens to be true, and the room usually guesses it. But the first half — the depth — the room almost always underestimates: people name five to ten points. The real number is on the next slide, and the gap between what's named and what's real is exactly why it's worth pausing here.

If the room stays silent, both halves get named as options and the room votes by show of hands: "a drop of less than fifteen points" against "a drop by half." A closed question with two options almost always gets a show of hands; an open one almost never does.

One caveat before the reveal, so it doesn't later look like an excuse. Experience is NOT the same between the groups — thirty-six plus or minus eleven months against twenty-eight plus or minus thirteen. What actually distinguishes them is specialty, and the authors build their conclusion on exactly that, but saying "their experience is the same" would be saying something false.

**Sources.** [Bond et al., Journal of Electrocardiology 2018](https://doi.org/10.1016/j.jelectrocard.2018.08.007)
