---
id: s22
type: assertion_visual
duration_min: 1.5
assertion: "«Supervised machine learning doesn't live up to the hype. Sim-to-real has very real limits.» — Стефан Зельц-Аксмахер, март 2020."
learning_goal: "Honest first-person post-mortem"
learning_outcomes: [LO2]
chapter_ref: "§2.5 — Starsky lesson"
failure_bucket: strict_in
references: [seltz-axmacher-starsky-essay]
visual:
  pattern: quote_centerpiece
  primary: "Большая цитата с атрибуцией + контекст компании + 3 урока"
---

# Старски — первый, кто публично признал гэп

## Цитата

> «Supervised machine learning doesn't live up to the hype. Sim-to-real has very real limits.»
>
> — Стефан Зельц-Аксмахер, основатель и CEO Starsky Robotics, Medium essay «The end of Starsky Robotics», март 2020.

## Контекст

- **Starsky Robotics** — autonomous trucking стартап, основан в 2015 году.
- **Март 2020** — закрытие компании, **~$200M сожжено**.
- **Зельц-Аксмахер написал откровенное эссе** на Medium как post-mortem.
- **Первая волна жертв** autonomous trucking — за 2 года до Argo, за 3 года до Embark и TuSimple.

## Три урока из эссе

- **«Supervised ML не оправдывает ожиданий».** ML-стеки выглядели хорошо в demo, но edge-cases не масштабировались. Каждый новый edge-case требовал новых labeled данных, а получить эти данные требовало миллионов км public roads, что требовало денег, которых не было.
- **«Sim-to-real имеет реальные пределы».** Симуляция полезна, но не покрывает long-tail. ML-модель, обученная только на симулированных сценариях, плохо обобщает на public roads.
- **«Большие deal'ы с большими flotами не материализуются на pre-revenue scale».** Грузоперевозчики — консервативный customer, и они не покупают untested стек прежде, чем увидят production-history.

## Pedagogical point

Стефан Зельц-Аксмахер — это **first-wave casualty с honest first-person post-mortem**. Это редкий тип источника, потому что большинство founder'ов закрывают компании без публичных post-mortems. Когда вы видите такое эссе — читайте внимательно, это самый ценный источник о failure modes индустрии.

## Speaker notes

Этот слайд — короткая остановка на одной цитате, которая, на мой взгляд, лучше всего обобщает уроки autonomous-trucking failures 2020-2024 годов.

Стефан Зельц-Аксмахер был основателем и CEO Starsky Robotics, autonomous-trucking стартапа, основанного в 2015 году. К марту 2020 компания закрылась, сожгла примерно двести миллионов долларов capital. И Зельц-Аксмахер написал откровенное эссе на Medium под названием «The end of Starsky Robotics» как post-mortem.

Главная цитата. «Supervised machine learning doesn't live up to the hype. Sim-to-real has very real limits». Supervised машинное обучение не оправдывает ожиданий. Sim-to-real имеет реальные пределы.

Контекст. Старски была первой волной жертв. За два года до Argo, за три года до Embark и TuSimple. И Зельц-Аксмахер был первым, кто публично, на собственном имени, открыто признал технический гэп. До этого индустрия рассказывала, что вот-вот, через год-полтора, всё заработает.

Три урока из эссе. Первый — supervised ML не оправдывает ожиданий. ML-стеки выглядели хорошо в demo, но edge-cases не масштабировались. Каждый новый edge-case требовал новых labeled данных. А получить эти данные требовало миллионов километров public roads, что требовало денег, которых на pre-revenue scale нет.

Второй — sim-to-real имеет реальные пределы. Симуляция полезна для определённых классов задач, но она не покрывает long-tail. ML-модель, обученная только на симулированных сценариях, плохо обобщает на public roads.

Третий — большие deal'ы с большими floтами не материализуются на pre-revenue scale. Грузоперевозчики — это консервативный customer. Они не покупают untested стек прежде, чем увидят production-history.

Pedagogical point. Зельц-Аксмахер — это first-wave casualty с honest first-person post-mortem. Это редкий тип источника, потому что большинство founder'ов закрывают компании без публичных post-mortems. Когда вы — будущие инженеры — видите такое эссе — читайте внимательно. Это самый ценный тип источника о failure modes индустрии. Я рекомендую вам, после лекции, найти и прочитать «The end of Starsky Robotics» полностью. Это short read — около десяти-пятнадцати минут — и он даст вам интуицию об одной из главных причин, почему вся первая волна autonomous-trucking стартапов провалилась.
