---
id: s17
type: assertion_visual
duration_min: 3
assertion: "За 4 года: Argo Oct 2022, Embark Mar 2023, TuSimple Jan 2024, Waymo Via 2023, Starsky Mar 2020. Серия катастроф для AV-trucking."
learning_goal: "AV-bankruptcy timeline — 5 точек на одной линии"
learning_outcomes: [LO2]
chapter_ref: "§2.5 — Failure deep-dive"
failure_bucket: strict_in
references: [cnbc-argo-shutdown, techcrunch-embark-layoffs, sec-tusimple-13d]
visual:
  pattern: schema_timeline
  primary: "Горизонтальная timeline 2020-2024 с 5 точками — каждая событие + сожжённый капитал"
  acquisition_tiers: []
---

# AV-trucking bankruptcy timeline 2020-2024

## Пять точек на одной линии

- **Март 2020 — Starsky Robotics.** Первая волна жертв. Stefan Seltz-Axmacher Medium essay «The end of Starsky Robotics».
- **Октябрь 2022 — Argo AI.** Ford + VW pull funding одновременно. **~$7 миллиардов сожжено** за 5 лет; **Ford $2,7B impairment**; $827M net loss. 2 000+ увольнений.
- **Март 2023 — Embark Trucks.** 16 месяцев от SPAC IPO (ноябрь 2021) до банкротства. 230 employees layoff, asset liquidation. SPAC target market cap был $5,16 миллиарда.
- **2023 — Waymo Via.** Alphabet закрыла собственное trucking-направление. Даже бесконечный capital не нашёл profitable model.
- **Январь 2024 — TuSimple.** Nasdaq delisting; asset transfer в Chinese AIGC entities. **91%+ shareholder value lost**.

## Common patterns

- **Capital intensity без revenue.** Все non-survivors сжигали $1-7 миллиардов прежде, чем заработать первый коммерческий доллар.
- **SPAC IPO bubble 2021-2022.** Embark, TuSimple (более ранний), Aurora — все вышли через SPAC merger. Большинство не выжили public-market scrutiny.
- **Sim-to-real gap.** ML-стеки выглядели хорошо в симуляции, но не масштабировались на public roads с edge-cases.
- **Регуляторная неопределённость.** NHTSA SGO + state-level патчворк сложно навигировать без established legal team.
- **Misaligned customer demand.** Большинство стартапов искали продать «autonomous fleet» больших перевозчиков; перевозчики предпочитали dedicated lanes + safety operator, не полную автономию.

## Speaker notes

Failure deep-dive раздела два. Я хочу провести по пяти точкам на одной timeline, чтобы вы видели не отдельные кейсы, а паттерн.

Март 2020. Starsky Robotics — первая волна жертв autonomous trucking. Stefan Seltz-Axmacher, основатель и CEO, написал откровенное Medium-эссе «The end of Starsky Robotics». Главная цитата: «Supervised machine learning doesn't live up to the hype». И второе: «Sim-to-real has very real limits». Это важно — это first-person admission от founder, что ML не работает на public roads так, как работал в симуляции. Starsky первой попробовала и первой провалилась.

Октябрь 2022. Argo AI. Этот провал — самый крупный по абсолютным числам. Семь миллиардов долларов сожжено за пять лет. Из них Ford инвестировала более пяти миллиардов, VW — два с шестью десятых. Двадцать шестого октября 2022 года в earnings call Ford объявил решение свернуть Argo. Двадцать тысяч человек увольнений. Ford записал два миллиарда семьсот импейрмента и восемьсот двадцать семь миллионов чистого убытка только за этот квартал. Lesson — даже когда у вас два OEM-инвестора (Ford и VW) с почти бесконечным capital, если они одновременно решат, что L4 robotaxi everywhere — слишком big для startup-scale, проект мгновенно разваливается.

Март 2023. Embark Trucks. Шестнадцать месяцев от SPAC IPO в ноябре 2021 до банкротства в марте 2023. SPAC target market cap был пять и шестнадцать сотых миллиарда долларов — на момент merger Embark формально стоила больше, чем десятилетние профессиональные операторы. К марту 2023 — двести тридцать employees layoff, asset liquidation. Цитата Алекса Родригеса, CEO: «Капитальные рынки повернулись спиной к pre-revenue компаниям, так как сдвиги в timelines производителей задержали возможность scaled commercial deployment». Это canonical SPAC-bust 2021-2023 в одной компании.

2023. Waymo Via. Alphabet закрыла собственное trucking-направление. Это уникально, потому что у Alphabet практически бесконечный capital. Если даже Alphabet не нашёл profitable model для L4-trucking в отдельной business unit — это структурный сигнал, что вся индустрия не работает по unit economics, по крайней мере на эту дату.

Январь 2024. TuSimple. Nasdaq delisting; asset transfer в китайские AIGC entities. Девяносто один процент+ shareholder value lost. TuSimple — это была US-China hybrid компания, и её ситуация дополнительно осложнялась геополитическим давлением — US-side blocked технологический трансфер в Китай в 2023 году, а Китай-side активы выкупались независимо.

Общие паттерны. Capital intensity без revenue. Все non-survivors сжигали один-семь миллиардов прежде, чем заработать первый коммерческий доллар. SPAC IPO bubble 2021-2022. Sim-to-real gap. Регуляторная неопределённость. Misaligned customer demand — большинство стартапов искали продать «автономный флот» большим перевозчикам, но перевозчики предпочитали dedicated lanes плюс safety operator, не полную автономию.

Survivor consolidation 10:1. Из тридцати+ серьёзных AV-trucking стартапов 2015-2020 выжили три-четыре. Это не вопрос technical quality — Argo и Embark имели технически compelling demos. Это вопрос business model в capital-intensive, slow, brutally Darwinian рынке.
