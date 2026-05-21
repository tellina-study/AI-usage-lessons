---
id: s31
type: assertion_visual
duration_min: 2.5
assertion: "NHTSA SGO октябрь 2025: 65 сообщений, 54 подтверждённых смертельных случая с Tesla Autopilot. EA22002 идентифицировало 13 fatal crashes с foreseeable misuse."
learning_goal: "Tesla Autopilot fatalities + naming-driven over-reliance lesson"
learning_outcomes: [LO2, LO7]
chapter_ref: "§3.4 — Tesla Autopilot fatalities"
failure_bucket: strict_in
references: [wikipedia-tesla-autopilot-crashes, nhtsa-ea22002]
visual:
  pattern: data_chart_fatalities_breakdown
  primary: "Bar chart 65 reported vs 54 verified + EA22002 13 fatal crashes + 4 lessons"
---

# Tesla Autopilot: 54 verified fatalities NHTSA

## Числа

- **65 сообщений** в NHTSA SGO (Standing General Order on Crash Reporting) к октябрю 2025 года.
- **54 verified fatalities** — подтверждённых.
- **EA22002 investigation:** идентифицировало **13 fatal crashes с foreseeable misuse**.
- **2024 SGO data:** crashes в reduced-visibility conditions.
- **2025 new investigation:** ~2,9 миллионов Tesla vehicles.

## EA22002 investigation summary

- NHTSA открыл investigation в 2022 году специфически для Tesla Autopilot.
- Главный вопрос: достаточно ли driver-monitoring? Достаточно ли warning system?
- Identified pattern: водители используют Autopilot в условиях, для которых он не предназначен — например, чтобы спать, чтобы reading, чтобы выполнять non-driving tasks.
- **Foreseeable misuse** — концепт из engineering standards. Если 13 fatal crashes имеют foreseeable misuse pattern — это структурная проблема дизайна, не индивидуальная вина водителей.

## Уроки

- **Naming matters.** «Autopilot» и «Full Self-Driving» invite over-reliance — водитель думает, что машина «pilot», в реальности — это L2 ADAS.
- **Driver-monitoring обязателен.** Не optional. Не camera looking at face — это реальный engagement check.
- **Edge cases в perception:** sun glare, parked emergency vehicles, reduced visibility — distribution shift in real-world conditions.
- **Vision-only без HD-map** — research-stage для L4, не production-safe.

## Pedagogical point

54 fatalities на ~70 миллионов миль Autopilot operation (extrapolation Tesla disclosures) — статистически на порядок выше, чем human-driver baseline (~1 fatal на 100M миль). Это означает: Autopilot НЕ безопаснее human driver на статистически значимой базе. Vendor PR утверждает обратное, но независимая NHTSA disclosure показывает structural pattern.

## Speaker notes

Tesla Autopilot — это самая large-scale safety story в AV-индустрии. На середину 2025 года в базе NHTSA SGO зафиксировано шестьдесят пять сообщений, пятьдесят четыре подтверждённых смертельных случая, связанных с Tesla Autopilot или Full Self-Driving.

EA22002 — это investigation, которое NHTSA открыл в 2022 году специфически для Tesla Autopilot. Главный вопрос — достаточно ли driver-monitoring и warning system. Investigation identified тринадцать fatal crashes с foreseeable misuse pattern. Foreseeable misuse — это концепт из engineering standards. Если пользователь использует продукт в способе, который дизайнер мог предвидеть, и это приводит к fatalities, это — структурная проблема дизайна, не индивидуальная вина пользователя.

Pattern идентифицированный NHTSA. Водители используют Autopilot в условиях, для которых он не предназначен. Чтобы спать. Чтобы reading. Чтобы выполнять non-driving tasks. И Autopilot не обнаруживает это и не выходит из автоматического режима достаточно надёжно.

В 2024 году NHTSA расширил scope SGO data на crashes в reduced-visibility conditions. Это конкретный pattern — Autopilot имеет более высокий crash rate в conditions с sun glare, fog, ночь без street lights, рядом с parked emergency vehicles (police car lights confuse perception).

В 2025 году открыто новое investigation на approximately двух миллионов девятисот тысяч Tesla vehicles. Это шире, чем EA22002, и включает дополнительные categories.

Уроки. Первое — naming matters. «Autopilot» и «Full Self-Driving» invite over-reliance. Водитель видит название «Pilot» и думает, что машина управляет, как aircraft autopilot — то есть автономно. В реальности Autopilot — это L2 ADAS, который требует driver attention 100% времени.

Второе — driver-monitoring обязателен. Не optional. И не просто camera looking at face — это реальный engagement check, который detects когда водитель distracted и intervenes.

Третье — edge cases в perception. Sun glare, parked emergency vehicles, reduced visibility — это distribution shift in real-world conditions, который не покрывается training data.

Четвёртое — vision-only без HD-map. Это пока research-stage для L4. Waymo HD-map + LiDAR + remote ops + formal safety case — доказанный pattern. Tesla vision-only — пока не доказан на сравнимом mileage и safety basis.

Pedagogical point. Statistical comparison. Пятьдесят четыре fatalities на approximately семьдесят миллионов миль Autopilot operation — это extrapolation Tesla disclosures, может быть subject to verification. Если мы пересчитываем на per-100-million-miles baseline — это получается на порядок выше, чем human-driver baseline (один fatal на сто миллионов миль).

Это означает — Autopilot не безопаснее human driver на статистически значимой базе. Vendor PR утверждает обратное, но independent NHTSA disclosure показывает structural pattern.

Lesson для инженера. Когда вендор показывает statistics типа «Autopilot is X% safer than human driver» — проверяйте denominator, baseline, и source. Tesla сама публикует Tesla Vehicle Safety Report, но он использует Tesla's own definition «mile in Autopilot» и сравнивает с human-driver fatalities на ALL miles, не на comparable highway miles. Это apples-to-oranges comparison.
