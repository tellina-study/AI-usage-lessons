---
id: s30b
type: failure_case_double_optic
duration_min: 2.2
assertion: "Май 2022: John Deere remote-brick 27 единиц в Мелитополе ($5M) — anti-theft success. Январь 2025: FTC v. Deere — десятилетние ограничения ремонта. Декабрь 2025: FCC ban DJI (80% US ag-drones). Один механизм, две стороны: AI security feature сегодня = AI control surface завтра."
learning_goal: "AP6 + двойная оптика как stand-alone framework"
learning_outcomes: [LO5]
chapter_ref: "§5.2 Часть 3 — Привязка к поставщику + Мелитополь + FTC + FCC"
references: [register-2022-05-deere, ftc-2025-01-deere, north-dakota-monitor-2025-fcc-dji]
visual:
  pattern: schema_double_optic
  primary: "Двойная оптика 2-col comparison: Side A anti-theft (CNN фото трактора Мелитополь) / Side B vendor control (The Register фото + DJI Agras T40 официальное фото) — реальные изображения, не родовой FPV-дрон"
---

# Привязка к поставщику — двойная оптика John Deere

## Assertion

Май 2022: John Deere remote-brick 27 единиц в Мелитополе ($5M) — anti-theft success. Январь 2025: FTC v. Deere — десятилетние ограничения ремонта. Декабрь 2025: FCC ban DJI (80% US ag-drones). Один механизм, две стороны: AI security feature сегодня = AI control surface завтра.

## Visual

В центре сверху — diagram «двойной оптики». Один центральный mechanism box: **«Geo-locking + VIN-locking»**. От него — две стрелки в две стороны:

**Side A (←):** **anti-theft success** (с точки зрения собственника) — Mr/Mrs. Ukrainian farmer ★ + photo (Deere green tractor)
**Side B (→):** **vendor control surface** (с точки зрения зависимого) — фермер РФ / FieldView пользователь ★ + photo (закрытый FieldView dashboard)

Над diagram — caption: «**Один механизм. Две стороны. Видимы с разных позиций**».

Под diagram — 3 horizontal timeline events в Ocean rounded boxes:

**Event 1 — Май 2022: Мелитополь** (реальное новостное фото John Deere трактора в Украине, CNN 2022-05-01):
- John Deere remote-brick 27 единиц техники
- Перевезены из Мелитополя в Чечню (~1126 км)
- **$5 миллионов** market value, не запустилось
- Anti-theft AI сработал по дизайну (Side A)

**Event 2 — Январь 2025: FTC v. Deere** (реальное новостное фото рядa тракторов Deere, The Register 2025-01-15):
- FTC + AG Illinois + AG Minnesota
- Десятилетние ограничения ремонта
- Только Deere-authorized dealers имеют **Service ADVISOR** software tool
- Trial 2026 (vendor control surface — Side B)

**Event 3 — Декабрь 2025: FCC ban DJI** (официальное фото DJI Agras T40, dji.com):
- 22 декабря 2025: foreign-made drones в Covered List
- **DJI = 80% US ag-spray drone flights**
- Не-китайские альтернативы (Skydio, Geo-scan) **в 2,5× дороже**
- Vendor lock-in на геополитическом уровне

Bottom callout 14pt italic в Teal-tint box: «**AP6. «AI-driven equipment» = ловушка привязки к поставщику.** Чем больше AI и телематики, тем сильнее vendor control surface. Альтернатива: open-source farming hardware (Farm Hack), право на ремонт, multi-vendor стратегия, mechanical fallback'и».

Footer 12pt italic: «Фото: CNN 2022-05-01; The Register 2025-01-15; dji.com/t40 · Источники: The Register 2022-05-02 (Мелитополь); FTC press 2025-01-15; North Dakota Monitor 2025 (FCC DJI)».

## Speaker notes

Второе условие среды — привязка к поставщику, и здесь парадоксальная двойная оптика, которую нужно понимать целиком.

Январь 2025-го — FTC против John Deere. Пятнадцатого января 2025 года Federal Trade Commission США с генеральными прокурорами Иллинойса и Миннесоты подали иск против Deere за unfair practices — десятилетние ограничения на ремонт оборудования фермерами и независимыми ремонтниками: доступ к инструменту Service ADVISOR, нужному для full-functional repairs, есть только у Deere-authorized dealers. Судья отклонил попытку Deere закрыть дело; trial ожидается во второй половине 2026 года. Фермер не покупает комбайн за пятьсот тысяч долларов с AI-стеком — он лицензирует право его использовать, пока Deere разрешает: тот же паттерн, что у Tesla с FSD subscription, применительно к АПК-технике.

Май 2022-го — remote-brick в Мелитополе. Российские военные изъяли двадцать семь единиц техники John Deere из Мелитополя и перевезли в Чечню, около тысячи ста двадцати шести километров; на месте техника не запустилась — Deere дистанционно «забрикала» все двадцать семь устройств через GPS и VIN-locking. Для воровавших — пять миллионов долларов потерянной market value; для Deere — практическая демонстрация удалённого контроля.

Один и тот же механизм даёт две противоположные интерпретации в зависимости от стороны наблюдения.

Сторона А — anti-theft success. С точки зрения украинской стороны это победа технологии над войной: украденная техника остановлена, ущерб вору пять миллионов, AI-функция сработала по дизайну — легитимный аналог Apple Find My для частной собственности на промышленном уровне.

Сторона Б — vendor control surface. Тот же механизм позволяет Deere дистанционно отключить оборудование любого фермера: не оплатившего подписку, не подписавшего EULA-обновление, попавшего под санкции или в политический разрыв. Российские фермеры после февраля 2022 года получили это на практике: техника у них физически, но облачные сервисы, обновления прошивки и Service ADVISOR недоступны. Climate FieldView вышел из РФ в 2022 году вместе с Bayer Crop Science — агрохолдинги, инвестировавшие в платформу, потеряли доступ; Microsoft и Amazon ушли тем же годом.

AI security feature сегодня — это AI control surface завтра: тот же механизм, что не дал комбайну работать в Чечне, становится тревогой для любого фермера в юрисдикции, попавшей в политический разрыв. Право собственности становится фиктивным — фермер лицензирует использование, а не владеет техникой с AI-стеком. Российский опыт после 2022 года — естественный эксперимент, применимый к любому фермеру на периферии, не только к России.

Декабрь 2025-го — FCC ban DJI и Autel. Двадцать второго декабря FCC внесла foreign-made drones и UAS-критические компоненты в Covered List, запретив новые product authorizations. DJI — восемьдесят процентов ag-spray drone flights в США, китайские дроны в целом — около девяноста процентов рынка; в 2024 году спрей-дронами обработано десять и три десятых миллиона акров, около двухсот пятнадцати миллионов выручки custom applications. Не-китайские альтернативы — Skydio, Geo-scan — в среднем в два с половиной раза дороже: та же привязка к поставщику, но на геополитическом уровне.

Главный анти-ИИ критерий — AP-шесть: AI-driven equipment — ловушка привязки к поставщику. Альтернатива: open-source farming hardware (Farm Hack, Open Source Ecology), право на ремонт, multi-vendor стратегия с явной exit-route, mechanical fallback — готовность работать без AI-функций при их отключении.

## Источники

- The Register (2022-05-02) — John Deere disables Ukraine tractors.
- FTC press release (2025-01-15) — FTC v. Deere.
- North Dakota Monitor (2025) — FCC ban DJI ag-drones.
- CSO Online 572811 — Мелитополь analysis.

Изображения (подключены в Фазе 3 вместо родового фото FPV-дрона — K-2 fix):
- CNN (2022-05-01) — «Russian troops in Melitopol plunder $5M farm vehicles from Ukraine» (новостное фото John Deere трактора).
- The Register (2025-01-15) — «Oh, Deere! FTC sues tractor maker» (новостное фото ряда тракторов Deere).
- dji.com/t40/specs — официальное фото DJI Agras T40 (страница продукта).
