---
id: s39
type: assertion_visual
duration_min: 2
assertion: "Семь критериев «когда AI плохая идея». Прогоните предложенное AI-решение через эту матрицу — если хоть один срабатывает, нужен redesign."
learning_goal: "Consolidation 7 критериев по OODA — главная takeaway-матрица лекции"
learning_outcomes: [LO3]
chapter_ref: "§5.1 — Семь критериев"
references: []
visual:
  pattern: schema_matrix
  primary: "Matrix 7 строк × 3 колонки + gold pivot на #4 + #5"
---

# Семь критериев «когда AI плохая идея»

## Assertion

Семь критериев «когда AI плохая идея». Прогоните предложенное AI-решение через эту матрицу — если хоть один срабатывает, нужен redesign.

## Visual

Под assertion — большая matrix в Ocean rounded box, 7 строк × 3 колонки (#, звено, критерий, иллюстрация). Header row Primary mid с белым текстом; tела строк альтернируют Surface light / White:

| # | Звено | Критерий | Иллюстрация |
|---|---|---|---|
| **1** | Sense | Low-data domain или distribution shift | Adversarial SAR ATR; новые цели |
| **2** | Sense | High-stakes single-sensor без избыточности | F-35 ALIS без HITL flight gate |
| **3** | Decide | Long-tail edge cases с low ML confidence | Mission planning под новые ROE |
| **4** | Decide | High-stakes life-and-death без HITL | **Lavender** canonical anti-example |
| **5** | Act | Автономия не нужна, человек медленнее но безопаснее | **737 MAX MCAS** как «решение проблемы, которой не было» |
| **6** | Act | COTS sensor дешевле + reliable | AoA-redundancy на 737 MAX стоила бы порядки меньше |
| **7** | Cross-cutting | Граница HOOL → HOTL — treaty-territory, не engineering | LAWS · UN GGE |

Gold accent — на строки #4 (Lavender) и #5 (MCAS) — канонические learning cases. Иконка `triangle-alert` в gold справа от каждой.

Под matrix — bottom callout 16pt italic в Teal-tint box: «**Главное в этой матрице — она инструмент**. Один срабатывает → redesign; несколько → пересмотр фундаментального подхода».

Источник footer 12pt italic: «Критерии распределены по разделам как закрывающий takeaway. Cross-ref главы — §5.1».

## Speaker notes

Соберём в одну матрицу все шесть критериев, выведенных по разделам, плюс один cross-cutting — итого семь критериев «когда не AI» для аэрокосмической и оборонной области.

В звене Sense — два критерия. Первый: low-data domain или distribution shift inevitable. Иллюстрация — adversarial SAR ATR, новые цели. Второй: high-stakes single-sensor без избыточности. Иллюстрация — F-35 ALIS без HITL flight gate.

В звене Decide — два критерия. Третий: long-tail edge cases с low ML confidence — нужна abstention. Иллюстрация — mission planning под новые ROE. Четвёртый: high-stakes life-and-death без HITL. Канонический контрпример — Lavender.

В звене Act — два критерия. Пятый: автономия не нужна, человек медленнее но безопаснее. Канонический пример — 737 MAX MCAS как «решение проблемы, которой не было». Шестой: COTS sensor дешевле и надёжнее. AoA-redundancy на 737 MAX стоила бы порядки меньше всех trim-AI.

И один cross-cutting, седьмой: граница HOOL → HOTL — это treaty-territory, не engineering. Это про LAWS и UN GGE.

Главное в этой матрице — она инструмент. Когда вам предлагают AI-решение для аэрокосмической или оборонной задачи, прогоните его через эти семь критериев. Если хоть один срабатывает — это не значит «нельзя», это значит «здесь нужен redesign». Если срабатывает несколько — стоит пересмотреть фундаментальный выбор подхода.

Эта матрица — не догма. Она работает в 2026 году с теми данными, которые у нас есть. Через 5 лет, возможно, появятся новые критерии — например, про energy footprint AI-систем в боевых условиях, — и старые могут сместить акценты. Это рабочий инструмент, который надо обновлять с опытом.
