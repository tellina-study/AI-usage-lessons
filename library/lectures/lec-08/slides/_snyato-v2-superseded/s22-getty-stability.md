---
id: s22
type: assertion_visual
duration_min: 2
assertion: "Getty против Stability AI: UK High Court 04.11.2025 — Stability выиграл primary claims (weights ≠ copy по CDPA). US case MTD 10.02.2026."
learning_goal: "Case 2: cross-jurisdiction split (UK win vs US pending)"
learning_outcomes: [LO4]
chapter_ref: "§3.3 — Getty против Stability AI"
references: [bird-bird-ruling, getty-stability-uk]
visual:
  pattern: assertion_visual
  primary: "Bird & Bird ruling screenshot + UK vs US split visual + «Урок: проверяй обе юрисдикции»"
  backup: assets/backup/s22-getty-uk-ruling.png
---

# Getty против Stability — UK win vs US pending (Case 2)

## Assertion

Getty против Stability AI: UK High Court 04.11.2025 — Stability выиграл primary claims (weights ≠ copy по CDPA). US case MTD 10.02.2026.

## Visual

Сверху assertion 24pt. Центр — split visual: левая половина «UK High Court» (Union Jack subtle background tint) с зелёным маркером «Stability won primary claims (CDPA — weights ≠ copy)» + дата 04.11.2025; правая половина «US case» (subtle US flag tint) с amber маркером «MTD 10.02.2026 — pending» + дата 10.02.2026. Под split — Bird & Bird ruling article screenshot в Ocean rounded box. Внизу — крупный gold «УРОК ДЛЯ ИНЖЕНЕРА»: «Юрисдикции расходятся — то, что legal в UK по CDPA, не legal в US по «добросовестное использование». Для global deployment проверяй обе».

## Speaker notes

Второй кейс по авторскому праву — Getty Images против Stability AI. Это дело иллюстрирует критически важный для инженеров факт: разные юрисдикции выносят разные решения по одному и тому же типу спора. UK High Court ruling четвёртого ноября 2025 года: Stability AI выиграл primary copyright claims. Ключевая правовая логика по UK Copyright, Designs and Patents Act 1988 — CDPA: weights модели не являются «copy» в смысле UK copyright law. Соответственно, обучение модели на изображениях Getty не является нарушением primary copyright по CDPA. Это победа для AI-индустрии в UK. Параллельно идёт US case с motion to dismiss слушаниями десятого февраля 2026 года. US правовой контур принципиально другой: «добросовестное использование» doctrine в Section 107 Copyright Act с four-factor test. Здесь возможен совершенно противоположный исход. Bird and Bird, специализирующаяся на IP law, опубликовала детальный analysis UK ruling, который мы цитируем в материалах лекции. Что эта split юрисдикций означает практически. Урок для инженера: юрисдикции расходятся. То, что legal в UK по CDPA, не legal в US по «добросовестное использование». Для global deployment проверяй обе. Если ты строишь креативный AI продукт для глобального рынка, у тебя должен быть jurisdiction-aware compliance layer: продукт может вести себя по-разному в зависимости от того, где он deployed. Это не теоретическое требование — это уже эмпирический факт 2025-2026 годов. И ещё один важный нюанс. UK win Stability не означает «no risk in UK». Это означает only «primary copyright claims rejected». Secondary claims — например, trademark или passing-off — могут остаться. И права на образ в любой юрисдикции — это отдельный, не-copyright класс правового регулирования. Юрисдикционный split — это не «UK легализовал AI training», а только «UK ruling по конкретному типу claim».
