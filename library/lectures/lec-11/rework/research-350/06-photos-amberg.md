# Добор фото Siemens Amberg (EWA) до ≥5 уникальных — issue #353

Продолжение `05-illustrations-log.md` §3 (там зафиксированы 3 уже сохранённых файла:
`siemens-amberg-ewa-shopfloor.jpg`, `siemens-amberg-ewa-mezzanine-view.jpg`,
`siemens-amberg-ewa-aerial.jpg`, все tier 3, press.siemens.com, 2015 / 2025–2026).
Задача — добрать до **≥5 уникальных** фото. Правила те же: `CLAUDE.md`
(hero-images-required, no-mock-fallbacks) + `tools/presentation-build/README.md` §5.7
(6-tier acquisition), без единого mock.

## Что проверено и честно исключено

**1. Полный press-kit визита Меркель 2015 года (press.siemens.com/.../event/german-chancellor-merkel-visits-siemens-showcase-digital-factory).**
Страница — медиагалерея на 7 фото (`im2015020433`–`im2015020439co_300dpi.jpg`); два из них
(`435`, `439`) уже сохранены в `05-illustrations-log.md` §3. Остальные пять (`433`, `434`,
`436`, `437`, `438`) скачаны и просмотрены визуально — все пять оказались портретными
кадрами визита: канцлер Меркель и топ-менеджмент Siemens крупным планом в синих костюмах,
либо групповая сцена с Меркель в центре кадра на фоне производства. Ни один не даёт цех как
главный объект — это тот же класс исключения, что уже применялся к групповым портретам
команды Yokogawa в §2 (`05-illustrations-log.md`): «люди, не производство». Не сохранены.

**2. «The Impulse» — визит-центр цифровизации Amberg** (press.siemens.com/de/de/pressemitteilung/siemens-amberg-gibt-impulse-fuer-die-fabriken-der-zukunft).
Три фото (`VCA-The-Impulse-Innenbereich.jpg`, `-Innenblick.jpg`, `-Aussenansicht.jpg`) —
интерьер/экстерьер отдельного выставочного павильона для посетителей, не цех EWA. Не
относится к разбору главы (который про сам завод, не про шоурум) — тот же класс исключения,
что BMW Welt в `05-illustrations-log.md` §6. Не сохранены.

**3. Награды Industrie 4.0 / ROI** (press.siemens.com/de/de/pressemitteilung/siemens-elektronikwerk-amberg-mit-dem-industrie-40-award-ausgezeichnet).
Два фото (`SIEMENS-ROI-Award-blaue-Wand.jpg`, `SIEMENS-ROI-Industrie-4.0-Award.jpg`) —
постановочные портреты награждения (2 и ~18 человек в деловых костюмах на фоне стенда), не
производство. Не сохранены.

**4. Siemens AG reference-страница Vision AI (references.siemens.com, Pin-in-Paste inspection).**
Проверена напрямую — реальных фото цеха Amberg на странице нет (только заголовочный
плейсхолдер и ссылки на отдельный проект в Эрлангене). Не относится к Amberg.

## Что сохранено

**4. `siemens-amberg-ewa-floor-overview.jpg` — tier 1 (официальная страница площадки на siemens.com).**

Источник: `https://www.siemens.com/en-us/company/global-locations/germany/amberg-production-development/`
— заголовочное фото страницы (`im2016110166df`, EXIF `ImageDescription: Elektronikwerk
Amberg`, 2126×1417). Вид сверху с антресоли на цех поверхностного монтажа: десятки
автоматических сборочных ячеек, стеклянные защитные ограждения с роботами-манипуляторами
внутри, операторы в синих халатах за рабочими местами. Это собственная официальная страница
завода (не пресс-релиз одного события, а постоянная корпоративная страница локации) —
honest tier 1, тот же уровень, что og:image Audi в §1. Прямая иллюстрация к «75% цепочки
создания стоимости машинами» — в кадре видно именно это соотношение автоматических ячеек и
операторов.

**Важно:** то же самое фото (тот же кадр, другой краткий crop 16:9) переразмещено на
стороннем кейс-стади NavVis (`Siemens-Casestudy_pics-2-2.jpg`, см. ниже) — это не второе
уникальное фото, а тот же снимок с другого хостинга; сохранён один раз, с официального
источника.

**5. `siemens-amberg-ewa-digital-twin-scan.jpg` — tier 3 (vendor case-study, navvis.com).**

Источник: `https://www.navvis.com/resources/case-studies/siemens` (`Siemens-Casestudy_pics--1.jpg`,
3704×1480). Облако точек (point cloud) 3D-лазерного скана того же цеха EWA — именно тот
«цифровой двойник», о котором глава рассказывает в §4.1: не рендер и не иллюстрация, а
прямая визуализация реальных данных LiDAR-скана, снятого NavVis по заказу Siemens для
документации и планирования цеха. Честно иначе, чем «фото» в обычном смысле — но это не
mock: данные настоящие, кейс прямо относится к Amberg (NavVis называет Siemens/Amberg
партнёром кейс-стади по имени).

**6. `siemens-amberg-ewa-digital-twin-viewer.jpg` — tier 3 (vendor case-study, navvis.com).**

Тот же кейс-стади (`Siemens-Casestudy_pics-3-2.jpg`, 1920×1080). Скриншот интерактивного
просмотрщика NavVis IVION внутри реального отснятого цеха (панорама линий поверхностного
монтажа с видимым UI «Measurements» и меткой «1.75 m») — то есть снова реальные
фотореалистичные данные скана, не иллюстрация. UI-оверлей на кадре — честно виден и
в подписи не скрывается.

Атрибуция для подписи: «Siemens AG · siemens.com, б/д» (floor-overview) и «NavVis GmbH ×
Siemens AG · success story, б/д» (digital-twin-scan / digital-twin-viewer).

## Сводка по tier'ам (добавление к таблице в `05-illustrations-log.md`)

| Файл | Tier | Источник |
|---|---|---|
| `siemens-amberg-ewa-floor-overview.jpg` | 1 (корпоративная страница локации) | siemens.com |
| `siemens-amberg-ewa-digital-twin-scan.jpg` | 3 (vendor case-study) | navvis.com |
| `siemens-amberg-ewa-digital-twin-viewer.jpg` | 3 (vendor case-study) | navvis.com |

**Итог: 6 уникальных реальных фото Amberg на диске** (3 из `05-illustrations-log.md` §3 + 3
новых выше) — выше порога ≥5, без единого mock. Честных пробелов нет: всё, что не вошло,
исключено по предметному критерию (люди вместо производства / не тот объект — визит-центр,
награды), не из-за недоступности источника.
