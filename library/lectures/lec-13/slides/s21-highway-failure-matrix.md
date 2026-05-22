---
id: s21
type: assertion_visual
duration_min: 1.5
assertion: "Четыре причины schwankenia AV-trucking startup'ов: capital intensity / regulatory / SPAC-bust / sim-to-real gap."
learning_goal: "Failure-matrix Раздел 2"
learning_outcomes: [LO2, LO7]
chapter_ref: "§2.6 — Серия банкротств: общие паттерны"
failure_bucket: strict_in
references: []
visual:
  pattern: failure_matrix_4_rows
  primary: "Таблица 4 строки × 3 колонки: причина / пример / что делать инженеру"
---

# Четыре причины провала AV-trucking startup'ов

## Матрица

| Причина | Пример (компания → год) | Что делать инженеру / оценщику |
|---|---|---|
| **Capital intensity без revenue** | Argo AI ($7B → Oct 2022); Cruise ($10B → Dec 2024) | Проверять unit economics: capital сожжённый / коммерческая выручка. Если revenue <5% от capital — flag. |
| **Регуляторная неопределённость** | TuSimple (US-China tension → Jan 2024); Tesla NHTSA EA22002 | Запрашивать legal team опыт. Какие СА государственно одобренные? Сколько NHTSA SGO crash reports? Что в pipeline EA-investigations? |
| **SPAC IPO bubble 2021-2022** | Embark (16 мес от SPAC до банкротства); TuSimple early days | Не вкладывать в pre-revenue SPAC merger без 5+ лет commercial history. Public market scrutiny убьёт hype. |
| **Sim-to-real gap** | Starsky (March 2020); общая causa каждого недо-выжившего | Запрашивать ratio км в симуляции / км на public roads. Если только sim — серьёзный red flag. |

## Связи с другими уроками лекции

- **Cruise (capital intensity + regulatory) — детально на s29.** GM dragging incident Oct 2023 → DMV suspension → Dec 2024 exit.
- **Tesla (regulatory + sim-to-real Variants) — s27, s31.** Vision-only без HD-map — research-stage в эффективности vs Waymo HD-map+LiDAR.
- **Survivors применяют crawl-walk-run** против всех 4 причин (s19).

## Speaker notes

Замыкая failure deep-dive раздела два — четыре причины, на которые рекуррентно ломаются AV-trucking стартапы. Этот чек-лист — практический инструмент для оценки.

Первая причина — capital intensity без revenue. Argo AI и Cruise сожгли семь и десять миллиардов соответственно прежде, чем заработать значительную коммерческую выручку. Lesson для инженера или оценщика: проверять unit economics. Capital сожжённый к коммерческой выручке. Если revenue менее пяти процентов от capital — это flag.

Вторая причина — регуляторная неопределённость. TuSimple — US-China геополитическое давление, и компания не смогла навигировать. Tesla — постоянные NHTSA investigations, EA22002, и неясность future regulatory action. Lesson: запрашивать legal team опыт. Какие SA государственно одобренные? Сколько NHTSA SGO crash reports? Что в pipeline EA-investigations?

Третья причина — SPAC IPO bubble 2021-2022. Embark — шестнадцать месяцев от SPAC merger до банкротства. SPAC target market cap пять с шестнадцати сотых миллиарда долларов — на момент merger Embark формально стоила больше, чем десятилетние профессиональные операторы. TuSimple вышла через IPO, но рано. Lesson: не вкладывать в pre-revenue SPAC merger без пяти+ лет commercial history. Public market scrutiny убьёт hype.

Четвёртая причина — sim-to-real gap. Starsky первым публично признал эту проблему через essay Стефана Зельц-Аксмахера в марте 2020. Но все non-survivors сталкивались с тем же — ML-стек выглядел хорошо в симуляции, но не масштабировался на public roads с edge-cases. Lesson: запрашивать ratio километров в симуляции к километрам на public roads. Если только sim — серьёзный red flag.

Эти четыре причины — взаимосвязанные. SPAC-bust 2021-2022 ускорил capital exit. Sim-to-real гэп замедлил commercial deployment. Это снизило revenue, что увеличило capital burn ratio. Что притянуло регуляторное scrutiny. И так замкнулся круг.

И обратно к survivors — Waymo, Aurora, Mobileye применяют crawl-walk-run против всех четырёх причин. Многолетние safety-operator километры до driverless. Conservative ODD expansion. Не SPAC merger (Aurora через SPAC, но с longer history). Honesty о limitations.
