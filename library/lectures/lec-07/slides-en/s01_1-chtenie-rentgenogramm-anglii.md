---
# НОВЫЙ КАДР, прожарка сторителлинга #293, Этап A. Место — ВТОРОЕ, сразу за обложкой: зал
# получает масштаб отрасли раньше любого словаря. Номер `s01_1` — подномер между `s01` и
# `s01a`; буквенной схемой это место недостижимо (между пустым хвостом и `a` строк нет), см.
# docstring `deckkit/slidefile.py::order_key`. Московские 55 из 100 сюда НЕ взяты намеренно:
# это удар раздела об инструментальной диагностике, и предъявлять его дважды значит потратить
# его впустую.
# РАЗНОЧТЕНИЕ ЗНАМЕНАТЕЛЯ — В ЗАМЕТКАХ, НЕ НА КАДРЕ (§7.1/§7.2): на кадре стоит та пара, у
# которой знаменатель опубликован таблицей с методикой; вторая официальная версия («свыше
# семи миллионов») названа в заметках вместе с тем, кто какое число произносит.
id: s01_1
local_id: В-01_1
section: "0. Вход"
type: udar
title: "Reading chest X-rays in England"
assertion: "Отрасль уже живёт так: из 8,19 млн рентгенограмм грудной клетки, выполненных в Англии за год к марту 2024 года, около 2,8 млн прочитала обученная модель — то есть каждый третий снимок открывает не человек первым; вопрос вечера не «придёт ли модель», а что теперь делает человек"
source: "NHS England, Diagnostic Imaging Dataset Annual Statistical Release 2023/24, table 6 — https://www.england.nhs.uk/rightcare/wp-content/uploads/sites/2/2024/11/DID-Annual-Statistical-Release-2023-24.pdf"
media: ""
media_needed: "иллюстрация не нужна и запрещена замыслом: кадр держит одну величину во весь экран, любое изображение рядом отнимает у неё и площадь, и первый взгляд"
media_note: "кадр-удар, тёмная заливка: единственный тёмный кадр деки, и тем он и работает — после белой обложки экран меняется целиком"
figure:
  value: "2.8 million"
  unit: "chest X-rays read by the model in a year"
  base: "out of 8.19 million taken in England in the year to March 2024"
  invert: true
timing_min: 0.35
in_bucket: false
method_steps: ["заземление"]
form: []
vfy: true
status: собран
---

## Visible slide text

## Speaker notes

In England, in the year ending March 2024, 8,194,405 chest X-rays were taken — across all referral routes, not just suspected-cancer cases. A trained model read about 2.8 million scans out of that flow. Roughly every third chest X-ray in the country is now opened first by something other than a person. That is the evening's first number, and it settles the question of whether this is already happening at all.

The numerator and the denominator come from different hands, and that is worth knowing before stating the share. 8.19 million is official health-service statistics, an annual report on diagnostic imaging, a table with a published counting method. 2.8 million is the figure named by the tool's developer. The government does not give its own numerator at all: it states something else — the tool is in use in roughly half of England's trusts, and four million people got either a diagnosis or the lifting of a suspicion faster.

And the denominator itself has a second official version. A government announcement about the same rollout speaks of "over seven million chest X-rays a year." The gap between the two government figures is more than a million scans, and the resulting share moves between thirty-four and forty out of a hundred. The figure on the slide is the pair whose denominator is published as a table; there are, in fact, two official denominators, and the room has a right to know that. These two bases are examined in more detail in the conversation about instrumental diagnostics — along with why the share of trusts and the share of scans do not have to match: a trust can be connected and still send through only a small part of its flow.

From here, the whole evening is about one thing: what the person does within this picture. The scan has been read, and not by them. The model's accuracy will get its own number with its own base in every breakdown; the evening's question is what happens to the procedure that has, until now, held down the cost of error — double reading of a scan by two independent readers, a colleague's second opinion, arbitration on disagreement, a signature under the report, a case review after the outcome. Not one of these devices was invented for machine reading, and none was invented against it; all of them exist because one person makes mistakes, and the procedure already knows that.

A large number, on its own, says nothing about either benefit or harm. Two-plus million scans read is not "the model saved two million people" and not "two million people were left without a doctor." It is a volume, and only a volume. What exactly changed for the doctor, the patient, and the department — the volume does not say; it says that the time has come to answer that question.

Russia belongs in the same picture, and its numbers are worth stating alongside. Moscow's radiology diagnostic services have, in cumulative total, processed more than eighteen million studies, about 1.4 million a month, and roughly eighty percent of them come from the regions. Nobody here has a share of the nationwide flow: no one publishes the number of scans done per year across the country, and the "about a quarter" estimate circulates in official statements with no denominator at all. An estimate from a denominator that does not exist is not an estimate, which is why England stands first on the slide: it has both halves of the fraction.

If the room asks about the United States — figures of this kind are not published there at all. Two other quantities are published: how many devices with a trained model have been cleared over the entire history, and what share of doctors say they use a model. Neither has anything to do with the share of the flow actually read, and they cannot be added to the English share.

What to take from this slide: the industry is already living this way. The evening's question is what the person does now, and who measured that.

**Sources.** [NHS England, Diagnostic Imaging Dataset Annual Statistical Release 2023/24, table 6](https://www.england.nhs.uk/rightcare/wp-content/uploads/sites/2/2024/11/DID-Annual-Statistical-Release-2023-24.pdf) · [UK government announcement, 10 June 2026](https://www.gov.uk/government/news/ai-to-speed-up-cancer-diagnosis-for-millions-of-nhs-patients) · [Vasilyev et al., *Digital Diagnostics* 2025;6(1):5–22](https://doi.org/10.17816/DD641703)
