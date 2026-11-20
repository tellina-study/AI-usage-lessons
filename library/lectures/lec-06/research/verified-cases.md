---
title: "Внешне верифицированные кейсы — Лекция 6 (cad-cam) — копия для discoverability"
source: "notes/research/osi-primenimosti-ii/verified-cases/lec-06-verified.md"
issue: "#349"
status: research-backup, not-reviewed
date_copied: 2026-11-20
---

> **Происхождение.** Это внешне верифицированное свидетельство реальных кейсов (деплойменты/
> исследования с явным исходом, метрикой, датой и именованным инструментом, 2018–2026),
> собранное в рамках research-задачи issue #349 (`notes/research/osi-primenimosti-ii/`).
> Это дополнительный справочный материал для deep-dive главы / backup для Q&A / самостоятельного
> изучения — **не методическая критика и не fact-check лекционного контента**: не прошло ревью
> `methodology-critic` или `fact-checker` как материал лекции, и **не заменяет собственные кейсы
> главы**, если только человек-редактор не решит сознательно включить конкретный кейс в
> `chapter.md`.
>
> Копия ниже — точная (verbatim) копия
> `notes/research/osi-primenimosti-ii/verified-cases/lec-06-verified.md` для обнаруживаемости из
> папки лекции; каноническая версия и её история — в `notes/research/`.

---

---
title: "Лекция 6 (cad-cam) — независимо верифицированные кейсы, внешние по отношению к материалу лекции"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 6 — индустрия `cad-cam`: верифицированные кейсы (не из лекции)

## Подход к поиску

Поиск вёлся через `WebSearch`/`WebFetch` отдельно от материала `library/lectures/lec-06/chapter.md`
и от уже существующих 27 строк `L06-001`…`L06-027` реестра (`reestr-reshenij.csv`) — ни один
кейс ниже не повторяет уже размеченный там (проверено построчно по `case_name`). Стратегия:
(1) широкий поиск по «generative design / CAM-оптимизация / AI в инженерном проектировании» с
фильтром на реальные компании и опубликованные метрики; (2) целевой поиск академических
бенчмарков text-to-CAD / CAD-generation за 2022–2026; (3) целевой поиск документированных
провалов/ограничений (критика индустрии, академические негативные результаты, банкротства).
**Бюджет `WebSearch` закончился в середине работы** (лимит сессии общий на все параллельные
исследовательские сессии); вторая половина поиска сделана только через `WebFetch` по URL,
найденным до этого момента, плюс прямые догадки по доменам (arXiv abstract-страницы, Wikipedia).
Это сузило охват относительно первой половины: многие перспективные зацепки (ResearchGate,
MDPI, PMC, несколько корпоративных блогов) **вернули 403/CAPTCHA и не были перепроверены** —
такие зацепки исключены из таблицы, а не включены на веру.

**Важная находка процесса, а не результата.** Минимум три кандидата, звучавшие как реальные
кейсы («Vanguard Machining» — аэрокосмический суб-поставщик, AI-CAM на 5-осевых станках, −30%
цикл/+40% к стойкости инструмента; типовой «CNC-цех» с titanium-деталями), при прямой проверке
через `WebFetch` оказались **иллюстративными/вымышленными примерами маркетингового блога**, а не
документированными развёртываниями — их источники сами не утверждают, что это реальная компания.
Они **намеренно не включены** в таблицу ниже, хотя превосходно подошли бы по метрикам — это
ровно тот тип «кейса из пальца», который правило курса запрещает.

## Покрытие по годам

Все 5 лет (2022–2026) покрыты минимум одним кейсом в каждой из двух групп:

| Год | Успех | Провал/неуспех |
|---|---|---|
| 2022 | Aston Martin DBR22 (DAPS) · ScienceDirect topology-opt (оценка по PII) | Engineering.com критика generative design |
| 2023 | nTop NASA EXCITE bracket · Divergent 3D/Czinger 21C (DAPS) | Negative-Data Generative Models (ship hull) |
| 2024 | Bugatti Tourbillon (DAPS) · Hexagon Esprit Edge | CAD-Prompted Generative Models (feasibility/novelty tradeoff) · Mercedes-AMG DAPS (оценка года) |
| 2025 | — (см. ограничение ниже) | Design Fixation in GenAI · Desktop Metal Chapter 11 · Knowledge-Guided AI Inverse Design |
| 2026 | Predictive Prototyping (GPT-RAG) · KAN manufacturability · STEP-LLM | Text2CAD-Bench · MUSE Benchmark · Self-Improving CAD Agents |

**Честный пробел: 2025 для успешной группы.** Несмотря на отдельный целевой поиск, устойчивого
2025-датированного успешного развёртывания (не исследовательской статьи с неоднозначным
результатом) не найдено в доступном окне поиска — несколько кандидатов (3D Systems/Oqton,
nTop-кейсы) либо не подтвердились по дате, либо оказались заблокированы для перепроверки.
Это не означает «в 2025 успехов не было» — означает, что в рамках этого бюджета поиска такой
кейс не был найден и не был натянут искусственно.

## Честная оценка качества источников

- **Высокое качество (прямая первичная проверка через `WebFetch`):** nTop NASA EXCITE bracket,
  Divergent 3D/Czinger (прямые цитаты Kevin Czinger, Yale News), все 7 arXiv-кейсов (Text2CAD-
  Bench, MUSE, Self-Improving CAD Agents, Design Fixation, Negative-Data Generative Models,
  CAD-Prompted Generative Models, Predictive Prototyping, KAN, STEP-LLM), Desktop Metal
  (Wikipedia, фактологически консервативный источник для корпоративных дат).
- **Среднее качество (сниппет поисковика с цитатой, прямой fetch источника заблокирован 403):**
  Hexagon Esprit Edge (mmsonline.com), ScienceDirect topology-opt 2022, Monolith AI (vehicle-
  dynamics-international.com, клиент не назван).
  Qualitative для:  Engineering.com критика (именной автор и дата, но сама статья — качественная
  критика без цифр).
- **Низкое качество / повышенный риск (оставлено с явным флагом, не удалено):** MIT D-Lab
  bracket (единственный источник — блог-агрегатор `graftconcepts.com`, первичную публикацию MIT
  D-Lab найти и перепроверить не удалось из-за исчерпания `WebSearch`-бюджета); Mercedes-AMG DAPS
  (упомянуто внутри статьи Newsweek без даты, год — оценка по контексту).
- **Общее ограничение метода:** почти все «успешные» индустриальные кейсы (Divergent/Czinger,
  Bugatti, Aston Martin, Hexagon) идут из пресс-дружественных источников (интервью с основателем,
  трейд-пресса, пресс-релиз вендора) без независимого аудита — тот же паттерн смещения, что курс
  уже фиксировал для лекций 5/8/10/13 в `reestr-reshenij-README.md` п.3. Контрастно к этому —
  академические провалы (arXiv) заметно более строгие и воспроизводимые источники, чем
  академические/индустриальные успехи — асимметрия качества источника сама по себе интересный
  сигнал: в CAD/CAM отрасли задокументированные ограничения методов (benchmarks) методологически
  сильнее, чем задокументированные победы (press releases).

## Таблица кейсов

| case_name | year | source_url | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nTop NASA EXCITE bracket (Field Optimization) | 2023 | https://www.ntop.com/resources/blog/optimizing-the-mass-and-natural-frequency-of-the-nasa-excite-bracket-with-field-optimization/ | low | none | weeks-months | none | hybrid | yes | medium | not-applicable | success | high | +26% первая собственная частота при +1,5% массы vs лучшая альтернатива; гибрид классической topology optimization + генеративного shell/lattice |
| Divergent 3D / Czinger 21C (DAPS) | 2023 | https://news.yale.edu/2023/07/24/czingers-disrupt-manufacturing-top-speeds | low | none | weeks-months | none | hybrid | yes | high | not-applicable | success | medium | Czinger: «20–40% массы убрано» нейросетевой/ML-оптимизацией; серийный гиперкар, но источник — интервью основателя, не независимый аудит |
| Bugatti Tourbillon — шасси/подвеска через DAPS | 2024 | https://www.newsweek.com/next-great-supercar-might-3d-printed-1943183 | low | none | weeks-months | none | hybrid | yes | high | not-applicable | success | medium | Серийный гиперкар (представлен июнь 2024); та же DAPS-платформа, что у Czinger; дата публикации самой статьи не указана явно |
| Aston Martin DBR22 — задний подрам через DAPS | 2022 | https://www.newsweek.com/next-great-supercar-might-3d-printed-1943183 | low | none | weeks-months | none | hybrid | yes | medium | not-applicable | success | medium | DBR22 представлен авг. 2022 (Monterey Car Week); 3D-печать через DAPS, ограниченная серия |
| Hexagon Esprit Edge — AI-CAM программирование (IMTS 2024) | 2024 | https://www.mmsonline.com/products/hexagons-ai-powered-manufacturing-solution-reduces-programming-times | low | none | hours-days | none | classical-ml | no | low | not-applicable | success | medium | Заявлено −75% времени программирования за счёт анализа истории реза; прямой fetch источника заблокирован (403), данные — из сниппета поисковика |
| Topology optimization aerospace part (ScienceDirect) | 2022 | https://www.sciencedirect.com/science/article/abs/pii/S2214785322006460 | low | none | hours-days | none | rule-based | yes | high | not-applicable | success | medium | ~20% снижения массы при сохранении деформации под нагрузкой; год оценён по номеру PII статьи (прямой fetch — 403, не перепроверено напрямую) |
| Monolith AI — автомобильный клиент (трек-тесты) | 2023 | https://www.vehicledynamicsinternational.com/news/simulation/an-ai-system-to-slash-development-times-and-costs.html | low | none | seconds-minutes | none | deep-learning | unclear | medium | not-applicable | success | low | −70% времени трек-тестов, −50% стоимости по заявлению источника; клиент не назван, год — не указан явно в источнике (оценка) |
| Predictive Prototyping — оценка дизайн-концептов с GPT-RAG | 2026 | https://arxiv.org/abs/2601.12276 | low | none | seconds-minutes | none | foundation-model | unclear | low | not-applicable | success | high | GPT-RAG точнее оценивает стоимость/performance, чем индивидуальные и краудсорс-человеческие оценки; прототип на основе GPT превзошёл и коммерческий, и topology-optimized baseline |
| KAN-based manufacturability assessment | 2026 | https://arxiv.org/abs/2601.06334 | low | none | seconds-minutes | none | deep-learning | yes | low | not-applicable | success | high | AUC 0,99/0,98/0,94 (drilling/milling/комбинированно) — превосходит 14 ML-бейзлайнов; принято в IEEE Access т.14 (2026) |
| STEP-LLM — генерация CAD STEP из текста | 2026 | https://arxiv.org/abs/2601.12641 | low | none | seconds-minutes | none | foundation-model | not-applicable | low | not-applicable | success | low | «Устойчивый прирост» над бейзлайном Text2CAD (RAG+реструктуризация+RL); точные числа недоступны в абстракте — направление положительное, величина не подтверждена |
| Text2CAD-Bench — invalidity rate по сложности | 2026 | https://arxiv.org/abs/2605.18430 | low | U3 | seconds-minutes | none | foundation-model | not-applicable | low | no | failure | high | Доля невалидных моделей растёт с ~15% до 70–90% при росте сложности геометрии/топологии — метод, не неопределённость задачи |
| MUSE Benchmark (manufacturable/functional/assemblable text-to-CAD) | 2026 | https://benchmarklist.com/benchmarks/muse_benchmarking_manufacturable_functional_and_assemblable_text_to_cad_generation/ | low | U3 | seconds-minutes | none | foundation-model | not-applicable | low | no | failure | high | Лучшая закрытая модель (GPT-5.5) — 67,14% итогового балла; лучшая открытая (GLM-5.1) — 24,06%; оба далеки от production-ready |
| Self-Improving CAD Generation Agents — baseline без FEA-фидбека | 2026 | https://arxiv.org/abs/2605.17448 | low | U3 | hours-days | F-B | agentic-llm | not-applicable | low | no | failure | high | Codex (GPT-5.5) и Claude Code (Opus-4.7) без FEA-петли не производят ни одного строго проходящего артефакта; лучшая конфигурация — ~20% соответствия требованиям |
| Understanding Design Fixation in GenAI | 2025 | https://arxiv.org/abs/2502.05870 | unclear | U3 | unclear | none | foundation-model | not-applicable | low | no | partial | medium | GenAI-инструменты воспроизводят эффект фиксации дизайна (сужение к знакомым решениям), снижая новизну/разнообразие — как и у людей, но без компенсирующих механизмов человеческого брейнсторминга |
| Negative-Data Generative Models — baseline GAN (ship hull) | 2023 | https://arxiv.org/abs/2306.15166 | low | U3 | seconds-minutes | none | deep-learning | not-applicable | unclear | no | failure | high | Ванильная GAN, обученная на 30k валидных корпусов судна, даёт лишь 6% валидных результатов (94% нарушают гидродинамические ограничения) без метода negative-data |
| Desktop Metal — банкротство Live Parts/Live Suite (Chapter 11) | 2025 | https://en.wikipedia.org/wiki/Desktop_Metal | low | none | season-years | none | hybrid | not-applicable | medium | yes | failure | high | AI-генеративное ПО (Live Parts, морфогенетические алгоритмы) само по себе не провалилось технически; компания обанкротилась (июль 2025) после срыва слияния со Stratasys (2023) и последующей продажи Nano Dimension — чистый внешний/бизнес-драйвер, не отказ метода |
| CAD-Prompted Generative Models — feasibility/novelty tradeoff | 2024 | https://arxiv.org/abs/2407.08675 | low | U3 | seconds-minutes | none | deep-learning | not-applicable | low | no | partial | medium | При низком весе CAD-подсказки (~0,35) feasibility растёт без потери новизны, но общий паттерн — устойчивый tradeoff: выше feasibility обычно означает ниже новизну |
| Engineering.com — критика «отвеченного инженером» generative design | 2022 | https://www.engineering.com/an-engineers-answer-to-generative-design/ | unclear | unclear | unclear | unclear | rule-based | unclear | unclear | no | failure | medium | Названный автор (Roopinder Tara), именные примеры (включая известный GM-кронштейн) как «непроизводимые при требуемом объёме», «оптимизированы под один случай нагрузки, разрушаются при обратной» — качественная, не числовая критика |
| MIT D-Lab bracket redesign — «35% ускорение» при явных условиях | 2026 | https://graftconcepts.com/blog/generative-design-35-speedup-only-under-right-conditions.php | low | none | hours-days | none | rule-based | no | low | no | partial | low | 14ч против 21,5ч ручного проектирования — но источник сам указывает, что выигрыш дала автоматизация GD&T-разметки ограничений, а не генеративный алгоритм как таковой; единственный источник — агрегатор-блог, первичную публикацию MIT D-Lab не нашли/не перепроверили |
| Mercedes-AMG — компоненты DAPS, не допущенные в серию | 2024 | https://www.newsweek.com/next-great-supercar-might-3d-printed-1943183 | low | none | season-years | none | hybrid | yes | high | not-applicable | undetermined | low | Статья прямо цитирует: компания «пока не использовала детали Divergent в серийном автомобиле» — проект идёт, исход не решён; год статьи не указан явно, оценка по контексту (Tourbillon как «готовящийся») |
| Toward Knowledge-Guided AI for Inverse Design in Manufacturing | 2025 | https://arxiv.org/abs/2506.00056 | moderate | U3 | unclear | none | deep-learning | not-applicable | unclear | no | partial | medium | Перспективная статья: чисто data-driven (black-box) подходы «часто не справляются» в реальных производственных условиях — разреженные данные, высокая размерность, сложные ограничения; качественный, не единично-кейсовый вывод |

## Явные противоречия/нюансы для рамки курса

1. **Контрпример к «гейт — сильнейший предиктор».** Hexagon Esprit Edge и Monolith AI —
   успешные кейсы **без** явного гейта (`axis4_gate=no/unclear`), в то время как несколько
   успешных академических кейсов (Predictive Prototyping, STEP-LLM, KAN) идут в исследовательском
   контексте с `axis4_gate=not-applicable/unclear`, но тоже успешны. Это не опровергает находку
   файла 10 (96,4% провалов корпуса — без гейта), но показывает, что **присутствие гейта не
   обязательно для успеха** — оно коррелирует с низким blast radius провала, а не гарантирует
   исход напрямую.
2. **Асимметрия качества источника между успехом и провалом — новый, не покрытый ранее сигнал.**
   В этой отрасли задокументированные **провалы/ограничения методов** идут из рецензируемых или
   preprint-академических источников с воспроизводимыми числами (Text2CAD-Bench, MUSE,
   Negative-Data GAN), тогда как задокументированные **успехи** — почти исключительно из
   пресс-дружественных источников (интервью основателя, трейд-пресса вендора) без независимого
   аудита. Если эта асимметрия систематична по всему корпусу — это означает, что доля `success`
   в реестре может быть смещена вверх самим характером того, что попадает в публичные источники
   («провалы» в CAD/CAM отрасли публикуются как наука, «успехи» — как маркетинг).
3. **Desktop Metal — чистый `external_driver=yes` кейс**, ровно того типа, что рамка курса уже
   выделяет отдельно: AI-технология (Live Parts) не была технически дискредитирована в найденных
   источниках — компания обанкротилась из-за срыва слияния и рыночных условий. Хороший пример,
   что «провал ИИ-продукта» и «провал ИИ-метода» — разные вещи, которые легко спутать при
   поверхностном чтении новостного заголовка.
4. **Self-Improving CAD Generation Agents — прямое подтверждение «разрыва надёжности
   foundation-model/agentic-llm».** 0% строго проходящих артефактов на первой попытке без
   FEA-петли — один из самых резких зафиксированных чисел во всём корпусе этого исследования,
   согласуется с «agentic-llm/foundation-model хуже по надёжности» выводом из `00-rezyume.md`.

---

## Связанные канонические файлы исследования (issue #349)

- `notes/research/osi-primenimosti-ii/reestr-reshenij-verified.csv` — сводный CSV 248 внешне
  верифицированных кейсов по всем 12 лекциям.
- `notes/research/osi-primenimosti-ii/reestr-reshenij-verified-README.md` — README к нему.
- `notes/research/osi-primenimosti-ii/reestr-reshenij.csv` + `reestr-reshenij-README.md` —
  исходный канонический реестр 421 кейса из материалов самого курса (issue #349).
