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
