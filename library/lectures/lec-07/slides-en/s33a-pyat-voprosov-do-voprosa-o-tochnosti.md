---
# НОВЫЙ КАДР (переделка раздела 2 по канону PR #286, п. 3 наряда). Закрывает находку
# методической прожарки: §2.9 главы даёт четыре вопроса инженера как «рабочее правило,
# сформулированное проверяемо», и это — по оценке прожарки — самый ценный для зала
# практикующих инженеров вынос раздела. На кадре его не было НИ ОДНОГО: оба упоминания
# жили в заметках `s31` и `s50`, то есть в слое, которого зал не видит.
# СЧЁТ В ГЛАВЕ БЫЛ ПРОТИВОРЕЧИВ, И ПРОТИВОРЕЧИЕ ПОПРАВЛЕНО В ГЛАВЕ, А НЕ ОБОЙДЕНО ЗДЕСЬ.
# `chapter-part1c.md:235` говорит «ошибиться можно в трёх местах» (вход · набор · цель — и
# ровно три разбора раздела — круг 6 добавил к ним два отечественных), а `:239` — «вопросы, и каждый из них в этом разделе
# провалил по одному внедрению». Второе неверно арифметически: внедрений в разделе три, а не
# четыре, и вопрос «чем измерен вход» провалил не внедрение — у пульсоксиметра обученной
# модели нет вовсе, там нечему было внедряться. Сверено по §2.5–2.8. В главе формулировка
# исправлена тем же кругом; здесь кадр говорит то же и так же: три вопроса сорвали по
# внедрению, четвёртый сорвал измерение до всякой модели.
# ПОРЯДОК ВОПРОСОВ — ПО ПОРЯДКУ РАЗДЕЛА, не по весу: группа (§2.2 и Таиланд), вход (§2.5),
# набор (§2.7), цель (§2.8). Так зал узнаёт каждый вопрос по уже разобранному случаю.
# ПРИНЯЛ АДРЕС И ПОЛНОТУ ЗАМЕРА ПРИБОРА, Этап B прожарки сторителлинга (#293, П5): кадр
# `s26a` («Что работает и что не работает, когда измерение читает модель») снят, и вместе с
# ним с видимого слоя раздела ушло единственное место, где у замера насыщения крови стоял
# адрес. Сам тезис и его числа — 12 раз из ста против 4 — на этом кадре стояли и стоят, второй
# строкой перечня; снятый кадр их удваивал (прожарка П5: «это дубль „чем измерен вход“ из
# s33a — оставить одно место»). Перенесено сюда три вещи, которых здесь не было:
#   (1) АДРЕС работы — поставлен в `source`, то есть в подвал, а не только в заметки: число
#       стоит на видимом слое, и адрес у него обязан быть там же;
#   (2) НАПРАВЛЕНИЕ смещения — прибор показывает ВЫШЕ, чем даёт анализ, значит опасное
#       снижение насыщения пропускается чаще. Без направления «смещение одностороннее»
#       ничего не говорит: сторона важнее величины;
#   (3) ДАТЫ двух документов регулятора — предупреждение 19.02.2021 и проект требования
#       испытывать приборы на разных тонах кожи 06.01.2025. Прежняя формулировка заметок
#       («регулятор это признал документом») называла факт и не называла, чем именно.
# ЧЕГО СО СНЯТОГО КАДРА ЗДЕСЬ НЕ ВОССТАНАВЛИВАЕТСЯ, и это проверено, а не пропущено: его
# половины «работает / не работает» (постоянство · поток · воспроизводимость против годности
# входа · переноса · смещённого входа) стоят ДОСЛОВНО столбцами на `s33`, выводе того же
# раздела. То есть шаг «что работает, а что нет» у раздела остался; с кадра `s26a` он только
# перестал предъявляться дважды.
id: s33a
local_id: s2-09a
section: "2. Инструментальная и лабораторная диагностика"
type: summary
title: "Five questions asked before the question of accuracy"
assertion: "Прежде чем спрашивать про точность, спрашивают на какой группе посчитаны доли, чем измерен вход, из чего собран обучающий набор, что система считает своей целью и во что обходится ложная тревога — три из этих пяти вопросов сорвали в разделе по одному внедрению, четвёртый сорвал само измерение, в котором обученной модели нет, а пятый развёл два московских случая: в одном автономию дали, в другом запретили"
source: "Sjoding et al., New England Journal of Medicine 2020 — https://doi.org/10.1056/NEJMc2029240 · US regulator warning, February 19, 2021, draft guidance January 6, 2025"
media: ""
media_needed: "иллюстрации нет: кадр и есть перечень из четырёх строк, каждая со своим случаем; картинка здесь отняла бы место у самих вопросов"
media_note: "—"
blocks:
  - {label: "Questions before the question of accuracy", value: "five", note: "each one paid for by a case already broken down"}
  - {label: "Sank a deployment", value: "3 of 5", note: "Thailand · skin · program selection", key: true}
  - {label: "The fourth sank the measurement itself, the fifth settled the question of autonomy", value: "the device · the cost of an alarm", note: "the cost of an alarm is what told the two Moscow cases apart"}
timing_min: 0.7
in_bucket: true
method_steps: ["вывод раздела"]
form: []
vfy: false
status: собран
---

## Visible slide text

**"What's its accuracy" is question six. Five come before it.**

- **On what group were the shares computed?** The set was assembled from images already selected for quality; in the field, that selection is made by a human with no rule — *Thailand*.
- **What measured the input?** The device read normal while the blood test showed oxygen deprivation: **12 times out of 100 against 4**. There is no trained model in the device.
- **What was the training set made from?** Dark tones were scarce in the sets: on dark skin, the model distinguishes sick from healthy **9–15 out of 100 worse** (100 is no misses, 50 is a coin flip) — *skin*.
- **What does the system treat as its target?** Trained on future spending, while the decision being made was about illness — *program selection*.

- **What does a false alarm cost, and is there time to check it?** One city: on the preventive stream, autonomy was **granted**, on emergency scans it was **withheld** — **293 false alarms against 4** from the physician.

**Three sank a deployment each. The fourth sank the measurement itself. The fifth decides whether a human can be removed at all.**

## Speaker notes

Five questions get asked before the question of accuracy: on what group were the shares computed, what measured the input, what was the training set made from, what does the system treat as its target, and what does a false alarm cost. "What's its accuracy" is question six. Each of the five is already paid for by a case already broken down, so none of them hangs there as generic advice.

The first question is about the group, and it runs through the entire section. We started with the fact that one and the same system gives eight correct alarms out of a hundred and seventy-nine out of a hundred, and the difference is set not by the device but by whoever decided who gets examined. But this question has a second, less obvious half, and Thailand is what sank it. The lab set used to measure reading accuracy was assembled from images that had already passed a quality selection. In the field, there is a selection too — made by a human nobody told the rule for. So the group the shares were computed on and the group the system actually works on differed not by diagnosis but by input quality, and nobody measured this before deployment.

The second is what measured the input. This is the cheapest of the four questions and the least often asked. "What data was it trained on" gets asked often; "what obtained every value in that data" — almost never, even though the device's own documentation answers it, not a study. A device that reads blood oxygen saturation from light absorption in tissue stands here as proof that bias can exist before any training at all: a discrepancy with direct blood testing in 11.7 percent of measurements in patients with dark skin against 3.6 percent in light-skinned patients. Without the denominators, this number does not read: eighty-eight discrepancies out of seven hundred forty-nine measurements against ninety-nine out of two thousand seven hundred seventy-eight. This is one named cohort from one study; the multicenter cohort in the same paper gives different numbers, and the two are not stated side by side — two sets from one study read as a single sample and get spliced together.

The direction of the bias matters more than its size here. The device reads HIGHER than the blood test does — meaning it misses dangerous drops in saturation more often, that is, the error leans toward "everything is fine." And this is not researchers' speculation but a recognized measurement problem, recorded in two documents: a US regulator warning from February 19, 2021, and a draft guidance from January 6, 2025, requiring these devices to be tested across different skin tones. There is no trained model in the device at all — it is optics and light-absorption arithmetic devised long before any machine learning. A system that takes blood saturation as an input — and early-warning systems do, we will meet one in the next section — inherits the bias: it does not create it, does not amplify it through any fault of its own, but receives an already-biased number and works with it as if it were a measurement. Strength of evidence: a prospective comparison against direct blood testing, with the direction confirmed independently and recorded in a regulator's document — high.

Hence a conclusion that is easy to miss while arguing about algorithmic fairness: what needs checking is not only the model, but also whatever measured its input.

The third is what the training set was made from. The skin breakdown: three models lose nine to fifteen points of area under the curve on dark tones, which were scarce in the sets. And this is also the section's one piece of good news: this gets fixed by collection and labeling, not by choice of method. Fine-tuning on a representative set closed the gap; three algorithmic bias-correction methods did not.

The fourth is what the system treats as its target. Selection into a high-attention program: the target variable chosen was future treatment spending, because it exists for everyone, it is numeric, it needs no labeling, and it correlates with illness. And what it reflects is utilization, which differs across groups with the same underlying health. Nobody wrote down what the decision was actually supposed to target, and what the data happened to contain became the target instead.

Now about the count, and this slide's count is honest rather than rounded. There are four questions, and three deployments in this section — and the temptation to say "each question sank a deployment" has to be put down. Three questions sank one deployment each: group — Thailand, dataset — skin, target — program selection. The fourth, about the input, sank none, because the pulse oximeter has no trained model at all: there was nothing there to deploy. And that is exactly what makes it the most useful of the four — it is the only one checking something that sits upstream of the model and will outlive any replacement of it.

If asked why the accuracy question is placed fifth, and whether it is even needed. It is needed, but it is derivative: the answer to it only reads correctly after the first two. A stated accuracy figure without a named group and a named prevalence does not mean anything — that is the rule this section hands off to the whole lecture, and it is also what explains why the order of questions runs this way and not in reverse.

The fifth is what a false alarm costs and whether there is time to check it. This question appeared last in the section, and turned out to be the one that settles the question of autonomy. The two Moscow cases stand side by side not for balance: one city, one oversight body, one circle of registered products. On the preventive stream, the model was tuned to raise alarms generously — and sent to work without a human, because a false alarm there costs one follow-up exam, and there is time. On emergency head scans, the same generosity produced 293 false alarms against four from the physician, and the authors state directly: the model's place is second reader, not first. A false alarm there costs a deployed crew, and there is no time to check it. The quality of the models does not tell these two cases apart.

**Sources.** [Sjoding et al., New England Journal of Medicine 2020](https://doi.org/10.1056/NEJMc2029240) — the discrepancy between the blood-saturation device and direct testing. The addresses for the other four questions are on the slides of their own breakdowns.

And the question for the room on this slide is a prediction. Five questions are in front of you, and behind each stands a case already broken down today. I ask you to name which of the five, in your view, sinks a deployment most often — and to say why in one phrase. The answer we'll arrive at: the first three each sank a deployment, the fourth broke the measurement itself, the fifth decides whether a human can be removed at all — meaning the costliest thing is not accuracy, but the trigger threshold and who works through the false alarms. The room usually names the composition of the training set; it is third in order, and not first in cost.
