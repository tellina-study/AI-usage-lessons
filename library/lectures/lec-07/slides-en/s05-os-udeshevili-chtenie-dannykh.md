---
id: s05
local_id: В-05
section: "0. Вход"
type: summary
title: "Example of a human–AI system at work: 50 doctors read case write-ups"
assertion: "Несущая ось лекции: удешевление одного шага оплачивается на четырёх других, и все четыре адреса платежа — работа человека"
source: "Goh et al., JAMA Network Open 2024 — https://doi.org/10.1001/jamanetworkopen.2024.40969"
media: "rework/deck/assets/s05-podpis-pod-soglasiem.jpg"
media_needed: "добыт: подпись под документом в клинической обстановке — устройство, которым процедура удерживает цену ошибки"
media_note: "настоящий снимок, не стилизация; расхождение с планом названо в s05-podpis-pod-soglasiem.url"
scheme:
  kind: shkala
  unit: "median structured-reasoning score, % of maximum"
  caption: "the gap between the pair and the solo human is 2 points, not significant"
  marks:
    - {value: 92, label: "Model alone"}
    - {value: 74, label: "Human alone"}
    - {value: 76, label: "Human on top of the model", key: true}
pol_slov: 142   # О10/О13/О20/О21 (#229) — история правок кадра в журнале решений, здесь состав ПОСЛЕ правки по п.8 владельца. Чем заняты слова: тройка 92 · 74 · 76 со своей базой и единицей (балл структурированного рассуждения) · описание опыта целиком — кто и сколько, что делали глаголом, чем мерили, что распределяли жребием (§5.13, «читается без голоса») · разряд третьего числа («модель одна» в жребий не входила) · формула оси и четыре адреса платежа · вопрос лекции. СНЯТО по п.8 (владелец, 2026-10-15): лозунг из заголовка — заголовок теперь называет предмет кадра дословно его словами («Пример работы системы человек–ИИ»), а формула оси переехала в тело одной строкой (+3); строка «Младшие разработчики пишут с моделью больше, старшие не успевают проверять. Этого никто не измерял» снята целиком (−14) вместе с абзацем заметок, который её оправдывал: владелец велел убрать её и «вычистить подобное везде». Пол опущен 158 → 145 по этому вычету, выше прежнего не поднимался ЗАМЕР ПО СОБРАННОМУ PDF полосы Входа и раздела 1 (render_sec.py 0 1, 2026-10-15, 14 страниц): 142 слов на этом кадре; медиана полосы 142,5, максимум 263, блокирующих 0. Поле выставлено ПО ЗАМЕРУ, не по оценке: прежнее число в этой строке называло состав до правки по замечаниям владельца и после неё было бы разрешением на чужой вес.
timing_min: 1.15
in_bucket: false
method_steps: []
form: ["ось", "вопрос лекции"]
vizforma: "ось"
vfy: false
status: собран
---

## Visible slide text

**Three seconds and zero rubles, against 48 seconds of human reading.** *The units are different — the comparison is only on order of magnitude.*

**How it was measured.** Fifty practicing doctors each read five real case write-ups and built out their reasoning: hypotheses, justification, which tests to order. They were scored blind, on a structured-reasoning scale. The two human conditions were randomized; "model alone" was not part of the randomization.

**Reading the data got cheaper — it's paid for by a step the human does.**

**What pays for it:** attention — looking after the model · skill — stops doing it themselves · signature — put down without reading · **arbitration — now costs more than the old reading did**. And the check of the suggestion itself has been measured: **1.99 seconds** by median.


**The model looked first. What does the person do now — and who measured that?**

## Speaker notes

There's one number I'm naming here that I'll name three more times tonight, because it measures the fourth payment — the one that looks the most harmless. Arbitration now costs more than the old reading did; we'll get to that at the screening stage. But how much the check of the suggestion itself costs has been measured — one and ninety-nine hundredths of a second by median. I'll give the base right away, because without it the number sounds stronger than it is: the measurement is from a lab, and taken outside medicine entirely — twenty-one programmers, one thousand ninety-six code-assistant suggestions shown, behavioral telemetry. This is the time the person keeps the suggestion on screen BEFORE deciding to accept it. The same study has a second median alongside it, six and forty-eight hundredths of a second, and the two must not be confused: that one counts the check AFTER acceptance. The question "does the person have time to read before they sign off" is answered by the first. Carrying this over to a doctor is done by analogy, and I'm calling it an analogy.

Reading medical data has come to cost three seconds and zero rubles — against 48 seconds of human reading on average, 25 by median. The units behind these two figures are different: a chest X-ray and a mammogram are read differently, so the comparison only holds at the order-of-magnitude level, and that's exactly how it's labeled on the slide. The tool opens in a browser, the computation runs on the same laptop, the scan never leaves for a server, and there's no barrier to entry at all. What follows is what sits on the other end of this cheapening, and there are four addresses where the payment lands.

The trio on the row of plates is one measurement, and it has to be named in full. Fifty practicing doctors read written descriptions of real cases — complaints, history, test results already in hand — five cases per doctor, and built out their reasoning: hypotheses, justification, which tests to order. They were scored blind, on a structured-reasoning scale, and two human conditions were randomized: the doctor as usual — seventy-four out of a hundred; the doctor on top of the model — seventy-six. The two-point difference is not statistically significant: p equals zero point six zero, meaning a gap this size happens freely by chance, and it cannot be called a gain. The model running alone — ninety-two — was not a randomized arm and carries less weight as evidence. From here comes the short formula by which the whole lecture reads: ninety-two was bought, seventy-six is what actually works, and the difference between them doesn't show up in the reporting. The trial names the reason for the null result itself: the suggestion arrived ready-made, and no one taught the doctors how to question it and when not to trust it. The tool was handed over; the procedure for working with it was not.

Attention. The person looks after the model, and their visual search narrows — this has been measured by eye movement, and in both directions: with a correct suggestion, the area of the scan scanned by the eye shrinks, and reading quality goes up; with a suggestion that missed a finding, the area scanned shrinks the same way, and reading quality collapses.

Skill. The person stops doing on their own what they'd done for years. This was measured by disabling the assistant: the detection rate in procedures done without it, among those accustomed to it, turned out lower than it had been before the assistant ever appeared. The body of evidence here is weaker than for the other three, and it's worth naming that weakness plainly: in real work, the consequence has been measured once, and it's disputed; the same phenomenon has been measured by random assignment in a training setting, but on real work there isn't a single replication.

Signature. The person confirms a decision they didn't read. The requirement that a person remain the last link is written down by the regulator; a check of that requirement itself was found at 56 of 717 radiology devices — eight percent.

Arbitration. Resolving one disagreement now costs more than the old reading did: a scan takes 48 seconds on average, 25 by median — resolving a disagreement on arbitration takes two minutes twelve seconds, that is, five readings. And as first human readings were cut in half, the volume of arbitration grew by more than half.

Half of this axis is already familiar to the course from the last lecture: a step gets cheaper, and the bill is paid somewhere else. What's new here is one thing, and it's the whole reason the axis is announced — the address of the payment. It's paid in the step a human does, not in money, and not in compute time.

Now about how these four words keep living on, because hearing them once isn't enough. The course already knows the vocabulary of forms the process can be affected by, from the last lecture, and its nine names carry almost every breakdown that follows: "the load moved to a different step," "the operator changed," "the cost of error shifted." The four payment addresses don't replace or repeat that vocabulary — they answer a different question about the same case. A form says what happened to the work: where it now sits, how much of it there is, whose hand does it, what an error ends in. An address says at which human step this happened: do they look second now, have they stopped doing it themselves, did they sign something unread, are they handling a disagreement as a step that's new.

From here comes the order every breakdown follows from now on. Each one ends with a form — or with a named refusal to assign one, and that refusal is as much a verdict as a name is. In the summary, forms are mapped back onto the four addresses, and that mapping is done by count: against every address stands a measurement with its stated order of magnitude. Both halves need to be held in mind: a form measures the work, an address measures the person. They must not be mixed up: work can move in a way no human step ever feels, and a person can pay where the work never moved at all.

**Sources.** [Goh E. et al., JAMA Network Open 2024;7(10):e2440969, 28 October 2024](https://doi.org/10.1001/jamanetworkopen.2024.40969) · [photo: NIAID, Wikimedia Commons, CC BY 2.0](https://commons.wikimedia.org/wiki/File:Clinical_Trial_Volunteer_Signs_Informed_Consent_Form_%2845116548901%29.jpg)

The relocation of work has nine forms, and the full list will be presented at the first breakdown.
