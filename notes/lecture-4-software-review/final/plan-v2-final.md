# Лекция 4 «AI в разработке программного обеспечения»
## Plan v2-final — synthesized from v1 + Phase 1 critique + orchestrator roast

**Issue:** #99 · **Branch:** `issue-99-lec-04-software-production`
**Длительность:** 75 мин (~70 активный + ~5 Q&A/буфер) · **Аудитория:** 3 курс ИУ6 (универсально, без локального binding в chapter)
**Curriculum level:** Module 1, **первая отраслевая** лекция (после обзорных Л1–Л3) · **LO (canon): LO1 + LO4 + LO7**
**Slide count: 32 (s01–s32 + suffix-дивайдеры по необходимости)** — финально зафиксировано (cascade-lock до Phase 2).
**Tone:** инженерно-аналитический, anti-hype. Тезис: *AI меняет цену написания кода, не цену понимания, что строить и кто отвечает; уровень автономии — измеряемое инженерное решение под задачу, не ощущение.*

**Changelog v1 → v2 (Phase 1 + roast, 8 пунктов SYNTHESIS):**
- [P0-1] §5/§12 strict-in операционализирован per-artifact (именованные блоки + квантификация); slides честно **11 solid/32 ≈ 34%** + путь до ~42% усилением s25/s26; L4 waiver НЕдоступен — failure-плотность главы проектируется намеренно.
- [meth-2/4 + reader S-1] Раздел 4 разнесён (тест+review | безопасность с retrieval; ≤2 security подряд) + retrieval в Р4/Р5.
- [meth-2 + reader N-4] s17 METR: добавлен **КАК измерять** (A/B на своих задачах, реальное время); late-2025 reversal → chapter deep-dive.
- [reader S-3/N] A/B-граница артикулирована единым паттерном «AI делает / кто решает / где человек обязателен» по A→D; s03 — явная таблица-мэппинг Л3-лестница→A–D; s01 — gloss perception-gap; s04 — disclaimer «лестница = карта».
- [meth-1] LO4 зафиксирован как **entry-Apply** (worked + think-pair-share), full mastery = Семинар 4; success-критерий → оси матрицы s29.
- [meth-5/6] course-конструкты помечены scaffold+атрибуция; §7 inline-safety-net (prompt-injection/лестница/plan-act-check-iterate из Л3); §10 pre-Phase-2 sanity vs finalized Л3.
- [roast] pacing честная (Σ slide-times ~55 + retrieval ~8 + переходы ~7 = 70 + 5 = 75); §2.2↔§4 нумерация синхронна.
- [P2] SWE-bench inline-define s12; CWE inline s22, ≤2 источника видимо; s28 (методологии) — отдельный слайд, не совмещён.

---

## 1. Контекст и зависимости

### 1.1 Промис из Л3 — выполняется
Л3 закрыла обзорный модуль («как выбрать архитектуру / когда не ИИ»). Л4 — первая отраслевая: **применяем рамку Л3 к разработке ПО**. Несущая ось — **лестница автономности A→D** (course-scaffold-конструкт, атрибуция на s04), прямое продолжение «лестницы сложности» Л3: чем выше автономия, тем строже критерий «здесь обязателен человек / non-AI control».

### 1.2 Что НЕ повторяем (надстраиваем) + inline-safety-net

| Тема | Где (Л1–Л3) | Что Л4 делает | Inline-safety-net |
|---|---|---|---|
| Типы AI, чат/агент/модель | Л1 | Используем | — |
| «почти правильно» ← сэмплинг | Л2 | Ссылаемся как механизм | 1 фраза-напоминание |
| Лестница сложности; «когда не ИИ»; агент plan→act→check→iterate; prompt injection | Л3 (chapter — канон-пререквизит, PR #91 merged) | **Применяем**: A→D = та же лестница; CamoLeak = prompt-injection в dev | мини-определение каждого при 1-м упоминании (НЕ дублировать визуально Л3) |

§10: pre-Phase-2 — book-editor сверяет §-ссылки на Л3 против finalized `library/lectures/lec-03/chapter*.md`.

### 1.3 Курсовая прогрессия
Л1→Л2→Л3 (обзор) → **Л4 (ПО — первая знакомая индустрия)** → Л5–Л17. Парный **Семинар 4** «AI в цикле разработки ПО: автодополнение, чат-ассистент, агент» (LO1/LO4/LO7) — **место full mastery LO4**.

### 1.4 Сквозные темы (canon, обязательны)
Безопасность (корп.код/секреты в чат; уязвимости AI-кода+ложная уверенность; slopsquatting; CamoLeak prompt-injection; least-privilege агента) · Человек vs AI (решает «что строить» — essential complexity Brooks; отвечает — accountability не делегируется; ревью — всегда человек) · Выбор инструмента (уровень A–D + конфиг solo/team — LO7) · Паттерн «structure+constraints+tests» (TDD как спека для LLM) / антипаттерн «слепое копирование без ревью, vibe-coding без гейтов».

### 1.5 Owner-бриф — карта покрытия
Прогрессия A→D + оркестратор/трекер → Разделы 1–3; тест+угрозы/безопасность → Раздел 4; методологии×ИИ + параллели/различия + «практики не уходят, уточняются» (Brooks/DORA) + solo+ИИ vs команда+ИИ + docs-as-code → Раздел 5; инструменты в/из → s27; сторителлинг — failure-нить (Replit/METR/curl/slopsquatting/Anthropic-junior); глубокая глава как Л3; стиль слайдов lec-01/02/03.

---

## 2. Центральный вопрос и арка

### 2.1 Центральный вопрос
> **«AI пишет код всё лучше — где он реально ускоряет, где замедляет или вредит, и что в работе инженера НЕ делегируется?»**
s04 задаёт; 5 точек возврата (s08 / s13 / s17 / s21+s23 / **s26** — «где человек обязателен»; [P2-1 Phase-4 consistency fix: было ошибочно s23/s27 → точка 4 = s21+s23, точка 5 = s26 §5.2 Brooks/DORA — синхрон с chapter §0.3]); payoff s29–s31 (матрица уровней + «когда не/опасно» + чек-лист).

### 2.2 Арка (35 слайдов = 32 + 3 suffix-ID дивайдера, 75 мин) — несущая ось A→D

> **[Решение #101, 2026-05-17 — owner GATE B]** Симметрия roadmap-бара: добавлены **3 раздела-дивайдера** для Разделов 1/5/6 (раньше дивайдеры были только у Р2/3/4 = s10/s14/s18). Полная схема — **6 дивайдеров на 6 контент-разделов** (Р0 = открытие, без дивайдера): **s04a** (Р1), s10 (Р2), s14 (Р3), s18 (Р4), **s24a** (Р5), **s28a** (Р6). Реализация — **suffix-ID, cascade-safe** (как Лекция 3): глава финализирована GATE A с маркерами `[for-slide-sNN]` s01–s32 — renumber их рассинхронит; suffix-ID s04a/s24a/s28a НЕ трогает главу, chapter_ref и нумерацию s01–s32. Owner-override GATE-0 Q4 «slide-count LOCKED=32» → **35** (явное документированное решение, реестр `notes/decisions.md`). Pacing: +3×~0.3 ≈ +1 мин, поглощается буфером (5→~4 мин). strict-in: дивайдеры partial→out, count=15 неизменно; слайдо-доля 15/35≈43% (≥40% держится), минутная 54.5% не затронута — methodology-critic re-confirm.

| Раздел | Слайды | Бюджет* | Функция |
|---|---|---|---|
| 0. Открытие + карта лестницы + ЦВ | s01–s04 | 8 | Hook (GATE0-Q1); cover+roadmap; **s03 = карта лестницы A→D (KEYSTONE): 4 уровня × что делает AI / кто решает / живой пример + линза анализа**; s04 ЦВ + якоря «где человек обязателен» (Л3-связь = 1 строка, БЕЗ disclaimer-футера) |
| 1. A+B автодоп/мелкие | s05–s09 | 11 | s05 **цена ошибки растёт с автономией A→D** (несущий принцип, не meta); A (автодоп +55%лаб/+7–22%поле); B (чат); 70/80%-проблема; «почти правильный» (66%) |
| 2. C кодинг-агент | s10–s13 | 10 | Многофайл/тесты/итерация; SWE-bench Verified 88.7 vs **Pro 64.3** (незнакомый код); review/merge gate (GitClear) |
| 3. D оркестратор+трекер | s14–s17 | 10 | issue→PR/multi-agent; деструктив без гейта (Replit/Kiro/PocketOS); **METR −19% + КАК измерять** |
| 4a. Тест+ревью | s18–s20 | 7 | AI×TDD; AI-review первый проход/человек второй; retrieval |
| 4b. Безопасность | s21–s24 | 11 | Угрозы (уязвимый код+ложная уверенность); slopsquatting (+retrieval); корп.код/секреты+CamoLeak |
| 5. Методологии/конфиг/люди | s25–s28 | 11 | Методологии×ИИ (TDD№1); Brooks+DORA «уточняются, не уходят»; solo vs команда; docs-as-code+инструменты |
| 6. Фреймворк+финал | s29–s32 | 12 | Матрица уровень×задача; «когда не/опасно» (LO7); чек-лист+apply (LO4); мост Семинар 4+Q&A |
| Буфер | — | 5 | Q&A |

\* **Pacing (честно):** Σ slide-times ≈ 55 + retrieval-моменты ≈ 8 (s01/s08/s17/s22/s31) + переходы/комментарий ≈ 7 = 70 активных + 5 буфер = **75**. Раздел-бюджеты выше включают retrieval+переходы (не двойной учёт). Финальная per-slide разбивка — chapter Phase 2.

---

## 3. Learning Outcomes

| LO | Формулировка (canon) | Достижение | Slides | Success-критерий |
|---|---|---|---|---|
| **LO1** | Классифицировать типы AI-решений, сопоставить с задачами индустрии | Таксономия A→D + классы dev-инструментов (s27) | s03–s17, s27 | По dev-задаче назвать уровень A–D + класс инструмента |
| **LO4** (entry-Apply; full mastery — Семинар 4) | Применить AI-инструменты для типовой аналитической задачи | s31: лектор worked — 1 задача на 3 уровнях (формат Сем-4) → студенты **think-pair-share** mini-apply задача B | **s31**, s32(ДЗ) | За 2 мин: уровень + ≥2 причины по осям матрицы s29 + ≥1 «где человек обязателен» |
| **LO7** | Обосновать выбор архитектуры AI (чат/агент/RAG/API/модель) | Матрица уровень×задача + конфиг solo/team + «когда не/опасно» | s04,s13,s17,s23,**s29–s31** | Обосновать уровень+конфиг по осям (незнакомость кода/обратимость/критичность/аудит/цена ошибки) + «когда было бы иначе» |

LO4 — осознанно **entry-level Apply** на лекции (worked example + think-pair-share); полный Apply/mastery — парный Семинар 4. Не косметика: success-критерий привязан к осям матрицы s29.

---

## 4. Slide list (s01–s32; детализируется в chapter)

> **Deck-wide tone-принцип (ENFORCED, все 32 слайда — Решение #100, 2026-05-17).** Каждый слайд **подаёт новое студенту, который сталкивается с темой впервые** — не защищает подход, не оправдывается, не объясняет курсовую методологию. На видимом слое **0**: §-кодов / (sNN) / (Раздел N) / LO-кодов; ссылок-кодов на чужие лекции; «course-scaffold / не отраслевой стандарт / возвращаемся N раз / мы не вводим нового / это проекция правила Л3» дисклеймеров; meta-комментариев «зачем этот слайд». Атрибуция course-scaffold и Л3-связь, если нужны для научной честности, — **в speaker notes**, не на слайде. Заголовок и 1-я строка каждого слайда — содержательное утверждение по теме, а не про устройство лекции. (Каскад Л2-R1/Л3 рецидив → anti-patterns #36–#39.)

**Раздел 0 (8):**
- **s01 Hook (3, `case_study`)** [GATE0-Q1 — реком. METR] — METR RCT: 16 экспертов, свои репо; с AI **+19% времени**, а прогноз/вера −20% ускорение. 1-строчный inline-gloss: «perception-gap — разрыв между ощущением скорости и измеренным фактом». Open-Q (30 сек): «ускоряет ли вас AI — на сколько? откуда знаете?». *Partial→out (раскрытие s17).*
- **s02 Cover+roadmap (0.5, `cover`)** — roadmap 0–6, gold-маркер Раздел 0.
- **s03 Карта лестницы автономности A→D (2.5, `matrix`/`comparison`, KEYSTONE — несущая ось всей лекции)** — таблица: 4 строки **A / B / C / D** × колонки **что делает AI · кто принимает решение · живой пример**. A — автодополняет строку в потоке (Copilot-tab); B — пишет функцию/фикс по запросу в чате; C — кодинг-агент берёт многофайловую задачу, гоняет тесты, итерирует; D — оркестратор берёт issue из трекера и доводит до PR сам. Эти же 3 колонки = **линза, которой разберём каждый уровень дальше** (бывш. s05-«единый паттерн» свёрнут сюда; 4-я ось «типичный риск / где человек обязателен» проявится в Разделах 1–4). Л3-связь = **1 строка в теле**: «как лестница сложности из Лекции 3 — выбираешь ступень под задачу, не выше». Заголовок и 1-я строка — про сами уровни, не про устройство курса. Атрибуция course-scaffold (карта лекции, не отраслевой ГОСТ) — **в speaker notes**, 0 §-кодов/disclaimer на слайде.
- **s04 Центральный вопрос (2, `assertion_visual`)** — ЦВ крупно. Под ним рамка ответа: «ответ — не "AI хорош/плох", а: назвать **уровень A–D**, конфигурацию и **точку, где человек обязателен**». 5 якорей «где человек обязателен» — **именами по смыслу**, не §-коды и не «возвращаемся N раз»: «почти правильный» код · merge/ревью · деструктив на prod · безопасность кода · «что строить» (essential). Disclaimer-футер course-scaffold **удалён** (атрибуция → speaker notes s03). Задаёт 5 точек возврата (s08/s13/s17/s21+s23/s26) — связками в речи, не кодами на слайде.

**Раздел 1 — A+B (11):**
- **s05 Цена ошибки растёт с автономией (2, `assertion_visual`)** — несущий принцип (бывш. слот «единый паттерн» — рамка свёрнута в s03; **слот переиспользован, НЕ renumber**): чем выше ступень A→D, тем больше автономия и **радиус поражения** ошибки → обязательные точки человека смещаются и ужесточаются. Это «почему» центрального вопроса и контентный мост в Раздел 1 — не meta, не защита таксономии. Ранний посев, собирается в матрице s29 (ось «цена ошибки»). Strict-in judgment-якорь (пересчёт §5 на Phase-7).
- **s06 Уровень A: автодополнение (2.5, `case_study`)** — спускаемся на 1-ю ступень лестницы с s03. Copilot-класс; +55% лаб (CI,p=.0017)/+7–22% поле; человек = постоянный фильтр каждого токена; риск автопринятия (клоны/уязвимости). Подаём как новое: что это, где уже стоит, в чём ловушка — без «мы не вводим нового».
- **s07 Уровень B: мелкие задачи в чате/inline (2, `assertion_visual`)** — 2-я ступень: AI генерит функцию/фикс по запросу, человек ставит задачу и ревьюит результат. Учим **границу A↔B как различение** (A = строка-в-потоке, человек в цикле каждый токен; B = задача-фрагмент, человек-ревью-после), а не как оправдание классификации.
- **s08 «70/80%-проблема» + «почти правильный» (3, `case_study`, IN-BUCKET)** — быстро до 70–80%, последние 20–30% (edge/integration/prod) труднейшие; SO-2025: 66% — топ-фрустрация «почти правильно»; дороже явно неверного. Урок: ревью+тесты до доверия. Think-pause (30 сек). *ЦВ-возврат 1.*
- **s09 Паттерн structure+constraints+tests (2, `assertion_visual`)** — canon-паттерн промпта для кода; мост к TDD (s25).

**Раздел 2 — C (10):**
- **s10 Divider + Уровень C (1, `section_divider`)**.
- **s11 Что делает агент C (2.5, `process`)** — многофайл/тесты/итерация = plan→act→check→iterate Л3, применённый к коду (мини-напоминание термина).
- **s12 Знакомый vs незнакомый код (3, `comparison`, IN-BUCKET, LO7)** — **inline-define SWE-bench** (бенчмарк: решить реальные GitHub-issue, % решённых). Verified ~88.7% vs **Pro ~64.3%** (приватные кодбазы) `[VFY-day-of диапазон]`. Критерий: незнакомее/критичнее код → ниже доверие, строже gate.
- **s13 Review/merge gate (3.5, `case_study`, IN-BUCKET)** — антипаттерн «принять PR не читая»; GitClear 211M строк: клоны 8.3→12.3%, рефакторинг 24→9.5%, churn 5.5→7.9% (скорость≠качество). Альт.: обязательный человеческий ревью + DRY-метрики в CI. *ЦВ-возврат 2.*

**Раздел 3 — D (10):**
- **s14 Divider + Уровень D (1, `section_divider`)**.
- **s15 issue→PR/multi-agent (2.5, `process`)** — человек = стратегия/approval/merge/prod-гейт.
- **s16 Деструктив без гейта (3, `case_study`, IN-BUCKET, SECURITY)** — Replit (code-freeze + удалил prod-БД + солгал + 95/100; rollback работал), Kiro (13ч outage), PocketOS (9 сек). Урок: hard human-gate на prod/деструктив, least-privilege, проверенный rollback, accountability не делегируется. *эталон failure-слайда.*
- **s17 METR −19% + КАК измерять (3, `case_study`, IN-BUCKET)** — perception-gap раскрыт; **actionable: A/B на своих задачах, фиксировать реальное время, селективно (не high-context legacy)**. late-2025 «unreliable signal» reversal → chapter deep-dive (не на слайд). Retrieval. *ЦВ-возврат 3.*

**Раздел 4a — тест+ревью (7):**
- **s18 Divider + не только код (0.5, `section_divider`)**.
- **s19 AI × тестирование/TDD (3, `assertion_visual`)** — тест = исполняемая спецификация для LLM; mutation-score gate, не только coverage.
- **s20 AI code review (3, `comparison`)** — AI первый проход (Greptile ~82% catch/11 FP vs CodeRabbit ~44%/2), человек второй; FP-noise; не заменяет, дополняет.

**Раздел 4b — безопасность (11):**
- **s21 Угрозы: уязвимый AI-код + ложная уверенность (3, `case_study`, IN-BUCKET, SECURITY)** — NYU ~40% сценариев / анализ 12.1% CWE (**inline: CWE — каталог типов уязвимостей**; Python 16–18%>JS>TS); Stanford: с AI вносят больше уязвимостей и увереннее. Урок: обязательный SAST/secret-scan (inline-define) на AI-код; threat-modeling не делегируется. ≤2 источника видимо. *ЦВ-возврат 4 — частично; полный возврат s23.*
- **s22 Slopsquatting (3, `case_study`, IN-BUCKET, SECURITY)** — inline-define; ~20% сэмплов выдумывают пакеты, 58% воспроизводимо → supply-chain атака (прямая связь с Л3 «когда не доверять выводу»). Альт.: lockfile+хэш-пин, allowlist реестров, проверка пакета до install. Retrieval poll (20 сек). `[VFY]`.
- **s23 Корп.код/секреты + prompt-injection (3, `case_study`, IN-BUCKET, SECURITY, LO7)** — canon: код в публичный чат = утечка; CamoLeak — prompt-injection в Copilot Chat эксфильтрует секреты (CVE→chapter, не на слайд). Альт.: изоляция untrusted, egress-контроль, least-privilege, не давать агенту широкий доступ к секретам. *ЦВ-возврат 4 (полный).*
- **s24 Сводка «когда человек обязателен» Р1–4 (2, `summary`, IN-BUCKET)** — консолидирует 4 точки возврата перед методологиями (anti-«страшилка»: каждый риск → контроль).

**Раздел 5 — методологии/конфиг/люди (11):**
- **s25 Методологии × ИИ (3, `matrix`, IN-BUCKET, LO7)** — TDD №1 (тест=спека), spec-driven, trunk+CI-gates; что меняется в DoD/quality-gates; **хуже всего — vibe-coding без гейтов (явный критерий-антипаттерн)**.
- **s26 Brooks+DORA: практики уточняются, не уходят (3, `case_study`, IN-BUCKET)** — AI бьёт *accidental*, не *essential* complexity (inline: accidental=рутина/boilerplate, essential=«решить что строить» — труднейшее, Brooks); DORA «AI amplifies what's already there» (stability↓ 2-й год). Исторические методики/управление командой остаются, калибруются. *ЦВ-возврат 5.*
- **s27 solo+ИИ vs команда+ИИ + инструменты в/из (3, `comparison`, LO7)** — trade-off скорость/стоимость vs надёжность/ответственность/масштаб; solo=«exhausted bottleneck»/single point of failure; команда=peer-review/ownership. Инструменты: Copilot стагнирует (всё ещё #1 охват, рост встал), Claude Code/Cursor растут; уходит практика vibe-coding-без-гейтов. `[VFY-day-of]` adoption.
- **s28 docs-as-code (2, `assertion_visual`)** — частично: AGENTS.md/CLAUDE.md как машиночитаемый контекст агента — де-факто стандарт (авг 2025); «спека замещает код как истину» — **пока vendor-claim, честно помечаем «слабо подтверждено»**.

**Раздел 6 — фреймворк+финал (12):**
- **s29 Матрица «уровень × задача» (3, `matrix`, IN-BUCKET, LO7)** — оси: незнакомость кода · обратимость операции · критичность/prod · нужен аудит/ответственность · цена ошибки. Когда A/B/C/D; нижняя плашка «деструктив/prod/ответственность/обучение → человек обязателен».
- **s30 Когда ИИ в разработке не нужен/опасен (2, `assertion_visual`, IN-BUCKET, LO7)** — детерминированная верифицируемая задача / high-stakes без ревью / обучение junior (Anthropic −17%) / автономия без гейта. *ЦВ payoff.*
- **s31 Чек-лист + apply (3.5, `summary`+exercise, LO7+LO4)** — 6–8 вопросов (уровень? обратимо? тест-оракул? кто ревьюит/мержит? секреты? знакомость кода?); лектор worked задача A на 3 уровнях → think-pair-share mini-apply задача B (формат Семинара 4).
- **s32 Мост Семинар 4 + следующие индустрии + Q&A (1.5 + ≤5 буфер, `summary`+`qa_minimal`)** — «лестница A–D — линза для всех отраслей дальше»; ДЗ=Семинар 4.

---

## 5. AI-Failure & Judgment ≥30% strict-in (L4 — waiver НЕдоступен, Решение #82; реестр §3.6 — только Л1/Л2)

**Slides honest recompute (partial→out, Решение #78):** solid IN — s08, s12, s13, s16, s17, s21, s22, s23, s24, s29, s30 = **11/32 ≈ 34%**; усиление до ~42% — s25 (vibe-coding-критерий явный), s26 (DORA-провал «amplifies слабость» как failure-якорь), s27 (solo single-point-of-failure) → +3 = 14/32 ≈ 44%. Минутная доля ≈ **~45%** (честная метрика). Partial→out: s01(hook), s06–s07/s11/s15 (калибровка уровней), s28(docs частично), s31(payoff), s32(мост). **[Решение #100, 2026-05-17 — ЗАКРЫТО]** s05 переопределён «единый паттерн» → «цена ошибки растёт с автономией» = judgment/limits-якорь, **strict-in**. Пересчёт methodology-critic (v3 re-QA, 2026-05-17): **15/32 = 46.9% слайдов / 54.5% минут (42/77)**; single-cluster снят (Р1–Р6 = 41–82% секции, max-кластер Р4 = 14.3% deck); ≥40% holistic с запасом ~15 п.п., концентрации в один артефакт нет (chapter ~69%). `deck-part2.yaml ai_failure_judgment` синхронизирует designer v3.1 (count 14→15, s05 in_bucket).

**Per-artifact operationalized (НЕ постулат — именованные блоки + квантификация):**

| Артефакт | In-bucket ядро (named) | Квант. ориентир | Контроль |
|---|---|---|---|
| **chapter** | 5 детальных кейсов: #1 Replit, #10 METR, #5 curl-slop, #6 slopsquatting, #16 Anthropic-junior (≥600 слов каждый) + сводная таблица 17 кейсов + блок «критерий "человек обязателен"» ≥80 слов × 6 разделов + deep-dive (CamoLeak, GitClear, DORA-7cap, Stanford-confidence, METR-update) | **≥40%** (несущая ось A→D НЕ failure → плотность инженерить намеренно: failure-кейс + «когда не/опасно» завершают КАЖДЫЙ раздел) | methodology-critic Phase 3 (пересчёт strict-in) |
| **slides** | 14 strict-in слайдов (см. выше) assertion-evidence | **≥40%** (14/32≈44%) | methodology-critic Phase 7 |
| **speech** | Нарратив #1 Replit + #10 METR(+как измерять) + #5 curl + #16 junior; устный «критерий человек-обязателен» ≥50 слов × 6 разделов | **≥35%** | methodology-critic Phase 10 |

Counter-check: распределено по 6 разделам (s08-Р1, s12/s13-Р2, s16/s17-Р3, s21/s22/s23/s24-Р4, s25/s26/s27-Р5, s29/s30-Р6) — single-cluster снят (Р4 не >40% strict-in-минут после s24-консолидации + Р5-усиления).

---

## 6. Glossary lock (черновой; финал Phase 4)

лестница автономности A–D (course-scaffold) · автодополнение · кодинг-агент · оркестратор · «почти правильный» код · 70/80%-проблема · perception-gap · SWE-bench (Verified/Pro) · TDD · spec-driven development · trunk-based · quality-gate · mutation-тестирование · SAST/DAST/SCA · secret-scanning · supply-chain · slopsquatting · prompt injection (Л3) · vibe-coding (антипаттерн) · accidental vs essential complexity (Brooks) · docs-as-code · AGENTS.md/CLAUDE.md · accountability.
Forbidden anglicisms: пайплайн→конвейер, фоллбэк, эдж-кейс→краевой случай, инсайт.

## 7. Forbidden + inline-required
**Forbidden:** код>3 строк на слайде; vendor/benchmark-числа как незыблемые (→`[VFY]`/notes); CVE-номера на видимом слое (→chapter); «Лектору»/«Вы здесь»/тайминг/subtitle-инициатива; **видимые §-коды / (sNN) / (Раздел N) / LO-коды / course-scaffold-disclaimer / «не вводим нового»/«проекция Л3»/«возвращаемся N раз» meta** (Deck-wide tone-принцип §4, Решение #100; рецидив Л2-R1/Л3 → P0/P1, anti-patterns #36–#39); slide add/del без request (REPORT); локальный binding в chapter; «магия/10× инженер» хайп; deep SDK/IDE-UI; полная математика SWE-bench/METR.
**Inline-required (1-е упоминание):** SWE-bench, mutation-тест, SAST/DAST/SCA, CWE, slopsquatting, perception-gap, accidental/essential, docs-as-code, quality-gate, vibe-coding, supply-chain + **safety-net Л3**: prompt-injection, лестница сложности, plan→act→check→iterate (мини-фраза, не визуальный дубль Л3).

## 8. Микро-упражнения/retrieval
s01 open-Q 30с («ускоряет ли вас AI — откуда знаете?»); s08 think-pause 30с; s17 retrieval 30с («как бы измерили реальный эффект?»); s22 poll 20с («дали бы агенту `npm install` из его предложения?»); s31 apply 2мин (think-pair-share, LO4). ≈5–6 мин, в §2.2.

## 9. Свежесть (fact-checker)
`[VFY-day-of]`: SWE-bench Verified/Pro числа+лидеры (s12 — Л1-урок ARC-AGI устарел за 2 дня), adoption-доли (SO/JetBrains/DORA, s27), market-size, «лучший инструмент». `[FACT-CHECK]`: METR late-2025 «unreliable» (s17 — early-2025 RCT + честная оговорка, reversal в chapter), slopsquatting % (s22). Стабильные (yearly+): Brooks essential/accidental, METR early-2025 perception-gap, SO-2025 trust↓ direction, Anthropic −17% junior, GitClear churn, инциденты с датами (Replit/Kiro/curl/CamoLeak).

## 10. USER GATE 0 — РЕШЕНИЯ ВЛАДЕЛЬЦА (2026-05-16, зафиксировано)
- **Q1 Hook = METR −19% perception-gap** (s01). Replit-деструктив остаётся s16.
- **Q2 Глубина chapter = 22k+ как Глава 3** (глубокий референс + deep-dive boxes + Q&A-бэкап). **Явное документированное owner-решение:** red-flag «>15k слов» (`tools/lecture-production/README.md` §6) СНЯТ для `lec-04/chapter.md` (governance escape-hatch, `notes/decisions.md` 2026-05-16). Split по Document Size Limit 600 строк (waiver недоступен) — `chapter.md` + `chapter-part2.md`[+part3] с кросс-ссылками.
- **Q3 plan-v2-final ОДОБРЕН** → Phase 2 chapter draft.
- Q4 (slide-count LOCKED=32), Q5 (LO4 = entry-Apply, mastery Семинар 4) — закрыты в v2.
**Pre-Phase-2 (orchestrator/book-editor):** сверить §-ссылки Л3 против finalized `library/lectures/lec-03/chapter*.md` (PR #91 merged).

## 11. Source-of-truth chain
`notes/lecture-4-software-review/{2026-05-16/plan-v1.md, 2026-05-16/phase1-critique/*, final/plan-v2-final.md}` → `library/lectures/lec-04/{chapter[+parts], deck[+parts], slides/*, speech.md}`. Историч. `notes/lecture-4-review/`=медицина(Л7) — НЕ путать.

## 12. Phase 2 brief
book-editor: `library/lectures/lec-04/chapter.md` — глубокий референс (как Л3: 22k+, red-flag>15k снят owner-Q2; split по Document Size Limit 600 → chapter.md+chapter-part2.md[+3] с кросс-ссылками) — 6 разделов (mirror §2.2) + deep-dive boxes (METR-методология+late-2025-update; CamoLeak механизм+CVE; GitClear; DORA-7cap; Stanford confidence; spec-driven; Brooks «No Silver Bullet» первоисточник; tools adoption-таблица) + «вероятные вопросы + ответы» на раздел. LO1+LO4+LO7 (success §3). Glossary §6 + Forbidden/inline §7 ENFORCED. **strict-in ≥40% holistic — failure/judgment-плотность проектировать намеренно (каждый раздел завершать failure-кейсом + критерием «когда не/опасно»; ось A→D сама НЕ засчитывается)**. `[FACT-CHECK]`/`[VFY]` §9. Tone инженерно-аналитический anti-hype. book-first. Speaker-notes markers `[for-slide-sNN]` s01–s32. Pre-write: сверить Л3-ссылки vs finalized lec-03/chapter*.

**Status:** v2-final ready → pre-gate self-check → **USER GATE 0** (Q1–Q3).
