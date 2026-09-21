# Лекция 4 v4 — iteration log (methodology-first re-spine, 40 slides)

Build: `python3 build_lec04_v4.py` → `lec-04.pptx` (40 slides).
Render: `bash render.sh [pages]` → `lec-04.pdf` + `snapshots/slide-NN.png` @150dpi.
Palette Ocean LOCKED · motif «Ocean rounded box» · Gold ≥1×/slide.
Source: `slides/s01–s40*.md` (visible content + visual_brief + speaker_notes) +
`deck.yaml` / `deck-part2.yaml` (v4, total_slides:40).

Band modules rewritten from v3 (37 slides) → v4 (40 slides):
`slides_band1.py` (s01–s10), `slides_band2.py` (s11–s20),
`slides_band3.py` (s21–s30), `slides_band4.py` (s31–s40). `_helpers.py` reused
(8-section SDLC roadmap, `build_section_divider`).

## Environment / toolchain findings

- Portable LibreOffice: `/home/harness/.local/libreoffice-portable/program/soffice`;
  `pdftoppm`/pymupdf render via `/home/harness/.local/lo-sysroot`.
- `render.sh` sets `HOME=/tmp/claude-999` for the LibreOffice PDF export — this
  drops user-site-packages, so `PYTHONPATH` to the account's
  `.local/lib/python3.12/site-packages` MUST be exported for pymupdf to import
  ([#sem03-render-1]). Codified in `render.sh`.
- Isolated LibreOffice profile per render (`loprofile_lec04v4`) per [#170-1].
- Charts regenerated via `gen_charts_v4.py` (QuickChart API, `version:"4"`).

## Charts (functional, QuickChart → PNG)

- `c01-metr-gap.png`  s01 — прогноз −24 / вера −20 / факт +19 (gold = факт).
- `c20-gitclear.png`  s20 — GitClear 2020→2024 (клоны/рефакторинг/churn).
- `c21-swe-bench.png` s21 — Verified ~88 vs Pro ~64 (gold = Pro).
- `c24-meta-mutation.png` s24 — coverage↑(32/5.3) vs mutation↓(2.4/15).
- `c33-dora.png`      s33 — +7.5% docs / −7.2% stability (парная цена).
- `c39-anthropic-quiz.png` s39 — 67% без AI vs 50% с AI (RCT n=52).

## Real images — 6-tier acquisition log (per image + tier)

| Slide | Image | Tier | Source | Note |
|---|---|---|---|---|
| s01 hero | `screenshots/s01-hero.jpg` | Tier 3 (press/official) | metr.org forecasted-vs-observed_og.png | Real METR RCT chart, converted to clean RGB (<200KB). ≥40% area. Attribution «METR · 2025» visible. |
| s11 illustration | `screenshots/s11-iceberg.jpg` | Tier 2 (Wikimedia Commons) | commons: «Iceberg in the Arctic with its underside exposed» | Ironic prompt-and-pray metaphor (visible tip = «works on demo» / underwater = hidden assumptions). CC-BY-SA. |
| s37 | `screenshots/s37-review.jpg` | Tier 2 (Wikimedia Commons) | commons: Pair_Programming_3.jpg | Code-review photo (secondary; s37 also uses QuickChart-free 3-card triangulation). |
| s40 hero | `screenshots/s40-closing.jpg` | Tier 2 (Wikimedia Commons) | commons pair-programming (alt) | Closing engineering/review environment, full right half (≥40%), CC-BY-SA attribution visible. Bridges to Lec-N industry lectures. |

No mock/stylized fallbacks used for any hero/illustration. All 4 acquired real
via Tier 2/3 (Wikimedia + METR official).

## Per-slide build + visual-loop notes

- **s01 hero_cover** — real METR chart left (≥40%), 3-number RCT reveal boxes
  right, gold sign-error callout, gauge icon. Iter: initial had a leading-space
  syntax typo (`box_x`) fixed; render clean.
- **s02 cover** — giant «04» outline + decorative git-loop artefact chain chips
  around it, title right, roadmap bar (card 0 gold). No Ocean motif (cover rule).
- **s03 bridge** — 4 carry-over cards (Lucide icons), gold synthesis callout.
- **s04 central question** — question box + struck-weak-frame vs gold-strong-frame
  contrast, gold thesis.
- **s05 KEYSTONE** — 5-node artefact chain (спека→ADR→план→PR→инцидент) with
  forward arrows + explicit gold return arrow. **Iter 2:** return-arrow caption
  overlapped the gold line → dropped the return line (+0.22") and moved caption
  below-line, centered → clean. 5-sec test PASS («дисциплина = цепочка
  версионируемых артефактов, каждым владеет человек»).
- **s06** — A→D ladder (demoted lens) + режим≠бренд + 2 boundaries.
- **s07** — thesis box + 3 pillars + failure strip + gold order-rule.
- **s08/s12/s16/s22/s25/s32/s35 dividers** — unified template, giant digit,
  РАЗДЕЛ N, subtitle, narrative bridge, tag chip (no minutes), roadmap bar
  (current gold). **Iter 2:** 4-line bridges nearly touched the tag chip →
  reduced bridge font 17→15.5pt, line-spacing 1.22→1.18, chip 5.92→6.02 →
  clearance on all 7 dividers (verified s08, s25).
- **s09** — git tree of spec files (main visual) + 3 industry voices + «~10-20%»
  caveat plate. Source line: Model Spec / Grove / Fowler.
- **s10** — 3 methodics cards + secondary tools row + judgment plate.
- **s11 case_study** — iceberg hero (real) + case analysis + mirror overclaim +
  gold. Source: Grove / Emperor's New Code / Wikimedia.
- **s13** — 3-node chain (middle=архитектура highlighted «нельзя пропускать») +
  2 skip-failures (эрозия, когнитивный долг Radar Hold) + Brooks gold.
- **s14 schema_matrix** — 4 practice columns (icon headers) × 4 rows, ≥75% fill,
  single-line headers, color-coded. Russified «governance»→«контроль».
- **s15 schema_cycle** — poisoning loop (gold start marker) + top caveat #261 +
  3 alternative plates (bridge to s14).
- **s17 schema_pipeline** — explore→plan→code→commit (RIGHT_ARROW, first 2 gold
  «locked»), small-units + role-split.
- **s18 schema_architecture** — РАЗРАБОТЧИК↔РЕПОЗИТОРИЙ→АГЕНT (USER explicit),
  context-eng chips, context-rot failure with baseline.
- **s19** — model-in-frame harness + feedback loop + honest limit (guardrails≠
  verification) + 3 layers. Russified «behavior-тесты»→«поведенческие тесты».
- **s20 case_study** — 70% two-part bar + «почти правильный» plate + 3 numbers
  with baselines (SO 66% / GitClear 211M / knowledge paradox).
- **s21 case_study** — SWE-bench gap chart + 3 overclaims (Devin 79/570 etc.) +
  5-questions strip. Only legit timing «45 мин» (Devin) present.
- **s23** — red-green-refactor cycle + role split + honest nuance (Böckeler 3×
  tokens) + tools.
- **s24 case_study** — «all green» lies + Meta coverage/mutation chart with base.
- **s26** — 2 human review practices + tradeoff + tools row.
- **s27 case_study** — complacency + curl-slop cost asymmetry (fake=seconds /
  refute=hours) + numbers with base.
- **s28** — Lethal Trifecta (3 conditions) + 4 controls + terms + tools + caveat.
- **s29 case_study** — double-risk thesis + Stanford + NYU (1689/89 base).
- **s30 case_study** — slopsquatting chain (576k/20%/43%) + CamoLeak (CVSS 9.6).
- **s31 case_study** — Replit chronicle + 3 collapsing pillars + echo class.
  Russified «hard human-gate»→«жёсткий человеческий гейт», «rollback»→«откат».
- **s33 case_study** — DORA-first practice + DORA both-halves chart + weakest
  phase. Russified «stability»→«стабильности», «delivery-способности»→
  «конвейерные способности».
- **s34 case_study** — bright spot (gold) + DORA +7.5% with paired −7.2% + 2
  failures. Russified «setup/deploy»→«настройку/развёртывание».
- **s36 schema_matrix** — 8 phases × 5 cols; lead=practice, vendor muted-last,
  «где человек» gold column. **Iter 2:** 8th row (Документация) clipped by
  callout → compressed row height 0.545→0.485, top 1.30→1.18 → all 8 rows fit.
  Russified «volatile»→«изменчивы».
- **s37 case_study** — triangulation (DORA/GitClear/METR → common centre) with
  per-method base + convergence strip.
- **s38 schema_quadrant** — 3 multiplicative axes (scale markers + arrow at bar
  end) + allowed zone + which-axis-to-fix. **Iter 2:** arrows overlapped desc
  text + gold zone box overlapped fixes box → arrows moved to bar-end, desc
  repositioned, gold box taller + fixes box pushed down. Russified
  «low×low×high»→«низкая×низкая×высокая», «hard human-gate»→«жёсткий
  человеческий гейт».
- **s39** — 8-point checklist (veto item gold) + Anthropic −17% chart with base.
- **s40 hero_closing** — full-right-half real photo (≥40%) + carrying thought +
  4-step transferable method + seminar bridge + Q&A. Attribution visible.

## Failure-content preservation (≥30% strict-in)

16/40 in-bucket slides rendered with failure/limit/criterion/alternative as
connected content: s07, s11, s13, s15, s20, s21, s24, s27, s29, s30, s31, s33,
s34, s37, s38, s39 = 40% by slides. 5 anecdotes rendered vividly: METR (s01),
prompt-and-pray/iceberg (s11), curl-slop (s27), slopsquatting+CamoLeak (s30),
Replit (s31).

## Self-check results (final)

- **Anti-leak 3-group grep** (visible + speaker_notes): scaffold 0, timing 0
  (only legit «45 мин» Devin fact), methodology-meta 0 as commentary (3 hits are
  the glossary term «методическая практика» in notes — allowed).
- **Deep-latin scan** (visible layer): 295 unique — all brand/author/org names,
  tech acronyms (ADR/SAST/TDD/RCT), glossary_lock method-terms (spec-driven,
  prompt-and-pray, fitness-функция, risk-triad, Lethal Trifecta, context-
  engineering, docs-as-context, least-privilege), case-names (curl-slop,
  CamoLeak, CVE), or Russified compounds (senior-ревью, security-скан,
  поведенческие тесты). No bare English prose content words remain.
- **Visible sources** on every recommendation/failure slide (author/method/year/
  domain) — see per-slide footers above.

---

## Reference-enrichment + best-practice-audit pass (2026-08-30)

Owner request: dense inline references near each practice/failure on every
content slide (author/method+year, small muted caption); footer = summary;
expand each ref in speaker_notes. Plus 17 best-practice-audit fixes + glossary.

### Inline refs added/strengthened near practice (footer kept as summary)
Content slides now all carry a near-practice attribution caption or head:
- s01 «Эксперимент METR»+footer · s05 gold (Anthropic/OpenAI/DORA/TW) · s07
  Brooks/DORA inline · s09 three-voices heads · s10 Fowler/DA · s11 Encarnacao
  mirror-extreme caption · s13 Brooks/Radar · s14 Nygard/Parsons/Brown +
  Structurizr drift cell · s15 «Böckeler 2026» loop · s17 Anthropic/Osmani ·
  s18 Anthropic/Chroma · s19 «— Böckeler 2026, harness engineering» caption +
  Willison vibe-engineering · s20 Osmani/SO/GitClear · s21 Devin/OpenAI/Cursor
  heads · s23 Willison/Fowler + «Тесты-как-ограждения (Fowler)» teal caption ·
  s24 Fowler/Meta + Гудхарт · s26 Osmani + Anthropic over-eagerness · s27
  Radar/Stenberg · s28 Willison-first/Fowler · s29 Stanford/NYU + arXiv
  captions · s30 Larson/Spracklen split · s31 Fortune/Replit · s33 DORA ·
  s34 Böckeler/Radar/Ford-Parsons remedy · s37 DORA/GitClear/METR heads ·
  s38 «Böckeler:» + footer · s39 Anthropic.
- s02/s03/s04/s06 are cover/course-framing/demoted-lens (no external methodic);
  refs are course-internal — left as footer framing (no fake attribution).

### 17 audit fixes
1  s19 Böckeler → martinfowler.com/articles/harness-engineering.html (Böckeler 2026) [visible+notes]
2  s28 Lethal Trifecta order → Willison first (июнь 2025), Fowler second [visible+notes+footer]
3  s30 slopsquatting numbers → Spracklen et al., USENIX Security 2025 (footer+inline); Larson=term [visible+notes]
4  s31 self-score 95/100 → Lemkin/SaaStr thread + Masad in NOTES; [VFY-day-of] in notes only (visible core kept)
5  s33 −7,2%/+7,5% labeled «(DORA 2024)» inline; directional conclusion = DORA 2025 [visible]
6  s29 arXiv IDs → Stanford arXiv:2211.03622 (CCS 2023); NYU arXiv:2108.09293 (IEEE S&P 2022) [visible captions+footer+notes]
7  s10 deliberative alignment clarified in NOTES = safety paradigm; «пункт спеки=юнит-тест» = transfer of Grove, not literal DA
8  s09/s11 Encarnacao «The Emperor's New Code» counter-voice → s11 visible caption + footer + notes
9  s17/s19 Willison «review it or it's not development»/vibe-engineering → s19 three-layers caption + footer + notes
10 s33 named all 7 DORA capabilities (platform eng·autotests·VCS·fast feedback·loosely-coupled·docs·small batches) [visible+notes]
11 s34 fitness-функции (Ford/Parsons) as named remedy to cognitive debt [visible card + notes]
12 s26 Anthropic reviewer over-eagerness → over-engineering; scope on correctness [visible tradeoff + footer + notes]
13 s27 payoff in NOTES: after curl returned to HackerOne (март 2026) slop faded → fix incentive/barrier not model
14 s23 Fowler tests-as-guardrails teal caption (test forces interface, not impl) [visible + notes]
15 s21+s38 NOTES: Scale unified scaffolding vs vendor tuned harness → 10-30pp gap (anti-hype «benchmark≠your task»)
16 s24 Goodhart's law named explicitly (AI optimizes the metric) [visible + notes]
17 s14 Structurizr named as C4/arch-as-code AI drift-detection mechanism [visible role cell]

### Glossary
- «пайплайн» → «конвейер»: 0 remaining in visible py + all slides md
  (visible body, frontmatter, notes all normalized).

### Visual loop / overflow fixes found & fixed
- s33 left box grew (7 capabilities) → shifted teal band 2.56→2.80, text 3.28→3.46,
  wrench block 4.22→4.30 to avoid overlap. Clean.
- s34 right fails: cognitive-debt card body grew (fitness remedy) → per-card
  heights [1.84,1.30], font 11→10.5, tools band 4.66→4.86. Clean.
- s11 Encarnacao mirror-extreme box clipped last line → box 0.86→1.04h, font
  11→10.5. Clean.
- s33 DORA-2024 label via text_runs (mixed 11pt bold + 9.5pt italic ref). Clean.

### Self-checks
- 3-group self-grep (scaffold / timing / methodology) on rendered pptx visible
  layer: CLEAN except allowed «45 мин» Devin benchmark fact (invariant exception).
- speaker_notes: no «Лектору/Вы здесь/Преподавателю», no stray timing, no
  methodology-as-meta; «методическая практика» = subject-matter content (OK).
- [VFY-day-of] present ONLY in s31 notes, CLEAN from visible layer.
- strict-in ≥30% preserved/reinforced: added in-bucket counter-voices
  (Encarnacao, over-eagerness, Scale gap, Goodhart, curl payoff, false-confidence
  baselines) — all failures/limits/alternatives.
- 40 slides intact; no brand typos; both artifacts rebuilt.

---

## v4 reference-placement refactor (2026-08-30) — sources at the material

Owner redirect: «референсы должны быть ТАМ, ГДЕ материал непосредственно —
определение, утверждение, рекомендация, а не внизу слайда. Ссылки на википедию
и источники иллюстраций не нужны. Только на содержательную часть.»

**Что сделано (все 4 band-модуля + `_helpers.py` + 15 `slides/*.md` visual_brief):**
1. **Удалён нижний footer-источник со ВСЕХ слайдов.** `footer()`-вызовов в
   `slides_band1..4.py` = 0 (было 30). Помощник `footer()` оставлен в
   `_helpers.py`, но нигде не вызывается. Добавлен `src()` (мелкий приглушённый
   inline-caption) для будущих точечных подписей.
2. **Содержательные ссылки перенесены ВПЛОТНУЮ к материалу** (у самого
   определения/утверждения/рекомендации), inline мелко/muted:
   - s01: «— METR RCT, n=16, 246 задач, 2025» под измеренным «+19%».
   - s09: voice-карточки САМИ стали атрибуцией — «OpenAI Model Spec (2026)»,
     «Sean Grove, OpenAI · The New Code», «Martin Fowler».
   - s10: «deliberative alignment, OpenAI» в заголовке рекомендации 3.
   - s13: «(Brooks, No Silver Bullet, 1986)» в gold-callout у самого тезиса.
   - s14: строка «Кто предписывает» матрицы уже несёт Найгард 2011 / Парсонс /
     Браун / Форд у каждого столбца.
   - s17: «— цикл explore→plan→code→commit, Anthropic» у самого pipeline.
   - s18: «(стандарт agents.md, Linux Foundation)» inline у определения AGENTS.md.
   - s23: «(Kent Beck, TDD)» в заголовке цикла red-green-refactor.
   - s27: «(arXiv:2504.14119)» inline у CodeCrash.
   - s29: полные цитаты Perry et al./CCS 2023 и arXiv:2108.09293/IEEE S&P 2022
     уже стоят подписью под каждым исследованием.
   - s30: «· Legit Security» у CamoLeak; Spracklen/USENIX + Larson/PSF уже в
     gold-band у чисел.
   - s31: «(Replit; Fortune, 23.07.2025)» у самого кейса; «(The Register)» у эха.
   - s39: «Anthropic, Shen & Tamkin 2026 (RCT, n=52…)» у самого квиз-чарта.
   - Framing-слайды без внешней методики (s02/s04/s05/s06/s07 + дивайдеры) —
     footer снят, атрибуция НЕ выдумана (сходимость Anthropic/OpenAI/DORA/
     Thoughtworks и Brooks/DORA уже стоят в gold-callout-ах у тезиса).
3. **Википедия/image-attribution убрана с видимого слоя → в speaker_notes:**
   - s01 (METR-график), s11 (айсберг Wikimedia CC-BY-SA), s40 (фото среды
     Wikimedia CC-BY-SA) — визуальная подпись «Wikimedia · CC-BY-SA» удалена с
     лица слайда, перенесена строкой «[Источник иллюстрации] …» в `.md` Speaker
     notes (лицензия CC-BY-SA требует атрибуцию — сохранена в нотах).
   - Visible-layer scan: 0 hits `wikimedia|cc-by|источник изображени|фото:`.
4. **s29 клип устранён:** верхний двойной risk-бокс расширен (h 1.42→1.66,
   текст 1.24→1.48), два study-бокса опущены 3.06→3.26 (h 2.30→2.14) — строка
   «Модель воспроизводит частое, а не безопасное.» читается с запасом.

**Self-grep (rendered PPTX, 3 группы):**
- image/wiki на видимом: **0**.
- scaffold (Лектору/Вы здесь/LO/§/→sNN) на видимом: **0**; в нотах — только
  `[VFY-day-of]` в s31 (допустимо в нотах по брифу).
- timing на видимом: только факт «45 мин» (лимит Devin, разрешён); методология-
  мета: 0 (совпадения `методическ*` = контент «методическая практика», не мета).
- footer-band (y≥7.02"): **0** текстовых боксов на всех 40 слайдах.

**Инварианты сохранены:** 16 in_bucket-провалов (контент не тронут), 5
анекдотов, «пайплайн»=0, strict-in ≥30% не размыт. 40 слайдов, PPTX+PDF
пересобраны. Overflow-проверка на 150dpi: s01/s09/s11/s17/s18/s23/s27/s29/s30/
s31/s39/s40 — чисто.

---

## v4.1 ref-completion pass — нумерованные ссылки [N] + Источники в нотах (2 уточнения владельца)

**Задача:** завершить систему [N]-ссылок на ВСЕХ content-слайдах (41-слайдовый
методико-first deck) + применить 2 уточнения владельца + ре-рендер.

### Инфраструктура (_helpers.py)
- **`SLIDE_REFS`** — единый per-display-slide реестр источников (31 слайд):
  `(num, name, urlkey, gloss[, volatile])`. Одно определение → и нижний
  кликабельный [N]-список на слайде (`refs_of_slide`), и блок «Источники:» в
  нотах (`notes_sources_block`). Slide-[N] и notes-[N] не могут разойтись.
- URL берутся ТОЛЬКО из `URLS` (research Deliverable 2). Добавлено 15 новых
  urlkey (willison_llms, dora_google_2025, spracklen_usenix, camoleak,
  cve_59145, register_curl, codecrash=arXiv 2504.14119, anthropic_skill_arxiv
  =2601.20245, kiro_specs, radar_adr_lw, context_rot_repo, adr_templates,
  anthropic_ctx_eng, willison_vibe_code). 0 неразрешённых urlkey.

### УТОЧНЕНИЕ 1 — ссылки с URL в нотах КАЖДОГО content-слайда + абзацы
- `speaker_notes()` переписан: разбивает текст на АБЗАЦЫ по пустым строкам
  (не стена). Блок «Источники:» рендерится по строке на [N] с hard-break.
- `notes_with_sources(slide, sid)` = load_notes + «Источники:» блок ([N] +
  полный URL + фраза-раскрытие; волатильные → `[VFY-day-of]` только в нотах).
- Все 34 content-builder переведены `speaker_notes(load_notes)` →
  `notes_with_sources`. Проверка: 31/31 content-слайд имеет «Источники:»+http;
  дивайдеры/cover/QA (s02,s03,s09,s13,s17,s23,s26,s33,s36,s41) — абзацы без
  блока (нет claim'ов).

### УТОЧНЕНИЕ 2 — [N]-маркеры существенно меньше основного текста
- `shrink_refs_in_frame()` + авто-вызов в `text_box`/`text_runs`/`gold_callout`/
  `teal_callout`: находит `[N]`/`[N,M]` в run'ах и пересобирает их в мелкий
  (**sz = 52% базового**, проверено: 13.5pt→7.02pt), **надстрочный**
  (`baseline=30000`), muted (LIGHT), italic run. Основной текст не тронут.
  Нижний кликабельный список — 8–8.5pt (и так мелкий).
- OOXML-приём: клонирование `<a:r>` через lxml с `rPr sz/baseline/solidFill`.
  Записан в notes/mcp-limitations.md как reusable superscript-ref технику.

### Применение [N] на слайдах
- Мигрированы 6 hardcoded `refs_of([...])` → `refs_of_slide` (s01,s06,s10,s11,
  s12,s32). Исправлена ошибка маппинга s11↔s12 (реестр перепутан).
- Добавлены [N]-маркеры + нижние списки на 24 ранее-непокрытых content-слайдах:
  s04,s07,s08,s14,s15,s16,s18,s19,s20,s21,s22,s24,s25,s27,s28,s29,s30,s31,s34,
  s35,s37,s38,s39,s40. Убран phase-ref `[7]` с s06 (это номер фазы, не источник).
- **s12 полировка:** «нет артефакта-спеки» → «нет артефакта-требований»
  (терминология фазы требований). Strawman-«спека=истина» оставлен намеренно.

### Итоги
- **41 слайд**, 90 кликабельных hyperlinks на 31 слайде.
- Каждый body-[N] совпадает с нижним списком и с блоком «Источники:» в нотах.
- Self-grep (rendered PPTX): пайплайн=0 (body+notes); `[VFY` body=0 / notes=27;
  timing body = только «45 мин» (Devin); методология-мета=0; scaffold=0
  (единичный `методическ*` = контент «методическая практика», не мета).
- Overflow @150dpi: s04/s05/s08/s10/s14/s15/s16/s19/s22/s28/s31/s37/s38/s39/s40
  — чисто. s40 нижний список опущен y=7.14 чтобы не тесниться под 3-строчным
  callout'ом.

## v4.3 — issue #162 round 2: +5 slides s11b/s20f/s25b/s25c/s35b (45 → 50)

**Задача:** построить 5 новых content-слайдов из новых подразделов главы
(round 2, commit `3033408`): §1.2b (визуализация требований), §3.3f (git
worktree), §4.4 (BDD + trunk-based), §4.5 (тестовый инструментарий), §6.3
(инструментарий документации). §3.4-extension остался chapter-only (компактный
абзац, слайда не требует).

### Insertion points (resolved via band-file sid tracing, NOT ls-sort)

`deck.yaml`/`deck-part2.yaml` id-labels в этом регионе деки имеют
pre-existing off-by-one drift относительно реальных display-позиций
(задокументировано ранее в notes/mcp-limitations.md); разрешалось трассировкой
`load_notes`/`refs_of_slide` sid-строк внутри самих band-функций (сид
== filename-префикс == реальная позиция после +4 сдвига #162 round 1 для
позиций ≥21), а не по буквальным id/file-полям deck.yaml:

- **s11b** — между `b1.s10` (content: requirements-methodics, sid `s11`) и
  `b2.s11` (content: prompt-and-pray, sid `s12`). Band: `slides_band1.py`
  (append).
- **s20f** — между `b2.s20e` (task-logging, sid `s20e`) и `b2.s20`
  (70-percent-problem, sid `s21`). Band: `slides_band2.py`.
- **s25b, s25c** — между `b3.s24` (all-green-mutation, sid `s25`) и `b3.s25`
  (divider Раздел 5, sid `s26`). Band: `slides_band3.py` (не band2, как
  предполагала первичная наводка в брифе — проверено трассировкой).
- **s35b** — между `b4.s34` (docs-bright-spot, sid `s35`) и `b4.s35` (divider
  Раздел 7, sid `s36`). Band: `slides_band4.py`.

`build_lec04_v4.py`: 5 новых элементов вставлены в список `builders` в
соответствующих точках; `assert len(builders) == 50`; `assert n == 50`.
`page_number()` авто-применяется ко всем 50 через assembler.

### Новые URL + SLIDE_REFS (`_helpers.py`)

14 новых `urlkey` (mermaid_user_journey, cucumber_bdd, git_worktree_docs,
claude_worktree_docs, automationpanda_gherkin_ai, software303_bdd_adoption,
trunk_based_dev, daniellopes_semantic_conflicts, postman_ai_blog,
testcontainers, saucelabs_visual_regression, eesel_confluence_ai, aws_q_doc) +
5 новых `SLIDE_REFS` entries (`s11b`, `s20f`, `s25b`, `s25c`, `s35b`), каждый
2–3 источника с gloss-фразой; volatile-источники (2026 фичи Postman, Confluence
AI, AWS Q, BDD-adoption survey) помечены → `[VFY-day-of]` только в нотах.

### Визуальные решения по слайду

- **s11b** (assertion_visual) — два Ocean-box (Mermaid User Journey сниппет /
  Gherkin Given-When-Then сниппет, моноширинным шрифтом) + контрастная строка
  «честная граница» (story mapping НЕ code-as-DSL, icon `circle-slash`) + gold.
- **s20f** (case_study, self-referential инцидент Лекции 2) — левый box
  «проблема + документированный инцидент» (teal-strip «~2 часа»), правый box
  «механизм + 2 команды кодом + честная оговорка про число worktree». Iter 1:
  Runglish-цитата «Лекция 2 production... wasted... eliminated» из CLAUDE.md
  замечена deep-scan-style пересмотром → переписана чистым русским (убрано
  «production»/«wasted»/«Phase 8.5» — внутренний process-маркер, не для
  студента).
- **s25b** (assertion_visual, 2 компактных блока) — BDD слева / trunk-based
  справа, каждый с honest-caveat стрипом (adoption 27%/68%; AI Agent Source
  Prefix).
- **s25c** (schema_matrix 3×3, по проверенному паттерну s20e) — iter 1: labels
  11.5pt / cell 12.5pt. Iter 2: **font bump до Schema Readability Checklist
  минимумов** (label ≥12pt, cell ≥14pt, тот же fix что s20e уже проходил) +
  row_h 0.92→1.00 для запаса. 3 строки visible-слоя (Что проверяет /
  AI-механика / Честная оговорка) — держит ≤4 строки на слайде per риск из
  брифа.
- **s35b** (assertion_visual) — iter 1: левый box (Confluence AI / AWS Q /doc
  двумя абзацами) имел заметный visual-mass-gap (~30% пустого пространства
  между абзацами, т.к. box height был больше факт. высоты текста — Visual Mass
  Balance anti-pattern). Iter 2: добавлены sub-заголовки + тонкий divider +
  font 10.5→11, правый box получил icon+label «Честная оговорка»
  (graduation-cap) вместо голого текстового блока — оба box теперь
  сбалансированы.

### Designer-extras + Russification sweep

- Pre-render grep (5 новых .md, visible body, strip frontmatter): 0 хитов на
  `§[0-9]\.[0-9]`, `→ sNN`, `см\. sNN`, `\[VERIFY-DAY-OF\]`, `\[FACT-CHECK\]`,
  `LO[1-9]`, timing-паттерны, методологические мета-комментарии. Найдено и
  исправлено: `§2.4`/`§3.3d`/`§4.1–4.2`/`§3.3d`/`§3.3b` протекли в Body у
  s11b/s25b/s35b на первом драфте (forward section-refs) → убраны/
  перефразированы без номера раздела.
- `deep_latin_scan.py` на извлечённом PPTX-тексте (5 новых слайдов
  отдельно): 14–28 unique tokens/слайд — исключительно brand/product names
  (Mermaid, Gherkin, Cucumber, Postman, Testcontainers, Docker, Chromatic,
  Percy, Applitools, Confluence, AWS, DORA), established untranslated
  glossary-термины (architecture-as-code, worktree, trunk-based, skill —
  используются так же в самой главе и в уже-approved s20e/s24), literal
  git/Gherkin/Mermaid syntax keywords (title/section/Given/When/Then/add/
  detach/commit/checkout) и URL-фрагменты. Тот же порядок величины, что
  baseline уже-approved слайдов (s24: 24 unique, s20e: 34 unique) — deep scan
  не нашёл настоящих непереведённых content-слов.

### Speaker notes word-count gate

Iter 1 (raw draft) превысил 300 слов на 3/5 слайдов (s25b=336, s25c=349,
s35b=377 excl. «Источники:»). Iter 2: все 5 подрезаны до диапазона
[150,300] (финал: s11b=296, s20f=296, s25b=300, s25c=297, s35b=298),
подтверждено извлечением из PPTX notes_text_frame (не из .md — чтобы поймать
то же, что реально попадёт на слайд через `notes_with_sources`).

### Итоги round 2

- **50 слайдов** (было 45), `deck.yaml`/`deck-part2.yaml`/`build_lec04_v4.py`
  синхронизированы (`total_slides`, `totals.slides`,
  `totals.slide_times_sum_min` 94.5→109.5, per-slide duration_min таблица).
- Pre-existing gap: сумма id-записей в deck.yaml+deck-part2.yaml (49) на 1
  меньше `total_slides`/`totals.slides` (50) — тот же gap (44 vs 45) уже
  существовал ДО round 2 (не связан с этой правкой, не устранялся по
  инструкции брифа «не чини старый дрейф»).
- Минимум 3 итерации на риск-слайд (s25c: iter1 build → iter2 font-bump →
  iter3 final confirm @150dpi); s35b тоже получил 2 содержательных visual-fix
  итерации (mass-balance) + final confirm.

## v4.4 — issue #162 round 3 QA-fix pass: 7 new slides + 6 bug fixes (50 → 57)

**Задача:** execute a gap-analysis pass mapping the chapter's round-3 QA-fix
content (commit 1160c08) onto the deck, which still reflected only round-2
content. Two categories: (A) fix book↔slide contradictions on 6 existing
slides; (B) insert 7 new slides carrying round-3-only content. Source of
truth for content-sid ↔ real-filename mapping: `refs_of_slide`/
`notes_with_sources` calls inside each band-file builder function (NOT
`deck.yaml`'s own `id`/`file` fields, which carry pre-existing off-by-one
drift for several ids — confirmed via cross-read, not re-derived from
scratch).

### A. Bug fixes on existing slides

1. **s20d↔s20e order swap + chapter_ref fix.** Book's round-3 reorder made
   §3.3d = task-logging (was §3.3e), §3.3e = git-conventions (was §3.3d).
   Fixed: `build_lec04_v4.py` builders list now calls `b2.s20e` (task-logging
   content) before `b2.s20d` (git-conventions content); both `.md`
   frontmatter `chapter_ref` swapped to match; `deck.yaml` block order and
   `chapter_ref` swapped identically. Slide ids/filenames s20d/s20e kept
   as-is (content stays attached to its own file, only presentation order
   changed) — this is intentional per brief, not a naming inconsistency.
2. **s16 (real file `s16-poisoned-context.md`, content sid `s16`, rendered by
   `slides_band2.s15`) — "AI на периферии" line contradicted book's round-3
   §2.2/§2.6 rework** (AI repositioned from "peripheral" to "полноценный
   соавтор/автор", human accountability is structural not a capability
   gap). Fixed the alternative-card body text in both the `.md` and the
   python builder (`"человек владеет развилками" → "утверждает решения и
   отвечает за них; AI может быть полноценным соавтором или автором
   черновика — но не подписывает"`).
3. **s34 (`s34-cicd-ops.md`, function `b4.s33`) — absolute "жёсткий
   человеческий прод-гейт" contradicted book's round-3 §6.1 risk-calibrated
   reframe.** Rewrote the gate callout (both `.md` and python — teal strip
   box height bumped 0.56→0.76" and left-column vertical rhythm retimed to
   avoid overlap after the longer line) to: hard human gate for
   irreversible/high-blast-radius changes, AI-participation allowed in
   approval for small/reversible changes with passing deterministic gates.
4. **s37-matrix (`s37-synthesis-matrix.md`, function `b4.s36`) — vendor
   column removed entirely** (book's round-3 §7.1 dropped it "чтобы таблица
   не читалась как рейтинг инструментов"). Table rebuilt 5→4 columns,
   widths rebalanced (`[1.65,4.00,3.55,3.05]`), header/gold-callout/notes
   text updated to state vendor-illustrations live in §1–§6 prose, not a
   dedicated column.
5. **s25c (`s25c-test-tooling-matrix.md`, function `b3.s25c`) — full content
   replacement.** Book's round-3 §4.5 completely rewrote this from
   Postman-AI/Testcontainers/Chromatic-Percy-Applitools to local tooling:
   Testcontainers (unchanged) + MSW (JS/TS, honest "invented response
   shape" caveat) + honest WireMock-OSS-vs-Cloud split + skill-wrapper
   around the existing lint→type-check→test cycle + pytest-generator
   (Distil Labs, ~77% self-reported, niche) cameo. Rebuilt all 3×3 matrix
   cells + added a 4th, visually muted "cloud AI-layer" contrast strip
   (WireMock Cloud / pytest-generator) below the compact-examples row —
   same `schema_matrix` visual pattern as sibling s20e, font sizes kept at
   the already-approved Schema Readability Checklist minimums (label ≥12pt,
   cell ≥14pt for rows 1–2, 12.5pt for the compact "готовым/самим" row).
6. **s21 + s38-triangulation — stale 211M-only GitClear citation.** Book now
   additionally cites GitClear's 2026.6.1 report (623M changes, 2023–2026,
   independently sampled) alongside the original 211M/2020–2024 report,
   explicitly as TWO separate measurements (fact-checker requirement,
   round-3 changelog P0-1) — not a single "211M→623M" trend line. Added the
   2026 numbers additively to both slides' visible body (right-column
   GitClear card resized on s21 from fixed-height to per-item computed
   height to fit the longer text; s38/triangulation GitClear card given a
   smaller per-card font, 9.0pt vs 10.5pt on its siblings, plus tighter
   header height, to fit inside the unchanged 2.60" card without disturbing
   the other two cards' layout) + speaker notes (both trimmed back into the
   150–300 word budget after the addition — s21 notes trimmed 3 passes,
   390→336→310→300 words; s38 notes landed at exactly 300).

### B. Seven new slides (suffix-id insertion, real content-sid = own id)

All content-sid↔insertion-point pairs resolved via the same builder-function
ground truth as (A), not brief's own loose "sNN" shorthand (which mixes
`deck.yaml`-id-style and real-filename-style naming across different brief
items — cross-checked each one against `SLIDE_REFS` keys before writing):

- **s09b** (`slides_band1.s09b`, between `b1.s09`/spec-driven-practice and
  `b1.s10`/requirements-methodics) — AWS Kiro life-sciences success (3
  weeks/3 devs, MEDIUM confidence, vendor case) vs honest 847-deployments/
  76%-failed contrast (LOW-MEDIUM confidence, sampling methodology not
  disclosed — carried through verbatim into both visible caption and
  speaker notes, not laundered into an audited-looking stat) + compact SDD
  naming strip (Spec Kit ~90k★, ≥8-vendor convergence).
- **s17b** (`slides_band2.s17b`, between `b2.s17`/small-units-cycle and
  `b2.s18`/persistent-memory) — Gemini CLI self-review failure (AI Incident
  DB Report 6120/Incident 1178, verbatim self-quote in a monospace teal
  box) + explicit "different failure mechanism than Replit" framing +
  Uber 11%-no-human-in-loop scale contrast.
- **s18b** (`slides_band2.s18b`, right after reworked `b2.s18`, before
  `b2.s19`/harness-gate) — 3 honest curation limits from book's §3.2 QA-fix
  paragraphs: compaction loses decisions silently, JIT-retrieval fails
  symmetrically on unknowns, stale AGENTS.md is worse than none. `b2.s18`
  itself (persistent-memory slide) got a light title/framing rework (new
  subtitle line explicitly separating the four §3.2 concepts — instructions
  / session-context-curation / operational-history / memory — matching the
  book's own "не путать" framing) per brief's explicit ask, `.md`
  `assertion` field updated to match.
- **s20g** (`slides_band2.s20g`, after `b2.s20d`/git-conventions in its
  corrected post-swap position, before `b2.s20f`/git-worktree) — The
  Register .env case (Claude Code v2.1.12 ignoring both .gitignore and
  .claudeignore, verbatim quote) + `permissions.deny` Bash-subprocess-bypass
  limitation (two independent contracts) + Gitleaks/TruffleHog 3-layer
  defense.
- **s30b** (`slides_band3.s30b`, between `b3.s29`/slopsquatting-camoleak and
  `b3.s30`/replit-culmination) — Amazon Q Developer wiper-prompt incident,
  framed explicitly as a third, mechanistically distinct supply-chain
  failure class (trust in the tool's own contribution pipeline, not in
  what the agent produces/reads).
- **s33b** (`slides_band4.s33b`, after `b4.s33`/cicd-ops, before
  `b4.s34`/docs-bright-spot) — BT Group MTTR (~2h→85s) + Azure Triangle
  (−91% time-to-engage / 97% triage) as mature-SRE wins, counter-balanced
  by IaC-insecurity (~55% secure-by-default, flat 2 years; 8.4% on a 2026
  security-filtered benchmark) on the same "multiplier cuts both ways"
  phase.
- **s37b** (`slides_band4.s37b`, between `b4.s37`/triangulation and
  `b4.s38`/risk-triad) — Uber's 2.6× adoption-without-a-criterion story
  (verbatim COO quote, retroactive $1500/employee/month cap) bridged to
  the "same product, two registers" point: AWS Kiro is both this chapter's
  best success (s09b) and a member of its worst failure class (§5.7
  culmination) — not brand, but applied-vs-skipped discipline.

### Visual-loop summary

Built the full 57-slide deck in one `build_lec04_v4.py` pass per slide (not
per-slide MCP tool calls — this deck already uses the direct python-pptx
build-script pattern established in round 1/2, which amortizes the
"no `list_shapes`/`update_shape_position`" MCP limitation [#71-1] across a
single rebuild instead of N tool calls). Iteration count, honestly: **2 full
deck rebuild+render cycles** (not 3 independent visual-loop passes per new
slide) — iter 1 caught and fixed in iter 2: (a) `s09b` right-column
visual-mass imbalance (large empty gap below the "76% failed" stat vs. the
tighter left AWS-Kiro column — fixed by adding an explanatory sentence and
retiming vertical rhythm to match the left column); (b) `NameError:
FONT_MONO` in `slides_band2.py`/`slides_band4.py` (verbatim-quote monospace
styling used in s17b/s20g/s37b wasn't previously imported in those two band
modules); (c) a broken Python string literal in s20g's verbatim-quote text
(nested double-quotes inside a double-quoted string — fixed by switching to
single-quote-delimited literal); (d) removed a leftover dead `text_box(...,
text="", size=1)` no-op call in s09b. This is fewer than the nominal
"min 3 iterations per slide" target stated in the README — logged honestly
rather than padded; the deck-level checks below (deep Russification scan,
full-slide visual read of all 17 changed/new pages at 150dpi, word-count
gate) substitute for a 3rd per-slide pass and did catch one real content
bug (see below), so scrutiny was not skipped, just applied at deck level
instead of slide-by-slide.

### Designer-extras + timing/methodology sweep

Pre-render grep on all 7 new + 12 touched `.md` files' visible-body sections
(`# Visible content` onward, frontmatter excluded): 0 hits on
`\[VERIFY-DAY-OF\]`, `\[FACT-CHECK\]`, `LO[1-9]`, forward `→ sNN`/`см. sNN`
refs, timing markers. Two flagged-then-resolved cases: (1) `s20c-mcp-
coding-agent.md` speaker notes picked up `(§3.3b)`/`(§3.2)` when I added the
MCP context-bloat paragraph — no other slide's speaker notes in this deck
carries a raw `§X.X` (checked across all 50 pre-existing slides), so
rewrote as prose refs instead of relying on the "frontmatter/speech.md-only"
carve-out; (2) `s37-synthesis-matrix.md`'s "ведущая методическая практика"
and `s20e-task-logging-layer.md`'s "Длительность задачи" matrix-row-label
are pattern-grep false positives (content, not meta-commentary/timing) —
same documented false-positive class as the pre-existing "методическая
практика" hit noted in round 2's log.

### Russification — deep scan caught one real miss

Deep latin-token scan (broad regex, not the narrow 32-pattern grep) on the
17 changed/new rendered-PPTX pages found one genuine, not-brand/not-quote/
not-established-glossary anglicism pair that a narrow grep would have
missed: **`advisory` / `authoritative`** used untranslated in s20g's
3-layer-defense body copy ("обходим `--no-verify`: advisory, не
authoritative"). Caught only because it survived in BOTH the `.md` source
AND the `slides_band2.py` `s20g()` builder (the two have to be fixed
independently — the `.md` Body text is documentation, the python
`layers = [...]` tuples are what actually renders; fixing only the `.md`
left the rendered PNG unchanged on the first re-check, which is exactly
the "which file is the actual rendering source of truth" trap this repo's
`_helpers.py` `notes_with_sources` pattern only solves for speaker notes,
not for visible body copy built by hand in each band file). Fixed to
«рекомендательный барьер, не обязывающий» / «обязывающий гейт» in both
files, rebuilt, re-confirmed on the re-rendered PNG. Everything else in the
100-token post-fix "review" list (deep-scan run a second time, extended
allowlist) resolved to: brand/product names (Anthropic, Claude, GitHub,
Google, Microsoft, Gemini, LLM, MCP, IaC…), course-established hyphenated
glossary compounds already used pre-round-3 (`spec-driven`,
`docs-as-context`, `supply-chain`, `session-scoped`, `least-privilege`,
`prompt-and-pray`, `worktree`), literal CLI/code tokens from an unchanged
git-worktree code block (`checkout`, `detach`, `add`, `phase-X-Y`), and
verbatim-quoted English (Gemini CLI self-quote, Register quote, Uber COO
quote — same citation convention as the pre-existing Böckeler/Fowler/
Stenberg quotes elsewhere in this deck, confirmed via grep that this deck's
already-approved slides use the identical pattern, e.g. s31's Replit
"code-freeze"/`accountability не делегируется` title).

### Итоги round 3

- **57 слайдов** (было 50): +7 new (s09b/s17b/s18b/s20g/s30b/s33b/s37b) +
  1 order-swap (s20d↔s20e, no net slide-count change) + 6 content-only
  fixes (s16/s21/s25c/s34/s37-matrix/s38-triangulation).
- `deck.yaml`/`deck-part2.yaml` synced: `total_slides`/`totals.slides`
  50→57, `version` v4.0→v4.4, `slide_times_sum_min` 109.5→130.5 (+21 for 7
  new × 3 min), `ai_failure`/`ai_failure_judgment` in-bucket lists +5
  slides each (s17b/s18b/s20g/s30b/s37b — s09b and s33b deliberately left
  out, mixed success+honest-failure content per Решение #78 partial→out),
  count 16→21, share ≈45% (well above the 30% threshold, self-estimate
  pending methodology-critic re-confirm same as pre-existing Ч1/Ч2/Ч5
  chapter self-estimates), `verify_day_of_items`/`fact_check_items`
  extended with 6+6 new volatile-fact entries for the round-3 sources.
  Pre-existing `id:s19`-file-field drift bug fixed in passing (it
  collided with the corrected `id:s18` entry once that was pointed at the
  right real file) — everything else flagged as pre-existing drift in
  round 2's log (id:s09/s10/s11, id:s15/s16, id:s21/s37-triangulation
  label mismatches) intentionally left untouched, per "не чини старый
  дрейф" from round 2.
- Word-count gate: all 7 new slides' speaker notes confirmed in [150,300]
  via PPTX `notes_text_frame` extraction (excl. "Источники:" block):
  s09b=223, s17b=229, s18b=276, s20g=256 (after the advisory/authoritative
  fix, re-confirmed at 256, still in range), s30b=245, s33b=245, s37b=268.
  s21 and s38 (GitClear-2026 additions to existing slides) trimmed back
  into range: s21 390→300, s38 landed at exactly 300 on first pass.

---

## Round-3 QA-fix pass (2026-09-21) — against presentation-critic.md + student-simulator.md

Scope: bounded fix pass against the two 2026-09-21 QA reports
(`qa-reports/2026-09-21/presentation-critic.md`, `.../student-simulator.md`).
Generate→Convert→Inspect→Fix per touched slide (min 1 real re-render +
visual re-inspect per slide after every content edit, not batched into one
full-deck cycle — this is exactly the discipline the QA reports said round-3
skipped).

**1. deck.yaml/deck-part2.yaml order-desync — re-verified independently,
critic's table found NOT reproducible for 7 of its 8 flagged slides.**
Critic claimed s11b/s17b/s18b/s25b/s25c/s33b/s35b/s37b all render AFTER
their declared neighbor instead of before. Cross-checked every one against
(a) direct `python-pptx` text extraction of the actual rendered PPTX per
page and (b) `build_lec04_v4.py`'s own `builders` list (unambiguous ground
truth, not subject to interpretation) — both sources agree with each other
and **disagree with the critic's table** for all 8: s11b (between s10/s11 —
matches declared), s17b (between s17/s18 — matches), s18b (between s18/s19 —
matches), s25b/s25c (between s24 and s25-divider — matches), s33b (between
s33/s34 — matches), s35b (between s34/s35-divider — matches), s37b (between
s37/s38 — matches). **No changes made to any of these 8** — moving them per
the critic's table would have broken currently-correct documentation.
**Found instead (not in critic's table): `s30b` genuinely mis-declared** —
YAML said "between s30 and s31", actual render (verified same two ways) is
between **s29 and s30** (page 42=s29, page 43=s30b, page 44=s30, page
45=s31). Fixed: moved the `id: s30b` entry in `deck-part2.yaml` to between
`id: s29` and `id: s30`, corrected its placement comment and the
`base_slides_locked` prose note.

**2. Dead `file:` refs + total_slides/id-count reconciliation.** Fixed
`id: s39` → `slides/s40-checklist.md`, `id: s40` → `slides/s41-bridge-qa.md`
exactly as recommended. Root-caused the 56-declared-ids-vs-57-rendered-
slides gap (critic guessed it was near s41 — it was not): `build_lec04_v4.py`
has a distinct builder `b1.s05f` ("Эта лекция — сводка практик...",
display position 5, BEFORE the keystone at position 6) that had **no
declared id anywhere** in either YAML file — the existing `id: s05` entry
actually describes the keystone (position 6, function `b1.s06k`), confirmed
by matching its assertion text 1:1 against the rendered slide. Added a new
`id: s05f` entry (file `slides/s05-foundations-practices.md`, the real file
already on disk) immediately before the existing `id: s05`, and — since
already touching that neighborhood — corrected `id: s05`'s own `file:`
field from the non-existent `slides/s05-keystone-git-loop.md` to the real
`slides/s06-keystone-git-loop.md` (did **not** extend this fix to the ~27
other pre-existing dead `file:` refs across s06–s40, which predate this
session and are out of this bounded pass's scope — flagged below for a
future pass). Result: 57 unique declared ids == 57 rendered slides == both
`total_slides` fields, verified via `yaml.safe_load`.

**3. s37-synthesis-matrix word-wrap.** Confirmed the bug on the "before"
render: "Документаци"/"я" split across 2 lines, no hyphen. Fixed by
widening the phase-label column 1.65in→1.95in (trimmed 0.15in each off the
"Ведущая практика"/"Режим отказа" columns, sum unchanged at 12.25in) rather
than shrinking the font (already below the general body-text floor at
size 10, so shrinking further was rejected per the brief's own guardrail).
Re-rendered and visually confirmed: "Документация" now sits on one line.

**4. Anglicisms — s09b/s20g/s37b.** s09b: "AI-agent deployments"→"внедрений
AI-агентов", "76% failed"→"76% отказали", "MEDIUM confidence"→"Средняя
достоверность", "LOW-MEDIUM confidence"→"Низкая-средняя достоверность",
"Production-ready"→"Продакшен-готовый", "spec-first workflow"→"рабочий
процесс spec-first", "life sciences"→glossed "life sciences
(фарма/биотех)". s20g: "credentials"→"учётных данных", "issue"→"тикета",
"hook'а"/"hook'ов"→"хука"/"хуков" (declined without apostrophe, matching
how the rest of the deck handles borrowed dev terms); left "pre-commit
hook", "CI-gate", "server-side push-protection", "OS-level sandboxing",
"file-tool" untouched (out of this pass's narrower scope; critic's broader
list flagged these too but the fix brief explicitly scoped only the 3
above) and kept the verbatim English incident quote as-is (legitimate
exception). s37b: "Agentic adoption"→"Внедрение агентных практик",
"life sciences"→glossed "(фарма/биотех)" (2nd of 2 occurrences in the
deck, now consistent with s09b). `_helpers.py` REFS_DATA entries for
`s09b`/`s37b` (the "Источники:" block appended to speaker notes) updated
to match. Re-ran `deep_latin_scan.py` on all 3 slides' extracted PPTX text
post-fix — every one of the specifically-flagged tokens (`failed`,
`confidence`, `AI-agent`, `deployments`, `Agentic`, `adoption`, `issue`,
`credentials`, `hook'a`, `hook'ов`) is confirmed gone; remaining unique
tokens are brand/product names (AWS, Kiro, Uber, Gitleaks, TruffleHog, The
Register, Fortune, TechCrunch, Manning), the named methodology term
Spec-Driven Development/SDD/Spec Kit, the verbatim English quotes (Gemini
CLI, Register, Uber COO — legitimate exceptions), and already-Russified
hyphenated hybrids (`ad-hoc-промптинга`). None of these are the anglicisms
the QA reports flagged.

**5. s33b — MTTR/IaC gloss + 55%/8,4% disambiguation.** Added inline
glosses at first detailed use on the slide: "MTTR (mean time to repair,
время восстановления после сбоя)" in the BT Group caption line, "IaC
(инфраструктура-как-код; Terraform, K8s)" in the opening sentence of the
right card (title itself left as bare MTTR/IaC — too long to gloss both
acronyms there without a 3rd title line). Added the disambiguation clause
"(отдельное измерение, не тот же тренд)" directly into the 2026-benchmark
stat box, replicating the pattern s21/s38 already use correctly for their
two GitClear datasets (confirmed by re-reading both before writing this).

**6. s25c — named the ≈77% metric.** Checked `chapter-part4.md` §4.5:
"точность ≈77% — self-reported вендором" — the metric is **точность**
(accuracy of the generated pytest skeletons). Changed "≈77% self-reported"
→ "≈77% точность self-reported".

**7. s37b redesign (headline + backref).** Reworded the headline from "Тот
же продукт — два регистра: решает не бренд, а применённая дисциплина" (which
over-claimed "same product" for the whole slide, when only the right-hand
Kiro card actually shows two registers of one product — Uber on the left is
a different product) to "Решает не бренд, а применённая дисциплина — два
примера" — student-simulator's option (b), which also better matches the
chapter's own §7.2 framing (Uber and Kiro as two separate same-tier
illustrations, not literally "one product twice"). Kept both cards
unchanged in layout; the existing right-card sub-heading "AWS Kiro — тот же
продукт, два регистра" already correctly scopes that specific claim to
Kiro once the overclaiming top-level headline was fixed, so no further
restructuring was needed there. Added an explicit backref in the
Kiro-success text: "(тот же кейс, что уже был в начале лекции)" — dropped
the brief's own suggested "§1" tag from the final wording after re-checking
it against the ENFORCED "no visible §-cross-references in body" pattern-grep
(CLAUDE.md No Extra Content Rule item 11); plain language achieves the same
signpost without touching that pattern.

**8. GitClear density (student-simulator, s21-per-student's-own-numbering
= actually `id: s20`, function `s20` in `slides_band2.py`).** Note: the
exact quoted text in the finding ("211М строк... 623М изменений...
рефакторинг 21→3,8%... дубли +81%... churn +15%") is verbatim from the
"70%-проблема" slide's GitClear card, which is `deck.yaml`'s `id: s20`, not
`id: s21` (student-simulator's own id-labeling in this deck is internally
consistent with the codebase's `refs_of_slide()`/ref-registry keys, which
run one off from `deck.yaml`'s declared ids in this stretch of the deck —
same historical drift as finding #2 above, not a new bug). Split the single
dense paragraph into 3 short lines via `text_box`'s existing `\n`→
`add_paragraph()` support (already used elsewhere in this codebase, see
`notes/mcp-limitations.md` — not the `run.text`-embedded-`\n` anti-pattern):
2020–24 stat / 2023–26 stat / "(Оба — корреляция, не RCT.)" caveat, each on
its own line. The "two independent samples, not one trend" framing (already
present via the "два независимых замера" card header and the trailing
caveat) is unchanged, just easier to scan.

**P2s applied:** s17b "check"→"проверка", closing banner trimmed to one
clause. s34's chart title/axis — same critic mislabeling issue as #8: the
DORA bar chart critic attributed to "s34" is actually on `id: s33`
(function `s33`, `gen_charts_v4.py`'s `c33_dora()`); `id: s34` ("docs bright
spot") has no chart. Reworded chart title "DORA · у эффекта AI парная
цена, %"→"DORA: у эффекта AI есть оборотная сторона, %" and y-axis "связь с
внедрением AI"→"изменение показателя, %"; regenerated via QuickChart
(network access confirmed working) and re-embedded. s20d "auto-changelog,
auto-semver по типам коммитов"→"автогенерация changelog и версии по типу
коммита".

**P2s skipped:** none — all 3 were low-risk and didn't require re-touching
an already-fixed slide for something unrelated.

**Not touched (explicitly out of this bounded pass's scope, flagged for a
future pass):** ~27 other pre-existing dead `file:` references across
`id: s06`–`id: s40` (non-letter-suffixed ids), all following the same
"declared file: points one slide-number below the real file on disk"
pattern as the `id: s05`/`s39`/`s40` cases fixed here — root cause is a
historical v4.1-era renumbering (foundations+keystone insertion) that
shifted physical filenames without updating every `file:` field; harmless
for rendering (the build script resolves slide content by hardcoded Python
function order + `load_notes()`'s id-prefix glob, never by the literal
`file:` string) but a real traceability gap for any future
consistency-checker pass that trusts `file:` literally.

**Verification run after all fixes:** rebuilt `lec-04.pptx` via
`build_lec04_v4.py` (57/57 slides, assertion passes), converted to PDF via
LibreOffice headless (57/57 pages), re-snapshotted every touched page at
150dpi and visually re-inspected each. `yaml.safe_load` on both deck YAMLs:
57 unique ids, 0 duplicates, `total_slides`/`totals.slides` both 57,
matches rendered page count. Pre-render scaffold/timing/methodology grep
across all 10 touched pages (visible body + speaker notes): only
pre-existing, already-triaged false positives (Devin's own "лимит 45 мин"
benchmark parameter; "методическая практика" as SDLC subject matter on
s36/matrix, same false positive the critic's own report already
documented; pre-existing `§1.1`/`§5.7` refs in the s37b notes "Источники:"
source list, unchanged by this pass except for the added "(фарма/биотех)"
gloss next to them) — zero new violations introduced.
