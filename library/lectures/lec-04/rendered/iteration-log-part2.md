# Iteration Log — Лекция 4, Part 2

`iteration-log.md` (part 1) is already at 1083 lines (pre-existing, over the
CLAUDE.md 600-line doc-size limit before this round touched it) — continuing
here per the lec-03 precedent (`iteration-log-part2.md`) rather than growing
part 1 further.


<!-- Навигация по журналу итераций Лекции 4 -->
| Файл | Что внутри |
|---|---|
| `iteration-log.md` (part 1) | v4-переспина (40 слайдов), окружение/тулчейн, раунды 1–4 |
| `iteration-log-part2.md` (part 2) | Round-5 (мемы) · **Round-6 блок 1** (контекст/инструкции) |
| `iteration-log-part3.md` (part 3) | **Round-6 блок 2** (инструментарий) · **блок 3** (тестирование) |
| `iteration-log-part4.md` (part 4) | **Round-6 блок 4** (ревью + доставка) · **блок 5** (закрытие) |
| `iteration-log-part5.md` (part 5) | **Round-6 сборочный проход** — слияние пяти веток + сквозная проверка колоды |

Файлы разбиты по лимиту 600 строк на документ (CLAUDE.md § Document Size
Limit). Хронология сквозная: part 1 → part 2 → … → part 5.

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

## Round-6 Block 1 — кластер «контекст/инструкции» по замечаниям владельца (2026-09-23)

Изолированный worktree `/tmp/lec04-block1-context`, ветка
`issue-162-lec04-block1-context`. Параллельно ещё 4 блока правят ДРУГИЕ
слайды в своих копиях — трогались **только** 4 цели ниже, ничего «попутно»
не чинилось (в том числе замеченный, но чужой дефект переноса
«последстви/я» в ячейке ADR на p17 — оставлен как есть).

**Архитектурная заметка (как в round-4/5):** настоящий источник рендера —
функции в `slides_band*.py`; `slides/*.md` — планировочный слой, местами
дрейфующий. Правились `.py` (источник) и зеркалились `.md` там, где есть
чистое соответствие. Отображаемые страницы ↔ функции (проверено рендером,
не по памяти): p17=`b2.s14`, p22=`b2.s18`, p23=`b2.s18b`, p24=`b2.s19`.
После вставки нового слайда: p18=`b2.s14b`, p23=`b2.s18`, p24=`b2.s18b`,
p25=`b2.s19`. Дек 57 → **58** слайдов.

### 1. НОВЫЙ слайд `s14b` (позиция p18, сразу после матрицы четырёх практик)

Запрос владельца: «слайд 17 — после него ещё один слайд с примерами
артефактов/инструкций по каждому типу, чтобы заземлить и пояснить».

Имя выбрано по уже установленной в этом деке конвенции вставок
(`s09b`/`s11b`/`s17b`/`s18b`/`s20b`–`s20g`/`s25b`/`s30b`/`s33b`/`s35b`):
новая функция называется по ИМЕНИ ПРЕДШЕСТВУЮЩЕЙ функции + суффикс, файл
слайда и ключ `SLIDE_REFS` — тем же именем. Отсюда `s14b` (а не `s15b`):
предыдущий слайд строит функция `b2.s14`. Коллизии glob'а нет:
`load_notes("s14")` ищет `s14-*.md`, а не `s14b-*.md`.

Содержание — реальные фрагменты артефактов из `chapter-part2.md`
§2.2–§2.5, не выдуманные плейсхолдеры: скелет ADR (контекст · решение ·
статус · последствия, формат Найгарда), два теста-инварианта
(направление зависимостей «оплата не зависит от UI» + бюджет 200 мс —
оба примера названы в §2.3 дословно), Structurizr-DSL для C4 (§2.4
называет именно PlantUML/Mermaid/Structurizr) и конвейер-гейт для
четвёртой колонки. Про четвёртую колонку честно: у эволюционной
архитектуры **своего** артефакта нет — §2.5 описывает её как сборку трёх
предыдущих «с максимумом автоматизации», поэтому показан CI-шаг, который
прогоняет все три вместе. Визуально слайд намеренно повторяет шапки,
иконки и цвета предыдущего — связь «то же самое, но файлами» читается
без подписи.

- **iter 1** — заголовок в 58 символов свернулся в 2 строки и наехал на
  подзаголовок; в колонке ADR последняя строка сниппета упиралась в
  границу белой коробки (запас 0,015in). Замерил по рендеру фактическую
  ширину символа (0,2167 in/симв. при 24pt) → предел 56 символов, а не
  «на глаз».
- **iter 2** — заголовок сокращён до 51 символа (одна строка), высота
  коробки со сниппетом 1,86 → 1,96in, `assert p95(...) < 200` собран в
  одну строку (33 симв. ≤ 36 при 8,5pt).
- **iter 3** — в ADR добавлен counterfactual к «2 с» («вместо
  мгновенного» — база к измеримой величине, § Baseline Mandate), из
  подписи C4 убраны «диффается/ревьюится» подряд (русификация), хвост
  YAML-сниппета переписан на «красный шаг блокирует / слияние изменений».
- **iter 4** — моноширинный кегль поднят 8,5 → **9pt** ради задних рядов:
  пересчитал самую длинную строку каждого сниппета (max 33 симв. при
  лимите 34) — влезает; шаг строки 0,175 → 0,186, геометрия пересобрана.
- **iter 5 (in situ)** — полный ребилд 58/58, рендер настоящей p18 со
  штампом страницы: переполнений нет, соседние p17/p19 не задеты.

5-секундный тест: «у каждой из четырёх практик есть файл в репозитории с
примером» = утверждение слайда. PASS.

### 2. p22 → p23 (`b2.s18`) — переструктурировано по УРОВНЯМ

Запрос владельца: «не понятно — структурировать по уровням контекста/
памяти, заземлить на разработку или убрать; пояснить, что такое JIT;
упомянуть практики распределения контекста по документации/репозиторию».

Диагноз подтверждён рендером до правки: подзаголовок обещал «четыре
смежных, но разных понятия», а тело показывало совсем другое — ряд
«разработчик ↔ репозиторий → агент», отдельную коробку курирования и
плашку context rot; ни одного из четырёх понятий как уровня на слайде не
было, JIT висел голой плашкой без определения.

Стало: четыре явные горизонтальные полосы ровно по карте §3.2
`chapter-part3.md` — (1) постоянные инструкции, (2) контекст одной
сессии, (3) операционная история задач, (4) память-слот-1. В каждой
полосе три зоны: кто ведёт + срок жизни · что это · **конкретный пример
из разработки** (`AGENTS.md` с дословной командой `pnpm test` ·
определение JIT · разбор инцидента с датой и статусом · Mem0/Cognee/
Graphiti/Letta). JIT-извлечение определено прямым текстом: «агент
открывает нужный файл в тот момент, когда задача его потребовала, а не
грузит весь репозиторий заранее». Справа — колонка «Что куда класть в
репозитории» (README · AGENTS.md · ADR · комментарий в коде · разбор
инцидента), которой раньше не было вообще. Context rot и база
~172k/~334k сохранены отдельной teal-плашкой как обоснование уровня 2 (а
не как самостоятельный блок ни к чему). Мем Monkey Puppet из round-5
оставлен на месте, координаты не трогались.

Слияние двух слайдов в один рассматривалось (владелец допускал «или
убрать») и отклонено: после перестройки p23 и p24 стали строго
параллельными (уровни ↔ пределы уровней), и это само по себе несущая
часть объяснения — один слайд на восемь блоков был бы плотнее любого
существующего в деке.

- **iter 1** — заголовок в 2 строки на подзаголовке; подзаголовок обрезан
  справа; строка «кто ведёт» вылезала под рамку в 4 полосах из 4; текст
  зоны «что это» переполнял полосы 1, 3, 4; третья строка нижней плашки
  и правая колонка тоже переполнялись.
- **iter 2** — заголовок 54 симв. (одна строка), подзаголовок 128 симв.
  (одна строка), все «кто ведёт» ужаты до ≤28 симв., тексты зон обрезаны
  под лимит 4 строк (замерено: 35 симв./строка при 9,5pt на 3,00in),
  полосы 0,84 → 0,86 с шагом 0,06, правая колонка — запись «комментарий
  в коде» сокращена с 3 строк до 2. Переполнений не осталось.
- **iter 3** — «кто ведёт» поднято на 0,03in от нижней грани; шаг записей
  правой колонки 0,52 → 0,545, чтобы не оставлять пустого низа (баланс
  визуальной массы).
- **iter 4 (in situ)** — рендер настоящей p23: мем, список источников и
  штамп страницы не пересекаются.

### 3. p23 → p24 (`b2.s18b`) — пределы ПО ТЕМ ЖЕ уровням

Было 3 карточки вперемешку (компакция / JIT / несвежий AGENTS.md).
Стало 4 карточки в том же порядке и тех же цветах, что уровни на
предыдущем слайде: предел уровня 1 (устаревший файл хуже отсутствия,
с режимом отказа «команда сборки, которую давно заменили»), уровня 2
(компакция теряет молча ↔ JIT не спросит о неизвестном — §3.2 сам
называет их двумя сторонами одного компромисса, поэтому они в одной
карточке), уровня 3 (архив стареет тише одного файла) и уровня 4
(память закрепляет ошибочный вывод, если её читает только сам агент —
§3.2 «проверяют на entrenchment» + §3.3d). Четвёртая карточка — новая:
предела уровня 4 на слайде раньше не было вовсе.

- **iter 1** — заголовок в 2 строки; в карточке 1 заголовок занял 3
  строки и вытолкнул тело за рамку; тело карточки 3 упиралось в границу.
- **iter 2** — заголовок 58 симв. (одна строка), заголовки карточек
  приведены к 2 строкам (замерено: ~21 симв./строка при 12,5pt bold).
  Остался клип последнего слова в карточках 1 и 3.
- **iter 3** — измерил фактический шаг строки по рендеру: **0,18in**, а
  не расчётные 0,153 (LibreOffice добавляет ascent/descent). При высоте
  1,74in это 9 строк максимум — тексты карточек 1 и 3 ужаты ровно до 9.
  Клипа нет.
- **iter 4 (in situ)** — рендер настоящей p24, чисто.

### 4. p24 → p25 (`b2.s19`) — расшифровка SAST и least-privilege

Запрос владельца прямой: «расшифровать sast, least-priveledge». Оба были
голыми ярлыками плашек; раскрывались только на p41, то есть на 16
слайдов позже первого появления. Полный аудит акронимов round-3 счёл
SAST «в пределах словаря аудитории» — владелец это суждение для данного
слайда отменил явно, правило README §5.8b применено.

Место нашлось без переверстки: между второй строкой плашек и золотым
кругом «МОДЕЛЬ» было ~0,30in пустоты. Ряды плашек подняты на 0,06in и
уплотнены (шаг 0,56 → 0,52), в освободившуюся полосу вписана компактная
строка-глосса 9,5pt курсивом (цвет MID).

- **iter 1** — глосса в 160 симв. легла в 3 строки и третьей упёрлась в
  верх круга «МОДЕЛЬ».
- **iter 2** — по замеру фактической ширины (≈72 симв./строка при 9,5pt
  курсив на 5,49in) текст сокращён до 136 симв. → ровно 2 строки, низ на
  3,00in против верха круга 3,02in.
- **iter 3 (in situ)** — рендер настоящей p25: две строки, коллизий нет.

«sandbox» намеренно **не** глоссирован: в задании его нет, а добавлять
сверх задания запрещено (No Extra Content Rule).

### Проверки перед сдачей

Греп по 4 затронутым `.md` (тело + speaker notes, frontmatter исключён) и
**отдельно** по извлечённому тексту готового PPTX (видимый слой + заметки
страниц 18/23/24/25):

- scaffold-маркеры (`[VERIFY-DAY-OF]`, `[FACT-CHECK]`, `LO[1-9]`,
  `§N.N`, `→ sNN`, `(sNN)`, «Вы здесь», «Лектору») — **0** в теле и
  заметках. В `.md` 9 совпадений, все во frontmatter (`learning_outcomes`,
  `chapter_ref`, `learning_goal`, `visual_brief`) — по правилу исключены.
- тайминг (`\d+ мин`, «Тайминг», «Длительность», ⏱/⏰) — **0**.
- методические мета-комментарии (`методическ*`, `педагогическ*`, «на этом
  этапе студент», «зачем это в Лекции») — **0**.
- длина speaker notes: p18 — 247 слов, p23 — 271, p24 — 272, p25 — 288
  (без блока «Источники:»). Все в коридоре 150–300.
- глубокий скан латиницы (`tools/presentation-build/deep_latin_scan.py`)
  по видимому слою и заметкам этих страниц: 66 уникальных токенов, разбор
  поштучно — код и пути внутри сниппетов (`def`, `assert`, `workspace`,
  `pytest`, `docs/adr`, `pnpm` и т.д.), имена собственные и бренды
  (Thoughtworks, Chroma, Willison, Structurizr, Mem0/Cognee/Graphiti/
  Letta, README, AGENTS.md), словарные термины дека (ADR, C4, DSL, JIT,
  fitness-функция) и заголовки источников в списке ссылок. Новых
  англицизмов в повествовательном тексте не добавлено; наоборот, из
  подписи C4 убраны «диффается/ревьюится» подряд, а SAST и
  least-privilege теперь расшифрованы. Токены `guardrails`, `evals`,
  `merge`, `pull request` в заметках p25 — существующий текст, не
  затронутый этой правкой.

### Затронутые файлы

- `rendered/slides_band2.py` — новая функция `s14b`; `s18` и `s18b`
  переписаны целиком; в `s19` добавлена строка-глосса и уплотнены ряды
  плашек. Другие функции не трогались.
- `rendered/_helpers.py` — одна новая запись `SLIDE_REFS["s14b"]`
  (Найгард · Thoughtworks fitness function · Браун C4/Structurizr ·
  Форд/Парсонс/Кюа). URL берутся из существующего реестра, новых не
  придумано.
- `rendered/build_lec04_v4.py` — `b2.s14b` вставлена между `b2.s14` и
  `b2.s15`; оба `assert` 57 → 58; шапка-docstring обновлена до v4.5.
- `slides/s14b-architecture-artifacts.md` — новый.
- `slides/s19-persistent-memory-layer.md`, `slides/s18b-curation-limits.md`
  — тело и заметки перезаписаны под новую структуру, `type` у первого
  сменён на `schema_layered`.
- `slides/s20-harness-gate.md` — добавлена строка-глосса + пункт в
  `visual_brief`.
- `deck.yaml` — новая запись `s14b`; у `s18`/`s18b` обновлены
  `assertion`/`learning_goal`/`type`; `total_slides` 57 → 58;
  `version` v4.4 → v4.5.
- `deck-part2.yaml` — `totals.slides` 57 → 58, `slide_times_sum_min`
  130,5 → 133,5, дополнен `base_slides_locked`.
- `rendered/lec-04.pptx` / `lec-04.pdf` — пересобраны, 58/58.

**ВНИМАНИЕ СБОРЩИКУ.** `deck.yaml` / `deck-part2.yaml` / `_helpers.py` /
`build_lec04_v4.py` — общие файлы. Блок 1 единственный добавляет слайд,
поэтому только он меняет счётчики (57→58) и список сборки; остальные
блоки round-6 правят содержимое существующих слайдов. При слиянии
счётчик слайдов надо брать из этой ветки, а правки содержимого — из
остальных. Номера страниц после p17 сдвинуты на +1: то, что другие блоки
называют pNN при NN > 17, здесь pNN+1.

`lec-04-notes.pdf` **не** перегенерирован — его пересборка делается один
раз после слияния всех блоков, иначе пять веток перезапишут один бинарник.
