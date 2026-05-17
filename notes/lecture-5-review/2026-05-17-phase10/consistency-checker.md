# Consistency Checker Report — Лекция 5 — 2026-05-17 (Phase 10, mode=full: chapter ↔ slides ↔ speech)

**Scope:** chapter (chapter.md + chapter-part2.md + chapter-part3.md, finalized v2, ~22650 слов, source of truth) ↔ slides (33 LOCKED: s01–s32 + s04a, deck.yaml + deck-part2.yaml) ↔ speech (speech.md, v1 draft, ~5650 stripped слов). Glossary `glossary.yaml` (status=locked 2026-05-17) — terminology canon. Plan `notes/lecture-5-review/final/plan-v2-final.md` (v2-final) — arc canon. Phase 7 baseline `qa-reports/2026-05-17-v1/consistency-checker.md` (APPROVE-CLEAN, chapter↔slides) used as regression reference. Read-only.

## VERDICT: **APPROVE-WITH-POLISH**

Counter-check applied (REVISE triggers: terminology drift on key term / numeric drift / ЦВ not char-identical / orphan ref): **0** terminology-drift on key glossary terms (all observed variants are glossary-sanctioned aliases, introduce-at-first-use discipline held in all 3); **0** numeric/attribution/date drift across all 3 artifacts; **0** orphan refs (speech covers all 33 LOCKED slides 1:1, no deleted-slide references); **0** §-leak / LO-code / FACT-CHECK / VERIFY-DAY-OF in spoken body. Central question is **word-and-order-identical** across chapter §0.3 / deck.yaml / s04 visible / speech s04 — the *only* delta is punctuation-for-oral-delivery (parenthetical → comma-set), characterised below as **P2**, not a ЦВ-mismatch (no REVISE trigger fired). Arc / 5-return-points / failure-thread / Knight-callback-discipline / forward-pointer direction / Семинар-5 Bloom-boundary are fully consistent. No P0/P1. One P2 (ЦВ oral-punctuation variant) — optional polish, non-blocking.

## Severity counts
- **P0** (factual contradiction / missing coverage): **0**
- **P1** (significant drift / tone / missing cite): **0**
- **P2** (minor inconsistency): **1**

## Cross-artifact matrix (cornerstone: concept / number → chapter § → slide → speech → aligned?)

| Item | Chapter | Slide | Speech | Aligned? |
|---|---|---|---|---|
| **Central question** (verbatim) | §0.3 | deck.yaml `central_question` + s04 visible | s04 spoken | ✓ word/order-identical; speech差 = oral punctuation only (P2 below) |
| Cover tagline (shortened ЦВ) | §0 framing | s02 «Под какую задачу — какой тип ИИ, почему именно он, и где он ломается» | s02 spoken does NOT recite ЦВ (correct — only s04 does) | ✓ intentional cover subtitle, Phase 7-cleared |
| Единый паттерн карточки (5 шагов) | §0.4 | s04 (5 шагов teal) | s04 «пять шагов… задача / тип и почему / пример / где ломается / альтернатива и критерий» | ✓ same 5 steps; «не отраслевой стандарт» disclaimer held all 3 |
| 5 типов + CV-пласт map | §0.4 | s03/s04 | s03 «пять типов… шестым пластом CV» | ✓ same set/order/analogies |
| **4 понятия с нуля** (FP/FN+матрица, прокси-bias, distribution shift) | §0.2 (4 items, FP/FN+матрица paired) | s03 visible | s03 «Четыре понятия… ошибки 1/2 рода, матрица ошибок, прокси-предвзятость, дрейф распределения» | ✓ count «четыре» preserved; enumeration is sanctioned NL restatement (glossary L40 pairs FP/FN+матрица as one canonical) |
| **6 типов ИИ** set/order/analogies | §0.4/§6.1 | s03/s04/s29 | s03/s04/s29 | ✓ прогноз→товаровед / аномалии→облако+выброс / скоринг→инспектор / LLM→студент-справочник / recsys→продавец / CV сквозной — identical |
| **5 ЦВ-return points** | §1.5/§2.4/§3.4/§4.4/§5.5 | s09/s14/s18/s23/s28 | s09«первый»/s14«второй»/s18«третий»/s23«четвёртый»/s28«пятый, последний» | ✓ exact order/count/anchoring |
| **Failure-нить** Zillow→fraud-FP→Apple Card→Air Canada/Klarna→Wendy's | Заключение + per-§ | s09→s14→s18→s23→s28→s30 | s09→s14→s18→s23→s28→s30 | ✓ identical chain/order all 3 |
| **Knight = callback-only** | DDB1 + §1.5/§2.4/§3.5 callbacks | s09/s14/s19 callback + s30 list | s09/s14 callback + s19 criterion + s30 list | ✓ never standalone failure case in any artifact |
| Zillow $300M/кв · $500M+ · ~2000 (~25%) · −25% | §0.1/§1.5 | s01/s09 | s01 (all 4) / s09 raspackage | ✓ identical |
| distribution shift inline-define с нуля | §1.5 | s09 | s09 «модель училась на одном мире, работает в другом» | ✓ same intuition, introduced at s09 |
| асимметрия цены ошибки | §1.5 | s09 | s09 «≈0 в рекомендации vs десятки тыс.$ необратимо» | ✓ identical |
| Knight $440M / ~45 мин / 2012 | DDB1 + §1.5/§2.4 | s09/s14/s19 | s09 «четыреста сорок миллионов / сорок пять минут / 2012» | ✓ identical, callback framing |
| Opendoor — same type, survived | §1.5 / DDB1 | s09 | s09 «Opendoor пережил… консервативная обвязка» | ✓ identical thesis |
| X5 >70% · +5 млрд ₽ · −2% | §1.3 | s07 | s07 (all 3, «по заявлению компании») | ✓ identical, attribution held |
| Магнит F&R после SAP/Blue Yonder | §1.3 | s07 | s07 «после ухода SAP, Blue Yonder» | ✓ identical |
| Stripe ~32% / JPMorgan −30% / **Visa ~$40 млрд FY2023 (~80 млн)** | §2.2 | s12 | s12 «тридцать два / тридцать / сорок миллиардов FY2023» | ✓ identical (Visa $40 млрд not $30, v2 fact-integrity held) |
| Банк России антифрод (по материалам, no bare number) | §2.2 | s12 | s12 «по материалам Банка России» | ✓ attribution held |
| Матрица ошибок TP/TN/FP/FN; FP=1-й род / FN=2-й род | §2.3 | s13 | s13 «ошибка первого рода / второго рода» | ✓ identical, introduced с нуля at s13 |
| accuracy лжёт (1M / 1000 фрода → 99,9%) | §2.3 | s13 | s13 «миллион / тысяча / 99,9» | ✓ identical example |
| cost-sensitive / precision↔recall различитель | §2.3 / §2.4 | s13 / s14 | s13 «стоимостно-взвешенная» / s14 «точность против полноты» | ✓ distinction preserved |
| FP $5 кофе vs $5000 лечение | §2.4 | s14 | s14 «кофе за пять / пять тысяч за медицину» | ✓ identical |
| Сбер ~100% ИИ · до 5000 параметров · +350 млрд ₽ · >80% opt-out | §3.2 | s17 | s17 (all, «по заявлениям банка», «по материалам Банка России») | ✓ identical |
| **Apple Card: NYDFS НЕ нашёл нарушения (~400k)** | §3.4 | s18 | s18 «нарушения не нашёл / ~400 000 / доказанно дискриминировала — фактологически неверно» | ✓ exact precise wording held all 3 |
| прокси-предвзятость механизм с нуля | §3.4 | s18 | s18 «убрал графу пол, но десяток коррелирующих» | ✓ same «на пальцах», introduced at s18 |
| Критерий «автоматизация без gate» (3 типа → 1 класс) | §3.5 | s19 | s19 «Zillow / антифрод / Knight → критерий-вывод» | ✓ criterion-not-failure framing held |
| Т-Банк >40% / 70% планируют — НЕ «>90%» (class-5 подмена базы) | §4.1 | s21 | s21 «>40% verified; >90% — только как обучающий пример подмены базы» | ✓ counter-example correct all 3 |
| 5 классов ошибок fact-checking | §4.2 | s22 | s22 «галлюцинация / устаревшее / прокси-bias / обман метрикой / подмена базы» | ✓ same 5 |
| grounding аналогия (студент со справочником) | §4.3 | s22 | s22 «студент на экзамене → открывает справочник» | ✓ identical analogy |
| Air Canada (callback Л3, суд 02.2024) | §4.4 | s23 | s23 «callback Лекции 3, не дубль; трибунал февраль 2024» | ✓ callback framing held |
| Klarna ~2/3 · 11→<2 мин · ~$40 млн · откат 2025 | §4.4 | s23 | s23 (all, «заявлено компанией», CEO косвенной речью) | ✓ identical, augmentation lesson |
| Двухуровневый вывод (тип необходим, не достаточен) | §4.5 | s24 | s24 pivot «не сводка, а мост» | ✓ pivot-not-recap held |
| collaborative/content-based/hybrid + слабости | §5.1/§5.2/§5.4 | s26/s27 | s26 «коллаборативная/контентная + cold-start/popularity/over-spec» / s27 hybrid | ✓ canonical terms, introduced с нуля |
| Amazon ~35% / Netflix ~75% — историческая McKinsey-оценка | §5.3 | s27 | s27 «исторически приводимая оценка ~2013, НЕ свежий заголовок» | ✓ fact-discipline held all 3 |
| Wendy's $20 млн / surge backlash 02.2024 / откат | §5.5 | s28 | s28 «двадцать миллионов / февраль 2024 / откатила формулировку» | ✓ identical |
| прокси≠цель — единый класс | §5.5, DDB5 | s28/s29 | s28 «прокси вместо цели… тот же механизм, что пузырь» | ✓ same unifying class (NL variants — see Terminology) |
| Матрица «задача × тип ИИ» + нижняя «не ИИ» строка | §6.1 | s29 (6 строк, нижняя gold) | s29 (6 rows row-for-row + нижняя «обычный код, движок правил, НЕ ИИ») | ✓ identical structure/content |
| 5 проявлений «необходим, не достаточен» | §6.2 | s30 (Zillow/Apple Card/Air Canada/Klarna/Wendy's) | s30 (same 5, same fixes) | ✓ identical |
| ФЗ-152/PII/биометрия/on-prem · KYC/liveness/JWO >1000 | §6.3 (А+Б) | s31 (2 панели) | s31 (2 блока: данные+закон / CV-пласт; «свыше тысячи ревьюеров»; Amazon оспаривал) | ✓ aggregation + two-sided framing held |
| Just Walk Out >1000 (Amazon оспаривал масштаб) | §6.3, DDB6 | s31 | s31 «Amazon оспаривал такую трактовку» | ✓ two-sidedness held |
| Чек-лист 8 пунктов + Семинар 5 (Apply, Bloom-граница) | §6.4/§6.5 | s32 | s32 «8 вопросов; лекция распознать/назвать, семинар самостоятельно верифицировать» | ✓ lecture≠seminar boundary held |
| Forward-pointer Л7 (§2.2/§4.3/§2.5, §-stripped) | §2.3/§3.4/§6.3 | s13/s18/s31 | s13«построим в Лекции 7» / s18«увидим в Лекции 7» / s31«углубим в Лекции 7» | ✓ forward direction, §-numbers stripped from speech (semantically consistent) |

## Coverage parity (3-artifact)

- **Chapter [for-slide-sNN] markers ↔ deck ↔ speech:** 33 distinct chapter markers (s01–s32 + s04a) = 33 deck slide IDs = 33 speech fragments (`## [sNN]` headers). **1:1:1.** Exactly one speech fragment per slide; no chapter LO/section without slide; no slide assertion without chapter grounding; no speech fragment introducing a claim/number absent from chapter.
- **s29 aggregation:** chapter §6.1 matrix (6 rows incl. bottom «не ИИ») → s29 6-row matrix → speech s29 walks all 6 rows row-for-row including the gold bottom «обычный код / движок правил / НЕ ИИ» row. Coverage complete.
- **s31 aggregation:** chapter §6.3 split (А данные+закон / Б CV-пласт) → s31 2-panel → speech s31 «Блок первый — данные и закон / Блок второй — компьютерное зрение» covering all sub-blocks (ФЗ-152/PII/on-prem-vs-cloud + KYC/liveness/биометрия-необратима/JWO). Aligned.
- **Interactive moments ↔ speech:** s01 open_question / s09 think_pause / s14 poll / s23 think_pause / s28 think_pause / s32 qa — each reflected in speech body as `[обращение к залу]`/`[пауза 30 сек / 20 сек]` beat with the chapter-matching wording; durations match deck (s01=30 сек, s09=30, s14=20, s23=30, s28=30). ✓
- **Pre-flight actionability:** speech pre-flight section carries all VERIFY-DAY-OF (cbr.ru / Сбер / X5) + FACT-CHECK (Stripe/JPMorgan/Visa / Т-Банк / Klarna / Amazon-Netflix / Just Walk Out) items with URLs/sources/instructions, synced to deck-part2 verify_day_of/fact_check items. Actionable, not vestigial. ✓

## Terminology drift (terminology-only sub-mode, vs locked glossary.yaml — all 3 artifacts)

**No drift on any key term.** Every observed cross-artifact form is an explicitly glossary-sanctioned canonical or alias, and the introduce-at-first-use discipline holds in all 3 artifacts:

- `distribution shift` ↔ `дрейф распределения` (glossary L23-24, both canonical) — speech introduces canonical «дрейф распределения» at s09 first, reuses consistently; chapter/s09 same. Inflections in connected prose, no competing form. ✓
- `поиск аномалий` ↔ `anomaly detection` (glossary L31-34, alias-equivalent) — speech s11 introduces both together («поиск аномалий», then «anomaly detection» context), matches chapter §2.1 / s11. ✓
- `прокси-предвзятость` (canonical) / `прокси-bias` (alias, glossary L59-62) — speech uses canonical «прокси-предвзятость» at first intro (s18, s22), `прокси-bias` only in compact callback (s18 «опасный даже без злого умысла — прокси-предвзятость», later «прокси-bias»-pattern) — exactly matches chapter usage pattern; no drift. ✓
- `прокси≠цель` (canonical, glossary L99-102, no alias) — speech body uses `прокси вместо цели` (×2, s28), `прокси≠цель` (×1, s28), `прокси не равно цель` (×1, s29). **NOT drift:** these are the same concept's natural-language restatements, character-for-character matching chapter §5.5/DDB5/§6.1 wording (chapter itself uses «прокси вместо цели» / «прокси≠цель» / «прокси не равно цель» interchangeably as NL forms of the single class label). Phase 7 baseline already adjudicated this exact pattern as non-drift; speech reproduces chapter's own register. ✓
- `false positive/false negative`, `ошибка первого/второго рода`, `матрица ошибок` (glossary L39-42 aliases) — speech s13 introduces «ложно-положительный/ошибка первого рода», «матрица ошибок» с нуля; chapter §2.3 / s13 same canonical pair. ✓
- `circuit-breaker / kill-switch / аварийный выключатель` (glossary L127-130) — speech uses «аварийный выключатель» consistently (s09/s19/s29), Russian canonical-alias; chapter uses «circuit-breaker/kill-switch (аварийный выключатель)» — speech选择 the RU alias for oral delivery, glossary-sanctioned, no drift. ✓
- `collaborative/content-based/hybrid`, `cold-start/popularity bias/over-specialization`, `filter bubble (информационный пузырь)`, `dynamic pricing (динамическое ценообразование)`, `grounding`, `KYC/liveness/hidden human cost`, `SHAP`, `iBuying`, `augmentation`, `ФЗ-152` — all consistent canonical/alias forms across chapter + slides + speech + glossary. Speech s26/s27 introduce RU canonicals («коллаборативная/контентная фильтрация», «информационный пузырь», «динамическое ценообразование») at first use, matching chapter §5.1/§5.2. ✓
- **Forbidden anglicisms** (пайплайн/фоллбэк/эдж-кейс/инсайт): **0 occurrences** in speech spoken body and in slides. (Single grep hit at speech L591 is in the non-spoken self-assessment block — exempt; «конвейер» used in literal sense at s17/s19, not as пайплайн-substitute.) ✓
- **course-scaffold term:** «единый паттерн карточки типа ИИ» presented teach-not-defend in all 3 (chapter §0.4 disclaimer, s04 disclaimer-плашка, speech s04 «не отраслевой стандарт и не термин из учебника… наш с вами рабочий конструкт»). Not in glossary as canonical — correctly so. ✓

## Orphan reference / leak detection (3-artifact)

- **Speech ↔ deck:** `slides_covered` frontmatter = all 33 (s01–s32 + s04a); 33 `## [sNN]` fragment headers exactly match deck.yaml + deck-part2.yaml IDs; **0** speech slide-tokens outside the 33-ID set; **0** references to deleted/renumbered slides (deck LOCKED=33, never reduced). No orphan refs. ✓
- **§-leak / code-leak in spoken body** (`## [s01` … `## [Резерв`): `[FACT-CHECK]`=0, `[VFY]`=0, `[VERIFY-DAY-OF]`=0, LO-codes=0, `§\d.\d`=0, `→sNN`=0. All verify/fact-check cues isolated to non-spoken pre-flight section. ✓
- **Cross-slide / chapter-§ refs in speech spoken text:** 0 (`§X.X` and `→sNN` both = 0 in spoken body; chapter §-anchors correctly translated to plain «в Лекции 7» / «раздел про фрод» NL forms). ✓

## Central question / arc / failure-thread / forward-pointer (3-artifact)

- **Central question:** `«Финансы и ритейл — отрасли максимального внедрения ИИ. Под какую задачу — какой тип ИИ, почему именно он [(а не LLM везде) | , а не LLM везде,] и где этот тип ломается?»` — **identical lexemes and word order** across chapter §0.3, deck.yaml `central_question`, s04 visible, speech s04. The sole difference: chapter/deck/s04 use the **parenthetical** `(а не LLM везде)`; speech s04 uses the **comma-set** `, а не LLM везде,`. Same words, same order, same meaning — punctuation adapted for oral reading. This is **not** a ЦВ-mismatch (no REVISE trigger) — it is a P2 oral-delivery normalization (D1 below). s02 cover correctly does NOT recite the full ЦВ in either slide or speech (s02 uses the intentional shortened tagline on the slide only; Phase 7-cleared). ✓ (with P2)
- **5 ЦВ-return points:** chapter (§1.5/§2.4/§3.4/§4.4/§5.5) → s09/s14/s18/s23/s28 → speech «возвращается первый/второй/третий/четвёртый/пятый, последний раз». Speech drops chapter's «ребром» qualifier («возвращается ребром первый раз» → «возвращается первый раз») — sanctioned conversational compression, exact order/count/anchoring preserved. ✓
- **6 типов ИИ:** same set / order / analogies in chapter §0.4/§6.1, s03/s04/s29, speech s03/s04/s29 (товаровед / облако+выброс / инспектор-расчёт / студент-справочник / продавец / CV сквозной). ✓
- **Failure-нить:** identical chain Zillow→fraud-FP→Apple Card→Air Canada+Klarna→Wendy's in chapter Заключение and across s09→s14→s18→s23→s28→s30 and speech same. Knight = callback-only (s09/s14 + s19 criterion + s30 list), never standalone — exactly as chapter (DDB1 + callbacks). Just Walk Out = s31 illustration only. ✓
- **Forward-pointers Л7:** all 3 in speech body are correct forward direction («построим/увидим/углубим в Лекции 7»), §-numbers (§2.2/§4.3/§2.5) correctly stripped from speech, retained in chapter — semantically consistent (Л7 is after Л5, intro-here-deepen-in-Л7). Семинар 5 Bloom-boundary (lecture=Understand «распознать класс + назвать принцип» / Семинар 5=Apply «самостоятельно верифицировать») identical in chapter §4.2/§6.5, s22/s32, speech s22/s32. ✓

## DISCREPANCIES

### D1 — Central question: parenthetical vs comma-set (oral-delivery punctuation)
**Severity:** P2 (minor; NOT a ЦВ char-mismatch — no REVISE trigger; words and word-order are identical across all 4 loci).
**Where:** chapter §0.3 / deck.yaml `central_question` / s04 visible body all read `«…почему именно он **(а не LLM везде)**, и где этот тип ломается?»`. Speech s04 spoken reads `«…почему именно он**, а не LLM везде,** и где этот тип ломается?»`.
**Issue:** The parenthetical clause `(а не LLM везде)` in the written/displayed artifacts is rendered as a comma-delimited inline clause `, а не LLM везде,` in the spoken speech. Lexemes, sequence and semantics are byte-identical save for the bracket→comma substitution. This is a deliberate and defensible oral-reading adaptation (parentheses do not survive speech; a lecturer cannot voice a bracket), and the speech self-assessment (L573) explicitly claims char-identity, which is true at the word level. It is logged only because the consistency-checker contract requires the ЦВ to be reported as character-exact across artifacts, and this is the single character-level deviation in the entire 3-artifact set.
**Recommendation (optional polish, speech only — chapter is source of truth and correct, do NOT touch chapter/deck/s04):** either (a) leave as-is — comma-set is the linguistically correct oral form of a parenthetical and changes nothing semantically; or (b) if strict char-parity is desired for the on-screen-vs-spoken match, the lecturer simply pauses at the commas (already implied by `[понизить голос, читать медленно]`). No artifact change required to ship. Non-blocking — APPROVE-WITH-POLISH stands with or without this.

## Coverage gaps
None. Every chapter LO, section, in-bucket failure block, deep-dive-derived criterion, number, attribution and date has a corresponding slide and a corresponding speech fragment; no slide or speech fragment introduces a claim/number/date absent from chapter; no speech fragment overclaims beyond chapter (e.g. Apple Card stays «NYDFS не нашёл нарушения», Klarna stays augmentation-lesson not «ИИ заменяет», >90% used only as base-substitution counter-example, Visa $40 млрд not $30, Amazon/Netflix as historical McKinsey estimate, Just Walk Out two-sided). strict-in failure/judgment content is carried into speech distributed across all sections (s09 · s13/s14 · s16/s18/s19 · s22/s23/s24 · s28 · s29/s30/s31 — not single-cluster), consistent with chapter's distributed design — methodology-critic owns the % verdict; cross-artifact distribution is consistent here.

## Топ-фиксов (per artifact)
- **Chapter:** none (source of truth, internally consistent, no own P0/P1; Phase 7 confirmed; Phase 10 re-verified against speech — no contradiction surfaced).
- **Slides:** none new at Phase 10 (the Phase 7 optional P2 on s13 «1-го/2-го» vs «первого/второго рода» intra-slide alias mix is a slides-only cosmetic carry-over, still optional, not re-raised as a cross-artifact issue — speech consistently uses «первого/второго рода», so no 3-artifact drift).
- **Speech:** (optional P2 only) D1 — ЦВ oral-punctuation variant; leave as-is or rely on lecturer pause. No structural change.

## Note for orchestrator
Phase 10 3-artifact alignment is exceptionally tight and regression-clean vs the Phase 7 chapter↔slides APPROVE-CLEAN baseline: numbers (Visa $40 млрд, Knight $440M/45min, Klarna $40 млн, Сбер 350 млрд/5000, Wendy's $20M, Just Walk Out >1000, Zillow $300M-q/$500M+/~2000/−25%), attributions/dates, fact-discipline caveats (РПД «>90%» strictly counter-example-only in all 3; Amazon/Netflix historical estimate; Apple Card «не нашёл нарушения»; Just Walk Out two-sided), terminology (glossary lock respected, 0 forbidden anglicisms in spoken body, introduce-at-first-use held in all 3), central question (word/order-identical), 5 return points, failure-thread, Knight-callback discipline, forward-pointer direction and Семинар-5 Bloom-boundary all carry into speech without drift. The single P2 (D1) is an oral-delivery punctuation normalization, not a ЦВ mismatch — no REVISE trigger fired. No PROPOSED GLOSSARY UPDATE needed; glossary canonical forms are well-chosen and consistently honored across all 3 artifacts. Verdict **APPROVE-WITH-POLISH** — speech may proceed to Phase 11/GATE C; D1 is optional cosmetic, not a gate blocker.
