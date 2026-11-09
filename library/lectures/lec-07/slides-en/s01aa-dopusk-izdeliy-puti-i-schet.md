---
# СЛИТЫЙ КАДР, прожарка сторителлинга #293, Этап A. Было три кадра — механизмы допуска
# (`s01aa`), счёт изделий (`s01ab`), применение (`s01ac`); стало два: этот и `s01ac`.
# Сюда сведены механизмы допуска и счёт изделий, туда — применение и поток.
# ЧТО СНЯТО С ВИДИМОГО СЛОЯ И КУДА: подробности американских классов риска, сроков
# рассмотрения, освобождений и российских форм оценки — в заметках, где они и были.
# Число «3,1 по-настоящему новых изделия в год» переехало сюда строкой тела со своей базой
# и ОСТАЁТСЯ ЗДЕСЬ.
# ПОПРАВКА ЭТАПА E (решение владельца 2026-10-22): кадр `s01ab` ВОЗВРАЩЁН переработанным —
# страновой ряд снова стоит на экране, следующим кадром, и у каждой его строки назван свой
# признак отбора. Здесь стояло, что ряд снят и произносится голосом; это больше не так, и
# абзац заметок, который так говорил, переписан. Разделение простое: на этом кадре — ПУТИ
# допуска и счёт по ним (1 553 · 21 · 3,1 в год), на `s01ab` — СОСТАВ массива и страны.
# Ни одно число не стоит на обоих.
id: s01aa
local_id: В-01aa
section: "0. Вход"
type: analitika
title: "Device clearance for a model-equipped device: paths and counts"
assertion: "Без регистрационного удостоверения изделие нельзя ни применить на человеке, ни купить за бюджетные деньги; в США дорог две — короткая по похожести на уже допущенное изделие и полный цикл с собственными клиническими испытаниями, — и 1 553 изделия с ИИ из 1 614 прошли короткой, 21 полным циклом; короткого пути в России нет, регистрация целиком идёт от 0,6 до 3 млн рублей по классам; по-настоящему новых изделий прибавляется 3,1 в год, и эта линия не ускоряется"
source: "Полная запись источников в репозитории курса · допуск в США, ступени и доли — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/09a-dopusk-usa-puti-i-doli.md · допуск в России — https://github.com/tellina-study/AI-usage-lessons/blob/main/library/lectures/lec-07/rework/research/09b-dopusk-rossiya.md"
media: ""
media_needed: "снимок страницы решения о допуске — настоящее письмо о клиренсе 510(k) рядом с российским регистрационным удостоверением; два документа, по которым изделие попадает к человеку"
media_note: "свидетельство, а не оформление: два документа разной силы рядом. Места под иллюстрацию на кадре сейчас нет — схему трёх порядков и полосу плашек экран занимает целиком"
scheme:
  caption: "The full US track is close to the Russian one; Russia has no short track"
  arrows: true
  rows:
    - {label: "US, short track", steps: ["Application", "Resembles a predicate device", "Clearance"]}
    - {label: "US, full cycle", steps: ["Application", "Trials", "Review", "Clearance"]}
    - {label: "Russia, all classes", steps: ["Trials", "Toxicology", "Clinical data", "Review"]}
blocks:
  - {label: "Via the short track", value: "1,553 of 1,614", note: "by resemblance to an already-cleared device"}
  - {label: "Via the full cycle", value: "21 of 1,614", note: "with the device's own clinical trials"}
  - {label: "Registration in Russia, all-in", value: "RUB 0.6–3 million", note: "class 1 → class 3", key: true}
timing_min: 0.75
in_bucket: true
method_steps: ["заземление", "описание порядка", "счёт с базой"]
form: []
vizforma: "ряды"
vfy: true
status: собран
---

## Visible slide text

**Without a registration certificate, a device cannot be used on a person or bought with budget money.**

**Truly new devices are added at a rate of 3.1 a year:** 56 by the end of 2025, against 7 in 2010. The rest of the growth comes through resemblance to a predecessor.

## Speaker notes

Device clearance is a question an engineer on a medical project hears before the question of the model's accuracy. Until a device is cleared, it cannot be applied to a person at any level of accuracy; after clearance, nobody revisits the accuracy until the next change to the device.

Let's start with the American side, because more machine-learning devices have gone through it than through any other. There, devices are split into three classes by risk to the person; the class is assigned to the type of device, and it is what determines the mandatory clearance track — the path is chosen long before the developer writes the first line of code. On the short track, the manufacturer does not prove safety and effectiveness from scratch: it proves that its device is substantially equivalent to an already legally marketed one. The comparison covers intended use and technical characteristics, sometimes bench data, rarely minimal clinical data; this track almost never requires prospective trials, nor a long-term patient outcome. The full cycle requires the device's own clinical data and a full manufacturing dossier, and for significant applications, also a public hearing before an outside panel.

The Russian track is built differently at both ends. There are four classes, and they are assigned by duration of use and invasiveness, not by intended purpose: two devices with the same intended use can get different classes. Toxicology studies are mandatory at every class, including the first. Clinical trials come in two forms, and this part is worth reading straight from the order's own wording: trials involving people are required when the device is of a new type, when new, complex, or unique methods are used, and when an analysis of clinical data has not confirmed effectiveness and safety. Further on, verbatim: "In all other cases, clinical trials of medical devices are conducted in the form of an analysis and evaluation of clinical data." The gate here is the novelty of the device or method; there is no mention of risk class in this clause at all, nor of whether a registered analogue exists. And there is a last stage the short American track does not have at all: a state review of quality, effectiveness, and safety, commissioned by the oversight body, not by the manufacturer's own application. The basis for registration is phrased with the conjunction "and": trial results *and* review.

The price in money. For review on the short track in the US, the applicant pays $26,067; for the full cycle, $579,272. The Russian review fee is tied to the class: from 72,000 to 184,000 rubles plus 11,000 for issuing the certificate. The figure on the slide, 0.6 to 3 million, is not the fee — it is the full "turnkey" cost of registration: an estimate from registration intermediaries, in which the fee is only one part, the rest being the lab, toxicologists, and dossier preparation.

Now the count of devices, and the figures are taken by direct reading of the regulator's own table, not from an industry digest: digests on this subject disagree with each other by hundreds of devices. In the list as of 17 October 2026 there were 1,614 devices with a trained model, and every share from here on is counted from that number. 1,553 went through the short track — 96.2%. 40 got a new class with no predecessor. 21 devices went through the full cycle with their own clinical trials — 1.3%, while across all medical devices over the system's history, the share going through the full cycle is about 1.87%: for devices with a model, it is even lower than average. The practical meaning of this fraction is this: a typical model reaches the clinic by proving resemblance to an already-cleared device, while nobody measures patient outcomes along the way.

And about the figure on the slide — 3.1 truly new devices a year. If you remove the short track and count only devices cleared with no reference to a predecessor, the cumulative count gives 7 by 2010 and 56 by the end of 2025. Plus 49 over sixteen years, 3.1 a year on average, and the line does not grow year over year: 7 · 2 · 7 · 10 · 6. The short track adds to the pool fast; genuine novelty adds about three devices a year, and it is this second line that is worth keeping in mind when thousands of cleared devices are quoted.

If asked right now why the countries can't be lined up against each other: no single international definition of a "truly new device" exists, and each country counts by its own criterion.

**Sources.** [FDA, AI/ML-Enabled Medical Devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices) · [Ministry of Health Order No. 2n, published in Rossiyskaya Gazeta](https://rg.ru/documents/2014/04/23/minzdrav-dok.html) · [Order No. 885n, Ministry of Justice document](https://polimertest.ru/gallery/gallery-Prikaz_ot_30_08_21_N_885n_.pdf) · [Russian Tax Code, art. 333.32.2](https://pravo.ppt.ru/kodeks/nk/st-333.32.2) · [FDA, MDUFA Performance Goals](https://www.fda.gov/media/158308/download) · [Korea, count of 549](https://www.etnews.com/20260410000195) · [Korea, reimbursement 49 of 549](https://www.dataeconomy.co.kr/news/articleView.html?idxno=42899) · [China, clinical evaluation pathways](https://medinform.jmir.org/2026/1/e85538) · [Webiomed](https://webiomed.ru/novosti/sistema-webiomed-stala-pervoi-rossiiskoi-razrabotkoi-v-oblasti-iskusstvennogo-intellekta/)
