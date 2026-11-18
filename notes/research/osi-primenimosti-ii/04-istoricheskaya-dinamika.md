---
title: "«Отступающая граница» ИИ — универсальный паттерн или механизм-зависимое движение?"
type: research
issue: "#349"
date: 2026-11-18
---

# Отчёт: «Отступающая граница» ИИ — универсальный паттерн или механизм-зависимое движение?

> **Провенанс.** Полный текст четвёртого из четырёх независимых research-отчётов по issue #349,
> переданный оркестратором вербатим. Этот отчёт вводит мнемонику **U1–U4** (механизмы
> неопределённости, см. [`01-os-neopredelennosti.md`](01-os-neopredelennosti.md)) и **F-A/F-B/F-C**
> (механизмы скорости обратной связи, см. [`02-os-fidbeka.md`](02-os-fidbeka.md)) и классифицирует
> каждый по тому, движется ли он во времени. Раздел «Где я явно подозреваю overreach» сохранён
> полностью, всеми 7 пунктами, без сокращений — он прямое указание задания.

## 1. Rich Sutton, "The Bitter Lesson" (2019)

**Источник:** Sutton, R. (2019). *The Bitter Lesson*.
http://www.incompleteideas.net/IncIdeas/BitterLesson.html.

**Что утверждается буквально:** «The biggest lesson that can be read from 70 years of AI
research is that general methods that leverage computation are ultimately the most effective,
and by a large margin.» Это тезис про **метод**, а не про задачу: *general search + learning,
масштабируемые компьютом*, систематически обходят *hand-crafted human-knowledge-engineering*
методы — не потому что задача стала «проще», а потому что компьют (Moore's Law) растёт
экспоненциально, а человеческое знание — нет.

Исторические примеры: шахматы (Deep Blue, 1997 — massive deep search, не human chess
understanding), Go (после ~20 лет human-knowledge подходов победил масштабированный self-play
search + value function), речевое распознавание (DARPA-конкурсы 1970-х: статистические HMM vs.
human-knowledge фонемные модели — выиграла статистика), computer vision (edge detection/SIFT →
deep learning только на convolution + invariances).

**Важное уточнение:** Sutton **нигде явно не говорит про feedback delay или credit assignment**
как отдельную ось. Его аргумент — про то, *каким методом* решать задачу (built-in knowledge vs.
scalable search/learning), а не про то, *какой тип задачи* принципиально решаем. Bitter Lesson —
это **meta-claim об инженерном методе**, а не прямая теория о природе задачи. Применительно к
механизмам: Bitter Lesson напрямую бьёт только по механизму **(3) current-method engineering
bottleneck** — и ничего не говорит про (1) aleatoric ceiling, (2) non-stationarity, (4) algorithm
aversion, (A) absolute delay, (B) credit-assignment unsolvability, (C) hard-real-time
admissibility.

**Claim об универсальности vs ограничения:** Sutton формулирует это как урок, который снова и
снова *должен* выучиваться и **не выучен до конца**. Он не делает explicit claim о пределах.
**Важно:** Sutton НЕ говорит «со временем compute решит aleatoric-ограниченные задачи» —
присвоение Bitter Lesson статуса «теория универсальной отступающей границы для ЛЮБОЙ
неопределённости» — это overreach, не поддержанный текстом.

**Вывод:** Bitter Lesson поддерживает receding-frontier **только для механизма (3)** engineering
bottleneck, и только в части «метод vs domain knowledge». Молчит про (1),(2),(4),(A),(B),(C).

## 2. AI effect / Tesler's Theorem

**Источники:** Larry Tesler, цит. в McCorduck, P. (1979). *Machines Who Think*. «AI is whatever
hasn't been done yet» (Hofstadter's naming; Tesler's own phrasing: «Intelligence is whatever
machines haven't done yet»). McCorduck (1979) дала паттерну имя **«AI effect»**.

**Релевантность:** прямой социологический конфаунд. Если граница «неопределённости, которую может
взять ИИ» выглядит отступающей частично из-за того, что мы *переопределяем* «настоящую сложную
задачу» каждый раз, когда старая решена (шахматы перестали считаться «тестом интеллекта» после
Deep Blue; OCR перестал считаться ИИ), то наблюдаемое «движение границы» — отчасти артефакт
измерения, а не реальное расширение метода. Это **ортогональный источник шума в самом измерении**
«граница сдвинулась» — любое утверждение «граница Х сдвинулась между 1990 и 2020» нужно очищать
от AI-effect-артефакта, искать *количественные* benchmark-данные, а не нарративные «раньше это
считалось ИИ-хард» утверждения.

## 3. Moravec's Paradox — эрозия: количественные данные

**Источники:** Moravec, H. (1988), *Mind Children* (оригинал); Epoch AI gradient-updates
(нарративный, без цифр); несколько 2024-2026 opinion-piece обзоров.

**Количественные данные (из истории ImageNet/grasping, не Moravec-специфичных источников):**

*Распознавание изображений:* ILSVRC top-5 error: 2010 — ~28%, 2011 — ~26%, **2012 (AlexNet) —
15.3%**, **2015 (ResNet-152) — 3.57%**, ниже человеческого бейзлайна ~5.1% (Karpathy,
самоизмерение, 2014 — важная оговорка: один тренированный человек на этой задаче, не
"человеческое зрение" в общем). За 8 лет: 28.2% → 2.3% error.

*Robotic grasping:* ранние learning-методы (до DL) — успех ~22.5%; CNN на Cornell Grasping
Dataset — 89%; Dex-Net 2.0 — 90%; более свежие методы на неизвестных объектах в сложных условиях:
73% → 93%; GGS-CNN — 96.7%/93.8%; один метод — 98.25%.

Эти цифры — реальное измеримое движение границы в домене, который Moravec называл «трудным для
машин». Но: это controlled-benchmark success rates (известные/заданные объекты, контролируемые
условия), не open-world manipulation.

**Критически важная контр-находка — METR (п.7) напрямую противоречит «парадокс полностью
эродировал»:** METR обнаружили, что time horizon для agentic computer-use задач (OSWorld,
WebArena — требуют визуального восприятия экрана + точных кликов) **в 40–100 РАЗ короче**, чем
для software/math задач, при сопоставимой относительной скорости роста (doubling каждые ~2–6
мес. везде). Причина: «75% failed examples были due to mouse click inaccuracies» —
перцептивно-моторная точность остаётся узким местом даже в 2025 году.

**Вывод:** Moravec's paradox **частично эродировал в абсолютном выражении** (голые числа ошибок
резко упали), **но относительный gap между символьным/языковым и сенсомоторным доменом не
исчез** — он пересчитался в новых единицах (METR time-horizon) и там всё ещё виден 40-100x
множитель. Это аргумент против «универсальной равномерной отступающей границы»: paradox
воспроизводится на новой метрике спустя десятилетия deep learning — структурный, не просто
«метод пока слаб», разрыв между перцептивно-моторной и символьной неопределённостью.

## 4. Dulac-Arnold et al. "Challenges of Real-World RL" — что решено к 2024-2026

**Источники:** Dulac-Arnold, Mankowitz, Hester (2019/2021) — **9 challenges**: (1) sample
efficiency, (2) system delays, (3) high-dimensional spaces, (4) safety constraints, (5) partial
observability/non-stationarity, (6) poorly-specified reward, (7) real-time inference, (8) offline
learning, (9) interpretability.

**Ключевая находка — честный негативный результат:** запрошенный явный 2022-2026 systematic
follow-up/retrospective **не найден**. Нашёлся только non-canonical survey (arxiv 2601.15353,
digital-health-focused), который даже не цитирует Dulac-Arnold по имени. Из этого survey
косвенно:
- **Sample efficiency** — частично отступающая (offline-данные/causal RL/LLM-augmented learning
  как incremental mitigations).
- **Non-stationarity** — явно описана как структурно нерешённая: «changing relationships between
  action, reward, or state variables»; continual-learning решение названо «largely theoretical».
- **Sparse/delayed reward (credit assignment)** — явно нерешённая при длинных горизонтах: «Online
  RL is often challenged by the lack of feedback... when the scientific goal is to optimize a
  long-term or distal outcome»; surrogate/causal reward redesign — паллиатив, не решение.
- **Partial observability** — обходится инженерным костылём (LLM "vetoes"), не решается.

**Вывод:** нет авторитетного систематического аудита 2024-2026. Косвенно: sample efficiency
выглядит receding; **non-stationarity и sparse/delayed credit-assignment при длинных горизонтах
выглядят stuck** — соответствует гипотезе, что механизм (B) sparsity/credit-assignment НЕ
решается ожиданием/новыми методами. Флаг: слабое доказательство (один non-canonical survey,
health-domain bias).

## 5. Distribution-shift robustness: receding или нет?

**Источники:** EarthShift benchmark (arxiv 2605.29330) — geospatial foundation models **на
15-20% хуже** OOD в среднем независимо от архитектуры/масштаба, некоторые FM (SAM, DINO) немного
устойчивее, но «not enough to justify their increased scale and cost»; Tabular foundation models
(arxiv 2607.26000v1) — **не демонстрируют** врождённой устойчивости к distribution shift,
деградация системна; Vision — zero-shot FM генерализуются «significantly better» на
covariate-shift, но без точной количественной сверки; IJCAI 2026 survey — OOD robustness назван
**«primary technical bottleneck»** для trustworthy FM.

**Вывод:** картина смешанная и domain-dependent, явно НЕ универсальное улучшение.
Геопространственные и табличные данные — нет прогресса; vision — позитивный, но не
квантифицированный сигнал. Прямо поддерживает: non-stationarity/distribution-shift (механизм 2)
НЕ универсально расширяется методом, в отличие от Moravec-перцепции, где абсолютные числа
двигались резко.

## 6. Aleatoric noise ceiling / zero-validity environments — time-invariant by construction?

**Источники:** Kahneman (zero-validity environment, из *Thinking, Fast and Slow*, развивая Meehl
1954): stock-pickers «their failures reflect the basic unpredictability of the events that they
try to forecast»; «selection of stocks is more like rolling the dice than like playing poker».
Markets paper (arxiv 2606.08209, *Instrumental Probability, the ℙ–ℚ Wedge, and the Limits of
Learnable Alpha*) — разграничивает истинную случайность и *сложность предсказания*, формально
определяемую через **entropy rate** стационарного процесса; рынки «hardest exactly where
prediction is costly, competitive, unstable, or destroyed by use» — если паттерн найден и
эксплуатируется, он самоуничтожается (reflexivity/arbitrage) — это встроенный в среду механизм, а
не «метод пока слаб». «Beyond Random Walks: Exploring the Learnability Threshold of AI Agents in
Algorithmic Markets» формализует Learnability Threshold — границу, за которой detectable patterns
не дают positive net-of-cost возврата. Lyapunov exponent/chaos: Lyapunov time ограничивает
горизонт предсказания с экспоненциальным ростом ошибки; формальный результат (arxiv 2605.05218,
Horizon-Constrained Rashomon Sets for Chaotic Forecasting) — эффективное множество допустимых
моделей сжимается экспоненциально с lead time со скоростью, заданной максимальным Lyapunov
exponent.

**Моя логика (reasoned through):** zero-validity environment/entropy rate/Lyapunov-limit —
**определительно time-invariant**, если верно специфицированы условия (истинная стационарная
энтропия процесса; истинный chaos с положительным Lyapunov exponent) — никакое улучшение метода в
рамках той же информации не сдвинет предел, потому что предел определён через *отсутствие*
извлекаемой регулярности. Это тавтология концепции, логически устойчивая.

**Критическая оговорка — где это рушится на практике:**
1. **Рынки/reflexivity** — ceiling частично *конструируется деятельностью самих предсказателей*
   (арбитраж уничтожает паттерн) — не чисто природный aleatoric шум, а game-theoretic
   equilibrium-эффект. Правильнее: «рынки = zero-validity *для публично доступной информации и
   широко используемых стратегий*, по построению equilibrium», не «навечно непредсказуемы
   физически».
2. **Погода (п.8)** — классический chaos-ceiling пример, который реально сдвинулся эмпирически
   (GraphCast) — значит "2-week limit" был смесью Lyapunov-limit атмосферы И
   current-method-bottleneck в initial-condition estimation, а не чистый (1).

**Вывод:** есть explicit академическая опора для «некоторые потолки постоянны by construction,
другие — текущие инженерные ограничения», но это синтез из нескольких источников (Kahneman/Meehl
+ entropy-rate markets paper + Lyapunov-horizon formal results), не единая прямая формулировка в
одном источнике — и даже «canonical» chaos-примеры (погода) при разборе оказываются частично
engineering-bottleneck.

## 7. METR / Epoch — общий закон "отступающей границы"

**Источники:** METR, *Measuring AI Ability to Complete Long Software Tasks* (2025-03-19) — time
horizon (длина задачи по человеко-времени на 50% reliability) **doubling каждые ~7 месяцев**
2019-2024. METR, *How Does Time Horizon Vary Across Domains?* (2025-07-14) — **прямой
количественный ответ**:
- Software/math/scientific-QA: 50–200+ минут, doubling каждые 2–6 мес.
- Agentic computer use (OSWorld, WebArena): **в 40–100 раз короче** абсолютный horizon, растёт с
  похожей относительной скоростью.
- Autonomous driving (Tesla FSD): ~0.6 doublings/год (~20-мес. doubling time) — заметно медленнее
  прочих.
- Явная причина отставания computer-use: «75% failed examples были due to mouse click
  inaccuracies».
- Авторские оговорки: «all benchmarks are somewhat artificial», ограниченное покрытие
  occupations, многие benchmarks без human baselines, явный selection bias: evidence «from
  benchmarks in a limited range of domains, especially those that AIs are relatively good at».
- METR собственная заметка «Clarifying limitations of time horizon» (2026-01-22) — сами
  предупреждают не переобобщать метрику.

**Вывод — сильнейшая находка всего отчёта:** METR даёт ровно то количественное измерение
«отступающей границы», которое гипотеза ищет, и оно явно **НЕ однородно по доменам**:
экспоненциальный рост наблюдается везде, но (а) абсолютный уровень различается на 1-2 порядка в
пользу символьных/текстовых доменов, (б) скорость роста тоже неоднородна (driving медленнее).
Прямое количественное подтверждение «не универсальный, а неравномерный, mechanism-dependent»
паттерн.

**Overreach-флаг:** METR benchmark-набор selection-biased в сторону доменов, где AI уже
относительно хорош — домены, где AI совсем не может (пока), возможно не вошли в выборку вообще —
угроза любому выводу «граница движется равномерно экспоненциально везде».

## 8. Контрпримеры: что НЕ сдвинулось за десятилетия

**Погода (не чистый контрпример):** классический "two-week" chaos-limit; новые данные (2025,
arxiv 2504.20238, *Atmospheric Predictability Beyond 30 Days with Machine Learning*) — используя
gradient-based optimization начальных условий с GraphCast, skill up to **27.5 дней**
(statistically significant anomaly correlation до 33 дней), error reduction 86% at day-10.
**Важная оговорка:** cross-model validation с Pangu-Weather дал «significant but considerably
smaller improvements» — часть эффекта model-specific error correction, не чистое улучшение
знания динамики атмосферы. Погода — смесь (1) aleatoric/chaos ceiling и (3) engineering
bottleneck, разделить сложно; не чистая иллюстрация ни для одной стороны.

**Землетрясения (сильный кандидат на «реально не сдвинулось»):** «rupture nucleation at depths
of 5-30 km where direct observation impossible... stress accumulates over decades... combined
with inability to measure deep fault stress with required precision likely renders deterministic
short-term prediction fundamentally impossible» — явная формулировка структурного предела через
(а) принципиальную observability-проблему и (б) chaos. Эмпирически: «in their best performances,
machine learning analyses are about as good as the standard methods of quake forecasting» —
десятилетия ML не дали измеримого улучшения. Более чистый пример aleatoric/physical-observability
ceiling, НЕ замаскированный engineering-bottleneck — сама observability-проблема не зависит от
метода.

**Рынки** — разобрано в п.6: 50 лет ML/статистики не дали устойчивого alpha относительно chance
(с учётом costs), но причина частично reflexivity/arbitrage (game-theoretic, не чисто физический
предел) — более тонкий случай, чем землетрясения.

**Причинный вывод из наблюдательных данных на длинном горизонте** — не нашёл прямого «не
двинулось за 30 лет» с чёткой количественной базой. Честно: этот подпункт остался недоказанным ни
в одну сторону.

## Критический синтез: карта механизмов

| № | Механизм | Движется со временем? | Самое сильное свидетельство | Уверенность |
|---|---|---|---|---|
| U1 | Aleatoric noise ceiling / zero-validity environments | **Не движется**, но границы часто путают с (3) | Землетрясения: ML ≈ традиционные методы спустя десятилетия; markets entropy-rate paper (2606.08209) формально отделяет true unpredictability от hard-to-predict | Средняя-высокая для «чистых» случаев (землетрясения); низкая для смешанных (погода) |
| U2 | Non-stationarity / distribution shift | **Не движется универсально**, domain-dependent | EarthShift (geospatial FM на 15-20% хуже OOD), tabular FM survey, IJCAI 2026 (OOD = "primary technical bottleneck") | Средняя — свидетельство смешанное и свежее |
| U3 | Current-method engineering bottleneck | **Движется, быстро и измеримо** | Bitter Lesson; ImageNet 28%→2.3% за 8 лет; grasping 22.5%→98%; METR doubling 2-7 мес. | Высокая |
| U4 | Algorithm aversion / trust | **Не исследовал в этой сессии** — явный gap покрытия, нужен отдельный проход (Dietvorst et al.) | — | Не оценено |
| F-A | Absolute signal delay | **Движется почти тривиально** — engineering/patience вопрос, слабо затронут напрямую | Косвенно | Низкая эмпирическая, высокая логическая |
| F-B | Sparsity/confounding → credit-assignment unsolvable | **Не движется принципиально при длинных горизонтах и N≈1**; инженерно смягчается при N≫1 goal-conditioned повторах (Hindsight Experience Replay) | Dulac-Arnold-derived survey (2601.15353): sparse/delayed reward при distal outcomes описан как нерешённый | Средняя — единственный прямой источник не canonical |
| F-C | Hard/soft real-time admissibility (binary) | **Не "движется" по определению** — категориальное свойство задачи, не continuum | METR driving-lag как косвенное подтверждение (моя интерпретация, не explicit claim источника) | Средняя — вывод мой, явный флаг |

**Уточнение к строке F-B (добавлено при прожарке, issue #349):** «не движется принципиально»
верно именно для горизонта с N≈1 нерасчленимых повторов и confounded исходом (пример фермера —
один сезон, одна смешанная причина провала/успеха). Для горизонта с N≫1 повторов и
goal-conditioned структурой вознаграждения (симулируемая/дёшево повторяемая среда, цель
выразима как состояние) часть credit assignment инженерно решена — Hindsight Experience Replay
(Andrychowicz et al., 2017, arXiv:1707.01495) и её развития. Полный разбор, какие именно
предпосылки у фермера не выполняются — файл 02 §3, врезка «Контр-пример». См. также
`prozharka.md` Finding 3.

## Где я явно подозреваю overreach (самокритика)

1. **Bitter Lesson используется людьми (не самим Sutton) как универсальный закон «всё решит
   compute+scale», включая aleatoric/credit-assignment случаи.** Текст эссе этого не говорит.
   Нужно явно отделить: Sutton = аргумент про метод (3), не про природу задачи.
2. **Moravec-erosion заявления подкреплены числами из ImageNet/grasping, которые сами по себе не
   являются "Moravec-paradox" измерениями** — approximation, не прямое цитирование кого-то, кто
   явно измерял "эрозию парадокса". Связка моя, не источника.
3. **Землетрясения как "чистый aleatoric ceiling"** — риторически сильный пример, но единственное
   прямое доказательство — одна формулировка (не peer-reviewed консенсус в строгом смысле);
   формулировка содержит hedge-слово "likely". Не выдавать за доказанную теорему.
4. **F-C (hard-real-time = категориальный, не движется)** — моя интерпретация METR driving-lag
   данных, не explicit claim источника. METR не даёт такого объяснения. Корреляция ≠
   подтверждение причины. Самый слабый пункт карты.
5. **Markets-as-reflexive-not-aleatoric разграничение** — моя аналитическая конструкция поверх
   одной статьи (2606.08209); статья не делает ровно то разграничение, которое я ей приписал.
6. **Dulac-Arnold-follow-up тред дал отрицательный результат** (искомого систематического аудита
   не существует) — нельзя путать «использовал ближний суррогат вместо канонического follow-up»
   с «нашёл ответ на вопрос брифа».
7. **Algorithm aversion (U4)** — фактически не исследован в этой сессии, хотя входит в заявленные
   4 механизма неопределённости. Явный пробел покрытия, а не "механизм не движется" — честно
   отметить как неисследованное.

## Главный вывод

Паттерн **не универсальный**: метод-зависимые узкие места (U3) двигаются быстро и измеримо;
структурные узкие места, завязанные на observability/aleatoric-физику (U1, землетрясения) и на
distal credit-assignment при длинных горизонтах (F-B) — не двигаются сопоставимо, несмотря на
смену эпох метода; non-stationarity (U2) даёт смешанную, явно не решённую картину даже в 2024-2026
обзорах. Лучшее количественное доказательство неравномерности — METR cross-domain time-horizon:
экспоненциальный рост почти везде, но абсолютный уровень различается на 1-2 порядка между
символьными и перцептивно-моторными доменами, и это расхождение воспроизводится спустя 13 лет
deep learning после "ImageNet moment" — персистентная структура, не временный разрыв на старте
новой парадигмы.
