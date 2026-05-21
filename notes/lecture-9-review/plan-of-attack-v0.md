# Лекция 9 — Plan-of-attack v0 + ROAST

**Issue:** #118
**Worktree:** `/tmp/lec-09-wt`
**Branch:** `issue-118-lec-09-aerospace-defense`
**Дата:** 2026-05-20
**Статус:** до USER GATE A (chapter), нужен scope-sign-off

---

## 1. Зафиксированный scope (из Q&A 2026-05-20)

| Вопрос | Решение |
|---|---|
| Региональный фокус | **Глобальный + российский** (симметрично lec-07 FDA+mosmed.ai). Российский слой — Роскосмос (геопространство), отеч. БПЛА, оборонка по открытым источникам. |
| LAWS / летальное автономное оружие | **Ключевой failure-блок.** UN GGE, Maven walkout 2018, IDF Lavender 2024 (если подтверждено), human-in-the-loop как инженерный паттерн, провалы автономного targeting. |
| ≥50% media | **Осмысленное медиа** = реальные фото (спутник/самолёт/дрон), сгенерированные диаграммы, графики QuickChart, mermaid-схемы, скриншоты. Иконки в boxes НЕ считаются. ~32-35 слайдов → ≥16-18 media-rich. |
| Темп старта | Phase 0 запущен в background. |

---

## 2. Phase map (11 фаз + 3 USER GATEs)

| # | Phase | Owner-agent | Async? | Гейт |
|---|---|---|---|---|
| 0 | Research brief (5 файлов) | general-purpose (WebSearch) | **bg** | — |
| 1 | Plan critique | methodology-critic + reader-text-only | par | — |
| 2 | Chapter draft | book-editor | seq | — |
| 3 | Chapter critique | methodology + fact-checker + reader-text | par | — |
| 4 | Chapter revision | book-editor | seq | — |
| 4.5 | Pre-gate (chapter) | orchestrator (self) | — | — |
| — | **USER GATE A** | пользователь | — | ✋ |
| 5 | Slides draft from chapter | presentation-designer | seq | — |
| 6 | Visual loop (≥3 iter/слайд) | presentation-designer | seq | — |
| 7 | Slides QA | pres-critic + student-sim + reader-rendered + consistency + fact-checker | par×5 | — |
| 8 | Slides revision | presentation-designer | seq | — |
| 8.5 | Pre-gate (slides) | orchestrator (self) | — | — |
| — | **USER GATE B** | пользователь | — | ✋ |
| 9 | Speech draft | speech-writer | seq | — |
| 10 | Speech critique | methodology + fact-checker + consistency | par | — |
| 11 | Speech revision + manifest update | speech-writer + orchestrator | seq | — |
| 11.5 | Pre-gate (final) | orchestrator (self) | — | — |
| — | **USER GATE C** | пользователь | — | ✋ |

---

## 3. Несущая ось — 3 кандидата (финал после Phase 0)

**Опция А: «Sensor → Decision → Action» (OODA-loop)**
- Pros: классическая военная инженерная модель, знакома Bauman-аудитории, естественно ложатся sensor fusion / ATR / autonomy / kinetic action.
- Cons: жёстко-военная, гражданская авиация и космос «прижимаются» к решающему контуру неестественно.

**Опция Б: «Уровни автономии» (L0-L5 как в авто, но для аэрокосмоса)**
- Pros: педагогически чистая лестница, прямо ведёт к LAWS-вопросу и human-in-the-loop, легко мапятся провалы (низкая автономия — ALIS false positives, средняя — Lavender targeting controversy, высокая — Patriot friendly fire).
- Cons: требует точного определения уровней для аэрокосмоса (нет общепринятой шкалы как у SAE для авто).

**Опция В: «Гражданское ↔ оборонное dual-use»**
- Pros: важная этическая рамка, естественно интегрирует Maven walkout, спутниковые снимки (Maxar Ukraine 2022), DJI как gray-zone.
- Cons: легко скатиться в политику, размывается технический фокус, сложнее для критики «здесь AI не нужен».

**Рекомендация (предварительная):** **Опция Б**. Самая педагогически сильная, поддерживает курсовую миссию «учить говорить нет неподходящему ИИ», keystone-слайд в Разделе 0 = «лестница автономии» — даёт сквозную ось на 75 минут. Финал — после прочтения `05-narrative-options.md` из Phase 0.

---

## 4. Failure / judgment budget (ENFORCED ≥30% strict-in)

Цена пропуска (Лекция 4 = ~5 циклов deck-revision) известна. Зашиваю в план ДО Phase 1:

| Артефакт | Бюджет strict-in | Носители |
|---|---|---|
| chapter.md (~10-12k слов) | **≥3000-3600 слов** в обозначенных Failure/Limit/Alternative секциях | Раздел про LAWS + раздел про ALIS/ODIN + раздел про автономии-провалы + критерии «здесь AI не нужен» в каждом доменном разделе |
| slides (~32-35) | **≥10-12 слайдов** полностью in-bucket | F-35 ALIS fiasco, Boeing MCAS automation lesson, Maven walkout, GPS spoofing RQ-170, ATR adversarial, Patriot friendly fire, Lavender controversy (если подтверждённый источник), UN GGE map, human-in-the-loop pattern, «когда не AI» критерии |
| speech.md (~5k слов) | **≥1500 слов** в failure-арках | Открытие через провал, явный «выученный урок» в каждой технической секции, критерии-блок |

**Counter-check:** если на Phase 7 facto-проверке доля окажется <30% strict-in либо сконцентрирована в одном артефакте — verdict REVISE, не APPROVE-WITH-POLISH.

---

## 5. Media budget (≥50% слайдов с осмысленным медиа)

Operationalization для presentation-designer brief на Phase 5:

| Категория медиа | Засчитывается? | Примеры для lec-09 |
|---|---|---|
| Реальная фотография (Wikimedia/NASA/Unsplash/CC) | ✅ | Спутник Maxar, F-35, Lancet БПЛА, NASA satellite imagery, drone footage screenshot |
| Сгенерированная диаграмма (mermaid/drawio) | ✅ | OODA-loop, sensor fusion архитектура, supply chain map, LAWS taxonomy |
| График / chart (QuickChart) | ✅ | F-35 ALIS false-positive rate, drone production timeline 2020-2026, satellite launches/year |
| Real-world скриншот UI/панели | ✅ | Anduril Lattice, Palantir Gotham (если public), SDA tracking map |
| Визуальный кейс (BEFORE/AFTER object detection) | ✅ | ATR на спутниковом снимке, медицинский imagery analogue |
| Стилизованная иконка в rounded box | ❌ | Lucide/Heroicons как декорация — не считается |
| Только текст + bullets | ❌ | — |
| Только Ocean-rounded-box без media | ❌ | — |

**Target:** 18-20 media-rich слайдов из ~32 общих → 56-62%. Запас выше 50% компенсирует риск, что 1-2 media не пройдут лицензионную проверку.

**Pipeline:**
1. Phase 5 — designer составляет media-shopping-list для каждого in-scope слайда ДО рендера.
2. Phase 6 visual loop — каждый media-слайд проходит лицензионную проверку (Wikimedia/CC-only приоритет, NASA public domain, гос.источники открытые) перед finalize.
3. Phase 7 — pres-critic + reader-rendered явно verify media-share и качество media-vs-text баланса.
4. Phase 8.5 — orchestrator-independent grep media-share через ls + manual count.

---

## 6. Russian context — спец. правила

- Только **открытые источники**. ТАСС/RIA — не как факт, а как «источник заявляет, что…».
- Симметричный фактчек: западные и российские источники должны проходить одинаковую планку.
- LAWS-блок — позиции **разных сторон** (Stop Killer Robots vs DoD vs РФ). Лекция не агитирует.
- Санкционный контекст (NVIDIA export controls 2022+, отечественные процессоры) — техн.факт, не политика.
- Студенты Bauman могут работать в ВПК. Лекция учит **инженерному суждению**, не лояльности и не диссидентству.

---

## 7. ROAST v0 (8 рисков + митигации)

### R1 — Over-engineering: попытка покрыть «всё»
**Риск:** аэрокосмос + оборонка = 4-5 разных доменов (гражданская авиация, космос, БПЛА, наземные системы, кибер). 75 минут не вытянут.
**Митигация:** в Phase 1 plan critique жёстко резать до 3-4 доменов + явная нотация «выходит за рамки лекции». Counter: курс-curator проверит, что вырезанное покрыто другими лекциями (lec-06 CAD, потенциальная lec-13/14).

### R2 — Unverified externals: IDF Lavender, российские БПЛА AI-компонент
**Риск:** Lavender controversy 2024 — много источников разной достоверности. Российские БПЛА — заявления производителей не проверяемы.
**Митигация:** Phase 0 research жёстко требует distinguish «подтверждено в peer-reviewed/реcпектабельном источнике» vs «заявлено компанией/гос.». fact-checker на Phase 3 + Phase 7 проверит каждое утверждение. Спорное — выводить в формулировке «по сообщениям/source X утверждает».

### R3 — Missing owner: media licensing pipeline не описан в `tools/presentation-build/README.md`
**Риск:** ≥50% media — много фото. Кто owner лицензионной проверки? Designer self-checks могут пропустить.
**Митигация:** В brief presentation-designer на Phase 5 — обязательное поле `licence:` на каждый external asset (CC-BY-X / public-domain / NASA / Wikimedia / fair-use-educational). Phase 7 fact-checker делает грубый licence-audit. Если 1-2 asset подвисают — заменяются на mermaid/QuickChart-эквивалент.

### R4 — Bundled risk: LAWS-блок + Russian-context-блок одновременно
**Риск:** оба политически чувствительны, бандл → один баг тянет revision обоих.
**Митигация:** разнести в плане в **разные разделы** (LAWS — Раздел 5 «этика и границы»; Russian context — distributed примерами в разделах 2-4). Critic проверяет каждый отдельно.

### R5 — Hook outdated: «strawberry» уже не работает для 2026
**Риск:** Раздел 0 hook должен быть 2026-evergreen, не упирающийся в текущее поколение моделей.
**Митигация:** Phase 1 plan critique включает hook engagement check. Кандидаты hook (выбор после Phase 0):
- BEFORE/AFTER object detection на свежем спутниковом снимке (визуальный, evergreen).
- F-35 ALIS → ODIN: «вот проект, который провалился — почему?» (failure-first hook).
- Drone footage с явным AI-аннотированием цели (мощно, но требует выбора кейса без политизации).

### R6 — Missing fundamentals: студент не знает что такое SAR, ATR, sensor fusion
**Риск:** аэрокосмос-специфичная терминология не разъяснена. Студент ИУ6 — инженер, но не профильный.
**Митигация:** Раздел 1 = «Карта AI в авиакосмосе» с **обязательным glossary-слайдом** (SAR / ATR / ISR / EW / LAWS / OODA). methodology-critic Phase 3 ловит missing-fundamentals явно.

### R7 — Scope creep на чёрные данные
**Риск:** студенту захочется «а как у нас?» — соблазн уйти в гипотезы про закрытые российские программы.
**Митигация:** в speech-brief Phase 9 — явная инструкция «Q&A backup: на вопросы про закрытые программы — отвечать "не имеем открытых данных, гипотезы избегаем"». В chapter.md — Q&A backup-секция.

### R8 — Tools-per-taxonomy не размечены (Лекция 4 lesson)
**Риск:** Phase 0 даст «общий обзор инструментов», не привязанный к уровням несущей оси.
**Митигация:** Уже в Phase 0 brief требуется tools-per-taxonomy-level (если ось = «уровни автономии» — на каждый уровень 2-4 доминирующих инструмента 2026 в вендор-режиме). lecture-outline template уже это требует для L4+.

---

## 8. Open questions (после Phase 0)

1. Финал narrative-оси: А / Б / В (или гибрид) — выбираем после `05-narrative-options.md`.
2. Hook кандидаты: 3 варианта выше — пользователь выбирает или утверждает после Phase 1 critique.
3. Russian-context глубина: 1 раздел / распределено / минимально — calibration после `04-russian-context.md`.
4. Lavender 2024 — включать ли явно, если в публичных источниках 2026 есть consensus? Решение после fact-checker Phase 3.

---

## 9. Что НЕ в плане сейчас (намеренно)

- Wiki-обновление (`wiki/`) — отдельный follow-up после GATE C, не блокирует production.
- Seminar lec-09 sem-09 — не в этом scope, отдельная задача.
- Diagram refresh — если в lec-09 появятся reusable diagrams, по `/diagram-refresh` после GATE C.
- Перевод/публикация на tellian.io — после GATE C.

---

**Следующий шаг:** дождаться Phase 0 (3-5ч). Когда research готов — оркестратор пишет v1 plan (`notes/lecture-9-review/plan-v1.md`) и спавнит Phase 1 critics. Никакой content-работы до GATE A approval scope.
