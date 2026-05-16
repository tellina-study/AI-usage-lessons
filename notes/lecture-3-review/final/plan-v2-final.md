# Лекция 3 «Архитектуры AI-систем: агенты, RAG, API»
## Plan v2-final — synthesized from v1 + Phase 1 critique + orchestrator roast

**Issue:** #87 · **Branch:** `issue-87-lec-03-architectures`
**Длительность:** 75 мин (~70 активный + ~5 Q&A/буфер) · **Аудитория:** 3 курс ИУ6 (универсально, без локального binding в chapter)
**Curriculum level:** introductory/overview (Модуль 1, лекция 3 — последняя обзорная перед отраслевыми)
**Дата:** 2026-05-16 · **Phase:** Phase 1 → roast → **USER GATE 0** → Phase 2 chapter
**LO (canon-locked, РПД):** **LO7** primary («Обосновать выбор архитектуры AI: чат, агент, RAG, API, модель — для задачи») + **LO4** secondary («Применить AI-инструменты для типовой аналитической задачи»).
**Slide count: ЗАБЛОКИРОВАН = 30 (s01–s30 monotonic)** — cascade-tracking lock до Phase 2.
**Tone:** инженерно-аналитический, anti-hype. Тезис: *выбор архитектуры — инженерное решение под задачу, не мода; часто правильный ответ — самый простой, иногда — вообще без ИИ.*

**Changelog v1 → v2 (Phase 1 + roast):**
- [R-1] Фикс CJK-обрывка «框架» → «Фреймворк» (orchestrator roast — чистота).
- [meth-P1-3] §5 strict-in пересчитан честно (partial→out по решению #78): не 52%, а **12/30 ≈ 40%**. s01/s14/s26/s29 — partial → НЕ в bucket.
- [meth-P1-4 + roast] §5: добавлена per-artifact таблица strict-in с %-ориентирами; кейсы #13/#14 занесены в chapter deep-dive (book-first: speech не вводит то, чего нет в chapter).
- [meth-P1-1 / reader-P1] LO4 усилен: s28 = worked example (лектор) + mini-apply (студенты) + success-критерий §3 + «mastery = Семинар 3»; человек-валидатор вынесен в отдельный beat s29 (разгрузка s28).
- [meth-P1-2 / reader-structural] Раздел 4 реструктурирован: s24 split → s24 (данные/retention) + s25 (атаки через инструменты, «карта + 4 правила», CVE→chapter/notes); s15 разгружен (PEFT/LoRA only; DPO/RFT → 1 строка + chapter); multi-agent дебаты = 1 строка s22 + chapter deep-dive (закрыт §10-Q5).
- [reader-P1] s03 — явный мост к эмбеддингам Л2; s04 — disclaimer «лестница = карта лекции, не требование понять сейчас»; §7 — список inline-required терминов.
- [reader-P1] fine-tuning — gap пререквизита закрыт: inline-define в s14 (1 предложение) + glossary.
- Hook — **открытый вопрос USER GATE 0** (Air Canada vs $4,200 loop); рекомендация — Air Canada.

**USER GATE 0 — РЕШЕНИЯ ВЛАДЕЛЬЦА (2026-05-16, зафиксировано):**
- **Q1 Hook = Air Canada** (s01). $4,200-loop остаётся в s23.
- **Q2 Глубина chapter = 22k+ слов, БЕЗ верхней границы** (максимальный референс). **Явное документированное owner-решение:** red-flag «>15k слов» из `tools/lecture-production/README.md` §6 СНЯТ для `lec-03/chapter.md` (governance escape-hatch, см. `notes/decisions.md` 2026-05-16). Глава ОБЯЗАНА быть разбита на части (Document Size Limit 600 строк, waiver недоступен) — `chapter.md` (индекс+§0–§2) + `chapter-part2.md` (§3–§5) с двусторонними кросс-ссылками.
- **Q3 plan-v2-final ОДОБРЕН** → Phase 2 chapter draft.

---

## 1. Контекст и зависимости

### 1.1 Промис из Лекции 2 — выполняется
Lec-2 s28 обещала Л3 = «как AI выходит за пределы чата»: RAG (поверх эмбеддингов s10–s12 Л2), tools/function calling, MCP, agent loop. Л3 раскрывает все 4 + добавляет несущую ось «как ВЫБРАТЬ архитектуру» (LO7).

### 1.2 Что студент уже знает / что НЕ повторяем

| Тема | Где в Lec-1/2 | Что Л3 делает |
|---|---|---|
| Типы AI, промпт=роль+задача+контекст | Lec-1 | Используем; не переобъясняем |
| Эмбеддинги, semantic search | Lec-2 §2 | Готовый блок → строим RAG (similarity НЕ переобъясняем) |
| Single-shot / autoregressive inference | Lec-2 §4 s21 | Надстраиваем tool use / agent loop вокруг |
| Температура, 4 ручки API | Lec-2 §4 s19–20 | Не повторяем; API-слой = structured output, function calling, caching |
| ML vs LLM decision tree | Lec-2 s25 | Расширяем до полной лестницы код→…→multi-agent |
| Контекстное окно, «lost in the middle» | Lec-2 §3 s16–17 | Связка с «context rot» (тот же феномен, новый термин — явная сшивка в s08) |
| **fine-tuning** | Lec-1 — поверхностно (тип использования), Lec-2 — нет | **Gap → inline-define в s14 (1 предложение) + glossary**; здесь — как архитектурный выбор |

### 1.3 Курсовая прогрессия
Lec-1 (типы/промпт) → Lec-2 (почему промпт работает) → **Lec-3 (как собрать систему и КАК ВЫБРАТЬ архитектуру)** → отраслевые Lec-4–17 применяют выбор. Парный **Семинар 3** «Архитектурный выбор: чат/агент/RAG/API — 3 кейса» (LO7+LO4) — место mastery LO4.

### 1.4 Сквозные темы курса (canon, обязательны)
- **Безопасность:** API-ключи, уровни доступа, кто видит данные в цепочке агент→инструмент→внешний API→провайдер (s24–s25).
- **Человек vs AI:** человек-валидатор проверяет *результат и факты*, не self-rationale модели (CoT может быть unfaithful) — s07 + s29.
- **Выбор инструмента:** ядро (LO7) — лестница s26 + матрица s27 + чек-лист s28.
- **Паттерны/антипаттерны:** Chain-of-thought (паттерн лекции) + его предел; анти-паттерны — overengineering агентом, fine-tune ради знаний, RAG без observability.

---

## 2. Центральный вопрос и арка

### 2.1 Центральный вопрос
> **«У меня есть задача и доступ к LLM. Какую архитектуру выбрать — и когда правильный ответ "не ИИ"?»**
Задаётся s04; возвращается в каждом «когда НЕ» (s08/s12/s17/s22) и закрывается payoff s26–s28.

### 2.2 Арка (30 слайдов, 75 мин)

| Этап | Слайды | Бюджет | Функция |
|---|---|---|---|
| 0. Открытие+recap+ЦВ | s01–s04 | 8 | Hook (провал неверного выбора); cover+roadmap; recap Lec-2 + мост к эмбеддингам; ЦВ + лестница (с disclaimer) |
| 1. Промпт и границы | s05–s08 | 9 | Дефолт=1 вызов; **Chain-of-thought** + его предел (unfaithful); context engineering / context rot (когда НЕ RAG) |
| 2. RAG | s09–s13 | 12 | Принцип (retrieval поверх Л2-эмбеддингов + LLM); когда; **когда НЕ**; провал на масштабе + Air Canada как grounding |
| 3. Fine-tune vs промпт vs RAG | s14–s17 | 9 | FT не «ушёл» — сузился; PEFT; провал catastrophic forgetting; критерии (гибрид=норма) |
| 4. API·tools·MCP·агенты+безопасность | s18–s25 | 19 | API-слой; MCP; agent loop plan→act→check→iterate; workflow vs agent; провалы агентов; безопасность данных/retention; атаки через инструменты |
| 5. Фреймворк решения + финал | s26–s30 | 12 | Лестница; матрица; чек-лист (LO7 payoff)+LO4 apply; человек-валидатор+NANDA; мост к отраслям+ДЗ+Q&A |
| Буфер | — | 5 | Q&A |

Pacing: slide-times ~55 + retrieval ~8 + переходы ~7 = 70 активный + 5 буфер = 75. Финальная разбивка по слайдам — в chapter Phase 2.

---

## 3. Learning Outcomes

| LO | Формулировка (canon) | Достижение | Slides | Success-критерий |
|---|---|---|---|---|
| **LO7** | Обосновать выбор архитектуры AI (чат/агент/RAG/API/модель) для задачи | Лестница+матрица+критерии «когда НЕ»+чек-лист; каждый раздел даёт «когда НЕ применять» | s04,s08,s12,s17,s22,**s26–s28** | Студент по задаче называет архитектуру И ≥2 причины по осям матрицы И ≥1 «когда это было бы НЕ так» |
| **LO4** | Применить AI-инструменты для типовой аналитической задачи | s28: worked example (лектор применяет чек-лист к задаче A) → mini-apply (студенты, задача B формата С3) | **s28**, s30(ДЗ) | Студент за 2 мин проходит 8-шаговый чек-лист на новой задаче и формулирует обоснованный выбор; mastery — Семинар 3 |

LO4 = применение аналитической рамки выбора к задаче (это и есть «типовая аналитическая задача» инженера-архитектора). Не косметика: worked example + mini-apply + измеримый success + явная передача mastery в Семинар 3.

---

## 4. Slide list (s01–s30 LOCKED)

**Раздел 0 (8 мин):**
- **s01 Hook — Air Canada (3, `case_study`)** [GATE0-Q1 LOCKED] — чат-бот выдумал тариф-политику → трибунал 14.02.2024 обязал платить; «что выбрали (генеративный чат) vs что было нужно (детерм. lookup)». Retrieval 30 сек. *Partial→out из strict-in (урок раскрыт в s13).*
- **s02 Cover+roadmap (0.5, `cover`)** — roadmap 0–5, gold-маркер «Раздел 0».
- **s03 Recap Lec-2 + мост (1.5, `assertion_visual`)** — single-shot inference в центре → 4 обвязки. **Speaker note (reader-P1):** «RAG = semantic search из Лекции 2 §2 + LLM сверху; детали — Раздел 2».
- **s04 ЦВ + лестница (3, `assertion_visual`)** — ЦВ крупно + лестница код→промпт→RAG→workflow→агент→multi-agent. **Disclaimer (reader-P1):** «лестница — карта лекции, не требование понять всё сейчас; каждый уровень разберём».

**Раздел 1 (9 мин):**
- **s05 Дефолт=один вызов (2, `assertion_visual`)** — «самая дешёвая надёжная архитектура — 1 вызов с хорошим промптом; не усложняй без причины».
- **s06 Chain-of-thought (2.5, `case_study`)** — паттерн лекции; worked example без/с CoT; retrieval 30 сек.
- **s07 Предел CoT: текст ≠ мысль (2, `case_study`, IN-BUCKET)** — CoT не обязан отражать реальную причину (Claude 3.7 ~25%, DeepSeek R1 ~39%; Anthropic апр-2025 `[VFY числа]`); урок: человек проверяет результат, не self-rationale.
- **s08 Context engineering (2.5, `assertion_visual`, IN-BUCKET)** — курировать минимальный высокосигнальный контекст; context rot (точность падает с длиной — это «lost in the middle» из Л2 §3, **явная сшивка термина**); когда НЕ RAG: малый стабильный корпус → full-context+caching.

**Раздел 2 (12 мин):**
- **s09 Divider + что такое RAG (1, `section_divider`)**.
- **s10 Принцип RAG (3, `process`)** — retrieval (similarity из Л2) → контекст → генерация с опорой; gold «ответ с цитатой».
- **s11 Когда RAG (2.5, `assertion_visual`)** — знание меняется/большое; нужна свежесть+провенанс; приватная база.
- **s12 Когда НЕ RAG (2.5, `comparison`, IN-BUCKET)** — корпус <~200k ток. → full-context+caching; фикс. политика → детерм. lookup; нет observability retrieval → скрытая бомба.
- **s13 Провал RAG на масштабе (3, `case_study`, IN-BUCKET)** — «вернул что-то ≠ вернул правильное» (legal-AI неверные прецеденты, medical-RAG смешал пациентов; retrieval тих сломался после ~10k док.); Air Canada revisited как grounding; альт.: retrieval-eval/observability, structure-aware chunking, hybrid+rerank. GraphRAG — 1 строка (chapter deep-dive).

**Раздел 3 (9 мин):**
- **s14 «Fine-tuning ушёл»? — нет, сузился (2.5, `assertion_visual`)** — **inline-define (reader-P1):** «дообучение = доп. обучение готовой модели на своих данных; в Л1 — как тип использования, здесь — как архитектурный выбор». 2026: FT = поведение/стиль/формат/политика/дистилляция, НЕ знания. *Partial→out (калибровка области, не провал/критерий).*
- **s15 PEFT вместо full-FT (2, `assertion_visual`)** — LoRA/QLoRA: адаптеры, базовые веса заморожены. **Разгружен (reader-P1):** DPO/RFT — 1 строка + chapter deep-dive.
- **s16 Провал: catastrophic forgetting (2.5, `case_study`, IN-BUCKET)** — узкий агрессивный FT деградирует общие способности (тяжелее с масштабом); нет eval-петли+версии датасета → откат невозможен → не делай. Альт.: PEFT/RAG.
- **s17 Критерии: что куда (2, `comparison`, IN-BUCKET, LO7)** — знание меняется→RAG (не FT); поведение/тон/формат→FT(PEFT); гибрид=норма 2026.

**Раздел 4 (19 мин):**
- **s18 Divider + работа через API (1, `section_divider`)**.
- **s19 API-слой (2.5, `assertion_visual`)** — structured output (JSON-схема), function calling (LLM→JSON→внешняя система→результат назад), prompt caching (числа → speaker notes/`[VFY]`, НЕ на видимый слой — roast).
- **s20 MCP — стандарт (2, `assertion_visual`)** — Anthropic 11/2024; принят OpenAI 03/2025, Google 04/2025; → Linux Foundation. «USB-C для инструментов LLM». `[VFY-day-of]` adoption.
- **s21 Agent loop plan→act→check→iterate (3, `process`)** — «другой AI» лекции; ReAct/Reflexion; gold-точка «check»=валидация.
- **s22 Workflow vs Agent (2.5, `comparison`, IN-BUCKET, LO7)** — Anthropic «Building Effective Agents» 12/2024: найди простейшее; предсказуемая→workflow; непредсказуемая+ценность оправдывает 4–15× токенов→агент. **Multi-agent дебаты Cognition vs Anthropic — 1 строка** (chapter deep-dive).
- **s23 Провалы агентов (3, `case_study`, IN-BUCKET)** — #1 $4,200/63ч в петле (нет budget/loop-лимитов); #3 reliability compounding (5×99%→95%); #15 multi-agent хрупкость на зависимостях. Альт.: budget/loop-gates, checkpoints, single-threaded.
- **s24 Безопасность: данные в цепочке (2.5, `assertion_visual`, IN-BUCKET, SECURITY)** — карта «кто видит данные: агент→инструмент→внешний API→провайдер»; retention: NYT v. OpenAI приказ хранить все логи (#11); граница ZDR Anthropic — third-party/MCP/Files вне ZDR (#12). Правило: карта данных по фиче; не слать регулируемое без ZDR/BAA.
- **s25 Атаки через инструменты (2.5, `case_study`, IN-BUCKET, SECURITY)** — недоверенный контент = команда: GitHub MCP heist (#6); tool poisoning/rug-pull (#8). **Видимый слой: карта + 4 правила** (least-privilege, изоляция недоверенного контента, human-in-the-loop на write, allowlist/pin). CVE-номера → chapter/notes (reader-P1: не на introductory-слайд).

**Раздел 5 (12 мин):**
- **s26 Лестница сложности (2, `process`, LO7)** — код(без ИИ)→промпт→RAG/context-eng→workflow→агент→multi-agent; «подниматься только при необходимости». *Partial→out (framework-payoff, не «провал+урок»).*
- **s27 Матрица + когда НЕ ИИ вовсе (3, `matrix`, IN-BUCKET, LO7)** — оси: объём знания·частота изменений·свежесть/провенанс·стоимость·латентность·аудируемость·риск недетерминизма; нижняя плашка «детерминированная верифицируемая задача → обычный код; ИИ добавил бы только недетерминизм+стоимость+латентность+поверхность инъекции».
- **s28 Чек-лист + apply (3, `summary`+exercise, LO7 payoff + LO4)** — 8 вопросов «прежде чем строить»; лектор worked-example на задаче A → студенты mini-apply задача B (формат С3: «поиск в 200 PDF» / «бот техподдержки на корп. базе»).
- **s29 Человек-валидатор + NANDA (1.5, `assertion_visual`)** — агент делает, человек проверяет результат+факты (не self-rationale; callback s07); MIT NANDA ~95% пилотов без ROI — дело в интеграции, не модели (`[VFY]`, как отчёт). *Partial→out (mixed: судебный/калибровка).*
- **s30 Мост к отраслям + ДЗ С3 + Q&A (1.5 + ≤5 буфер, `summary`+`qa_minimal`)** — «эта рамка — база Лекций 4–17: в каждой индустрии "какая архитектура и почему"». ДЗ=Семинар 3.

---

## 5. AI-Failure & Judgment ≥30% strict-in (честный пересчёт, решение #78 partial→out)

**Strict-in слайды (полностью in-bucket: провал+урок+альт / фундам. ограничение / критерий «не применять» / сравнение с более правильным инструментом):**
s07, s08, s12, s13, s16, s17, s22, s23, s24, s25, s27, s28 = **12 / 30 ≈ 40% по слайдам**; по минутам ≈ 30/70 ≈ **~43%**.
**Partial → OUT (честно НЕ засчитаны):** s01 (hook, урок отложен в s13), s14 (калибровка области FT), s26 (лестница-payoff), s29 (mixed).

**Per-artifact strict-in (holistic, L3 без waiver — каждый меряется отдельно):**

| Артефакт | In-bucket блоки | Ориентир strict-in | Контроль |
|---|---|---|---|
| chapter.md | Детальные кейсы #1,#4,#5,#11,#2 + сводная таблица ограничений + deep-dive boxes (#13 DPD, #14 Chevrolet/MyCity, #6–#12 security, multi-agent дебаты) + разделы «когда НЕ» | **≥40%** | methodology-critic Phase 3 |
| slides | 12 strict-in слайдов (assertion-evidence) | **≥40%** (12/30) | methodology-critic Phase 7 |
| speech | Нарратив #4 (hook), #1 ($4,200), #13/#14 (есть в chapter → book-first OK), критерии «когда НЕ» в каждом разделе | **≥35%** | methodology-critic Phase 10 |

Waiver НЕ применяется и не нужен — failure/judgment = несущая линия лекции (LO7). Counter-check: single-artifact concentration отсутствует (распределено по 5 разделам × 3 артефакта).

---

## 6. Glossary lock (черновой; финализируется Phase 4 после chapter)

архитектура AI-системы · промпт · few-shot · **Chain-of-thought** (CoT 1× в скобках) · **RAG** (поиск-дополненная генерация 1×) · retrieval · **fine-tuning/дообучение** (inline-define s14; PEFT/LoRA расшифровка 1×) · контекст-инжиниринг (≠ промпт-инжиниринг) · tool use / function calling (вызов инструментов 1×) · **MCP** · агент (plan→act→check→iterate) · workflow (предопределённые пути; в chapter — «сценарий/рабочий поток») · grounding (опора на источник) · observability (наблюдаемость) · **ZDR** · least-privilege · prompt injection · distillation (дистилляция) · catastrophic forgetting · context rot.
Forbidden anglicisms (speech Англицизм Pass): пайплайн→конвейер, фоллбэк, эдж-кейс, инсайт.

---

## 7. Forbidden additions + inline-required terms

**Forbidden (No Extra Content, без approval):** формулы attention/трансформера (Л2); код SDK >3 строк на слайде; vendor-pricing цифры на видимом слое (→ `[VFY]`/notes); CVE-номера на видимом introductory-слое (→ chapter/notes); «Лектору»/«Вы здесь»/subtitle/тайминг на слайдах (кроме roadmap s02); slide add/delete без user request (REPORT); color-only highlight без текст-маркера; не запрошенный cross-slide мост-текст; footer-tax; MCP wire-format / RFT-DPO математика / полный multi-agent дебат — только chapter deep-dive.

**Inline-required (определить при первом упоминании — reader-P1):** faithfulness, ZDR, least-privilege, grounding, observability, distillation, prompt injection, retrieval, function calling, workflow, context rot, PEFT, fine-tuning.

---

## 8. Микро-упражнения / retrieval

| Слайд | Тип | Длит. | Активность |
|---|---|---|---|
| s01 | open Q | 30 сек | архитектура для «узнать правило тарифа»? |
| s06 | think pause | 30 сек | поможет ли CoT этой задаче? |
| s13 | poll | 20 сек | RAG вернул ответ — как узнать, что правильный? |
| s28 | apply (LO4) | 2 мин | чек-лист к задаче B формата С3 |

≈5–6 мин, включено в §2.2.

---

## 9. Свежесть (fact-checker; freshness enforced)

`[VFY-day-of]`: s07 (CoT %), s20 (MCP adoption/принятие), s24 (retention статус). `[FACT-CHECK]` (preprint/single-source, framing «исследования показывают»/«illustrative»): catastrophic-forgetting механизмы (arXiv 2026-01), $4,200 loop (single-author 2026-04), MIT NANDA (отчёт+методология, не закон). prompt caching числа — speaker notes only, vendor-published `[VFY]`. CVE-2025-6514/49596, GitHub MCP heist, NYT v. OpenAI, Air Canada 14.02.2024 — исторические, cite as-is (в chapter/notes, не на видимом слое).

---

## 10. Решения USER GATE 0

| # | Вопрос | Рекомендация |
|---|---|---|
| Q1 | **Hook s01:** Air Canada vs $4,200 agent loop | **Air Canada** — universal, юр. ставки, прямо рамкирует тезис «неверная архитектура = последствие»; $4,200 остаётся в s23 |
| Q2 | **Глубина chapter 16–22k слов** (выше governance red-flag 15k) — нужно явное owner-решение (память feedback_chapter_depth + governance escape-hatch) | Подтвердить: глава = референс+Q&A-бэкап; слайды/речь = 75-мин срез. methodology-critic подтвердил методическую корректность |
| Q3 | Общее одобрение plan-v2 → переход к Phase 2 chapter | — |
| — | Q4 (LO4) и Q5 (multi-agent) из v1 — **закрыты** в v2 (s28 worked+mini-apply; multi-agent 1 строка+chapter) | — |

---

## 11. Source-of-truth chain
```
notes/lecture-3-review/
├── 2026-05-16/plan-v1.md (orchestrator draft)
├── 2026-05-16/phase1-critique/{methodology-critic.md, reader-text-only.md}
└── final/plan-v2-final.md (ЭТОТ ФАЙЛ — после roast+Phase1; → USER GATE 0 → Phase 2)
library/lectures/lec-03/
├── chapter.md [PRIMARY] ← derives from v2 (глубокий референс; feedback_chapter_depth)
├── deck.yaml + slides/*.md ← derived from chapter
└── speech.md ← derived from chapter + slides
```

## 12. Phase 2 brief (book-editor, USER GATE 0 ✅ 2026-05-16)
`library/lectures/lec-03/chapter.md` — **глубокий расширенный референс, 22k+ слов БЕЗ верхней границы (red-flag >15k снят явным owner-решением Q2; decisions.md 2026-05-16)**. Document Size Limit 600 строк — waiver НЕТ → разбить: `chapter.md` (frontmatter+§0 Введение/Цели+§1 Промпт/границы+§2 RAG) + `chapter-part2.md` (§3 Fine-tune+§4 API·MCP·агенты+безопасность+§5 Фреймворк) с двусторонними кросс-ссылками; общий changelog в `chapter.md`. 5 разделов (mirror §2.2: Промпт/границы → RAG → Fine-tune vs промпт vs RAG → API·tools·MCP·агенты+безопасность → Фреймворк решения) + Введение/Цели. Deep-dive boxes «что не вошло, но важно»: GraphRAG internals, RFT vs DPO, MCP wire-format, ReAct/Reflexion/Plan-Execute, полный дебат Cognition↔Anthropic multi-agent, vendor retention детали, CVE-хронология, кейсы #13 DPD / #14 Chevrolet-MyCity. «Вероятные вопросы аудитории + развёрнутые ответы» в конце каждого раздела (Q&A-бэкап). LO7+LO4 (success-критерии §3). Glossary §6 + Forbidden/inline §7 — ENFORCED. `[FACT-CHECK]`/`[VFY]` по §9. Speaker-notes markers `[for-slide-sNN]`, s01–s30 monotonic. Tone: инженерно-аналитический, anti-hype, strict-in ≥40% holistic. После draft — Phase 3 (methodology-critic + fact-checker + reader-text-only).

**Status:** v2-final ready → **USER GATE 0** (Q1–Q3).
