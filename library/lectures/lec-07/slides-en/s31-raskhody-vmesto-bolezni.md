---
# ЧИСЛО, КОТОРОГО НЕТ В ПЕРВОИСТОЧНИКЕ, СНЯТО С КАДРА (п. 7 наряда; канон §14, строка
# «число на слайде = число в главе», и прямо — «разные наклонения считаются расхождением»).
# БЫЛО: плашка «Мест уходило не тем, кому нужнее — 28,8 из ста». Два дефекта разом.
# ПЕРВЫЙ: 28,8 — это разность 46,5 − 17,7, выведенная нами. У Obermeyer и соавторов (Science
# 2019) такого числа нет ни в каком виде; вычисленное выдавалось за измеренное.
# ВТОРОЙ: изъявительное прошедшее — «уходило». Глава требует обратного дословно
# (`chapter-part1c.md:211`): «произносить это надо условным наклонением, иначе глава выдаст
# арифметическое упражнение за внедрённое исправление». 46,5 — это расчёт авторов на тех же
# данных: они заменяют на границе отбора более здорового пациента более больным, пока разрыв
# не исчезнет, и смотрят, какой состав получится. Ни внедрения, ни переобучения за этим нет.
# СТАЛО: обе измеренные точки названы своими именами, 17,7 как наблюдаемая доля, 46,5 — в
# сослагательном («поднялась бы»), с прямой пометкой, что это расчёт, а не внедрение.
# Выведенная разность не произносится вовсе: называть её значило бы вернуть ту же подмену
# через запятую.
# СВЁРТКА (#229): кадр собран из s31 и s32 (второй файл в slides/_snyato/). Сведён в одну форму §5.13 сессией содержания: три вопроса владельца (п. 29 — сколько выпало, сколько лишних попало, какой эффект на деньги и здоровье) отвечены плашками, а на третий ответ — «не измеряли», и он назван на кадре.
id: s31
local_id: s2-08
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 5: selection into a high-attention program — a score instead of a physician's decision"
assertion: "Целевой переменной взяты будущие расходы на лечение, а решение принималось о болезни: при равном балле у пациентов одной группы болезней оказалось на 26 процентов больше, и доля этой группы среди отобранных составила 17,7 из ста, а при полностью убранном разрыве в здоровье поднялась бы до 46,5 — расчёт авторов, не внедрение; эффекта же на деньги и здоровье работа не измеряла вовсе, а исправление только посчитала"
source: "Obermeyer et al., Science 2019 — https://doi.org/10.1126/science.aax2342"
media: ""
media_needed: "кадр из первоисточника: график зависимости числа болезней от балла. Журнал не открытого доступа — права проверить; запасной вариант — собственная перерисовка с атрибуцией в подвале"
media_note: "иллюстрация не добыта"
blocks:
  - {label: "The cost of both errors", value: "an unwatched illness · an occupied slot", note: "coordinator time — someone else didn't get in"}
  - {label: "Share of Black patients among those selected: physician decided → the score decided", value: "19 → 17 out of 100", note: "49,618 patients of one hospital, 2013–2015; one sample, both regimes on it"}
  - {label: "At the same score, Black patients have more chronic conditions than white patients", value: "by 26 out of 100", note: "the score called equally healthy people whose health actually differs; 100,009 patient-years", key: true}
  - {label: "If the score had targeted illness rather than spending: the same share", value: "18 → 47 out of 100", note: "the authors' own calculation on the same data (17.7 → 46.5); this is a computation, not a deployment — no such rollout ever happened", key: true}
scheme:
  arrows: true
  rows:
    - {label: "Physician (saw the score)", steps: ["patient chart", "cue: the score", "the physician's decision"]}
    - {label: "The score alone", steps: ["chart + spending", {text: "spending forecast", ai: true}, "threshold-based selection"]}
pol_slov: 183   # #283 задача 2: объявлен ЗАНОВО после добавления `scheme` (без модели / с моделью
  # прогноза расходов). Добавление схемы дало блокирующие ([высота], затем [кегль]) при прежних
  # 221 слове и 4 плашках с длинными подписями/заметками — плашки сокращены (label короче, два
  # дублирующих куска note убраны: честный отказ «отбор без балла в работе нет» теперь несёт
  # сама схема рядом подписью ряда «Врач (видел балл)»), тело сокращено (строка «вход/выход»
  # снята — её держит схема). Итог: 0 блокирующих, 0 предупреждений о поле/кегле (тело держит
  # рабочий размер, не упёрлось в пол). Прежняя история ниже (О20, #229) — про состав ДО этой
  # правки, сохранена как есть.
# [ПРЕЖНЕЕ, #229] pol_slov: 221   # О20 (#229): объявлен ЗАНОВО после свёртки s31+s32 — прежнее число называло состав до склейки. Склейка дала 206 слов по PDF, 5 плашек (вторым рядом), тело 8,5 пт и два блокирующих. Сжато ЗАМЕНОЙ.
# СКАЗАННОЕ ДВАЖДЫ, снято: «Исправление посчитали и не применили» стояло и заголовком второй половины, и строкой тела, и подписью плашки — осталась подписью плашки, у самого числа; «Покупает такой счёт администрация или плательщик, не врач, и „дорого лечится" от „болен" он не отличает» снято как пересказ соседнего «обучено предсказывать расходы, а решение принималось о болезни» — механизм назван один раз; «Как мерили. Задним числом по данным одной больницы авторы сравнивали балл с числом активных хронических состояний» ушло в заметки: устройство замера здесь ретроспективное и однотипное, а место первой строки занял шаг стадии — чего не было вовсе; «Расчёт авторов на тех же данных — не измерение» в подвале дублировал подпись своей же плашки.
# ЧЕМ ЗАНЯТЫ СЛОВА: три вопроса владельца (п. 29) отвечены числами, и каждый ответ — плашкой. «Сколько лишних попало и сколько выпало» — ПРЕЖНЯЯ РЕДАКЦИЯ отвечала на него разностью 28,8, и эта строка описывает её, а не действующий кадр: разность снята, см. верх фронтматтера. Ответ теперь дают обе измеренные точки — наблюдаемая 17,7 и контрфактическая 46,5 в сослагательном. «Больше опознанных — плохо или хорошо» — «при равном балле болезней больше на 26 процентов», то есть больше опознанных тут не выигрыш, а признак того, что балл считает не болезнь. «Какой эффект на деньги и здоровье» — ответ «работа этого не измеряла: посчитан состав отобранных, а не исходы людей» (13 слов): числа на этот вопрос нет, и пробел назван на кадре, а не замазан оценкой отраслевого масштаба в 200 миллионов человек, которая выборкой измерения не служит.
# ЧТО ЕЩЁ ВСТАЛО: шаг стадии в заголовке и первой строке («отбор в программу повышенного внимания — балл вместо решения врача», §5.18 и §5.22) — владелец заметил, что пример скорее из отбора, чем из исследования, и кадр теперь называет свой шаг сам.
# ЦЕНА, названная числом (замер по собранному PDF): пять плашек → четыре (второго ряда больше нет), тело поднялось с 8,5 до 14,0 пт, оба блокирующих ушли. Слов 206 → 221: проза срезана вдвое, но три ответа владельцу числами прибавили больше, чем ушло.
timing_min: 1.65
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало", "упоминание"]
form: ["сетка", "[VFY]", "форма 5", "форма 7"]
vfy: true
status: собран
---

## Visible slide text

**Selection into a high-attention program.** A physician used to decide — now a single number decides. **It is trained to predict future treatment spending**, while the decision being made was about illness: spending reflects utilization, and utilization differs across groups with the same underlying health.

**How it's built.** *Forecasting on structured data.*

**The cost of an error moved** — onto the group that, at the same score, has more illness. **The study did not measure the effect on money or health.**

## Speaker notes

This is about a high-attention program: a hospital sets aside a limited number of slots for people who need closer-than-usual monitoring. The cost of both errors is counted in slots. Someone who needed the program and didn't get in — the illness progresses unwatched, and it is found out at hospitalization. Someone who didn't need it and got in anyway — a slot and a coordinator's time are spent, meaning someone else, a third person, didn't get in.

Both classical regimes are counted on the same sample. With selection by the treating physician's decision, the share of the group in question among those actually selected is 19.2 out of 100. With selection by a single spending-forecast score, it is 17.2 out of 100. The two numbers are close, differing only by the label of the regime, which is why they are not said back to back.

A limitation of this count has to be named out loud, and it matters: the physician selecting patients had already seen the score — above the threshold, he received a cue. So what is counted is selection by a physician who has the score at hand; there is no selection without the score anywhere in the publication. The comparison therefore runs not between "human" and "model", but between two regimes, in one of which the human works with a cue.

The model against these regimes. The system computes one score per patient, selection runs on a threshold, and the target variable taken is future treatment spending. The result: at the same score, one group turned out to have 26 percent more illness. In other words, to get into the program, they had to be sicker at the same assessed risk. The base is named in full: 49,618 patients of one academic hospital, 100,009 patient-years, 2013–2015. The denominator belongs to one hospital, and conclusions about the size of the skew belong to it, not to the industry.

Here is how it's built: input is chart records and spending data, output is one score per person and threshold-based selection. The publication gives no name for the commercial algorithm — and this is a refusal to name it, not an omission: the authors are analyzing a system they are not permitted to name.

The mechanism is worth unpacking slowly: the choice of target variable was engineering-sound, and it is instructive exactly because of that. Spending exists for every patient, it is numeric, requires no labeling, and really does correlate with illness. But spending reflects utilization — how much a person has used medicine — and utilization differs across population groups with the same state of health. The error is not in the model, and not in the data, taken separately: nobody wrote down what the decision was supposed to target, and what the data happened to contain became the target instead.

The authors calculated what would happen if the health gap at the selection boundary were removed: the share of this patient group among those selected would rise from an observed 17.7 to 46.5 out of 100. This has to be stated in the conditional, or the exercise gets passed off as an implemented fix. The calculation works like this: at the boundary, a healthier patient is swapped for a sicker one until the gap closes, and the resulting composition is observed. There is no deployment behind this, and no retraining either.

The authors also actually retrained a model, and the result is weaker than the calculation. Their own predictor, based on the number of active chronic conditions, gives 26.7 out of 100 in the highest-risk group, against 14.1 for their own spending predictor trained on the same data. And the observed share of 17.7 belongs to the commercial algorithm the authors are analyzing — a third model — and one cannot be subtracted from the other: no such difference exists in the original source. The more precise lesson: changing the target variable moves the composition of those selected, and still falls short of 46.5.

What moved. The performer changed: selection used to be done by the treating physician, now a single score does it. And the cost of an error shifted — onto the group that, at the same score, has more illness. The pair that closes this breakdown: delivered consistent selection where manual selection is inconsistent; required a match between spending and illness that does not exist; net, for one group selection got worse than before, and the fix is, to this day, only calculated.

On scale and its denominator — separately, because these two numbers are easy to combine wrongly. Models of this class are applied, by industry estimate, to roughly 200 million people a year. This is a coverage estimate, not a measurement sample: the skew was measured on 49,618 patients of one hospital, and conclusions about its size belong to that denominator, not to the two hundred million. These numbers are in different units and cannot be added together — which is why only the second one is on the slide.

And something worth saying to an engineer directly. The target variable in this task was not chosen out of laziness: spending exists for every patient, it is numeric, requires no labeling, and really does correlate with illness. Anyone sitting in this room would have chosen the same one, given the same data and the same deadline. The error is not in the choice — it is that nobody wrote down what the system treats as its target, and so nobody checked whether that target matches the decision's actual purpose. There is no procedure for that check in the order of work, and the section's conclusion says so.

And a last point, on the limits of this lesson. This was measured at one academic hospital over three years, on 49,618 patients. The conclusion about the mechanism — that choosing the target variable moves the composition of those selected — carries over; the specific size of the skew carries over nowhere, and it must not be stated as an industry figure.

**Sources.** [Obermeyer et al., Science 2019](https://doi.org/10.1126/science.aax2342)

What exactly was being decided: who to call in for intensified monitoring.

And about the tool itself: the publication gives no name for the algorithm.
