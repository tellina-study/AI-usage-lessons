---
# ПРОИЗВОДСТВЕННЫЙ ЯЗЫК ВЫЧИЩЕН С ВИДИМОГО СЛОЯ (п. 17 наряда; §11.6 — расширенный список
# паттернов, и §6.3 — «протечки процесса»: слова, которыми мы описываем между собой свою
# работу, на кадре стоять не могут). Греп по телу, плашкам, столбцам и схемам обоих разделов.
# ЗАМЕНЕНО ЗДЕСЬ: «достроить ладонь „модель · человек · пара"» — наш внутренний образ, снят ещё при резке тела; здесь закреплено, что он не вернётся
# ПЛАШКИ РАЗГРУЖЕНЫ ПОД СХЕМУ (пп. 11-12 наряда). Схема заняла бюджет высоты, и кадр перестал
# держать прежний набор плашек: сборка давала [высота] s47/тело: места под тело не осталось (0,15 дюйма). Снято по двум правилам, не на глаз.
# §7.1 — оговорка о НАДЁЖНОСТИ замера уходит в заметки целиком, знаменатель остаётся на кадре.
# §5.15 — упоминание из ДРУГОЙ работы на кадре разбора есть библиография, а не разбор; его место
# в заметках, и там оно уже стоит целиком. Ни одно измеренное число не потеряно: снятое
# перечислено поимённо ниже и читается вслух.
# СНЯТО С КАДРА: плашка «другая программа, трое смотрят сразу» (22 против 3,4 из ста, и отзыв 14,2 против 4,6) — это ДРУГАЯ программа и другая работа, упоминание рядом с разбором; хвост плашки интервальных раков про состав пропущенного (крупных 38 против 48, агрессивных 43 против 59)
# СХЕМА ДОБАВЛЕНА (п. 11 наряда, §11.3: «схема обязательна у каждого кадра типа `case`»).
# Замер прожарки: схема нашлась у 5 кадров `case` из 12 в разделе, и не было её ровно у семи
# самых тяжёлых по тексту — то есть там, где она нужнее всего. §10.3: схема решения несёт
# инженерное содержание, текст — пояснение к ней, не замена; поэтому вместе со схемой из тела
# СНЯТО то, что она теперь показывает сама (п. 12 наряда, плотность: чинить схему и объём
# вместе, а не по очереди).
# СВЁРТКА (#229): кадр собран из s47 и s48 (второй файл в slides/_snyato/). Сведён в одну форму §5.13 сессией содержания: величина переведена в пропущенные раки (та же единица, что у s41 и s28), арбитр назван, а отсутствие замера модели одной названо пробелом — достраивать его нечем.
# СЛИЯНИЕ РАЗДЕЛОВ 1 и 2/3: номер разбора и сжатое тело взяты у раздела 2/3 (дивайдер s35
# называет шведское испытание третьим; длинное тело давало блокирующее [высота]), а ПОРЯДОК
# ЧТЕНИЯ — у раздела 1: глава (chapter-part1b §1.4) говорит «второго читателя заменили, а первый
# остался человеком и прочёл каждое исследование». Схема пришла слиянием со «модель читает
# первой» и исправлена здесь: это тот самый факт, которым один случай рассказывался как два
# разных (коммит 881873997, s47 + s38), и s38 после слияния говорит именно «человек первым».
id: s47
local_id: s3-10
section: "3. Постановка диагноза"
type: case
title: "Example 3: the Swedish trial — the second human reading replaced by a model"
assertion: "ТО ЖЕ ИСПЫТАНИЕ, что разобрано Примером 1 раздела 1 (DOI 10.1016/S0140-6736(25)02464-X) — здесь оно взято под другим вопросом (точность пары), и порядок чтения назван тот же: радиолог первый, модель вторая. Один человек с моделью и арбитражем на разногласиях пропускает двадцать раков из ста против двадцати шести у двойного человеческого чтения, и человеческого чтения при этом вдвое меньше; исход по интервальным ракам измерен, и улучшение по нему не доказано — показана не-худшесть; модели одной это испытание не измеряло вовсе"
source: "The MASAI final analysis, The Lancet 2026 — https://doi.org/10.1016/S0140-6736(25)02464-X · safety analysis, Lancet Oncology 2023 — https://doi.org/10.1016/S1470-2045%2823%2900298-X · Dembrower et al., Radiology 2025 — https://doi.org/10.1148/radiol.242566"
media: ""
media_needed: "рисунок исходов из итоговой публикации — добыть, права проверить; запасной вариант — собственные плашки с атрибуцией данных"
media_note: "иллюстрация не добыта"
blocks:
  - {label: "Missed cancers: double reading → one reader with the model and an arbiter", value: "26 → 20 out of a hundred present", note: "randomized trial, 105,934 women; the difference is robust", key: true}
  - {label: "Interval cancers per 1,000 screened: double reading → with the model", value: "1.76 → 1.55", note: "93 out of 52,872 versus 82 out of 53,043. Improvement is NOT proven: ratio 0.88 with an interval of 0.65–1.18 — non-inferiority", key: true}
  - {label: "Volume of human reading", value: "down by 44.3 percent", note: "baseline — double reading, two human readings per image; interim analysis, 80,033 screened", key: true}
pol_slov: 190   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 186 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
# СКАЗАННОЕ ДВАЖДЫ, снято: «Цена обеих ошибок как в скрининге: пропуск — рак позже; ложный вызов — месяцы тревоги» снято по п. 40 владельца («цену убрать») — та же цена названа плашками на s28 и в разделе отбора, а здесь она переехала в саму единицу: «пропущенных раков» и «повторных вызовов» — это обе стороны ошибки, и стоят они у своих чисел; «Устроено как в примере отбора: вход — снимок скрининга, выход — риск вместо второго чтения» и «Модель против них. Читает первой, человек — сам, разногласие разбирает третий» говорили одно устройство дважды — осталась одна строка, и владелец это прямо разрешил («со схемой точностей „модель против" и „устроено" можно не писать»); плашка «База чувствительности — итоговый анализ, 105 934 женщины» ушла подписью к плашке пропущенных раков, то есть к самому числу; «Появился шаг „нужно ли второе чтение"; объём человеческого чтения упал там же» — объём стоит своей плашкой, в теле остался только арбитраж; «туда дошло 5 489 случаев из 54 991» заменено на знаменатель, который относится к самим 22 и 3,4 — «1 886 находок против 1 858».
# ЧЕМ ЗАНЯТЫ СЛОВА: величина переведена в человеко-центричную единицу (§5.19 и п. 40 — «что за чувствительность? если точность — так и писать», «нужна человеко-центричная метрика»): «пропущенных раков 26 → 20 из ста имевшихся» вместо «чувствительность 73,8 → 80,5». Единица та же, что на s41 и s28, — примеры раздела стали сравнимы между собой, чего владелец и требовал. Арбитр назван («к нему уходит только расхождение, а не весь поток», 10 слов — п. 40, «арбитр — это кто?»). Названо, почему человеческого чтения стало меньше (п. 40). И названо ОТСУТСТВИЕ замера модели одной: «ладонь „модель · человек · пара" достроить нечем» (11 слов) — владелец просил «модель xx, под ней человек yy, а с арбитром zz», и этой ладони в испытании нет; выдумать её было бы ровно тем, что раздел учит ловить, поэтому пробел назван на кадре.
# ЦЕНА, названная числом (замер по собранному PDF): семь плашек → четыре, тело поднялось с НУЛЯ МЕСТА до 12,5 пт, блокирующее ушло. Слов 150 → 269 — самый тяжёлый кадр полосы, и занят он двумя программами: у второй (трое смотрят сразу) своя пара чисел с обратным знаком доверия, и без неё кадр показывает только выигрыш. Замерено по дороге: вторая программа прозой не садится — 10,5 пт и блокирующее; та же пара чисел плашкой держит 12,5. Делить кадр на два разрешено оркестратором и НЕ понадобилось.
scheme:
  caption: "Only disagreements go to the arbiter, not the whole stream"
  arrows: true
  rows:
    - {label: "Double reading", steps: ["two radiologists separately", "disagreement reconciled", "decision"]}
    - {label: "Second reading — the model", steps: ["radiologist first", {text: "model second", ai: true}, "disagreement — a third reader", "decision"]}
timing_min: 2.2
in_bucket: true
method_steps: ["контрольная линия", "①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено", "⑤что переехало", "пара дало–потребовало"]
form: ["форма 3", "форма 4а", "сетка", "[VFY]", "упоминание"]
vfy: true
status: собран
---

## Visible slide text
**105,934 women in the Swedish program were randomized between two reading orders.** The second order uses less human reading: only a disagreement goes to the arbiter.

**This trial never measured the model alone,** and there's no single reading without arbitration either: the comparison was against a strong classical mode.

**Disagreement, the fifth input distortion, became a new piece of work; recalls became neither more nor fewer.**

## Speaker notes

A Swedish randomized trial of the national screening program: 105,934 women randomized between two reading orders. In the control arm, classical double reading runs as usual — two independent radiologists with a third arbitrating any disagreement; in the second arm, the second human reading is replaced by the model, and the radiologist reads first. A disagreement is still resolved separately, and this is disagreement, the fifth of the six input distortions, appearing a second time this evening — in a different country and a different trial.

Strength of evidence: four sites, enrollment from April 2021 to December 2022, outcomes preregistered. Nineteen people were excluded from the analysis; 53,043 entered the model arm and 52,872 the control. The design is single-blind, for non-inferiority. This is the only measurement in the section where a patient outcome is actually measured; the rest measured reading accuracy, gaze, or a reasoning score.

What was compared. The control arm ran classical double reading: two independent radiologists, a third arbitrating any disagreement, sensitivity 73.8 out of a hundred with an interval from 68.9 to 78.3 — this is the baseline; the model arm got 80.5 with an interval from 76.4 to 84.2, and the difference is robust, p equal to 0.031. This is the only one of the trial's three figures where a difference is actually proven: for interval cancers, only non-inferiority is shown, and reading volume was counted on a different sample. The model arm: the model reads the stream, one radiologist reads on their own, and an arbiter resolves any disagreement between them; sensitivity 80.5 with an interval from 76.4 to 84.2, and the gain is significant. Specificity is the same in both arms — 98.5 out of a hundred healthy women. In other words, the second reader was replaced, while independence and arbitration were preserved and rebuilt around the new participant.

Arbitration and the threshold. The model issues a suspicion score, the radiologist gives their own report, and on disagreement the case goes to an arbiter who sees both. The arbiter's workload is set by the rate of disagreement, and that in turn by the threshold: shifting the threshold toward suspicion raises both the number of disagreements and the number of recalls for further workup. Classical double reading had a threshold too, but it was set by each reader's own practice, where it's unrecorded and untunable; moving to the model turned it into an explicit parameter that someone now has to maintain. The second classical mode — a single reading without arbitration, which programs with no resource for a second reader run on — wasn't reproduced in this trial: the comparison was against the strong mode.

The tool's design is named just as precisely, and just as incompletely, as in the last case study: input — a mammogram, output — a suspicion score against which a threshold is set. What the system was trained on and how often it's updated after deployment, the publication doesn't disclose — and that's not a gap in the research, it's the nature of a trial report.

The reading physician's rung is "looks first": they see every exam on their own and produce their own report, with no one else's shown to them. The arbiter looks only at disputed cases, and that's set by the program's own design. The task type is image recognition. What the system was trained on, the program doesn't publish: there's no way here to check a vendor's claim against the product's name, and either way the gain in this case study belongs not to the device but to the design of the procedure around it.

On interval cancers — disease found between screening rounds — precision matters. In the double-reading arm it's 1.76 per 1,000 screened, with the model 1.55: that's 93 cases out of 52,872 versus 82 out of 53,043. The rate ratio is 0.88, with an interval from 0.65 to 1.18 — the interval crosses one, there's no significance, and the trial was designed to claim non-inferiority. Reading 1.55 against 1.76 as a proven improvement is not allowed. What is proven, and proven strongly, is something else: sensitivity is significantly higher, the outcome didn't worsen, and the composition of what was missed shifted toward the less dangerous side — 16 percent fewer invasive cancers (75 versus 89), 21 percent fewer large ones at stage T2 or above (38 versus 48), and 27 percent fewer aggressive subtypes (43 versus 59).

And why this measurement turns the whole section around. The other measurements all showed the same error mechanism: a person trusts the suggestion more than they should, and pays for it in attentiveness, in odds of a correct answer, or in access to the tool wasted for nothing. The asymmetry of trust, examined earlier in this section on a Swedish program with three independent readings, is broken in the opposite direction here: a source that was confirmed as cancer more than six times as often was recalled a third as often. So the rule of this section isn't "people trust the machine too much" — that's only half of what's been measured. Trust in a finding's source is set by the design of the procedure, not by the source's accuracy, and it's calibrated independently of that accuracy — in either direction. Don't soften the conclusion: the model and its accuracy are sound in this measurement; what broke is what was built around it.

**Sources.** [MASAI, final analysis, The Lancet 2026](https://doi.org/10.1016/S0140-6736%2825%2902464-X) · [Dembrower et al., Radiology 2025, ScreenTrustCAD](https://doi.org/10.1148/radiol.242566)
