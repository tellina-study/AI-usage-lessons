---
id: s23
type: failure_case
duration_min: 2
assertion: "20 июня 2025 — потеря связи с MethaneSAT после 15,5 месяцев работы (26% от designed lifetime). Single satellite = catastrophic single point of failure для regulatory MRV."
learning_goal: "Failure 1 Q2 + 4 урока: SPOF + hardware reliability + regulator constraint + AI зависит от upstream data"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part3.md]
  sections: ["§3.3 MethaneSAT loss"]
visual:
  type: image
  description: "MethaneSAT loss announcement EDF press release screenshot, июнь 2025"
  source_url: "https://www.methanesat.org/news/methanesat-update"
  acquisition_tier: 3
visible_numbers: ["20 июня 2025 — потеря", "15,5 месяцев = 26% от 5-летнего lifetime", "$5,7M/мес realized vs $1,5M/мес планировалось"]
russification_check: "MethaneSAT, EDF, GHGSat, Carbon Mapper, Tanager-1, Bridger Photonics, SeekOps — brand list; «единичная уязвимость» (SPOF), «regulatory infrastructure» — RU."
speaker_notes_target_words: 240
---

# MethaneSAT loss 20 июня 2025. Single satellite = catastrophic SPOF.

## Visible content

Заголовок: «20 июня 2025 — MethaneSAT потерян после 15,5 месяцев» (28pt deep ocean).
Sub: «4 марта 2024 запуск → 20 июня 2025 «spacecraft anomaly». 26% от 5-летнего designed lifetime.» (16pt italic)

**Слева — Ocean rounded box «Timeline»:**

- **4 марта 2024** — запуск SpaceX Falcon 9.
- **2024-2025** — ~2 000 data files, 180+ сцен, 10 публикаций.
- **20 июня 2025** — потеря связи. Причина не объявлена («spacecraft anomaly»).
- **Реализованная стоимость:** $88M / 15,5 мес = **~$5,7M/мес** vs планируемые $1,5M/мес при 5-летнем lifetime — **в 4× выше**.

**Справа — Ocean rounded box «4 фундаментальных урока»:**

1. **Single-satellite = catastrophic SPOF** для regulatory MRV infrastructure (gold accent).
2. **Hardware reliability — fundamental constraint.** Любая satellite mission имеет non-zero failure probability → constellation model essential.
3. **Regulatory enforcement не может опираться на 1 спутник.** EU после loss → mix GHGSat + ground OGI primarily.
4. **AI без stable upstream data source не работает.** ML слой над данными, не источник данных.

**Bottom bar:**

«Post-MethaneSAT mitigation: Carbon Mapper Tanager-1 + GHGSat 13-constellation + Bridger Photonics aerial + EU flexibility Level 4. Planned MethaneSAT-2 — Q4 2025 intention, funding/timeline неопределённы [VFY].»

## Speaker notes

Двадцатого июня 2025 года команда MethaneSAT объявила потерю связи со спутником. Через примерно пятнадцать с половиной месяцев после запуска четвёртого марта 2024 года — что составляет около двадцати шести процентов от designed lifetime в пять лет. Конкретная причина потери публично не объявлена; команда указывает на «spacecraft anomaly».

Четыре фундаментальных урока.

Первый — один спутник mission равно catastrophic single point of failure для regulatory MRV infrastructure. Когда EU Methane Regulation 2024/1787 предусматривает использование satellite measurements как accepted data source — и primary global satellite NGO-owned data source потерян — что делать с этой data infrastructure? Ответ к концу 2025 года: scramble к alternative data sources. Но resilience matters from day one.

Второй — даже с успешным запуском и хорошими данными первого года надёжность аппаратуры остаётся fundamental constraint. MethaneSAT работал отлично пятнадцать с половиной месяцев. Это не «технология провалилась»; это «спутник в космосе — это аппаратура с конечной reliability». Для главный infrastructure нужно группировка model, не single mission.

Третий — regulatory enforcement не может опираться на один спутник. EU regulator после MethaneSAT loss принимает GHGSat данные с осторожностью и приоритизирует ground OGI campaigns для соответствие. Это усиливает позицию ground OGI как альтернативного инструмента и снижает зависимость от satellite AI MRV.

Четвёртый — AI без stable верхний слой данных source не работает. Это самый глубокий урок. MethaneSAT использовал AI для downstream processing — atmospheric retrieval, plume detection, emission quantification. Когда upstream sensor stream исчезает — все downstream ML-модели становятся бесполезны на новых данных. То же самое случилось бы при потере любой ключевой сенсорной модальности. AI — это слой над данными, не источник данных.

Реализованная стоимость per month — пять и семь десятых миллиона vs планируемые полтора. В четыре раза выше cost effectiveness, чем обосновывала миссию.
