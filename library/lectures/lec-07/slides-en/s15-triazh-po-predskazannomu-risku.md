---
id: s15
local_id: s1-04
section: "1. Первичный скрининг и отбор на обследование"
type: comparison
title: "Example 1, with a model: who gets the second reading"
assertion: "Модель ставит снимку оценку риска и по ней решает, выполнять ли второе человеческое чтение, — это механика отбора, а не диагностики: заключение по каждому исследованию по-прежнему выдаёт человек; объём второго чтения упал на 44,3 процента, из ста женщин с раком программа стала находить 81 вместо 74, а цена лежит в устройстве процедуры — второго независимого человека большинство обследованных больше не получает"
source: "Swedish program, final analysis — https://doi.org/10.1016/S0140-6736%2825%2902464-X"
media: ""
media_needed: "настоящий снимок рабочего места чтения скрининговых снимков с очередью исследований на экране; запасной сюжет — страница публикации с таблицей исходов"
media_note: "свидетельство, а не оформление"
razbor_part: "2 из 3 (единый кейс в трёх частях — шведская программа, не два разных «2 из 2»): часть 1 — ①цена ошибки и ②классические режимы, на s13; часть 2 — здесь, начало ③«модель против них» (механика отбора: оценка риска решает, кому достанется второе чтение); часть 3 — продолжение ③ (британский арбитраж, время), обратная сторона доверия находке, германские 0%/56,7% подробнее и честно названный ⑤пробел обучения/обновления/дрейфа, на s15a, issue #270"
blocks:
  - {label: "Out of a hundred women with cancer — found", value: "74 → 81", note: "105,934 women, randomized into two arms", key: true}
  - {label: "Called in for nothing: a second image", value: "2.0 → 2.2 out of a hundred", note: "80,033 women from the same program"}
  - {label: "Less second human reading", value: "by 44.3 percent", note: "the same 80,033 women"}
pol_slov: 245   # issue #270, добавлена мостовая фраза «Арбитраж и доверие находке — кадром следом.» в конец абзаца про Германию, готовит разряд продолжения (s15a) без того, чтобы путать его с этим кадром; razbor_part получил зеркальную дополняющую строку с перечнем, что ушло на s15a. Остальное содержание НЕ ТРОНУТО. ЗАМЕР ПО СОБРАННОМУ PDF раздела 1 (render_sec.py 1, 2026-10-18, 12 страниц): 245 слов на этом кадре (было 244); медиана полосы 183, максимум 286 (`s13a`), блокирующих 0 (`build_lec07.py --only s15,s15a`). #229 п.15 (владелец: «от механики отбора перешли к механике диагностики… сейчас бесполезен и внезапен»). Кадр переписан на то, что в работе измерено, и первым словом заголовка стоит, ЧТО модель делает: решает, кому нужно второе чтение. Чем заняты слова: мост на s13 первой строкой (та же программа, то же приглашение — изменилось одно) · описание опыта целиком, включая шкалу 1–10 и правило деления потока (chapter-part2b.md:120) · строка «это механика отбора, а не диагностики» — она и есть ответ на замечание · устройство с входом и выходом · названный пробел по имени изделия и три изделия режима · цена в устройстве процедуры · две процедуры одной фразой (Швеция против Германии). ЧЕТЫРЕ ПЛАШКИ, каждая со своей выборкой, и три из четырёх стоят в ТЕХ ЖЕ единицах, что классический режим на s13: пара 74 → 81 из ста женщин с раком (вместо «чувствительность 73,8 → 80,5» — §5.20, термин заменён человеческими словами, §5.19 — единица человеко-центричная; это единственная значимая разница в работе, p = 0,031) · найдено 5,1 → 6,1 на 1000 с оговоркой «значимости не достигла» · 2,0 → 2,2 из ста позванных зря · −44,3 процента второго чтения. Пара интервальных раков 1,76 → 1,55 на кадр НЕ поставлена сознательно: она целиком, вместе с оговоркой о значимости, стоит на s47 в разделе 3, и вторая её копия здесь была бы тем же числом на двух кадрах. Германия ушла с плашки в тело: её разряд ниже (жребия не было, применять модель радиолог решал сам), и на плашке рядом с рандомизированными числами она читалась бы с ними в одном ранге. Вес куплен описанием опыта и четырьмя подписанными выборками: ни одно число здесь не читается без своей — склейка 80 033 и 105 934 есть ровно тот дефект, который разбирает сам раздел ЗАМЕР ПО СОБРАННОМУ PDF полосы Входа и раздела 1 (render_sec.py 0 1, 2026-10-15, 14 страниц): 244 слов на этом кадре; медиана полосы 142,5, максимум 263, блокирующих 0. Поле выставлено ПО ЗАМЕРУ, не по оценке: прежнее число в этой строке называло состав до правки по замечаниям владельца и после неё было бы разрешением на чужой вес.
timing_min: 0.95
in_bucket: false
method_steps: ["③модель против них", "④как это устроено", "упоминание", "вторая половина разбора s13"]
form: ["упоминание"]
vfy: true
status: собран
timing_min: 0.95
---

## Visible slide text

The same program and the same invitation. One thing changed.

**What they did.** Women were randomized. One arm: two readers, a third on disagreement. The other: a radiologist reads first and issues their own conclusion, while the model scores the scan for risk from 1 to 10: at 1–9 there's no second reading, at 10 double reading stays.

**The conclusion is issued by the human. The model selects who gets read twice.**

**How it's built:** input — a mammogram, output — a risk score. Publications don't give the system's name; standing in for it are Transpara, Lunit INSIGHT MMG, and iCAD ProFound. *Image recognition.*

## Speaker notes

The Swedish program set up a randomized trial: one arm kept reading scans the old way — two people, with arbitration on disagreement — in the other, the model scored each scan for risk on a ten-point scale and used it to sort the flow: at a score of one to nine, the second independent reading doesn't happen at all; at ten, double reading stays. The first reading remained human: the radiologist reads the case themselves and issues their own conclusion, and no study bypasses them — but most of those examined no longer get a second independent conclusion. Outcomes were written down in advance. The model did not work as a second reader, and this has to be stated precisely: the second-reading step was removed for most of the flow — which is why the volume dropped by 44.3 percent, not by half.

The program has two publications, and their samples differ: an interim safety analysis on eighty thousand randomized women, and a final analysis on a hundred six thousand. The figures from them can't be combined into one list: the volume of human reading belongs to the interim analysis, while the pair of 74 and 81 out of a hundred women with cancer belongs to the final one. The share of healthy women spared unnecessary alarm is the same in both arms, 98.5 out of a hundred. And a third pair that doesn't appear on the slide: 6.1 against 5.1 found per thousand examined in the interim analysis, p equals zero point zero five two — meaning it didn't reach significance, which is why it isn't shown on screen, and is spoken only with that caveat. A figure placed under someone else's sample becomes a different claim.

This breakdown's answer to the section's question: most of those examined no longer get a second independent human reader. Double reading as a mechanism of mismatched errors has been replaced by one human reading on top of the model plus arbitration — and the cost sits right here, in the construction of the procedure, not in the device's accuracy. And the stage here is still exactly what it was: the model doesn't make a diagnosis and doesn't read in the person's place — it decides who gets read twice, meaning it selects, the same as the whole stage does.

The German program stands here for contrast, and it deserves less trust than the Swedish one: this is an observational deployment, each radiologist decided for themselves whether to use the model, and there was no random assignment to groups. So the direction is confirmed, but the magnitude can't be credited to the model. The construction of the work has been published — double reading with model support against ordinary double reading, meaning the second reader in Germany was never replaced. From here follows a conclusion that a single deployment can't give on its own: the phrase "the model was deployed in screening" means two different procedures, and the question "did detection go up" says nothing on its own until the order of work it went up inside is named.

And here's a case where coverage is reported but the construction of the work isn't: the domestic radiology platform. More than sixteen million studies across seventy-five regions, with the counting method undisclosed; how many radiology studies are done in the country per year in total isn't published, so a coverage share can't even be computed. There's no independent protocol in the open comparing it against a doctor with no model. This is a claim about one single source, and it doesn't extend to the screening programs.

The system's construction is named on the slide to exactly the extent the publications name it: the input is a digital mammogram, the output is a risk score and the study's place in the reading queue. What the system was trained on isn't published by any of the three programs, and it has no name of its own in these studies either — they say "a commercially available system." Standing in for it are Transpara, Lunit INSIGHT MMG, and iCAD ProFound; which one exactly stood in the Swedish program doesn't follow from what's published, and a name can't be substituted by guesswork. A breakdown that can't be checked against the device's name can only be checked against the construction of the procedure — which is why the procedure is what's examined here.

Significance levels for both pairs of figures. The pair of 74 and 81 out of a hundred: sensitivity of 80.5 percent with an interval of 76.4 to 84.2 against 73.8 with an interval of 68.9 to 78.3, significance level 0.031 — the difference holds up. The pair of 5.1 and 6.1 per thousand: a rate ratio of 1.2 with an interval of 1.0 to 1.5, level 0.052 — not significant, and the interval's lower bound touches one. The difference between these two pairs is exactly why they're placed side by side.

The slide's two figures sit on different samples, and they can't go into one list: the volume of human reading belongs to the interim safety analysis, the pair of 74 and 81 out of a hundred women with cancer belongs to the final one. A figure placed under someone else's sample becomes a different claim. What the system was trained on isn't published by any of the three programs, and which of the named systems actually stood in the Swedish one doesn't follow from what's published; a name can't be substituted by guesswork.

**Sources.** [MASAI safety analysis, Lancet Oncology 2023](https://doi.org/10.1016/S1470-2045%2823%2900298-X) · [MASAI final analysis, The Lancet 2026](https://doi.org/10.1016/S0140-6736%2825%2902464-X) · [Eisemann et al., PRAIM, Nature Medicine 2025](https://doi.org/10.1038/s41591-024-03408-6)
