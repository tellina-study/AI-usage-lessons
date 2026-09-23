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

---

## Round-6 Block 2 — пять слайдов инструментального блока (2026-09-23)

Issue #162, ветка `issue-162-lec04-block2-tooling`. Пять целевых слайдов —
p25 (s20b, skills), p26 (s20c, MCP), p27 (s20e, логирование задач),
p28 (s20d, git-конвенции), p30 (s20f, worktree). Никакие другие слайды не
трогались; `deck.yaml` / `deck-part2.yaml` не трогались; счёт слайдов
57 → 57.

### Состояние на момент возобновления (предыдущая сессия упёрлась в лимит)

Сессия была прервана лимитом использования на середине правки переполнения
текста. Восстановление по факту (`git diff` + рендер незакоммиченного
`lec-04.pptx`), а не с нуля:

| Слайд | Состояние, которое я застал | Что оставалось |
|---|---|---|
| p25 s20b | переписан целиком (три dev-скилла + блок «когда skill не нужен») | заголовок в 2 строки; перенос в буллетах терял висячий отступ; лишний воздух в сером блоке |
| p26 s20c | переписан целиком (подмножество API/CLI + риск→митигация) | грамматика заголовка; англицизмы (issues / pull request) |
| p27 s20e | переписан целиком (порядок по возрастанию сложности + трекер) | «pull request» без русского эквивалента |
| p28 s20d | переписан целиком (ЧТО ЭТО / ЗАЧЕМ ЭТО НУЖНО); **переполнение, на котором прервалась сессия, оказалось уже исправлено** — проверено рендером, а не по логу | русификация «pull request» |
| p30 s20f | **не тронут вообще** — исходный текстовый вариант round-2 | весь слайд |

Speaker notes всех пяти оставались старые (они грузятся из
`slides/*.md` через `load_notes`, то есть это живой вход рендера, а не
планировочный слой) — переписаны в этой сессии.

### p30 (s20f) — сначала поиск «примера посильнее», потом схема

Веб-поиск (13 запросов, 9 фетчей) отдельным агентом, затем самостоятельная
верификация двух находок через прямой фетч страниц:

- **claude-code #60295** (18.05.2026, closed as not planned) — две сессии
  Claude Code в **одном рабочем каталоге** на разных ветках; `git checkout`
  одной молча меняет рабочее дерево другой, в issue приложен reflog.
  Это ровно тот механизм, который объясняет схема.
- **claude-code #55724** (03.05.2026, closed as duplicate) — 13 параллельных
  агентов с `isolation: "worktree"`: 5 закоммитили, **8 потеряли
  несохранённую работу** на конкуренции за `.git/index.lock`; при 5 сессиях
  сбой изредка, при 10+ почти наверняка. Важно: это отказ **уже с
  worktree** — граница самого решения, а не аргумент за него.
- **Чего не нашлось (честно):** постмортема named-компании с часами/деньгами
  по этому классу отказа публично нет. `incident.io` описывает проблему
  («all your Claude conversations are stepping on each other in the same
  working directory»), но это блог «как мы работаем», без числа — как
  инцидент не подаётся. Кандидат с бóльшим числом часов (#18998, «8+ часов»)
  отвергнут: повреждается глобальный конфиг, а не рабочая копия git, и
  отчёт машинно-сгенерированный — выдавать его за «параллельные сессии над
  одним checkout» было бы натяжкой.

**Решение:** сделано и то, и другое, но носителем смысла стала схема
(как и просил владелец), а числа пошли подписями. `~2 часа` Лекции 2
демотированы до придаточного в подписи к левой панели.

Схема — две панели с **общей трёхрядной сеткой** (подписи рядов слева,
один раз на обе панели): СЕССИИ → ФАЙЛЫ В РАБОТЕ → ИСТОРИЯ `.git`.
Ряд 1 и ряд 3 в обеих панелях **намеренно одинаковые**; отличается только
ряд 2 — слева один общий блок, справа три отдельных (`/wt-a`, `/wt-b`,
`/wt-c`). Это и есть утверждение слайда, показанное геометрией: разводятся
файлы, история остаётся одна. Стрелки — `MSO_SHAPE.DOWN_ARROW` (локальный
хелпер `_down_arrow` в `slides_band2.py`, вертикальный аналог
`right_arrow` из `_helpers.py`), не линии.

### Итерации визуального цикла

**p30 (s20f) — 4 итерации**

- *iter 1* (собрал схему целиком): подписи под обеими панелями (3 строки при
  `h=0.50`) уезжали под нижнюю ленту карточек — «Курс потерял на» обрезано;
  в карточке команд последняя строка «дублируется.» вываливалась за рамку;
  список источников (стало 4 вместо 2) переносился на вторую строку и лез
  к номеру страницы. → сократил обе подписи, поднял ленту на `4.32`,
  перекомпоновал карточку команд.
- *iter 2*: подпись левой панели всё ещё в 3 строки — реальная ёмкость
  строки оказалась ~64 знака, а не ~75, как я считал. Убрал «reflog
  приложен» (уехало в notes), заменил «checkout одной сессии» на «одна
  сессия незаметно переключает» (заодно минус англицизм). Источники
  укоротил в `SLIDE_REFS` + `refs_of_slide(size=8.0)`.
- *iter 3*: чисто. Формулировка ряда 3 правой панели «та же одна история —
  **строка** не изменилась» двусмысленна (строка текста?) → «история та же
  — **этот уровень** не изменился».
- *iter 4*: полная пересборка деки + проверка на 50 % (ряд 5+ в аудитории) —
  схема читается целиком, подписи 9.5 pt курсивом на пределе, но разборчивы.
  5-сек-тест: считанное сообщение — «три сессии: слева общая папка, справа
  у каждой своя, история общая» = утверждение слайда. PASS.

**p25 (s20b) — 3 итерации**

- *iter 1* (застал от предыдущей сессии, проверил рендером): заголовок в
  2 строки — единственный такой среди четырёх соседей; перенос внутри
  буллета терял висячий отступ, и продолжение читалось как пятый пункт;
  «Пример:» почти касался золотой плашки. Ошибку первого взгляда на
  полном зуме («блок переполнен») **опроверг кропом** — текст был внутри.
- *iter 2*: заголовок в одну строку (20 pt), все четыре буллета укорочены
  до одной строки каждый, карточки подросли (`1.14 → 1.22`), убран
  дубль формулировки «просто скажите в чате» между буллетом и плашкой.
- *iter 3*: у серого блока осталось ~0.38″ пустоты снизу — заметно больше
  паддинга всех остальных блоков слайда, читается как недоделка →
  `h 1.72 → 1.56`. Проверка на 50 %: PASS.

**p26 (s20c) — 2 итерации** (слайд застал готовым, правки точечные)

- *iter 1*: грамматика заголовка — «убирает человека-мост**а**» (мост
  неодушевлённый, винительный = «мост»). Англицизмы: `issues`,
  `pull request` в теле.
- *iter 2*: «задачи, заявки на слияние (pull request), сборки»;
  «спрятанные в публичных **задачах** инструкции … через создаваемые
  **заявки на слияние**». Рендер: карточка GitHub MCP выросла до 4 строк,
  проверено — в рамку укладывается.

**p27 (s20e) — 2 итерации** (аналогично)

- *iter 1*: «1 окно контекста = 1 pull request» — англицизм, причём p27
  идёт в деке **раньше** p28, где термин глоссировался.
- *iter 2*: «1 окно контекста = 1 заявка на слияние» — переносится в
  2 строки, в ячейку (`row_h=0.58`) укладывается, проверено кропом.

**p28 (s20d) — 2 итерации**

- *iter 1*: переполнение «ЗАЧЕМ»-блоков, на котором оборвалась предыдущая
  сессия, **уже было исправлено** — подтверждено рендером (все три колонки
  внутри рамок, чипы 1.55″ не переполнены). Расхождение лога и факта
  разрешено в пользу факта.
- *iter 2*: перевернул глоссу вслед за p26/p27 — «**Заявка на слияние**
  (pull request)», а не наоборот: русский термин первым, английский в
  скобках при первом видимом употреблении.

### Speaker notes

Переписаны все пять (старые описывали прежнее содержание слайдов).
Связный читаемый текст для самостоятельного разбора, без режиссёрских
ремарок, тайминга и обращений к лектору:

| Слайд | слов |
|---|---|
| s20b | 255 |
| s20c | 262 |
| s20d | 262 |
| s20e | 263 |
| s20f | 280 |

Все в коридоре 150–300.

### Прочие затронутые файлы

- `_helpers.py` — два новых ключа в `URLS` (issues #60295 / #55724) и две
  новые записи в `SLIDE_REFS["s20f"]`; имя ссылки [1] укорочено, чтобы
  список из 4 источников лёг в одну строку. Больше в `_helpers.py` ничего.
- `slides/s20{b,c,d,e,f}-*.md` — секции `## Speaker notes` (живой вход
  рендера) + строки `assertion:` во frontmatter, приведённые в соответствие
  с переформулированными слайдами. Блоки `# Visible content` в этих файлах
  **не** синхронизировались — следую решению round-4/5 не чинить
  исторический дрейф планировочного слоя в рамках задачи по слайдам.
- `deck.yaml` / `deck-part2.yaml` / `chapter*.md` / `speech.md` — **не
  трогались** (вне задания).

### Pre-render greps (набор из CLAUDE.md), по пяти целевым слайдам

Прогон по свежей выгрузке из пересобранного `lec-04.pptx` (видимый слой и
speaker notes отдельно):

- Скаффолд (`[VERIFY-DAY-OF]` / `[FACT-CHECK]` / `LO[1-9]` / `§N.N` /
  `→ sNN` / `(sNN)` / «Вы здесь» / «Лектору» / «Преподавателю» /
  `[пауза]` / `[слайд]`) — **0** в видимом слое, **0** в notes.
- Тайминг (`\b[0-9]+\s*мин\b`, «Тайминг», «Время раздела», ⏱/⏰) —
  **0** и **0**.
- Методические мета-комментарии («методическ…», «педагогическ…»,
  «На этом этапе студент», «Зачем это в Лекции») — **0** и **0**.
- Оговорка про `[VFY-day-of]`: 7 вхождений в notes пяти слайдов и 50 по
  всей деке — это автогенерируемый блок «Источники:» (`notes_sources_block`
  помечает волатильные ссылки), конвенция деки, существовавшая до этого
  раунда. Новых меток раунд не добавил: обе новые ссылки s20f заведены
  неволатильными.

### Deep latin-token scan (`tools/presentation-build/deep_latin_scan.py`)

Видимый слой пяти слайдов: 121 вхождение / 93 уникальных токена.
Ни одного неглоссированного англицизма в нарративе. Разбор всех 93:

- **литералы кода и путей** (моноширинный/команды/примеры имён):
  `git worktree add --detach`, `cd`, `checkout -b`, `/wt-a`, `/wt-b`,
  `/wt-c`, `.git/index.lock`, `feat(auth)`, `fix(api)`,
  `claude/security-patch`, `ai/refactor-auth-flow`, `fix-final`,
  `notes/decisions.md`, `Backlog.md`, `notes/research/*.md`,
  `lint+type-check+test skill`, `testcontainers-docker skill`,
  `README Generator skill`, `ruff/mypy/pytest`, `eslint/tsc/vitest`;
- **имена продуктов и брендов:** AGENTS.md, SKILL.md, Agent Skills
  standard, Claude Code, Codex CLI, Cursor, GitHub MCP, Playwright MCP,
  Filesystem MCP, Postgres, Kafka, Jira, Linear, GitHub Issues,
  Conventional Commits / Conventional Branch, TodoWrite/Task*, arXiv;
- **заголовки источников в нижнем списке** (по критерию самого сканера
  допустимы): «Claude Docs — Skills», «Willison — the lethal trifecta»,
  «Destefanis — Authoring Agent Skills», «claude-code #60295/#55724» и др.;
- **термины-примитивы, глоссированные рядом по-русски:** `skill`
  (слайд рядом объясняет: «подгружается только когда задача релевантна»),
  `worktree` («своя папка каждой сессии» в шапке той же панели),
  `pull request` (теперь **только** как скобочная глосса после «заявка на
  слияние»), `Lethal Trifecta` («Смертельная тройка (Lethal Trifecta)»).

Speaker notes пяти слайдов (блок «Источники:» исключён как машинный):
32 вхождения / 22 уникальных — те же три категории, новых англицизмов нет.

### Проверка объёма правок

`git diff -U0` по `slides_band2.py`: все ханки внутри `s20b`…`s20f`.
По `_helpers.py`: только `URLS` и `SLIDE_REFS["s20f"]`. Пересборка —
57/57 слайдов, счёт не изменился.

---

## Round-6 Block 3 — кластер §4 «Тестирование» (issue #162)

Ветка `issue-162-lec04-block3-testing`, worktree `/tmp/lec04-block3-testing`.
Правки владельца по страницам 32 / 34 / 36 / 37 старой нумерации (57 слайдов).
Источник содержания — `chapter-part4.md` §4.2–§4.5.

**Отображаемая страница → builder → файл слайда** (нумерация yaml/builder
отстаёт от имён `.md` на 1 — исторический сдвиг v4.1, не трогали):

| стр. (было) | builder | slides/*.md | что сделано |
|---|---|---|---|
| 32 | `b3.s21` | `s22-anti-hype-benchmarks.md` | УДАЛЁН целиком |
| 34 → 33 | `b3.s23` | `s24-tdd-discipline.md` | рецепт из 5 шагов вместо констатации |
| 36 → 35 | `b3.s25b` | `s25b-bdd-trunk-based.md` | явные «+ / −» + микропримеры |
| 37 → 36 | `b3.s25c` | `s25c-test-tooling-matrix.md` | 5 категорий (+Playwright, +закрытый контур), строки «что делает / без него невозможно» |

Итог: **57 → 56 слайдов**, штамп «N / 56» пересчитан сборщиком автоматически.

### 1. Удаление страницы 32 («Бренд и бенчмарк-число ≠ инженерная дисциплина»)

Проверка на несущие связи перед удалением (grep по `rendered/*.py`,
`slides/*.md`, `deck*.yaml`, `speech.md`):

- **Ссылок вида «см. слайд N» на эту позицию нет** ни на одном слайде.
- **SWE-bench Verified/Pro** — введён в Лекции 3 (chapter-part4.md §4.3 прямо
  ссылается на это как на перекрёстную опору), в этой лекции остаётся одно
  упоминание на s38/risk-triad: «растёт с незнакомостью задачи (ось SWE-bench
  Pro)» — самостоятельная формулировка, не требующая удалённого слайда.
  ЗАФЛАЖЕНО сборочному проходу как единственная остаточная зависимость.
- **Вендор-скепсис** темы не теряет: остаётся s20 (70%-проблема с двумя
  выборками GitClear), s37 (триангуляция), s38 (risk-triad).
- **Devin 13,86% / OpenAI / Cursor Composer** — больше нигде в деке не нужны
  (упоминание «Composer (C)» на s07 — про лестницу автономности, независимо).
- `c21-swe-bench.png` и `band-mocking-spongebob.png` **оставлены в assets** —
  их использует EN-дек (`slides_band3_en.py`), который в этом блоке не трогали.

Что изменено: builder-вызов убран из `build_lec04_v4.py` (57→56) **и** из
`build_lec04_v4_pub.py` (41→40, иначе legacy-сборка падала бы), тело функции
`b3.s21` удалено, запись `SLIDE_REFS["s22"]` удалена, `slides/s22-anti-hype-
benchmarks.md` удалён, запись `- id: s21` удалена из `deck.yaml`.

`deck.yaml` / `deck-part2.yaml` (ЕДИНСТВЕННЫЙ блок раунда, который правит
общий файл — прочие блоки правят только содержимое своих слайдов):
`total_slides` 57→56, `version` v4.4→v4.5, `totals.slides` 57→56,
`slide_times_sum_min` 130.5→127.5, Р3-разбивка 30.5→27.5, `in_bucket_slides`
−s21 / `count` 21→20 / `share_by_slides` «21/47 ≈ 45%» → «20/46 ≈ 43%»
(порог 30% держится с запасом), из `verify_day_of_items` убран
`s21_swe_bench_numbers`, из `fact_check_items` — `s21_devin_openai_swe_bench`
(`s21_gitclear_2026_dataset` ОСТАВЛЕН: он про 70%-проблему, там display-
нумерация, а не builder-нумерация).

**Известный доставшийся дрейф, НЕ чинили:** поля `file:` в `deck*.yaml`
систематически отстают на 1 от реальных имён `slides/*.md` (напр. запись
`id: s23` указывает на `slides/s23-tdd-discipline.md`, а фактический файл —
`s24-tdd-discipline.md`). Починка этого — отдельная задача на весь файл,
не блок-локальная.

**Остаётся для сборочного прохода (вне рамок блока, зафлажено, не трогали):**
`speech.md` содержит секцию `## [s22] — Провал: бренд и бенчмарк ≠ дисциплина`
(+ упоминания в `[VFY-day-of]`-списке и в сводке strict-in), а EN-дек
(`slides_band3_en.py`, `slides-en/`, `deck.en.yaml`) по-прежнему 57 слайдов.

### 2. Страница 33 — TDD: рецепт вместо констатации

Запрос владельца: «если форсинг порядка агенту не работает, то что работает —
дай рецепт или лекарство». Источник — §4.2 (разведение ролей, red-green-
refactor с человеческим владением спекой, «проверка не аутсорсится»,
«инцидент → регресс-тест»), §4.3 (гейт по доле пойманных дефектов) и
deep-dive box (альтернатива форсингу — harness engineering).

Было: gold-плашка «Важный нюанс — структура ≠ ритуал» (лозунг, без действия).
Стало: компактная плашка «Что НЕ работает» (Böckeler: выигрыша нет, ~3×
токенов) + ДОМИНИРУЮЩИЙ блок «Что работает вместо — рецепт из пяти шагов»:

1. человек формулирует, ЧТО тест обязан утверждать (инвариант / критерий
   приёмки), до генерации кода;
2. порядок генерации оставлен агенту — тест и код вместе или код, а следом
   тест; форсить «сначала тест» не нужно;
3. утверждения теста читает человек: тест держится за поведение, а не за
   реализацию (Fowler [3]);
4. прогон — только детерминированный исполнитель (скрипт / CI с настоящим
   кодом возврата); «модель сказала: зелёные» — не прогон;
5. гейт — по доле реально пойманных дефектов, не по проценту покрытия;
   каждый инцидент → постоянный регресс-тест.

Шаг 5 намеренно НЕ называет «mutation score»: термин вводится на следующем
слайде, вперёд-ссылка была бы утечкой course-scaffold. Заголовок и gold-
callout переписаны под инвариант «не тест написан первым, а тест существует,
утверждает решённое человеком и прогнан машиной».

### 3. Страница 35 — BDD / trunk-based: явные «+» и «−»

Запрос владельца: «пояснить подробнее особенности + и − подходов… не понятно
для тех, кто первый раз видит». Источник — §4.4 целиком.

Структура каждой колонки теперь: определение → **микропример одной строкой**
(`Given слот свободен · When нажали «Забронировать» · Then слот занят` /
`ветку claude/fix-auth создали утром — влили до обеда, за флагом`) →
teal-блок «+ ЧТО ДАЁТ» → gold-блок «− ЧЕМ ПЛАТИТЕ». Плюс и минус — разные
блоки разного цвета, не проза; gold применён к «минусу» ОБЕИХ колонок
(правило «на каждой карточке или ни на одной»).

«~27%» получил базу прямо на слайде: «~27% проектов с открытым кодом, где
есть тестовый фреймворк (68% — Ruby)» — знаменатель назван, как требует
baseline-мандат. «Честная оговорка» про adoption, которая раньше была
приглушённой сноской, теперь полноценный «минус», как и просил владелец.

Заголовок переписан под новую структуру: «…что дают и чем платите».

### 4. Страница 36 — локальный инструментарий: +Playwright, +закрытый контур

Запрос владельца: «я хотел, чтобы тут был Playwright и что-то ещё… вместо
честной оговорки и готовым/сами напиши — когда и для чего нужен, что без него
сделать нельзя или трудно».

Было 3 колонки (БД / сеть / CI-цикл) со строками «что делает / честная
оговорка / готовым-самим». Стало **5 карточек** в сетке 3 + 2 (шестая ячейка
— teal-блок «Критерий выбора», чтобы нижний ряд не был полупустым — баланс
визуальной массы), у каждой две строки: **ЧТО ДЕЛАЕТ** и **БЕЗ НЕГО
НЕВОЗМОЖНО / ОЧЕНЬ ТРУДНО** — для ВСЕХ пяти, включая три старых.

Добавлены (обе — из §4.5 главы, не выдуманы):
- **Playwright** (категория «Интерфейс») — прямой запрос владельца; §4.5
  первым абзацем называет его как пример того же класса локального
  инструментария. Формулировка «без него» — собственный пример владельца:
  агент никогда не видит настоящий интерфейс, отладка фронтенда вслепую.
  На p26 (MCP-слайд, блок 2) Playwright остаётся как MCP-сервер — здесь он
  впервые предъявлен как **тестовая категория**, не дубль.
- **pytest-generator (Distil Labs)** (категория «Закрытый контур») — §4.5
  описывает его как полностью локальную генерацию тестов («runs entirely on
  your local machine»). Это единственная из названных главой сущностей,
  дающая ПЯТУЮ отдельную категорию (у WireMock категория та же, что у MSW —
  сеть, поэтому он остался внутри карточки MSW как не-JS-аналог).
  «Без него»: любая AI-генерация тестов = отправка исходного кода во внешний
  сервис; для закрытого контура это запрет, а не неудобство.

Честные оговорки не потеряны, но свёрнуты в ОДНУ приглушённую строку внизу
(мок-догадка MSW без реального примера ответа; AI-функции WireMock — в
платном WireMock Cloud, не в локальном ядре; ≈77% pytest-generator заявлены
вендором) — вместо двух строк матрицы, которые владелец просил убрать.

Ширина: 5 колонок в один ряд дали бы ~2,35″ и шрифт <10pt — вместо этого
сетка 3+2 с карточками 3,98″ (шрифт тела 10,5pt, как в остальном деке).
Это осознанный уход от «широкой матрицы», которую в прошлый раз пришлось
подрезать.

Новая иконка: `monitor` (Lucide, 4 варианта палитры) — сгенерирована через
`rsvg-convert` из `cdn.jsdelivr.net/npm/lucide-static`, лежит в
`assets/icons/monitor-{white,mid,teal,gold}.png`. Набор иконок деки не
меняется (Lucide).

### Визуальный цикл (Generate → Convert → Inspect → Fix)

Быстрый цикл: `build_blk3_test.py` + `render_blk3_test.sh` собирают ТОЛЬКО
3 правленых слайда (~8 с на итерацию против ~90 с на полный дек);
`render_blk3.sh` — полная сборка для финальной проверки. Снимки —
`snapshots/r6b3/` (gitignored).

| итер. | что смотрел | что менял | что стало проходить |
|---|---|---|---|
| i1 | все 3 слайда, первый рендер | — | структура верна на всех трёх; LibreOffice переносит текст шире расчёта |
| i1→i2 | переполнения | s23: gold-плашка 0,88→1,02, рецепт сдвинут, Fowler перенесён из левой плашки в шаг 3; s25b: тексты сжаты, блоки увеличены; s25c: заголовок в одну строку, карточки 2,28→2,42, «MSW (для не-JS — WireMock OSS)» → «MSW» | s25c: все блоки внутри границ |
| i2→i3 | остаточные наложения | s23: шаг 3 сокращён (3 строки → 2, перекрывал шаг 4); s25b: `boxh` 4,14→4,18, блоки «+/−» переразмерены; s25c: карточка 5 сокращена, формулировки «критерия выбора» согласованы с подписями категорий | s23 чист полностью |
| i3→i4 | s25b «− ЧЕМ ПЛАТИТЕ» вылезал за внешний бокс | 3 буллета вместо 2 длинных, «~27% OSS-выборки» → «~27% проектов с открытым кодом» (заодно русификация) | s25b: блоки внутри границ |
| i4→i5 | s25b для «тех, кто видит впервые» | добавлены микропримеры Given-When-Then и жизненного цикла ветки; заголовок под «+/−» | смысл читается без преподавателя |
| i5→i6 | строки-примеры переносились на 2-ю строку и обрезались | примеры сокращены до одной строки, заголовок до одной строки | s25b чист полностью |
| i6→i7 | русификация | «Цикл: Discovery → Formulation → Automation» → «обсудили примеры → записали сценарии → гоняем как тесты»; «Для не-JS — WireMock OSS» → «Вне JS — WireMock (открытый код)»; «в платном Cloud, не в локальном OSS-ядре» → «в платном WireMock Cloud, а не в локальном ядре с открытым кодом» | s25c чист полностью |

Итого реальных итераций: s23 — 4, s25b — 6, s25c — 7 (минимум 3 выдержан).

**5-секундный тест (после ≥3 итераций, на 150 dpi при 50% масштаба):**
- p33 — читается «форсить порядок не надо, есть рецепт из 5 шагов» = assertion. PASS.
- p35 — «две методики, у каждой плюсы и цена» = assertion. PASS.
- p36 — «пять слепых каналов агента и чем каждый закрыть» = assertion. PASS.

**Читаемость с задних рядов:** тело карточек 10,5–11pt, заголовки блоков
12–12,5pt, приглушённые строки 9,5pt (строка честных ограничений и строки-
примеры). 9,5–10,5pt — принятая в этой деке плотность (прежняя версия s25c
использовала 9,5pt в той же роли), ниже обще-курсового порога 12pt; отмечено
как осознанное отклонение ради 5 категорий на одном экране, не как недосмотр.

### Проверки перед сдачей

Grep по извлечённому видимому слою PPTX **и** по заметкам докладчика
(`python-pptx`, все 56 слайдов):

- scaffold (`Лектору` / `Вы здесь` / `[VERIFY-DAY-OF]` / `[FACT-CHECK]` /
  `LO[1-9]` / `§[0-9]` / `→ sNN` / `(sNN)` / «точка возврата» / «в материалах
  лекции» / «course-scaffold») — **0 на p32–p37**;
- тайминг (`N мин`, «Время раздела», «Тайминг», «Длительность», ⏱/⏰) —
  **0 по всей деке**;
- методические мета-комментарии — **0 на правленых слайдах** (2 попадания на
  p2 и p51 — доставшиеся, слово «методическая практика» как термин материала,
  не мета-комментарий, вне этого блока);
- висячие ссылки на удалённый слайд (`SWE-bench`/`Devin`/`13,86`/
  «контаминация») — **0**, кроме зафлаженного «(ось SWE-bench Pro)» на s38.

Latin-token scan по видимому слою правленых слайдов: остаются только
бренды и канонические термины (BDD/TDD/Given-When-Then/Testcontainers/MSW/
WireMock/Playwright/pytest-generator/Postgres/Kafka/Redis/Docker/HTTP/API/
DORA/Ruby/git/CI/Beck/Böckeler/Fowler/Willison/Qodo/Junie/AWS Q/Anthropic/
Stop-hook), все аббревиатуры с русским пояснением при первом появлении
(BDD — разработка через поведение; accessibility — дерево элементов
страницы; feature-флаги — включатели функций). Убрано в этом раунде:
Discovery/Formulation/Automation, OSS-ядро, «для не-JS».

Заметки докладчика: s24 — 243 слова, s25b — 267, s25c — 279 (все в 150–300),
связный студенческий текст, без описаний вёрстки и без реплик лектору.

### Затронутые файлы

- `rendered/build_lec04_v4.py` — 57→56, docstring v4.5.
- `rendered/build_lec04_v4_pub.py` — 41→40 (legacy-сборка не должна падать).
- `rendered/slides_band3.py` — `s21` удалён; `s23` / `s25b` / `s25c` переписаны.
- `rendered/_helpers.py` — удалена запись `SLIDE_REFS["s22"]`.
- `rendered/assets/icons/monitor-{white,mid,teal,gold}.png` — новые.
- `rendered/build_blk3_test.py`, `rendered/render_blk3_test.sh`,
  `rendered/render_blk3.sh` — инструменты цикла этого раунда.
- `rendered/lec-04.pptx` / `.pdf` — пересобраны, 56/56.
- `slides/s22-anti-hype-benchmarks.md` — удалён.
- `slides/s24-tdd-discipline.md`, `slides/s25b-bdd-trunk-based.md`,
  `slides/s25c-test-tooling-matrix.md` — видимый слой + заметки обновлены.
- `deck.yaml`, `deck-part2.yaml` — счётчики, доли, списки (см. §1).
- `chapter*.md`, `speech.md`, EN-дек — **НЕ трогали** (вне рамок блока).
