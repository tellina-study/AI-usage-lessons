---
id: s40
type: assertion_visual
duration_min: 3
assertion: "Семь вопросов вендору на завтра — практический инструмент для кармана."
learning_goal: "Q&A + 7 vendor-вопросов для логистического AI"
learning_outcomes: [LO2, LO7]
chapter_ref: "§5 — Замыкание"
references: []
visual:
  pattern: vendor_questions_checklist
  primary: "Чек-лист 7 вопросов в rounded boxes + 'почему' под каждым"
---

# Семь вопросов вендору на завтра

## Чек-лист

**1. Какое сравнение с OR-baseline (Google OR-Tools, Gurobi, CPLEX)?**
Why — UPS ORION показывает, что OR часто работает лучше ML для well-defined optimization. Если поставщик не делал сравнения — red flag.

**2. Какой ваш ODD (Operational Design Domain), и как валидируется новое расширение?**
Why — Cruise dragging incident октября 2023 — провал именно ODD-дисциплины. Расширение ODD без extensive валидации — anti-pattern.

**3. Какой ваш driver-monitoring stack (для L2/L3)?**
Why — Tesla EA22002 идентифицировало 13 fatal crashes с foreseeable misuse — структурная проблема дизайна, не индивидуальная вина водителей.

**4. Какой ваш ratio км в симуляции / км на public roads?**
Why — Starsky sim-to-real gap. Если только simulation — серьёзный red flag.

**5. Какой error rate на сезонных distribution shifts (Black Friday, Christmas)?**
Why — distribution shift на сезонных пиках убивает ML-модели, обученные на off-peak data.

**6. Какие сертификации (FDA Part 11, ATEX, ISO 26262, NHTSA SGO)?**
Why — regulatory audit обязателен в safety-critical категориях. Black-box ML не проходит audit.

**7. Какова unit economics на машину / на маршрут / на тонну груза?**
Why — Pony.ai первый robotaxi с per-vehicle positive operating profit (Гуанчжоу Nov 2025, Шэньчжэнь Feb 2026). Без per-unit data — нельзя оценить sustainability.

## Speaker notes

Это последний content slide лекции. Я хочу оставить вас с практическим инструментом в кармане — семью вопросами, которые вы зададите любому vendor'у логистического AI.

Первый вопрос. Какое сравнение с OR-baseline? Google OR-Tools, Gurobi, CPLEX. Это очень важный вопрос, потому что часто vendor proposals для маршрутизации выглядят как ML-стек, но не показывают сравнения с classical OR. Если вы спрашиваете «а как вы сравнивались с Gurobi или OR-Tools», и получаете ответ «мы не делали такого сравнения» — это red flag. Это означает, что либо ML-решение не лучше OR, либо vendor не знает OR.

Второй вопрос. Какой ваш ODD, и как валидируется новое расширение? Это вопрос ДОДмишний, особенно для AV-программ. Cruise dragging incident октября 2023 года — провал именно ODD-дисциплины. Расширение ODD без extensive валидации — anti-pattern, который killed Cruise.

Третий вопрос. Какой ваш driver-monitoring stack для L2 или L3 systems? Tesla EA22002 идентифицировало тринадцать fatal crashes с foreseeable misuse pattern — это структурная проблема дизайна, не индивидуальная вина водителей. Driver-monitoring — обязательная feature, не optional.

Четвёртый вопрос. Какой ваш ratio километров в симуляции к километрам на public roads? Starsky sim-to-real gap — главная причина их failure. Если vendor показывает миллионы километров в симуляции но meanings нет километров на public roads — серьёзный red flag.

Пятый вопрос. Какой error rate на сезонных distribution shifts? Black Friday, Christmas, Halloween — каталог наполняется новыми категориями. Sparrow vision-классификатор часто ошибается чаще. Спросите vendor про сезонную динамику — какой error rate на пиковых сезонах vs обычное время? Как часто переобучается модель?

Шестой вопрос. Какие сертификации? FDA Part 11 для pharma cold-chain. ATEX для opasных зон. ISO 26262 для automotive safety. NHTSA SGO mandatory для AV-операторов в США. Regulatory audit обязателен в safety-critical категориях. Black-box ML не проходит audit.

Седьмой вопрос. Какова unit economics? Per машину, per маршрут, per тонну груза. Pony.ai — первая робoтакси с per-vehicle positive operating profit. Гуанчжоу ноябрь 2025, Шэньчжэнь февраль 2026. Без per-unit data — нельзя оценить sustainability vendor business model. И если vendor не публикует unit economics — это либо «still negative», либо «not disclosed for competitive reasons». Любой sceptic считает первое.

Эти семь вопросов carry с собой. Это вторая main payoff лекции — practical toolkit для оценки vendor proposals.

И теперь — Q&A. Я готов отвечать на ваши вопросы.
