# Iteration Log — Лекция 4, Part 2

`iteration-log.md` (part 1) is already at 1083 lines (pre-existing, over the
CLAUDE.md 600-line doc-size limit before this round touched it) — continuing
here per the lec-03 precedent (`iteration-log-part2.md`) rather than growing
part 1 further.

## Round-5 — real imgflip memes, replacing round-4's "meme = brand logo" miss (2026-09-22)

**Owner correction (verbatim intent):** round-4 added small official
brand-logo corner badges (curl / AWS / GitHub Copilot / Replit / Google
Gemini / Uber) on 7 slides and reported them as the "memes" ask. Owner:
that's not what "memes" means — wants actual internet memes (known template
+ custom caption), same method Лекция 2/3 already use successfully
(download blank template from imgflip, bake RU caption via PIL), not
reused/overlapping with Лек-2/3's own templates.

**Why round-4 fell short:** it tried a "real found meme" search via Reddit's
API (blocked, HTTP 403 in this sandbox) and rejected generic stock photos as
not-incident-specific — reasonable instincts, but never attempted the
method THIS COURSE already uses elsewhere (imgflip blank-template + PIL
caption bake). This round uses that method directly.

### Method

1. Fetched `https://api.imgflip.com/get_memes` (public, no-auth, top-100
   popular templates with confirmed id + direct image URL) instead of
   guessing/memorizing imgflip ids — a first attempt at hand-recalled
   template URLs produced at least one wrong id (a remembered "Stonks" URL
   actually resolved to Tuxedo Winnie the Pooh, an EXCLUDED lec-03 template
   — caught before download, abandoned that approach in favor of the API).
2. Cross-checked owner's exclusion list against actual directory listings
   (`lec-02/rendered/assets/web/*.jpg` + `lec-03/rendered/assets/web/
   memes-src/*`) + grep of both lectures' `iteration-log*.md` "meme"/"мем"
   sections — **owner's own list was incomplete**: found 8 additional
   already-used templates not in the owner-supplied list (Math Lady,
   Gandalf/token, Surprised Pikachu, Joker Burning Money, Pepe Silvia,
   Spotlight, Well Yes Actually No, Press X to Doubt). Final exclusion set
   = owner's 26 + these 8 = 34 templates, all avoided.
3. Downloaded 7 fresh, non-excluded blank templates directly from imgflip
   (`assets/web/memes-src/*.jpg` + `.url` sidecar per convention).
4. Wrote `gen_memes_r5.py` (technique ported from `lec-02/gen_memes_v33_r2.py`
   + `lec-03/make_memes_v6.py`: DejaVuSans-Bold, white-stroke-black impact
   text OR — new for this deck's real estate — a side caption panel in
   Ocean surface tint with a bordered box, used for 5 of 7 composites).
5. Baked RU captions (Russification per course convention; kept "diff" and
   "коммитит" bare — both already used bare elsewhere in this deck's own
   body text, e.g. s21's own gold_callout "читать diff до accept", s20d/e
   git-conventions slides use "коммит"/"коммитит" throughout — consistent
   with established deck vocabulary, not a new anglicism).

### Why a new "band" composite technique, not lec-02/03's column style

This deck (`build_lec04_v4.py`) is far denser than Лек-2/3 — every ocean_box
on every one of the 57 slides is packed edge-to-edge with body text; there
was no free ≥2in² gap inside any box on any of the 7 target slides without
rewriting substantial body copy (risking factual/citation fidelity on a
stats-heavy deck). Inspecting rendered PNGs found one **consistent, genuinely
empty** zone across nearly every slide instead: the gap between
`gold_callout`'s own bottom edge (~y=6.30-6.34in) and `refs_of_slide`'s text
(~y=7.02-7.06in) — roughly 0.6-0.7in tall, full slide width, present because
`gold_callout` and `refs_of_slide` are laid out independently and neither
fills that gap by design. Verified empty via direct pixel scan (see s31 fix
below) rather than assumed from code coordinates alone.

Built `compose_strip()`: crops the recognizable character(s) out of a
template, fixes height at 0.64in, appends a bordered Ocean-surface caption
panel (1-2 short lines, 13-15.5pt — physically legible, computed via
`font_pt/72*DPI` baked at DPI=300 so the final embed is crisp) sized to fit
the caption text, placed bottom-right of the slide (right of the ref list,
which is left-aligned and short enough not to reach that x-range on any of
these 7 slides — confirmed per-slide, not assumed). Used for 5/7 slides
(s15, s21-func/anti-hype, s27-func/review, s30-func/slopsquatting,
s18-func/persistent).

For the 2 portrait-native templates (Hide the Pain Harold, Boardroom
Suggestion) that don't crop cleanly to a short wide strip without losing the
joke: Harold's two panels were merged side-by-side (the joke IS that the
face doesn't change between "before" and "after" — showing both panels is
the point); Boardroom Suggestion was cropped to panel 3 only (the
consequence split, self-contained without needing the empty speech
bubbles filled). Both then ran through the same `compose_strip()` as the
other 5 — one unified technique across all 7, not two different systems.

### Per-slide placements (7 slides, 7 memes — all via the "band" slot)

| Meme | Template | Target slide (page / fn) | Caption | Fit rationale |
|---|---|---|---|---|
| `band-x-everywhere.png` | X, X Everywhere (Buzz/Woody) | p18 `b2.s15` — poisoned-context loop | «плохой паттерн, плохой паттерн везде» | reinforces the loop's own repetition ("AI копирует ещё увереннее") |
| `band-mocking-spongebob.png` | Mocking Spongebob | p32 `b3.s21` — anti-hype/SWE-bench gap | «фРоНтИр, в 4 рАзА бЫсТрЕе» | mocking-case echo of the Cursor quote already on this exact slide |
| `band-evil-kermit.png` | Evil Kermit | p40 `b3.s27` — review complacency + curl-slop | «надо прочитать diff» / «и так сойдёт» | direct callback to the complacency card on the same slide (left column) |
| `band-domino-effect.png` | Domino Effect | p44 `b3.s30` — slopsquatting/CamoLeak | «одно фейк-имя пакета → эксплойт» | cascading chain reaction matches slopsquatting's own 3-step chain diagram |
| `band-monkey-puppet.png` | Monkey Puppet | p22 `b2.s18` — persistent instructions/context rot | «решение тихо исчезло при сжатии» | silent-failure humor, though placed on the persistent-instructions slide rather than s18b (curation-limits) — see "s18 vs s18b" note below |
| `band-hide-the-pain-harold-merged.png` | Hide the Pain Harold (both panels) | p31 `b2.s20` — 70%-problem | «выглядит нормально — падает в 3 часа ночи» | false-confidence: the "почти правильный код" thesis IS Harold's own joke (nothing looks different until it breaks) |
| `band-boardroom-panel3.png` | Boardroom Suggestion (panel 3) | p45 `b4.s31` — Replit culmination | «не трогать!» — «агент всё равно коммитит» | explicit human instruction ignored — the slide's own central point; **swapped for round-4's Replit logo badge**, not added alongside it |

**s18 vs s18b:** brief allowed either. Attempted s18b (curation-limits) first
— its 3-card row is packed edge-to-edge (checked: card height 3.30in,
content already fills to within 0.12in of the card bottom on all 3 cards);
fitting a meme there would have required shrinking all 3 cards ~25% and
rewording each body paragraph, risking the "почти всегда" precision Loss on
a slide that's specifically about honest technique limits. s18 (persistent
instructions main slide) had the same universal bottom-band gap as every
other slide and the "context rot" concept (silent degradation) is
close enough to "silent failure" to carry Monkey Puppet's joke without
touching any existing text. Flagging this substitution explicitly per the
brief's own "if you think X, do the swap/keep, just note reasoning" instruction.

### Kept round-4 logos (6 of 7) — reasoning per slide

- **s28/p40 (curl)** — curl-slop-as-DDoS card names curl's own real
  bug-bounty program; the logo IS the incident's subject, not decoration.
  Added Evil Kermit to the ADJACENT complacency card instead (same slide,
  left column) rather than crowding this card.
- **s30b/p43 (AWS)** — brief's own explicit suggestion to consider keeping:
  Amazon Q Developer is an AWS product and the slide's whole point is
  "trust extends to the vendor's own supply chain" — brand attribution
  matters more here than a joke. Kept as-is, no meme added to this slide.
- **s30/p44 (GitHub Copilot)** — CamoLeak specifically named "GitHub
  Copilot Chat" in the slide's own body text; direct incident attribution.
  Added Domino Effect to the OTHER column (slopsquatting) on the same
  slide instead.
- **s37b/p54 (Uber + AWS)** — both cards name the real companies as the
  case-study subject (Uber's own adoption story, Kiro as an AWS product);
  not evaluated as a meme candidate in this round (not on the brief's
  candidate-slide list, left untouched).
- **s17b/p21 (Google Gemini)** — Gemini CLI self-review incident,
  vendor-specific; not on the brief's candidate list, left untouched.

**Replaced:** s31/p45 (Replit) — see table above. Round-4's own log already
documented that a real "found meme" search failed here (Reddit 403 +
generic stock art rejected); Round-5's imgflip-template method succeeded
where that attempt didn't.

### Iteration discipline (Generate→Convert→Inspect→Fix, ≥3 per touched slide)

Built a fast single-slide test harness (`render_test.sh` + `/tmp/
single_slide.py`, reusing this deck's own `render.sh` LibreOffice/profile
setup) instead of rebuilding all 57 slides per edit — renders one function
to an isolated one-slide PPTX/PNG in ~15s vs. the full-deck build+convert.

- **s15 (p18)** — iter1: composed X-Everywhere band meme, placed bottom-
  right, rendered clean on first placement (no defects found). iter2:
  pixel-cropped zoom on the meme/ref-list boundary — confirmed no overlap.
  iter3: full-deck rebuild + re-snapshot at true page 18 — confirmed page-
  number stamp (bottom-right, y=7.16-7.44) doesn't collide either (different
  y-band from the meme).
- **s21-func/p32** — iter1 clean placement first try (same band pattern
  already validated on s15). iter2/iter3: re-inspected for kerning/contrast
  on the mocking-case caption specifically (alternating case is harder to
  misjudge for legibility) — confirmed readable at final embed size.
- **s27-func/p40** — iter1: initial render showed the 5-entry ref list
  wrapping to 2 lines (this slide has 5 citations vs. others' 1-3) — visual
  concern that the wrapped second line might run under the meme. iter2:
  pixel-cropped the exact boundary region — confirmed the wrap happens at
  the FAR LEFT (citation text restarts at x=0.55) and never reaches the
  meme's x-range (8.96-12.80in); no actual collision, false alarm caught
  and resolved by direct measurement rather than assumption. iter3: full-
  deck re-render at true page 40, re-confirmed.
- **s30-func/p44** — iter1 clean placement. iter2: verified GitHub Copilot
  logo (kept, right column) and new Domino meme (left column, bottom band)
  don't create a "two competing visual elements" imbalance — confirmed
  fine, they're on opposite slide halves and different visual zones (corner
  badge vs. bottom band). iter3: full-deck re-render, confirmed.
- **s18-func/p22** — iter1 clean placement, no collision with the existing
  (pre-existing, round-4-era) "flame" icon in the adjacent context-rot box
  — different location entirely. iter2/iter3: re-inspection, confirmed
  clean at true page 22.
- **s20-func/p31 (Harold)** — iter1: built the two-panel merge, composed
  into the band format — clean on first placement (band technique already
  validated 3× by this point in the round). iter2/iter3: verified caption
  physical size (13.5pt) reads clearly at the final 4.79×0.64in embed size;
  confirmed against the 5-entry-vs-2-entry ref-list-width lesson from s27 —
  this slide has only 2 refs, no wrap risk.
- **s31-func/p45 (Boardroom, REAL FIX FOUND)** — iter1: removed the round-4
  Replit logo badge, placed the meme at y=6.36in (same offset formula as
  the other 6 band slides) — **rendered with the meme's top edge visibly
  touching the gold_callout's own last text line** ("Accountability не
  делегируется."). Investigated via direct pixel scan (`numpy` mask over
  the rendered PNG, restricted to the callout's own x-range to exclude the
  meme's own caption text from polluting the measurement — first scan
  attempt incorrectly included the meme's caption pixels and reported a
  false 6.93in "overflow" that was actually my own new text) — confirmed
  the callout's real text bottom is 6.35in against a 6.30in box (a ~0.05in
  pre-existing, trivial rendering slack, NOT a real overflow bug) but my
  meme's y=6.36in left near-zero breathing room. **Fix:** nudged meme to
  y=6.50in, h=0.56in (from 0.64in), width rescaled to preserve the
  composite's native aspect ratio (3.82in from 4.37in). iter2: re-rendered,
  re-cropped the same boundary — confirmed clear gap now. iter3: full-deck
  rebuild, re-confirmed at true page 45, also confirmed the ref list
  (1 entry only, far left) still clear.

### Systematic verification pass (all 7, after individual iteration)

Ran a `numpy`-based pixel scan across all 7 slides' `gold_callout`-to-meme
boundary (not just the one that needed fixing) — confirmed callout text
bottoms cluster at 6.26-6.28in against the standard 6.34in box on 6/7
slides (comfortable ≥0.12in gap to each meme's y=6.40in start), and the
7th (s31/Replit, different box geometry: y=5.70/h=0.60→6.30) is the one
documented fix above. Full 57-slide `build_lec04_v4.py` re-run (57/57
assert pass) + full-deck LibreOffice convert + all 7 true page numbers
re-snapshotted and re-read visually one final time in situ (with the
page-number stamp present, confirming no collision with that either).

### Pre-render greps (CLAUDE.md-mandated set)

Ran against a fresh full-deck python-pptx text extraction (978 text runs,
title+body shapes, all 57 pages) post-rebuild:

- `[VERIFY-DAY-OF]` / `[FACT-CHECK]` / `LO[1-9]` / `§[0-9]+\.[0-9]+` /
  `→ s[0-9]+` / `\(s[0-9][0-9]\)` / "Вы здесь" / "Лектору" — 1 hit, p52
  "§1–§6" — pre-existing body-content cross-reference within a vendor-names
  sentence (not a navigation/forward-ref marker, not touched this round,
  not on any of the 7 target slides).
- Timing markers (`[0-9]+\s*мин`, "Тайминг", "Длительность", ⏱/⏰) — 1 hit,
  p32 "лимит 45 мин" — the SAME pre-existing Devin-benchmark-parameter
  false positive already triaged in the round-3 log entry (part of the
  SWE-bench body text on the exact slide I added a meme to, but the meme
  itself introduces no new text — this is 100% pre-existing content).
  This slide (p32) IS one of my 7 targets, so double-checked specifically:
  confirmed the "45 мин" phrase sits in the pre-existing Devin bullet body
  ("...лимит 45 мин; независимо ~15%..."), not anywhere near or related to
  my meme addition.
- Methodology meta-commentary (`методическ`, `педагогическ`, "На этом
  этапе студент", "Зачем это в Лекции") — 0 hits.

**Caveat on this grep's own coverage:** the 7 baked meme captions are NOT
extractable via python-pptx (they're pixels inside a PNG, not PPTX text
runs) — they were verified manually by eye instead (see the composite PNGs
referenced in the table above). None contain timing/methodology/scaffold
language; all are short in-character jokes.

### Deep latin-token / anti-anglicism check on the 7 baked captions (manual, not automatable via the pptx-text-extraction tool)

All 7 captions are Russian except two already-established deck terms used
bare elsewhere in this deck's own visible body text: "diff" (s21's own
gold_callout: "читать diff до accept"; s27-func's own body: multiple bare
uses) and "коммитит"/"коммит" (s20d/s20e git-conventions slides use this
russified verb form throughout). Both are consistent with existing deck
vocabulary, not new anglicisms introduced by this round.

### Touched files

- `library/lectures/lec-04/rendered/gen_memes_r5.py` (new) — generation
  script, run via `python3 gen_memes_r5.py`.
- `library/lectures/lec-04/rendered/assets/web/memes-src/*.{jpg,jpg.url}`
  (new, 7 templates + sidecars) + 2 derived source crops
  (`hide-the-pain-harold-merged.jpg`, `boardroom-panel3.jpg`).
- `library/lectures/lec-04/rendered/assets/web/band-*.png` (new, 7
  composites — the actual embedded images).
- `library/lectures/lec-04/rendered/assets/web/attribution.md` (new).
- `library/lectures/lec-04/rendered/_helpers.py` — added `WEB = ASSETS /
  "web"` constant.
- `library/lectures/lec-04/rendered/slides_band2.py` — `WEB` import added;
  `s15`, `s18`, `s20` each get one `add_image(...)` call added before their
  `refs_of_slide(...)` line. No existing text/shape touched.
- `library/lectures/lec-04/rendered/slides_band3.py` — `WEB` import added;
  `s21`, `s27`, `s30` each get one `add_image(...)` call added, same
  pattern. No existing text/shape touched.
- `library/lectures/lec-04/rendered/slides_band4.py` — `WEB` import added;
  `s31` has its round-4 Replit logo badge (2 shapes: image + caption
  text_box) REMOVED and one `add_image(...)` call added in the bottom band.
- `library/lectures/lec-04/rendered/render_test.sh` (new) — fast single-
  slide render helper for the iteration loop (see above).
- `library/lectures/lec-04/rendered/lec-04.pptx` / `.pdf` — rebuilt,
  57/57 slides.
- `slides/*.md` — **NOT touched** (per round-4's own documented
  architecture note: these are a planning layer that has already drifted
  from the true render source in `slides_band*.py`; this round follows the
  same "не чини старый дрейф" precedent and did not attempt an .md↔.py
  resync, which was out of scope for a meme-only ask).
- `chapter.md` / `chapter-part*.md` / `speech.md` — **NOT touched** (out of
  scope per brief).

### Final count

**7 slides touched, 7 real memes added** (below the brief's 6-10 target
range's upper half, at the lower-middle — honest count, not rounded up).
6 of round-4's 7 logo badges kept as-is (reasoned per-slide above); 1
(Replit) swapped for a meme. No new slides added. No overlap with Лек-2/3's
34-template combined exclusion set (26 owner-listed + 8 found on
independent re-check).

---

## Round-6 Block 5 — закрывающий кластер (p54–p57) + статистика по отрасли в начале (#162)

Ветка `issue-162-lec04-block5-closing`, worktree `/tmp/lec04-block5-closing`.
Параллельно с четырьмя другими блоками раунда 6; тронуты ТОЛЬКО перечисленные
ниже слайды. **Итог: 57 → 58 слайдов** (+1 вставлен в начало).

Нумерация: `pNN` = позиция в колоде ДО этой правки (как в замечаниях
владельца). После вставки s03b всё начиная с бывшего p4 сдвинуто +1.

### 1. p54 (`slides_band4.s37b`, теперь p55) — «нет эффектов»: диагноз

Замечание владельца дословно: «слайд 54 - нет эффектов». Формулировка
неоднозначная, поэтому сначала — рендер и разбор, потом правка.

**Что проверялось (в порядке приоритета из брифа):**

- **(a) дефект рендера.** Отрендерил p54 при 150 dpi и сверил с тем, что
  round-4/round-5 записали как «должно быть на слайде»: логотип Uber
  (Wikimedia, Tier 2) + логотип AWS + подписи-атрибуции + иконки `scale` /
  `split` + gold callout + список ссылок. **Всё на месте, ничего не потеряно.**
  Мем-полосы раунда-5 на этот слайд и не ставились (её 7 слайдов — p18, p22,
  p31, p32, p40, p44, p45), так что и тут пропажи нет. Гипотеза (a) — не
  подтвердилась.
- **(c) пропавший визуальный элемент из лога.** Тот же вывод: лог round-4
  §5 пункт 5 обещает ровно два логотипа, оба рендерятся. Не подтвердилась.
- **(b) слайд не доносит свой вывод — ПОДТВЕРДИЛАСЬ.** Несущий вывод левой
  карточки — что при росте внедрения в 2,6 раза **измеримого эффекта не
  появилось** — существовал на слайде ТОЛЬКО внутри непереведённой
  английской цитаты COO, набранной моноширинным 9,5 pt
  («It's hard to draw a connection… That link is not there yet»). По-русски
  слайд читался так: четыре внушительных числа про охват (32→84%, 95%, 70%,
  $500–2000) и строка про расходы. **Слова «эффект» на слайде не было
  вообще.** Заголовок («Решает не бренд, а применённая дисциплина») вывод
  тоже не нёс. То есть замечание «нет эффектов» читается буквально: на
  слайде нет строки эффекта — притом что именно она и есть его payoff
  (`assertion` в `slides/s37b-*.md` прямо говорит «сам COO признал, что связи
  с ценностью пока нет»). Побочно это же было и нарушением anti-anglicism
  mandate (§5.8): ключевое утверждение — непереведённым английским.

**Что сделано:**

1. Левая карточка перестроена в явную последовательность
   **«Масштаб внедрения → Эффект → Реакция»** (раньше: числа, цитата,
   строка про расходы — без ролей).
2. **«Эффект: не прослеживается»** вынесен отдельным ЗОЛОТЫМ блоком
   (`GOLD_TINT` + стройка `GOLD` 1.8pt) — это теперь и главный акцент
   карточки, и единственный gold-элемент верхней части слайда.
3. Цитата COO **переведена на русский** (перевод взят из `chapter-part5.md`
   §7.2, где он уже есть в скобках), с атрибуцией «— Эндрю Макдональд,
   президент и операционный директор Uber». Английский оригинал со слайда
   убран (остаётся в главе).
4. Заголовок несёт вывод: «**Масштаб внедрения — ещё не эффект:** решает не
   бренд и не охват, а применённая дисциплина» (было — только рамка про
   дисциплину).
5. Правая карточка: серая строка-мост дополнена «…здесь исход измерим в обе
   стороны — в отличие от масштаба без критерия слева» — так контраст
   «слева эффекта нет / справа измеримый исход в обе стороны» становится
   явным, а не подразумеваемым.
6. Gold callout начинается с «Рост внедрения сам по себе не является
   результатом: 2,6× за месяц без заранее заданного критерия дали рост
   расходов и неподтверждённый эффект».
7. `фарма и биотех (life sciences)` — русское ведущее, английское как
   глосса (было наоборот).

**Остаточная неопределённость (честно):** формулировка «нет эффектов» —
две буквы от «не видно эффектов на слайде» и от «покажи, что эффектов нет».
Обе читаются одинаково и обе закрываются одной и той же правкой, поэтому
дальше уточнения не требовалось. Если владелец имел в виду третье (напр.
анимационные эффекты появления — их в этом деке нет нигде), правка всё
равно не вредит, но тогда исходное замечание остаётся открытым — это
отмечено в отчёте assembly-проходу.

### 2. НОВЫЙ слайд s03b (display p4) — общая статистика по отрасли

Замечание: «и в начале презы надо добавить общую статистику по отрасли».

**Место вставки.** Прочитаны p1–p10. Поток вступления: p1 hook METR → p2
обложка+роадмап → p3 мост из Модуля 1 → p4 центральный вопрос → p5 фундамент
практик → p6 keystone. Статистика вставлена **между мостом и центральным
вопросом**: сначала масштаб («внедрять или нет» индустрия закрыла), сразу
после — вопрос лекции («что делает это надёжным»). Это же даёт смысловую
скобку с переформулированными p55/p56 в конце: там ровно та же мысль —
спор «да/нет» снят, считается цена и меры.

**Цифры — только проверенные веб-поиском в день правки, обе первичные:**

| Число | База / counterfactual | Источник |
|---|---|---|
| 84% используют или планируют использовать AI-инструменты | 76% годом ранее (2024); n > 49 000 из 177 стран | Stack Overflow Developer Survey 2025 (пресс-релиз + раздел AI) |
| 51% профессиональных разработчиков — ежедневно | половина от тех же респондентов | Stack Overflow 2025, раздел AI |
| 90% используют AI в работе | +14 п.п. к 2024; n > 5 000 | DORA / State of AI-assisted Software Development 2025 |
| медиана ~2 ч/день | ≈ четверть 8-часового рабочего дня | DORA 2025 |
| 46% не доверяют точности вывода | против 31% годом ранее | Stack Overflow 2025 (пресс-релиз) |
| >80% отмечают рост эффективности / 24% высоко доверяют | контраст внутри одной выборки | DORA 2025 |

Каждое измеримое утверждение несёт базу прямо рядом (§ Baseline /
Counterfactual Mandate). На слайде есть явная честная оговорка о разнице
формулировок опросов («используют или планируют» у SO vs «используют» у
DORA) — числа не складываются и не выдаются за одну шкалу.

**Проверка на дублирование по деку:** ни 84%-adoption, ни 90%, ни 51%, ни
46%/31% в деке раньше не встречались. Совпадение чисел с s37b («84%» у Uber)
— разной природы, поэтому герой-число нового слайда намеренно **90%**
(DORA), а не 84%, чтобы одинаковая цифра не работала мега-стат дважды.
Существующее «SO 66% почти правильно» (p20) не трогалось и не повторено.

**Артефакты:** `gen_charts_r6b5.py` (новый) → `assets/charts/c03b-adoption.png`
(QuickChart, Ocean-палитра, 76 / 84 / 90; последний столбик gold);
`slides/s03b-industry-adoption.md` (новый, заметки 285 слов);
`_helpers.py` — `URLS["so_survey_2025_ai"|"so_survey_2025_press"]` +
`SLIDE_REFS["s03b"]`; `slides_band1.s03b`; `deck.yaml` — запись слайда +
`total_slides: 57 → 58`; `build_lec04_v4.py` — вставка в список builders,
ассерты 57 → 58.

### 3. p55 (`slides_band4.s38`, теперь p56) — переформулировка «не да/нет, а уровень»

Замечание: «уже не стоит вопрос да или нет. всегда да, но вот цена, риски и
соответственно инструменты их митигации надо понимать и применять».

Сверено с `chapter-part5.md` §7.3 — книга и так **не бинарна**: «не
"доверять / не доверять AI" вообще, а на каждой задаче перемножать три оси и
ставить контроль туда, где произведение это требует». Бинарность была
привнесена слайдом. Механика триады не менялась (три оси, перемножение,
зона low×low×high, «какую ось чинить») — она и есть аппарат расчёта уровня.

- Заголовок: «risk-triad: "когда AI да / нет" = …» → «**Вопрос не «AI или
  нет», а какой уровень автономии:** вероятность × влияние × обнаружимость».
- Добавлена бирюзовая полоса-тезис под заголовком: «AI в том или ином
  режиме применяется почти всегда — триада отвечает не «да / нет», а какой
  потолок автономии допустим и чем он оплачен».
- «Зона допустимого vibe-coding» → «**Где потолок автономии самый высокий**»;
  «Любая другая комбинация → дисциплина» → «Любая другая комбинация — **не
  запрет AI**, а потолок ниже и обязательные меры».
- «Триада подсказывает, что чинить» → «**Чем оплачивается более высокий
  уровень**» (те же три меры — они и есть «инструменты митигации» из
  замечания).
- Gold callout: цитата Бёкелер оставлена дословно, рамка дописана вне
  кавычек — «решение принимается не один раз и не про инструмент целиком, а
  на каждой задаче»; «игнор всех трёх осей» → «ни одна из трёх осей не
  посчитана».
- Заметки (272 → 300 слов) переписаны под ту же рамку.

### 4. p56 (`slides_band4.s39`, теперь p57) — парная переформулировка

Замечание: «соответственно тоже, не да/нет, а как и когда».

Сверено с `chapter-part5.md` §7.4: «чек-лист — это **распределение бремени
доказательства**, а не "всегда выбирай меньше AI"… для подходящей задачи
чек-лист **приведёт** к высокой автономии осознанно». Снова: книга не
бинарна, бинарен был слайд.

Восемь вопросов сохранены (они и есть рабочий критерий), переформулированы
как настройка режима:

- Заголовок: «Чек-лист "когда AI да / когда нет" + что это значит лично для
  вас» → «**Восемь вопросов — не «AI или нет», а как, где и с каким
  контролем его применить**».
- п.1 «Какая это фаза?» → «…**Она задаёт режим отказа**».
- п.2 (самый бинарный, отмечен в брифе) «Можно ли решить без AI? Да → не
  добавляйте AI» → «**Что здесь решается детерминированно? Эту часть пишет
  обычный код, AI — на разбор и проверку**» — ровно рассуждение из
  mini-apply §7.4 главы (детерминированную часть — кодом, узкий AI-шаг — на
  разбор).
- п.3 «→ человек» → «**решает человек, AI на периферии**».
- п.4 (вето) «→ жёсткий гейт» → «→ **потолок автономии вниз**, жёсткий гейт».
- п.5 «Нет → не доверять» → «→ **сначала оракул, потом автономия**».
- п.6 «least-priv + изоляция» → «**минимум прав и изоляция**» (русификация).
- п.7 «Merge и accountability» → «**Слияние и ответственность**» (русификация).
- п.8 «→ не делегировать генерацию» → «→ **генерацию не делегировать**».
- Gold callout: «**Чек-лист не решает «применять AI или нет» — он выдаёт
  режим**: для подходящей задачи приведёт к высокой автономии, для
  неподходящей — опустит потолок и назовёт обязательные меры…».
- Строка «при обучении писать должны вы» переехала из callout в правую
  колонку, к данным Anthropic, к которым она относится.
- Заметки (318 → 298 слов) переписаны под ту же рамку.

**Согласованность пары p55/p56 (проверено отдельно):** обе теперь используют
один словарь — «потолок автономии» / «режим» / «обязательные меры» / «не
запрет AI»; обе явно отрицают бинарность в заголовке одной и той же
конструкцией «не «AI или нет», а …»; p55 даёт аппарат расчёта уровня, p56 —
восемь вопросов, которые этот уровень настраивают. Термин «триада риска»
приведён к одному виду и в заметках закрывающего слайда (был `risk-triad`).

### 5. p57 (`slides_band4.s40`, теперь p58) — убрана отсылка к семинару

Замечание: «убрать отсылку к семинару». Это была **регрессия**, а не первый
недосмотр: `visual_brief` слайда s40 (чек-лист) с раунда 1 прямо фиксирует
«БЕЗ «mastery — Семинар 4» (эти — в речи Phase 9, не на слайде)» — то же
правило на закрывающем слайде нарушалось.

- Удалён бирюзовый блок «Семинар 4 — примените чек-лист к реальным кейсам
  своими руками» (2 шейпа: `filled_rect` + `text_box`).
- Удалена та же отсылка из **заметок докладчика** («Парный Семинар 4 — место,
  где вы примените чек-лист…») — заметки печатаются в раздаточный
  notes-PDF, то есть тоже студенческий артефакт.
- `learning_goal` и `visual_brief` в `.md` обновлены (мост теперь — к
  следующим отраслевым лекциям, а не к семинару).
- **Перебалансировка после удаления** (иначе между блоком метода и
  «Вопросы?» оставалась дыра ~0,6"): ocean-box метода вырос 2,72 → 3,02",
  шаг нумерованных пунктов 0,50 → 0,56", кегль пунктов 10,5 → 11 pt,
  «Вопросы?» 30 → 32 pt. Ничего нового на слайд не добавлено.

### Итерации Generate→Convert→Inspect→Fix

Полный дек пересобирался и конвертировался целиком на каждой итерации
(`build_lec04_v4.py` → LibreOffice → PDF → PNG 150 dpi через
`render_local.sh` — копия `render.sh` с путём этого worktree).

- **iter 1 (все 5 слайдов):** первая сборка. Найдено: (p56) gold callout
  переполнен — последняя строка «(вероятность ↑).» вылезла за нижнюю грань
  плашки; (p56) грамматическая ошибка «только при низкая × низкая × высокая»;
  (p56) буллет «машинный оракул (тест, SAST, прогон)» переносился на вторую
  строку и налезал на следующий; (p55) gold callout переполнен после
  удлинения текста; (p58) после удаления полосы «Семинар 4» осталась дыра;
  (p4) заголовок карточки дублировал заголовок диаграммы; (p4) диаграмма
  чуть высока, нижние подписи поджаты.
- **iter 2:** p56 — колонки опущены (ay 1,90 → 1,94, ah 1,00 → 1,06),
  gold-плашка 1,56 → 1,70", ocean-плашка 1,42 → 1,58", callout 0,88 → 1,00"
  и y 5,14 → 5,44; грамматика и буллеты переписаны. p55 — callout 0,62 →
  0,78", y 5,72 → 5,66. p58 — бокс 2,72 → 3,02", шаг 0,50 → 0,56",
  «Вопросы?» на 6,36. p4 — заголовок карточки «Масштаб: почти вся отрасль
  уже внутри», диаграмма 2,30 → 2,16", тексты подняты. Перерендер: все
  переполнения ушли.
- **iter 3:** прицельная вычитка. p55 — «life sciences (фарма/биотех)» →
  «фарма и биотех (life sciences)» (русское ведущее). p57 — снят голый
  «(least-privilege)», callout 0,78 → 0,86". Прогон трёх обязательных greps
  по извлечённому из PPTX тексту (visible + notes).
- **iter 4:** правки по итогам greps и deep-latin-scan (см. ниже) +
  приведение длины заметок к 150–300 слов; финальный полный рендер всех 58
  страниц, соседние нетронутые слайды (p5 центральный вопрос, p54
  триангуляция) перечитаны — не поехали.

**5-секундный тест (после iter 4, на PNG 150 dpi) — 5/5 PASS**, прочитанное
совпало с `assertion`: p4 «почти вся отрасль уже пользуется, но доверяет
меньше половины» · p55 «внедрение выросло в 2,6×, а эффекта нет» · p56
«вопрос не да/нет, а какой уровень автономии» · p57 «восемь вопросов про как
и с каким контролем» · p58 «цена написания кода ≠ цена понимания».

**Projector 50%:** минимальные кегли — 9 pt (служебная оговорка о методологии
опросов на p4), 9,5 pt (перевод цитаты, подписи осей p56), 10,5 pt тело,
12–13 pt подзаголовки, 19–22 pt заголовки; несущие тезисы ≥ 10,5 pt.

### Pre-render greps (независимый прогон по собранному PPTX, 58 слайдов)

Извлечение через `python-pptx`: видимый слой (все text_frame) + заметки.

- **scaffold** (`Лектору|Преподавател|Вы здесь|[VERIFY-DAY-OF]|[FACT-CHECK]|
  LO[1-9]|§[0-9]|→ sNN|(sNN)|Семинар|…`) — **0 на моих пяти слайдах**
  (видимый слой и заметки). По деку осталось 2 видимых + 3 в заметках:
  p53 «§1»/«§6» (тело предложения про вендор-имена), p14 «§2», p53 —
  всё пре-существующее на чужих слайдах, не трогал. Отдельно найдено и
  **исправлено** своё: в `SLIDE_REFS["s37b"]` глосса содержала «(§1.1)» и
  «(§5.7)», которые попадали в блок «Источники:» заметок p55 — §-ссылки
  из глоссы убраны.
- **timing** (`\b[0-9]+\s*мин(ут)?\b|Время раздел|Тайминг|Длительность|⏱|⏰`)
  — **0 на моих пяти**. По деку: p33 «45 мин» (параметр бенчмарка Devin,
  уже триажировано в раунде 3), p28 «ДЛИТЕЛЬНОСТЬ» (слово из содержания
  чужого слайда).
- **методология** (`(методическ|педагогическ)\w*|На этом этапе студент|…`) —
  **0 на моих пяти**. По деку: p9, p2, p53 — пре-существующее.

### Deep latin-token scan (broad regex + brand-allowlist), мои 5 слайдов

Видимый слой + нарративная часть заметок (блок «Источники:» исключён — URL и
названия отчётов там латиницей законно).

Не-allowlisted unique: p4 = 1 (`AI-`, обрывок «AI-инструменты») · p55 = 4
(`AI-`, `Kiro-` — обрывки; `life sciences` — оставлено глоссой после русского
«фарма и биотех») · p56 = 1 (`senior-`, термин дека) · p57 = 0 · p58 = 1
(`CC-BY-SA`, лицензия в подписи к фото).

По ходу **исправлены реальные англицизмы** в заметках p55: «agentic coding
users» → «тех, кто работает в агентном режиме», «success story» → «история
успеха», «production-ready» → «готовый к проду», «spec-driven-дисциплина» →
«спека-first дисциплина» (термин дека). В видимом слое p56/p57 заменены
«Merge и accountability» → «Слияние и ответственность», «least-priv» →
«минимум прав».

**Длина заметок (150–300 слов):** p4 = 285 · p55 = 279 · p56 = 300 ·
p57 = 298 · p58 = 232. Связный текст, без «Лектору», без описаний вёрстки,
без таймингов.

### Тронутые файлы

- `rendered/slides_band4.py` — `s37b`, `s38`, `s39`, `s40`.
- `rendered/slides_band1.py` — новая функция `s03b` (перед `s04`).
- `rendered/_helpers.py` — 2 записи в `URLS`, запись `SLIDE_REFS["s03b"]`,
  снятие §-ссылок из глоссы `SLIDE_REFS["s37b"]`.
- `rendered/build_lec04_v4.py` — вставка `b1.s03b`, ассерты 57 → 58.
- `rendered/gen_charts_r6b5.py` (новый) + `assets/charts/c03b-adoption.png`.
- `rendered/render_local.sh` (новый) — копия `render.sh` с путём этого
  worktree (у оригинала `REND` зашит на другой worktree и он бы перезаписал
  чужой PDF).
- `slides/s03b-industry-adoption.md` (новый).
- `slides/s37b-uber-kiro-dual-register.md`, `s39-risk-triad.md`,
  `s40-checklist.md`, `s41-bridge-qa.md` — видимое содержание + заметки
  приведены к рендеру (в этом раунде `.md` **синхронизированы**, в отличие
  от раундов 4–5, где правка была только визуальной).
- `deck.yaml` — запись s03b + `total_slides` 57 → 58.
- `rendered/lec-04.pptx` / `.pdf` — пересобраны, 58/58.
- `chapter*.md`, `speech.md`, `deck-part2.yaml`, слайды других блоков —
  **не тронуты**.

### Для assembly-прохода раунда 6

- Вставка s03b сдвигает **все** display-позиции начиная с бывшей p4 на +1.
  Блок 1 вставляет после p17, блок 3 удаляет p32 — по позициям не
  пересекаемся, но `deck.yaml`, `build_lec04_v4.py` и `_helpers.py` —
  общие файлы, конфликты слияния ожидаемы именно в них.
- `total_slides` в `deck.yaml` выставлен 58 **из расчёта только этого
  блока**; после слияния всех пяти блоков его нужно пересчитать, как и
  ассерты в `build_lec04_v4.py` (сейчас два: `len(builders)` и `n`).
- `deck-part2.yaml` строка `slides: 57` (в блоке totals) **не трогалась** —
  оставлена assembly-проходу, чтобы не плодить конфликт в файле, который
  правят другие блоки.
