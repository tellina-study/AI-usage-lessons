# Consistency Checker Report — Лекция 5 — 2026-05-17 (Phase 7, mode=chapter+slides)

**Scope:** chapter (chapter.md + chapter-part2.md + chapter-part3.md, finalized v2, source of truth) ↔ slides (33: s01–s32 + s04a) + deck.yaml/deck-part2.yaml. Glossary `glossary.yaml` (status=locked 2026-05-17) used as terminology canon. Plan `notes/lecture-5-review/final/plan-v2-final.md` used as arc canon. Read-only.

## VERDICT: **APPROVE-CLEAN**

Counter-check applied: **0** terminology-drift on key terms (all variants are glossary-sanctioned aliases), **0** numeric/attribution drift, **0** orphan refs, **0** §-leaks/LO-code leaks in visible body, central question character-identical, arc/failure-thread/Knight-callback fully consistent. No P0/P1. One cosmetic P2 (intra-slide alias mix in s13) — does not block; optional polish.

## Severity counts
- P0 (factual contradiction / missing coverage): **0**
- P1 (significant drift / tone / missing cite): **0**
- P2 (minor inconsistency): **1**

## Cross-artifact matrix (concept / LO / number → chapter § → slide → aligned?)

| Item | Chapter | Slide(s) | Aligned? |
|---|---|---|---|
| Central question (verbatim) | §0.3 | deck.yaml `central_question`; s04 visible | ✓ char-identical |
| Cover tagline (shortened ЦВ) | §0 framing | s02 «Под какую задачу — какой тип ИИ, почему именно он, и где он ломается» | ✓ intentional tagline |
| Единый паттерн карточки (5 шагов) | §0.4 | s04 (5 шагов teal-лентой) | ✓ same 5 steps |
| Карта 5 типов + CV-пласт | §0.4 | s03, s04 (прогноз·аномалии·скоринг·LLM·recsys + CV) | ✓ same set/order |
| 4 понятия «с нуля» (FP/FN, матрица, прокси-bias, distribution shift) | §0.2 | s03 visible строка | ✓ same 4 |
| LO1 (классиф. типов) primary | §0.5 | s04, s05–s28, s29 (matrix payoff) | ✓ |
| LO2 (применимость) | §0.5 | s06, s09, s14, s23, s28, s30 | ✓ |
| LO3 (риски/безопасность) | §0.5 | s13, s18, s23, s24, s30, s31 | ✓ |
| LO6 (ошибки/ограничения, Understand) | §0.5 | s01, s09, s14, s18, s21, s22, s23, s28, s29, s30 | ✓ Understand-уровень держится |
| Zillow $300M/кв · $500M+ · ~2000 (~25%) · −25% | §0.1, §1.5 | s01 (все 4), s09 (раскрытие) | ✓ identical |
| distribution shift inline-define | §1.5 | s09 visible+notes | ✓ same intuition |
| асимметрия цены ошибки (≈0 vs десятки тыс.$×N) | §1.5 | s09 | ✓ |
| Knight Capital $440M / ~45 мин 2012 (callback, не кейс) | DDB1 + §1.5/§2.4/§3.5/§6.2 | s09, s14, s19 callback + s30 в 5-принципном синтезе | ✓ callback-only, never standalone |
| Opendoor — тот же тип ИИ, выжил | §1.5, DDB1 | s09 | ✓ |
| X5 >70% · +5 млрд ₽ · −2% списаний | §1.3 | s07 (все 3, +VFY footer) | ✓ identical, «заявлено компанией» |
| Магнит F&R после SAP/Blue Yonder | §1.3 | s07 «по заявлению компании» | ✓ |
| Stripe −32% / JPMorgan −30% / Visa ~$40 млрд FY2023 (~80 млн) | §2.2 | s12 (все, vendor-reported footer) | ✓ identical (Visa $40 млрд, не $30) |
| Банк России антифрод (по материалам, не голое число) | §2.2 | s12 «по материалам Банка России, 2025» | ✓ атрибуция держится |
| Матрица ошибок TP/TN/FP/FN; FP=1-й род / FN=2-й род | §2.3 | s13 (2×2) | ✓ |
| accuracy лжёт (1M / 1000 фрода → 99,9%) | §2.3 | s13 | ✓ identical example |
| cost-sensitive / precision↔recall | §2.3 / §2.4 | s13 / s14 | ✓ различитель сохранён |
| FP $5 кофе vs $5000 лечение | §2.4 | s14 | ✓ identical |
| Сбер ~100% ИИ · до 5000 параметров · +350 млрд ₽/2023 · >80% opt-out | §3.2 | s17 (все, VFY footer) | ✓ identical, «по заявлению банка» |
| Apple Card: NYDFS НЕ нашёл нарушения (~400k) | §3.4 | s18 «доказана дискриминация — фактологически неверно» | ✓ точная формулировка held |
| прокси-предвзятость механизм с нуля | §3.4 | s18 | ✓ same «на пальцах» |
| Критерий «автоматизация без gate» (3 типа → 1 класс) | §3.5 | s19 (Zillow/fraud/Knight → критерий-формула) | ✓ |
| Т-Банк >40% / 70% планируют голос — НЕ «>90%» (подмена базы кл.5) | §4.1 | s21 (verified + «>90%»=сам урок) | ✓ counter-example correct |
| 5 классов ошибок fact-checking | §4.2 | s22 | ✓ same 5 |
| grounding аналогия (студент со справочником) | §4.3 | s22 | ✓ |
| Air Canada (callback Л3, суд 02.2024) | §4.4 | s23 «callback, не дубль Л3» | ✓ callback framing held |
| Klarna ~2/3 · 11→<2 мин · ~$40 млн · откат 2025 | §4.4 | s23 (все, заявлено) | ✓ identical, augmentation-урок |
| Двухуровневый вывод (тип необходим, не достаточен) | §4.5 | s24 (pivot, не ретро-сводка) | ✓ |
| collaborative/content-based/hybrid + слабости | §5.1/§5.2/§5.4 | s26, s27 | ✓ canonical terms |
| Amazon ~35% / Netflix ~75% — историческая McKinsey-оценка | §5.3 | s27 (footer «НЕ свежий headline») | ✓ fact-discipline held |
| Wendy's $20 млн / surge-pricing backlash 02.2024 / откат | §5.5 | s28 | ✓ identical |
| прокси≠цель — единый класс (accuracy/скоринг/Klarna/filter bubble) | §5.5, DDB5 | s28, s29 | ✓ same unifying class |
| Матрица «задача × тип ИИ» + нижняя строка «не ИИ вовсе» | §6.1 | s29 (6 строк, нижняя gold) | ✓ |
| 5 проявлений «необходим, но не достаточен» | §6.2 | s30 (Zillow/Apple Card/Air Canada/Klarna/Wendy's) | ✓ |
| ФЗ-152/PII/биометрия/on-prem · KYC/liveness/JWO >1000 | §6.3 (А+Б) | s31 (2 панели, агрегация 5 sub-маркеров) | ✓ агрегация корректна |
| Just Walk Out >1000 ревьюеров (Amazon оспаривал масштаб) | §6.3, DDB6 | s31 «Amazon оспаривал масштаб» | ✓ двусторонность held |
| Чек-лист 8 пунктов + Семинар 5 (Apply, Bloom-граница) | §6.4/§6.5 | s32 | ✓ граница лекция≠семинар held |
| РПД «>90%» НЕ как факт | §4.1 (class-5 подмена базы) | s21 (используется ТОЛЬКО как counter-example) | ✓ |

## Coverage parity

- **Chapter [for-slide-sNN] markers vs deck:** 33 distinct markers in chapter (s01–s32 + s04a) — exactly match 33 deck slides. **0 chapter-LO/section without slide.** s02 has no chapter marker — expected (cover, DERIVED; deck `chapter_ref §0.2` is a soft context pointer, not a hard-marker requirement). No P0.
- **s31 aggregation:** chapter §6.3 has 5 `[for-slide-s31]` sub-block markers (А данные+закон / Б CV-пласт); plan §4 LOCKED = 1 slide. s31 aggregates both into a 2-panel slide — visible content covers all 5 sub-blocks (ФЗ-152/PII/on-prem-vs-cloud + KYC/liveness/биометрия-необратима/JWO). Coverage complete; aggregation documented in deck `totals.s31_decision`. ✓
- **s04a divider:** chapter §1.1 `[for-slide-s04a]` → s04a divider. Consistent. ✓
- **Slide assertions ↔ chapter grounding:** every slide assertion traces to a chapter passage with the same claim and the same numbers. No slide overclaims beyond chapter.
- **Interactive moments:** s01 open_question / s09 think_pause / s14 poll / s23 think_pause / s28 think_pause / s32 qa — each reflected in chapter as Think-pause/Poll/Q&A beat at the matching §. ✓

## Terminology drift (terminology-only sub-mode, vs locked glossary.yaml)

All cross-artifact term forms checked against `glossary.yaml` (status=locked). **No drift detected** — every observed variant is an explicitly glossary-sanctioned alias:

- `distribution shift` ↔ `дрейф распределения` — both canonical (glossary L23–24). "дрейф модели"/"дрейфуют"/"дрейф паттернов фрода" appear in connected prose as inflections, not competing canonical forms; the term is always introduced via canonical form first (s09). ✓
- `прокси-предвзятость` (canonical) / `прокси-bias` (alias, glossary L59–62) — both used appropriately; visible body uses canonical at first intro (s03, s18 «прокси-предвзятость»), alias `прокси-bias` for compact callbacks (s22/s29) — matches chapter usage pattern. ✓
- `прокси≠цель` / `прокси ≠ цель` — the chapter's single unifying error class (glossary L99–102); spacing variant is purely typographic, same concept, no semantic drift. "прокси вместо цели"/"смещение через прокси" appear in connected prose as the same concept's natural-language restatement (matches chapter §5.5/DDB5 wording) — not a competing canonical label. ✓
- `false positive/false negative (FP/FN)`, `ошибка 1-го/2-го рода` ↔ `ошибка первого/второго рода` — all glossary aliases (L39–42). ✓
- `поиск аномалий` ↔ `anomaly detection`; "обнаружение аномалий" (s12) — glossary alias-equivalent (note L31–34: «поиск аномалий (anomaly detection)»), used in connected prose, no drift. ✓
- `collaborative/content-based/hybrid recommender`, `cold-start/popularity bias/over-specialization/serendipity`, `filter bubble`, `dynamic pricing`, `grounding`, `KYC/liveness/hidden human cost`, `circuit-breaker/kill-switch`, `SHAP`, `iBuying`, `augmentation` — all consistent with chapter + glossary canonical forms. ✓
- Forbidden anglicisms (пайплайн/фоллбэк/эдж-кейс/инсайт): **0 occurrences** in slides. ✓

## Orphan reference / leak detection

- Slide-to-slide / chapter-§ refs in slide visible body: **0** orphan refs (`→sNN`, `см. sNN`, `см. слайд`, `§X.X` all = 0 in visible body). ✓
- LO codes / `[VERIFY-DAY-OF]` / `[FACT-CHECK]` / `[for-slide]` / «Лектору» / «Вы здесь» in visible body: **0** (single `LO1` hit is in s29 frontmatter `learning_goal` — exempt). ✓
- All 33 deck IDs (s01–s32 + s04a) present as slide files; loader cross-link (deck.yaml↔deck-part2.yaml) consistent; no deleted/renumbered slide producing orphan. ✓

## Forward-pointer Л7 direction (introduce-here, deepen-in-L7 — not bridge-back)

Verified correct in all 3 visible-body forward-pointers:
- s13: «Формальный аппарат (sensitivity/specificity) **строится в Лекции 7**» (chapter §2.3 forward-pointer → Л7 §2.2). ✓
- s18: «Канонический разбор механизма (Obermeyer/Optum) — **Лекция 7 (медицина)**» (chapter §3.4 → Л7 §4.3). ✓
- s31: «Bias компьютерного зрения … **углубляется в Лекции 7**» (chapter §6.3 → Л7 §2.5). ✓

§-numbers (§2.2/§4.3/§2.5) correctly **stripped** from visible body (slides say only «Лекция 7 (медицина)»), retained in chapter — semantically consistent, no §-leak. ✓

## Central question / arc / failure-thread

- **Central question:** character-identical across chapter §0.3, deck.yaml `central_question`, s04 visible. s02 cover uses the shortened tagline (intentional cover subtitle derived from §0 framing) — not a contradiction. ✓
- **5 ЦВ-return points:** chapter (§1.5/§2.4/§3.4/§4.4/§5.5) → s09 «первый» / s14 «второй» / s18 «третий» / s23 «четвёртый» / s28 «пятый, последний» — exact order/count/anchoring. ✓
- **6 типов ИИ:** same set/order/analogies (прогноз→товаровед; аномалии→облако+выброс; скоринг→инспектор; LLM→студент со справочником; recsys→продавец; CV-пласт сквозной) — s03/s04/s29 carry the same map as chapter §0.4/§6.1. ✓
- **Failure-нить Zillow→fraud-FP→Apple Card→Air Canada/Klarna→Wendy's:** identical chain and ordering in chapter Заключение and across s09→s14→s18→s23→s28→s30 synthesis. Knight = callback-only (s09/s14/s19 + s30 list), never a standalone failure case — exactly as chapter (DDB1 detail + callbacks). ✓

## DISCREPANCIES

### D1 — s13 intra-slide alias mix (1-го/2-го рода vs первого/второго рода)
**Severity:** P2 (minor cosmetic; NOT drift — both forms are glossary L40 sanctioned aliases)
**Where:** s13 visible matrix uses «*(ошибка 1-го рода)*» / «*(ошибка 2-го рода)*»; s13 speaker notes use «ошибка первого рода» / «ошибка второго рода». Chapter §2.3 uses «Ошибка первого рода» / «Ошибка второго рода».
**Issue:** Within a single slide the visible body and its own notes use two different (both legal) alias forms of the same canonical term. Not a contradiction and not cross-artifact drift (glossary explicitly lists both as aliases), but for the slide where this term is *introduced from scratch* (G-2), one consistent form per slide reads cleaner for a first-time student.
**Recommendation (optional polish, slides only — chapter is source of truth and correct):** in s13 visible matrix, align to the chapter/notes form «(ошибка первого рода)» / «(ошибка второго рода)» for intra-slide consistency at the point of first introduction. No chapter change. Non-blocking — APPROVE-CLEAN stands with or without this polish.

## Coverage gaps
None. Every chapter LO, section, in-bucket failure block, deep-dive-derived criterion, and number has a corresponding slide; no slide assertion lacks chapter grounding; no slide introduces a claim/number absent from chapter.

## Топ-фиксов (per artifact)
- **Chapter:** none (source of truth, internally consistent, no own P0/P1).
- **Slides:** (optional P2 only) s13 — unify «1-го/2-го рода» → «первого/второго рода» in visible matrix for intra-slide consistency at first-introduction point.
- **Speech:** N/A this phase (Phase 7 = chapter↔slides; speech check is Phase 10).

## Note for orchestrator
chapter↔slides alignment is exceptionally tight: numbers, attributions, fact-checking caveats (Visa $40 млрд not $30; РПД «>90%» used only as the base-substitution counter-example; Amazon/Netflix as historical McKinsey estimate; Just Walk Out two-sided framing; Apple Card «NYDFS не нашёл нарушения»), terminology, central question, arc, and the Knight-as-callback discipline are all carried into slides without drift. Glossary lock is respected. No PROPOSED GLOSSARY UPDATE needed. Verdict APPROVE-CLEAN; the single P2 is optional polish, not a gate blocker.
