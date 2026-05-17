# Лекция 4 «AI в разработке программного обеспечения»
## Plan v1 — orchestrator draft (input для Phase 1 critique)

**Issue:** #99 · **Branch:** `issue-99-lec-04-software-production`
**Длительность:** 75 мин (~70 активный + ~5 Q&A/буфер) · **Аудитория:** 3 курс ИУ6 (универсально, без локального binding в chapter)
**Curriculum level:** Module 1, **первая отраслевая** лекция (после обзорных Л1–Л3) · **LO (canon, course-plan.md): LO1 + LO4 + LO7**
**Дата:** 2026-05-16 · **Phase:** Phase 1 (план → critique → roast → USER GATE 0 → Phase 2 chapter)
**Tone:** инженерно-аналитический, anti-hype. Тезис: *AI меняет цену написания кода, но не цену понимания, что строить и кто отвечает; правильный уровень автономии — инженерное решение под задачу, измеряемое, а не ощущаемое.*

**Inputs:**
- Canon: `library/project/course-plan.md` (Лекция 4 brief: «84% используют AI / 46% не доверяют; "почти правильный" код; IDE-интеграция vs чат vs coding agent»; LO1/LO4/LO7; паттерн «structure+constraints+tests»; антипаттерн «слепое копирование без ревью»; безопасность «корп. код в публичный чат»; человек «разработчик выбирает архитектуру, AI реализует, ревью — человек»).
- Research: `notes/research/lecture-4/{trends-2026,failures-and-limitations,progression-and-configs,tools-landscape,sources}.md`.
- Owner-бриф (см. §1.5).
- Формат-эталон: `notes/lecture-3-review/final/plan-v2-final.md`. Стиль слайдов/глубина главы — как lec-01/02/03 (Ocean palette; глава = глубокий референс + deep-dive + Q&A-бэкап).
- Пререквизит: Л3 (лестница сложности, «когда не ИИ», агенты/RAG/API) — Л4 **применяет** рамку Л3 к самой знакомой индустрии.

---

## 1. Контекст и зависимости

### 1.1 Промис из Л3 — выполняется
Л3 закрыла обзорный модуль «как выбрать архитектуру / когда не ИИ». Л4 — первая отраслевая: берём ту же рамку и **применяем к разработке ПО**. Несущая ось Л4 — **лестница автономности A→D**, прямое продолжение «лестницы сложности» Л3 (инструмент → агент → оркестратор): чем выше автономия, тем строже критерий «здесь обязателен человек / non-AI control».

### 1.2 Что НЕ повторяем (надстраиваем)

| Тема | Где (Л1–Л3) | Что Л4 делает |
|---|---|---|
| Типы AI, чат/агент/модель | Л1 | Используем; не переобъясняем |
| Внутренности LLM («почти правильно» ← сэмплинг) | Л2 | Ссылаемся как механизм, не переобъясняем |
| Лестница сложности, «когда не ИИ», агент plan→act→check→iterate, prompt injection | Л3 | **Применяем** к dev: A→D = та же лестница; prompt-injection → CamoLeak в dev-агенте |
| API/tool use | Л3 | Не повторяем; фокус — dev-инструменты и workflow |

### 1.3 Курсовая прогрессия
Л1 (типы) → Л2 (почему) → Л3 (как выбрать/когда не ИИ) → **Л4 (применение к ПО — первая знакомая индустрия)** → Л5–Л17 другие индустрии. Парный **Семинар 4** «AI в цикле разработки ПО: автодополнение, чат-ассистент и агент» (LO1,LO4,LO7) — место mastery LO4 (одна задача тремя способами + чек-лист доверия).

### 1.4 Сквозные темы курса (canon — обязательны)
- **Безопасность:** корп.код/секреты в публичный чат = утечка; уязвимости в AI-коде + ложная уверенность; slopsquatting; prompt-injection в dev-агенте (CamoLeak); least-privilege для агента.
- **Человек vs AI:** разработчик решает «что строить» (essential complexity, Brooks) и отвечает (accountability не делегируется); AI реализует; ревью — всегда человек.
- **Выбор инструмента:** какой уровень A→D и конфигурация (solo+AI vs team+AI) под задачу — ядро (LO7).
- **Паттерны/антипаттерны:** паттерн — «structure + constraints + tests» (TDD как спецификация для LLM); антипаттерн — слепое копирование AI-кода без чтения/ревью, vibe-coding без гейтов.

### 1.5 Owner-бриф (обязательно покрыть, отмечено где)
прогрессия A→D + оркестратор/трекер (§2.2 Раздел 1–3); тестирование+угрозы/безопасность (Раздел 4); подходы/методологии×ИИ (Раздел 5); параллели/различия с людьми (Раздел 5); «исторические практики не уходят, уточняются» — Brooks/DORA (Раздел 5); solo+ИИ vs команда+ИИ (Раздел 5); docs-as-code — честно «частично, как машиночитаемый контекст» (Раздел 5 + deep-dive); инструменты востребованные/уходящие (s_tools); отличный сторителлинг (failure-нить Replit/METR/curl/slopsquatting/Anthropic-junior); глубокая глава как Л3; стиль слайдов как lec-01/02/03.

---

## 2. Центральный вопрос и арка

### 2.1 Центральный вопрос
> **«AI пишет код всё лучше — где он реально ускоряет, где замедляет или вредит, и что в работе инженера НЕ делегируется?»**
Задаётся s04; точки возврата — на каждом «где человек обязателен» (s08/s12/s16/s21/s26); закрывается payoff s27–s29 (матрица уровней + чек-лист «прежде чем делегировать»).

### 2.2 Арка (~30 слайдов, 75 мин) — несущая ось: лестница автономности A→D

| Этап | Слайды | Бюджет | Функция |
|---|---|---|---|
| 0. Открытие+recap Л3+ЦВ | s01–s04 | 8 | Hook (perception-gap METR / Replit — GATE0-Q1); cover+roadmap; recap «лестница Л3 → лестница автономности»; ЦВ |
| 1. A+B: автодополнение и мелкие задачи | s05–s09 | 12 | Уровень A (автодоп, +55% лаб / +7–22% поле); B (чат/inline); «70/80%-проблема»; «почти правильный» код (66% фрустрация); паттерн structure+constraints+tests |
| 2. C: кодинг-агент, крупные задачи | s10–s13 | 11 | Многофайловые правки/тесты/итерация; SWE-bench Verified 88.7% vs **Pro 64.3%** (незнакомый код); review/merge gate; антипаттерн «принять PR не читая» |
| 3. D: оркестратор + трекер | s14–s17 | 10 | issue→PR автономно, multi-agent; **METR −19%** (perception-gap); деструктив без гейта (Replit code-freeze + ложь + 95/100; Kiro 13ч; PocketOS 9 сек) |
| 4. Не только код: тесты и безопасность | s18–s23 | 16 | AI×TDD; AI-review (Greptile 82% / FP) первый проход, человек второй; угрозы: уязвимости AI-кода (~40% / 12.1% CWE) + ложная уверенность; slopsquatting; CamoLeak prompt-injection; корп.код/секреты в чат |
| 5. Методологии, конфигурации, люди | s24–s27 | 12 | Методологии×ИИ (TDD №1, spec-driven, trunk+gates); Brooks essential≠accidental + DORA «amplifies»; solo+ИИ vs команда+ИИ; docs-as-code (частично); инструменты в/из |
| 6. Фреймворк + финал | s28–s31 | 11 | Матрица «уровень×задача», когда человек обязателен, «когда ИИ в разработке опасен/не нужен» (LO7 payoff); чек-лист «прежде чем делегировать» + apply (LO4); мост Семинар 4 + Q&A |
| Буфер | — | 5 | Q&A |

Pacing уточняется в v2 (slide-times + retrieval + переходы = 70 + 5 буфер).

---

## 3. Learning Outcomes

| LO | Формулировка (canon) | Как достигается | Slides | Success-критерий |
|---|---|---|---|---|
| **LO1** | Классифицировать типы AI-решений и сопоставить с задачами индустрии | Таксономия лестницы A→D (автодоп/чат/агент/оркестратор) + классы dev-инструментов | s04–s17, s_tools | По dev-задаче студент называет уровень A–D и тип инструмента |
| **LO4** | Применить AI-инструменты для типовой аналитической задачи | s30: лектор разбирает 1 dev-задачу на 3 уровнях (формат Семинара 4) → студенты mini-apply: выбрать уровень+чек-лист для задачи B | **s30**, s31(ДЗ) | За 2 мин: уровень + ≥2 причины + ≥1 «когда человек обязателен» + чек-лист |
| **LO7** | Обосновать выбор архитектуры AI (чат/агент/RAG/API/модель) для задачи | Матрица уровень×задача + конфигурация (solo+AI/team+AI) + критерии «когда не ИИ/опасно» | s04,s12,s16,s21,**s28–s30** | Студент обосновывает уровень+конфиг по осям (риск/незнакомость кода/обратимость/ответственность) и «когда было бы иначе» |

LO4 = применение рамки выбора уровня автономии к dev-задаче (это и есть «типовая аналитическая задача инженера»). Mastery — Семинар 4.

---

## 4. Slide list (v1, s01–s31; детализируется в chapter)

**Раздел 0 (8 мин):**
- **s01 Hook (3, `case_study`)** [GATE0-Q1] — реком.: **METR −19%** (16 экспертов, свои репо: с AI +19% времени, а верили в −20% ускорение — perception-gap). Альтернатива: Replit (деструктив в code-freeze + ложь). Hook рамкирует тезис «измеряй, не верь ощущению» + «автономия без гейта». *Partial→out (урок раскрыт в s15/s17).*
- **s02 Cover+roadmap (0.5, `cover`)** — roadmap 0–6, gold-маркер «Раздел 0».
- **s03 Recap Л3 → лестница автономности (1.5, `assertion_visual`)** — «лестница сложности Л3 (код→промпт→…→агент) проецируется на разработку как A→D». 4 ступени превью.
- **s04 Центральный вопрос (3, `assertion_visual`)** — ЦВ крупно + 4 «где человек обязателен» якоря. Disclaimer «лестница — карта лекции».

**Раздел 1 — A+B (12 мин):**
- **s05 Уровень A: автодополнение (2.5, `assertion_visual`)** — Copilot-класс; +55% лаб (CI, p=.0017) / +7–22% поле; человек = постоянный фильтр; риск автопринятия.
- **s06 Уровень B: мелкие задачи в чате/inline (2.5, `case_study`)** — генерит функцию/фикс; человек ставит+ревьюит.
- **s07 «70/80%-проблема» (2.5, `assertion_visual`, IN-BUCKET)** — быстро до 70–80%, последние 20–30% (edge/integration/prod) — самые трудные, требуют senior.
- **s08 «Почти правильный» код (2.5, `case_study`, IN-BUCKET)** — SO 2025: 66% — топ-фрустрация; «почти правильно» дороже явно неверного (маскирует баг). Урок: ревью+тесты до доверия. *ЦВ-возврат 1.*
- **s09 Паттерн: structure+constraints+tests (2, `assertion_visual`)** — canon-паттерн промпта для кода; мост к TDD (Раздел 5).

**Раздел 2 — C (11 мин):**
- **s10 Divider + Уровень C: кодинг-агент (1, `section_divider`)**.
- **s11 Что делает агент C (3, `process`)** — многофайл, тесты, итерация (plan→act→check→iterate из Л3, применённый к коду).
- **s12 Знакомый vs незнакомый код (3, `comparison`, IN-BUCKET, LO7)** — SWE-bench Verified ~88.7% vs **Pro ~64.3%** на приватных кодбазах; критерий: чем незнакомее/критичнее код — тем ниже доверие, строже gate. `[VFY-day-of]` числа. *ЦВ-возврат 2.*
- **s13 Review/merge gate (2.5, `case_study`, IN-BUCKET)** — антипаттерн «принять PR не читая»; GitClear: клоны 8→12%, рефакторинг 24→9% (скорость ≠ качество). Альт.: обязательный человеческий ревью + DRY-метрики.

**Раздел 3 — D (10 мин):**
- **s14 Divider + Уровень D: оркестратор+трекер (1, `section_divider`)**.
- **s15 issue→PR автономно, multi-agent (2.5, `process`)** — человек = стратегия/approval/merge/prod-гейт.
- **s16 METR −19% perception-gap (3, `case_study`, IN-BUCKET)** — измеряй реальное время, не ощущение; на знакомом сложном коде эксперт замедляется. `[FACT-CHECK]` update late-2025 «unreliable». *ЦВ-возврат 3.*
- **s17 Деструктив без гейта (3, `case_study`, IN-BUCKET, SECURITY)** — Replit (code-freeze + ложь + 95/100), Kiro (13ч), PocketOS (9 сек). Урок: hard human-gate на prod/деструктив, least-privilege, проверенный rollback, accountability не делегируется.

**Раздел 4 — тесты и безопасность (16 мин):**
- **s18 Divider + не только код (1, `section_divider`)**.
- **s19 AI × тестирование/TDD (3, `assertion_visual`)** — тест = исполняемая спецификация для LLM; mutation-gate, не только coverage.
- **s20 AI code review (2.5, `comparison`)** — AI первый проход (Greptile 82% catch / 11 FP vs CodeRabbit 44%/2), человек — второй; FP-noise; не заменяет.
- **s21 Угрозы: уязвимый AI-код + ложная уверенность (3, `case_study`, IN-BUCKET, SECURITY)** — NYU ~40%, анализ 12.1% CWE (Python 16–18%); Stanford: с AI вносят больше уязвимостей и увереннее. Урок: обязательный SAST/secret-scan на AI-код, threat-modeling — не делегируется. *ЦВ-возврат 4.*
- **s22 Slopsquatting (3, `case_study`, IN-BUCKET, SECURITY)** — ~20% сэмплов выдумывают пакеты, 58% воспроизводимо → supply-chain атака (связь с Л3 «когда не доверять выводу»). Альт.: lockfile+хэш-пин, allowlist, проверка пакета. `[VFY]`.
- **s23 Корп.код/секреты + prompt-injection (2.5, `case_study`, IN-BUCKET, SECURITY)** — canon: код в публичный чат = утечка; CamoLeak (CVE-2025-59145) — prompt-injection в Copilot Chat эксфильтрует секреты. Альт.: изоляция untrusted, egress-контроль, least-privilege, не давать агенту широкий доступ к секретам.

**Раздел 5 — методологии, конфигурации, люди (12 мин):**
- **s24 Методологии × ИИ (3, `matrix`, IN-BUCKET, LO7)** — TDD №1 (тест=спека), spec-driven, trunk+CI-gates; что меняется в DoD/quality-gates; хуже всего — vibe-coding без гейтов.
- **s25 Brooks + DORA: практики не уходят, уточняются (3, `assertion_visual`, IN-BUCKET)** — AI бьёт *accidental*, не *essential* complexity («решить что строить» — труднейшее); DORA «AI amplifies what's already there» (stability↓ 2-й год). Исторические методики/управление командой остаются, калибруются.
- **s26 solo+ИИ vs команда+ИИ (2.5, `comparison`, LO7)** — trade-off скорость/стоимость vs надёжность/ответственность/масштаб; solo = «exhausted bottleneck», single point of failure; команда сохраняет peer-review/ownership. *ЦВ-возврат 5.*
- **s27 docs-as-code + инструменты в/из (2.5, `assertion_visual`)** — docs-as-code частично: AGENTS.md/CLAUDE.md как машиночитаемый контекст — де-факто стандарт (авг 2025); «спека замещает код как истину» — пока vendor-claim (честно). Инструменты: Copilot стагнирует (всё ещё #1 охват, рост встал), Claude Code/Cursor растут; уходит практика vibe-coding-без-гейтов. `[VFY-day-of]` adoption.

**Раздел 6 — фреймворк + финал (11 мин):**
- **s28 Матрица «уровень × задача» (3, `matrix`, IN-BUCKET, LO7)** — оси: незнакомость кода · обратимость операции · критичность/prod · нужен ли аудит/ответственность · стоимость ошибки. Когда A/B/C/D; нижняя плашка «деструктив/prod/ответственность → человек обязателен».
- **s29 Когда ИИ в разработке не нужен/опасен (2, `assertion_visual`, IN-BUCKET, LO7)** — детерминированная верифицируемая задача / high-stakes без ревью / обучение junior (Anthropic −17%) / автономия без гейта. *ЦВ payoff.*
- **s30 Чек-лист «прежде чем делегировать» + apply (3, `summary`+exercise, LO7+LO4)** — 6–8 вопросов (уровень? обратимо? тесты-оракул? кто ревьюит/мержит? секреты? знакомость кода?); лектор worked-example задача A на 3 уровнях → студенты mini-apply задача B.
- **s31 Мост к Семинару 4 + следующие индустрии + Q&A (1.5 + ≤5 буфер, `summary`+`qa_minimal`)** — «эта лестница — линза для всех отраслей дальше»; ДЗ = Семинар 4.

---

## 5. AI-Failure & Judgment ≥30% strict-in (L4 — waiver НЕдоступен, Решение #82)

**Strict-in слайды (полностью in-bucket: провал+урок+альт / фундам. ограничение / критерий «не/опасно» / сравнение с не-ИИ практикой):**
s07, s08, s12, s13, s16, s17, s21, s22, s23, s24, s25, s28, s29 = **13 / 31 ≈ 42%** по слайдам; по минутам ≈ **~45%**.
**Partial→OUT:** s01 (hook), s05/s06 (калибровка уровней), s27 (tools — частично), s30 (payoff-чек-лист), s31 (мост).

**Per-artifact strict-in (holistic, каждый артефакт отдельно):**

| Артефакт | In-bucket ядро | Ориентир | Контроль |
|---|---|---|---|
| chapter | Детальные кейсы #1 Replit, #10 METR, #5 curl-slop, #6 slopsquatting, #16 Anthropic-junior + сводная таблица 17 кейсов + deep-dive (CamoLeak, GitClear, DORA, Stanford-confidence) + «когда не/опасно» | **≥40%** | methodology-critic Phase 3 |
| slides | 13 strict-in слайдов assertion-evidence | **≥40%** | methodology-critic Phase 7 |
| speech | Нарратив #1 Replit, #10 METR, #5 curl, #16 junior + критерии «когда человек обязателен» каждого раздела | **≥35%** | methodology-critic Phase 10 |

Waiver неприменим (L4 ∉ L1–L3). failure/judgment — несущая линия (это лекция о суждении инженера при делегировании ИИ). Counter-check: распределено по 6 разделам, не single-cluster.

---

## 6. Glossary lock (черновой; финализируется Phase 4 после chapter)

лестница автономности (A автодополнение / B мелкие задачи / C кодинг-агент / D оркестратор+трекер) · автодополнение (не «автокомплит») · кодинг-агент · оркестратор · «почти правильный» код · 70/80%-проблема · perception-gap (разрыв ощущение↔факт) · SWE-bench (Verified/Pro) · TDD (тест-первым) · spec-driven development · trunk-based · quality-gate · mutation-тестирование · SAST/DAST/SCA (расшифровка 1×) · secret-scanning · supply-chain · slopsquatting (галлюцинация пакета) · prompt injection (из Л3) · vibe-coding (антипаттерн: без тестов/спеки/гейтов) · accidental vs essential complexity (Brooks) · docs-as-code · AGENTS.md/CLAUDE.md (машиночитаемый контекст агента) · accountability (не делегируется).
Forbidden anglicisms (speech Англицизм Pass): пайплайн→конвейер, фоллбэк, эдж-кейс→краевой случай, инсайт.

---

## 7. Forbidden additions + inline-required

**Forbidden:** реальный длинный код на слайде (>3 строк); vendor-pricing/benchmark-числа как незыблемые (→ `[VFY]`/speaker notes); CVE-номера на видимом introductory-слое (→ chapter/notes); «Лектору»/«Вы здесь»/тайминг/subtitle-инициатива; slide add/delete без user request (REPORT); локальный binding в chapter; «магия AI»/«10× инженер» хайп; глубокий разбор конкретного SDK/IDE-UI; полная математика SWE-bench.
**Inline-required (определить при 1-м упоминании):** SWE-bench, mutation-тестирование, SAST/DAST/SCA, slopsquatting, perception-gap, accidental/essential complexity, docs-as-code, quality-gate, vibe-coding, supply-chain.

---

## 8. Микро-упражнения / retrieval

| Слайд | Тип | Длит. | Активность |
|---|---|---|---|
| s01 | open Q | 30 сек | «ускоряет ли вас AI — на сколько? откуда знаете?» |
| s08 | think pause | 30 сек | «как отличить "почти правильный" код от правильного?» |
| s17 | poll | 20 сек | «дали бы агенту доступ к prod-БД? при каком условии?» |
| s30 | apply (LO4) | 2 мин | чек-лист к dev-задаче B (формат Семинара 4) |

≈5–6 мин, включено в §2.2.

---

## 9. Свежесть (fact-checker; freshness enforced)

`[VFY-day-of]` (weekly/quarterly, критично): SWE-bench Verified/Pro числа и лидеры (s12 — Л1-урок: ARC-AGI устарел за 2 дня), «лучший инструмент»/leaderboard, adoption-доли (SO/JetBrains/DORA), market-size. `[FACT-CHECK]` (контринтуитив/обновляемое): METR late-2025 «unreliable signal» (s16 — подавать как early-2025 RCT + честная оговорка про update); slopsquatting % (s22). Стабильные (yearly+, без day-of): Brooks essential/accidental, METR early-2025 perception-gap, SO-2025 trust↓ direction, Anthropic −17% junior, GitClear churn, исторические инциденты с датами (Replit/Kiro/curl/CamoLeak CVE).

---

## 10. Открытые вопросы USER GATE 0

| # | Вопрос | Рекомендация |
|---|---|---|
| Q1 | Hook s01: METR −19% perception-gap vs Replit-деструктив | **METR** — контринтуитивно, рамкирует «измеряй, не верь ощущению» + личный для аудитории; Replit остаётся s17 |
| Q2 | Глубина chapter — как Л3 (22k+, deep-dive + Q&A-бэкап)? | Да, owner-директива (память feedback_chapter_depth); зафиксировать в плане v2 |
| Q3 | Slide count ~31 — ок? | Да, как Л3 (30) +1 (Раздел 4 безопасности плотный) |
| Q4 | LO4-apply: s30 worked+mini-apply (формат Семинара 4) достаточно? | Да; mastery — Семинар 4 |
| Q5 | Общее одобрение plan-v2 → Phase 2 chapter | — |

---

## 11. Source-of-truth chain
```
notes/lecture-4-software-review/
├── 2026-05-16/plan-v1.md (ЭТОТ ФАЙЛ)
├── 2026-05-16/phase1-critique/{methodology-critic.md, reader-text-only.md}
└── final/plan-v2-final.md (после roast+Phase1 → USER GATE 0 → Phase 2)
notes/research/lecture-4/ (research, committed)
library/lectures/lec-04/{chapter.md[+parts], deck.yaml[+parts], slides/*.md, speech.md} (производные)
```
Историческое `notes/lecture-4-review/` = старая медицина (Л7) — НЕ путать/НЕ трогать.

## 12. Phase 2 brief (preview, финализируется в v2)
book-editor пишет `library/lectures/lec-04/chapter.md` — глубокий расширенный референс (как Л3: ориентир 22k+, red-flag>15k снят owner-решением; разбить на части по Document Size Limit 600 строк) — 6 разделов (mirror §2.2) + deep-dive boxes «что не вошло, но важно» (полный METR-методологический разбор + update; CamoLeak механизм + CVE-хронология; GitClear-метрики; DORA 7 capabilities; Stanford «уверенность+уязвимость»; spec-driven детали; Brooks «No Silver Bullet» первоисточник; tools adoption-таблица) + «вероятные вопросы аудитории + развёрнутые ответы». LO1+LO4+LO7. Glossary §6, Forbidden/inline §7 — ENFORCED. `[FACT-CHECK]`/`[VFY]` §9. Tone инженерно-аналитический, anti-hype, strict-in ≥40% holistic. book-first.

**Status:** v1 ready → orchestrator roast → Phase 1 critique (methodology-critic + reader-text-only) → USER GATE 0.
