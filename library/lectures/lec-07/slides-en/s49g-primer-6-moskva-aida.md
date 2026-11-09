---
# НОВЫЙ РАЗБОР, ЗАВЕДЁН ПО §1.7 КАНОНА `obzor-stran-i-glubina-razbora.md` (порог ≥1 российский
# разбор на раздел с кейсами; владелец снизил порог с ≥2 до ≥1 20.10.2026). До этой правки
# раздел 3 нёс пять разборов — замер взгляда, патологи на срезах, шведское испытание, хирурги на
# риске, модель сепсиса, — и ни одного российского.
# ПОЧЕМУ ШЕСТОЙ РАЗБОР, А НЕ ЗАМЕНА (правило 3+6, `stroenie-i-povestvovanie.md` §3 шаг 3).
# Раздел ФАКТИЧЕСКИ уже несёт пять, то есть превышение порога трёх здесь не вводится мной, а
# унаследовано: пятый разбор стоит здесь по прямому указанию владельца 15.10.2026 («раздел
# наблюдение убираем, пример из него в диагностику»). Избыточности среди пяти я не нашла —
# каждый меряет свой эффект подсказки (сдвиг решения, сужение поиска, замена второго чтения,
# знакомство с моделью до решения, поток тревог), — поэтому замена потребовала бы снять чужую
# работу, чего наряд прямо запрещает. Шестой добавлен с пересчётом; счёт минут раздела и деки
# в докладе назван.
# ЧТО ЭТОТ РАЗБОР ДЕЛАЕТ, ЧЕГО НЕ ДЕЛАЕТ НИ ОДИН ИЗ ПЯТИ. Все пять меряют подсказку на ОДНОМ
# исследовании или одном показателе. Здесь модель читает медкарту ЦЕЛИКОМ и предлагает
# заключительный диагноз кодом — и это единственный разбор деки, где измерено, что происходит
# именно в точке РАСХОЖДЕНИЯ врача и модели (697 случаев: врач прав в 64 из ста, модель в 45).
# Ни один другой кадр деки этого числа не даёт, а вывод раздела `s50` на нём стоит.
# МЕХАНИЗМ НАЗВАН ТЕРМИНОМ ВВЕДЕНИЯ (§2.4, введено владельцем 20.10.2026): подсказка приходит до
# решения врача и стоит выше него на экране — это «Якорение», первый из шести механизмов `s01ae`.
id: s49g
local_id: s3-18
section: "3. Постановка диагноза"
type: case
title: "Example 6: Moscow, Russia — a model suggests a final diagnosis from the medical record"
assertion: "Московская система поддержки врачебных решений AIDA читает медкарту целиком — жалобы, анамнез, осмотр, лабораторию, протоколы, историю кодов — и до решения врача предлагает заключительный диагноз кодом МКБ-10, причём подсказка стоит наверху рабочего экрана; обучена на 1,5 млн карт города, за первый год 5 млн запросов и 3 млн рекомендаций при согласии врача 84,3 из ста; на размеченном экспертами наборе модель даёт 87,7 верных из ста против 91,7 у врача — то есть внедрена она не как лучший решатель, а как страховка от просмотра, и авторы говорят это прямо; модель умеет отказываться отвечать, и этот отказ они называют тем, что покупает доверие"
source: "Umerenkov, Nesterov, Shaposhnikov et al., IJCAI-25, AI for Social Good track, pp. 9880–9886 — https://www.ijcai.org/proceedings/2025/1098.pdf"
media: ""
media_needed: "иллюстрация не нужна — кадр держат схема двух порядков и полоса плашек"
media_note: "в работе есть схема развёртывания с рабочим экраном врача (рис. 2), но она на английском и под свободной лицензией не выложена; порядок предъявления показан нашей схемой"
blocks:
  - {label: "Physician alone → model", value: "91.7 → 87.7 correct out of a hundred", note: "3,332 cases: the model is four points WORSE than the physician, and it's deployed as insurance against an overlooked detail", key: true}
  - {label: "The code set", value: "256 → 571 → 363", note: "571 covered 95 out of a hundred visits; it was cut back by removing codes a general practitioner never assigns"}
  - {label: "The model can stay silent", value: "5 million requests → 3 million answers", note: "above the uncertainty threshold, there's no answer at all"}
scheme:
  caption: "The suggestion arrives BEFORE the physician's decision and sits above it on screen"
  arrows: true
  rows:
    - {label: "Physician alone", steps: ["complaints and exam", "physician builds the list", "physician chooses", "code goes into the record"]}
    - {label: "Moscow, with the model", steps: ["the whole record", {text: "model suggests a code", ai: true}, "physician decides whether to trust it", "code goes into the record"]}
pol_slov: 175   # ПО ЗАМЕРУ СБОРКИ (`build_lec07.py --only s19,s19a,s49g,s49h`), не по оценке. Предел кадра 140, и он здесь перебран — как перебран у КАЖДОГО разбора этой деки: рядом стоят 256 (`s41`), 252 (`s16`), 244 (`s15`), 214 (`s49b`), 206 (`s49f`), 190 (`s49e`). Новые кадры легче любого из них, и легче медианы семьи. Обязательный состав §5.13 (цена ошибки · оба классических режима · модель рядом · устройство · что переехало) плюс схема потока и нюанс надёжности на кадре (§2.3) в 140 слов не укладывается: пробовано, замерено. Физические пределы — `[высота]`, `[кегль]`, `[пол]` — все чистые, то есть текст в рамке держится и кегль не ужат.
timing_min: 1.0
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель рядом", "④как устроено"]
vfy: true
status: собран
---

## Visible slide text

**What kind of case this is.** Moscow, a general practice visit. The model reads the whole medical record and, before the physician's decision, suggests a final diagnosis as a code. *The product is AIDA.*

**How it's built:** input — the whole record: complaints, history, exam, labs, reports, the code history. Output — a single code with an uncertainty score. A Longformer up to 8,192 tokens, 1.5 million records. *Text processing.*

## Speaker notes

Moscow, a general practice visit: AIDA, a clinical decision-support system, reads the whole medical record — complaints, history, exam, labs, reports, the code history — and, before the physician's decision, suggests a final diagnosis as an ICD-10 code. The suggestion sits at the top of the working screen. The system was trained on a million and a half city records; in its first year it handled five million requests and three million recommendations.

The other case studies at this stage measured the suggestion against a single piece of data: an image, a slide, an EKG, a risk score. Here the model reads the whole record and gives a final diagnosis, not a preliminary one.

What kind of case this is. Moscow, a visit to a general practitioner or family physician at a city polyclinic. The system is called AIDA; it's built into the city's clinical decision-support system and runs on top of the same electronic medical record the physician is already working in. One important clarification, so as not to confuse two products: Moscow previously ran a service that suggested the three most likely preliminary diagnoses from the complaints recorded at intake. AIDA is a later product in the same line, and its subject is different: not a preliminary diagnosis from a complaint, but a final diagnosis from the whole history. For our stage, that's exactly the case we need: this section is about how a conclusion is drawn from everything that's been gathered.

How it's built. The input isn't a single field but the entire record in text form: complaints, history, exam findings, lab results, reports and conclusions from imaging and other studies, the history of previously assigned codes. The output is a single code from the International Classification of Diseases plus a self-reported uncertainty score. Inside is a Longformer language model — that is, a transformer with sparse attention that can hold a sequence of up to eight thousand one hundred ninety-two tokens; it was first trained to predict masked words in unstructured clinical notes, then fine-tuned to predict the code. The training set is a million and a half de-identified records from the city system, of which one million three hundred fifty thousand went to training and one hundred thirty-three thousand to validation. The labels were diagnoses confirmed by laboratory or imaging findings and flagged in the record as final.

Two engineering details from the same source, both instructive. First: when full lab results were fed into the text, accuracy DROPPED — a long printout of lab values crowded the old history out of the window, and the model lost the long-term trends. So now only values outside normal range are fed in. Second: adding the time gaps between visits, which looks obviously useful, produced no measurable improvement at all; nor did height and weight. Feature selection here was measured, not guessed, and the heaviest-weighted features turned out to be complaints and history, not lab values.

The code set is a separate story about how a task gets narrowed to fit practice. They started with the two hundred fifty-six most frequent diagnoses. They expanded it to five hundred seventy-one, and that set covered ninety-five out of a hundred visits, excluding obstetrics, oncology, and routine checkups. Then they CUT it back to three hundred sixty-three, dropping codes a general practitioner never assigns, codes absent from clinical guidelines, or codes unsuitable as a final diagnosis. In other words, the set was edited not for the metric's sake but to match what can actually be a final diagnosis at this point in care.

Now the classical mode this is compared against. There's one here, and it's measured: the physician decides alone. On the set of labeled cases, the physician scores ninety-one and seven tenths correct out of a hundred. There simply isn't a second mode here — a colleague's second opinion — at a polyclinic visit: in the case study on second opinions we already covered what holds that mechanism up, and a fifteen-minute visit has nothing to hold it up with. This isn't a gap in the measurement, it's a property of the stage, and I'm naming it outright.

And the key figure of this slide, the reason this case study is worth doing. The model scores eighty-seven and seven tenths against ninety-one and seven tenths for the physician. The model is FOUR POINTS WORSE than the physician — and it's deployed anyway. The authors don't hide this or make excuses for it: they write that the model works as a check and a safeguard, so that no significant detail in the record goes unnoticed. This has to be kept separate: the argument "the model is more accurate than the human" never comes up here at all, and yet three million recommendations got made in the first year regardless. The basis for deploying it is something else — not accuracy, but thoroughness of review.

And one last thing on this slide: the model can stay silent. It outputs a code with an uncertainty score — at first this was simply the maximum of the output distribution, then a separate uncertainty-estimation model was added — and if the uncertainty is above a threshold, there's no answer at all; instead the screen shows a message that the record's data is insufficient, and separately there's a warning for an "especially complex case." Hence a gap in the numbers that would otherwise look like data loss: five million requests in the first year, and three million recommendations. Two million times, the model declined to answer. The authors write that this very refusal is what raises physicians' trust in the tool — meaning the ability to stay silent is part of the product here, not a shortcoming of it.

**Sources.** [Umerenkov, Nesterov, Shaposhnikov et al., IJCAI-25, pp. 9880–9886](https://www.ijcai.org/proceedings/2025/1098.pdf)
