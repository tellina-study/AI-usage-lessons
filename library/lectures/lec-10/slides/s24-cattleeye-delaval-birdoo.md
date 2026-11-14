---
id: s24
type: working_case_grid
duration_min: 2
assertion: "CattleEye CCTV + cloud AI: lameness score по биомеханике; 60 ферм, 11k коров (GEA channel >250k). DeLaval VMS V310: 99,8% attachment rate (998/1000 успешных подключений). Cargill Birdoo CV: >95% точность weight estimation, экономия 10-30 г корма на бройлера."
learning_goal: "3 working cases L3 — узкие задачи + measurable ROI"
learning_outcomes: [LO1a]
chapter_ref: "§3.2 + §3.3 Часть 2 — CattleEye, DeLaval, Cargill Birdoo"
references: [gea-cattleeye-product-page, dairyreporter-2019-delaval-vms, prnewswire-2022-cargill-birdoo]
visual:
  pattern: 3card_grid
  primary: "3-card grid (CattleEye CV bounding-box detection + DeLaval VMS V310 robot press photo + Cargill Birdoo official brand asset) — все реальные изображения, Tier 1"
---

# CattleEye + DeLaval VMS V310 + Cargill Birdoo

## Assertion

CattleEye CCTV + cloud AI: lameness score по биомеханике; 60 ферм, 11k коров (GEA channel >250k). DeLaval VMS V310: 99,8% attachment rate (998/1000 успешных подключений). Cargill Birdoo CV: >95% точность weight estimation, экономия 10-30 г корма на бройлера.

## Visual

Под assertion 28pt bold — 3-card grid horizontal. Каждая card в Ocean rounded box.

**Card 1 — CattleEye:**
- Сверху — реальное изображение с официальной страницы продукта GEA: корова на выходе из прохода, CV bounding-box вокруг головы (детекция для lameness score)
- Caption: «Lameness score по биомеханике движения»
- Архитектура: CCTV + cloud AI; **non-invasive** (нет ошейника)
- 60 ферм, 11 000 коров; через GEA channel — фермы, обслуживающие **>250 000 коров**
- Приобретена GEA в 2024 году

**Card 2 — DeLaval VMS V310:**
- Сверху — реальная пресс-фотография робота-доильного аппарата (DairyReporter, статья о запуске V310, ноябрь 2019)
- **99,8% attachment rate** ★ gold accent
- = 998 успешных подключений из 1000 (оставшиеся 2 — ручное вмешательство)
- +15% North American installations 2025
- Flow-Responsive Milking стандарт на новых V300 с июня 2025

**Card 3 — Cargill Birdoo:**
- Сверху — официальный брендовый логотип Birdoo (пресс-релиз Cargill через PR Newswire, январь 2022) — демо-скриншот CV-оценки веса не найден публично, использован подтверждённый официальный актив
- **>95% точность** weight estimation **без физического взвешивания**
- Экономия **10-30 г корма на бройлера** через точное дозирование (раньше переход на финишный корм)
- Americas-exclusive внедрение

Bottom callout 14pt italic в Teal-tint box: «**Общий паттерн:** узкая задача + measurable ROI + augmentation, не replacement. **Тенденция консолидации L3:** MSD приобрёл Antelliq за $3,85 млрд; GEA приобрёл CattleEye в 2024. Рынок зрелый, новые входы сложнее».

Footer 12pt italic: «Источники: Fortune 2025-06; DeLaval press 2025-04; Cargill.com 2025 · Фото: gea.com/cattleeye; DairyReporter 2019; PR Newswire 2022».

## Speaker notes

Помимо SenseHub, три других working case на третьей ступени стоит рассмотреть, потому что они показывают разные архитектурные подходы к близким задачам.

CattleEye — другой ракурс. Корова идёт по коридору на выход из milking parlour. Камера снимает её походку с высоты; модель оценивает lameness score, балл хромоты, по биомеханике движения — симметрия шагов, амплитуда наклона головы, опускание зада. Хромота — одна из ведущих причин снижения молокоотдачи и преждевременной выбраковки; раннее выявление, когда корова ещё ходит, но уже компенсирует боль, даёт фермеру две-три недели на лечение до того, как процесс станет необратимым. Решение дёшево в развёртывании — CCTV плюс cloud, без надевания ошейника на каждое животное. Это структурно отличается от SenseHub: SenseHub требует надевания ошейника на каждое животное, CattleEye — нет. Шестьдесят ферм, одиннадцать тысяч коров напрямую; через канал GEA — фермы, обслуживающие более двухсот пятидесяти тысяч коров. Приобретена GEA в 2024 году — пример консолидации L3 рынка.

DeLaval VMS V310 — роботизированный доильный аппарат. Корова сама заходит в станцию, когда чувствует переполненное вымя — обычно два-три раза в день. Камера и лазерный сканер находят соски; роботизированная рука подсоединяет доильные стаканы. Девяносто девять и восемь десятых процента attachment rate означает: девятьсот девяносто восемь из тысячи попыток успешны — оставшиеся две требуют ручного вмешательства или повторной попытки. Это очень узкая задача, в которой ИИ плюс механика дают deterministically лучший результат, чем ручной труд. Корова не теряет время в очереди на доение, может доиться чаще, что увеличивает суточный надой; фермер освобождён от ночных и утренних доек; робот работает двадцать четыре на семь. Прирост северо-американских установок на пятнадцать процентов в 2025 году отражает экономическую логику в крупных молочных хозяйствах.

Cargill Birdoo — компьютерное зрение для оценки веса бройлера в курятнике без физического взвешивания. Камера сверху фиксирует силуэт птицы, модель оценивает её массу по visual features. Заявленная точность — более девяноста пяти процентов; экономия десять-тридцать граммов корма на бройлера благодаря возможности более точного дозирования: если средний вес стада уже достиг целевого, переходить с ростового корма на финишный раньше. Americas-exclusive — это узкая ниша, в которой решение работает и масштабируется.

Общий паттерн всех трёх — augmentation, not replacement. AI распознаёт сигналы, человек принимает решения. Узкая задача с измеримой обратной связью. Это структурный success третьей ступени, который объясняет, почему рынок L3 в 2024-2025 годах прошёл консолидацию — MSD за три и восемьдесят пять десятых миллиарда поглотил Antelliq, GEA приобрёл CattleEye — а не банкротства. Рынок зрелый.

## Источники

Цифры (60 ферм / 11k коров / GEA channel >250k; 99,8% attachment rate / +15% NA installations; Birdoo >95% точность / 10-30 г корма):
- Fortune (2025-06) — CattleEye GEA channel.
- DeLaval press (2025-04) — VMS V310 +15% NA installations.
- Cargill.com (2025) — Birdoo CV deployment.

Изображения (подключены в Фазе 3 вместо родовых фото коров — K-2 fix):
- gea.com/en/products/milking-farming-barn/gea-herd-management/cattleeye/ — официальная страница продукта CattleEye (GEA).
- DairyReporter (2019-11-26) — «DeLaval VMS V310 milking system launches».
- PR Newswire (2022-01-11) — «Cargill Expands Portfolio of Artificial Intelligence-Powered Innovations» (Birdoo).
