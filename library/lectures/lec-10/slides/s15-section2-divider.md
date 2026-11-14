---
id: s15
type: section_divider
duration_min: 0.2
assertion: "Раздел 2 — L2 «Робот». Узкая специализация работает (LaserWeeder, Saga UV-C, Tevel); универсальный «autonomous farm robot» — банкротится (Monarch, FarmWise)."
learning_goal: "Visual divider — переход в Р2 + 7-card progress bar с gold-подсветкой Р2"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "frontmatter"
references: []
visual:
  pattern: section_divider_with_progress
  primary: "Большое «2» + title + 1-фраза-фрейм + 7-card progress bar с gold-подсветкой Р2"
---

# Раздел 2. Автономная и роботизированная техника в поле

## Assertion

Раздел 2 — L2 «Робот». Узкая специализация работает (LaserWeeder, Saga UV-C, Tevel); универсальный «autonomous farm robot» — банкротится (Monarch, FarmWise).

## Visual

Слева — огромная цифра «2» outline-стилем (~280pt, Primary light очень светлый). Справа — large title 34pt bold «Раздел 2. Автономная и роботизированная техника в поле» (термин отрасли, заголовком) + 1 фраза-фрейм 18pt italic Primary mid: «L2 «Робот» — узкая специализация работает; универсальный «autonomous farm robot» банкротится» (ярлык лестницы — подзаголовком).

Внизу — progress bar: 7 horizontal cards, текущая (Р2) выделена gold. Caption 12pt italic: «LaserWeeder working case + РФ-параллель CV vs sensor-fusion · 4 working specialization cases · 3 провала (Monarch, FarmWise, strawberry)» — порядок совпадает с фактической последовательностью кадров раздела (s16→s17→s18→s19→s20→s21).

## Speaker notes

Поднимаемся на вторую ступень — L2, уровень автономных машин и роботов. Это semi-controlled environment: машина движется по полю, но её собственная физика — вибрации, GPS-приёмник, датчики препятствий, оптика камеры — даёт частичный контроль над тем, что машина видит и как реагирует. Логически это шаг между первой ступенью полностью открытого поля и третьей ступенью полу-закрытой среды животноводческой фермы.

И здесь проявляется один из главных уроков AgTech 2026 года: специализация побеждает универсальность. Узкие специализированные роботы — LaserWeeder для weeds на конкретных культурах, Saga Robotics Thorvald для UV-C ночной обработки клубники, Tevel Aerobotics для сбора яблок — работают и масштабируются. Универсальные «farm robots» — Monarch MK-V, FarmWise — банкротятся.

В этом разделе мы разберём canonical working case LaserWeeder G2, сразу за ним — критическое сравнение Cognitive Pilot и ИТЭЛМА как архитектурного выбора внутри ИИ-домена, не как «AI vs не-AI». Затем ещё четыре working specialization cases. И завершают раздел три провала: Monarch Tractor с исками 2025-го за «autonomous» при сломанной автономии, FarmWise wind-down плюс Naïo recovery как структурную невозможность generic CV-стека в реальном поле, и затянувшийся pilot phase робота-сборщика клубники.

## Источники

- Chapter v3.1 §2 Часть 1 + Часть 2.
