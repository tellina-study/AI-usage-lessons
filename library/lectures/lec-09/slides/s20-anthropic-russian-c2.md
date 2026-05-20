---
id: s20
type: assertion_visual
duration_min: 2
assertion: "Anthropic-Palantir-AWS (ноябрь 2024): Claude на IL6. Российский C2 — Svod / Glaz-Groza с явным single-source caveat."
learning_goal: "Anthropic IL6 + Russian Svod (one-source caveat); сравнение"
learning_outcomes: [LO1a]
chapter_ref: "§2.2 — Anthropic + Russian C2"
references: [businesswire-2024-anthropic, csis-2026-bondar]
visual:
  pattern: matrix
  primary: "2 cards: Anthropic IL6 + Russian C2 with caveat"
---

# Anthropic IL6 + Russian C2 — две разные карты

## Assertion

Anthropic-Palantir-AWS (ноябрь 2024): Claude на IL6. Российский C2 — Svod / Glaz-Groza с явным single-source caveat.

## Visual

Под assertion — 2 равные карточки в Ocean rounded box.

**Слева — Anthropic-Palantir-AWS** (gold accent):
- Logos: Anthropic + Palantir + AWS GovCloud (24px LobeHub)
- Date: **7 ноября 2024**
- 3 пункта capabilities:
  - Claude 3 + 3.5 на **IL6** — высший US gov-cloud уровень
  - Complex data processing
  - Pattern identification · time-sensitive decisions
- Bottom callout: «Точка инфлексии в industry posture (см. Раздел 4.5)»

**Справа — Russian Svod / Glaz-Groza** (caveat tint):
- 3 компонента:
  - **Svod Tactical Situational Awareness Complex** — анонс август 2025, разработка с 2024
  - **Glaz** — приложения для операторов дронов (геомэппинг)
  - **Groza** — fire-control + mission management
  - **ZOV Maps** — геопространственная платформа
- Source: «CSIS Bondar апрель 2026 + Russian official press»
- Italic caveat (Teal-tint): «Independent western verification отсутствует. Effectiveness — uneven по CSIS»

Внизу — bridge 12pt italic: «Мы упоминаем эти системы потому, что они существуют как попытка. Не упоминать был бы перекос; некритично сообщать как success — была бы пропаганда».

## Speaker notes

Четвёртый кейс декабрьского состава — Anthropic-Palantir-AWS partnership от 7 ноября 2024 года. Хронологически — один из ключевых сдвигов поздних 2024-х: Anthropic вывел свои модели Claude 3 и Claude 3.5 на IL6 — Impact Level 6, высший US gov-cloud уровень секретности — через Palantir и AWS GovCloud. Use cases: complex data processing, pattern identification, time-sensitive decisions. Это точка инфлексии в industry posture — между Maven walkout 2018 года и этим partnership всего шесть лет, и AI-индустрия прошла полный цикл от «отказа от военных контрактов как принцип» до «военные контракты — критический revenue stream». Разбор этого сдвига — в Разделе 4.5.

Пятый кейс — российский C2. Российская попытка decision-support аналога Palantir MSS. По CSIS, Bondar, апрель 2026, Россия строит экосистему network-centric warfare на основе трёх компонентов. Svod Tactical Situational Awareness Complex — объявлен в августе 2025, активная разработка с 2024, экспериментальное развёртывание в подразделениях с осени 2025. Параллельно — Glaz и Groza-ZOV digital ecosystem. Glaz — приложения для операторов дронов: разведка, геомэппинг. Groza — fire-control и mission management. ZOV Maps — геопространственная платформа.

Caveat явный single-source. Information о Svod и Glaz-Groza поступает из двух источников: Russian official press — Ростех, MoD статьи — и CSIS-аналитика на основе этой press плюс OSINT. Independent western verification отсутствует. Effectiveness в combat — по CSIS — uneven.

Pedagogically мы упоминаем эти системы, потому что они существуют как попытка, и студент-инженер должен знать, что в российском оборонном AI этот класс задач разрабатывается. Не упоминать был бы перекос; некритично сообщать как success — был бы пропаганда. Мы выбираем промежуточный путь: упомянуть с явной оговоркой источников. Это лучший паттерн работы с непроверяемыми данными вообще — не «верить» и не «отвергать», а явно маркировать уровень доказательности.
