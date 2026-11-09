---
# СХЕМА ДОБАВЛЕНА (п. 11 наряда, §11.3: «схема обязательна у каждого кадра типа `case`»).
# Замер прожарки: схема нашлась у 5 кадров `case` из 12 в разделе, и не было её ровно у семи
# самых тяжёлых по тексту — то есть там, где она нужнее всего. §10.3: схема решения несёт
# инженерное содержание, текст — пояснение к ней, не замена; поэтому вместе со схемой из тела
# СНЯТО то, что она теперь показывает сама (п. 12 наряда, плотность: чинить схему и объём
# вместе, а не по очереди).
# ВОССТАНОВЛЕНО (#283, задача 2) вместе с s30 — см. комментарий там. `section` поправлен на
# актуальное имя раздела (было дочернее название ДО слияния разделов 2+3).
# ПЕРЕИМЕНОВАНО СЛОВО «ПОПРАВКА» В СХЕМЕ (владелец 2026-10-20, «переименуй»). Было «Поправка
# метода» / «алгоритмическая поправка» в значении «алгоритмическая коррекция систематического
# смещения модели». Это КОЛЛИЗИЯ С ИМЕНЕМ МЕХАНИЗМА: «Поправка» — шестое из шести когнитивных
# искажений входа (`s01ae`, рамка работы владельца), и там оно значит ровно обратное по субъекту —
# ВРАЧ правит заключение модели, когда находит в нём ошибку (`s63a`, `s64`). Один и тот же кадр
# раздела 2 называл тем же словом действие алгоритма над собой. Стало «Коррекция алгоритмом» /
# «алгоритмическая коррекция» — слово из той же работы и из главы (`chapter-part1c.md`), новых
# понятий не введено. Форма сохранена 1:1, включая повтор корня между подписью ряда и шагом:
# у исходной пары «Поправка метода» / «алгоритмическая поправка» он был ровно такой же.
# Вес кадра не изменился — 160 слов видимого слоя до правки и 160 после (замер частичной сборкой).
# Смысл не изменился: тот же путь против смещения, тот же исход «разрыв не уменьшился».
# Корень «правк» в замену не взят сознательно — «врач правит» и есть содержание механизма «Поправка».
id: s30a
local_id: s2-07a
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 4, cost: dataset composition is what heals the gap"
assertion: "Цена ошибки сместилась на подгруппу, которой в обучающем наборе было мало, и единственное измеренное исправление пришло из состава данных, а не из алгоритмических методов борьбы со смещением"
source: "Daneshjou et al., Science Advances 2022 — https://doi.org/10.1126/sciadv.abq6147"
media: ""
media_needed: "иллюстрация не нужна — плашка пары и строка о прочерке держат экран сами"
media_note: "—"
blocks:
  - {label: "Fine-tuned on a set with an equal share of dark tones", value: "light 73 · dark 76 out of 100", note: "the gap didn't disappear, it flipped; what heals it is collection and labeling, not the algorithm", key: true}
  - {label: "Three algorithmic bias-correction methods", value: "did not shrink the gap", note: "same study, same data"}
  - {label: "For the classical methods, the gap", value: "was never measured at all", note: "neither the meta-analysis nor the reviews break accuracy down by skin tone"}
  - {label: "Delivered → required", value: "an assessment where there is no dermatologist → a dataset matching the composition of those it works on", note: "net: the average holds up, the cost lands on the subgroup"}
pol_slov: 137   # О10 (#229): разбор: названный пробел «разрыв у классических не измерен» + база у каждого числа + подвал-рукоятка. О13 (#229): вставлена работа, на место которой пришла модель («посмотреть на образование и решить, показывать ли врачу»; «делал это врач глазом или специалист дермоскопом; теперь снимок читает модель»), пункт 1 «кто и что делал»: кадр начинался со сместившейся цены, и что именно сместилось, зал без голоса не видел
opyt_net: "вторая половина примера: опыт описан на s30 — один и тот же набор на три модели, 656 изображений с биопсией (208 светлых · 241 средних · 207 тёмных), светлые тона против тёмных в пунктах площади под кривой. Здесь стоит цена и проверка исправления ИЗ ТОЙ ЖЕ работы (дообучение на представительном наборе против трёх методов борьбы со смещением, chapter-part1c.md:168) — своего отдельного опыта у этих двух строк нет, а пересказывать описание соседнего кадра значило бы занять им четыре плашки, которые тут и держат экран"
scheme:
  caption: "Of two paths against bias, one worked, and it isn't a matter of picking a method"
  arrows: true
  rows:
    - {label: "Algorithmic correction", steps: ["algorithmic correction", "the gap did not shrink"]}
    - {label: "Dataset composition", steps: ["fine-tuning on a representative set", "the gap closed"]}
timing_min: 0.8
in_bucket: true
method_steps: ["⑤что переехало", "пара дало–потребовало"]
form: ["форма 7"]
vfy: true
status: собран
---

## Visible slide text

**What moved.** The cost of an error shifted: the dataset average stayed respectable, while the subgroup underrepresented in the training set pays.

**The absence of a measurement does not prove equality.**

*The fix is measured in this same study; in a real clinical setting, none of the three is.*

## Speaker notes

There is one form here, and it is named directly: the cost of an error shifted. The place is the same and the performer is the same, but what the error actually costs got distributed differently — differently for different people. Average accuracy on the dataset stays respectable, and a deployment report with one number will show everything is fine. The subgroup whose images were underrepresented in the training set is the one that pays, and its contribution to the average sinks by construction: it is the smaller part of the dataset.

The fix in this breakdown is actually measured, and that is a rare thing — bias usually gets discussed without the remedy ever being checked. Fine-tuning on a representative set closes the gap, and even flips it. Three algorithmic bias-correction methods did not shrink it significantly. The conclusion here is uncomfortable for engineering taste: what fixes the gap is collection and labeling — the part of the work most often outsourced and treated as grunt work. The model does not fix it.

What an engineer should take from this. The composition of the training set is not grunt work and not something to hand off to an intern: here it turned out to be the only thing that fixes the measured gap, while three methods built specifically to fight bias did not fix it. This is an uncomfortable conclusion, and it is checkable — the check sits in the same study, right next to the gap itself.

The pair that closes this breakdown. Delivered: a standing assessment of a skin lesion where there is no dermatologist — access, not accuracy. Required: a dataset that mirrors the composition of those the system will actually work on, and knowing that composition in advance. Net: the average holds up, the cost of the error moved onto a subgroup, and you cannot see this from the average.

And the line that carries the whole breakdown. The gap by skin tone is measured for the model, and never measured at all for the classical methods: neither the direct-comparison meta-analysis nor the reviews break accuracy down by skin tone. So there is nothing to say "the model is worse than the human on this subgroup" with, and claiming it would be exactly the mistake this breakdown exists to catch. The correct statement is different, and checkable: for the model the gap is measured and named; for the human it is measured by nobody, and the absence of a measurement is not evidence of equality.

This is worth holding onto for a second, because the opposite gets said more often. From the fact that the gap by skin tone is unmeasured for classical examination, it does not follow that classical examination has no gap: it only follows that nobody looked. The difference between "measured and equal to zero" and "unmeasured" is exactly the difference between evidence and its absence, and confusing the two is equally wrong in either direction.

Hence a practical question for any vendor: on whom was your average computed, and which subgroups dissolved into it. This question is worth asking before purchase, not after deployment, because after deployment the average will be the only number in the report — and it will look good.

And about how this cost looks in a report. If a system like this were deployed and measured with one number — average accuracy across all images — the report would show smooth, honest well-being: the average really does hold up. The shifted cost can only be seen by breaking the measurement down by subgroup, which means knowing in advance which subgroups to break it down by. This study broke it down by skin tone; which subgroup will turn out to matter in the next task does not follow from the model itself in any way, and someone who knows the subject has to name it.

**Sources.** [Daneshjou et al., Science Advances 2022](https://doi.org/10.1126/sciadv.abq6147)
