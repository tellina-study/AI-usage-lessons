---
id: s26
type: takeaway
duration_min: 2
assertion: "Медицинский AI к 2026 — работающая инфраструктура. И вместе с этим — конкретная responsibility framework."
learning_goal: "3 takeaways — explicit LO1+LO2+LO3+LO8; 3 принципа = вход в копилку синтеза Лекции 17"
learning_outcomes: [LO1, LO2, LO3, LO8]
frame_mapping: ["Другой AI", "Человек vs AI", "Безопасность"]
chapter_ref: "§5.1 — Три главных вывода"
references: []
visual:
  pattern: matrix
  primary: "3-card summary layout (Диагностика ✓ / Drug discovery частично / Ответственность на враче) + Lucide иконки (activity / flask-conical / users)"
  illustration:
    type: schematic
    sources:
      - "Self-generated 3-card layout через PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `activity` (диагностика), `flask-conical` (drug discovery), `users` (ответственность), 96px hero size, recolored"
    caption: "3 takeaways — сырьё для копилки синтеза Лекции 17"
interaction: none
---

# 3 takeaways — медицинский AI к 2026 году

## Assertion

Медицинский AI к 2026 — работающая инфраструктура. И вместе с этим — конкретная responsibility framework.

## Visual

3 равные takeaway-cards в Ocean rounded box по горизонтали. Card 1 (Primary mid): иконка `activity` 96px сверху, заголовок «AI-диагностика работает ✓» 22pt semi-bold; текст 16pt: «mosmed.ai 14M+ исследований; FDA 1 451 devices; MASAI 44% workload ↓; CV-pipeline 2017–2024 уровня». Labels: LO1, LO2. Card 2 (Primary mid, **gold highlight на «Нобель 2024»**): иконка `flask-conical`, заголовок «Drug discovery — частично», текст: «AlphaFold solved structure prediction; Нобель 2024 (Hassabis + Jumper + Baker). Insilico Rentosertib peer-reviewed Phase IIa. DSP-1181 discontinued. Clinical attrition unchanged». Labels: LO2, LO3. Card 3 (deep): иконка `users`, заголовок «Ответственность — на враче», текст: «AI подсказывает, врач решает. Инженер делает responsibility технически выполнимой. 3 принципа → копилка для синтеза; финал — Лекция 17». Labels: LO3, LO8.

## Speaker notes

Если коротко описать, что мы прошли — три вывода и одно operational следствие. Первый. AI-диагностика работает. mosmed.ai обработал более четырнадцати миллионов исследований за пять лет в семидесяти четырёх регионах России; FDA одобрил тысячу четыреста пятьдесят одно AI/ML-устройство кумулятивно к концу 2025 года, семьдесят шесть процентов — радиология; MASAI Sweden RCT 2024–2025 подтвердил, что AI-supported маммография повышает чувствительность скрининга с семидесяти трёх и восьми десятых до восьмидесяти и пяти процентов при снижении нагрузки радиолога на сорок четыре процента. Это не футурология; это computer-vision-pipeline уровня 2017–2024 годов в production-форме.

Второй. Drug discovery работает частично. AlphaFold предсказал более двухсот миллионов структур белков и получил Нобелевскую премию по химии 2024 года — Hassabis, Jumper и Baker, последний за computational protein design. Insilico Rentosertib стал первым AI-designed препаратом с peer-reviewed positive Phase IIa readout в Nature Medicine, июнь 2025 года. DSP-1181 — discontinued. AI ускоряет discovery в пять–десять раз; clinical attrition rate около девяноста процентов AI не меняет, потому что эта статистика определяется биологией, а не алгоритмом.

Третий. Ответственность — на враче. AI подсказывает, врач решает. Инженер строит систему так, чтобы responsibility была технически выполнима: transparency и калибровка confidence, audit-trail, деперсонализация данных, post-market monitoring. Конкретные три принципа — transparency + calibration; validation set покрывает deployment population; audit-trail + post-market monitoring — это вход в копилку персонального чек-листа. Не финальный синтез — сырьё; финал собирается на Лекции 17 «Систематизация знаний и навыков» из всех отраслевых кейсов курса. Если в одной фразе: врач ставит диагноз, AI подсказывает, инженер делает так, чтобы врач мог по-настоящему решать.
