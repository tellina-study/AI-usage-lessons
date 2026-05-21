---
id: s34
type: assertion_visual
duration_min: 3
assertion: "Хуситы, Красное море, конец 2023 года. За 2 месяца контейнерный трафик упал на 90 процентов. Это область, в которой ML слеп по определению."
learning_goal: "Houthi crisis + Cape of Good Hope rerouting + ML out-of-distribution"
learning_outcomes: [LO2, LO7]
chapter_ref: "§4.1 — Houthi Red Sea 2024"
failure_bucket: strict_in
references: [atlas-institute-red-sea, jpmorgan-red-sea]
visual:
  pattern: timeline_with_chart_and_map
  primary: "Hero photo: контейнеровоз в Красном море/Cape rerouting map. Внизу — chart 90% drop + 30% time увеличение"
  acquisition_tiers:
    - "Tier 2: Wikipedia Commons «Red Sea crisis»"
    - "Tier 6: Reuters / AP photos"
---

# Хуситы в Красном море: ML слеп по определению

## Цифры

- **Декабрь 2023 — атаки начались.** Houthi движение Йемена, координированное с региональной геополитической ситуацией.
- **К февралю 2024:** контейнерный трафик через Красное море **упал на 90%** (US DIA).
- **Daily transit trading volume:** 4 миллиона метрических тонн → 1,7 миллиона метрических тонн (**−57,5%**).
- **Прежде через Red Sea:** ~15% мировой морской торговли + ~30% global container traffic.
- **+30% transit time** Asia-Europe маршрутами через Cape of Good Hope.
- **−9% effective global container capacity** (J.P. Morgan).

## Что произошло технически

- **ML demand forecast полностью out-of-distribution.** Модели, обученные на 2018-2023 данных, не имели никакого signal про Houthi disruption.
- **Шиппинг-rates вырос в 3-5 раз** на Asia-Europe маршрутах за 2 месяца.
- **Просто-в-срок (JIT) supply chains broke** — компании, optimized на minimum inventory, оказались в shortage.
- **Resilient survivors:** компании с redundancy + multi-source supply + scenario planning капабельностью.

## Что НЕ работало

- **AI demand forecast** — полностью out-of-distribution.
- **Optimization solvers** — нет данных о new transit times для recalibration.
- **Real-time tracking** — данные есть, но это symptom, не cause.

## Что РАБОТАЛО

- **Human dispatchers** в exception-teams Maersk, MSC, CMA CGM, Hapag-Lloyd — реальное rerouting decisions.
- **Scenario planning** — компании с pre-built сценариями (включая Houthi-type scenarios) могли быстро respond.
- **OR с manual override** — Gurobi/OR-Tools recalibrated с новыми ETAs.

## Speaker notes

Хуситы в Красном море — это canonical black-swan example для логистики 2020-х годов. Я хочу остановиться на этом кейсе три минуты, потому что он показывает фундаментальную ограниченность ML в логистике.

Что произошло. Хуситы — движение из Йемена — начали атаковать контейнеровозы в Красном море в конце ноября 2023 года, после геополитических событий региона. К февралю 2024 года, за два месяца, контейнерный трафик через Красное море упал на девяносто процентов.

Числа. Daily transit trading volume — четыре миллиона метрических тонн до crisis, один и семь десятых миллиона после. Минус пятьдесят семь с половиной процентов. Прежде через Red Sea шло около пятнадцати процентов мировой морской торговли и около тридцати процентов global container traffic. Шиппинг компании rerouting на Cape of Good Hope добавляет тридцать процентов transit time для Asia-Europe маршрутов. J.P. Morgan оценил снижение effective global container capacity на девять процентов.

Что произошло технически в ML domain. Demand forecast модели, обученные на данных 2018-2023, не имели никакого signal про Houthi disruption. Это не была bias или mis-calibration — это была complete distribution shift. Модель не «была обучена плохо» — она была обучена на distribution, которое перестало существовать.

Шиппинг-rates вырос в три-пять раз на Asia-Europe маршрутах за два месяца. Just-in-time supply chains broke. Компании, optimized на minimum inventory — например, retailers с zero-buffer на seasonal items — оказались в shortage.

Resilient survivors были компаниями с redundancy. Multi-source supply, не single supplier. Scenario planning капабельностью — pre-built сценариев для major disruption.

Что НЕ работало в этой crisis. ML demand forecast полностью out-of-distribution. Optimization solvers — нет данных о новых transit times для recalibration на первой неделе. Real-time tracking данных хватало, но это symptom, не cause — мы видели где корабли, но не могли predict где должны быть.

Что РАБОТАЛО. Человеческие диспетчеры в exception-командах Maersk, MSC, CMA CGM, Hapag-Lloyd. Реальное rerouting decisions делали люди, не модели. И scenario planning — компании, у которых были pre-built сценарии для major Red Sea disruption (на случай Iran-related или other geopolitical events), могли быстро respond. И OR с manual override — Gurobi и OR-Tools recalibrated с новыми ETAs от human dispatchers.

Lesson — главный pedagogical point. ML по определению слеп на out-of-distribution событиях. Это не «AI плохо обучена» — это структурная характеристика любого supervised ML. На уровне пять лестницы среды правильные инструменты — это human dispatchers + scenario planning + OR. Не ML.
