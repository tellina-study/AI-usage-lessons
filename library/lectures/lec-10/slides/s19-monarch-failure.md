---
id: s19
type: failure_case
duration_min: 2.2
assertion: "Сентябрь 2025: иск Burks Tractor (Idaho) — 10 тракторов за $773 088, «unable to operate autonomously». Ноябрь 2025: 102 сокращения (~38% штата). Апрель 2026: Caterpillar acqui-hire. Демо ≠ промышленное внедрение."
learning_goal: "AP — demo ≠ deployment; маркетинг «autonomous» = юридическая ловушка"
learning_outcomes: [LO2, LO5]
chapter_ref: "§2.4 Часть 2 — Strict-in F4 Monarch Tractor"
references: [techcrunch-2025-monarch-suit, techcrunch-2025-monarch-layoffs, techcrunch-2026-cat-acquisition]
visual:
  pattern: timeline_2018_2026
  primary: "Horizontal timeline 2018→2026 с 6 ключевыми точками (founded → MK-V → Foxconn → Idaho lawsuit → layoffs → Cat acquisition) + Monarch MK-V photo + TechCrunch иск headline"
---

# Monarch Tractor — «autonomous» при сломанной автономии

## Assertion

Сентябрь 2025: иск Burks Tractor (Idaho) — 10 тракторов за $773 088, «unable to operate autonomously». Ноябрь 2025: 102 сокращения (~38% штата). Апрель 2026: Caterpillar acqui-hire. Демо ≠ промышленное внедрение.

## Visual

Под assertion 28pt bold — горизонтальный timeline 2018→2026 с шестью ключевыми точками-маркерами (диаметр ~40px, Primary mid, c gold accent на ключевых датах):

- **2018** Founded в Livermore CA (выходцы Tesla + Karlo Mondavi)
- **2021-2022** Commercial launch MK-V $80-100k; Foxconn investment 2022
- **2024** Peak fundraising $133M
- **Август 2025** Foxconn продал Lordstown plant за $375M → **первый сигнал ухудшения** ★ gold
- **Сентябрь 2025** Burks Tractor (Idaho) иск: **10 тракторов за $773 088** «unable to operate autonomously» ★ gold
- **19 ноября 2025** Корпоративное письмо: **102 сокращения (~38% штата)**, риск shutdown
- **15 апреля 2026** **Caterpillar acqui-hire** ★ gold

Под timeline — 2-column nested layout:

**Левая колонка (50%):** Настоящее фото Monarch MK-V в поле (og:image статьи TechCrunch 2025-11-18 про иск Burks Tractor, оригинал — Monarch press, `techcrunch.com/wp-content/uploads/2024/07/monarch-Dairy-Riley.jpg`; обрезан в широкий баннер под строку) + caption «Monarch MK-V. Источник: Monarch press, публикация TechCrunch, 2025-11-18».

**Правая колонка (50%):** Текстовая карточка с дословной цитатой реального заголовка TechCrunch — «Monarch Tractor sued over tractors that were ‘unable to operate autonomously’» (18 ноября 2025) + caption «Дословный заголовок статьи об иске Burks Tractor». Это цитата, а не скриншот (headless-browser для захвата страницы недоступен в тулинге); прежняя версия файла несла перефразированный заголовок — заменён на дословный.

Bottom callout 14pt italic в Teal-tint box: «**Демо ≠ промышленное внедрение.** Маркетинг «autonomous» при том, что autonomy не выдержит судебной проверки = структурная trap. **Альтернатива:** supervised autonomy с явным disclosure capability / non-capability».

Footer 12pt italic: «Источники: TechCrunch 2025-08-13 (Foxconn); 2025-11-18 + 2025-11-19; 2026-04-15».

## Speaker notes

Перейдём к каноническому L2-провалу 2025 года — Monarch Tractor. Компания из Калифорнии, основана выходцами из Tesla и Карло Мондави в 2018 году: электрический трактор с автономным режимом для виноградников и овощных хозяйств. Привлечённый капитал — более двухсот двадцати миллионов долларов, из них сто тридцать три миллиона в раунде 2024 года; контрактный производитель — Foxconn с 2022 года.

В 2018-2020 — R&D и прототипы. В 2021-2022 — коммерческий запуск модели MK-V по цене около восьмидесяти-ста тысяч долларов за единицу, первые поставки в калифорнийские виноградники, инвестиция Foxconn усилила маркетинговое заявление об автономности. В 2023-2024 — заявки на «autonomous fleet operation» и пик привлечения капитала.

Дальше — каскад 2025-2026 годов. Четвёртого августа 2025-го Foxconn продал Lordstown plant за триста семьдесят пять миллионов — первый ясный сигнал ухудшения: контрактный производитель не вышел бы из производства без структурных проблем. В сентябре 2025-го — иск Burks Tractor Co. в суд штата Айдахо: десять тракторов 2024 года выпуска за семьсот семьдесят три тысячи восемьдесят восемь долларов, которые «unable to operate autonomously» — обещанная функциональность не работала. Дилер судится с производителем за несоответствие маркетинга «autonomous» контрактной реальности.

Девятнадцатого ноября 2025-го — корпоративное письмо о сокращении ста двух человек, примерно тридцати восьми процентов штата, с предупреждением о возможном закрытии. Компания заявляла переход из OEM в SaaS-провайдера автономии для тракторов сторонних производителей — но собственное корпоративное письмо признавало риск shutdown из-за сроков перехода.

Пятнадцатого апреля 2026-го Caterpillar приобрёл Monarch Tractor — acqui-hire post-failure: IP и инженерная команда консолидированы в автономном mining- и construction-дивизионе Cat, бренд Monarch фактически исчез. Это не возрождение технологии: закрытая дверь для direct-to-consumer модели Monarch и открытая дверь для retrofit-режима — AGCO PTx Outrun с предыдущего слайда — на смешанных парках техники. Strategic acquirer купил R&D-задел дешевле, чем создал бы сам.

Структурных причин несколько. «Autonomous» маркетинг без раскрытия supervised-autonomy: реальные машины требовали супервизии оператором, демо не равно надёжности в промышленной эксплуатации. Экономика general-purpose orchard tractor — субоптимальна. И специализация побеждает: в те же 2024-2026 годы LaserWeeder G2, Saga UV-C, Tortuga — все в коммерческой эксплуатации. Узкие решения выживают, универсальные «autonomous farm robots» банкротятся.

Главный выученный урок — анти-ИИ критерий AP-четыре: демо не равно промышленному внедрению. Маркетинг «autonomous» при том, что автономия не выдержит судебной проверки, — структурная ловушка для всей категории; автономия в сельском хозяйстве не yes/no, а градиент с десятками краевых случаев. Альтернатива: supervised autonomy с явным раскрытием способности и неспособности на каждое заявление.

## Источники

- TechCrunch (2025-08-13) — Foxconn Lordstown sale.
- TechCrunch (2025-11-18) — Burks Tractor lawsuit.
- TechCrunch (2025-11-19) — Monarch layoffs.
- TechCrunch (2026-04-15) — Caterpillar acquisition.
