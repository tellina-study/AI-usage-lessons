---
# СХЕМА ДОБАВЛЕНА (п. 11 наряда, §11.3: «схема обязательна у каждого кадра типа `case`»).
# Замер прожарки: схема нашлась у 5 кадров `case` из 12 в разделе, и не было её ровно у семи
# самых тяжёлых по тексту — то есть там, где она нужнее всего. §10.3: схема решения несёт
# инженерное содержание, текст — пояснение к ней, не замена; поэтому вместе со схемой из тела
# СНЯТО то, что она теперь показывает сама (п. 12 наряда, плотность: чинить схему и объём
# вместе, а не по очереди).
# СВЁРТКА (#229): кадр собран из s41 и s43 (второй файл в slides/_snyato/). Сведён в одну форму §5.13 сессией содержания: обе половины мерят ОДНУ величину — пропущенные раки, — и расходятся порядком предъявления подсказки.
id: s41
local_id: s3-15
section: "3. Постановка диагноза"
type: case
title: "Example 1: eye-tracking — with a false suggestion and with a correct one"
assertion: "Один и тот же читатель на тех же случаях пропускает вдвое больше раков там, где подсказка молчала, и находит больше там, где разметку запрашивал сам: сужение зрительного поиска измерено в обоих опытах, а знак ему задают правота подсказки и порядок её предъявления — при этом модель одна обошла пару читателя с моделью, и авторы говорят это сами"
source: "Taib et al., Radiology 2026 — https://doi.org/10.1148/radiol.252590 · Gommers et al., Radiology 2025 — https://doi.org/10.1148/radiol.243688"
media: ""
media_needed: "карта фиксаций взгляда из первоисточника — добыть, права проверить (журнал не открытого доступа); запасной вариант — собственная схема двух карт поиска. Ось площадей держит экран сама, поэтому иллюстрация теперь желательна, а не обязательна"
media_note: "иллюстрация не добыта"
blocks:
  - {label: "Missed cancers with a false suggestion: without → with", value: "29 → 61 out of a hundred present", note: "14 cases where the suggestion was silent; significant. The cost is later, worse treatment", key: true}
  - {label: "Missed cancers when readers requested the markup themselves: without → with", value: "165 → 115 out of 900 readings", note: "75 cancer cases per condition; a 5.6-point gain with an interval of −0.3…+11.4 — not significant. Reading time didn't change", key: true}
pol_slov: 200   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 196 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
# СКАЗАННОЕ ДВАЖДЫ, снято: два блока «Как читали» (устройство обоих опытов стояло прозой порознь) сведены в одну экспозицию первой строкой; «Семьдесят один из ста — это двадцать девять пропущенных раков» — величина стояла и плашкой, и прозой, осталась плашкой и в человеческой единице; «Сужение поиска само по себе ни польза, ни вред. Знак задаёт правота подсказки» и формула зеркала говорили одно — осталась формула; «Второй классический режим — второе человеческое чтение» снято, оно измерено на s47 той же единицей; блок «Цена обеих ошибок» прозой снят по п. 36 владельца («цена очевидна — убрать») — обе цены стоят теперь ПОДПИСЯМИ своих плашек, у самого числа, а не вторым разом в теле; «но модель одна выше пары» снято как пересказ соседнего «0,97 · модель одна 0,99».
# ЧЕМ ЗАНЯТЫ СЛОВА, что встало взамен: порядок предъявления как единственное расхождение двух опытов (24 слова — без него противоположные знаки слипаются в один опыт, §Ж2 реестра); три площади с 0,99 модели одной и интервалом РАЗНИЦЫ +0,03 (0,02–0,05) вместо двух перекрывающихся интервалов самих площадей (27 слов, §Ж1 и §Ж3); имя изделия второй работы Transpara 2.1.0, ScreenPoint Medical (5 слов, §Ж4 — раздел норму имени держит, s43 из неё выпадала); фокусировка и время по заказу владельца «с и без — точность, время, фокусировка» (19); противовес к интересам «данные опыта в её обучении не использовались» (7 слов, §Ж5 — обе половины или ни одной).
# ЦЕНА, названная числом (замер по собранному PDF, не по файлу): шесть плашек заменены двумя, тело поднялось с 8,5 до 15,0 пт, оба блокирующих ушли, слов 256 → 194. Это единственный кадр полосы, который стал ЛЕГЧЕ и по весу: на остальных вес вырос, потому что на них встало заказанное владельцем и найденное фактчеком.
# В ЗАМЕТКИ, не на кадр: зеркало внутри первой работы (специфичность 21 → 39, ложных вызовов 61 вместо 79 из ста здоровых) — на кадре уже стоит зеркало между работами, и два зеркала рядом читаются как одно.
scheme:
  caption: "The two studies diverge by the order in which the suggestion was presented"
  arrows: true
  rows:
    - {label: "The marker shown with the image", steps: ["image with the marker", "reading", "assessment"]}
    - {label: "Markup on request", steps: ["image", "reading", "request the markup", "assessment"]}
timing_min: 1.9
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало"]
form: ["сетка", "форма 4а", "форма 7", "[VFY]"]
vfy: true
status: собран
---

## Visible slide text

**Two measurements of one quantity.** 10 radiologists read 60 mammograms twice: on their own, and with a suggestion deliberately wrong in both directions. 12 radiologists in a different program: 150 exams, also read twice, with an approved system.

**A different order of presentation — the opposite sign.**

**How it's built.** Input — a mammogram, output — a suspicion score for the region. The second study names the product: **Transpara 2.1.0, ScreenPoint Medical.** **Focus:** the area of the image scanned fell from 11.1 to 9.5 out of a hundred, with longer dwell time in the right spot — 4.4 → 5.4 seconds.

**This narrowing is the second of the six distortions from the opening of the evening:** where the model stays silent, the gaze doesn't linger, and the model's miss becomes the reader's miss.

## Speaker notes

Ten radiologists read the same set of sixty mammograms twice: first on their own, then six weeks later with a suggestion that was deliberately wrong in both directions. Both the result and the eye movements were measured, so here you can see what mechanism changed the result. On cases where the suggestion stayed silent, missed cancers rose to 61 out of a hundred against 29 for the same readers — twice as many. That's what narrowing looks like, the second of the six distortions presented at the opening of the evening.

The set is enriched with cancers to roughly half, and that has to be kept in mind: in a live program, cancer occurs in a handful per thousand.

The baseline is the same reader's median sensitivity on the same cases without a suggestion: 71 out of a hundred, meaning 29 missed cancers out of a hundred present. There were fourteen silent cases, and the difference on them is robust. The cost of this figure isn't abstract: a missed cancer means later, worse treatment.

The second half of the same measurement shows the sign flipping within a single study: on the fourteen cases with a false-positive suggestion, the reader's specificity rose — from 21 to 39 out of a hundred. In other words, a wrong suggestion isn't simply harmful; the sign of the effect is set by which direction it was wrong in.

Exactly how this happened was measured, not guessed. On lesions the model missed, the reader's gaze lingered noticeably less often. The false suggestion narrowed the visual search. There was no verbal persuasion involved: no one argued to the reader that the lesion wasn't there — their eye simply stopped less often where no marker had been placed. And that's the most uncomfortable part of this case study: the effect sits below the level at which a person can control themselves by force of will.

The design of the second study, and why it sits on the same slide. Twelve radiologists from a screening program across ten institutions, experience ranging from 4 to 32 years with a median of 12. One hundred fifty exams, also read twice, but with an approved system — Transpara 2.1.0 made by ScreenPoint Medical. Here the result is the opposite: missed cancers went down, 115 out of 900 readings versus 165. A 5.6-point gain with an interval from minus 0.3 to plus 11.4 — not significant; reading time didn't change.

The area under the curve rose from 0.93 to 0.97: plus 0.03, with an interval from 0.02 to 0.05, and it rose for all twelve readers without exception.

Separately — a figure that sits on the lecture's own axis. The model alone scored 0.99, with an interval from 0.97 to 1.00, meaning higher than the pair of "reader with the system." The authors say this outright, and we won't hide it: in this study, the person next to the model didn't improve it — they made it worse.

Focus was measured here too: the share of the image's area covered by gaze fixations fell from 11.1 to 9.5 out of a hundred, while dwell time on the lesion area rose from 4.4 to 5.4 seconds. The same narrowing of the search as in the first study — but with a different outcome.

Why the signs diverged, and this is the only substantive explanation available. In the first study, the marker is displayed together with the image — that is, before the reader has formed their own opinion. In the second, the reader requests the markup themselves, after already having looked. The order of presentation isn't a matter of formatting — it's a controllable parameter with a measured price.

On the vocabulary of forms. The load at the same spot went down: same place, same performer, less work. But the sign of this form is set by whether the suggestion was right — with a false suggestion, the same form turns out to be a cost rather than a gain, because the model's miss becomes the reader's miss.

The strength of evidence is named alongside the figures. The first study — a reader compared against themselves — is strong in mechanism, medium in reader sample size: ten of them, and no generalization to the whole profession follows from it. The second — twelve readers from ten institutions, so wider in locations, but also not population-level. Both sets are enriched with cancers; ScreenPoint Medical provided the tested system, and that's disclosed in the publication itself.

The rung of involvement in the first study is "looks second": the suggestion appears on screen together with the case, that is, before the reader has formed their own opinion. In the second, they look first and request the suggestion themselves. These are different rungs, and it's them — not the model — that drive the results apart.

A short question for the room, and it's a prediction based on this very measurement. The reader's gaze was measured twice: on their own and with a suggestion. The area of the image scanned with a suggestion fell from eleven and one tenth to nine and a half out of a hundred, while in the marked spot the gaze lingered longer — from four and four tenths to five and four tenths seconds. I ask: what happened, then, to the cases where the suggestion stayed SILENT — did misses stay the same, go down, or go up? And by how much? I ask you to name it before I show it. The figure sits a line below on this same slide, and it's worth covering it with your hand for a second: the prediction "the same" is the one heard most often in the room, and missed cancers there became twice as many.

**Sources.** [Taib A., Partridge G., Phillips P., Chen Y. et al., Automation Bias in Action: Eye Tracking of Humans Reading Screening Mammograms with and without AI Prompts, 2024](https://doi.org/10.1016/j.acra.2024.03.013) · [Gommers J. J. J., Sechopoulos I., Broeders M. J. M. et al., Radiologists' Performance and Visual Search Patterns When Reading Screening Mammograms with Artificial Intelligence Support, 2025](https://doi.org/10.1016/j.jacr.2024.10.021)
