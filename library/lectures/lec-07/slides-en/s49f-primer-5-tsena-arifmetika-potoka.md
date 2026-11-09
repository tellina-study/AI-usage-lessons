---
# ПРЕФИКС СТАДИИ ПЕРЕПИСАН (переделка раздела 2 по канону PR #286, `storozha-i-priyomka.md` §14).
# Было `s4-06a` — префикс стадии «динамическое наблюдение и клинические тревоги». Стадия эта
# самостоятельным разделом деки не является: владелец снял её по имени 2026-10-15 («раздел
# наблюдение убираем, пример из него в диагностику» · «пример в диагностику в виде 1-2
# слайдов», запись — `_snyato/README.md`), и этот разбор стоит здесь по его указанию. Пока
# то решение не отменено письменно, кадр принадлежит разделу «Постановка диагноза» —
# и префикс обязан это говорить, иначе сторож «один раздел — один префикс стадии» ловит
# расхождение, которого по существу нет. Материал разбора при этом остаётся материалом
# стадии наблюдения, и заметки кадра это называют; на видимый слой такая оговорка не идёт (§7.1).
id: s49f
local_id: s3-17a
section: "3. Постановка диагноза"
type: case
title: "Example 5, the cost: eighteen alerts per hundred admissions"
assertion: "Два знаменателя разные — 18 из ста госпитализаций против 12 из ста поднятых тревог, — и чтобы найти один случай сепсиса, смена разбирает восемь тревог; вторая проверка другими авторами показала нулевое медианное опережение клинического решения, а разбор тревоги стал новой статьёй рабочего времени той же смены"
source: "Wong, Otles et al., JAMA Internal Medicine 2021, with an erratum in the same journal — https://doi.org/10.1001/jamainternmed.2021.2626 · Ostermayer et al., JAMIA Open 2024 — https://doi.org/10.1093/jamiaopen/ooae133 · alert volume during the epidemic — https://doi.org/10.1001/jamanetworkopen.2021.35286"
media: ""
media_needed: "иллюстрация не нужна — кадр держат схема «до/после» и полоса плашек"
media_note: "вторая половина свёртки снятого раздела наблюдения"
blocks:
  - {label: "To find one case, review", value: "eight alerts", note: "an earlier figure of fifteen was retracted by an erratum in the same journal", key: true}
  - {label: "A second validation, different authors and hospitals", value: "lead time — zero minutes", note: "median; 145,885 visits, 2023"}
  - {label: "Share of patients with an alert during the epidemic", value: "9 → 21 out of a hundred", note: "a different base — 24 hospitals: alert stream 953 → 1,363 while census fell 10,159 → 6,634"}
scheme:
  caption: "Reviewing an alert — a new step for the same shift"
  arrows: true
  rows:
    - {label: "Before", steps: ["scheduled rounds", "a score from the table", "call the physician or not"]}
    - {label: "After", steps: ["the record computes continuously", {text: "the model's alert", ai: true}, "review and dismissal"]}
pol_slov: 200   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 196 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
timing_min: 1.0
in_bucket: true
method_steps: ["③модель рядом", "⑤что переехало", "пара дало–потребовало"]
form: ["форма 4", "форма 3"]
vizforma: "ряды"
vfy: true
status: собран
---

## Visible slide text

**An alert arrives for 18 out of 100 admissions; 12 out of 100 raised alerts are confirmed**: counted from different things — don't mix them up.

**The scale was confirmed 8 out of 100, the model 12: it never left the classical band.** The populations differ: this compares order of magnitude, not superiority.

**Verbatim: "adds little to what physicians are already doing."**

**What shifted:** the load grew at the same spot; **a step appeared** — with the scale there was nothing to dismiss, since it computed its own threshold. **The input distribution shifted; the threshold stayed put. Alert stream, the fourth input distortion.**

## Speaker notes

The cost of the early-warning sepsis model, counted from the alert stream hitting the same shift. An alert arrived for eighteen out of a hundred admissions — six thousand nine hundred seventy-one alerts across thirty-eight thousand four hundred fifty-five admissions; twelve out of a hundred already-raised alerts were confirmed. The two denominators are different, and confusing them is the main place where case studies like this lie: collapsing these two numbers into one thought means saying something false.

That's how the alert stream works, the fourth of the evening's six input distortions: the model sends them one after another, and the physician dismisses almost all of them, including the ones that shouldn't be dismissed. The dismissal rate is measured across a whole class of such systems — a 2024 systematic review of drug-interaction alerts gives an average of 90 out of a hundred, with an interval from 85 to 95. This is worth reading both ways: most alerts really are excessive, and a high dismissal rate is in part a reasonable adaptation, not only fatigue.

From this comes the arithmetic: to find one case of sepsis, the shift has to review eight alerts. Per thousand admissions, that's roughly a hundred eighty-one alerts and twenty-two confirmed cases. The figure of fifteen alerts per case, which circulates in retellings of this study, was retracted by an erratum in the same journal: numbers live longer in retellings than in the original sources.

The comparison everything was counted for. The scale is confirmed eight out of a hundred, the model twelve. The model never left the band of the classical mode. The populations in the two studies are different, so this compares order of magnitude, not superiority; claiming superiority isn't allowed. And the reverse isn't true either: the model didn't fail — it landed roughly where the scale, which cost incomparably less, already stood. That "roughly where it already stood" is the actual result of this case study.

A second validation, by different authors and in different hospitals, adds something the first didn't measure — time. In the emergency department, it's the physician who recognizes sepsis: they examine the patient, order labs, start treatment. The validation compared the timing of the alert against the timing of that decision, across one hundred forty-five thousand eight hundred eighty-five visits to two departments in 2023. The median lead time was zero minutes; in roughly half the cases, physicians were already managing sepsis before the model spoke up. The authors' conclusion, verbatim: "adds little to what physicians are already doing." For the current version, validated prospectively across two hundred twenty-seven thousand ninety-one admissions in four systems, discrimination rose to a band of zero point eighty-two to zero point ninety-two, while confirmation stayed low — thirteen to twenty-six out of a hundred. The strength of evidence differs between these two validations, and that has to be stated: the first is retrospective, the second is prospective and multi-site.

What shifted. The alert now exists and runs without a human — around the clock, across every patient at once, from data that already sits in the record in machine-readable form. That's a real gain, and a specialist will take it: no scoring scale gets recalculated across the whole hospital every fifteen minutes. But reviewing and dismissing an alert became a separate line item of working time that didn't exist before this was deployed, and at some hospitals this step has its own staff now. The vocabulary form here is the fourth — the load grew at the same spot: same place, same hand, more reading and dismissing. The form "a step appeared" is about the review of the alert itself: with the scale, there was nothing to dismiss, since it computed its own threshold. And the form "same performer, now worse" doesn't apply to this case study, and this has been checked: no one measured the quality of the shift's work before and after the deployment, and such a measurement can't simply be invented, any more than a number can.

And one last figure that only reads correctly with its baseline; it sits on the slide as a pair, and the pair has to be said in full. Across twenty-four hospitals during a viral epidemic, the daily alert stream rose from nine hundred fifty-three to one thousand three hundred sixty-three — up forty-three percent. On its own, that means nothing: more patients, more alerts. But census over the same period fell from ten thousand one hundred fifty-nine to six thousand six hundred thirty-four patients — down a third. So alerts per patient didn't rise by forty-three percent — they rose by more than double: the share of patients with an alert rose from nine to twenty-one out of a hundred.

Here's what happened: the input distribution shifted — different patients, different illness — while the threshold stayed put, because no one recalculated it. The model didn't break and wasn't retrained; it kept computing the same thing it always had, on a flow that had changed. This carries over outside medicine almost without edits: at the exact moment the flow changes the most, the tool is wrong the most, and that's exactly the moment the organization has the fewest hands free to recalculate the threshold.

**Sources.** [Wong, Otles et al., JAMA Internal Medicine 2021, with erratum](https://doi.org/10.1001/jamainternmed.2021.2626) · [Ostermayer et al., JAMIA Open 2024](https://doi.org/10.1093/jamiaopen/ooae133) · [alert volume during the epidemic, JAMA Network Open 2021](https://doi.org/10.1001/jamanetworkopen.2021.35286)
