# Image Attribution — Лекция 3 deck v6 (dividers + memes)

Непубличная презентация (внутренний курс МГТУ). Требование по правам — только
эта таблица с указанием источника; на слайдах подписи-источники НЕ показываются
(включая мемы). Английские baked-in подписи мем-шаблонов обрезаны/перекрыты
русскими подписями в мем-стиле.

## v6.1 — мемы по всему деку (issue #185, owner: «а где мемы по тексту? почему только там где явно просил?»)

Owner-фидбек: мемы распределить по содержательным текстовым слайдам, а не только
на 4 явно запрошенных. Мем с мозгом (Expanding Brain) заменён (owner: «мем с
мозгом был уже»). Все blank-шаблоны — из imgflip API (`get_memes`),
id-подтверждены. Русские подписи наложены через PIL (`make_memes_v6.py`); там,
где у шаблона есть baked-in английская подпись, она перекрыта белым и переписана
по-русски. На слайдах со схемами / таблицами / чартами мемы НЕ добавлялись
(сохранён исходный визуал — сознательный баланс серьёзности).

| локальный файл (композит) | слайд | мем-шаблон (imgflip id) | тезис | blank-источник | лицензия |
|---|---|---|---|---|---|
| `s05-gru-ru.png` (из `memes-src/gru-plan.jpg`) | s05 | Gru's Plan, 4 панели (id 131940431) — **замена Expanding Brain** | эскалация архитектуры «на всякий случай» с абсурдной развязкой: задача была на три строки обычного кода | `https://i.imgflip.com/26jxvz.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `s05a-changemymind-ru.png` (из `memes-src/change-my-mind.jpg`) | s05a | Change My Mind (id 129242436) | роль-персона в промпте не повышает фактическую точность | `https://i.imgflip.com/24y43o.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |
| `s05c-pigeon-ru.png` (из `memes-src/is-this-a-pigeon.jpg`) | s05c | Is This A Pigeon (id 100777631) | протокольную роль system принимают за надёжную границу (а это лишь склонность) | `https://i.imgflip.com/1o00in.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |
| `s12-rollsafe-ru.png` (из `memes-src/roll-safe.jpg`) | s12 | Roll Safe (id 89370399) | не нужен RAG, если корпус влезает в контекст | `https://i.imgflip.com/1h7in3.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |
| `s19b-batman-ru.png` (из `memes-src/batman-slap.jpg`) | s19b | Batman Slapping Robin (id из get_memes `9ehk`) | «агент — просто чат подороже» → это другой порядок цены | `https://i.imgflip.com/9ehk.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |
| `s22c-pooh-ru.png` (из `memes-src/tuxedo-pooh.png`) | s22c | Tuxedo Winnie the Pooh (id 178591752) | плоский файл-лог vs граф-база знаний памяти (под требование масштаба) | `https://i.imgflip.com/2ybua0.png` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |
| `s22e-thisisfine-ru.png` (из `memes-src/this-is-fine.jpg`) | s22e | This Is Fine (id 55311130) | «файл-инструкция всё починит», пока агент-система горит (presence paradox) | `https://i.imgflip.com/wxica.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |
| `s24-alwayshasbeen-ru.png` (из `memes-src/always-has-been.png`) | s24 | Always Has Been (id 252600902) | данные, покинувшие периметр (вне ZDR), «так было всегда» вне вашей политики | `https://i.imgflip.com/46e43q.png` (2026-09-06) | Imgflip meme template — fair use, образовательный контекст |

Дополнительно сгенерированные, но НЕ размещённые композиты (нет чистого слота на
плотных схема/таблица-слайдах §3; blank оставлены для traceability):
`s11-pooh-ru.png` (Tuxedo Pooh для RAG-провенанса), `s15-doge-ru.png` (Buff Doge
vs Cheems: PEFT vs полное дообучение). Blank-шаблоны — в `memes-src/`.

## v6 — реальные интернет-мемы (первый мем-пасс, issue #185)

4 исходных мема (Drake / пират-cover / Distracted Boyfriend + прежний Expanding
Brain, теперь заменён на Gru's Plan). Композиты генерируются `make_memes.py`.

| локальный файл (композит) | слайд | мем-шаблон | источник blank-шаблона + дата | лицензия / статус |
|---|---|---|---|---|
| `s01-drake-ru.png` (из `drake-blank.jpg`) | s01 | Drake Hotline Bling (reject/approve) — reject: усложнять промпт ради точности; approve: выбрать архитектуру под задачу | imgflip `https://i.imgflip.com/30b1gx.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `cover-pirate-crop.png` (из `well-yes-actually-no.jpg`) | s02 (cover) | «Well yes, but actually no» (пират из Aardman/Sony «Pirates! Band of Misfits») — намёк «магической пилюли не существует»; английская baked-in подпись обрезана | imgflip `https://i.imgflip.com/2uctbv.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `s06-distracted-ru.png` (из `distracted-blank.jpg`) | s06 | Distracted Boyfriend — модель (парень) отвлеклась на «красивое объяснение вслух» и упустила «реальную причину ответа» | imgflip `https://i.imgflip.com/1ur9b0.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |

Blank-шаблоны (без подписей) оставлены на диске для traceability в `assets/web/`
и `assets/web/memes-src/`. Композиты с русскими подписями генерируются скриптами
`make_memes.py` (v6) и `make_memes_v6.py` (v6.1) и встраиваются в `build_v3.py`.
`s05-brain-ru.png` / `expanding-brain-blank.jpg` больше НЕ используются (заменены
Gru's Plan), оставлены для истории.

## v5 — divider-фото (Wikimedia Commons)

All images sourced from Wikimedia Commons (Tier 1) via Special:Redirect/file, width=1000.

| filename | source + date | license | direct URL |
|---|---|---|---|
| div-r1-knife.jpg | Wikimedia Commons — "Chef's knife" (retrieved 2026-09-06) | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:Chef%27s_knife.jpg |
| div-r2-library.jpg | Wikimedia Commons — "George Peabody Library" (retrieved 2026-09-06) | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:George_Peabody_Library.jpg |
| div-r3-tuning.jpg | Wikimedia Commons — "DiGiCo S21 Mixing Console 2017" (retrieved 2026-09-06) | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:DiGiCo_S21_Mixing_Console_2017.jpg |
| div-r4-robot-arm.jpg | Wikimedia Commons — "Factory Automation Robotics Palettizing Bread" (retrieved 2026-09-06) | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:Factory_Automation_Robotics_Palettizing_Bread.jpg |
| div-r5-control-panel.jpg | Wikimedia Commons — "Cockpit Convair Coronado Luzern" (retrieved 2026-09-06) | CC BY-SA (Commons) | https://commons.wikimedia.org/wiki/File:Cockpit_Convair_Coronado_Luzern.jpg |
| div-extra.png | Wikimedia Commons — "Silicon chip 3d" (retrieved 2026-09-06) | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:Silicon_chip_3d.png |
| (s30 bridge) | pre-existing: ../assets/screenshots/s30-coding.jpg (308KB, 1404x936, real JPEG) — NOT re-downloaded | see its .url sidecar | — |

Notes:
- License labels reflect typical Commons licensing for these files; verify exact per-file terms on the linked File: page before public publication. All are CC-licensed on Commons (no all-rights-reserved).
- div-extra.png is a genuine PNG (527x538). Optional fallback "AI/chip" image; use only if a 6th divider is needed.
