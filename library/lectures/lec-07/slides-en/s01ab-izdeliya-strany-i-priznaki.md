---
# ВОЗВРАЩЁН ПЕРЕРАБОТАННЫМ — решение владельца 2026-10-22 (#293, Этап E), дословно:
#   «зря потерял статистику по мед изделиям верни, можно как-то переработанно, но там
#   классно показано, что россия в топе».
# Кадр был снят Этапом A вместе со слиянием тройки Входа. Причина снятия записана в
#   `slides/_snyato/README-293.md`: строки странового ряда считаны по РАЗНЫМ признакам
#   новизны, а оговорка-рассуждение об этом на кадре запрещена §7.1 — без неё ряд врёт.
# ЧЕМ ПРИЧИНА СНЯТИЯ ЗАКРЫТА ПРИ ВОЗВРАТЕ. Не оговоркой, а данными: признак отбора встал
#   В ИМЯ СТРОКИ, рядом с полосой («Россия · весь реестр, разбивки нет»). §5.17 требует
#   называть пробел содержательно НА кадре — имя строки это и есть; §7.1 запрещает
#   рассуждение о замере — его здесь нет. Корея стоит двумя строками намеренно: два её
#   собственных признака дают 1,70 и 0,95, и разброс внутри одной страны шире расстояния
#   между половиной стран ряда.
# ИМЯ ФАЙЛА НОВОЕ (прежнее — `s01ab-statistika-dopuska-ii-izdeliy.md`, лежит в `_snyato/`):
#   кадр больше не про пути допуска, они целиком на `s01aa`. Номер `s01ab` тот же —
#   он не переиспользован под другой кадр, а возвращён своему.
# ДВОЙНОЙ СЧЁТ СО СЛИТЫМ `s01aa` РАЗОБРАН. Плашки «1 553 из 1 614» и «21 из 1 614» и
#   строка «3,1 по-настоящему новых изделия в год» при слиянии уехали на `s01aa` и
#   остаются ТАМ: там они отвечают на вопрос «какими путями», и схема трёх порядков
#   стоит рядом с ними. Сюда возвращается то, чего на `s01aa` нет ни одним знаком, —
#   состав массива по специальностям, доля изделий с моделью в потоке допуска с её
#   противофактом, страновой ряд и первые российские изделия.
id: s01ab
local_id: В-01ab
section: "0. Вход"
type: analitika
title: "Devices with a model: composition of the pool and countries"
assertion: "Три четверти всего массива изделий с обученной моделью — радиология (1 230 из 1 614), психиатрии нет ни одного изделия за всю историю; в 2025 году с моделью было каждое десятое новое медизделие США против двух на тысячу в 2015-м, при том что весь поток решений регулятора за те же десять лет вырос всего в 1,07 раза; страновой ряд на миллион населения считан по разным признакам отбора, и признак назван в каждой строке — у Кореи их два (1,70 и 0,95), российская строка считана по всему реестру и даёт 0,39, выше США, Японии и Китая"
source: "Полная запись источников в репозитории курса · счёт по таблице FDA — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/10-II-FDA-PERVICHNYY-SCHET.md · страновой разрез — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/11-dinamika-po-stranam-realno-novye.md · проверка Кореи и Китая — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/13-koreya-kitay-proverka.md"
media: "rework/deck/assets/s01ab-strany-i-priznaki.png"
media_needed: "добыто: собственная аналитика по шаблону `tools/presentation-build/analitika.py`, прогон `rework/deck/make_charts_244.py`"
media_note: "не иллюстрация, а сами данные кадра: шесть строк, у каждой назван свой признак отбора, знаменатель едет с числом у конца полосы. Российская полоса выделена заливкой — она и есть то, ради чего кадр возвращён. Пропорция 4,07 под полосу аналитического кадра во всю ширину; линии накопленного счёта, прежде занимавшие правую половину картинки, сняты — их число живёт строкой тела на `s01aa`"
blocks:
  - {label: "Radiology", value: "1,230 of 1,614", note: "zero in psychiatry across all history"}
  - {label: "New US medical devices, 2025", value: "one in ten", note: "in 2015 — two in a thousand"}
  - {label: "First Russian devices, 2020", value: "2 of 57", note: "no predicates existed, both went through trials", key: true}
timing_min: 0.75
in_bucket: true
method_steps: ["заземление", "счёт с базой"]
form: []
vizforma: "ряды"
vfy: true
status: собран
---

## Visible slide text

**The paths are counted — now the pool itself.** Korea has two selection criteria: 1.70 by innovative-device status, 0.95 by reimbursement. Russia is 0.39 across the whole registry — higher than the US, Japan, and China.

## Speaker notes

In the FDA's list as of 17 October 2026, there are 1,614 devices with AI or machine learning, and this slide breaks down what the pool is made of: by specialty, by share of the flow of new medical devices, and by country. The figures are taken by direct reading of the regulator's own table: industry digests on this subject disagree with each other by hundreds of devices. Every share from here on is counted from 1,614.

The breakdown by specialty explains what "AI in medicine" actually means. Radiology — 1,230 devices, 76.2%. Cardiology — 154, that's 9.5%. Neurology — 73, 4.5%. After that come anesthesiology, gastroenterology, hematology, pathology, ophthalmology, surgery, and clinical chemistry — each with 9 to 30 devices. Psychiatry has not a single device in the list across its entire history. In other words, AI in medicine as of 2026 is predominantly work with images, and the rest of the specialties together don't add up to even a quarter.

Now the share of the flow. The whole pool of AI-enabled devices is growing fast: 6 devices in 2014, 335 in 2025 — meaning one in ten new medical devices in the US in 2025 has AI, against two in a thousand in 2015. Alongside that sits a counterfactual, without which this growth reads wrong: the entire flow of new US medical-device clearance decisions grew only 1.07-fold over ten years — in other words, stayed in place, at about 3,063 decisions in 2015 and about 3,265 in 2025. AI-enabled devices did not replace something else; they were added on top.

Now the country row, and it has to be read row by row, not by the length of the bars. No single international definition of a "truly new device" exists, so each country is counted by its own criterion, and the criterion sits right in the row's name — it is not a caveat, it is part of the data.

Korea: 88 devices out of 549 cumulatively as of Q1 2026, criterion — voluntary innovative-device status, which the regulator assigns itself; against a population of 51.7 million, that comes to 1.70. The second Korean row is the same registry, a different criterion: whether the device has gone through insurance reimbursement. There are 49 of those out of 549, and the rate drops to 0.95. Two honest figures for one country, and the gap between them is bigger than the distance between the US and China in this same row. If the room remembers one thing from this slide, let it be this: it is not medicine that sets the order of the countries here, it is the chosen criterion.

China: 118 of 154 devices went through the company's own clinical trial as the clearance path, and separately for the high-risk class, 116 of 123; against a population of 1,409 million, that is 0.08. Japan: about 14 of 51, and this is an extrapolation of the overall share across all software medical devices onto the part involving AI, not a direct count — which is why the row reads "share recalculated." US: 61 of 1,614 against a population of 342 million — 0.18.

The Russian row stands on a different criterion, and that is stated right on the slide. Roszdravnadzor does not publish a breakdown of how many devices went through trials involving people versus a document-based evaluation, so the numerator holds all 57 registered devices, and against a population of 146 million that gives 0.39. The novelty criterion isn't applied to them — there's nothing to apply it to. What is reliably known: the first two Russian devices, from 2020, Webiomed and Botkin.AI, had no predicate device in the registry, and both went through full clinical trials with patient participation. By 2026, the registry had accumulated more than ten medical-image-analysis products, and for new applications in the same product category, a document-based evidence base already exists. So equating the 57 Russian devices with 57 "truly new" devices in the American sense would be wrong — and that is exactly why the row names its own criterion out loud instead of hiding it in a footnote.

And the reason this row is on the slide at all. Russia sits above the US, Japan, and China on it — that holds under any of the criteria counted here, and it is not a trivial point: in absolute terms it has 57 devices against America's 1,614. But a second thing also holds: its row is the only one to which the novelty criterion is not applied at all. Both statements live on the same slide, and neither cancels the other.

**Sources.** [FDA, AI/ML-Enabled Medical Devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices) · [Korea, cumulative count of 549, industry digest](https://www.etnews.com/20260410000195) · [Korea, reimbursement 49 of 549](https://www.dataeconomy.co.kr/news/articleView.html?idxno=42899) · [China, clinical evaluation pathways, JMIR Medical Informatics 2026](https://medinform.jmir.org/2026/1/e85538) · [Japan, final report on AI-based software medical devices](https://www.jfmda.gr.jp/wp/wp-content/uploads/2026/01/Final-Study-Report-for-Review-of-SaMD-utilizing-AI_English.pdf) · [Webiomed, first Russian AI-enabled device](https://webiomed.ru/novosti/sistema-webiomed-stala-pervoi-rossiiskoi-razrabotkoi-v-oblasti-iskusstvennogo-intellekta/)
