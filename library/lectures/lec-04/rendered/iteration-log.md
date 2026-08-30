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
