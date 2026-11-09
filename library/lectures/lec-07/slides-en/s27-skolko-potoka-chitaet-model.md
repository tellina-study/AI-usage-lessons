---
# КАДР ПЕРЕСОБРАН ПОД ЗАКАЗ ВЛАДЕЛЬЦА (круг 6, 2026-10-19): «хотя бы к одинаковым
# пропорциям сведи… достаточно просто показать общее количество и подтверждённая
# доля с ИИ и всё». Было: три панели на трёх разных основаниях счёта (млн
# исследований · доля трастов · кумулятивная доля одобрений за 30 лет) — каждая
# верна, вместе нечитаемы. Стало: один вопрос, одна ось, знаменатель числом под
# каждым столбцом. Диаграмма — `make_chart_s27.py`, там же записано, почему США
# на оси нет и почему оценка «четверть» на ось не идёт.
# ПОБОЧНАЯ ПОЧИНКА, НАЙДЕННАЯ ЭТИМ ЖЕ КРУГОМ: прежний `chapter_ref` кадра
# («§ Диагностическая визуализация… между §2.4 и §2.6») указывал на подраздел
# главы, КОТОРОГО НЕ СУЩЕСТВУЕТ — страновой блок жил только в деке. Теперь он
# написан в главе (§2.5а), и кадр выводится из него, а не из самого себя.
# Прежний `source` вёл на файл этого же репозитория — прямой запрет §11.5.
id: s27
local_id: s2-05
section: "2. Инструментальная и лабораторная диагностика"
type: analitika
title: "How much of the stream the model reads: one basis for three countries"
assertion: "Из ста снимков грудной клетки модель читает 55 в московском профилактическом потоке и 34 в Англии — но у английской доли два официальных знаменателя, 8,19 и 7 миллионов, и с ними она 34 или 40; у США числа этого вида нет вовсе, и похожие на него 34 процента там — доля врачей, а не снимков"
source: "Vasilyev et al., Digital Diagnostics 2025;6(1):5–22 — https://doi.org/10.17816/DD641703 · NHS England, Diagnostic Imaging Dataset 2023/24 — https://www.england.nhs.uk/rightcare/wp-content/uploads/sites/2/2024/11/DID-Annual-Statistical-Release-2023-24.pdf · UK government announcement — https://www.gov.uk/government/news/ai-to-speed-up-cancer-diagnosis-for-millions-of-nhs-patients"
media: "rework/deck/assets/s27-dolya-potoka-cherez-model.png"
media_needed: ""
media_note: "диаграмма собрана `make_chart_s27.py`, одна ось, знаменатель второй строкой под каждым столбцом. ПРОСМОТРЕНО ГЛАЗАМИ после сборки дважды: на первом прогоне подпись английского столбца обрезалась слева и числитель «2,8» пропадал («из 8,19 млн»), на втором дробный переводчик печатал «54,80» и ось «0,00 10,00». Обе правки внесены, третий прогон чист"
pol_slov: 145   # ПЕРЕМЕРЕН (#293, Этап B): кадр получил строку-мост («годность каждого снимка решил человек у прибора — теперь о самом потоке») после снятия кадра между ним и классическим режимом. 141 слово замером по собранному PDF + запас 4. ПРЕЖНЯЯ ПРИЧИНА ПОЛА: замер по собранному sec-2.pdf, круг 6: обзор по странам: два столбца с знаменателями + три видимые строки, в каждой свой знаменатель
timing_min: 1.1
in_bucket: false
method_steps: ["обзор по странам"]
form: []
vizforma: "один ряд столбцов, одна ось"
vfy: true
status: собран
---

## Visible slide text

**Gradability of every image was decided by a human at the machine — now about the stream itself.** There is one question: out of a hundred chest images taken in a country, how many did the model read. Any other comparison of countries here is a splicing of samples.

**The English share has two official denominators.** The numerator, 2.8 million, is stated by the developer. Health-service statistics give 8.19 million X-rays — which works out to 34 out of 100; the government's own announcement names "over 7 million" — the same 2.8 million gives 40 out of 100.

**The US has no figure of this kind at all.** What gets published is the share of products in the registry (76.5 of 1,430 over thirty years) and the share of physicians using the model (34 by survey). The second looks like the English figure down to matching digits, and measures something else.

## Speaker notes

This slide's question is framed so it can be answered with one kind of number, and the basis was not chosen for convenience. Out of every hundred chest images taken in a country, how many did a trained model read. Any other way of comparing countries on this question turns into a splicing of samples — exactly the error this whole section teaches you to catch, and it would be odd to commit it on the slide that leads into the breakdowns.

Moscow, preventive stream: fifty-five out of a hundred. More precisely — 54.8 percent: the model received 575,549 preventive chest images over five months of 2024 and classified 315,491 of them as normal, after which not a single human read them. This is a share on a named sample, with a published method and a named trigger threshold. The breakdown of this case itself follows on the next slide, and the number comes from there.

England, chest X-ray: thirty-four out of a hundred. The numerator here is 2.8 million images a year, the same number that opened the evening; back then it stood alone, filling the whole screen, and I said it was volume and only volume. Now we are dividing it, and this is worth pausing on, because the share depends on the denominator more than it sounds like it should. That 2.8 million itself is the tool developer's own words, not the state's. The denominator comes not from them but from the health service's official statistics: in the year to March 2024, England performed 8,194,405 chest X-rays across all referral types. Division gives 34 out of 100.

But the government's own announcement about this same deployment, in the same release, names its own denominator — over seven million chest X-rays a year. With that, the same numerator gives forty out of 100. Two official denominators for one question, a gap of more than a million images, a six-point spread in the share. This is stated here out loud, rather than one of the two being silently picked: a slide that teaches you to read the denominator has no right to hide its own.

It is worth naming separately who states which number, because these are different grades of evidence. The 2.8 million numerator comes from an interested party. The government does not give a numerator at all: it states the share of trusts — the tool runs in half of England's NHS trusts — and a count of people, four million, who got a faster diagnosis or had suspicion cleared faster. The share of trusts and the share of images do not have to match: a trust can be connected and still send through only a small part of its own stream.

Now the US, and here the slide carries not a number but a gap, named in words. The US does not publish a share of images read by a model. What gets published is something else: a cumulative 1,430 authorizations of products with a trained model, as of the end of 2025, 76.5 percent of them in radiology. This is a share of products in the authorization registry over thirty years, not a share of the annual stream.

There is a second American number, and the temptation to place it alongside is strong exactly because it looks alike: in a survey by a professional radiologists' association, thirty-four percent of physicians surveyed use a model in practice. It cannot stand next to the English thirty-four out of a hundred images — there it is a share of images, here a share of physicians. A physician using a model might run only one image in twenty through it. Putting these two numbers on one axis would mean committing a denominator swap right on the slide, and the matching first two digits would make it invisible.

And what remains for Russia as a whole, beyond the Moscow sample. Moscow services interpret 1.4 million studies a month, about eighty percent of them coming in from the regions; cumulatively, over eighteen million studies, 75 regions, around two and a half thousand medical organizations. The mayor's office estimates this stream at a quarter of all images performed in Russia. Nobody publishes a denominator for this estimate — neither a national annual image count, nor the rule by which anything gets included in it. That is why it is not placed on the axis: the axis carries only what has a denominator named as a number.

Three grades of evidence on one slide, and they cannot be read as one row. The Moscow share is a peer-reviewed prospective study with a published sample. The English one has a numerator from an interested party, a denominator from government statistics, and the government itself provides a second one. The "quarter" estimate is an official's statement with no denominator at all.

The breakdowns follow next, and the first two of them are domestic: one about how, on this very Moscow stream, the model was sent to work without a human; the second, about a task in the same city where it was not allowed to work without one.

**Sources.** [Vasilyev et al., *Digital Diagnostics* 2025;6(1):5–22](https://doi.org/10.17816/DD641703) · [NHS England, Diagnostic Imaging Dataset 2023/24, table 6](https://www.england.nhs.uk/rightcare/wp-content/uploads/sites/2/2024/11/DID-Annual-Statistical-Release-2023-24.pdf) · [UK government announcement, June 10, 2026](https://www.gov.uk/government/news/ai-to-speed-up-cancer-diagnosis-for-millions-of-nhs-patients)
