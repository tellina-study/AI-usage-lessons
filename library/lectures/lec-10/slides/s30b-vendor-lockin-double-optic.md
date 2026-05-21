---
id: s30b
type: failure_case_double_optic
duration_min: 2.5
assertion: "Май 2022: John Deere remote-brick 27 единиц в Мелитополе ($5M) — anti-theft success. Январь 2025: FTC v. Deere — десятилетние ограничения ремонта. Декабрь 2025: FCC ban DJI (80% US ag-drones). Один механизм, две стороны: AI security feature сегодня = AI control surface завтра."
learning_goal: "AP6 + двойная оптика как stand-alone framework"
learning_outcomes: [LO5]
chapter_ref: "§5.2 Часть 3 — Привязка к поставщику + Мелитополь + FTC + FCC"
references: [register-2022-05-deere, ftc-2025-01-deere, north-dakota-monitor-2025-fcc-dji]
visual:
  pattern: schema_double_optic
  primary: "Двойная оптика center diagram: один механизм geo-locking + VIN-locking → 2 интерпретации (Side A anti-theft / Side B vendor control); + 3 timeline events"
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

**Event 1 — Май 2022: Мелитополь** (фото / map):
- John Deere remote-brick 27 единиц техники
- Перевезены из Мелитополя в Чечню (~1126 км)
- **$5 миллионов** market value, не запустилось
- Anti-theft AI сработал по дизайну (Side A)

**Event 2 — Январь 2025: FTC v. Deere** (фото FTC press conference):
- FTC + AG Illinois + AG Minnesota
- Десятилетние ограничения ремонта
- Только Deere-authorized dealers имеют **Service ADVISOR** software tool
- Trial 2026 (vendor control surface — Side B)

**Event 3 — Декабрь 2025: FCC ban DJI** (icon + press headline):
- 22 декабря 2025: foreign-made drones в Covered List
- **DJI = 80% US ag-spray drone flights**
- Не-китайские альтернативы (Skydio, Geo-scan) **в 2,5× дороже**
- Vendor lock-in на геополитическом уровне

Bottom callout 14pt italic в Teal-tint box: «**AP6. «AI-driven equipment» = ловушка привязки к поставщику.** Чем больше AI и телематики, тем сильнее vendor control surface. Альтернатива: open-source farming hardware (Farm Hack), право на ремонт, multi-vendor стратегия, mechanical fallback'и».

Footer 12pt italic: «Источники: The Register 2022-05-02 (Мелитополь); FTC press 2025-01-15; North Dakota Monitor 2025 (FCC DJI)».

## Speaker notes

Второе условие среды — привязка к поставщику. И здесь мы видим парадоксальную двойную оптику, которую инженер должен понимать целиком.

Январь 2025-го — FTC против John Deere. Пятнадцатого января 2025 года Federal Trade Commission США совместно с генеральными прокурорами штатов Иллинойс и Миннесота подал иск против Deere за unfair practices — десятилетние ограничения способности фермеров и независимых ремонтников чинить оборудование Deere. Только Deere-authorized dealers имеют доступ к программному инструменту Service ADVISOR, который требуется для всех full-functional repairs. Федеральный судья отклонил попытку Deere прекратить дело; trial ожидается во второй половине 2026 года. Что это означает: фермер не «покупает» комбайн стоимостью пятьсот тысяч долларов с AI-стеком — он лицензирует право его использовать, пока Deere разрешает. Это тот же паттерн, что у Tesla с FSD subscription, но применительно к АПК-технике.

Май 2022-го — John Deere remote-brick в Мелитополе. В мае 2022 года российские военные изъяли двадцать семь единиц техники John Deere из Мелитополя в Запорожской области и перевезли в Чечню — около тысячи ста двадцати шести километров. На месте техника не запустилась. Deere дистанционно «забрикала» все двадцать семь устройств через GPS плюс VIN-locking. Для воровавших — пять миллионов долларов потерянной market value. Для Deere — практическая демонстрация удалённого контроля.

И вот здесь — самая методологически-важная этическая мысль раздела. Эту мысль нужно рассматривать как stand-alone framework, а не как примечание в потоке. Один и тот же механизм даёт две противоположные интерпретации в зависимости от стороны наблюдения.

Сторона А — anti-theft success. С точки зрения украинской стороны и общественности — это победа технологии над войной, защита частной собственности. Украденная техника действительно остановлена; ущерб вору пять миллионов. AI-функция сработала по дизайну. Этот сценарий — легитимное anti-theft применение AI и IoT, аналог системы Apple Find My для частной собственности на промышленном уровне.

Сторона Б — vendor control surface. Тот же механизм означает, что Deere может дистанционно отключить оборудование любого фермера: не оплатившего подписку, не подписавшего EULA-обновление, оказавшегося под санкциями, попавшего в политический разрыв. Российские фермеры после февраля 2022 года получили на практике этот сценарий — техника физически у них, но облачные сервисы, обновления прошивки, инструмент Service ADVISOR — недоступны. Climate FieldView вышел из РФ в 2022 году одновременно с уходом Bayer Crop Science; российские агрохолдинги, инвестировавшие в FieldView, потеряли доступ к платформе. Microsoft и Amazon ушли в том же 2022 году.

Урок инженерный. AI security feature сегодня — это AI control surface завтра. Тот же механизм, благодаря которому украденный комбайн не работает в Чечне, является основанием тревоги для каждого фермера в любой юрисдикции, попавшей в политический разрыв. Право собственности на оборудование становится фиктивным — фермер лицензирует право использования, а не владеет техникой со встроенным AI-стеком. Российский опыт после 2022 года — естественный эксперимент, иллюстрирующий, что бывает, когда импортный AI-стек становится недоступен. Это универсальный урок, не специфический для России — он применим к любому фермеру в любой стране периферии.

И декабрь 2025-го — FCC ban на DJI и Autel. Двадцать второго декабря 2025-го FCC добавила все foreign-made drones плюс UAS-критические компоненты в Covered List, запретив новые product authorizations. DJI занимает восемьдесят процентов всех ag-spray drone flights в США; китайские дроны в целом — около девяноста процентов рынка. В 2024 году спрей-дронами обработано десять и три десятых миллиона акров в США, около двухсот пятнадцати миллионов выручки от custom applications. Не-китайские альтернативы — Skydio, Geo-scan — в среднем в два с половиной раза дороже. Эта же логика — привязка к поставщику на геополитическом уровне, отрезающая цепочку поставок не из-за качества AI, а из-за политики.

И главный анти-ИИ критерий — AP-шесть. AI-driven equipment — это ловушка привязки к поставщику. Альтернатива: open-source farming hardware — Farm Hack, Open Source Ecology — право на ремонт, multi-vendor стратегия с явной exit-route, mechanical fallback — то есть готовность работать без AI-функций при их отключении.

## Источники

- The Register (2022-05-02) — John Deere disables Ukraine tractors.
- FTC press release (2025-01-15) — FTC v. Deere.
- North Dakota Monitor (2025) — FCC ban DJI ag-drones.
- CSO Online 572811 — Мелитополь analysis.
