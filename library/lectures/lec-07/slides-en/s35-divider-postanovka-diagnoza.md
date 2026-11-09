---
# ВОЗВРАЩЁН ИЗ `_snyato/` (переделка раздела 2 по канону PR #286). Причина снятия, записанная
# в `_snyato/README.md` дословно: «следствие слияния разделов: у слитого раздела один дивайдер,
# и это `s22`». Слияние разобрано и отменено — значит отменена и причина снятия: стадия
# постановки диагноза снова отдельный раздел деки, со своим дивайдером, своими одиннадцатью
# кадрами (`s3-*`) и своим выводом (`s50`).
# ПЕРЕЧЕНЬ ПЕРЕСОБРАН под §5.16 ДОСЛОВНО по заголовкам кадров — прежний перечень цитировал
# имена, которых на кадрах уже не было («измеренная тройка», «контрольная линия», «хирурги на
# септическом шоке»), а нумерация уехала на 4–8 из-за слияния. Сверено 2026-10-19 по `title:`:
# s41 «замер взгляда» · s44 «патологи читают срезы» · s47 «шведское испытание» · s49b «хирурги
# оценивают риск» · s49e «модель раннего предупреждения о сепсисе».
# ПЯТЫЙ РАЗБОР НАЗВАН ПО СВОЕЙ РАБОТЕ, А НЕ ПО СТАДИИ: он пришёл из стадии наблюдения, снятой
# владельцем 2026-10-15, и стоит здесь по его же указанию. Ярлык «непрерывное наблюдение» —
# это работа, а не место в сетке; вынести на кадр, что раздел снят, нельзя (§7.1).
id: s35
local_id: s3-01
section: "3. Постановка диагноза"
type: divider
title: "3. Diagnosis"
assertion: "Заключение по данным выносит человек, и читает он теперь не только снимок, но и подсказку модели рядом с ним"
source: "—"
media: "rework/deck/assets/s35-vrach-chitaet-s-ekrana.jpg"
media_needed: "Фотография: два врача-радиолога у одного экрана с медицинским изображением и подсказкой/аннотацией модели рядом. Нужен подлинный, узнаваемый снимок (пресс-фото больницы, фотобанк с указанием контекста съёмки), не постановочная стоковая иллюстрация с актёрами в белых халатах."
media_note: "вкручен кабинет чтения: ОДИН врач за двумя мониторами, модальность — томография. Поле просило двоих у одного экрана; в видимом тексте слайда ни числа читателей, ни модальности нет, и подпись под снимком переписана под то, что на нём. Права: CC BY 4.0 (Wellcome Collection), deck/images.md §3.1 РАСХОЖДЕНИЕ СНИМКА И ЗАМЕТОК — найдено сплошной сверкой О12 2026-10-14, правится НЕ здесь. Абзац заметок утверждает «врач за двумя мониторами, исследование на одном, РАБОЧИЙ СПИСОК НА ДРУГОМ». Снимок открыт и просмотрен: на ОБОИХ мониторах срезы компьютерной томографии, рабочего списка нет ни на одном. Остальное в абзаце верно — врач один, два монитора, диктофон в руке. Снимать надо придаточное про рабочий список, а не снимок. Заметки за границей добычи."
timing_min: 0.6
in_bucket: false
method_steps: ["дивайдер"]
form: []
vfy: false
status: собран
---

## Visible slide text

# 3. Diagnosis

**There, the stage produced values — here, a finding is made from them, and a human signs it.** He now reads not only the image, but also the cue next to it: the order in which they are presented affects the outcome.

In order:

**Example 1: eye-tracking — with a false cue and with a correct one**

**Example 2: pathologists read slides — with a cue and without**

**Example 3: the Swedish trial — the second human reading replaced by a model**

**Example 4: surgeons assess risk — on their own, and after seeing the model**

and, carried over from continuous monitoring, **Example 5: an early-warning model for sepsis**

**Example 6: Moscow, Russia — a model proposes a final diagnosis from the medical chart**


## Speaker notes

This section crosses the same boundary that separated the second section from the first, only from the other side: the data has already been measured and read by the system, but a human signs the finding. The cue sits next to the image, and this section's question is what the human actually looks at after that — the image itself, the cue, or by now a habit of trusting the screen. The industry calls this stage diagnosis, and it settles one question: what explains the finding. Its decision is to name the disease and sign for that name.

Without a trained model, this stage is held up by three regimes, and all three get their own slides further on. Reading by a single specialist, with a signature. Double independent reading, where two people look separately and do not know each other's opinion. And arbitration — a third person who works through a disagreement. Independence here is not politeness, it is a condition: the moment the two share a common source of a cue, the second opinion stops being second, and the measured discrepancy rates show it.

The six breakdowns run in increasing order of exactly what is measured, and they are worth naming here, so the slide gets recognized later by a name already heard.

The first is eye-tracking. The same reader, on the same mammograms, misses twice as many cancers where the cue stayed silent; this shows up in eye movement — a false cue narrowed the visual search. The same slide carries the same quantity with the opposite sign: in a different program, where the reader requests the annotation himself, missed cancers went down. Both halves sit on one slide deliberately: without the second, the first breakdown reads as a failure rather than a measurement of a mechanism, and the sign of the effect is set not by the cue itself but by whether it is correct.

The second is pathologists reading slides. The same mechanics of the effect, carried over from the eye to the decision: the same cue raises the odds of a correct answer fourfold when the model is right, and drops them fourfold when it is wrong, while the gain across the group as a whole is not significant. A report with one number would show "no effect" here — and that is the most useful thing this section can say about averaging.

The third is the Swedish trial. The only randomized trial in this section with preregistered outcomes, and the only breakdown where the pair came out stronger than either side alone: one human reading on top of the model, with arbitration on disagreements, against double human reading — with half the human reading.

The fourth is surgeons assessing risk. The breakdown that was promised in the previous lecture. On three outcomes out of four, the pair is more accurate than the surgeon alone, and on septic shock — the one outcome where the human had his own edge — it dropped below both the human and the model.

The third and fourth stand next to each other deliberately: the tool is the same, and the results are opposite, and what diverges between them is not the model but the mechanics of the procedure — whether the independence of the two opinions is preserved, and in what order the cue is presented.

The fifth is an early-warning model for sepsis, and it is the only one in this section where the decision is made continuously, rather than on a single case. It comes from the continuous-monitoring stage, which does not run as its own section in this lecture, so on the divider it is named by its own job, not by its place in the cycle. This breakdown rests on two bases that must not be confused: an alarm is raised for eighteen hospitalizations out of a hundred, and twelve out of a hundred raised alarms get confirmed. To find one case, a shift has to work through eight alarms. The classical regime here is not zero — it is a point scale computed by hand, and it was confirmed eight out of a hundred against twelve for the model — the model never left that band.

Between the breakdowns sit two unnumbered slides, and they have no number for a reason, not by oversight. A cardiogram with an incorrect machine readout answers the question of what trust is calibrated against, and does not assign a cost to either error. A review of a hundred and six experiments draws a rule from other people's measurements: where the pair beats the human and where it falls below the model. Neither of the two fits the form of a detailed breakdown, and passing them off as breakdowns would double-count.

This section holds one through-line, and it is worth naming before the breakdowns. The "human plus model" pair is not equal to either the human or the model alone, and which side will tip the balance cannot be said in advance — it has to be measured. Usually, though, anything but this gets measured: the model's accuracy separately, the physician's satisfaction separately, and the third quantity, the one the pair was actually assembled for, is counted by nobody.

The "task × data type" grid is not drawn section by section — it is assembled once, in the wrap-up, across all sections at once.

The image alongside is a real reading room: a physician at two monitors, both showing CT slices, a voice recorder in hand.
