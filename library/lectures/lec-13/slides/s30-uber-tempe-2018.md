---
id: s30
type: assertion_visual
duration_min: 2.5
assertion: "18 марта 2018, Tempe, Arizona. Элейн Хёрцберг — первая жертва беспилотника. Uber отключил заводское экстренное торможение, водитель безопасности смотрел телевизор."
learning_goal: "Uber Tempe — first AV pedestrian fatality + NTSB lessons"
learning_outcomes: [LO2, LO7]
chapter_ref: "§3.4 — Uber Tempe 2018"
failure_bucket: strict_in
references: [wikipedia-elaine-herzberg, ntsb-har-19-03]
visual:
  pattern: case_study_with_ntsb_quote
  primary: "Hero photo: NTSB investigation diagram (вид сверху на сцену incident) + NTSB cited quotes"
  acquisition_tiers:
    - "Tier 5: Wayback Machine for NTSB report PDF imagery"
    - "Tier 6: Reuters / AP press"
---

# Uber Tempe 2018: first AV-pedestrian fatality

## Факты

- **18 марта 2018**, ~22:00, Tempe, Arizona.
- **Элейн Хёрцберг**, 49 лет — пересекала дорогу с велосипедом вне crosswalk.
- **Uber Volvo XC90** с safety operator на bord.
- **Скорость удара: ~40 mph.**
- **Backup driver:** pleaded guilty endangerment 2023, 3 года supervised probation.

## Что технически произошло

- **Camera detected pedestrian 5,6 секунды до удара.**
- **Perception classifier failed:** не классифицировал как pedestrian (потому что Hertzberg была вне crosswalk + с велосипедом, distribution-edge).
- **Uber отключил заводское automatic emergency braking** (AEB) на Volvo XC90 — to avoid «conflicting interventions».
- **Backup driver:** watching TV (Hulu) во время инцидента, не следила за дорогой.

## NTSB quote (HAR-19/03)

> «The Uber Advanced Technologies Group's deactivation of its automatic emergency braking system increased the risks associated with testing automated vehicles on public roads.»

> «Uber's inadequate safety culture and inadequate safety risk assessment procedures were cited as factors.»

## Уроки

- **ODD critical:** training data bias на pedestrians вне crosswalk — perception classifier не обобщался.
- **Disabling factory safety systems** — anti-pattern. Никогда не отключать factory AEB ради «smoother autonomous behavior».
- **Safety driver attention** не reliable. Human factors — водители теряют alert в pre-autonomous mode за 10-15 минут.
- **Безопасная культура organization matters.** Uber ATG имела «inadequate safety culture» по NTSB.

## Speaker notes

Uber Tempe 2018 — это первая жертва беспилотного автомобиля в истории. Это самый важный safety case в AV-индустрии, и я хочу остановиться на два с половиной минут, потому что NTSB report HAR-19/03 — это canonical regulatory source.

Восемнадцатого марта 2018 года, примерно в десять вечера, в Tempe, Arizona, погибла Элейн Хёрцберг — сорок девять лет. Она пересекала дорогу с велосипедом вне crosswalk. Uber Volvo XC90 со скоростью около сорока миль в час ударил её. Безопасный водитель был на бортe, но не следила за дорогой.

Что технически произошло. Камера Uber detected pedestrian пять и шесть десятых секунды до удара. Это означает — perception работал, объект был обнаружен. Но perception classifier failed — не классифицировал объект как pedestrian. Hertzberg была вне crosswalk и с велосипедом, что попадало в distribution-edge для training data Uber. Модель видела «что-то», но не понимала, что это пешеход, и не triggered emergency response.

Дальше — Uber отключил factory automatic emergency braking на Volvo XC90. Не от plain forgetfulness — Uber делал это намеренно, to avoid conflicting interventions с собственным perception-стеком. Это означает, что когда Uber-стек failed классифицировать pedestrian, factory AEB тоже не сработал, потому что был отключен.

И backup driver — она смотрела Hulu, телевизионное шоу, во время инцидента. Не следила за дорогой.

NTSB report HAR-19/03 цитирует две важные вещи. Первая: «The Uber Advanced Technologies Group's deactivation of its automatic emergency braking system increased the risks associated with testing automated vehicles on public roads». Деактивация AEB увеличила риски. Вторая: «Uber's inadequate safety culture and inadequate safety risk assessment procedures were cited as factors». Inadequate safety culture цитировалось как factor.

Backup driver — pleaded guilty endangerment в 2023 году, три года supervised probation. Uber как корпорация — никаких criminal charges, но settled with Hertzberg family.

Уроки. Первый — ODD critical. Training data bias на pedestrians вне crosswalk — perception classifier не обобщался. Lesson: всегда расширять training set до full pedestrian behavior distribution, включая edge cases.

Второй — никогда не отключать factory safety systems. Anti-pattern. Если Uber-стек conflicted с Volvo factory AEB, это означает, что Uber-стек недостаточно качественный. Решение — поднять качество Uber-стека, не отключать factory.

Третий — safety driver attention не reliable. Human factors literature показывает, что водители теряют alert в pre-autonomous mode за десять-пятнадцать минут. Это не вина водителя, это структурная характеристика human attention. Lesson — single safety driver недостаточно для тестов на public roads.

Четвёртый — безопасная культура организации matters. Uber ATG имела inadequate safety culture по NTSB. Lesson — engineering culture, не алгоритмы, определяет real safety profile AV-программы.

И последнее — этот кейс стал foundation для NHTSA Standing General Order on Crash Reporting, который сейчас обязывает всех AV-операторов в США reporting crashes. Это институциональный legacy от смерти Элейн Хёрцберг.
