---
id: s25
type: failure_case
duration_min: 2
assertion: "MethaneSAT измерил ~15 Mt/год; EPA inventory ~4 Mt/год — фактор разрыва 4×. Stanford 2024 aerial: ~7 Mt = фактор 2. Это structural methodological gap, не «AI ошибается»."
learning_goal: "Failure 2 Q2 + 4× discrepancy crisis"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part3.md]
  sections: ["§3.5 4× discrepancy: industry vs регулятор"]
visual:
  type: chart
  description: "Horizontal bar chart: MethaneSAT 15 Mt | Stanford aerial 7 Mt | EPA inventory 4 Mt — все на one axis, factor labels"
  acquisition_tier: self_render
visible_numbers: ["MethaneSAT 15 Mt vs EPA 4 Mt = 4×", "Stanford 2024: 7 Mt = 2×", "9-satellite test: 58% identified, 41 false negatives"]
russification_check: "MethaneSAT, EPA, Stanford, Bridger Photonics, BC LDAR, Atmospheric Measurement Techniques, Copernicus, Nature — brand list; «эталонная разметка», «межотраслевая триангуляция» — RU."
speaker_notes_target_words: 230
---

# 4× discrepancy: MethaneSAT 15 Mt vs EPA 4 Mt. Structural gap, не AI ошибается.

## Visible content

Заголовок: «4× разрыв industry vs регулятор — structural methodological gap» (28pt deep ocean).
Sub: «MethaneSAT measured ~15 Mt/год US O&G. EPA Inventory ~4 Mt. Stanford 2024 aerial ~7 Mt = factor 2.» (16pt italic)

**Слева — horizontal bar chart (Ocean motif):**

| Источник | Mt/год | Factor vs EPA |
|---|---|---|
| **MethaneSAT 2024** | **15 Mt** (gold bar) | **4×** |
| Stanford aerial 2024 (Nature) | 7 Mt | 2× |
| **EPA Inventory** | 4 Mt | baseline 1× |

Под bar — 9-satellite single-blind test 2024 (AMT/Copernicus): **0 false positives, 58% correctly identified, 41 false negatives** на known ground truth.

**Справа — Ocean rounded box «Почему это structural»:**

1. **EPA emission factors** калиброваны 10-20 лет назад → не отражают operational mix современного производства; missing intermittent superemitters.
2. **Satellite vs aerial — разные ответы.** Aerial campaigns ограничены days/weeks; satellite — cloud cover + ветер. **Разные методы → разные ответы.**
3. **No agreed ground truth.** Industry, регулятор, NGO, академия — нет согласованного методологического стандарта.

**Bottom bar (gold tint):**

«**Урок для LO7:** AI MRV — promising technology, но не ready для contract enforcement без cross-validation protocols. EU 2024/1787 требует Level 4/5 = de-facto triangulation. Это engineering necessity, не bureaucracy.»

## Speaker notes

Центральный numerical conflict Раздела 3.

MethaneSAT измерения US oil&gas метан эмиссии — примерно пятнадцать миллионов тонн в год. EPA Inventory официальная оценка — примерно четыре миллиона тонн в год. Фактор разрыва — примерно четыре.

Параллельная Stanford 2024 study, опубликована в Nature в марте 2024 года. Aerial campaign на US O&G basins; результат — более шести миллионов тонн в год, точная цифра в paper около шести-семи с половиной миллионов. Это фактор два outlier от EPA Inventory — не такой большой, как MethaneSAT factor четыре, но всё равно значительный.

Aerial vs OGI на одних и тех же sites. Aerial measurements от Bridger Photonics в четыре раза выше, чем ground OGI на тех же sites — British Columbia LDAR (выявление и устранение утечек) validation study. Ground OGI системно underestimates утечки, потому что OGI inspector проходит сайт за десять-двадцать минут и физически не видит intermittent emissions.

Девятисателлитный single-blind тест 2024 года в Atmospheric Measurement Techniques. Ноль ложные срабатывания — хорошо. Но только пятьдесят восемь процентов correctly identified; сорок один false negative — пропущенных реальных утечек. Даже когда AI MRV хорошо настроена, она пропускает почти половину реальных эмиссий.

Что этот конфликт означает. EPA коэффициенты эмиссии были откалиброваны десять-двадцать лет назад и не отражают реальный operational mix современного нефтегазового производства. MethaneSAT и aerial campaigns показывают, что real-world эмиссии выше — потому что они захватывают intermittent superemitters. Satellite плюс aerial AI detection methods inconsistent друг с другом. Это не «один прав, другой нет» — это methodological calibration difference.

Главное. No agreed эталон. У отрасль, регулятора, NGO, академии — нет согласованного методологического стандарта. Урок: AI MRV — promising, но не ready для контрактное принуждение без протоколы перекрёстной валидации. EU 2024/1787 требует Level 4/5 = триангуляция. Это инженерная необходимость, не избыток bureaucracy.
