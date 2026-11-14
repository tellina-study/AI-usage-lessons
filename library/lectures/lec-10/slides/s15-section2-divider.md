---
id: s15
type: section_divider
duration_min: 0.2
assertion: "Раздел 2 — L2 «Робот». Узкая специализация работает (LaserWeeder, Saga UV-C, Tevel); универсальный «autonomous farm robot» — банкротится (Monarch, FarmWise)."
learning_goal: "Visual divider — переход в Р2 + 7-card progress bar с gold-подсветкой Р2"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "frontmatter"
references: [deere-autonomous-tractor-2026]
visual:
  pattern: section_divider_with_progress
  primary: "Уменьшенное «2» + photo-card (John Deere 9RX, автономный трактор, Tier 1 og:image deere.com) + title + 1-фраза-фрейм + 7-card progress bar с gold-подсветкой Р2"
---

# Раздел 2. Автономная и роботизированная техника в поле

## Assertion

Раздел 2 — L2 «Робот». Узкая специализация работает (LaserWeeder, Saga UV-C, Tevel); универсальный «autonomous farm robot» — банкротится (Monarch, FarmWise).

## Visual

Слева — уменьшенная цифра «2» outline-стилем (~220pt, Primary light очень светлый), под ней — фото-карточка в Ocean rounded box: John Deere 9RX 640 с прицепным орудием в поле (автономный режим), боковой ракурс, съёмка днём (Tier 1 og:image, deere.com/autonomous-tractor); caption 8.5pt italic под фото: «John Deere 9RX — автономный трактор. Источник: deere.com». Справа — large title 34pt bold «Раздел 2. Автономная и роботизированная техника в поле» (термин отрасли, заголовком) + 1 фраза-фрейм 18pt italic Primary mid: «L2 «Робот» — узкая специализация работает; универсальный «autonomous farm robot» банкротится» (ярлык лестницы — подзаголовком).

Внизу — progress bar: 7 horizontal cards, текущая (Р2) выделена gold. Caption 12pt italic: «LaserWeeder working case + РФ-параллель CV vs sensor-fusion · 4 working specialization cases · 3 провала (Monarch, FarmWise, strawberry)» — порядок совпадает с фактической последовательностью кадров раздела (s16→s16b→s16a→s17→s18→s19→s20→s21; s16b — инженерная структура vs ИИ-часть LaserWeeder, добавлен issue #340).

## Speaker notes

Поднимаемся на вторую ступень — L2, уровень автономных машин и роботов. Это semi-controlled environment: машина движется по полю, но её собственная физика — вибрации, GPS-приёмник, датчики препятствий, оптика камеры — даёт частичный контроль над тем, что машина видит и как реагирует. Логически это шаг между первой ступенью полностью открытого поля и третьей ступенью полу-закрытой среды животноводческой фермы.

И здесь проявляется один из главных уроков AgTech 2026 года: специализация побеждает универсальность. Узкие специализированные роботы — LaserWeeder для weeds на конкретных культурах, Saga Robotics Thorvald для UV-C ночной обработки клубники, Tevel Aerobotics для сбора яблок — работают и масштабируются. Универсальные «farm robots» — Monarch MK-V, FarmWise — банкротятся.

В этом разделе мы разберём canonical working case LaserWeeder G2 — сначала как состоявшийся кейс с деньгами и акрами, потом отдельно механику штанги и модель распознавания сорняков внутри неё, и только после этого цену её ошибок против классических режимов. Сразу за ним — критическое сравнение Cognitive Pilot и ИТЭЛМА как архитектурного выбора внутри ИИ-домена, не как «AI vs не-AI». Затем ещё четыре working specialization cases. И завершают раздел три провала: Monarch Tractor с исками 2025-го за «autonomous» при сломанной автономии, FarmWise wind-down плюс Naïo recovery как структурную невозможность generic CV-стека в реальном поле, и затянувшийся pilot phase робота-сборщика клубники.

## Источники

- Chapter v3.1 §2 Часть 1 + Часть 2.
- John Deere, страница autonomous-tractor (deere.com/en-us/products-solutions/tractors/autonomous-tractor) — фото 9RX 640, issue #340.
