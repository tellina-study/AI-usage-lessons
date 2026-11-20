# Iteration log — часть 5 (issue #340, раунд "фото сплющены — трактор и корова")

**Контекст.** Владелец после двух раундов "исправлено" всё ещё видел сплющенные
фото ("трактор и корова"). Оркестратор прогнал собственный AR-diagnostic
(python-pptx `shape.image.size` vs `shape.width/height`) по ВСЕЙ деке (52
слайда, не только 4 ранее тронутых) и нашёл **8 SEVERE (diff>0.3) + 2 minor
(diff 0.03-0.3)** — ни один из них не пересекался с предыдущими двумя раундами
(те трогали s08b/s17/s20/s25, затем s07a/s10/s16b/s23c).

## Найденные 10 кейсов + root cause per slide

| slide | root cause | fix |
|---|---|---|
| s07 (See&Spray) | box AR 2.55 (банер) создан дизайном, source AR 1.33 | re-crop source к AR 1.8 (видна вся опрыскивательная машина), frame сужен/центрирован под новый AR вместо растяжения |
| s09 (TerraMind) | box AR 2.00 vs source (почти квадратный Sentinel-2 tile) AR 1.04 | center-crop источника к AR 2.0 — текстура снимка, без «субъекта», потеря верха/низа не дезориентирует |
| s14 (РФ L1) | **НЕ фото** — chart `c14-rus-digi.png` (QuickChart PNG) был 1600×1000 (AR 1.6), embed в box AR 2.30 | chart регенерирован через QuickChart на нативном AR 2.305 (тот же data/colors/range), файл перезаписан in-place |
| s19 (Monarch Tractor, **owner-named**) | embedded файл УЖЕ был экстремальным banner-crop (1200×332, AR 3.61) реального фото, дополнительно растянутый box'ом AR 4.10; трактор читался как едва заметная полоска | передран с ПОЛНОГО (нерезанного) пресс-фото (передокачан с techcrunch.com), tighter + off-center crop на обеих осях → весь трактор ясно виден; box вырос h=1.45→1.905 (AR 3.12), подпись/отступ/takeaway сжаты, чтобы не упереться в footer |
| s23 (SenseHub cow, **owner-named**) | source — ПОРТРЕТНОЕ фото (1280×1927, AR 0.66) коровы, насильно в landscape box AR 1.5; прямой crop отрезал бы ноги или голову | **re-sourced** целиком — найдено настоящее landscape (AR 1.5, точное совпадение, 0 crop) public domain USDA-фото (Reinford Farms, ушные бирки видны чётко) |
| s34 (GNSS/связь) | box AR 2.12 vs квадратный (1280×1280) спутниковый render | off-center crop (bias_y=0.35, сохраняет весь спутник+панели, обрезает в основном пустой космос сверху) |
| s30b (vendor lock-in) | box AR 3.55 vs source AR 1.78 (Мелитополь трактор) | re-crop к AR 2.75 (мягче banner, весь трактор+2 человека видны); box height 5.0→5.1, photo height 1.55→2.0 — 2 другие фото на этом слайде (FTC thumbnail, DJI icon) уже совпадали точно, не тронуты |
| s37s (L4 retail hero thumbnail) | крошечный box 0.62×0.60 (AR 1.03) vs source AR 1.5 | left-biased crop (сохраняет вывеску «Перекрёсток», которая в левых 2/3 кадра) — 3 неиспользуемых кандидата (`p37s-grocery.jpg` и т.д.) оставлены на диске нетронутыми |
| s05c (ретроспектива, minor) | хардкод `img_w = img_h * 1.6` устарел — реальные PNG 1587×906/1568×899 (AR≈1.75) | заменено на PIL-вычисление реального AR каждого chart-файла во время сборки вместо константы |
| s21 (клубника, minor) | box AR 1.375 vs source AR 1.50 (минимальный stretch ~8%) | center-crop к AR 1.375 |

## Верификация (raw output ниже в session report)

- `fix_aspect_ratios.py` расширен (`offset_crop_to_aspect` + `JOBS_ROUND2` +
  `make_hero_crop_monarch()`), запущен — все round-1 + round-2 джобы
  регенерированы с `ratio≈target` (diff <0.002 везде).
- Rebuild (`build_lec10.py`) → 52 слайда, без ошибок.
- LibreOffice portable (`~/.local/lo-portable-env.sh` — на этой машине
  `soffice` не в `$PATH` напрямую, обнаружен через `find / -iname soffice`,
  работает только после `source`) → PDF.
- **AR-diagnostic (оркестраторский скрипт дословно) на пересобранной деке:
  0 SEVERE, 0 minor по ВСЕЙ 52-слайдовой деке.**
- 10 затронутых слайдов отрендерены в PNG, каждый просмотрен глазами — ни
  одного растяжения/дезориентирующего кадрирования; s19 и s23 (named cases)
  явно показывают целую технику/животное в landscape.
- Hyperlink r:id: s19 (`techcrunch.com/.../monarch-tractor-sued...`) и s23
  (`commons.wikimedia.org/.../20180124-OSEC-PJK-0944...`) проверены через XML
  `ppt/slides/_rels/slideN.xml.rels` → `rId3` резолвится, и тот же `rId3`
  реально используется в `hlinkClick` внутри `slideN.xml` (не orphaned rel).
  Pre-existing hyperlinks (s14 Wikimedia фото пшеницы, s37s Perekrestok фото)
  тоже устояли (slide4.xml.rels / slide23.xml.rels / slide47.xml.rels).
- `deck.yaml`: сумма `timing_min` по всем 52 слайдам = **90.0** (без
  изменений — раунд был illustration-only, ни один `timing_min` не трогался).
- Trading-residue grep: 0 regressions в RU build-скриптах (все hits —
  pre-existing комментарии про удаление трейдинг-раздела issue #340 v3.9).
  **Побочная находка (НЕ в scope этого раунда):** `build_lec10_*_en.py` (EN
  track) всё ещё использует старые "L5" ярлыки — EN re-sync происходит
  отдельной фазой после approve RU (bilingual rule), не regression этого
  раунда.
- Designer-extras grep (`[VERIFY-DAY-OF]`, `LO[1-9]`, `§[0-9]+\.[0-9]+`,
  timing/методология паттерны) по visible body + speaker_notes всех 52
  слайдов — 1 hit, pre-existing (`§3.4` в footer slide40, не тронут этим
  раундом, не введён этой правкой).

## Asset provenance (новые файлы)

- `assets/photos/monarch-full-source.jpg(.url)` — полный (нерезанный) Monarch
  MK-V пресс-фото, передокачан с techcrunch.com (тот же источник, что и уже
  существующий обрезанный `p19-monarch-mkv-real.jpg`).
- `assets/photos/p19-monarch-mkv-hero-crop.jpg` — произведён из
  `monarch-full-source.jpg` через `fix_aspect_ratios.py::make_hero_crop_monarch()`.
- `assets/photos/p23-cow-eartag-landscape.jpg(.url)` — новый источник (USDA,
  Preston Keres, public domain, Reinford Farms PA 2018), заменяет портретный
  `p23-cow-ear-tag.jpg` (последний НЕ удалён с диска).
- `assets/charts/c14-rus-digi.png` — перезаписан in-place (тот же filename,
  QuickChart v3 API, `min:0/max:80` corrected — v2 Chart.js синтаксис без
  `v=3` параметра игнорировал `scales.y.min/max` и авто-масштабировал от ~20).
- 6 × `-crop.jpg` файлов (s07/s09/s34/s30b/s37s/s21) через расширенный
  `fix_aspect_ratios.py`.

**Status: COMPLETE.**

## Раунд "ни одного реального фото/рендера механизма" (issue #340, 2026-11-20)

**Контекст.** Владелец независимо от aspect-ratio раундов выше: «а где
дополнения иллюстраций которые я просил? сейчас почти все механизмы не
понятно как выглядят и как устроены, надо показать как они выглядят и
работают (фото или рендер) не схема». Оркестратор независимо нашёл 4 слайда:
s07a (3 generic icon camera/cpu/target вместо фото), s18 (4 карточки — родовые
tractor/leaf/package иконки вместо named-product фото), s23c (реальное фото
уже было, но 0.75×0.55in — пятно размером с иконку), s16b (реальный рендер уже
был, но 2.20×0.95in — тоже слишком мелко).

### s07a — добавлено реальное фото (6-tier, tier 1 успех)

og:image с `deere.com/.../see-spray-ultimate` оказался press-asset
`see-spray-ultimate-camera-feature-1-png.webp` — буквально крупный план одной
из 36 камер на боковой штанге, с проводкой и маркировкой спрей-магистрали
("20 PSI W.P."). Обрезан от маркетингового зелёного градиента-оверлея (crop,
без изменения содержимого) → `p07a-see-spray-camera-boom-crop.jpg` (655×758).
3-шаговая icon-схема (камера→CNN→форсунка) оставлена РЯДОМ с фото текстом без
своих иконок (иконки были decorative дублем того, что теперь показывает фото).

**Found-and-fixed bug в процессе:** первая правка спэйсинга (попытка сжать
①-③ чтобы выделить место под фото) случайно свела `err_y` слишком близко к
label-строке «①…» — обводка ocean_box наехала на верх букв (видно на
PNG-инспекции iter1 как "перечёркнутый" текст). Пофикшено явным
`gap = label_bottom + 0.05` вместо магических смещений — тот же паттерн бага
повторился бы в «⑤» секции (та же магическая арифметика), исправлен сразу
везде в этом блоке.

### s18 — 4/4 реальных фото найдены (6-tier, все tier 1 кроме Solinftec)

- Solinftec Solix: solinftec.com вернул 403 на automated fetch (tier 1
  заблокирован) → tier 3 (futurefarming.com press-фото, сам робот с видимым
  брендингом "SOLINFTEC" на корпусе).
- Saga UV-C: og:image sagarobotics.com — два робота Thorvald UV-C ночью, но
  кадр из виноградника, не из клубничного тоннеля (та же платформа, другая
  культура) — честно подписано overlay-полосой на самом фото.
- Tevel: официальный press-фото с сайта (не просто og:image-превью) — летающий
  дрон с рукой-захватом среди нектаринов.
- AGCO PTx Outrun: og:image ptxag.com — Fendt-трактор с белым lidar/radar
  receiver на крыше кабины, тянущий grain cart, который разгружает комбайн.

**Found-and-fixed bug:** первая версия клала caveat-подпись для Saga отдельной
строкой НИЖЕ фото, что сдвигало весь текстовый блок этой карточки на 0.2in
ниже трёх остальных — ряд выглядел неровным (visual mass balance). Исправлено:
caveat переехал на overlay-полосу на самом фото (как подпись источника на
фото), все 4 карточки сверены на одной baseline.

### s23c и s16b — существующие реальные фото увеличены, источник не менялся

- s23c SenseHub collar: 0.75×0.55in → 1.60×1.17in (×~4.5 по площади), левая
  колонка перекомпонована вокруг фото как hero-элемент (заголовок отдельной
  строкой сверху, текст про 3 сигнала — сбоку от фото, не над мелкой
  картинкой).
- s16b LaserWeeder module: 2.20×0.95in → 2.64×1.20in (×~1.6 по площади),
  нижняя gold-полоса подросла 1.42→1.50in для места, pipeline-текст справа
  сузился незначительно.

### Проверка (orchestrator, не самоотчёт субагента)

- AR-diagnostic по всей деке (52 слайда): **0 flagged** (было 0 до правки,
  осталось 0 — новые фото все вставлены с `w,h` строго по native px AR,
  без stretch).
- `python-pptx` слайд-индекс целевых 4 кадров подтверждён текстовым поиском
  (s07a=13, s16b=26, s18=29, s23c=37), соседние слайды (12,14,25,27,28,30,36,38)
  сверены — порядок и контент не съехали.
- PDF: 52/52 страниц непустые (`page.get_text()`), сверка на тот самый
  известный баг #212-2 (stale/перезаписанный pptx во время конверсии).
- Новый footer-hyperlink на s07a (John Deere) проверен в сыром XML
  собранного pptx: `slide13.xml.rels` → `rId6` → `https://www.deere.com/...`,
  `<a:hlinkClick r:id="rId6"/>` на самом run'е — не самоотчёт, реальный r:id.
- deck.yaml / slides/*.md НЕ тронуты (`git diff --stat` пустой) — бюджет
  90.0 мин / 52 слайда подтверждён суммой `timing_min` по всем слайдам.

**Asset provenance:** все 5 новых фото-файлов имеют `.jpg.url` рядом с honest
tier-acquisition note (см. `assets/photos/p07a-*.url`, `p18-*.url` ×4).
