---
id: s17b
type: assertion_visual
duration_min: 2.5
assertion: "DSP-1181 (2020): «первый AI-designed drug в clinical trials». В 2022 — Phase 1 discontinued. AI ускорил design; clinical efficacy — отдельная задача."
learning_goal: "Drug discovery reality check — defensible balance"
learning_outcomes: [LO2, LO3]
frame_mapping: ["Человек vs AI", "LLM anti-pattern", "Безопасность"]
chapter_ref: "§3.4 — DSP-1181: проверка реальностью"
references: [synapse-patsnap-dsp1181, sumitomo-2020-pr, cas-insights-2024, recursion-2024-pr]
visual:
  pattern: timeline
  primary: "3-event timeline (янв 2020 entry → 2022 discontinue → 2026 current=Discontinued); pivot 2022 ≥2× larger (negative gold-grey)"
  illustration:
    type: news
    sources:
      - "Synapse Drug Profile DSP-1181 — https://synapse.patsnap.com/drug/a785db59b5d54d209ddfe8619dfcc2b0"
      - "Sumitomo 2020 press — https://www.sumitomo-pharma.com/news/20200130.html"
      - "CAS Insights — https://www.cas.org/resources/cas-insights/ai-drug-discovery-assessing-the-first-ai-designed-drug-candidates-to-go-into-human-clinical-trials"
      - "Recursion + Exscientia merger Aug 2024 — https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-enter-definitive-agreement-create"
    caption: "DSP-1181 timeline: Sumitomo, Synapse/PatSnap, CAS Insights"
interaction: none
---

# DSP-1181 — reality check: AI ускорил design, не clinical

## Assertion

DSP-1181 (2020): «первый AI-designed drug в clinical trials». В 2022 — Phase 1 discontinued. AI ускорил design; clinical efficacy — отдельная задача.

## Visual

Горизонтальный 3-event timeline. Event 1 (январь 2020, Primary light): «Exscientia + Sumitomo Dainippon — DSP-1181 Phase 1 entry (Japan, OCD)». Event 2 (2022, gold-grey **2× larger**, oval anchor — negative pivot): «Phase 1 discontinued в Японии — cause not specified». Event 3 (2026 current, deep): «Synapse/PatSnap status = Discontinued». События соединены em-dash. Под timeline — info-card в Ocean rounded box с insight 16pt: «AI ускорил design (12 мес vs 4–5 лет). Clinical efficacy — отдельная задача биологии. Маркетинговое «AI drug = быстро + эффективно» — две объединённые в рекламе claim'ы». Сверху assertion.

## Speaker notes

Параллельно с success-историей Rentosertib важно рассмотреть и обратный сценарий — препарат, на который десять лет назад указывали как «доказательство AI-революции в drug discovery» и который не дошёл до пациентов. Это DSP-1181.

В январе 2020 года японская Sumitomo Dainippon Pharma и британская AI-биотех Exscientia объявили о запуске Phase 1 испытаний нового препарата для обсессивно-компульсивного расстройства. Заявлено: путь от target identification до Phase 1 entry занял около двенадцати месяцев против традиционных четырёх–пяти лет для аналогичных задач. Препарат был назван «первым AI-designed drug в clinical trials» и стал главным маркетинговым примером для индустрии в 2020–2022 годах.

Что произошло дальше. В 2022 году Phase 1 в Японии была остановлена. Причина discontinuation публично не раскрыта — источники указывают на возможную комбинацию efficacy, safety или business decision, но без специфики. На май 2026 года глобальный R&D-статус DSP-1181 в Synapse Drug Profile зафиксирован как Discontinued.

Инженерный урок из этого кейса. AI ускорил design phase — это verifiable, эта часть работает. Но clinical efficacy — отдельная задача, отдельная биология. Маркетинговое обещание «AI drug = быстро + эффективно» — это две объединённые в рекламе claim'ы, которые в реальности независимы. AI не сделал DSP-1181 эффективным; AI ускорил поиск кандидата, а кандидат не показал ожидаемого клинического результата.

Это полезный антипод Rentosertib. Insilico показал, что AI-design'ed препарат может добраться до peer-reviewed Phase IIa с положительным эндпойнтом. DSP-1181 показал, что AI-design'ed препарат может не добраться до пациента. Оба случая совместимы с реальностью: около девяноста процентов clinical attrition rate в индустрии — статистика, на которую AI не влияет. Если вы будете строить AI для drug discovery — две claim'ы должны быть отделены: «ускоряем design» — техническая мера; «повышаем approval probability» — клинико-биологическая.
