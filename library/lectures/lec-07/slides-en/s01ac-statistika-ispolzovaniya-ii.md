---
# ТРЕТИЙ кадр блока «допуск и поток»: `s01aa` — пути допуска, `s01ab` — состав массива и
# страны, здесь — применение. Содержание кадра не менялось ни Этапом A (слияние унесло
# соседний `s01ab`, а не этот), ни Этапом E (возврат `s01ab` вернул соседа на место).
# Тайминг опущен с 0,8 до 0,65 вместе со всем Входом.
# МОСТ С `s01ab` СТОИТ В ЗАМЕТКАХ, А НЕ НА КАДРЕ, и это замер, а не пропуск: строку-мост
# в тело пробовали, и слот тела здесь 0,45" — прогон назвал 0,57" и дал блокирующее
# `[высота]`. Срезать под мост пришлось бы либо знаменатель, либо вопрос залу. Заметки
# при этом открываются ровно мостом — «До этого места речь шла о том, сколько изделий
# допущено. Допуск — ещё не применение», — и после возврата `s01ab` он читается точнее,
# чем читался до него. Видимый слой кадра Этапом E НЕ тронут ни одним знаком.
# ИЗВЕСТНЫЙ ПОВТОР, НАЗВАННЫЙ, А НЕ ЗАМОЛЧАННЫЙ: «49 из 549» стоит и в плашке этого кадра
# («допущено и оплачивается»), и знаменателем корейской строки возмещения на `s01ab`.
# Это одно число в двух разных утверждениях: там — второй признак отбора у одной страны,
# здесь — половина пары «допуск шире оплаты». Снять его с одного из кадров значит снять
# утверждение, а не повтор; решение — владельцу.
id: s01ac
local_id: В-01ac
section: "0. Вход"
type: analitika
title: "Using the model: doctors and the flow of studies"
assertion: "Пользуется ИИ в работе около 3 миллионов врачей из 13–15 миллионов по миру, в США доля выросла с 38 до 66 процентов от примерно 1,1 миллиона практикующих, в России регулярно применяют 15–25 процентов от 770 тысяч; именованные диагностические платформы — Aidoc, Qure.ai, Annalise, московская платформа — обрабатывают 79–86 миллионов исследований в год против мирового потока визуализации 3,6–4,2 миллиарда, то есть 1,9–2,4 процента, и это пол счёта, а не потолок; рядом стоят категории другого рода работы, которые в эту долю не складывают, — документация (30 миллионов сводок СберМедИИ) и административное решение об оплате (53 миллиона решений Medicare Advantage на 34,1 миллиона застрахованных); допуск при этом систематически шире оплаты — у 1 614 американских изделий постоянный код оплаты есть у трёх"
source: "Полная запись источников в репозитории курса · агрегаты внедрения — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/14-vnedrenie-agregaty.md · использование и эффект — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/10b-ii-ispolzovanie-i-effekt.md"
media: "rework/deck/assets/s0Xc-potok-za-god.png"

media_needed: "добыто: собственная аналитика по шаблону `tools/presentation-build/analitika.py`, прогон `rework/deck/make_charts_244.py`"
media_note: "не иллюстрация, а сами данные кадра. Столбцы лежат, потому что единица у каждого своя и подпись из двух строк стоя не читается. Viz.ai в ряд не поставлен намеренно: 230 млн — люди в зоне покрытия, не события за год, и в одном ряду со случаями это была бы склейка разных счётов"
blocks:
  - {label: "US doctors", value: "38% → 66%", note: "of 1.1 million practicing, 2023 and 2024"}
  - {label: "Cleared and reimbursed", value: "3 of 1,614 · 49 of 549", note: "permanent payment codes, US · reimbursement, Korea"}
  - {label: "People within coverage", value: "230 million", note: "Viz.ai, 2,000 hospitals; reach, not cases", key: true}
timing_min: 0.65
in_bucket: true
method_steps: ["заземление", "счёт с базой", "вопрос залу"]
form: []
vizforma: "плашки"
vfy: true
status: собран
---

## Visible slide text

**Doctors worldwide: 3 million of 13–15 million. Russia: 15–25% of 770,000.** Who has a model standing in their loop — and who looks into its failures?

## Speaker notes

How many doctors in the world actually work with a trained model: about three million out of thirteen to fifteen million practicing. In the US the share rose from thirty-eight to sixty-six percent of about 1.1 million doctors; in Russia, fifteen to twenty-five percent of 770,000 apply it regularly. Clearing a device is not yet using it, and the counters involved are different: cleared, installed, in use, cases processed per year. Every figure from here is labeled with which counter it is, because they keep getting added together, producing a quantity nobody has actually measured.

How many doctors use it. For the US there's a series taken with one method: 38 percent in a 2023 survey, 66 percent in a November 2024 survey. The denominator is practicing US doctors, and it itself does not converge to one number: a licensing census gives 1,082,000, the association of medical colleges gives 1,032,000, an independent 2025 estimate gives about 1.11 million. We take 1.1 million as a working average; the eight-percent spread does not change the order of magnitude. In absolute terms that is a rise from roughly 410,000 to 720,000 doctors in a year. Alongside sits a second, stricter count — a survey by the professional network Doximity, winter 2025–2026: 63 percent on the same base. The gap between the two counts is not an error: one counts any professional contact with AI, including a one-off use; the other counts regular use within the clinical process. Both figures are honest.

For Europe there is no direct survey of all doctors; there are two indirect measurements. The European Society of Radiology, 2024 survey: 47.9 percent of respondents use AI in practice, and the denominator matters here — 572 people answered out of 28,000 invited, meaning this is self-selection, not a random sample. The British radiology department census of 2025: AI in at least one application is present in 75 percent of departments, but the counter here is the department, not the doctor. There's a curious reversal in the same report: a drop in workload from AI-drafted reports is noted by 24 percent of departments, an increase by 37 percent, and the remaining 56 percent see no change at all.

For Russia there is no single annual survey with one method, and that is a property of the data itself. There are one-off surveys: more than half of doctors have worked with neural networks at least once, 15–25 percent apply them regularly. The denominator is 771,700 doctors in 2025, and the series over the years is not monotonic; the Ministry of Health separately names 614,000 doctors in state organizations, a narrower basket. Over the range of the share, that's 115,000–190,000 people, and this is an estimate from a share, not a direct count of the absolute number.

How many cases pass through the model. These deployments are different categories of work, and that's worth stating before the numbers. Aidoc — 60 million cases of diagnostic triage a year; Qure.ai — 7 million tuberculosis screenings in one fiscal year; Annalise in the British system — 2.8 million chest X-rays a year across forty-plus trusts; the Moscow platform — 16 million studies by the 2026 report (an earlier report the same year gives 9–10 million, and the method isn't disclosed in either). These four are one category, diagnostic imaging, and only they can be honestly added: 60 plus 7 plus 2.8 plus 16 — 85.8, that is, 79–86 million studies a year accounting for the range in the Moscow platform's figures. Beyond that are two categories of a different kind of work, and they are not part of this sum: the digital doctor's assistant from SberMedAI — 30 million status summaries, which is documentation, not diagnosis; payment decisions in Medicare Advantage — 53 million, which is an administrative decision. Adding all six into one figure would be exactly what this lecture's screening chapter warns against: the same phrase, "passes through the model," here means different procedures with no common unit. Viz.ai is not included in the diagnostic sum for a different reason: it sits in the same American hospitals as Aidoc, and adding it would double-count part of the same scans. I'll name Viz.ai's own figure separately: two thousand hospitals and 230 million people within its coverage area — that is the reach of the service area, not cases per year.

Share of the total flow. The global volume of diagnostic imaging is 3.6–4.2 billion procedures a year: X-ray over 2.5 billion, ultrasound over 500 million, CT about 375 million, MRI 100–150 million. Against that, the diagnostic subtotal — 79–86 million — is 1.9–2.4 percent of the global flow. And this is the floor of the count, not the ceiling: it does not include China, where more than 1,200 top-tier hospitals use AI diagnostics but the volume flowing through them is not disclosed; it does not include most of automated appointment scheduling — a category with about sixty companies and not one industry-wide total; it does not include Korea or Japan.

And the category that touches more people at once than any diagnostic platform: administrative. 53 million prior-authorization payment decisions in 2024, against 34.1 million people insured under Medicare Advantage — that's 1.55 decisions per person a year. Not all of them went through an algorithmic check equally, but the order of magnitude is clear: AI in medicine does not reduce to diagnosis.

The last two figures are about the gap between clearance and payment, and everywhere it is measured in orders of magnitude, not percentages. US: 1,614 cleared algorithms, some payment code exists for 26, a permanent code with guaranteed payment exists for three. Korea: 549 cleared, 49 got reimbursement — meaning 500 devices are cleared and stay outside insurance. Germany: 56–59 digital applications are paid permanently or provisionally, but there's no published denominator of submitted applications in open sources. France: three telemonitoring devices got reimbursement, and all mobile apps were rejected — for a whole class, that's zero. I state the German and French rows without a share deliberately: their denominator isn't published, and a share of an unknown denominator measures nothing.

**Sources.** [AMA, AI use among US doctors](https://www.ama-assn.org/press-center/ama-press-releases/ama-ai-usage-among-doctors-doubles-confidence-technology-grows) · [Doximity, State of AI in Medicine 2026](https://www.doximity.com/reports/state-of-ai-medicine-report/2026) · [European Society of Radiology, 2024 survey](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11458846/) · [British departmental census, 2025](https://www.auntminnieeurope.com/imaging-informatics/artificial-intelligence/article/15828872/rcr-census-ai-underused-for-admin-tasks-that-cut-workload) · [Russia, overview of physician surveys](https://www.vshouz.ru/news/analitika/wcs-20706/) · [Aidoc, 60 million cases a year](https://www.medtechdive.com/news/aidoc-raises-150m-to-advance-clinical-ai-foundation-model/819042/) · [Viz.ai, two thousand hospitals and 230 million people](https://www.businesswire.com/news/home/20260728323403/en/A-Decade-of-Increasing-Access-to-Life-Saving-Treatments-Viz.ai-Celebrates-10-Years-2000-Hospitals-and-230-Million-Patients) · [Global imaging flow](https://readmymri.com/blog/how-many-medical-imaging-scans-are-done-per-year) · [Medicare Advantage, insured population](https://www.kff.org/medicare/medicare-advantage-2025-spotlight-a-first-look-at-plan-offerings/) · [Reimbursement for AI devices in the US](https://radiologybusiness.com/topics/artificial-intelligence/radiology-dominates-fda-cleared-ai-reimbursement-lags-far-behind) · [Korea, reimbursement 49 of 549](https://www.dataeconomy.co.kr/news/articleView.html?idxno=42899)
