---
# ВСТАВКА (issue #270, доработка инженерной глубины разбора по §2
# obzor-stran-i-glubina-razbora.md). Продолжение разбора s15 («Шведский
# скрининг с моделью: кому достаётся второе чтение»), не новый кейс —
# отмечено полем `razbor_part`. local_id СОЗНАТЕЛЬНО не `s1-04a`: этот
# суффикс в плане не свободен по смыслу, хоть файла под ним и нет —
# `plans/block-01-otbor.md` прямо резервирует `s1-04a` за ДРУГИМ, пока не
# внесённым содержанием («охват публикуют, устройство работы — нет»,
# отечественная платформа лучевой диагностики, 0,7 минуты, «единственная
# правка состава, которую я прошу»). Это иной материал, чем здесь
# (британский арбитраж / асимметрия доверия / германские 0% и 56,7% /
# честный пробел обучения-дрейфа), и присвоение той же строки другому
# содержанию сломало бы этот документированный адрес — тот же ход, что
# применил `s16a` для `s1-07a`, занятого `_snyato/s17-arifmetika-kanala.md`.
# Взят следующий незанятый суффикс `s1-04b`. `id: s15a` — адрес показа
# (кадр встаёт сразу после `s15`, перед `s16`: сортировка имён файлов
# `s15-...` < `s15a-...` < `s16-...` даёт этот порядок сама), из другого
# пространства имён, коллизии с `local_id` не образует (см. комментарий
# `s16a` про `make_deck_yaml.py`).
id: s15a
local_id: s1-04b
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 1, the cost: arbitration and trust in a finding"
assertion: "Отдельное британское испытание (2 центра NHS Англии, 50 000 женщин) посчитало цену нового шага: доля чтений, уходящих на арбитраж, выросла с 3,9 до 9,4 процента в одном центре и с 11,3 до 13,8 в другом (+142 и +22 процента — разница протокола, не шума), а один разбор расхождения по времени равен примерно пяти первичным чтениям (48 секунд против 2 минут 12 секунд, 441 276 случаев, Норвегия); отдельное шведское испытание на 54 991 женщине измерило обратную сторону доверия — находка одного радиолога уходит в разбор вшестеро чаще находки одной модели (14,2 против 4,6 процента случаев), хотя точность подтверждения у модели выше в шесть с лишним раз (22 против 3,4 процента); германская программа заменила 0 процентов человеческих чтений против гипотетических 56,7 процента при другом устройстве работы (финансирование — производитель системы, Vara); ни для шведской, ни для германской модели источники не раскрывают обучающую выборку, частоту переобучения и мониторинг дрейфа"
source: "Warren et al., Nature Cancer 2026 — https://doi.org/10.1038/s43018-026-01128-z"
media: ""
media_needed: "иллюстрация не нужна структурно: кадр держат четыре плашки с измеренными величинами и их базами (пятый пункт, честный пробел, — утверждение без числа) и схема «без модели / с моделью», которая с issue #270 r3 заменила словесное объяснение устройства арбитража в теле"
media_note: "—"
razbor_part: "3 из 3 (продолжение s13→s15, единый кейс в трёх частях — шведская программа, не новый кейс): часть 1 (s13) — ①цена ошибки и ②классические режимы; часть 2 (s15) — начало ③«модель против них» (механика отбора: модель решает, кому достанется второе чтение), позиция в потоке (вход/выход, имена изделий); часть 3 — здесь, продолжение ③ (британский арбитраж, время), обратная сторона доверия находке, германские 0%/56,7% подробнее и честно названный ⑤пробел обучения/обновления/дрейфа"
blocks:
  - {label: "Readings sent to arbitration", value: "up two- and fivefold", note: "two centers, 50,000 women: 3.9→9.4 and 11.3→13.8", key: true}
  - {label: "One arbitration review, by time", value: "equals five readings", note: "48 seconds against 2 minutes 12; 441,276 cases"}
  - {label: "Finding confirmed: radiologist → model", value: "3 → 22 out of a hundred", note: "54,991 women"}
scheme:
  arrows: true
  rows:
    - {label: "Without a model", steps: ["Two radiologists read", "Disagreement on recall", "Arbitration: a third reader"]}
    - {label: "With a model", steps: [{text: "Radiologist and model read", ai: true}, "More disagreements", "Arbitration: longer, more often"]}
pol_slov: 138   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 134 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
  # ПРЕЖНЕЕ ОБЪЯВЛЕНИЕ (205), сохранено как провенанс; к нынешнему кадру его число не относится:
  # названы по случаю (маммографический скрининг, продолжение), добавлена схема «без
  # модели / с моделью» (2 ряда × 3 шага, явный `ai: true` на шаге «Радиолог и модель
  # читают» — в этой деке `ai_by_word=False`, золото угадыванием не ставится), тело
  # прозы сокращено с 161 до 91 слова (схема берёт на себя объяснение устройства
  # арбитража, которое раньше было в прозе). ЗАМЕР ПО СОБРАННОМУ PDF раздела 1
  # (render_sec.py 1, 2026-10-19, 14 страниц): 205 слов на этом кадре; медиана полосы
  # 156, максимум 259 (`s16`), блокирующих 0 (`build_lec07.py --only
  # s15,s15a,s16,s16a,s18,s18a,s18b`). Поле выставлено ПО ЗАМЕРУ, не по оценке.
  # ПРЕЖНЕЕ ЗНАЧЕНИЕ (issue #270, доработка инженерной глубины §2
  # obzor-stran-i-glubina-razbora.md). ЧЕТЫРЕ ПЛАШКИ несут числа с базами (доля
  # арбитража +142%/+22% по двум центрам NHS · время арбитража ≈5 чтений, 441 276
  # случаев · PPV 3,4%→22% на отзыве 14,2%/4,6% · германская замена 0% против
  # гипотетических 56,7%), тело — пять абзацев интерпретации БЕЗ повторения чисел
  # из плашек (снято как сказанное дважды — та же дисциплина, что `s16a` применил к
  # перечню шести исходов): устройство арбитража · доверие находке с явным разводом
  # от чувствительности модели на s15 (§5 проверки, «не чувствительность модели с
  # кадра перед этим — другое измерение, другая выборка») · германский 0%/56,7% ·
  # честно названный пробел обучения/обновления/дрейфа (контраст с § 1.6 глазного
  # дна). ПЕРВЫЙ ПРОХОД (216 слов видимого текста, все числа повторены в теле)
  # упёрся в блокирующее [кегль] (тело ужато до 0.66 рабочего кегля, 9,5 пт — ниже
  # пола 12 пт): плотность плашек + полный повтор чисел в абзацах вместе не
  # укладывались в бюджет кадра. Числа убраны из тела во второй проход, плашки
  # оставлены единственным держателем точных величин — после этого кадр собрался
  # без единого предупреждения [пол]/[запас]/[кегль]. ЗАМЕР ПО СОБРАННОМУ PDF
  # раздела 1 (render_sec.py 1, 2026-10-18, 12 страниц): 253 слова на этом кадре;
  # медиана полосы 183, максимум 286 (`s13a`), блокирующих 0
  # (`build_lec07.py --only s15,s15a`). Поле выставлено ПО ЗАМЕРУ, не по оценке.
timing_min: 1.0
in_bucket: true
method_steps: ["③порог/арбитраж и действие человека после модели", "④как это устроено (продолжение: асимметрия доверия, германское 0%/56,7%)", "⑤честный пробел (обучение/обновление/дрейф)"]
form: ["форма 3"]
vfy: true
status: собран
---

## Visible slide text

**A British trial counted the cost of disagreement, the fifth of the six distortions from the front door:** more disagreements, and each one is reviewed by a third reader.

**Trust runs backward.** A radiologist's finding gets re-checked three times as often as the model's finding, even though it's confirmed six times less often.

**Germany replaced none of the human readings;** 56.7 out of a hundred is a recalculation, not a measurement.

**Training, updates, and drift aren't disclosed by sources.**

## Speaker notes

A British trial, in two centers of England's National Health Service: 50,000 women, the model placed as second reader, and the cost of a new step was measured — arbitration, resolving a disagreement with a third reader. Disagreements with the model went up: 5,283 arbitrations against 3,449 without it, on the same 50,000 women. This is what disagreement, the fifth of the six distortions presented at the front door, looks like.

The Swedish trial measured the volume and accuracy of reading; what happens to arbitration itself, it didn't measure. That was done by the British study, and the two trials must not be confused: the model doesn't remove arbitration — it changes its composition.

Without the model, 3.9 percent of readings went to arbitration in one center and 11.3 percent in the other; with the model as second reader — 9.4 percent and 13.8 percent: a 142 percent rise in the first center and a 22 percent rise in the second. The spread between centers isn't measurement noise, it's a difference in protocol: the first center only sends disagreements on recall to arbitration, the second sends every case of recall at all, and that choice of protocol sets the final load no less than the model itself does. A separate Norwegian measurement, on 441,276 cases, counted this in seconds: one primary mammogram reading takes 48 seconds on average (median 25), and resolving one disagreement at arbitration takes 2 minutes 12 seconds (median 1 minute 55 seconds). One arbitration review, by time, equals about five primary readings. This is a direct answer to "what does the person do after the model": they don't glance at the suggestion in passing — they carry out an operation that costs, by time, as much as five ordinary ones.

This new step comes with a measured asymmetry of trust, and it flips the usual story on its head. A separate Swedish randomized, preregistered trial on 54,991 women (the ScreenTrustCAD study) put a finding from any of three independent reads — two radiologists and the model — through the same consensus-discussion step and measured what happens to a finding from each source. A finding from one radiologist alone went to consensus review in 14.2 percent of cases (263 of 1,858) with a confirmation accuracy of 3.4 percent (9 of 263); a finding from the model alone went to review in only 4.6 percent of cases (86 of 1,886) — but its confirmation accuracy was 22 percent (19 of 86), more than six times higher. People systematically double-check a colleague's finding more often than the model's finding, even though the model's finding turns out more accurate by a wide margin. This is the first direct measurement of exactly this side — insufficient, not excessive — of trust; the rest of the course's material on trust talks about excessive human trust in the model; here the opposite is measured, among professionals, on a sample of almost 55,000 women. And this is not the same figure as the 80.5 against 73.8 percent that measures cancer detection — that figure is about the share of cancer found out of what existed in a sample of 105,934 women; this one is about the share of findings sent to re-review, on a different sample of 54,991 women. The two figures are easy to confuse precisely because both are "about the model and trust," and they have to be kept explicitly apart.

The German program stands here for contrast. Detection rose — 6.7 against 5.7 per 1,000 among 463,094 women screened — but the construction of the work is different here, and it's named in the very first sentence of the publication's own summary: it compared double reading with model support against ordinary double reading. To put it as a figure, not a general phrase: the model replaced zero percent of human readings — both radiologists kept reading every case, with no exception. The same publication's authors separately recalculated a different, never-deployed scenario: if the cases the model classified as normal had simply not been read by a human at all, the workload would have dropped by 56.7 percent. This figure isn't an observation, it's a hypothetical recalculation on the same data, and the authors themselves call it exactly that. The conflict of interest here is named outright, not with a euphemism: the study was funded by the system's manufacturer (Vara), and some of the co-authors are its employees. The gap between 0 percent replacement (what happened) and 56.7 percent (what would have been counted under a different construction of the work), on the very same dataset, is simultaneously an engineering detail and a breakdown of an overstated claim passed off as a measurement.

And the last point — an honestly named gap, not a guessed-at one. Neither for the Swedish model (Transpara, developer ScreenPoint Medical) nor for the German one (Vara) do sources disclose the volume and composition of the training sample, the frequency of retraining after deployment, or the protocol for monitoring drift in the live flow. In both cases this is a closed-vendor commercial model, and the degree of disclosure here is lower than in the retinal-fundus case further in this section, where at least an order-of-magnitude figure for the training sample and one specific regulatory document on updates turned up. The difference between "a gap named outright" and "a gap nobody asked about" is the same one this course already requires we not lose track of.

**Sources.** [Warren et al., "Impact of using artificial intelligence as a second reader in breast screening including arbitration," Nature Cancer 2026](https://doi.org/10.1038/s43018-026-01128-z) · [Hovda, Holen, Hofvind, European Radiology 2026](https://doi.org/10.1007/s00330-025-12273-x) · [Dembrower, Crippa, Eklund, Strand, "ScreenTrustCAD," Radiology 2025](https://doi.org/10.1148/radiol.242566) · [Eisemann et al., PRAIM, Nature Medicine 2025](https://doi.org/10.1038/s41591-024-03408-6)
