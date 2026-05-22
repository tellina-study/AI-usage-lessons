---
id: s32
type: assertion_visual
duration_min: 1.5
assertion: "Четыре урока городского AV: ODD дисциплина / driver-monitoring обязателен / naming matters / hardware ≠ платформа."
learning_goal: "Failure-matrix Раздел 3"
learning_outcomes: [LO2, LO7]
chapter_ref: "§3.6-3.8 — Urban failure-matrix (Cruise + Uber Tempe + Tesla NHTSA)"
failure_bucket: strict_in
references: []
visual:
  pattern: failure_matrix_4_rows
  primary: "Таблица 4 строки × 3 колонки: урок / кейс / что делать инженеру"
---

# Четыре урока городского AV

## Матрица

| Урок | Демонстрирующий кейс | Что делать инженеру |
|---|---|---|
| **ODD дисциплина критична** | Cruise (dragging incident + rapid ODD expansion); Uber Tempe 2018 (training data bias на pedestrians вне crosswalk) | При оценке AV-программы — какой ODD? Какие условия за пределами ODD? Какой процесс validation для new ODD expansion? |
| **Driver-monitoring обязателен** | Tesla Autopilot 54 fatalities NHTSA; EA22002 13 fatal crashes с foreseeable misuse | При L2/L3 systems — реальный engagement check, не camera looking at face. Что система делает при distracted driver? |
| **Naming matters** | Tesla «Autopilot» и «Full Self-Driving» — приглашают over-reliance | Никогда не называть L2 ADAS «pilot» / «autonomous» / «self-driving» / «full self-driving». Use SAE level terminology. |
| **Hardware ≠ платформа** | Cruise (GM hardware-OEM культура vs software-platform требования) | Когда OEM покупает software startup — какая cultural integration plan? Cruise GM показал, что отсутствие плана = anti-pattern (см. также GE Predix в Лекции 11). |

## Связи между уроками

- **ODD + driver-monitoring** — две стороны одной inverse coin. ODD определяет где система должна работать; driver-monitoring определяет, что делать, когда система за пределами ODD.
- **Naming + ODD** — naming приглашает или препятствует ODD-дисциплине. Если пользователь думает «autopilot», он не следит за ODD-edge. Если «driver-assist», он более ответственно.
- **Hardware ≠ платформа** — это lesson лекции 11 (GE Predix) — теперь рекуррентен в transport (Cruise GM, Argo Ford+VW).

## Speaker notes

Замыкая failure deep-dive раздела три — четыре урока городского AV, которые суммируют Cruise / Uber / Tesla кейсы.

Первый урок — ODD дисциплина критична. Cruise — главный пример. Rapid ODD expansion в SF без extensive валидации ночных смен. Uber Tempe — другой пример. Training data bias на pedestrians вне crosswalk означал, что Hertzberg в её специфической ситуации была за пределами effective ODD. Lesson — при оценке AV-программы: какой ODD? Какие условия за пределами? Какой процесс validation для new ODD expansion?

Второй урок — driver-monitoring обязателен. Tesla Autopilot — пятьдесят четыре fatalities NHTSA. EA22002 — тринадцать fatal crashes с foreseeable misuse. Lesson — при L2 и L3 systems — реальный engagement check, не просто camera looking at face. Что система делает при distracted driver? Это структурный design question.

Третий урок — naming matters. Tesla назвала L2 ADAS «Autopilot» и «Full Self-Driving». Это приглашает over-reliance. Lesson — никогда не называть L2 ADAS «pilot», «autonomous», «self-driving», «full self-driving». Use SAE level terminology — L2, L3, L4. Тогда пользователь понимает limitations.

Четвёртый урок — hardware ≠ платформа. Cruise — GM hardware-OEM культура vs software-platform требования. GM-Cruise hybrid culture не работала, потому что hardware OEM культура (квартальный отчёт, supply chain optimization, conservative engineering pace) не совместима с software platform требованиями (rapid iteration, accept failures in early stages, network effects, scale-first profitability-later). Lesson — это recall из Лекции 11 про GE Predix, и теперь рекуррентен в transport. Когда OEM покупает software startup — какая cultural integration plan?

Связи между уроками. ODD и driver-monitoring — это две стороны одной coin. ODD определяет где система должна работать. Driver-monitoring определяет, что делать, когда система за пределами ODD.

Naming и ODD — naming приглашает или препятствует ODD-дисциплине. Если пользователь думает «autopilot», он не следит за ODD-edge. Если «driver-assist», он более ответственно.

Hardware ≠ платформа — это lesson лекции 11 (GE Predix), теперь рекуррентен в transport — Cruise GM, Argo Ford+VW. Это структурный pattern OEM-software интеграции, и он работает не только для transport.

Эти четыре урока вы можете записать как чек-лист в кармане. При оценке любого AV-предложения от вендора — ODD дисциплина, driver-monitoring, naming, OEM-cultural integration.
