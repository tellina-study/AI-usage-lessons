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

## Round-6 Block 4 — ревью + доставка/эксплуатация: 5 слайдов (2026-09-23)

**Scope (owner brief, 5 слайдов):** p40 `s27` (провал ревью) · p41 `s28`
(практика безопасности) · p45 `s31` (Replit-кульминация) · p47 `s33`
(вход в Раздел 6) · p48 `s33b` (множитель и IaC). Файлы-источники:
`slides_band3.py` (p40/p41), `slides_band4.py` (p45/p47/p48), `_helpers.py`
(реестр ссылок), 5 × `slides/*.md`. `deck.yaml` / `deck-part2.yaml` и любые
слайды вне этих пяти — не трогались.

**Процессная оговорка (честно):** этот раунд выполнен в ДВА захода. Первый
заход упёрся в usage-limit ровно на старте финальной верификации, успев
довести содержание всех пяти слайдов; второй заход (эта запись) НЕ принимал
результат первого на веру — заново собрал колоду из исходников, отрендерил
все пять страниц, осмотрел их как чужую работу, нашёл и починил четыре
дефекта (ниже), и только потом прогнал полный sweep. Счётчик итераций ниже —
только за второй заход; итерации первого захода в нём не учтены, чтобы не
приписывать себе непроверенную работу.

### Что сделано по каждому слайду

**p40 — третий кейс (главная содержательная правка раунда).** Было 2 кейса
(благодушие + curl-slop), макет 2 колонки. Стало 3 колонки: добавлен кейс
«не прирост, а перераспределение» — Xu и др., arXiv 2510.10165. Все три
колонки теперь читаются как три проявления ОДНОГО механизма (AI снял
ограничитель на объём, стоимость проверки осталась прежней) — это и вынесено
в gold-callout вместо прежнего «AI не сделал спам злее».

**Верификация цитаты (нулевая терпимость к выдуманным цифрам, прецедент
round-3 с GitClear).** Источник проверен независимо, не по пересказу:

| Утверждение на слайде | Что говорит статья | Статус |
|---|---|---|
| Xu, Medappa, Tunc, Vroegindeweij, Fransoo | те же пять авторов | ✅ |
| 2 755 репозиториев | «consists of 2,755 repositories» | ✅ |
| 1 699 участников | «1,699 contributors from GitHub» | ✅ |
| 12 мес до и после | «12 months before and 12 months after» | ✅ |
| периферия +43,5% коммитов | «increased their commit activity by 43.5%» | ✅ |
| периферия +17,7% PR | «submitted 17.7% more PRs» | ✅ |
| ядро = топ-25%, периферия = 75% | «core contributors (top 25%) and peripheral contributors (rest 75%)» | ✅ |
| ядро −19% своих коммитов | «core contributors reduced their commit activity by 19%» | ✅ |
| ядро +6,5% ревью чужого | «review 6.5% more code after Copilot's introduction» | ✅ |
| доработка PR +2,4% | «experienced 2.4% … more code rework» | ✅ |

10 из 10 дословно. Название: «AI-Assisted Programming Decreases the
Productivity of Experienced Developers by Increasing the Technical Debt and
Maintenance Burden», v1 11.10.2025, v3 28.01.2026.

**Это НЕ METR, и на слайде это не выдаётся за METR.** Owner просил «METR или
эквивалентное строгое исследование». METR-RCT (он уже несущий на s01) меряет
другое — замедление опытного разработчика на задаче. Здесь панельное
исследование до/после по 2 755 репозиториям меряет перераспределение объёма
работы. Оба дают «−19%», и это РАЗНЫЕ −19%; в speaker notes разведение
сделано явной фразой, чтобы студент не склеил две цифры.

**p41 — упрощение + расшифровка всего.** С видимого слоя убран вторичный ряд
вендоров (GitHub CodeQL/Autofix/Dependabot · Google Big Sleep/OSS-Fuzz ·
AWS Q · Anthropic /security-review) — он переехал в speaker notes, где его
по-прежнему держит ссылка [3]. Освободившееся место отдано под расшифровку
КАЖДОГО термина прямо на слайде, а не отдельной плашкой-словариком:
least-privilege → наименьшие привилегии · sandbox → изолированное окружение ·
egress-allowlist → белый список получателей · SAST → static application
security testing → статический анализ кода до запуска · secret-scanning →
поиск утёкших ключей и токенов · SCA → software composition analysis →
проверка сторонних библиотек · supply-chain → цепочка поставок · egress →
канал наружу · prompt injection → подмена инструкции через прочитанный текст.

**p45 — «95» и «9 секунд».** Прежняя gold-плашка «"95/100" при худшем
результате · "9 секунд"» не читалась без сверки с другим слайдом по памяти:
9 секунд относятся к ДРУГОМУ инциденту (PocketOS/Cursor). Плашка убрана.
Число 95 расшифровано на месте — «оценка, которую агент поставил сам себе за
тот самый прогон, где стёр базу и солгал», в блоке «почему отчёт агента ничего
не доказывает». «9 секунд» осталось только внутри блока-эха и явно помечено
как отдельный инцидент. Правая колонка перестроена из трёх параллельных опор
в причинную цепочку сверху вниз: что произошло → почему запрет не сработал →
почему отчёт ничего не доказывает → что бы это остановило.

**p47 — один тезис на входе в раздел.** Было 6+ равноправных идей. Стало:
порядок инвестиций (сначала зрелость, потом AI) как двухшаговая фигура, DORA-
пара (+7,5% / −7,2%) как её доказательство. Семь способностей доставки НЕ
перечисляются полностью — названы числом с четырьмя примерами. Три прежние
равноправные врезки (риск-калиброванный гейт · «потребляет, но не владеет» ·
эксплуатация — слабейшая фаза) демотированы в один приглушённый абзац: они
нужны дальше по разделу, но не конкурируют с несущим тезисом.

**p48 — назван механизм.** Было два факта рядом под общей шапкой «множитель»
без объяснения связи (ровно это owner и спросил: «в чём проблема? больше
выкаток?»). Теперь обе колонки отвечают на одну и ту же пару вопросов в
одинаковых белых врезках — «Что умножает AI» и «Где гейт» / «Гейта нет».
Видно, что множитель ОДИН И ТОТ ЖЕ (объём × скорость), различается только
зрелость гейта: слева умножается уже проверенный шаг (runbook задаёт
допустимые действия, телеметрия показывает результат), справа — непроверенный
артефакт (конвейер проверяет синтаксис, а не безопасность → больше
конфигураций → меньше внимания на каждую → небезопасное доезжает до прода).
Сверено с `chapter-part5.md` §6.1–§6.2: формулировка «ограничение прав
защищает от действий агента, но не от содержания артефакта» — из книги.

### Итерации второго захода (Generate→Convert→Inspect→Fix)

**Iter 1 — осмотр как чужой работы.** Пересборка из исходников (57/57),
рендер p40/p41/p45/p47/p48 @150dpi, визуальный осмотр каждой.
Найдено 4 дефекта (все — в работе первого захода, ни один не был отмечен
в его самоотчёте):

- **D1 (P1, p48, регресс):** из видимого слоя пропал разделитель между ~55%
  и 8,4%. Раньше стояло «отдельное измерение, не тот же тренд»; без него два
  числа про безопасность стоят рядом и читаются как противоречие. Книга
  (`chapter-part5.md` §6.2) говорит именно «в **отдельном** 2026-бенчмарке».
- **D2 (P1, 5 × .md):** секции `# Visible content` во всех пяти .md остались
  от старых макетов — первый заход обновил только `## Speaker notes`.
  Заметки — живой источник (билдер читает их из .md), видимый слой — нет,
  поэтому расхождение не влияет на рендер, но .md по CLAUDE.md числится
  source-of-truth и его читают text-only-критики.
- **D3 (P2, p48):** hero-число подписано по-английски — «~55% secure-by-
  default», при том что строкой ниже уже стоит русская расшифровка.
- **D4 (P2, p47 + заметки):** «delivery-способностей». В `speech.md` (стр.
  540) зафиксировано собственное решение курса по этому самому термину:
  `delivery-способности` → «способности доставки». То есть это не стилистика,
  а расхождение с уже принятым решением.

**Iter 2 — правка D1/D3/D4 + пересборка + рендер p47/p48.** D1: «Отдельный
бенчмарк 2026 года, другое измерение: 8,4% на задачах с проверкой
безопасности» (2 строки, вписалось без переполнения). D3: «~55% безопасны по
умолчанию», расшифровка ниже дополнена «без правок человека», чтобы «из
коробки» не дублировалось. D4: «четыре из семи способностей доставки, которые
выделяет DORA» — на слайде и в заметках. Осмотр: переполнений нет, врезки не
наехали друг на друга.

**Iter 3 — англицизмы в блоке «Источники» + финальная пересборка.** Блок
«Источники:» дописывается в заметки из `SLIDE_REFS` в `_helpers.py`, то есть
это тоже видимый студенту текст, и туда deep-scan первого захода не заглядывал.
Исправлено в глоссах ТОЛЬКО пяти своих слайдов: `+170% issues` → «замечаний»
(s28) · `egress` → «канал наружу» (s29) · `curated-кейсы` → «отобранные
кейсы» (s29) · `first-party источник` → «источник первой стороны (сама
Microsoft)` и `time-to-engage` → «время до подключения дежурного» (s33b) ·
`IaC secure-by-default` / `security-filtered` → русские формулировки (s33b) ·
`+throughput` → «рост пропускной способности» (s34). Пересборка 57/57, рендер
всех пяти, финальный sweep.

D2 (ресинк `# Visible content` в пяти .md) выполнен отдельно от рендер-цикла —
он на картинку не влияет.

### Sweep на собранном PPTX (видимый слой + speaker notes, 5 слайдов)

Проверялось на реально собранном `lec-04.pptx` через извлечение текста из
шейпов и notes-frame, а не по исходникам.

| Проверка | Результат |
|---|---|
| Scaffold («Лектору» / «Вы здесь» / VERIFY-DAY-OF / FACT-CHECK / LO-коды / §X.X / → sNN / «точка возврата» / «в материалах лекции» …) | **0** |
| Timing (`N мин`, «Время раздела», «Тайминг», «Длительность», ⏱, ⏰) | **0** |
| Методология («методическ\*» / «педагогическ\*» / «на этом этапе студент» / «зачем это в Лекции» / «Преподавателю» …) | **0** |
| Длина speaker notes (норма 150–300 слов) | p40 **284** · p41 **289** · p45 **277** · p47 **270** · p48 **273** — все в норме |
| Слайдов в колоде | **57** (без изменений) |

**Deep latin-token scan** (`tools/presentation-build/deep_latin_scan.py` +
полный ручной разбор всех уникальных токенов, не только top-50, который
инструмент печатает по умолчанию). Видимый слой пяти слайдов: **102
уникальных латинских токена**, и после классификации остаток вне разрешённого
— **∅**. Разбивка:

- **Имена собственные / бренды / названия кейсов:** Google, Microsoft, Azure,
  BT Group, Replit, Amazon, Kiro, Cursor, PocketOS, GitHub, Copilot,
  HackerOne, curl, matplotlib, Terraform, Kubernetes, Fortune, The Register,
  Thoughtworks, Radar/Hold, Triangle, CodeCrash, SWR-Bench, Rubber-Stamp
  Collapse, TianPan.co, incident.io, Big Sleep, OSS-Fuzz, Willison, Fowler,
  Xu, Stenberg, arXiv, DORA.
- **Названия цитируемых работ** (остаются на языке оригинала, как принято в
  ссылках): «Complacency with AI-generated code», «Exploring Gen AI»,
  «the lethal trifecta», «matplotlib hit-piece».
- **Термины с русской расшифровкой на ТОМ ЖЕ слайде** (это и есть предмет
  правки p41, а не недосмотр): least-privilege, sandbox, egress-allowlist,
  egress, SAST + static application security testing, secret-scanning, SCA +
  software composition analysis, prompt injection, MTTR + mean time to repair,
  time-to-engage, runbook, IaC, code-freeze, accountability, production, SRE.
- **Команды и устоявшиеся сокращения:** gh / aws / gcloud, PR, LLM, DDoS, F1,
  vibe-coding, issue.
- **Хайп-ярлык в кавычках, который слайд отвергает:** «AI-CD/ops-продукт».

Снято этим раундом (было в видимом слое / заметках до правок, стало 0):
`secure-by-default`, `security-filtered`, `delivery-способностей`,
`first-party`, `curated-`, `critical-находок`, `throughput`, `+170% issues`.

### Открытые находки — ОТЧЁТ, не правил

1. **`[VFY-day-of]` в speaker notes — 50 вхождений на 34 слайдах колоды**
   (из них 9 на четырёх моих). Это осознанная общеколодная конвенция из
   прежних раундов: `_helpers.py` дописывает маркер в заметки для ссылок,
   помеченных `volatile`. Формально это scaffold-маркер в тексте, который
   видит студент (Pre-USER-GATE §5 требует 0 в visible body И в
   speaker_notes), но написание `[VFY-day-of]` не ловится стандартным
   паттерном `\[VERIFY-DAY-OF\]` — поэтому в прежних прогонах он не всплывал.
   **Не трогал:** править его на пяти слайдах из тридцати четырёх — значит
   развалить конвенцию; это решение уровня всей колоды.
2. **`slides/*.md` ↔ `slides_band*.py` — общеколодный дрейф.** Round-5 явно
   зафиксировал, что .md — планировочный слой, разошедшийся с настоящим
   источником рендера, и сознательно его не чинил. Этот раунд ресинкнул
   `# Visible content` ТОЛЬКО для своих пяти слайдов; остальные 52 остаются
   как были. Полный ресинк — отдельная задача.

### Тронутые файлы

- `rendered/slides_band3.py` — `s27` (p40) перестроен 2→3 колонки;
  `s28` (p41) упрощён и расшифрован.
- `rendered/slides_band4.py` — `s31` (p45) причинная цепочка; `s33` (p47)
  один тезис; `s33b` (p48) назван механизм.
- `rendered/_helpers.py` — новый URL `oss_review_burden` + ссылка [6] для
  s28; русификация глоссов в `SLIDE_REFS` для s28/s29/s33b/s34.
- `slides/s28-…`, `s29-…`, `s32-…`, `s33b-…`, `s34-….md` — speaker notes +
  ресинк `# Visible content`; у s28 обновлены `assertion` / `references` /
  `visual_brief` под третий кейс.
- `rendered/render_b4.sh` (новый) — рендер-хелпер, укоренённый в ЭТОМ
  worktree (у `render.sh` путь зашит в worktree round-5 и здесь не работает).
- `rendered/lec-04.pptx` / `.pdf` — пересобраны, 57/57.
- `deck.yaml` / `deck-part2.yaml` / `chapter*.md` / `speech.md` — **не
  трогались**.
