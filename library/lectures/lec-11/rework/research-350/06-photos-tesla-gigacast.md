# Фото для кейса Tesla Giga Press — цельная отливка кузова (issue #353)

Задача: найти реальные фотографии для кейса «Giga Press — цельная отливка кузова» тремя
ракурсами — (а) станок целиком, (б) готовая отливка крупным планом, (в) цех с несколькими
станками. Это **отдельный кейс от палатки GA4 2017–2018** (см. §7 `05-illustrations-log.md`) —
там разбирается ручная сборочная линия под тентом, здесь — сама технология гигалитья.

Существующий `s01-tesla-giga-press.png` (500×282, источник Wikipedia `Giga_Press`) не
перезаписан. Он сейчас орфанный: по §8 `05-illustrations-log.md` его в своё время сняли со
слайда `s32` и заменили на `tesla-fremont-model-y-single-piece-megacast.jpg` (сама отливка, а не
станок). Три новых файла ниже — дополнительный, более качественный материал на тот же кейс, а
не замена уже принятого решения по `s32`.

Протокол 6-tier (без mock), правила `CLAUDE.md` (hero-images-required, no-mock-fallbacks) +
`tools/presentation-build/trebovaniya-k-soderzhaniyu.md` §5.7.

## (а) Станок Giga Press целиком

**Tier сработал: 1 (og:image пресс-статьи Teslarati).**

Сохранено два файла — основной (на площадке Tesla) и альтернативный (более высокое разрешение,
но на площадке поставщика):

- **`tesla-gigacast-press-fremont.jpg`** — основной. Станок Giga Press (бело-красный корпус
  IDRA OL 6100 CS) на площадке Tesla Fremont, виден полностью в профиль, рабочие рядом для
  масштаба. Источник — og:image статьи Teslarati «Tesla begins Giga Press manufacturing at
  Fremont factory, first sighting in action» (22 января 2021,
  `https://www.teslarati.com/tesla-giga-press-fremont-factory-video/`). Credit в статье:
  «FoundryPlanet/YouTube». Разрешение 1437×802.
- **`tesla-gigacast-press-idra-9000t.jpg`** — секундарный, другой станок (OL 9000 CS, 9000
  тонн усилия) на площадке самого производителя IDRA в Травальято (Брешиа, Италия) во время
  Open House 2022 года. Источник — Wikimedia Commons,
  `File:2022-06-29-idra-italy-open-house-giga-press-9000t-john-stokes-sandy-munro.jpg`
  (Tier 2, **CC0**, автор Paul Sladen, дата съёмки 2022-06-29). Два человека для масштаба на
  фото подписаны: Джон Стоукс (IDRA) и Сэнди Манро (известный автомобильный инженер-ревьюер).
  Разрешение исходника 5184×3456 (уменьшено при сохранении до 2400×1600, чтобы не раздувать
  репозиторий — оригинал choice сохранён в `.url`). Годится, если нужен кадр станка «как
  товара поставщика», а не конкретно на территории Tesla.

## (б) Готовая отливка крупным планом

**Tier сработал: 1 (og:image пресс-статьи Teslarati).**

Существующий `tesla-fremont-model-y-single-piece-megacast.jpg` (январь 2021, см. §8 прежнего
лога) уже показывает однодетальную отливку заднего подрамника Model Y — использовать его
повторно для нового кейса означало бы задвоить один и тот же кадр на двух разных слайдах.
Вместо этого найдена **другая** отливка — из другого кузова (Cybertruck) и другого года:

- **`tesla-gigacast-cybertruck-closeup.jpg`** — цельная однодетальная отливка задней части
  кузова Cybertruck изнутри, снята крупным планом после снятия защитных чехлов: видна литая
  алюминиевая структура с рёбрами жёсткости, без единого сварного шва на всей видимой площади
  кадра — именно то визуальное доказательство «70 деталей в одну», которым известен метод.
  Источник — og:image статьи Teslarati «Tesla Cybertruck body with single-piece rear megacast
  spotted in Giga Texas» (10 декабря 2022,
  `https://www.teslarati.com/tesla-cybertruck-single-piece-rear-megacast-first-look-video/`).
  Credit в статье: «Kim Java/Twitter» (кадр снят на территории Giga Texas). Разрешение
  2226×1290 — заметно чётче и крупнее кадра, который уже используется на `s32`.

## (в) Цех с несколькими станками

**Tier сработал: 1 (og:image пресс-статьи Teslarati).**

- **`tesla-gigacast-giga-texas-floor.jpg`** — цех литейного участка Giga Texas: на заднем
  плане уже смонтированный и работающий первый станок Giga Press (виден логотип «TESLA» и
  «IDRA», табличка «OL 6100 CS»), на переднем плане — второй станок, ещё в заводской деревянной
  таре с маркировкой «IDRA», которую как раз распаковывают и готовят к монтажу; вокруг — техника
  и рабочие в касках и жилетах. Кадр документально показывает именно множественность станков на
  одном участке (один уже в работе, второй монтируется), а не постановочный «ряд машин» —
  честно отражает реальный момент (апрель 2021), когда на площадке физически стояли два станка
  одновременно. Источник — og:image статьи Teslarati «Tesla Gigafactory Texas gets its second
  Giga Press machine» (16 апреля 2021,
  `https://www.teslarati.com/tesla-giga-press-2-texas-pictures/`). Credit в статье: «Jeff
  Roberts». Разрешение 2048×1152.

**Честно исключено для (в):** drone-кадр с сайта Tesla Oracle («Fremont-Model-Y-Diecast-
Machines.jpg», из статьи «Tesla Fremont factory drone video shows the Model Y Giga Casting
machines & Roadrunner 'Magic Cube'») тоже показывает два станка на одной площадке, но поверх
кадра наложены красные кружки и текстовые подписи («Giant Tesla Diecast Machine - 1/2»),
добавленные самим блогом при публикации — это не кадр-мок, а аннотированная поверх реального
фото версия; по правилу чистоты слайда (без чужих подписей и графики поверх кадра) этот вариант
не взят, тогда как `tesla-gigacast-giga-texas-floor.jpg` — чистый кадр без наложений. Низкокачественный
(тёмный, в дыму) кадр с площадки Giga Shanghai (Wikimedia Commons,
`Tesla-giga-shanghai-locally-produced-lk-gigapress-platten.png`, июль 2020) просмотрен и
отклонён по той же причине: почти ничего не видно сквозь дверной проём и строительную пыль,
кадр не читается как «цех с несколькими машинами».

## Сводка по tier'ам

| Фото | Назначение | Tier | Источник |
|---|---|---|---|
| `tesla-gigacast-press-fremont.jpg` | (а) станок целиком, Tesla Fremont | 1 (og:image) | teslarati.com, 22.01.2021, credit FoundryPlanet/YouTube |
| `tesla-gigacast-press-idra-9000t.jpg` | (а) станок целиком, альт. (IDRA, поставщик) | 2 (Wikimedia Commons, CC0) | commons.wikimedia.org, 29.06.2022, автор Paul Sladen |
| `tesla-gigacast-cybertruck-closeup.jpg` | (б) готовая отливка крупным планом | 1 (og:image) | teslarati.com, 10.12.2022, credit Kim Java/Twitter |
| `tesla-gigacast-giga-texas-floor.jpg` | (в) цех с несколькими станками | 1 (og:image) | teslarati.com, 16.04.2021, credit Jeff Roberts |

Честных пробелов «не нашлось ничего настоящего» — **нет**: все три ракурса закрыты настоящими
фотографиями уровня tier 1–2, без обращения к tier 3–6 и без единого mock. Присвоение `sNN` и
финальный выбор между основным/секундарным вариантом (а) — на фазе сборки деки, как и для
находок `05-illustrations-log.md`.

Атрибуция для подписи на слайде (по выбору сборки деки):
- (а) основной: «Teslarati · FoundryPlanet/YouTube, январь 2021»
- (а) альтернативный: «Wikimedia Commons · Paul Sladen, CC0, июнь 2022»
- (б): «Teslarati · Kim Java/Twitter, декабрь 2022»
- (в): «Teslarati · Jeff Roberts, апрель 2021»
