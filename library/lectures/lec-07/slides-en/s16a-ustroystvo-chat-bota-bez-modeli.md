---
# ВСТАВКА (issue #270, доработка инженерной глубины разбора по §2 obzor-stran-i-glubina-razbora.md).
# Продолжение разбора s16 («Пример 1: чат-бот первой линии вместо звонка в практику»), не новый
# кейс — отмечено полем `razbor_part`. local_id СОЗНАТЕЛЬНО не `s1-07a`: этот номер плана уже занят
# историей — файл `_snyato/s17-arifmetika-kanala.md` несёт `local_id: s1-07a` и документированную
# инструкцию возврата («Как вернуть `s17`», `_snyato/README.md`); использование той же строки здесь
# для другого содержания сломало бы этот документированный адрес. Взят следующий незанятый суффикс
# `s1-07b`. `id: s16a` — адрес показа (кадр встаёт сразу после `s16`), из другого пространства
# имён, и коллизии с `local_id` не образует (см. `make_deck_yaml.py`: буквенный хвост любого вида
# читается как «вставка, номера в плане нет»).
id: s16a
local_id: s1-07b
section: "1. Первичный скрининг и отбор на обследование"
type: case
title: "Example 2, the architecture: who said what about what's inside Babylon"
assertion: "Собственная техническая публикация компании — разряд свидетельства выше, чем слова участника на s16, но не аудит — описывает не обученную модель, принимающую решение, а вероятностный граф первичной помощи с жёсткими правилами для красных флагов поверх него; нейросеть здесь считает быстрее, а решение не принимает; выход — один из шести взаимоисключающих вариантов; кто и как часто переписывает правила графа после ошибки, источники, включая публикацию самой компании, процессом не называют"
source: "Middleton et al., arXiv:1606.02041, 2016 — a publication by the company itself"
media: ""
media_needed: "иллюстрация не нужна структурно: кадр держат два разряда свидетельства, полоса шести исходов и схема «обычный путь / красный флаг» (с issue #270 r3 заменила словесное объяснение графа и правил в теле)"
media_note: "—"
razbor_part: "2 из 2; ①цена обеих ошибок, ②классические режимы, ③экзамен как основание, арифметика канала и пара дало–потребовало — на s16; здесь — ТРИ свидетельства о внутреннем устройстве порознь (Харви, Уоткинс, публикация компании), ④как это устроено и честно названный пробел в контуре обратной связи. Разведение Харви и Уоткинса стоит здесь по требованию главы: `chapter-part1b.md` называет их смешение в одно «он же» отдельной ошибкой атрибуции, и этот раздел — про силу свидетельства, то есть деталь не второстепенная"
blocks:
  - {label: "The decision output is one of", value: "6 options", note: "from 'call an ambulance' to 'you can handle it yourself'", key: true}
scheme:
  caption: "A red flag bypasses the graph entirely"
  arrows: true
  rows:
    - {label: "The ordinary path", steps: ["Symptoms as input", {text: "The graph computes — the neural net makes it faster", ai: true}, "One of the outcomes as output"]}
    - {label: "A red flag", steps: ["Symptoms as input", "A rule — bypassing the graph", "Always: an ambulance"]}
pol_slov: 155   # ЗАМЕР ПОСЛЕ R3 (issue #270, круг доводки 3): title и первая строка тела
  # названы по случаю (Babylon, «GP at Hand», чат-бот триажа первой линии), добавлена
  # схема «обычный путь / красный флаг» (2 ряда × 3 шага, явный `ai: true` на шаге
  # «Граф считает — нейросеть быстрее»: в этой деке `ai_by_word=False`, золото
  # угадыванием не ставится), тело прозы сокращено с 116 до 68 слов. ЗАМЕР ПО
  # СОБРАННОМУ PDF раздела 1 (render_sec.py 1, 2026-10-19, 14 страниц): 155 слов на
  # этом кадре; медиана полосы 156, максимум 259 (`s16`), блокирующих 0
  # (`build_lec07.py --only s15,s15a,s16,s16a,s18,s18a,s18b`). Поле выставлено ПО
  # ЗАМЕРУ, не по оценке.
  # ПРЕЖНЕЕ ЗНАЧЕНИЕ (issue #270, новый вставной кадр. ЗАМЕР ПО СОБРАННОМУ PDF раздела 1 (render_sec.py 1, 2026-10-18, 11 страниц): 162 слов на этом кадре; медиана полосы 177, максимум 286 (`s13a`), блокирующих 0 (`build_lec07.py --only s16,s16a`)). Снято как сказанное дважды: список шести исходов стоял и в плашке, и в теле дословно — в теле заменён на одну строку без перечисления (плашка несёт список). Чем заняты слова: два разряда свидетельства явно разведены (слова участника — на s16; опубликованная архитектура — здесь) · граф + жёсткие правила для красных флагов + роль нейросети только в скорости вычисления · плашка шести взаимоисключающих исходов · контур обратной связи назван пробелом явно, с указанием, чего именно не нашли (кто и как часто переписывает правила, без привязки к инцидентам) · итоговое утверждение «системного дизайна обученной модели… здесь не было вовсе».
timing_min: 0.75
in_bucket: true
method_steps: ["④как это устроено (опубликованная архитектура)"]
form: ["форма 1"]
vfy: false
status: собран
---

## Visible slide text

**Three people spoke, and that's not one source.** **Hugh Harvey**, the company's head of regulatory affairs in 2016–2017: inside, a decision tree of "if-then" rules in a table. **David Watkins**, a doctor outside the company: he's been writing to the regulator about missed cases since 2017. **The company itself**, a 2016 publication: a probabilistic graph plus hard-coded rules for red flags on top of it — on the diagram.

**Words from the inside · letters from the outside · the company's own publication. Not one independent check exists.**

**A trained model making the decision was never here at all.**

## Speaker notes

What actually stood inside the first-line chatbot is not reliably known, and three people have spoken about it — with different standing to speak. They have to be kept apart before anything else: folding three testimonies into one "same thing" is exactly the mistake this case is examined to catch. Hugh Harvey worked at the company as head of regulatory affairs for clinical AI in 2016–2017; his public claim — that inside the "AI algorithm" sat a decision tree of "if-then" rules in an ordinary table — is words from a person inside, about the internal construction. David Watkins never worked at the company: a general practitioner, he's documented recognition misses since February 2017 and reported them to the regulator, escalating the complaint to "critical" by 2018 — that's testimony from outside, about the system's behavior, not about its internals. Folding them into one "same thing" is an attribution error, and it stood twice in drafts of this very chapter; a section that teaches people to ask where a claim came from has to be precise about who made it. The third testimony is the company's own technical publication from 2016, and it can be trusted differently: not an independent check, but also not one person's recollection. The company itself has its own technical publication from 2016, and it can be trusted differently: it's not an independent check, but it's also not one former employee's account — it's what the company itself published about its own architecture. These two testimonies must not be confused: the "if-then" decision tree is a participant's words; what's described below is a published architecture.

The publication describes the system as a probabilistic graphical model of primary care: a directed acyclic graph in which diseases and symptoms are connected by prior probabilities and conditional dependencies. The structure of the graph — which nodes connect to which — is built and checked by expert physicians, not by lone engineers. This is already not the "if-then" decision tree in a table the participant talked about; it's a probabilistic model with its own structure.

But on top of the probabilistic part sits a separate mechanism, and it must not be confused with the graph itself. For a defined list of "red flags" — specific symptom combinations — the triage decision isn't derived by probabilistic reasoning at all; it's forced by a hard rule: such a combination leads straight to "call an ambulance," regardless of what the probabilistic part is showing at that moment. And separately from both parts, the publication mentions a neural network, but its role there is just one thing: it speeds up computation on the probabilistic model — it doesn't replace it, and it doesn't make the decision itself. Of the three components — the graph, the hard rules, the neural network — a trained model making the decision isn't in any of them.

From here follows a direct conclusion, and it stands as a statement, not as a caveat about missing material: the systematic design of a trained model making the decision — the thing this lecture's other engineering cases all require — simply was not here at all. This isn't a search gap: it's the honest answer to "how was the engineering built," for this particular case.

On output, the system didn't give a binary "yes/no" — it gave one of six mutually exclusive options: call an ambulance, go to urgent care, see a doctor urgently, see a doctor without urgency, go to a pharmacy, self-care. Six outcomes, not two — and that's also part of the architecture, not a detail of presentation: the more distinguishable outcomes on the output side, the more points at which a rule or the graph can go wrong in different ways.

The feedback loop — who rewrites the graph's rules, and how often, what happens specifically after a recorded error — isn't described as a process in any source found, including this very company publication. All it has is a general phrase about "iterative expert review": no frequency, no link to specific recorded cases, no answer to whether the rule was updated right after the missed heart attack discussed on the previous slide, and if so, how fast. The difference between "a gap named outright" and "a gap nobody asked about" is the same one this course already requires we not lose track of: a blank spot that was never named is indistinguishable, to the reader, from a blank spot nobody ever looked for.

Different pieces of this breakdown deserve different amounts of trust, and that's worth saying outright, since they come from different kinds of sources too. The per-head sum and contact frequency behind the cost calculation are official statistics and an independent assessment report: these can be trusted. The exam comparison and the independent test a year earlier are taken from secondhand accounts; the primary publications aren't open. The claim about a decision tree is a participant's words, and that's the weakest item here. The graph and rules architecture is the company's own technical publication: heavier than one participant's words, but lighter than an independent check, because the company is describing its own system. The bankruptcy facts and the deal sums that close out the breakdown are public filings and the business press.

**Sources.** [Middleton et al., "Sorting out symptoms," arXiv:1606.02041, 2016](https://arxiv.org/pdf/1606.02041)
