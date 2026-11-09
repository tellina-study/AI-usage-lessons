"""English captions for Seminar 9 diagrams (issue #319, EN track).

Key — the Russian string exactly as it stands in the drawing script; value —
the English string as it goes onto the canvas. Mechanics and the reason the
dictionary is its own file, not a second drawing script, are in
`tools/seminar-build/fig_toolkit.py`'s own docstring. Order follows draw
order, figure by figure; `BY_FIG` below says which string belongs to which
figure (used by `fig_toolkit.report()` to tell "key never reached the
canvas" apart from "key belongs to another drawing script"). Edited by hand.

This file is SHARED by all seven of sem-09's drawing scripts
(`make_figures_lestnitsa.py`, `make_figures_k1.py` .. `make_figures_k6.py`) —
`set_lang("en")` in `fig_toolkit.py` imports `STRINGS`/`BY_FIG` from here once,
regardless of which script runs. All twenty figures are covered in this one
pass; there is no per-script leftover to add later.

English terms follow the locked glossary (`library/seminars/sem-09/
glossary.en.yaml`) wherever a figure's own string names a glossary concept —
"knowledge base", "KB item", "cache breakpoint", "retry limit", "judge
model", "cross-check", "glyph height", "confidence", "exact match",
"refund", "request" all carry the glossary's own chosen English word, not a
fresh per-figure translation. Numbers are carried over unchanged in value;
only the decimal/thousands punctuation is re-set to English convention
(RU "1,5" → EN "1.5", RU "24 000" → EN "24,000"), the same adjustment
`fig_toolkit.py`'s own docstring already documents for sem-06's figures —
the measured quantity itself never changes.

Proper nouns stay as the glossary's own notes say: "Ольга" is "Olga"
(unchanged in English text, so it never needs a dictionary entry here), and
real identifiers (`qwen/qwen3-vl-8b-instruct`) are quoted verbatim inside the
translated sentence around them.

A miss (Cyrillic with no entry here) is never silent: `fig_toolkit.report()`
prints the list. An unused key is reported too — a typo in the key, or a
string the drawing script no longer draws.
"""

STRINGS = {

    # ── lestnitsa-dugi.png ──────────────────────────────────────────────────
    "1. Один вызов":
        "1. One call",
    "процесс спросил модель и записал ответ — можно ли на это положиться":
        "the process asked the model and recorded the answer — can it be relied on",
    "2. Цепочка решений":
        "2. Chain of decisions",
    "где в цепочке решает модель, а где обязан решать код":
        "where in the chain the model decides, and where the code must",
    "3. Ответ человеку":
        "3. Answer to a person",
    "процесс написал человеку — кто поручится, что это можно отправлять":
        "the process wrote to a person — who vouches that it's safe to send",
    "4. Знание вне промта":
        "4. Knowledge outside the prompt",
    "откуда процесс берёт факты и почему считает их верными":
        "where the process gets its facts, and why it trusts them",
    "5. Модель с полномочиями":
        "5. A model with authority",
    "модель не только отвечает, но и действует":
        "the model doesn't just answer, it acts",
    "6. Качество и выключатель":
        "6. Quality and the off switch",
    "как узнать, что процесс испортился, и как его остановить":
        "how to tell the process has broken, and how to stop it",
    "С7":
        "S7",
    "С8":
        "S8",
    "С9":
        "S9",
    "С10":
        "S10",
    "С11":
        "S11",
    "С12":
        "S12",
    "ось дуги снизу вверх: что процесс поручает модели и чем за это ручается":
        "the arc's axis, bottom to top: what the process hands to the model, and what it's willing to vouch for",
    "золотом обведена ступень этого занятия; заполненные ступени курс уже прошёл":
        "the gold outline marks this class's own rung; the filled rungs are ones the course has already climbed",

    # ── k1-shema-postanovka.png ─────────────────────────────────────────────
    "Где в потоке заявок встанет решение «отвечать самому»":
        "Where in the request flow the decision 'answer it myself' will sit",
    "форма и уведомление Ольге уже работают — вопрос в том, что встанет до того, как она ответит руками":
        "the form and the notification to Olga already work — the question is what goes in before she answers by hand",
    "Заявка":
        "Request",
    "форма: текст вопроса клиента":
        "form: the client's question as text",
    "Разбор и запись":
        "Parsing and logging",
    "классификация + строка в таблице":
        "classification + a row in the table",
    "Уведомление Ольге":
        "Notification to Olga",
    "короткое сообщение о заявке":
        "a short message about the request",
    "Ольга отвечает":
        "Olga answers",
    "по справочнику — руками, сама":
        "from the knowledge base — by hand, herself",
    "Строим сегодня: решение — ответить самому или передать человеку":
        "Building today: the decision — answer it myself or hand it to a person",
    "Пять способов решить это за Ольгу — до того, как заявка дойдёт до неё и она начнёт отвечать руками.":
        "Five ways to make this decision for Olga — before the request reaches her and she starts answering by hand.",

    # ── k1-shema-samootchet-i-geyt.png ──────────────────────────────────────
    "Где принимается решение «ответить самому или передать человеку»":
        "Where the decision 'answer it myself or hand it to a person' gets made",
    "одна и та же заявка и одна и та же база знаний — разница только в том, где записано решение":
        "the same request and the same knowledge base — the only difference is where the decision gets recorded",
    "Версия 1":
        "Version 1",
    "решение внутри текста ответа":
        "the decision lives inside the answer's own text",
    "Версия 2":
        "Version 2",
    "решение в отдельном поле":
        "the decision lives in a separate field",
    "Что делает модель":
        "What the model does",
    "Где записано решение":
        "Where the decision is recorded",
    "Кто может его проверить":
        "Who can check it",
    "Отвечает свободно":
        "Answers freely",
    "получает базу знаний целиком и пишет ответ одним текстом":
        "gets the whole knowledge base and writes the answer as one block of text",
    "Относит вопрос к пункту":
        "Assigns the question to an item",
    "называет один из заранее заданных пунктов базы — либо ни одного":
        "names one of the knowledge base's fixed items — or none at all",
    "Внутри абзаца ответа":
        "Inside the answer's paragraph",
    "«…отвечаю сам или отдаю человеку…» — словами, вперемешку с самим ответом":
        "'…I'll answer myself or hand this to a person…' — in words, mixed in with the answer itself",
    "В отдельном поле":
        "In a separate field",
    "опора на пункт базы № 7":
        "grounded in KB item #7",
    "значение, прочитанное кодом":
        "a value the code reads",
    "Никто":
        "No one",
    "сверить решение не с чем: отдельного значения не существует":
        "there's nothing to check the decision against: no separate value exists",
    "Код, условием":
        "Code, via a condition",
    "одинаково на этом вопросе и на любом следующем":
        "the same way on this question and on any next one",

    # ── k1-shema-spektr-deystviy.png ────────────────────────────────────────
    "Где на оси «решение у модели — решение у кода» стоит каждое действие":
        "Where each action sits on the axis 'the model decides — the code decides'",
    "решение целиком у модели":
        "the decision belongs entirely to the model",
    "решение у кода, модель не вызывается":
        "the code decides, no model call",
    "Модель решает":
        "The model decides",
    "и отвечает свободно":
        "and answers freely",
    "Модель называет пункт,":
        "The model names an item,",
    "код решает":
        "the code decides",
    "Модель называет":
        "The model names",
    "уверенность, код проверяет":
        "confidence; code checks",
    "Точное совпадение,":
        "Exact match,",
    "без модели":
        "no model involved",
    "Пятое действие стоит отдельно от этой оси: поиск во внешнем хранилище — своя ось, объём базы":
        "The fifth action sits off this axis entirely: search over external storage — its own axis, the size of the base",

    # ── k2-shema-postanovka.png ─────────────────────────────────────────────
    "Куда в вызове модели попадает дополненный справочник":
        "Where the extended knowledge base lands in the model call",
    "заявка, классификация и ответ не меняются — меняется то, что внутри справочника":
        "the request, the classification, and the answer don't change — what changes is what's inside the knowledge base",
    "вопрос клиента произвольным текстом":
        "the client's question, free-form text",
    "Классификация":
        "Classification",
    "вопрос относится к пункту справочника":
        "the question is matched to a knowledge base item",
    "Модель отвечает":
        "The model answers",
    "по справочнику целиком, одним вызовом":
        "from the whole knowledge base, in one call",
    "Ответ":
        "Answer",
    "уходит обратившемуся напрямую":
        "goes straight to the requester",
    "Ольга дополняет справочник":
        "Olga adds to the knowledge base",
    "дописывает новый пункт в конец списка — дополненное уезжает к модели тем же текстом, что и вопрос клиента":
        "appends a new item to the end of the list — the addition travels to the model as the same text as the client's question",

    # ── k2-shema-promt-i-kesh.png ───────────────────────────────────────────
    "Строение обращения: что уезжает к модели при каждом вопросе":
        "The shape of the call: what travels to the model on every question",
    "справочник едет к модели целиком, одним блоком текста":
        "the knowledge base travels to the model whole, as one block of text",
    "Одно обращение к модели":
        "One call to the model",
    "указание процессу":
        "instruction to the process",
    "база знаний целиком":
        "the whole knowledge base",
    "пункт 1 · оплата":
        "KB item 1 · payment",
    "пункт 2 · перенос":
        "KB item 2 · reschedule",
    "пункт 3 · документы":
        "KB item 3 · documents",
    "пункт 10 · связь с преподавателем":
        "KB item 10 · contact with the instructor",
    "контрольная точка":
        "cache breakpoint",
    "вопрос клиента":
        "client's question",
    "Правило порядка":
        "The ordering rule",
    "То, что меняется редко, держат ДО контрольной точки. То, что меняется от вопроса к вопросу, — после неё. Порядок пунктов перестаёт быть историей добавления и становится параметром процесса: у него появляется владелец.":
        "What changes rarely is kept BEFORE the cache breakpoint. What changes question to question goes after it. The order of items stops being a history of additions and becomes a parameter of the process — one with an owner.",
    "Чего этот шаг НЕ меняет":
        "What this step does NOT change",
    "Ни одного нового узла в процессе не появляется. Справочник по-прежнему едет к модели целиком при каждом обращении, и обращение растёт вместе с ним.":
        "Not one new node appears in the process. The knowledge base still travels to the model whole on every call, and the call keeps growing along with it.",

    # ── k2-shema-kesh-lovushka.png ──────────────────────────────────────────
    "Одна и та же правка, два разных исхода: решает раскладка блоков":
        "The same edit, two different outcomes: the block layout decides",
    "кэш читается только тогда, когда начало промта до точки совпало с прошлым вызовом знак в знак":
        "the cache is read only when the start of the prompt up to the breakpoint matches the previous call character for character",
    "Справочник одним блоком текста":
        "Knowledge base as one block of text",
    "один блок: 10 старых + новый":
        "one block: 10 old + the new one",
    "пункт 11 · дописан в конец":
        "KB item 11 · appended at the end",
    "весь блок изменился — прочитано 0, записано 3834, цена 1,271×":
        "the whole block changed — 0 read, 3834 written, price 1.271×",
    "Справочник четырьмя блоками, точка на новом":
        "Knowledge base as four blocks, breakpoint on the new one",
    "блок 1–3: старые 10 (не задеты)":
        "blocks 1–3: the old 10 (untouched)",
    "блок 4 (новый): пункт 11 · дописан":
        "block 4 (new): KB item 11 · appended",
    "точка переставлена сюда":
        "the breakpoint moved here",
    "старые блоки найдены по хэшу — прочитано 3762, цена 0,129×":
        "old blocks found by hash — 3762 read, price 0.129×",
    "контрольная точка — выше читается кэш, ниже — нет":
        "cache breakpoint — above it the cache is read, below it it's not",
    "Условие кэша":
        "The cache condition",
    "начало промта до контрольной точки совпадает знак в знак":
        "the start of the prompt up to the breakpoint matches character for character",
    "решает раскладка блоков, сложившаяся до правки":
        "the block layout in place before the edit decides",
    "кэш живёт минуты (у части провайдеров — час) и истекает сам":
        "the cache lives minutes (an hour, for some providers) and expires on its own",
    "Разница по цене — 9,8 раза":
        "The price difference — 9.8×",
    "Одна и та же дописанная правка: один блок — 1,271× цены прямого чтения, весь кэш сгорел. Четыре блока с точкой на новом — 0,129×, старое уцелело. Измерено на модели с явным кэшем, 27 вызовов этой серии.":
        "The same appended edit: one block — 1.271× the price of a cold read, the whole cache burned. Four blocks with the breakpoint on the new one — 0.129×, the old cache survived. Measured on a model with explicit caching, 27 calls in this series.",

    # ── k2-shema-gde-v-promte.png ───────────────────────────────────────────
    "Где внутри промта действует каждое из четырёх действий":
        "Where inside the prompt each of the four actions operates",
    "Инструкция":
        "Instruction",
    "Список базы":
        "Knowledge base list",
    "N пунктов, порядок важен":
        "N items, order matters",
    "Позиция в списке":
        "Position in the list",
    "допиши в конец, либо переставь частое к одному из краёв":
        "append it at the end, or move the frequent one to either edge",
    "Вокруг списка":
        "Around the list",
    "повтори вопрос клиента до списка, после или с обеих сторон":
        "repeat the client's question before the list, after it, or on both sides",
    "Другая структура":
        "A different structure",
    "список не внутри промта вовсе — находишь нужный пункт заранее":
        "the list isn't inside the prompt at all — you look up the needed item ahead of time",

    # ── k3-shema-postanovka.png ─────────────────────────────────────────────
    "Куда в потоке встанет проверка перед отправкой":
        "Where the pre-send check will sit in the flow",
    "заявка, классификация и ответ модели не меняются — между ответом и отправкой пока никого нет":
        "the request, the classification, and the model's answer don't change — right now there's no one between the answer and sending it",
    "Модель пишет ответ":
        "The model writes the answer",
    "по найденному пункту, свободным текстом":
        "from the matched item, as free text",
    "Ответ уходит клиенту":
        "The answer goes to the client",
    "без второго чтения":
        "with no second read",
    "Строим: проверка перед отправкой":
        "Building: a check before sending",
    "встаёт между тем, что написала модель, и тем, что получает человек, проверяя ответ до отправки":
        "sits between what the model wrote and what the person receives, checking the answer before it's sent",

    # ── k3-shema-tsikl.png ──────────────────────────────────────────────────
    "Цикл проверки ответа перед отправкой":
        "The loop that checks the answer before sending",
    "две развилки одной формы: сошлось — направо; иначе — вниз":
        "two branch points, the same shape: a match — to the right; otherwise — down",
    "вход":
        "input",
    "Вопрос клиента":
        "Client's question",
    "Генератор":
        "Generator",
    "модель пишет ответ клиенту":
        "the model writes the answer to the client",
    "Проверяющий":
        "Checker",
    "код сверяет пять заранее записанных требований":
        "code checks five requirements written down in advance",
    "Сошлось?":
        "Does it match?",
    "код сверяет условия":
        "code checks the conditions",
    "да":
        "yes",
    "Отправка клиенту":
        "Sent to the client",
    "ответ уходит обратившемуся":
        "the answer goes to the requester",
    "нет":
        "no",
    "Потолок исчерпан?":
        "Out of retries?",
    "считает счётчик попыток":
        "a retry counter keeps count",
    "Передать Ольге":
        "Hand to Olga",
    "вопрос уходит человеку":
        "the question goes to a person",
    "попытка не последняя":
        "not the last attempt",
    "Переделка":
        "Retry",
    "знает, что не прошло":
        "knows what didn't pass",
    "снова — и все уже пройденные требования заново":
        "again — and every requirement already passed gets rechecked too",
    "три попытки":
        "three attempts",
    "потолок выставлен вручную: без счётчика цикл не остановится сам":
        "the limit is set by hand: without a counter the loop won't stop on its own",
    "Цикл надёжен ровно настолько, насколько надёжен сам проверяющий: проверяющего нужно проверять тем же вниманием, что и генератора.":
        "The loop is only as reliable as the checker itself: the checker needs the same scrutiny as the generator.",

    # ── k3-shema-kto-verdikt.png ────────────────────────────────────────────
    "Кто выносит вердикт о годности ответа":
        "Who delivers the verdict on whether the answer is good enough",
    "Тот же исполнитель":
        "The same performer",
    "модель перечитывает собственный ответ":
        "the model re-reads its own answer",
    "Другая модель":
        "A different model",
    "судья получает пару ответов, выбирает":
        "the judge model receives a pair of answers and picks one",
    "Код":
        "Code",
    "формальный критерий — правило или тест, без модели":
        "a formal criterion — a rule or a test, no model involved",
    "Несколько исполнителей":
        "Several performers",
    "решатель выбирает лучший из трёх":
        "a decider picks the best of three",

    # ── k4-shema-postanovka.png ─────────────────────────────────────────────
    "Куда встаёт защита от инъекции":
        "Where the defense against injection goes",
    "решение о возврате принимает модель — защита встаёт до неё или внутри самого вызова":
        "the refund decision is made by the model — the defense goes before it, or inside the call itself",
    "Заявка на возврат":
        "Refund request",
    "текст клиента + ФИО":
        "the client's text + full name",
    "Решающая модель":
        "Deciding model",
    "читает текст заявки + список клиентов + правило «30 дней»":
        "reads the request text + the client list + the '30-day' rule",
    "Решение":
        "Decision",
    "возврат / отказ / менеджер":
        "refund / decline / manager",
    "Защита — пунктиром, этот кейс её строит и меряет":
        "The defense — dashed, this case builds and measures it",
    "Механическая проверка":
        "Mechanical check",
    "регулярные выражения, до модели":
        "regular expressions, before the model",
    "Классификатор на входе":
        "Classifier at the entrance",
    "отдельная дешёвая модель, до решающей":
        "a separate, cheap model, before the deciding one",
    "Усиление промта":
        "Prompt hardening",
    "инструкция внутри самого вызова модели":
        "an instruction inside the model call itself",
    "Усиление промта переписывает системную часть запроса решающей модели — без нового узла.":
        "Prompt hardening rewrites the system part of the deciding model's own call — no new node.",
    "Механика и классификатор — отдельные узлы: могут остановить заявку до модели.":
        "The mechanical check and the classifier are separate nodes: they can stop the request before the model.",

    # ── k4-shema-klassy-dereva.png ──────────────────────────────────────────
    "Как три признака разводят 64 заявки на пять классов":
        "How three features sort 64 requests into five classes",
    "каждый класс отличается от соседнего ровно одним признаком":
        "each class differs from its neighbor by exactly one feature",
    "8 заявок":
        "8 requests",
    "20 заявок":
        "20 requests",
    "12 заявок":
        "12 requests",
    "10 заявок":
        "10 requests",
    "14 заявок":
        "14 requests",
    "возврат положен":
        "refund due",
    "возврат не положен":
        "no refund due",
    "64 заявки":
        "64 requests",
    "Клиент в базе?":
        "Client on the list?",
    "Манипулирует текстом?":
        "Manipulating the text?",
    "Курс в последние 30 дней?":
        "Course within the last 30 days?",

    # ── k4-shema-voronka-atak.png ───────────────────────────────────────────
    "34 атаки проходят через слои по очереди":
        "34 attacks pass through the layers in turn",
    "у каждого слоя — свой шанс остановить, до решающей модели включительно":
        "every layer gets its own chance to stop one, right up to and including the deciding model",
    "Без единой защиты":
        "With no defense at all",
    "атаки":
        "attacks",
    "Механика":
        "Mechanics",
    "осталось 7":
        "7 left",
    "прошло насквозь":
        "got through",
    "Три защиты вместе":
        "All three together",
    "Классификатор":
        "Classifier",
    "осталось 6":
        "6 left",
    "осталось 5":
        "5 left",
    "осталось 0":
        "0 left",
    "Механика одна останавливает те же 28 атак, что и в связке со всеми тремя — остальное доделывает сама модель.":
        "Mechanics alone stops the same 28 attacks as all three combined — the model itself handles the rest.",

    # ── k5-shema-postanovka.png ─────────────────────────────────────────────
    "Тот же поток — сегодня разбираем настройки узла модели":
        "The same flow — today we're looking at the model node's own settings",
    "заявка, классификация и ответ устроены как раньше — холст не меняется":
        "the request, the classification, and the answer are set up as before — the canvas doesn't change",
    "Разбираем сегодня: настройки узла и промт":
        "Today: the node's settings and the prompt",
    "не новый узел — то, что внутри уже существующего узла решает, получит клиент на один и тот же вопрос один и тот же ответ или не получит":
        "not a new node — what's inside the node that already exists decides whether the client gets the same answer to the same question twice, or doesn't",

    # ── k5-shema-tri-ishoda.png ─────────────────────────────────────────────
    "Три вида негодности ответа, который уходит клиенту":
        "Three ways the answer going out to the client can be unfit",
    "три вопроса, по десять повторов одного и того же текста, температура ноль, одна и та же база в промте":
        "three questions, ten repeats each of the same exact text, temperature zero, the same knowledge base in the prompt",
    "Разброс":
        "Scatter",
    "заплатил 24 000 ₽ за 10 занятий, прошло 3 — сколько вернут? Формулы пересчёта в базе нет":
        "paid 24,000 ₽ for 10 classes, 3 happened — how much comes back? There's no recalculation formula in the knowledge base",
    "три разных ответа на один и тот же текст":
        "three different answers to the exact same text",
    "3 исхода из 10":
        "3 outcomes out of 10",
    "повторов одного вопроса":
        "repeats of one question",
    "трое узнают сумму, шестеро слышат «обратитесь к администратору», один получает ответ не на свой вопрос":
        "three learn the amount, six hear 'contact the administrator', one gets an answer to a different question entirely",
    "Устойчивая ошибка":
        "A stable error",
    "возврат ровно на 3000 ₽ — через руководителя или обычным порядком?":
        "a refund of exactly 3,000 ₽ — through the manager, or the usual way?",
    "один и тот же ответ десять раз подряд":
        "the same answer ten times running",
    "10 из 10":
        "10 out of 10",
    "ответов одинаковы — и все неверны":
        "answers are identical — and all wrong",
    "в базе сказано «для сумм выше 3000», а ровно 3000 выше 3000 не является; один повтор вдобавок переврал сумму клиента":
        "the knowledge base says 'for amounts above 3,000', and exactly 3,000 is not above 3,000; one repeat also got the client's own amount wrong",
    "Устойчивое противоречие":
        "A stable contradiction",
    "пропустил занятие без предупреждения — когда пересдача? В базе два пункта в напряжении":
        "missed a class with no warning — when's the retake? Two knowledge-base items pull in different directions",
    "оба пункта названы устойчиво, ноль расхождений":
        "both items get named consistently, zero drift",
    "ответов противоречат сами себе":
        "answers contradict themselves",
    "«бесплатная пересдача не предоставляется. Пересдачи проводятся каждую вторую субботу месяца»":
        "'a free retake is not provided. Retakes are held every second Saturday of the month'",
    "Для сравнения — тот же процесс на вопросе, ответ на который целиком лежит в базе: 25 повторов, 0 расхождений по существу. Устойчивость есть там, где ответ надо найти, и пропадает там, где его надо составить.":
        "For comparison — the same process on a question whose answer lies entirely in the knowledge base: 25 repeats, 0 substantive drift. Stability shows up where the answer has to be found, and disappears where it has to be composed.",

    # ── k6-shema-postanovka.png ─────────────────────────────────────────────
    "Где встанет автоматическое чтение фотографии":
        "Where automatic photo reading will go",
    "сегодня фотографию и текст сверяет только Ольга, глазами":
        "today only Olga cross-checks the photo against the text, by eye",
    "текст с суммой + фотография квитанции":
        "text with the amount + a photo of the receipt",
    "Ольга читает фото":
        "Olga reads the photo",
    "глазами, увеличивает нужный участок":
        "by eye, zooming into the relevant part",
    "Сравнивает с текстом":
        "Compares it with the text",
    "число с фото против числа из текста":
        "the number from the photo against the number from the text",
    "совпало — дальше; не совпало — уточнить у клиента":
        "matches — move on; doesn't — check with the client",
    "Строим: автоматическое чтение и сверка":
        "Building: automatic reading and cross-check",
    "вместо того, что сегодня делает Ольга глазами — читает фотографию и сверяет число с тем, что написано текстом":
        "instead of what Olga does today by eye — reads the photo and cross-checks the number against what the text says",

    # ── k6-shema-chtenie-i-sverka.png ───────────────────────────────────────
    "Сверку делает второе число, пришедшее мимо снимка":
        "The cross-check works because the second number bypassed the photo entirely",
    "фотографию модель читает пикселями; сумму из текста заявки набрал клиент — к сравнению приходят два значения, добытые разными путями":
        "the model reads the photo as pixels; the client typed the amount into the request text — the comparison brings together two values obtained by different routes",
    "Фотография квитанции":
        "Receipt photo",
    "вложение в заявке, снято телефоном":
        "an attachment to the request, shot on a phone",
    "Модель qwen/qwen3-vl-8b-instruct":
        "Model qwen/qwen3-vl-8b-instruct",
    "читает фотографию целиком, пикселями — без распознавания текста; возвращает сумму и дату":
        "reads the whole photo as pixels — no text recognition — and returns the amount and the date",
    "Сумма, которую клиент написал текстом заявки":
        "The amount the client wrote as text in the request",
    "это значение в снимок не заглядывало: клиент набрал его словами, и модель этот текст вовсе не читает":
        "this value never looked at the photo: the client typed it in words, and the model never reads that text at all",
    "число из снимка":
        "photo's number",
    "число из текста":
        "text's number",
    "Сверка в коде":
        "Code cross-check",
    "сравнивает два числа и решает, можно ли принимать заявку":
        "compares the two numbers and decides whether the request can be accepted",
    "совпали?":
        "do they match?",
    "Совпали":
        "They match",
    "заявка идёт дальше обычным порядком":
        "the request moves on, the usual way",
    "Разошлись":
        "They differ",
    "заявка уходит Ольге на ручную сверку":
        "the request goes to Olga for a manual check",
    "Сверка держится на том, что второе число пришло другим путём. Прочитать тот же снимок второй раз значит повторить ту же ошибку вторым голосом.":
        "The cross-check works because the second number arrived by a different route. Reading the same photo a second time would just repeat the same mistake in a second voice.",

    # ── k6-shema-vysota-simvola.png ─────────────────────────────────────────
    "Порог чтения зависит от высоты символа при неизменном весе файла":
        "The reading threshold depends on glyph height, even when the file size stays fixed",
    "одна и та же квитанция в шести разрешениях — чистое уменьшение одного файла, от полного размера до 53×64 пикс.":
        "the same receipt at six resolutions — a straight downscale of one file, from full size down to 53×64 px",
    "квитанция при полном размере":
        "receipt at full size",
    "Сумма":
        "Amount",
    "высота символа 64 пикс.":
        "glyph height 64 px",
    "Дата":
        "Date",
    "высота символа 32 пикс.":
        "glyph height 32 px",
    "сумма набрана ровно вдвое крупнее даты":
        "the amount is twice the date's size",
    "Квитанции синтетические: на каждой одна сумма и одна дата. Ломаются ОБА поля — но на разных шагах сжатия: дата раньше, сумма позже.":
        "The receipts are synthetic: each one carries a single amount and a single date. BOTH fields break — but at different compression steps: the date earlier, the amount later.",
    "Что стало с каждым полем по мере уменьшения снимка":
        "What happened to each field as the image shrinks",
    "полный размер":
        "full size",
    "53×64 пикс.":
        "53×64 px",
    "сумма":
        "amount",
    "дата":
        "date",
    "порог суммы":
        "sum threshold",
    "порог даты":
        "date threshold",
    "1,5–3,1 пикс.":
        "1.5–3.1 px",
    "высота символа суммы на её пороге (1/16 → 1/32)":
        "glyph height of the amount at its threshold (1/16 → 1/32)",
    "2,9–5,8 пикс.":
        "2.9–5.8 px",
    "высота символа даты на её пороге (четверть → восьмая)":
        "glyph height of the date at its threshold (quarter → eighth)",
    "Диапазоны пересекаются частично (2,9–3,1 пикс.) — порог суммы ниже порога даты, но не вдвое и не раздельными зонами.":
        "The ranges overlap partially (2.9–3.1 px) — the amount's threshold is lower than the date's, but not by half, and not in separate zones.",
    "Сжатие ломает оба поля — но на разной высоте символа: порог суммы ниже порога даты. И ломается уверенно: на сломанном разрешении все повторы поля сходятся на одном и том же неверном значении.":
        "Compression breaks both fields — but at a different glyph height for each: the amount's threshold is lower than the date's. And it breaks with confidence: at the broken resolution, every repeat of the field converges on the same wrong value.",

    # ── k6-shema-tri-potoka.png ─────────────────────────────────────────────
    "Где в потоке происходит распознавание":
        "Where in the flow the recognition happens",
    "1–2. Единый вызов":
        "1–2. A single call",
    "Фото + текст":
        "Photo + text",
    "несжатое или сжатое":
        "uncompressed or compressed",
    "Модель qwen3-vl-8b-instruct":
        "Model qwen3-vl-8b-instruct",
    "читает пиксели сама и сравнивает":
        "reads the pixels itself and compares",
    "3. Классическое распознавание":
        "3. Classic recognition",
    "Фото":
        "Photo",
    "Распознавание":
        "Recognition",
    "отдельный узел":
        "a separate node",
    "Готовый текст":
        "Finished text",
    "пикселей уже не видит":
        "no longer sees the pixels",
}

BY_FIG = {
    "lestnitsa-dugi.png": [
        "1. Один вызов",
        "процесс спросил модель и записал ответ — можно ли на это положиться",
        "2. Цепочка решений",
        "где в цепочке решает модель, а где обязан решать код",
        "3. Ответ человеку",
        "процесс написал человеку — кто поручится, что это можно отправлять",
        "4. Знание вне промта",
        "откуда процесс берёт факты и почему считает их верными",
        "5. Модель с полномочиями",
        "модель не только отвечает, но и действует",
        "6. Качество и выключатель",
        "как узнать, что процесс испортился, и как его остановить",
        "С7", "С8", "С9", "С10", "С11", "С12",
        "ось дуги снизу вверх: что процесс поручает модели и чем за это ручается",
        "золотом обведена ступень этого занятия; заполненные ступени курс уже прошёл",
    ],

    "k1-shema-postanovka.png": [
        "Где в потоке заявок встанет решение «отвечать самому»",
        "форма и уведомление Ольге уже работают — вопрос в том, что встанет до того, как она ответит руками",
        "Заявка",
        "форма: текст вопроса клиента",
        "Разбор и запись",
        "классификация + строка в таблице",
        "Уведомление Ольге",
        "короткое сообщение о заявке",
        "Ольга отвечает",
        "по справочнику — руками, сама",
        "Строим сегодня: решение — ответить самому или передать человеку",
        "Пять способов решить это за Ольгу — до того, как заявка дойдёт до неё и она начнёт отвечать руками.",
    ],
    "k1-shema-samootchet-i-geyt.png": [
        "Где принимается решение «ответить самому или передать человеку»",
        "одна и та же заявка и одна и та же база знаний — разница только в том, где записано решение",
        "Версия 1",
        "решение внутри текста ответа",
        "Версия 2",
        "решение в отдельном поле",
        "Что делает модель",
        "Где записано решение",
        "Кто может его проверить",
        "Отвечает свободно",
        "получает базу знаний целиком и пишет ответ одним текстом",
        "Относит вопрос к пункту",
        "называет один из заранее заданных пунктов базы — либо ни одного",
        "Внутри абзаца ответа",
        "«…отвечаю сам или отдаю человеку…» — словами, вперемешку с самим ответом",
        "В отдельном поле",
        "опора на пункт базы № 7",
        "значение, прочитанное кодом",
        "Никто",
        "сверить решение не с чем: отдельного значения не существует",
        "Код, условием",
        "одинаково на этом вопросе и на любом следующем",
    ],
    "k1-shema-spektr-deystviy.png": [
        "Где на оси «решение у модели — решение у кода» стоит каждое действие",
        "решение целиком у модели",
        "решение у кода, модель не вызывается",
        "Модель решает",
        "и отвечает свободно",
        "Модель называет пункт,",
        "код решает",
        "Модель называет",
        "уверенность, код проверяет",
        "Точное совпадение,",
        "без модели",
        "Пятое действие стоит отдельно от этой оси: поиск во внешнем хранилище — своя ось, объём базы",
    ],

    "k2-shema-postanovka.png": [
        "Куда в вызове модели попадает дополненный справочник",
        "заявка, классификация и ответ не меняются — меняется то, что внутри справочника",
        "Заявка",
        "вопрос клиента произвольным текстом",
        "Классификация",
        "вопрос относится к пункту справочника",
        "Модель отвечает",
        "по справочнику целиком, одним вызовом",
        "Ответ",
        "уходит обратившемуся напрямую",
        "Ольга дополняет справочник",
        "дописывает новый пункт в конец списка — дополненное уезжает к модели тем же текстом, что и вопрос клиента",
    ],
    "k2-shema-promt-i-kesh.png": [
        "Строение обращения: что уезжает к модели при каждом вопросе",
        "справочник едет к модели целиком, одним блоком текста",
        "Одно обращение к модели",
        "указание процессу",
        "база знаний целиком",
        "пункт 1 · оплата",
        "пункт 2 · перенос",
        "пункт 3 · документы",
        "пункт 10 · связь с преподавателем",
        "контрольная точка",
        "вопрос клиента",
        "Правило порядка",
        "То, что меняется редко, держат ДО контрольной точки. То, что меняется от вопроса к вопросу, — после неё. Порядок пунктов перестаёт быть историей добавления и становится параметром процесса: у него появляется владелец.",
        "Чего этот шаг НЕ меняет",
        "Ни одного нового узла в процессе не появляется. Справочник по-прежнему едет к модели целиком при каждом обращении, и обращение растёт вместе с ним.",
    ],
    "k2-shema-kesh-lovushka.png": [
        "Одна и та же правка, два разных исхода: решает раскладка блоков",
        "кэш читается только тогда, когда начало промта до точки совпало с прошлым вызовом знак в знак",
        "Справочник одним блоком текста",
        "указание процессу",
        "один блок: 10 старых + новый",
        "пункт 1 · оплата",
        "пункт 2 · перенос",
        "пункт 3 · документы",
        "пункт 10 · связь с преподавателем",
        "пункт 11 · дописан в конец",
        "вопрос клиента",
        "весь блок изменился — прочитано 0, записано 3834, цена 1,271×",
        "Справочник четырьмя блоками, точка на новом",
        "блок 1–3: старые 10 (не задеты)",
        "блок 4 (новый): пункт 11 · дописан",
        "точка переставлена сюда",
        "старые блоки найдены по хэшу — прочитано 3762, цена 0,129×",
        "контрольная точка — выше читается кэш, ниже — нет",
        "Условие кэша",
        "начало промта до контрольной точки совпадает знак в знак",
        "решает раскладка блоков, сложившаяся до правки",
        "кэш живёт минуты (у части провайдеров — час) и истекает сам",
        "Разница по цене — 9,8 раза",
        "Одна и та же дописанная правка: один блок — 1,271× цены прямого чтения, весь кэш сгорел. Четыре блока с точкой на новом — 0,129×, старое уцелело. Измерено на модели с явным кэшем, 27 вызовов этой серии.",
    ],
    "k2-shema-gde-v-promte.png": [
        "Где внутри промта действует каждое из четырёх действий",
        "Инструкция",
        "Список базы",
        "N пунктов, порядок важен",
        "Вопрос клиента",
        "Позиция в списке",
        "допиши в конец, либо переставь частое к одному из краёв",
        "Вокруг списка",
        "повтори вопрос клиента до списка, после или с обеих сторон",
        "Другая структура",
        "список не внутри промта вовсе — находишь нужный пункт заранее",
    ],

    "k3-shema-postanovka.png": [
        "Куда в потоке встанет проверка перед отправкой",
        "заявка, классификация и ответ модели не меняются — между ответом и отправкой пока никого нет",
        "Заявка",
        "вопрос клиента произвольным текстом",
        "Классификация",
        "вопрос относится к пункту справочника",
        "Модель пишет ответ",
        "по найденному пункту, свободным текстом",
        "Ответ уходит клиенту",
        "без второго чтения",
        "Строим: проверка перед отправкой",
        "встаёт между тем, что написала модель, и тем, что получает человек, проверяя ответ до отправки",
    ],
    "k3-shema-tsikl.png": [
        "Цикл проверки ответа перед отправкой",
        "две развилки одной формы: сошлось — направо; иначе — вниз",
        "вход",
        "Вопрос клиента",
        "Генератор",
        "модель пишет ответ клиенту",
        "Проверяющий",
        "код сверяет пять заранее записанных требований",
        "Сошлось?",
        "код сверяет условия",
        "да",
        "Отправка клиенту",
        "ответ уходит обратившемуся",
        "нет",
        "Потолок исчерпан?",
        "считает счётчик попыток",
        "Передать Ольге",
        "вопрос уходит человеку",
        "попытка не последняя",
        "Переделка",
        "знает, что не прошло",
        "снова — и все уже пройденные требования заново",
        "три попытки",
        "потолок выставлен вручную: без счётчика цикл не остановится сам",
        "Цикл надёжен ровно настолько, насколько надёжен сам проверяющий: проверяющего нужно проверять тем же вниманием, что и генератора.",
    ],
    "k3-shema-kto-verdikt.png": [
        "Кто выносит вердикт о годности ответа",
        "Тот же исполнитель",
        "модель перечитывает собственный ответ",
        "Другая модель",
        "судья получает пару ответов, выбирает",
        "Код",
        "формальный критерий — правило или тест, без модели",
        "Несколько исполнителей",
        "решатель выбирает лучший из трёх",
    ],

    "k4-shema-postanovka.png": [
        "Куда встаёт защита от инъекции",
        "решение о возврате принимает модель — защита встаёт до неё или внутри самого вызова",
        "Заявка на возврат",
        "текст клиента + ФИО",
        "Решающая модель",
        "читает текст заявки + список клиентов + правило «30 дней»",
        "Решение",
        "возврат / отказ / менеджер",
        "Защита — пунктиром, этот кейс её строит и меряет",
        "Механическая проверка",
        "регулярные выражения, до модели",
        "Классификатор на входе",
        "отдельная дешёвая модель, до решающей",
        "Усиление промта",
        "инструкция внутри самого вызова модели",
        "Усиление промта переписывает системную часть запроса решающей модели — без нового узла.",
        "Механика и классификатор — отдельные узлы: могут остановить заявку до модели.",
    ],
    "k4-shema-klassy-dereva.png": [
        "Как три признака разводят 64 заявки на пять классов",
        "каждый класс отличается от соседнего ровно одним признаком",
        "8 заявок",
        "возврат не положен",
        "20 заявок",
        "12 заявок",
        "возврат положен",
        "10 заявок",
        "14 заявок",
        "64 заявки",
        "Клиент в базе?",
        "да",
        "нет",
        "Манипулирует текстом?",
        "Курс в последние 30 дней?",
    ],
    "k4-shema-voronka-atak.png": [
        "34 атаки проходят через слои по очереди",
        "у каждого слоя — свой шанс остановить, до решающей модели включительно",
        "Без единой защиты",
        "атаки",
        "Решающая модель",
        "осталось 7",
        "прошло насквозь",
        "Три защиты вместе",
        "Механика",
        "осталось 6",
        "Классификатор",
        "осталось 5",
        "осталось 0",
        "Механика одна останавливает те же 28 атак, что и в связке со всеми тремя — остальное доделывает сама модель.",
    ],

    "k5-shema-postanovka.png": [
        "Тот же поток — сегодня разбираем настройки узла модели",
        "заявка, классификация и ответ устроены как раньше — холст не меняется",
        "Заявка",
        "вопрос клиента произвольным текстом",
        "Классификация",
        "вопрос относится к пункту справочника",
        "Модель отвечает",
        "по справочнику целиком, одним вызовом",
        "Ответ",
        "уходит обратившемуся напрямую",
        "Разбираем сегодня: настройки узла и промт",
        "не новый узел — то, что внутри уже существующего узла решает, получит клиент на один и тот же вопрос один и тот же ответ или не получит",
    ],
    "k5-shema-tri-ishoda.png": [
        "Три вида негодности ответа, который уходит клиенту",
        "три вопроса, по десять повторов одного и того же текста, температура ноль, одна и та же база в промте",
        "Разброс",
        "заплатил 24 000 ₽ за 10 занятий, прошло 3 — сколько вернут? Формулы пересчёта в базе нет",
        "три разных ответа на один и тот же текст",
        "3 исхода из 10",
        "повторов одного вопроса",
        "трое узнают сумму, шестеро слышат «обратитесь к администратору», один получает ответ не на свой вопрос",
        "Устойчивая ошибка",
        "возврат ровно на 3000 ₽ — через руководителя или обычным порядком?",
        "один и тот же ответ десять раз подряд",
        "10 из 10",
        "ответов одинаковы — и все неверны",
        "в базе сказано «для сумм выше 3000», а ровно 3000 выше 3000 не является; один повтор вдобавок переврал сумму клиента",
        "Устойчивое противоречие",
        "пропустил занятие без предупреждения — когда пересдача? В базе два пункта в напряжении",
        "оба пункта названы устойчиво, ноль расхождений",
        "ответов противоречат сами себе",
        "«бесплатная пересдача не предоставляется. Пересдачи проводятся каждую вторую субботу месяца»",
        "Для сравнения — тот же процесс на вопросе, ответ на который целиком лежит в базе: 25 повторов, 0 расхождений по существу. Устойчивость есть там, где ответ надо найти, и пропадает там, где его надо составить.",
    ],

    "k6-shema-postanovka.png": [
        "Где встанет автоматическое чтение фотографии",
        "сегодня фотографию и текст сверяет только Ольга, глазами",
        "Заявка",
        "текст с суммой + фотография квитанции",
        "Ольга читает фото",
        "глазами, увеличивает нужный участок",
        "Сравнивает с текстом",
        "число с фото против числа из текста",
        "Решение",
        "совпало — дальше; не совпало — уточнить у клиента",
        "Строим: автоматическое чтение и сверка",
        "вместо того, что сегодня делает Ольга глазами — читает фотографию и сверяет число с тем, что написано текстом",
    ],
    "k6-shema-chtenie-i-sverka.png": [
        "Сверку делает второе число, пришедшее мимо снимка",
        "фотографию модель читает пикселями; сумму из текста заявки набрал клиент — к сравнению приходят два значения, добытые разными путями",
        "Фотография квитанции",
        "вложение в заявке, снято телефоном",
        "Модель qwen/qwen3-vl-8b-instruct",
        "читает фотографию целиком, пикселями — без распознавания текста; возвращает сумму и дату",
        "Сумма, которую клиент написал текстом заявки",
        "это значение в снимок не заглядывало: клиент набрал его словами, и модель этот текст вовсе не читает",
        "число из снимка",
        "число из текста",
        "Сверка в коде",
        "сравнивает два числа и решает, можно ли принимать заявку",
        "совпали?",
        "Совпали",
        "заявка идёт дальше обычным порядком",
        "Разошлись",
        "заявка уходит Ольге на ручную сверку",
        "Сверка держится на том, что второе число пришло другим путём. Прочитать тот же снимок второй раз значит повторить ту же ошибку вторым голосом.",
    ],
    "k6-shema-vysota-simvola.png": [
        "Порог чтения зависит от высоты символа при неизменном весе файла",
        "одна и та же квитанция в шести разрешениях — чистое уменьшение одного файла, от полного размера до 53×64 пикс.",
        "квитанция при полном размере",
        "Сумма",
        "высота символа 64 пикс.",
        "Дата",
        "высота символа 32 пикс.",
        "сумма набрана ровно вдвое крупнее даты",
        "Квитанции синтетические: на каждой одна сумма и одна дата. Ломаются ОБА поля — но на разных шагах сжатия: дата раньше, сумма позже.",
        "Что стало с каждым полем по мере уменьшения снимка",
        "полный размер",
        "53×64 пикс.",
        "сумма",
        "дата",
        "порог суммы",
        "порог даты",
        "1,5–3,1 пикс.",
        "высота символа суммы на её пороге (1/16 → 1/32)",
        "2,9–5,8 пикс.",
        "высота символа даты на её пороге (четверть → восьмая)",
        "Диапазоны пересекаются частично (2,9–3,1 пикс.) — порог суммы ниже порога даты, но не вдвое и не раздельными зонами.",
        "Сжатие ломает оба поля — но на разной высоте символа: порог суммы ниже порога даты. И ломается уверенно: на сломанном разрешении все повторы поля сходятся на одном и том же неверном значении.",
    ],
    "k6-shema-tri-potoka.png": [
        "Где в потоке происходит распознавание",
        "1–2. Единый вызов",
        "Фото + текст",
        "несжатое или сжатое",
        "Модель qwen3-vl-8b-instruct",
        "читает пиксели сама и сравнивает",
        "3. Классическое распознавание",
        "Фото",
        "Распознавание",
        "отдельный узел",
        "Готовый текст",
        "пикселей уже не видит",
    ],
}
