---
# НОВЫЙ КАДР (круг 6, 2026-10-19) — второй российский разбор по заказу владельца.
# Поставлен ВПЛОТНУЮ к первому сознательно: тот же город, тот же надзор, тот же
# круг зарегистрированных изделий — и обратный ответ на вопрос «можно ли убрать
# человека». Пара снимает вывод, который из одного первого случая напрашивается.
# Это ЕДИНСТВЕННЫЙ разбор раздела, где провалилось САМО ЧТЕНИЕ, а не место,
# состав набора или определение цели, — поэтому вывод раздела (`s33`) этим же
# кругом переписан: прежняя его формулировка «ни в одном из трёх разборов не
# провалилось само чтение» после добавления этого кадра стала неверной.
# Глава: `chapter-part1c.md` §2.5в.
id: s27c
local_id: s2-05c
section: "2. Инструментальная и лабораторная диагностика"
type: case
title: "Example 2: Moscow — intracranial hemorrhage, where autonomy was withheld"
assertion: "Тот же город и тот же круг изделий: на 3 409 томограммах головы модель одна подняла 293 ложные тревоги против 4 у врача и пропустила 45 кровоизлияний — но все 12, пропущенные врачом, нашла она, и из этой взаимодополняемости авторы выводят место второго читателя, а не первого"
source: "Khoruzhaya et al., Journal of Clinical Medicine 2025;14(16):5700 — https://doi.org/10.3390/jcm14165700"
media: ""
media_needed: "Поиск: настоящая фотография рабочего места врача экстренной службы за просмотром компьютерной томограммы головы — монитор с серией срезов, врач за консолью. Подлинный снимок, не постановка."
media_note: "иллюстрации пока нет; высота кадра занята схемой и тремя плашками. Слабая картинка здесь хуже пустого поля"
blocks:
  - {label: "The cost of both errors", value: "death or irreversible damage · a crew deployed for nothing", note: "it comes down to minutes — there is no time to check an alarm"}
  - {label: "False alarms on 3,409 scans: model alone → physician", value: "293 → 4", note: "73 times more; every twelfth scan would have gone down the emergency path for nothing", key: true}
  - {label: "The misses never overlapped once", value: "45 and 12", note: "the physician found all 45 the model missed; the model found all 12 the physician missed"}
scheme:
  arrows: true
  rows:
    - {label: "What was proposed", steps: ["scan", {text: "the model reads alone", ai: true}, "the emergency path"]}
    - {label: "What the measurement showed", steps: ["scan", {text: "the model flags a suspicion", ai: true}, "the physician decides — and stays the first reader"]}
pol_slov: 165   # замер по собранному sec-2.pdf, круг 6: разбор по форме §5.13: три плашки, схема «что предлагали / что вышло», оговорка про отсутствующее измерение
timing_min: 1.3
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "⑤что переехало"]
form: ["форма 3"]
vfy: true
status: собран
---

## Visible slide text

**The same Moscow, the same circle of services — the opposite answer.** 3,409 head CT scans, 67 clinics, 2022–2024; hemorrhage in 1,101 people.

**This reads by count, not by share.** Out of 100 sick people, the model finds 96, the physician 99. False alarms: **293 against 4**.

**Caveat.** Here the physician worked **with the model's cue**; there is no measurement of "the physician without the cue" in this study.

## Speaker notes

Moscow, sixty-seven clinics, April 2022 to December 2024: 3,409 head CT scans, intracranial hemorrhage in 1,101 people. Three registered services reading the scan on their own were compared against the physician's finding. The cost of both errors here is of a different order than on the preventive stream, and everything else follows from it.

Intracranial hemorrhage is a condition where it comes down to minutes: how fast it is seen on the scan decides whether the person survives to treatment or not. A miss here is not a stage delayed by a year — it is death or irreversible damage. But a false alarm is not free here either: it is a deployed emergency crew and an operating-room slot taken up for nothing. And the key thing is that there is no time, on this path, to calmly check an alarm.

The classical regime: a radiologist reads the head scan himself. In this study he is taken as the comparison point too — but in a particular form, and that form has to be named before the numbers. The physician had access to the model's output as an assistive cue. There is no separate measurement of "the physician without the cue" in this study. So this study does not measure what the cue itself contributed; it measures something else — the model alone against the physician with a cue.

The share of sick people in the sample is thirty-two out of a hundred, and it has to be kept in mind: on a stream where hemorrhage occurs in a handful out of a hundred, these same shares would produce a completely different picture on the physician's desk.

The physician with the cue outperformed the model on every metric, and the gap in the shares looks moderate. Out of a hundred sick people, he finds ninety-nine against ninety-six. Out of a hundred healthy people, he does not alarm ninety-nine point eight against eighty-seven point four. This second pair is the entire story, but it does not read in shares — it reads in cases. On the same sample, the model raised 293 false alarms, the physician four. Seventy-three times more.

The main observation of this breakdown, and the reason it exists at all: the misses did not overlap in a single case. All forty-five hemorrhages the model missed, the physician found. All twelve the physician missed, the model found. Agreement between the two methods: eighty-nine point six percent.

What moved here. Autonomous operation is not considered at all: 293 false alarms out of 3,409 studies mean that every twelfth scan would go down the emergency path for nothing, and on the emergency path a false call costs more than a wait in line. The complementarity of the misses moves the model from first reader to second — its value is not that it reads better, but that it errs in different places. And for that, the work of sorting through 293 false alarms arrives — done by the very physician the model is supposed to help.

The pair that closes this breakdown. Delivered: twelve hemorrhages the physician missed and the model caught. Required: two hundred eighty-nine extra reviews on the same 3,409 studies.

And the lesson these two domestic breakdowns stand next to each other for. The task is the same — reading an image with a trained model. The city is the same, the circle of products is the same, the oversight is the same. The conclusion is the opposite: there, the model was sent to work without a human, and what that cost was measured; here, the authors state directly that the model's place is second reader, not first. What tells these two cases apart is not the quality of the models, but the cost of a false alarm and whether there is time. On the preventive stream, a false alarm costs one follow-up exam, and there is time. On the emergency path, it costs a deployed crew, and there is no time. From the same property of the model — raising alarms generously — one task gets permission to work without a human, and the other gets a ban on it.

And one last thing this breakdown adds to the section: it is the only one of the five where the reading itself failed. Not the setting, not the composition of the training set, not the definition of the target — the reading.

**Sources.** [Khoruzhaya et al., *Journal of Clinical Medicine* 2025;14(16):5700](https://doi.org/10.3390/jcm14165700)
