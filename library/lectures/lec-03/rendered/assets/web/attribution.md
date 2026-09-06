# Image Attribution — Лекция 3 deck v6 (dividers + memes)

Непубличная презентация (внутренний курс МГТУ). Требование по правам — только
эта таблица с указанием источника; на слайдах подписи-источники НЕ показываются
(включая мемы). Английские baked-in подписи мем-шаблонов обрезаны/перекрыты
русскими подписями в мем-стиле.

## v6 — реальные интернет-мемы (issue #185, owner: «реальные мемы как в Л2 v2»)

Заменены flat-иллюстрации на 4 слайдах реальными узнаваемыми мем-шаблонами
(imgflip meme-templates blank + русские подписи, наложенные через PIL). На
s05/s06 сопутствующие текст-блоки убраны полностью — тезис несёт мем.

| локальный файл (композит) | слайд | мем-шаблон | источник blank-шаблона + дата | лицензия / статус |
|---|---|---|---|---|
| `s01-drake-ru.png` (из `drake-blank.jpg`) | s01 | Drake Hotline Bling (reject/approve) — reject: усложнять промпт ради точности; approve: выбрать архитектуру под задачу | imgflip `https://i.imgflip.com/30b1gx.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `cover-pirate-crop.png` (из `well-yes-actually-no.jpg`) | s02 (cover) | «Well yes, but actually no» (пират из Aardman/Sony «Pirates! Band of Misfits») — намёк «магической пилюли не существует»; английская baked-in подпись обрезана | imgflip `https://i.imgflip.com/2uctbv.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `s05-brain-ru.png` (из `expanding-brain-blank.jpg`) | s05 | Expanding Brain (4 панели) — эскалация архитектуры как абсурд: один вызов → RAG → петли/инструменты → мульти-агентная оркестрация; композит: крайняя правая колонка мозгов + широкая русскоподписная колонка | imgflip `https://i.imgflip.com/2jnia2.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |
| `s06-distracted-ru.png` (из `distracted-blank.jpg`) | s06 | Distracted Boyfriend — модель (парень) отвлеклась на «красивое объяснение вслух» и упустила «реальную причину ответа» | imgflip `https://i.imgflip.com/1ur9b0.jpg` (2026-09-06) | Imgflip meme template — fair use, образовательный некоммерческий контекст |

Blank-шаблоны (без подписей) оставлены на диске для traceability:
`drake-blank.jpg`, `expanding-brain-blank.jpg`, `distracted-blank.jpg`,
`well-yes-actually-no.jpg`. Композиты с русскими подписями генерируются
скриптом `../../make_memes.py` и встраиваются в `build_v3.py`.

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
