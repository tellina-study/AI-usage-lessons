---
id: s38s
type: schema_matrix
duration_min: 1.5
assertion: "AP1 термодинамика > ML / AP3 порог точности ≠ внедрение / AP4 generic LLM как советник = антипаттерн / AP6 AI-equipment = vendor lock-in / AP7 AI-MRV без direct measurement = greenwashing. + AP2a/AP2b/AP5 inline."
learning_goal: "Главный consolidation takeaway лекции (LO5)"
learning_outcomes: [LO5]
chapter_ref: "§6.2 Часть 3 — Пять явных «когда не ИИ» — consolidation"
references: []
visual:
  pattern: schema_matrix
  primary: "Matrix 5 строк × 3 колонки (# / Критерий / Пример / Альтернатива) + 3 inline критерия снизу"
---

# Пять критериев «когда не AI» — главный takeaway

## Assertion

AP1 термодинамика > ML / AP3 порог точности ≠ внедрение / AP4 generic LLM как советник = антипаттерн / AP6 AI-equipment = vendor lock-in / AP7 AI-MRV без direct measurement = greenwashing. + AP2a/AP2b/AP5 inline.

## Visual

Под assertion 28pt bold — большая matrix в Ocean rounded box, 6 строк (header + 5 критериев) × 4 колонки. Header row Primary mid с белым текстом; тела строк альтернируют Surface light / White:

| # | Критерий | Пример из лекции | Альтернатива |
|---|---|---|---|
| **AP1** | **Закон термодинамики важнее ML** — фундаментальная экономика на порядок выше цены продукта | Vertical farming — LED ≈ 100× free sunlight; Plenty $940M, Bowery $32M | Открытый грунт при энергии <$0,10/кВт·ч; vertical только для high-value crops |
| **AP3** | **Пороговая точность ≠ готовность к внедрению** | Plantix 10-15% misdiagnosis × 10M+ = ~100k неправильных рекомендаций/год | Calibrated confidence + abstention; «не уверен → спроси эксперта» |
| **AP4** | **Обобщённый LLM в advisory mode** для high-stakes = категорический антипаттерн | ChatGPT/Bard рекомендация неправильного окна гербицида (Tzachor 2024) | RAG-grounded в local regulator + abstention + человек в цикле |
| **AP6** | **«AI-driven equipment» = ловушка vendor lock-in** | FTC v. Deere; Мелитополь remote-brick; FieldView выход из РФ; FCC ban DJI | Open-source hardware (Farm Hack); right-to-repair; multi-vendor; mechanical fallback |
| **AP7** | **AI-MRV для carbon claims без direct measurement** = scaled greenwashing | Verra 94% phantom credits; Pachama 8×; Bowery $32M never-used | Direct soil sampling + transparent uncertainty bands; AI как hypothesis, не fact |

**Gold accent** на критериях AP1 + AP6 (две самые «structural» — закон термодинамики + vendor lock-in trap).

Под matrix — secondary table в Teal-tint box: **Inline критерии (введены в §2 и §5):**

| # | Критерий | Пример | Альтернатива |
|---|---|---|---|
| **AP2a** | Архитектурный выбор внутри AI-домена | Cognitive Pilot CV vs ИТЭЛМА sensor-fusion | Другой класс AI (sensor-fusion вместо CV) |
| **AP2b** | Genuine не-AI альтернатива | FarmWise CV-weeders → Lemken/Kverneland механические | Mechanical / direct measurement |
| **AP5** | Cloud-first для off-grid = архитектурная ошибка | 18% US ферм без интернета; GNSS-jamming Финляндия; Starlink ban РФ | Edge ML / TinyML; hybrid с redundancy |

Bottom callout 16pt italic в gold-tint box: «**Это рабочая матрица 2026 года. Прогоните предложенное AI-решение через пять критериев — если хоть один срабатывает, нужен redesign**».

## Speaker notes

Соберём в одну таблицу пять явных критериев «здесь ИИ не нужен или не применим», которые мы разобрали в течение всей лекции. Это финальный consolidation для LO-пять — analyze, сформулировать как минимум пять явных критериев когда AI не применим.

Критерий первый — AP-один. Закон термодинамики важнее ML. Когда фундаментальная экономика (энергия или капитальные вложения) на порядок выше рыночной цены продукта — ML не закрывает разрыв, потому что он работает на знаменателе. Пример из лекции — вертикальное земледелие для commodity leafy greens: LED примерно в сто раз больше энергии, чем free sunlight; Plenty потерял девятьсот сорок миллионов, Bowery — тридцать два миллиона never-used equipment. Альтернатива — открытый грунт при энергии менее десяти центов за киловатт-час; vertical только для high-value crops.

Критерий второй — AP-три. Пороговая точность не равна готовности к внедрению. Даже девяносто процентов точности на масштабе — это сотни тысяч ошибочных high-stakes решений. Пример: Plantix десять-пятнадцать процентов misdiagnosis на десяти миллионах плюс загрузках — примерно сто тысяч неправильных рекомендаций по пестицидам в год. Альтернатива — uncertainty-aware рекомендация с abstention: не уверен — спроси эксперта.

Критерий третий — AP-четыре. Обобщённый LLM в режиме советника для high-stakes решений — категорический антипаттерн. Пример: ChatGPT и Bard рекомендации неправильного окна гербицида в Tzachor et al. в Nature Food 2024 года. Альтернатива — RAG-grounded в локальный регулятор: USDA-EPA, EU-EFSA, Россельхознадзор — плюс явный отказ при низкой уверенности плюс человек в цикле.

Критерий четвёртый — AP-шесть. AI-driven equipment — это ловушка привязки к поставщику. Чем больше AI и телематики в технике, тем сильнее vendor control surface. Примеры: FTC против Deere в 2025-м, Мелитопольский remote-brick в 2022-м, Climate FieldView выход из РФ, FCC ban DJI ag-drones. Альтернатива — open-source hardware Farm Hack, право на ремонт, multi-vendor стратегия, mechanical fallback.

Критерий пятый — AP-семь. AI-MRV для carbon claims без direct measurement — это inference с большой uncertainty, marketed как precise measurement — то есть scaled greenwashing. Пример: Verra девяносто четыре процента phantom credits, Pachama overestimation в восемь раз. Альтернатива — direct soil sampling значимой доли проектов плюс transparent uncertainty bands; AI как hypothesis, а не как fact.

Плюс три inline критерия, которые мы ввели в Разделах 2 и 5 и активно используем. AP-два-а — архитектурный выбор внутри ИИ-домена: когда CV не работает в open-environment, другой класс ИИ — sensor-fusion-AI — может быть более робастным; пример Cognitive Pilot против ИТЭЛМА. AP-два-б — genuine не-ИИ альтернатива: когда AI как класс не применим, mechanical работает; пример vertical farming → открытый грунт; FarmWise → Lemken Steketee. AP-пять — cloud-first для off-grid — архитектурная ошибка; альтернатива edge ML / TinyML.

Главное в этой матрице — она инструмент. Когда вам предлагают AI-решение для агро-задачи, прогоните его через эти пять критериев плюс три inline. Если хоть один срабатывает — это не значит «нельзя», это значит «здесь нужен redesign». Если срабатывает несколько — стоит пересмотреть фундаментальный выбор подхода.

Эта матрица — не догма. Она работает в 2026 году с теми данными, которые у нас есть. Через пять лет, возможно, появятся новые критерии, и старые могут сместить акценты. Это рабочий инструмент, который надо обновлять с опытом.

## Источники

- Chapter v3.1 §6.2 Часть 3.
- Lecture-wide synthesis всех failure-блоков.
