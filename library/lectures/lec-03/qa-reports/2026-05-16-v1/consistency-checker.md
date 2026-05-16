# Consistency Checker Report — Лекция 3 — 2026-05-16 (Phase 7 / build-deck Phase 4)

**Scope:** cross-artifact alignment **chapter (source of truth) ↔ slides** (deck.yaml + slides/*.md + rendered/snapshots/*.png). Speech.md ещё не существует (Phase 9) — вне scope.
**Inputs:** chapter v1.1 finalized (3 части, ~22450 слов) · deck.yaml v1 (30 слайдов) · slides/s01–s30.md · 30 PNG-снапшотов · glossary.yaml (locked 2026-05-16) · plan-v2-final.md.
**Mode:** chapter+slides full + terminology-only sub-mode (glossary LOCK enforced).
**Issue:** #87.

## VERDICT: APPROVE-CLEAN

Слайды полностью согласованы с главой. 0 P0, 0 P1, 3 P2 (косметика, не блокеры). Покрытие LO7/LO4 — полное; все цифры/даты/атрибуции совпадают с главой; терминология соблюдает glossary LOCK без forbidden-форм; нет orphan-ссылок; нумерация кейсов расходится между chapter (#1/#3/#15) и slides (1/2/3) — но это **намеренная introductory-деривация** по plan §7, а не drift (book-first: chapter wider, slide simplifies — допустимо). USER GATE B не блокируется этим отчётом.

## Severity counts

- **P0** (factual contradiction / missing coverage): **0**
- **P1** (significant drift): **0**
- **P2** (minor inconsistency): **3**

## Cross-artifact matrix (ключевые концепты / цифры / LO)

| Концепт / LO / Число | Chapter | Slide | Видимый слой (PNG) | Aligned? |
|---|---|---|---|---|
| Центральный вопрос (дословно) | §Введение L103 | deck.yaml L16 / s04 L22 | s04.png — verbatim | ✓ (P2: глифы кавычек) |
| LO7 (обосновать выбор) | §Цели LO7 | 30/30 слайдов | s04/s26/s27/s28 payoff | ✓ |
| LO4 (применить рамку) | §Цели LO4; §5.3 | s02,s04,s28,s30 | s28 worked+mini-apply | ✓ |
| Air Canada дата 14.02.2024 | §Введение L89 / §2.5 L314 | s01, s13 | s01.png / s13.png | ✓ |
| CoT faithfulness Claude 3.7 ~25% / DeepSeek R1 ~39% | §1.3 L157 (25%/39%) | s07 | s07.png «~25%»/«~39%» | ✓ |
| reliability 5×99%≈95% / 10→90% / 20→82% | §4.5 L49 + Box5 L274 | s23 | s23.png chart+числа | ✓ |
| $4,200 / 63ч; $1,000 к 12ч | §4.5 L46 | s23 | s23.png «$4 200 за 63 часа» | ✓ |
| MIT NANDA ~95%; 150 интервью+350+300 | §5.4 L257 / Box5 L276 / Источники L353 | s29 | s29.png «~95%» | ✓ |
| ~200k токенов (корпус в окно) | §1.5 L184 / §2.3 L284 / Q&A L356 | s08, s12 | s12.png «~200k» | ✓ |
| MCP adoption 11/2024→03/2025→04/2025→фонд | §4.2 L194 | s20 | s20.png mini-timeline | ✓ |
| Лестница 6 ступеней (код→…→multi-agent) | §5.1 L162-174 | s04, s26 | s04.png / s26.png | ✓ |
| Матрица 7 осей × 7 архитектур + нижняя плашка | §5.2 L195-219 | s27 | s27.png — ячейки совпадают | ✓ |
| Чек-лист 8 шагов | §5.3 L228-235 | s28 | s28.png — 8 пунктов | ✓ |
| Air Canada source (McCarthy Tétrault / ABA / Barnett) | Источники L321-322,335 | s01/s13 footer | s13.png footer | ✓ |
| Нумерация кейсов #1/#3/#15, #6/#8/#11/#12 | §4.5/§4.6/§4.7 канон | s23/s24/s25 → локально 1/2/3, без # | без # на видимом | ✓ намеренно (P2-3) |
| Glossary watched-термины (25) | chapter inline-define | slides | визуально сверено | ✓ 0 forbidden |

## DISCREPANCIES

### D1 — Глифы кавычек в центральном вопросе
**Severity:** P2
**Where:** chapter.md L103 `"не ИИ"` (прямые ASCII) vs deck.yaml L16 / s04 L22 `«не ИИ»` (ёлочки) — PNG s04 показывает «не ИИ».
**Issue:** одинаковый текст, разный типографский глиф кавычек вокруг «не ИИ». Семантически идентично; на восприятие студента не влияет.
**Recommendation:** опционально унифицировать на «ёлочки» в chapter.md L103 при следующей правке главы (book-first: меняем chapter, т.к. slide-форма «ёлочки» — корректная русская типографика). Не блокер, можно отложить.

### D2 — RAG-alias «поиск-дополненная генерация» использован более 1×
**Severity:** P2
**Where:** glossary.yaml: `RAG (Retrieval-Augmented Generation)`, alias `поиск-дополненная генерация (1×)`. Встречается: s09 assertion+visible (section title — 1 видимый), s10 notes, s02 notes, s09 notes.
**Issue:** Правило glossary — alias 1× при первом упоминании. На **видимом слое** alias появляется один раз корректно (s09 заголовок раздела «RAG: поиск-дополненная генерация» — это и есть первое введение). Дополнительные вхождения — только в speaker notes (s02/s10/s09), где это связный студенческий текст, а не повтор канона на слайде. Формально это не нарушение (notes ≠ visible canon), но стоит зафиксировать как наблюдение.
**Recommendation:** оставить как есть — видимый слой соблюдает «1×»; в notes пояснительный парафраз допустим (notes — для self-study). Не фиксить.

### D3 — Нумерация кейсов: chapter #1/#3/#15 vs slides локально 1/2/3
**Severity:** P2 (намеренная деривация, НЕ drift)
**Where:** chapter §4.5 использует канонические сквозные номера `Провал #1 / #3 / #15` (из `notes/research/lecture-3/failures-and-limitations.md`), §4.6 `кейс #11/#12`, §4.7 `кейс #6/#8`. Slide s23 нумерует локально `1. Петля без лимитов / 2. Reliability compounding / 3. Мульти-агентная хрупкость`; s24/s25 не выводят канонические # вообще.
**Issue:** Студент, читающий главу (#1/#3/#15), затем слайды (1/2/3), видит разную нумерацию **для тех же кейсов**. Факты, уроки, альтернативы идентичны — расходится только internal research-tracking индекс.
**Recommendation:** **НЕ фиксить.** Это соответствует plan §7 («CVE-номера / трекинг-индексы на видимом introductory-слое → chapter/notes») и introductory curriculum level. Канонические # — артефакт research-нумерации, не учебная сущность; их отсутствие на слайдах — корректная упрощающая деривация (book-first: chapter — wider reference, slide — 75-мин срез). Зафиксировано как осознанное расхождение, одобренное планом, а не как ошибка слайда.

## Coverage parity (полное)

- **chapter_ref → существование:** все 30 `chapter_ref` в deck.yaml указывают на реально существующие §-разделы; каждый `[for-slide-sNN]` (N=01..30) присутствует в chapter (1–7 вхождений на слайд). 0 orphan.
- **LO покрытие:** LO7 — на всех 30 слайдах; LO4 — s02/s04/s28/s30 (roadmap + apply), payoff §5.1/§5.2/§5.3 → s26/s27/s28. Совпадает с plan §3.
- **Assertion ⊂ chapter:** каждый slide.assertion проверен против `[for-slide-sNN]`-блоков главы — ни одного «слайд утверждает то, чего нет/иначе в главе». Spot-проверены тяжёлые: s07 (faithfulness 25/39 — §1.3), s13 (3 кейса+Air Canada — §2.4/2.5), s16 (forgetting растёт с масштабом — §3.3), s23 (3 провала+числа — §4.5), s24 (ZDR границы — §4.6), s27 (матрица — §5.2 ячейка-в-ячейку), s28 (8 шагов — §5.3).
- **Раздел chapter → slide-блок:** §1–§5 + Введение → s01–s30, порядок секций идентичен (Р0→Р1→Р2→Р3→Р4→Р5). Точки возврата ЦВ (§1.5/§2.3/§3.4/§4.4/§4.5) → s08/s12/s17/s22/s23 — соответствуют.
- **Deep-dive / Q&A в slide:** корректно НЕ вынесены на видимый слой (DPO/RFT, multi-agent дебат Cognition↔Anthropic, CVE-хронология, GraphRAG) — слайды помечают «в главе» (s15/s21/s22/s24/s25 sub-caption). Соответствует book-first + plan §7.

## Terminology-only sub-mode (glossary LOCK enforced)

- **Forbidden-формы:** grep по 25 watched-терминам + forbidden-списку (`раг`, `пайплайн`, `prompt` (lat) как термин, `файнтюнинг`, `фью-шот`, `тулюз`, `воркфлоу`, `ретривал`, `эм-си-пи`, `цепочка мыслей` как термин, `промпт-инжиниринг` как синоним контекст-инжиниринга, англицизмы фоллбэк/эдж-кейс/инсайт) по slides/*.md + видимому слою PNG → **0 нарушений**.
  - `prompt`-вхождения в slides — только компаунды `prompt injection` / `prompt caching` / hex-цвета / chapter_ref — НЕ как русский термин «промпт». ОК.
  - `промпт-инжиниринг` на s08 — это **корректное chapter-зафиксированное различение** (промпт-инжиниринг ≠ контекст-инжиниринг, §1.4), не forbidden-синоним. ОК.
- **Canonical соблюдён:** «архитектура AI-системы», «промпт», «RAG», «retrieval», «grounding», «observability», «golden set», «fine-tuning (дообучение)», «PEFT (LoRA/QLoRA)», «distillation», «контекст-инжиниринг», «context rot», «tool use / function calling», «MCP», «агент», «workflow», «prompt injection», «least-privilege», «ZDR», «BAA», «catastrophic forgetting», «faithfulness», «Chain-of-thought», «few-shot» — формы на слайдах дословно совпадают с canonical из glossary и с inline-define в главе (sample-проверка inline-define: s07 faithfulness, s10 grounding/retrieval, s12 observability, s14 fine-tuning, s15 PEFT, s16 catastrophic forgetting, s20 MCP, s24 ZDR/least-privilege/BAA, s25 prompt injection — все совпадают с §-дефинициями).
- **CoT alias (наблюдение, не нарушение):** glossary разрешает `CoT (1× в скобках при первом упоминании)`. Первый видимый ввод термина — s06 title «Chain-of-thought (пошаговое рассуждение)» (canonical ✓), далее по тексту `CoT`. На s04 (раньше по арке) `CoT` появляется в подписи ступени лестницы как уже-знакомая аббревиатура без раскрытия — но s04 не вводит термин (это roadmap-якорь, формальный ввод на s06). Граничный кейс, оставлен как есть: не P-级 — canonical-форма присутствует на слайде формального ввода (s06).

## Orphan-reference detection

- deck.yaml slide-IDs s01–s30 monotonic, без пропусков/дублей.
- Slide-to-slide callbacks: `callback s07` (s21 ×2, s29 ×3) → **s07 существует** (CoT faithfulness — корректная цель: «человек проверяет результат, не self-rationale»). 0 orphan.
- Chapter→slide refs: `слайд s19` (chapter.md L22 changelog P1-2, chapter-part2.md L183 downstream-нота) → **s19 существует**. Корректно.
- Видимый слой PNG (s21/s29): «callback s07» отображается — цель валидна.
- Никаких ссылок на удалённые/несуществующие слайды (slide-count LOCKED 30, удалений не было).

## Арка / sequence

Порядок s01–s30 строго следует chapter (§Введение→§1→§2→§3→§4→§5) и plan §2.2 (Р0 8м · Р1 9м · Р2 12м · Р3 9м · Р4 19м · Р5 11–12м). Section-divider'ы s09 (Р2) / s18 (Р4) на месте. Точки возврата центрального вопроса (chapter явно нумерует «первая/вторая/…/пятая точка»: §1.5, §2.3, §3.4, §4.4, §4.5) → отражены на s08/s12/s17/s22/s23 в assertion и notes. Финальный мост s30 → Лекции 4–17 + Семинар 3 совпадает с §5.5.

## book-first verdict

При проверке конфликтов chapter↔slide — **конфликтов уровня P0/P1 не найдено**. Все 3 P2 — косметика (D1 глифы) либо намеренная корректная деривация (D2 notes-парафраз, D3 introductory-упрощение нумерации), где slide правомерно уже/проще главы. **Глава НЕ требует правок** от consistency-checker'а. Issue для book-editor не поднимается.

## Топ-фиксов (per artifact)

- **Chapter:** ничего не требуется (опционально, при будущей правке: D1 — унифицировать кавычки `"не ИИ"`→`«не ИИ»` в L103 для типографической чистоты; не блокер GATE B).
- **Slides:** ничего не требуется. D2/D3 — оставить как есть (соответствуют glossary visible-rule и plan §7).
- **Speech:** N/A (не существует; Phase 9).

## PROPOSED GLOSSARY UPDATE

Нет. glossary.yaml canonical-формы оптимальны и соблюдаются слайдами без drift. Rename-предложений нет.
