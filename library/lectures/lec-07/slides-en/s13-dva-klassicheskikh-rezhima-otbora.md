---
id: s13
local_id: s1-03
section: "1. Первичный скрининг и отбор на обследование"
type: norm
title: "Example 1, without a model: a Swedish program calls people in by age"
assertion: "Шведский скрининг без модели посчитан в людях: на 1000 обследованных нашли 5,1 случая, 1,76 пропустили до следующего приглашения, 2,0 из ста вернули на второй снимок; второй порядок — ждать жалобу — даёт поздние стадии у 57 из ста найденных против 39 у приглашённых; цена обеих ошибок и порог назначены раньше, чем кто-нибудь измерил точность прибора"
source: "Swedish program, control arm — https://doi.org/10.1016/S0140-6736%2825%2902464-X · the Malmö trial"
media: ""
media_needed: "настоящий снимок страницы национальной программы скрининга, где назначены возраст и интервал приглашения"
media_note: "свидетельство, а не оформление — порог как документ. Кадр сложен из двух: прежние «режим первый» и «режим второй» стояли по кадру на режим и оставляли четверть экрана пустой"
blocks:
  - {label: "Found at the examination", value: "5.1 per 1,000", note: "Sweden, 80,033 women, double reading"}
  - {label: "Missed by the program, found by a symptom", value: "1.76 per 1,000 over two years", note: "control arm, 52,872 women", key: true}
  - {label: "Called in for nothing: a second image", value: "2.0 out of a hundred", note: "repeat image, sometimes a biopsy"}
  - {label: "Waiting for a complaint: late stage among those found", value: "57 → 39 out of a hundred", note: "Malmö, 1976–1986, invitation by randomization"}
pol_slov: 148   # ПЕРЕМЕРЕН (#293, Этап B): кадр получил одну строку-мост с предыдущего («назначены тем же решением, которым назначено, быть ли программе вообще») после снятия исторического кадра между ними. 148 слов замером по собранному PDF + запас 4. ПРЕЖНЯЯ ПРИЧИНА ПОЛА: #229 п.14 (владелец: «пояснить, о чём речь — шведский скрининг без ИИ и с ИИ, так и написать… показать два режима в сравнимых числах: зовём периодически → столько обследований, столько заболеваний, такие исходы; по жалобе → столько-то, последствия серьёзнее… в метриках, сравнимых с ИИ-кейсом дальше»). Чем заняты слова: ЧЕТЫРЕ ПЛАШКИ в человеко-центричных единицах — нашли 5,1 на 1000 (80 033 женщины, chapter-part1b.md:124) · пропустила программа, нашёл симптом 1,76 на 1000 за два года (52 872, :97) · позвали зря 2,0 из ста (:97) · поздняя стадия у 57 из ста найденных против 39 (Мальмё, :101). ТРИ ПЕРВЫЕ СТОЯТ В ТЕХ ЖЕ ЕДИНИЦАХ, в которых на s15 пойдёт то же плечо с моделью (5,1 → 6,1 и 2,0 → 2,2) — это и есть заказанная сравнимость. Пропуск перестал быть плашкой без числа: «счёт в разделе о диагнозе» снято, число названо здесь, а пара 1,76 → 1,55 с оговоркой о значимости остаётся на s47. Плюс тело: оба порядка названы работой людей (кто шлёт приглашение, кто читает, кто разбирает расхождение), отказ второго порядка от нуля назван на месте, порог-документ и строка «два числа с разных программ и эпох — две стороны цены, а не одна шкала» ЗАМЕР ПО СОБРАННОМУ PDF полосы Входа и раздела 1 (render_sec.py 0 1, 2026-10-15, 14 страниц): 216 слов на этом кадре; медиана полосы 142,5, максимум 263, блокирующих 0. Поле выставлено ПО ЗАМЕРУ, не по оценке: прежнее число в этой строке называло состав до правки по замечаниям владельца и после неё было бы разрешением на чужой вес.
timing_min: 0.85
in_bucket: false
method_steps: ["①цена ошибки", "②классические режимы"]
form: []
vfy: true
status: собран
---

## Visible slide text

**Everyone is called in by age and interval.** The program sends the invitation, two people read the scan, a third resolves a disagreement. There's no model here.

**Waiting for a complaint is the second order of work, and it's more widespread.** It doesn't work at zero: the uninvited will come in on their own, later and at a bigger stage.

**The threshold is a document:** age and interval are set before anyone ever measures a device's accuracy — and set by the same decision that decides whether the program exists at all.

**The woman with the letter was called in by the first order: only her year of birth, none of her own traits.**

## Speaker notes

The Swedish program calls everyone in for a mammogram by age and interval: the program sends the invitation, two people read the scan, a third resolves a disagreement. There's no model here at all, and the program is counted in people — out of a thousand examined, 5.1 cases were found, 1.76 were missed until the next invitation, and 2.0 out of a hundred were called back for a second scan. The threshold inside the program is set by the same decision that sets its existence: whom to call in, from what age, and how often. In other words, both the program and its threshold come from the same place — a document, not a device.

And one historical foundation under this. The question of when screening is justified at all was formalized by the World Health Organization in 1968: James Wilson and Gunnar Jungner laid out ten criteria that still hold today. The disease must have a recognizable early stage; a recognized treatment must exist, with the capacity to deliver it; the test must be acceptable to the population; the screening itself must be an ongoing process, not a one-off campaign. Not one of these ten criteria mentions an algorithm's accuracy — all ten were written decades before the first trained model. This is the lesson that holds the whole evening together: the question "is screening justified" doesn't reduce to the question "how accurate is the model inside it," and the first was posed and settled long before the second. As for where the idea of examining a person with no complaints even comes from: in the 1920s in the US, there was about one doctor for every eight hundred people, and there was physically nothing to examine everyone with; that hidden disease exists in a huge share of people who look healthy was shown by the draft boards of two world wars — forty-seven out of more than two million conscripted into the First World War were found to have a diagnosis never made before; and the first organized program for an entire city was the mass chest-X-ray campaign in Glasgow in the spring of 1957, seven hundred fifteen thousand people in five weeks, seventy-six out of a hundred adults in the city.

The threshold for intervention is a document. The age at which people are called in. The interval between invitations. The criterion by which a person is recalled for further testing. All of this is written into a health-authority document, and written long before anyone measures any device's accuracy. The model's developer doesn't set the threshold; the doctor at the monitor doesn't set the threshold; it's set by whoever decided what's worse — missing something or calling in someone unnecessarily. That's where the breakdown of any case starts: until the cost of both errors is named, no accuracy figure reads as anything.

The cost of a miss, in the first regime, is counted as the share of cancer found between two invitations: the program didn't catch it, a symptom did. The unit is honest, because it's counted on the same people the program examined — one and seventy-six hundredths of a case per thousand examined, over two years of follow-up. This figure has a second half — the same figure in the model arm — and it's presented where the reading of the scan is examined, together with the caveat about significance: without it, the improvement reads stronger than it's actually measured.

The cost of a false alarm is two people out of a hundred examined called back. Behind that sits a repeat scan, sometimes a biopsy, and a few weeks the person spends living with an open question. The last part doesn't make it into the reports, and it's a cost too — paid not by the program and not by the vendor, but by whoever was called in.

These figures share one base, and it has to be named along with them: the control group of the Swedish randomized screening program, fifty-two thousand eight hundred seventy-two women, double reading with no model at all, two years of follow-up. How much this order of work finds: five point one cases per thousand examined — this figure is counted on a different, smaller sample from the same program, eighty thousand thirty-three randomized women, and it's labeled with that sample on the slide separately. Further on, on the slide with the model, both of these figures will appear in the same units, and the comparison can be made directly. Assignment to groups is random, outcomes are written down in advance — nothing in this lecture will be stronger than this, and that's exactly why the control group works as a reference point for everything else.

The second classical regime is doing nothing and waiting for the person to come in on their own. It's harder to count than the first, because it doesn't work at zero: whoever wasn't called in will still show up eventually — later, and at a different stage. So the comparison has to be not "found or not found" but "when found." The one time this regime was measured by random assignment was when screening was first being introduced. The Malmö trial enrolled participants from the mid-1970s to the mid-1980s and randomly assigned the invitation: the two groups differed by exactly one thing — whether the person was called in or not. The share of stage II and higher among the cases found was ninety-one out of a hundred fifty-nine in the uninvited group — fifty-seven out of a hundred — against sixty-two out of a hundred sixty in the invited group, that is, thirty-nine out of a hundred.

A caveat, without which this second figure shouldn't be used. The trial ran nearly half a century ago: a different device, different treatment, a different era. This is a measurement of the regime, not of the equipment's properties, and it can't be transferred to today's technology. It can't be combined with the Swedish program's figures either: two different programs, two different eras, and together they give exactly one thing — two sides of a price set before any model at all. A trial like this can't be run today at all, because a program doesn't get suspended for the sake of a measurement. Replication: by direction of the effect — many times over, by different programs in different countries; by magnitude — no, and the magnitude depends heavily on the era.

The main thing worth taking from this slide: both prices and both regimes are set and counted before any model and with no model at all. When someone later says "the system reduces the number of misses by such-and-such percent," the first question won't be about the percent — it'll be about which of the two costs this system was supposed to reduce, who decided that, and exactly which "before" it was compared against.

The woman who got the letter fell entirely under the first regime. There isn't a single trait of her own in the decision to call her in: no complaint, no finding, no family history — only her year of birth and the interval, written into a document. From here, the lecture will track what the model does with her case; the first decision about her was made without her and before any model existed.

Two caveats, cut from the slide but required to be said out loud. First: the two regime figures come from different programs and different eras — together they give not a sum, but two sides of a price set before any model. Second: the share of late stages among cases found doesn't depend on how many cases were found — only on when they were found; that's exactly why it's suited to comparing two orders of work, whereas "how many were found" would simultaneously compare coverage, program power, and group size.

What to ask a vendor right on this slide: they say they're comparing "against how it was before" — ask exactly which "before" they counted.

The plates' units are stated in full: a false recall is two people out of a hundred examined, called back in the control arm of the Swedish program, where the scan was read by two people with no model at all and follow-up ran two years. Late stages are the share of stage II and higher among cases found in the Malmö trial, which assigned the invitation at random.

**Sources.** [MASAI safety analysis, Lancet Oncology 2023](https://doi.org/10.1016/S1470-2045%2823%2900298-X) · [MASAI final analysis, The Lancet 2026](https://doi.org/10.1016/S0140-6736%2825%2902464-X)
