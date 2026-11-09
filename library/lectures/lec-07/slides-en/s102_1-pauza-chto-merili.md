---
# НОВЫЙ КАДР-ПАУЗА, прожарка сторителлинга #293, Этап C (П3, «Итоги»). Место — ПЕРЕД `s103`,
#   то есть перед кадром, который отвечает на вопрос вечера. Четыре свода «Итогов» идут
#   таблицами и ведомостями подряд; ответ, пришедший сразу за четвёртой таблицей, зал читает
#   как пятую. Тёмный кадр с одной фразой — пауза между счётом и ответом.
# НОМЕР `s102_1` — подномер между `s102` и `s103` (`deckkit/slidefile.py::order_key`). Буквенный
#   хвост здесь не годится: `s102a` встал бы после `s102`, но подномер вернее показывает, что
#   кадр вставлен, а не был пропущен в нумерации.
#
# ФРАЗА ПЕРЕПИСАНА ПРОТИВ ЗАКАЗА, И ПРИЧИНА НАЗВАНА ЗДЕСЬ, А НЕ В ПЕРЕПИСКЕ.
#   Заказ Этапа C просил вынести на этот кадр строку `s103` ДОСЛОВНО: «Исхода пациента нет ни
#   у одного разбора». Строка не выдержала сверки:
#     · `chapter-part5b.md` §11.5 (таблица градации замера) перечисляет поимённо разборы,
#       дошедшие до ступени «исход пациента», и первым — скрининг: интервальные раки
#       1,55 против 1,76 на 1000;
#     · `chapter-part2b.md` про тот же разбор: «И это единственный случай ЭТОГО РАЗДЕЛА, где
#       измерен исход пациента» — то есть утверждение всегда было раздела, а не вечера;
#     · заметки `s49d` уже ловили эту же ошибку в себе: «Говорить „исход пациента не измерен
#       ни в одном из четырёх" нельзя: у хирургов первичный исход заявлен прямо — сто
#       пятьдесят больных, тридцать дней проспективного наблюдения».
#   Мелким шрифтом на `s103` завышение прожило незамеченным. На 54 пт во весь тёмный экран оно
#   стало бы заявлением лекции — ровно того класса, который лекция весь вечер разбирает у
#   поставщиков. Поэтому фраза говорит, ЧТО мерили, а оговорка называет исключение и его
#   настоящий итог: не улучшение, а не-худшесть.
# ПАРНАЯ ПРАВКА НА `s103`: завышенная строка снята и оттуда — иначе сторож бы молчал, а
#   опровергнутое утверждение осталось бы на кадре (`CLAUDE.md`: отменил — поправь в том же
#   круге). Обещание дивайдера `s96a` («ответ стоит первым кадром закрытия») переписано там же.
id: s102_1
local_id: s9-00
section: "7. Закрытие"
type: udar
title: "What the lecture used to measure the person's work"
assertion: "Пауза между счётом и ответом: весь вечер измерялось поведение человека — куда смотрит взгляд, что он подписывает, сколько находок делает без помощника, — а до ступени «что это сделало с больным» дошёл скрининг, и там показана не-худшесть, а не улучшение"
source: "MASAI final analysis, The Lancet 2026 — https://doi.org/10.1016/S0140-6736%2825%2902464-X"
media: ""
media_needed: "иллюстрация не нужна и запрещена замыслом: кадр держит одну фразу во весь экран, любое изображение рядом отнимает у неё и площадь, и первый взгляд"
media_note: "кадр-пауза, тёмная заливка — второй тёмный кадр деки после удара `s01_1`. Тёмный экран здесь делает ту же работу, что и там: показ меняется целиком, и зал поднимает голову"
fraza:
  text: "We measured the person's work, not what happened to the patient"
  note: "screening is the one that reached the patient's outcome: 1.55 interval cancers against 1.76 per thousand — showing non-inferiority, not improvement"
  invert: true
timing_min: 0.25
in_bucket: true
method_steps: ["свод"]
form: []
vfy: true
status: собран
---

## Visible slide text

## Speaker notes

Here I stop for a few seconds, and the stop has content, it isn't for breath. The four summaries that just went by counted up the evening: nine forms of relocated work, thirteen attributions out of twenty-one breakdowns, a map of tasks and data types, a ledger of four payments. All four answer the question "what happened to the work." Before answering the question the evening opened with, we need to say out loud what answer we don't have.

Here it is. Almost everything measured tonight measured the person's behavior: where the eye looks and how long it stays in the right area, what share of the scan's area the radiologist covered, how many findings the doctor made without the assistant, what they signed and in how many seconds, how closely their conclusion matched the machine's. These are real measurements, taken by real methods, and half of them are randomized. But their subject is one thing — the work, not the person the work is being done for.

Now the caveat, and it's on the slide, not just spoken, because without it the line above would be exactly the kind of overstatement we've spent the whole evening catching vendors making. Two breakdowns reached the "what did this do to the patient" rung tonight, and the first of them was the Swedish screening trial: one hundred five thousand nine hundred thirty-four women, outcomes pre-registered. The result of that reaching has to be said in full, not halfway. Interval cancers — the ones found between two examinations, meaning the ones the program missed — came to one and fifty-five hundredths per thousand against one and seventy-six hundredths. The rate ratio is zero point eight eight, confidence interval from zero point six five to one point one eight. The interval straddles one. So what's shown is not improvement, but non-inferiority: the model-assisted regime is no worse than the old one, and this trial says nothing more than that.

The second is the surgeons' breakdown, and it, too, declared a primary outcome — one hundred fifty patients, thirty days of prospective follow-up. Its result stood on its own slide: on three outcomes out of four the pair was more accurate than the surgeon; on septic shock it lost, in the one place the human was stronger. So it did reach the outcome rung, and the verdict there was mixed.

Why this pause belongs right here, before the answer. The answer that's about to come is built as four rungs of participation and three grounds for the signature. All seven pieces of that answer talk about the person: what they manage to see, and what holds up the requirement that they stand in the loop at all. Not one of them says what changed for the patient because of it. The room has a right to know the boundary of the answer before the answer, not after.

And one last thing this pause does not mean. It does not mean the evening's measurements are worth nothing: an intermediate quantity is a normal rung of measurement, and the grading scale we've used all evening places it third of four, not at zero. What it means is something else: whenever a vendor says "the model improves outcomes," the question to them is the same one we just asked ourselves on this slide — at which rung was this measured, and does the interval straddle one.

**Sources.** [MASAI final analysis, The Lancet 2026](https://doi.org/10.1016/S0140-6736%2825%2902464-X)
