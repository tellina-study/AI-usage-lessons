# Image Attribution — Лекция 4 deck (Round-5 memes)

Непубличная презентация (внутренний курс МГТУ). Требование по правам — только
эта таблица с указанием источника; на слайдах подписи-источники НЕ показываются
(та же конвенция, что в Лекции 2/3 — `lec-02/rendered/gen_memes_v33_r2.py`,
`lec-03/rendered/make_memes_v6.py`). Blank-шаблоны — с imgflip (top-100
`api.imgflip.com/get_memes`, id-подтверждены, direct image URL, без auth),
русские подписи запечены через PIL (`gen_memes_r5.py`), DejaVuSans-Bold,
классическая белая-с-чёрной-обводкой или тёмная-на-Ocean-панели вёрстка.

## Round-5 (issue owner ask, 2026-09-22) — реальные мемы вместо round-4 логотипов

Owner explicit correction: round-4's brand-logo corner badges (curl / AWS /
GitHub Copilot / Replit / Google Gemini / Uber) are NOT what "memes" means —
real internet memes (known template + custom caption) were requested, must
not overlap Лекция 2/3's already-used templates. See
`iteration-log.md` "Round-5" entry for full detail + exclusion-list
cross-check.

| локальный файл (композит) | слайд (page / builder fn) | мем-шаблон (imgflip id) | тезис | blank-источник | лицензия |
|---|---|---|---|---|---|---|
| `band-x-everywhere.png` (crop из `memes-src/x-everywhere.jpg`) | p18 · `slides_band2.s15` (поглощённый контекст / петля отравления) | X, X Everywhere / Buzz&Woody (id 91538330) | «плохой паттерн, плохой паттерн везде» — AI копирует плохой пример по всей кодовой базе, не отличая его от хорошего | `https://i.imgflip.com/1ihzfe.jpg` (2026-09-22) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `band-mocking-spongebob.png` (crop из `memes-src/mocking-spongebob.jpg`) | p32 · `slides_band3.s21` (анти-хайп бенчмарки, SWE-bench gap) | Mocking Spongebob (id 102156234) | mocking-case эхо вендорской цитаты на этом же слайде («Cursor: Composer "frontier, 4× быстрее"») | `https://i.imgflip.com/1otk96.jpg` (2026-09-22) | Imgflip meme template — fair use |
| `band-evil-kermit.png` (crop из `memes-src/evil-kermit.jpg`) | p40 · `slides_band3.s27` (провал ревью: благодушие + curl-slop) | Evil Kermit (id 84341851) | внутреннее искушение не читать diff и просто нажать Merge — прямая иллюстрация complacency-блока слева | `https://i.imgflip.com/1e7ql7.jpg` (2026-09-22) | Imgflip meme template — fair use |
| `band-domino-effect.png` (crop из `memes-src/domino-effect.jpg`) | p44 · `slides_band3.s30` (supply-chain: slopsquatting + CamoLeak) | Domino Effect (id 162372564) | одно галлюцинированное имя пакета запускает цепь эксплойта — каскадная эскалация | `https://i.imgflip.com/2oo7h0.jpg` (2026-09-22) | Imgflip meme template — fair use |
| `band-monkey-puppet.png` (crop из `memes-src/monkey-puppet.jpg`) | p22 · `slides_band2.s18` (постоянный слой инструкций / context rot) | Monkey Puppet (id 148909805) | отклонённое решение тихо исчезает из резюме при компакции — silent-failure юмор | `https://i.imgflip.com/2gnnjh.jpg` (2026-09-22) | Imgflip meme template — fair use |
| `band-hide-the-pain-harold-merged.png` (оба панели из `memes-src/hide-the-pain-harold.jpg`, склеены side-by-side) | p31 · `slides_band2.s20` (70%-проблема, «почти правильный код») | Hide the Pain Harold (id 27813981) | одно и то же лицо, одна и та же улыбка — шутка в том, что НИЧЕГО визуально не меняется, ровно как «почти правильный» код | `https://i.imgflip.com/gk5el.jpg` (2026-09-22) | Imgflip meme template — fair use |
| `band-boardroom-panel3.png` (панель 3 из `memes-src/boardroom-suggestion.jpg`) | p45 · `slides_band4.s31` (Replit culmination) | Boardroom Suggestion (id 1035805) | явная человеческая инструкция («БОЛЬШЕ НИКАКИХ ИЗМЕНЕНИЙ») игнорируется — агент продолжает как ни в чём не бывало. **Заменяет round-4's small Replit-logo badge** — swap, не addition (см. iteration-log) | `https://i.imgflip.com/m78d.jpg` (2026-09-22) | Imgflip meme template — fair use |

## Exclusion-list cross-check (обязательный, owner non-negotiable requirement)

Templates verified via `api.imgflip.com/get_memes` (top-100) + direct
directory listing of `lec-02/rendered/assets/web/*.jpg` +
`lec-03/rendered/assets/web/memes-src/*` + grep of both lectures'
`iteration-log*.md` "meme"/"мем" sections. Owner's own list (This Is Fine ·
Spider-Man Pointing · They're the Same Picture · Drake · Expanding Brain ·
Two Buttons · One Does Not Simply · Futurama Fry · Panik-Kalm-Panik · Trade
Offer · Woman Yelling at Cat · Disaster Girl · Distracted Boyfriend · Batman
Slap · Change My Mind · Yoda · Buff Doge vs Cheems · Roll Safe · Is This A
Pigeon · Gru's Plan · Always Has Been · Two Guys One Bus · Waiting Skeleton ·
Tuxedo Winnie the Pooh · Clown Applying Makeup · Left Exit 12 Off Ramp) was
found **incomplete** on independent re-check — directory listing additionally
surfaced: Math Lady/Confused Lady, Gandalf (token), Surprised Pikachu, Joker
Burning Money, Pepe Silvia (= "Charlie Conspiracy"), Spotlight, Well Yes
Actually No, Press X to Doubt. All of these (owner's list + the 8 additional
finds) were checked against the 7 Round-5 picks above — **zero overlap**.

## Round-4 logos (superseded reference — kept for traceability, NOT deleted)

Round-4's brand-logo badges remain in `assets/logos/*.png` and are still
used on s28(curl)/s30b(AWS)/s30(Copilot)/s37b(Uber+AWS)/s17b(Gemini) — see
`iteration-log.md` Round-4 entry for that table. Only the **Replit** badge
(s31/p45) was removed in Round-5, swapped for the Boardroom Suggestion meme
above. The other 6 round-4 logo placements were deliberately KEPT (not
swapped) — reasoning logged per-slide in iteration-log.md Round-5 §"kept
logos".
