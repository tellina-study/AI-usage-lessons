---
# «ТОЧНОСТЬ 94 ПРОЦЕНТА» СТОИТ БЕЗ БАЗЫ НАМЕРЕННО, и это не пропуск сторожа базы
# (`CLAUDE.md` § Baseline / Counterfactual Mandate). Это вопрос залу, и его предмет — именно
# отсутствие базы: число названо так, как его называют в рекламных материалах, а следующей
# строкой спрашивается, на какой группе оно посчитано. Дописать сюда знаменатель значило бы
# ответить за зал и снять вопрос. Проход по базам 2026-10-19 это место проверил и оставил.
# ПЕРЕЧЕНЬ СПОСОБОВ ВЕРНУЛСЯ НА КАДР (п. 14 наряда). `CLAUDE.md` § «Строение раздела
# отраслевой лекции», шаг 1(в), дословно: «какими способами эти данные получают — приём,
# удалённое исследование, разбор документов; перечень здесь обязателен и СТОИТ НА КАДРЕ».
# Прежняя редакция держала его голосом, и заметки это прямо объявляли: «на экране их перечня
# нет нарочно — перечень читается вслух». Четыре способа названы по главе (§ Раздел 2, вводка),
# у каждого — то свойство, из-за которого его нельзя заменить соседним: прибор по человеку ·
# проба без человека · протокол нагрузки в условиях измерения · снимающий и читающий разделены.
# ЧЕТВЁРТЫЙ СПОСОБ НЕСЁТ РАЗДЕЛ ДАЛЬШЕ: именно из разделения снимающего и читающего §2.4
# выводит, почему негодный снимок доходит до чтения незамеченным, — и на этом стоит `s26`.
# СТРОКА ЗАМЕТОК ПОПРАВЛЕНА ТЕМ ЖЕ КРУГОМ. Решение «перечня нет нарочно» владелец отменил
# ещё прошлым кругом (см. ниже, пп. 21-22: шесть действий вынесены схемой), а заметки
# продолжали объявлять залу отменённое — тот самый сторож, который возвращает снятое.
# СВЁРТКА (#229): кадр собран из s22a и s23 (второй файл в slides/_snyato/). Сведён сессией содержания: шесть действий стадии вынесены на кадр схемой (п. 22 владельца — «какие шесть действий?»), и схема же отвечает на п. 21 — на каких действиях стоит модель и зачем. Решение s23 «перечня на экране нет нарочно» этим ОТМЕНЕНО владельцем.
id: s22a
local_id: s2-01a
section: "2. Инструментальная и лабораторная диагностика"
type: norm
title: "The evidence: six actions of the stage, and the two the model took over"
assertion: "Стадия состоит из шести действий — назначить порог, снять измерение, решить, годно ли оно, прочесть и назвать две доли, пересчитать их под свою распространённость, сообщить результат тому, кто решает; без обученной модели все шесть делает человек по записанному правилу, модель заняла два — чтение измерения и сообщение результата, то есть вынесение первичного заключения, — и это не самые трудные два из шести"
source: "Roberts et al., Nature Machine Intelligence 2021 — https://doi.org/10.1038/s42256-021-00307-0"
media: "rework/deck/assets/s23-laborant-za-pultom-reshaet-o-godnosti.jpg"
media_needed: ""
media_note: "иллюстрация не поставлена: настоящий кабинет стоит на дивайдере раздела выше и на s26, где техник у прибора и есть предмет кадра"
scheme:
  caption: "Six actions of the stage; the model took over two"
  arrows: true
  rows:
    - {label: "Human — four", steps: ["set the threshold", "take the measurement", "decide if it's usable", "recompute for its own group"]}
    - {label: "Model — two", steps: ["read the measurement", "report the result"], arrows: false}
vizforma: "ряды"
pol_slov: 138    # О20 (#229): объявлен ВПЕРВЫЕ после свёртки s22a+s23, по собранному PDF. Склейка дала 155 слов и два блокирующих при теле 8,5 пт; теперь 138 слов, тело 12,5 пт, блокирующих нет. Проза срезана с 93 слов до 88, а вес держит схема шести действий — она и есть заказ владельца.
# ЧТО ВСТАЛО по пп. 21-22: шесть действий стадии вынесены на кадр СХЕМОЙ — владелец спросил «какие шесть действий?», и прежняя редакция s23 отвечала на это только голосом («на экране их перечня нет нарочно»). Решение отменено владельцем. Схема же отвечает и на п. 21 «на каких этапах и зачем ИИ»: два ряда, человек четыре действия, модель два. Шестью шагами в один ряд их ставить нельзя — §5.12 держит предел в четыре шага, и разбивка по исполнителю как раз и есть содержание кадра.
# ЗАЧЕМ ЗДЕСЬ МОДЕЛЬ — ответ на возражение владельца «если тут тупо измеряется, то ИИ вообще ни при чём»: измеряет прибор, а модель выносит ПЕРВИЧНОЕ ЗАКЛЮЧЕНИЕ по измеренному, и от него зависит, что обследуют дальше. Это ровно то, что владелец и назвал осмысленным («логично, если выносится первичное мнение / определяется ход обследования»), и прежде на кадре этого не было ни словом.
# СКАЗАННОЕ ДВАЖДЫ, снято: «Техник ставит человека к прибору, снимает, смотрит на экран и решает: читать или переснимать» — те же три действия теперь стоят шагами схемы, и отдельный кадр s26 разбирает это решение целиком; «Решение стадии: что измерено и с какой точностью» и «Почему после отбора» ушли в заметки — первое пересказывает схему, второе относится к порядку разделов, а не к стадии; «У прибора стоит человек: лаборант, техник, медсестра» слито в первую строку.
# ЖАРГОН СНЯТ по п. 2: «рабочая точка» заменена на «порог» — и в шагах схемы, и в теле. Владелец запретил это слово на видимом слое прямо.
# #293 Этап D: остатки термина сведены по ВСЕЙ деке к «порогу срабатывания»; пояснение строкой стоит на s24, где термин появляется впервые.
# ПЛАШКИ СНЯТЫ, упоминание ОСТАЛОСЬ: две плашки обзора Roberts стоили 2,5 пт кегля тела (замерено: с ними 8,5 пт и два блокирующих, без них чисто) — само упоминание с обоими своими числами и наблюдением переехало строкой тела, по §5.15 («список упоминаний несёт наблюдение, а не имя»). Оговорка «это вывод о качестве исследовательских работ, про внедрённые системы он не говорит ничего» осталась в заметках. 1.1
timing_min: 1.1
in_bucket: false
method_steps: ["заземление", "упоминание"]
form: ["вопрос залу"]
vfy: false
status: собран
---

## Visible slide text

**Four ways to take a measurement, and none can substitute for another:**

- **Instrumental examination** — the device works directly on the person
- **Laboratory analysis** — the person is no longer present, a retake on the spot is impossible
- **Functional test** — a load protocol is part of the measurement conditions
- **Remote examination** — the reader never saw the patient

**The model took over two of the six actions, and not the hardest two.** It does not set the threshold against the cost of an error, cannot order a retake, and leaves input gradability to a human.

**You're told "94 percent accuracy." On what group was it computed?**

## Speaker notes

This stage is called instrumental and laboratory diagnostics, and that is the name the industry itself uses for it. The person is already in view by the time it starts: the previous stage decided that he gets examined. Now measurements are taken on him — an image is made, a sample is taken, a device is connected, a measurement is recorded in the chart.

The data here is of a different kind than at selection. There it was year of birth and an interval; here it is an image, a device signal, a reading from blood, urine, tissue, or a culture. And two questions get decided on this data, not one. The first is what the measured values mean. The second, which never appears in marketing materials, is whether these values are even fit to be read at all.

There are four ways to obtain such data, and all four need naming, because the breakdowns ahead will split across them. Instrumental examination gives values taken by a device: a plain film, a CT scan, an endoscopy. Laboratory analysis gives readings from blood, urine, tissue, a culture — and some of these carry their own turnaround time that will not go away: a sputum culture itself takes three weeks. A functional test takes values under load, meaning it adds to the measurement the condition under which it was taken. A remote examination is built so that the person is imaged in one place and a specialist reads the image in another; this is not exotic — it is what radiology in areas with no local radiologist runs on.

The decision this stage makes reads as: what has been measured about the person, and with what accuracy. Interpretation follows after that — reading what was measured and issuing a finding on it, and that is the work of the next stage.

Now for why this stage comes after selection and not before it. Measurement accuracy is described by two shares, and they are computed on different groups: sensitivity takes only the sick, specificity only the healthy. The two are named as a pair and always for one threshold, and the protocol chooses the threshold against the cost of the outcome — chosen before the developer ever started work. What the physician at the visit actually gets is a third share, the share of alarms that are correct among all raised, and it depends on how many sick people are in the examined group. That group was assembled by the previous stage. So the order is forced: the denominator comes from selection, and before selection there is no readable meaning to the measurement at all. What this costs is counted in people on the next slide.

And how this decision is made without any model at all — by the classical regimes, by name. Quality control of the study: a human looks at the measurement obtained and decides whether it can be read or needs a retake, and the rule he decides by is written in the room's own instructions, not in the device. A specialist reading the measurement at a named trigger threshold: the threshold for declaring "sick" is set by protocol, and the reader works at that threshold without setting his own. The next slide is given entirely to the first of these — and it is given to it because it, and not the reading itself, is where the third of this section's five breakdowns, the Thai one, failed.

And the same field with the model, named before the breakdowns. Of the six actions, the trained model took over two: reading the measurement in full, without a specialist, and reporting the result — where instead of a value, a single score and a threshold-based cutoff land on the table. It does not set the threshold, cannot order a retake, leaves input gradability to a person without specialized training, and recomputing for its own prevalence is left to whoever applies it. It does add one step: a repeat visit for anyone whose measurement failed quality. Its benefit here is consistency: the ten-thousandth frame reads the same as the first.

A systematic review of work on COVID-19 pneumonia selected sixty-two out of two thousand two hundred twelve publications and found not one of them fit for clinical use. Every one of them computed the shares; almost none named the group they were computed on. The caveat is mandatory: this is a finding about the quality of research papers, and it says nothing about deployed systems. This mention does not become a breakdown — it has no numeric cost for either error, and no count against a classical regime.

And a question for the room, worth asking right here rather than at the end — it is also a one-move game. You're told "94 percent accuracy." I take one and the same system with one and the same trigger threshold and apply it to two groups of ten thousand people each, differing ONLY in the share of sick people among them. Not one line changes inside the system. The question: how far apart will the share of correct alarms be between these two groups? By how much — by half, by double, by tenfold? I'll ask for a number out loud, or one word in the chat. The next slide works this out, and the gap there is nearly tenfold; the room usually guesses one and a half to two. The question is asked right here, before the breakdown: a number the room names itself, it remembers and checks against later — a number it is simply handed does not stick the same way.

And a last thing worth saying before the breakdowns. The two actions the model took over are not the hardest of the six. The hard ones stayed with people: setting the threshold against the cost of an error, and deciding whether a measurement is usable. This is the overarching plot of the whole lecture, and in this section it shows most clearly of all.

**Sources.** [Roberts et al., Nature Machine Intelligence 2021](https://doi.org/10.1038/s42256-021-00307-0)
