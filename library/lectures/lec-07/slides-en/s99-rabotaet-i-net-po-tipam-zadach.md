---
# СЛИТ ИЗ ДВУХ КАДРОВ, Этап B прожарки сторителлинга (#293, П5). Было `s99` («Что работает и
# что не работает — по типам задач») и `s101` («Итог карты: четыре ячейки заняты пятью
# разделами»). Два свода отвечали на один вопрос с двух сторон и стояли встык: `s101` рисовал
# сетку и считал занятость клеток, `s99` разрезал тот же материал по типам задач. Строки у них
# совпадали — тип задачи, — и потому слияние не экономия места, а снятие удвоения: один разрез,
# одна таблица, один счёт.
# ФОРМА СМЕНИЛАСЬ С ДВУХ СТОЛБЦОВ НА ТАБЛИЦУ, и это решение, а не вкус. Два столбца у `s99`
#   стояли по канону («два столбца — только под противопоставление»), но модальность в них не
#   называлась вовсе, и после слияния счёт «четыре клетки из двенадцати» нечем было проверить
#   глазами. В таблице модальность стоит в той же строке, что и разрез: четыре строки задач на
#   три вида данных — двенадцать клеток, названа в каждой строке ровно одна, итого четыре.
#   Счёт проверяется с кадра, а не принимается на слово.
# ТАБЛИЦА ЧЕТЫРЕХСТРОЧНАЯ ПРИ ПРЕДЕЛЕ СЕМИ (П6-б п.4 прожарки: «не больше 6–7 строк на кадр»).
#   Пятая строка — измерение прибором — в таблицу НЕ ставится намеренно: она не входит в окно
#   двенадцати клеток, и строкой таблицы она сломала бы арифметику «четыре на три». Названа
#   отдельной строкой тела вместе с двумя другими местами вне окна.
# ЧТО УШЛО В ЗАМЕТКИ ЦЕЛИКОМ: имена разборов внутри каждой занятой клетки (пять разделов в
#   четырёх клетках), четыре процедуры удержания и правило «чем позже проверка, тем дольше живёт
#   ошибка», пятая строка без процедуры ни в одной юрисдикции, разбор каждой из шести задач
#   числами. Ни одно число с видимого слоя не потеряно: числа каждой строки стоят на кадрах
#   своих разборов, здесь их и не было.
# СЧЁТЧИКИ ПРОВЕРЕНЫ ОТДЕЛЬНЫМ ПРОХОДОМ (правило «структурный разрез → сплошной проход по
#   счётчикам»): «шестой тип» прежнего `s99` с кадра снят — шестёрка держалась перечнем из пяти
#   строк двух столбцов плюс один, а в таблице строк четыре, и слово «шестой» перестало
#   сходиться с нарисованным. Вместо счёта типов на кадре стоит счёт клеток, который считается
#   глазами: 4 из 12, вне окна ещё три.
id: s99
local_id: s8-02a
section: "6. Итоги"
type: summary
title: "The map of tasks and data types: four cells out of twelve, and what works in them"
assertion: "Четыре строки задач на три вида данных дают двенадцать клеток; за пять разделов названы четыре, в остальные восемь не зашёл никто, и вне окна лежат ещё три места — речь на приёме, видео и сигнал прибора, где обученной модели нет вовсе; у каждой занятой клетки граница «работает / не работает» одна и та же, независимо от стадии, и ни одна строка правой графы не про качество модели"
source: "—"
media: ""
media_needed: "иллюстрация не нужна: таблица задач и видов данных и есть предмет кадра, и рядом с ней фотография отнимает скорость чтения"
media_note: "строки таблицы — типы задач, и обе графы разреза стоят в той же строке, что модальность: иначе счёт клеток не проверяется глазами"
pol_slov: 190   # ОБЪЯВЛЕН ПОД СЛИТЫЙ СОСТАВ (#293, Этап B): 186 слов замером по собранному PDF + запас 4. Два прежних пола, 182 у `s99` и 137 у `s101`, в сумме 319 — слияние срезало с видимого слоя около сорока процентов: имена разборов внутри клеток, четыре процедуры удержания и разбор каждой задачи числами ушли в заметки целиком. Пол объявлен под три слагаемых, и каждое стоит на кадре потому, что без него кадр перестаёт быть сводом: (1) четыре строки таблицы с модальностью — без модальности счёт клеток не проверяется; (2) обе графы разреза в той же строке — вынос любой из них в заметки оставил бы половину противопоставления, запрещённую §3 строения раздела; (3) строка мест вне окна — честный пробел, названный содержательно, а не оговоркой (§5.17). Веса и кегля здесь нет нарочно: их печатает прогон на любой момент, а записанные прозой они устаревают молча
opyt_net: "свод: собирает уже предъявленное пятью разделами, своего замера не ставит — числа каждой строки стоят на кадрах своих разборов, занятость клеток считается по составу деки"
timing_min: 1.5
in_bucket: true
method_steps: ["свод"]
form: ["сетка"]
vfy: false
status: собран
---

## Visible slide text

**Four rows of tasks against three data types — twelve cells. Four are named; nobody went into the remaining eight across five sections.**

| task, and where it came up | what works | what doesn't |
|---|---|---|
| **classification** — image: screening, diagnostics | a standardized scan, fitness-for-analysis settled before the model | the subgroup underrepresented in the training set: it pays |
| **recognition** — image: screening, diagnostics, diagnosis | a flow filter: who gets read twice | grounds to drop a reading: savings from what goes unread |
| **retrieval and generation** — text: screening, diagnosis, documentation | a draft ready by the end of the visit | more complete than a human: the same person writes it, but the reader pays |
| **forecasting** — structured data: diagnostics, diagnosis | a signal alongside the scale | the decision: the target variable sets the aim, and a document sets the threshold |

**Three more spots lie outside the window.** Speech at the visit: typing by voice works; word endings and other people's speech do not. Video: highlighting during the procedure, with the spot staying with the person. Instrument signal: there is no trained model at all, yet there is bias.

**The right column, in not one row, is about the quality of the model** — it is about the fitness of the input, the composition of the data, the target set for training, and the assigned threshold. **Qualification occupies nothing in the window:** its assistant works on video.

## Speaker notes

Four rows of tasks against three data types give twelve cells. Across five sections, four are named; nobody went into the remaining eight. The material is the same as in the five stage conclusions, cut the other way — by task type. One task type runs through several stages: image recognition came up in screening, in instrumental diagnostics, and in diagnosis; forecasting on structured data came up in diagnostics and diagnosis. By stage, each one seems to have its own story; by type, you can see that the boundary between "works" and "doesn't" for a given task type is the same everywhere.

Twelve cells are a window into the course's full forty-two-cell grid, taken exactly to fit what the lecture examines in the clinic: retrieval and generation are combined into one row, there is no planning, just as there is no audio, video, code, or mixed data. The count can be checked right off the screen: each row names exactly one data type, there are four rows — so four cells are occupied, eight are empty.

The eight empty cells carry just as much content as the four occupied ones. The lecture has no classification or recognition on text at all; no retrieval or generation on images or structured data; no forecasting on text or images. There, either there is no tool of that class in the clinic, or there is one, but nobody holds the cost of its error in place with a procedure — and with no procedure, there's nothing to examine. An honest empty cell is better than a made-up occupied one.

The tools of five sections fit into four cells. Classification on images is occupied twice: by screening, which images the fundus, and by instrumental diagnostics, which assesses a skin lesion. Recognition on images, three times: screening with mammograms, diagnostics with triage of the flow in X-ray and CT, diagnosis with gaze tracking over the same mammogram. Retrieval and generation on text, three times: pre-visit intake triage, a language model reading case descriptions, and recording the visit with the discharge summary. Forecasting on structured data, twice: selection into the high-attention program and the early-warning sepsis model. The class of model does not distinguish the sections; what distinguishes them is the cost of a miss and the procedure built around the person.

Now through the table's rows, with numbers. Recognition on images works as a flow filter: it is capable of deciding what to flag and who gets a second read — the Swedish program measured this by lottery on more than a hundred thousand women, the Moscow triage on half a million scans. What it does not give is grounds to drop a reading, and that is visible in the Moscow case with the arithmetic right on the slide: one scan became more expensive for a human reader, and the thirty-three million in savings came entirely from that same fifty-five scans out of a hundred that nobody reads at all. The savings come from what goes unread, not from accuracy.

Classification on images works where the scan is standardized and the question of its fitness for analysis is settled before the model. Fundus imaging at the visit showed this: turnout rose from 22 out of 100 to 100. But right there stands the boundary too — in the field, a person decides a scan's fitness with no rule, and nobody watches the reject stream. And the second case of the same type, skin lesions, shows a second boundary: the average over the validation set stayed decent, and the subgroup underrepresented in the training set pays.

Retrieval and generation on text works as a draft ready by the end of the visit, and it did remove one real step — the document's structure no longer has to be held in your head while a living person is there. It does not write more completely than a human: in the blinded comparison of a hundred hospitalizations, the machine-written discharge summary came out shorter and more coherent, but less complete. And the cost shifts here: the same person writes it, but the reader pays — the one who opens the document a month later, having never seen the patient.

Forecasting on structured data works as a signal alongside the scale, not in place of it. A comparison against zero gives the wrong picture here: the scale was confirmed by 8 alerts out of 100, the model by 12, and it never left that band. As a decision, forecasting does not work, and the reason is an engineering one: the target is set by the variable it was trained on, and the threshold is set by a document. Selection into the high-attention program is the clearest case: the model was trained to predict cost, and the decision made was about illness. And separately, about why this particular cell is populated: structured data there is already gathered by someone before the model ever gets involved — orders written up, bedside vitals, treatment bills. The model arrives where the numbers are already sitting, and this observation transfers outside medicine almost without edits.

Three spots lie outside the window, and without them it reads as an oversight in selection. Speech recognition — two domestic breakdowns from the documentation section: the visit note that a voice assistant fills out, and voice dictation of the radiology report. It works as typing by voice instead of by keyboard, and forty years before this, the same technology lost to the keyboard: in 1981, voice input took four times as long and produced twelve errors against zero. It does not work — on word endings and on other people's speech in the room, when more than the physician ends up in the recording; and nobody measured time here — the sixty-two-plus percent is the share of physicians who think it got faster, not a measured time. Recognition on video — real-time highlighting for those who decide: the Polish trial and the domestic ArtInCol. And a measurement with an instrument signal, where there is no trained model at all: bias in a blood-oxygen-saturation sensor arrives before any model, and the system that takes its reading as input inherits the bias silently.

The qualification section is absent from the window for the same reason: the assistant that boxes a finding during the procedure works on video in real time, and video is not among the twelve cells shown — it has a place in the full grid, just outside the edge of this window. What matters here is that the one section all evening that measured the person, not the work, landed on a data type the window doesn't contain.

The third layer of this table is what, in each cell, holds the cost of error in place. The procedures differ across the four cells, and none of them match. For image recognition, what holds it in place is double reading, arbitration on disagreement, and recalculating the true-alarm rate against local prevalence. For image classification, it's the fitness of the input, settled before the model: a system that itself rejects an unfit scan, and a one-year repeat visit for those who came back clean. For forecasting, it's a review of false alarms, counted as working time, and a pre-approved plan for changes to the model. For text, it's physician review and signature, case review, and the stated boundaries of use. From this comes a rule that reads straight off the order of these rows: the later a check sits in the procedure, the longer an error lives. On images, it gets caught within the shift; on text, at the signature; on forecasting, at the next cut of data handed to the regulator. And wear on the hand gets caught nowhere: the review of authorization across three countries showed that there is no procedure anywhere that measures a physician without the assistant — not in the UK, where the work result counts toward authorization as a number, not in the US, where the same indicator exists and is declared off-limits as authorization, and not in Russia, where hours of study are counted. You cannot write "re-certification" in here — no such procedure exists in any jurisdiction.

And the conclusion that transfers outside medicine almost without edits. Look at the whole right column: not one of its rows is about the quality of the model. Fitness of the input, composition of the training data, the target set for training, the assigned threshold, who reads the document afterward — this is all engineering work built around the model, and it is exactly this work that decides whether the deployment succeeds or not. The quality of the model is not mentioned in this list, not once.
