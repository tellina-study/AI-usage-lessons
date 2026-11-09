---
id: s12a
local_id: s1-02a
# ПЕРЕЕХАЛ ВПЕРЁД, И ЭТО НЕ ПЕРЕНУМЕРАЦИЯ РАДИ ПОРЯДКА (2026-10-19,
# владелец: страновые данные стоят слишком поздно в разборе). Кадр стоял
# ПЯТЫМ — между `s13` («Пример 1, без модели») и `s15` («Пример 1, с
# моделью»), то есть обзор по странам разрезал разбор Примера 1 надвое.
# Два правила канона это запрещают сразу: §1б «Строения раздела» требует
# обзор отрасли ЦЕЛИКОМ прежде первого разбора, а §5.13 требует, чтобы
# разбор читался одной последовательностью (цена ошибки → классические
# режимы → модель → что переехало). Теперь кадр идёт сразу за `s12` («Как
# устроен отбор»), до первого разбора; `s13` → `s15` стали соседями, как
# того и требует форма. Был `id: s13a` / `local_id: s1-03a`.
section: "1. Первичный скрининг и отбор на обследование"
type: analitika
title: "Screening programs by country, and where the model takes part"
assertion: "Охват классических программ разложен по пяти странам (Корея и Австралия названы в заметках: по одному столбцу каждая, обе программы на диаграмме уже показаны): внутри каждой строки свои программы со своим знаменателем, от 18,7 процента на лёгком в США до 83–85 на шейке матки в Швеции; там, где популяционной программы нет вовсе — простата в США, лёгкое в Нидерландах, — столбец не рисуется и отсутствие названо словами; модель встроена в государственную программу там, где классический охват ещё не отлажен (Польша и Хорватия на лёгком с 2020 года, Япония на колоректальном с отдельной страховой оплатой с 2024), а там, где охват отлажен десятилетиями, остаётся на уровне отдельной лаборатории; эффекта ИИ-компонента на исход не измерено ни в одной из семи стран"
source: "National screening-program reports, 2022–2025 — ten sources are listed in the notes"
media: "rework/deck/assets/s12a-ohvat-po-stranam.png"
media_needed: "добыто: собственная аналитика по шаблону `tools/presentation-build/analitika.py`, прогон `rework/deck/make_chart_s13a.py`"
media_note: "ПЕРЕСТРОЕНА ПОД §10.1/§11.4 (прожарка 2026-10-19). Было: десять строк «Лёгкое · США», «Лёгкое · Великобритания», отсортированных по величине, с подзаголовком «знаменатель у каждой строки свой» — то есть ранжирование несравнимых величин, которое к тому же не отвечало на вопрос «как дела в стране X»: строки одной страны лежали в разных концах диаграммы. Стало: строка — СТРАНА, внутри по столбцу на программу, порядок программ одинаков у всех стран, знаменатель подписан у конца КАЖДОГО столбца своим. Отсутствие программы нулевым столбцом не рисуется (ноль читался бы как измеренный охват) — названо словами в теле. Польша и Хорватия на диаграмме не столбцами, а плашкой: у них есть факт встроенной модели, но знаменателя охвата источники не публикуют"
blocks:
  - {label: "Model in the architecture", value: "Poland · Croatia", note: "lung, since 2020; sources give no coverage figure"}
  - {label: "Model with separate payment", value: "Japan, since 2024", note: "colorectal: 43% and 28% of hospitals", key: true}
  - {label: "Effect on patient outcome", value: "measured nowhere", note: "participation, coverage, and payment are measured"}
timing_min: 1.0
in_bucket: false   # кадр смешанный: охват по странам — нейтральная статистика,
  # строго in-bucket по § AI-Failure Content Rule только простата (осознанный
  # отказ от популяционной программы) и строка про неизмеренный эффект.
  # Правило требует partial → как out, поэтому false.
method_steps: ["обзор по странам"]
form: []
vizforma: "полоса + плашки"
vfy: true
status: собран
---

## Visible slide text

**Row = country, column = program.** No column, no program: prostate in the US, lung in the Netherlands — a decision both times, not a data gap.

## Speaker notes

Coverage of classical screening programs by country: a row is a country, a column is its program. Where there's no column, there's no program — prostate in the US, lung in the Netherlands, and both times that's a decision, not a gap in the data. There are four programs here besides mammography: lung, cervical, colorectal, and prostate, and each has its own answer to who gets called in and whether a trained model takes part in selection. The chart is laid out by country, not by program, deliberately: the question an engineer brings to a project like this is "how is this built here," not "where in the world is the percentage higher."

The rates are computed from different bases — invited, attending, or the whole target group by registry — and the denominator is labeled at the end of each column, right next to the number. They can't be combined into one ranking, and the chart doesn't offer that: within a country, the columns stand in the same program order every time, so the eye compares country to country along the same band.

Lung screening is an annual low-dose CT for people in a smoking-risk group. In the US, 12.8 million people meet the criteria, and 18.7 percent of them get screened — up from 4.5 percent in 2022, almost fourfold in two years, even as absolute coverage stays low. In the Netherlands there is no national program at all — even though it was the Dutch-Belgian NELSON trial, more than ten years ago, that proved a mortality reduction from exactly this kind of screening. Proven method effectiveness and a built program are two different things, and here the gap between them exceeds a decade. Meanwhile, in Poland and Croatia the model is built straight into the national program's architecture from the start, not layered on top of it by a vendor: Croatia, since 2020, is the first EU country with a fully integrated lung-screening program. Sources for neither country give a target-group denominator, so they don't appear on the coverage chart: the fact of the model's deployment is there; a coverage figure to compare it against is not.

Cervical screening shows a mirror image. Coverage here has been settled for decades and is higher everywhere: Sweden 83–85 percent, the UK 68.8 out of 16.5 million, Australia 74.2 and falling, the Netherlands 54.4. The model, meanwhile, is nowhere built into the program itself — only into separate commercial lab systems (Hologic in the US, Techcyte in Austria) and into a non-mandatory recommendation from a professional association in the UK.

Colorectal cancer is the strongest case of model involvement in this block. The Netherlands holds one of the highest coverage rates in the world, 67.1 percent, one and a half million people on a home fecal test — noticeably higher than the same country's cervical coverage in the same year: turnout depends on the type of test, home versus a visit, not just on a general screening culture. The US holds 63.5–67.4 percent across two 2023 measurements. Japan shows a persistent gap between men and women: 49.1 against 42.8 percent; on the chart this is one column, and the label at its end names both source figures, not an average. And since February 2024, Japan has been paying a separate insurance surcharge specifically for the AI component of colonoscopy — EndoBRAIN-EYE, the world's first case of paying not for the device as a whole, but specifically for its model-driven part. The condition narrows the field: the surcharge only applies to an endoscopist with at least five years of experience. By early 2025, the system had been deployed in 43 percent of university hospitals and 28 percent of regional hospitals; sources give no absolute count of such hospitals, and I'm naming that as a gap, not padding it with an estimate.

Two countries didn't make the chart: Korea holds 51.2–58.6 percent on lung screening across two 2023 measurements, Australia holds 74.2 and falling on cervical. Both carry just one column each, and both programs are already shown by other countries on the chart; the slide's band holds five groups so the labels stay readable, not seven. Separately — Korea's colorectal coverage is missing for a different, substantive reason: the available figure of 74.4 percent counts coverage across six types of screening combined, not colorectal on its own. Putting it in the colorectal column would mean substituting someone else's denominator — exactly the kind of conflation this whole section is examining.

Prostate is a case where the question about the model isn't even first in line. The current recommendation from the US task force, since 2018: the decision on a PSA test for men 55–69 is individual, after a conversation with a doctor; outside that window, including 70 and older, population-wide screening isn't recommended at all. This isn't a measurement gap but a considered regulatory position: prostate cancer grows so slowly in many men that it would never have surfaced in their lifetime, and the cost of overdiagnosis — surgery or radiation therapy, with incontinence and erectile dysfunction — outweighs the benefit of the finding for such cases. There's exactly one confirmed exception, and it's on the chart: since 2020, Sweden has run a registry-based invitation for men 50–74 across sixteen of twenty-one regions, 256,000 invited, 43 percent participation. The program, though, is built around the PSA test, not the model; a narrow pilot of MRI reading by a model inside it hasn't been measured as a separate figure.

And the last, most important point on this slide. The effect of the AI component itself on patient outcome — finding disease earlier, mortality — isn't measured by sources in any of these countries. What's measured is participation, coverage of the target group, or the fact of payment — that is, what happened to the organization, not what this changes for the person. From here comes a direct question for a vendor: if they say "deployed," ask into what exactly — into the program's architecture or as a separate layer on top of it — whether anyone pays for it separately, and whether there's any measurement of effect at all, or whether it stopped at regulatory clearance.

**Sources.** [American Cancer Society — US lung-screening coverage, 2025](https://pressroom.cancer.org/2025-lung-cancer-data) · [NHS England — cervical screening, 2023–24](https://digital.nhs.uk/data-and-information/publications/statistical/cervical-screening-annual/england-2023-24) · [Netherlands National Institute for Public Health — cervical-screening monitor, 2024](https://www.rivm.nl/sites/default/files/2026-01/monitor-2024-cervical-cancer-screening.pdf) · [Netherlands National Institute for Public Health — colorectal-screening monitor, 2024](https://www.rivm.nl/sites/default/files/2026-01/monitor-2024-colorectal-cancer-screening.pdf) · [Australian Institute of Health and Welfare — cancer screening programs report, 2025](https://www.aihw.gov.au/reports/cancer-screening/ncsp-monitoring-report-2025/contents/summary) · [US Preventive Services Task Force — prostate cancer screening](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/prostate-cancer-screening) · [Swedish Organised Prostate Cancer Testing, 2025 guidelines](https://cancercentrum.se/download/18.7ef8e06c1966b5e0eb8c615/1745839347877/swedish-opt-guidelines-2025.pdf) · [Cybernet — insurance surcharge for EndoBRAIN-EYE, February 2024](https://www.cybernet.co.jp/documents/pdf/news/press/2024/240216E.pdf) · [WHO European Observatory — national lung-screening program in Croatia, 2025](https://eurohealthobservatory.who.int/monitors/pace/case-studies/pace/pace-croatia-2025/croatia-implements-nationwide-lung-cancer-screening-programme-to-address-high-burden-of-disease) · [Lancet Western Pacific — lung screening in Poland](https://www.thelancet.com/journals/lanwpc/article/PIIS2666-6065(26)00066-0/fulltext)
