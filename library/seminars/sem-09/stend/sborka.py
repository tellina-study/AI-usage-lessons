#!/usr/bin/env python3
"""Собрать стенд Семинара 9 — issue #299.

Два разных по происхождению сценария в этом файле:

    vhod-s8.json    Задача 1 — публикация ВХОДНОГО состояния С9: та же структура, что
                     отдаёт `sem-08/stend/sborka.student_file()` (объединённый выход С8
                     с четырьмя доработками), но с восстановленными credential/таблицей —
                     для настоящей проверки прогонами. На стенде — «С9 · вход (выход С8)».
    case1-v1.json    Задача 2, Кейс 1, версия 1 — модель отвечает свободно, база знаний
                     целиком в промте, решение «отвечать/эскалировать» держится на
                     самоотчёте модели о своей уверенности.
    case1-v2.json    Задача 2, Кейс 1, версия 2 — та же модель и та же база, но решение
                     принимается детерминированной проверкой: структурированный вывод
                     называет пункт базы, на который опирается ответ, и код сверяет имя
                     пункта со списком существующих — вместо того, чтобы верить слову
                     модели «уверен».

## Имена и адреса — правило стенда для Семинара 9

Все сценарии этого файла публикуются с именем, начинающимся на «С9 · », и с вебхуком,
начинающимся на «s9-» — даже `vhod-s8`, чьё СОДЕРЖАНИЕ в точности повторяет выход С8:
имя и адрес живут в адресном пространстве занятия, которое их выложило, а не занятия,
чьё содержание они несут. Ни один узел С7/С8 на стенде этим файлом не переименовывается
и не удаляется — `vhod-s8()` переиздаёт структуру `student_file()` заново под новым
именем, не трогая опубликованные воркфлоу С8.

## Ключи — только из /home/harness/.n8n-lab-credentials

    python3 sborka.py                                      только записать json рядом
    N8N_API_URL=... N8N_API_KEY=... python3 sborka.py --push   выложить и опубликовать

`OpenRouter account` (`VbxiQn8TbqA4R2mw`) и `Telegram account (С8)` (`kfXE6PWKNzA56vc6`) —
существующие credential стенда, переиспользованы без новой инфраструктуры (прямое указание
задачи). Для Кейса 1 создана НОВАЯ таблица Data Table `s9_case1_answers`
(`U5BLSv5cPzVVyRGy`, через `POST /data-tables` 2026-10-24) — у неё своя схема строк
(question/answer/grounded_item/decision), отличная от `requests` С7/С8, остальное —
старая таблица `requests` эту схему не несёт и смешивать данные разных занятий в одной
таблице — не лучше, чем смешивать темы в одном справочнике.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

# Реюз структуры student_file() Семинара 8 — импортом модуля, не копией кода.
sys.path.insert(0, str((HERE.parent.parent / "sem-08" / "stend").resolve()))
import sborka as s8  # noqa: E402

OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}
TG_CRED = {"telegramApi": {"id": "kfXE6PWKNzA56vc6", "name": "Telegram account (С8)"}}
TELEGRAM_CHAT_ID = "266536553"

TABLE_ID = "xlDAQCm75jLAKNom"      # requests (С7/С8) — для vhod-s8 (та же, что у С8)
TABLE_NAME = "requests"
S9_TABLE_ID = "U5BLSv5cPzVVyRGy"   # s9_case1_answers — отдельная схема строк Кейса 1
S9_TABLE_NAME = "s9_case1_answers"

ANSWER_MODEL = "qwen/qwen-2.5-7b-instruct"

REFUND_THRESHOLD = s8.REFUND_THRESHOLD  # тот же порог 3000 ₽, единственный источник правды


# ---------------------------------------------------------------------------------------
# Задача 1 — вход С9 (переиздание student_file() С8 с восстановленными привязками)
# ---------------------------------------------------------------------------------------

def vhod_s8():
    """Публикует объединённый выход С8 как входное состояние С9 — настоящий, прогоняемый
    воркфлоу, а не стриженый файл на вынос. Берёт структуру из
    `sem-08.stend.sborka.student_file()` (4 доработки поверх `student.json`) и восстанавливает
    то, что та функция сознательно снимает перед выдачей студенту: credential модели и
    Telegram, таблицу Data Table, пути формы."""
    wf = s8.student_file()
    wf["name"] = "С9 · вход (выход С8)"
    for n in wf["nodes"]:
        if n["type"] == "@n8n/n8n-nodes-langchain.lmChatOpenRouter":
            n["credentials"] = OPENROUTER_CRED
        if n["type"] == "n8n-nodes-base.telegram":
            n["credentials"] = TG_CRED
        if n["type"] == "n8n-nodes-base.dataTable":
            n["parameters"]["dataTableId"] = {
                "__rl": True, "value": TABLE_ID, "mode": "list", "cachedResultName": TABLE_NAME}
        if n["type"] == "n8n-nodes-base.formTrigger":
            path = "s9-vhod-vozvrat" if n["id"] == "refund_form" else "s9-vhod-kurs"
            n["parameters"]["path"] = path
            n["webhookId"] = path

    # Находка прогона (execution 602, настоящий прогон на стенде, не самоотчёт): узел
    # `Same question, reworded? (LLM)` (цепочка `chainLlm`) ЗАМЕНЯЕТ $json на {text: ...} —
    # это поведение узла по умолчанию, не ошибка написания выражения. Унаследованное из
    # `dedup_nodes()` С8 (там этот путь не был измерен по колонкам таблицы — измерялась
    # только точность самой дедупликации, не судьба остальных полей после неё), ветка
    # «не дубль» приходила в `Write row` с `topic`/`urgency`/`status` = `None`: `$json.topic`
    # на этом шаге ссылался уже не на `Vocabulary check`, а на пустой объект LLM-ответа.
    # `dedup_nodes()` — общая функция С8, её не трогаем (задача ограничивает правки этим
    # файлом одной функцией `student_file()`); мост ниже восстанавливает поля ИМЕНОВАННОЙ
    # ссылкой на `Vocabulary check`, не полагаясь на проходящий через LLM-узел `$json`.
    bridge = {
        "id": "restore_vocab_fields", "name": "Restore vocabulary fields",
        "type": "n8n-nodes-base.set", "typeVersion": 3.4, "position": [460, 160],
        "parameters": {
            "mode": "manual", "includeOtherFields": True,
            "assignments": {"assignments": [
                {"id": "r1", "name": "topic", "type": "string",
                 "value": "={{ $('Vocabulary check').item.json.topic }}"},
                {"id": "r2", "name": "urgency", "type": "string",
                 "value": "={{ $('Vocabulary check').item.json.urgency }}"},
                {"id": "r3", "name": "contact_from_text", "type": "string",
                 "value": "={{ $('Vocabulary check').item.json.contact_from_text }}"},
                {"id": "r4", "name": "status", "type": "string",
                 "value": "={{ $('Vocabulary check').item.json.status }}"},
                {"id": "r5", "name": "extra_topics", "type": "string",
                 "value": "={{ $('Vocabulary check').item.json.extra_topics }}"},
            ]},
            "options": {},
        },
    }
    wf["nodes"].append(bridge)
    wf["connections"]["Same question, reworded? (LLM)"] = {"main": [[
        {"node": "Restore vocabulary fields", "type": "main", "index": 0}]]}
    wf["connections"]["Restore vocabulary fields"] = {"main": [[
        {"node": "Write row", "type": "main", "index": 0}]]}
    return wf


# ---------------------------------------------------------------------------------------
# Задача 2 — Кейс 1: база знаний в промте, версия 1 (свободно) / версия 2 (детерминированно)
# ---------------------------------------------------------------------------------------

# 10 пунктов базы — связный человеческий текст, каждый с устойчивым id (kb1..kb10),
# который структурированный вывод версии 2 обязан назвать явно. Три вопроса ВНЕ базы
# (программа лояльности, скидка за друга, демо-занятие) намеренно не покрыты ни одним
# пунктом — на них версия 1 должна ответить уверенно и неверно, это и есть материал кейса.
KB_ITEMS = [
    ("kb1", "Оплата", "Курс оплачивается на сайте по ссылке в личном кабинете (карта, "
     "Робокасса) или наличными на ресепшене при личном визите. Рассрочка не предусмотрена."),
    ("kb2", "Перенос занятия", "Перенести конкретное занятие можно не позднее чем за 24 "
     "часа до его начала — через личный кабинет (кнопка «Перенести») или сообщением "
     "администратору. Позже 24 часов занятие считается использованным."),
    ("kb3", "Документы при поступлении", "Нужен паспорт (копия разворота) и СНИЛС; если "
     "студенту не исполнилось 18 лет — согласие одного из родителей, бланк в личном "
     "кабинете."),
    ("kb4", "Возврат денег", "Возврат оформляется в течение 10 рабочих дней на карту, с "
     "которой была оплата. Для сумм выше 3000 рублей решение проходит через руководителя, "
     "это дольше стандартного срока."),
    ("kb5", "Пересдача пропущенного занятия", "Пересдачи идут каждую вторую субботу "
     "месяца, расписание публикуется в объявлениях личного кабинета за неделю."),
    ("kb6", "Пропуск без предупреждения", "Занятие считается проведённым, бесплатного "
     "повтора не предусмотрено — действует то же правило, что и перенос позже 24 часов."),
    ("kb7", "Сертификат", "Электронный сертификат формируется автоматически и появляется "
     "в личном кабинете в течение 5 рабочих дней после последнего занятия курса."),
    ("kb8", "Перевод на другой курс", "Перевод возможен при наличии мест на новом курсе; "
     "разница в стоимости пересчитывается администратором индивидуально."),
    ("kb9", "Работа в праздники", "Центр не работает в государственные праздники РФ, "
     "занятия на эти даты переносятся автоматически, уведомление приходит в личный "
     "кабинет."),
    ("kb10", "Связь с преподавателем", "Написать конкретному преподавателю можно через "
     "раздел «Сообщения» личного кабинета, ответ приходит в течение одного рабочего дня."),
]
KB_IDS = [item[0] for item in KB_ITEMS]

# Вопросы вне базы — материал кейса (версия 1 отвечает на них уверенно и неверно).
OUT_OF_KB_QUESTIONS = [
    "Какая у вас программа лояльности для постоянных клиентов?",
    "Если я приведу друга на курс, будет ли нам скидка?",
    "Есть ли бесплатное демо-занятие перед покупкой курса?",
]
# Вопросы внутри базы — для сравнения на тех же двух версиях.
IN_KB_QUESTIONS = [
    "Как перенести занятие, если я заболел?",
    "Какие документы нужны для поступления?",
    "Когда вернут деньги за отменённый курс?",
]


def kb_text():
    lines = ["База знаний учебного центра:"]
    for kid, title, body in KB_ITEMS:
        lines.append(f"{kid} · {title}: {body}")
    return "\n".join(lines)


def model_node(node_id, name, pos):
    return {
        "id": node_id, "name": name, "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "typeVersion": 1, "position": pos,
        "parameters": {"model": ANSWER_MODEL, "options": {}},
        "credentials": OPENROUTER_CRED,
    }


def client_question_form(path):
    return {
        "id": "c1_form", "name": "Client question", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [-180, 0], "webhookId": path,
        "parameters": {
            "path": path, "formTitle": "Вопрос в учебный центр",
            "formDescription": "Кейс 1 Семинара 9 — не форма студента С7",
            "formFields": {"values": [
                {"fieldLabel": "Вопрос", "fieldType": "textarea",
                 "placeholder": "например: когда вернут деньги за отменённый курс?",
                 "requiredField": True},
            ]},
            "options": {"appendAttribution": False},
        },
    }


def answer_row_node(node_id, name, pos, version, answer_expr, grounded_expr, decision_expr):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.dataTable",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "operation": "insert",
            "dataTableId": {"__rl": True, "value": S9_TABLE_ID, "mode": "list",
                             "cachedResultName": S9_TABLE_NAME},
            "columns": {
                "mappingMode": "defineBelow",
                "value": {
                    "version": version,
                    "question": "={{ $('Client question').item.json['Вопрос'] }}",
                    "answer": answer_expr,
                    "grounded_item": grounded_expr,
                    "decision": decision_expr,
                },
                "matchingColumns": [], "schema": [],
            },
            "options": {},
        },
    }


def case1_v1():
    """Версия 1 — модель отвечает свободно, имея базу знаний целиком в промте; решение
    «отвечать / отдать человеку» держится на самоотчёте модели («если не уверена —
    напиши, что не знает»). Естественная первая попытка, и именно её провал кейс
    разбирает: на вопросах вне базы модель отвечает уверенно и неверно вместо того,
    чтобы признать незнание — самоотчёт не работает как граница."""
    path = "s9-answer-free"
    nodes = [client_question_form(path)]
    nodes.append(model_node("c1_model_free", "Model (answer, free)", [60, 220]))
    nodes.append({
        "id": "c1_answer_free", "name": "Answer (free self-report)",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5,
        "position": [60, 0],
        "parameters": {
            "promptType": "define",
            "text": (
                "=Ты — ассистент поддержки учебного центра. Ниже база знаний, которой "
                "можно пользоваться для ответа.\n\n" + kb_text() + "\n\nВопрос клиента: "
                "{{ $json['Вопрос'] }}\n\nОтветь по существу и по-русски, коротко (2-4 "
                "предложения). Если ответа в базе знаний нет и ты не уверена — честно "
                "напиши, что не знаешь, и что ответит сотрудник. Если уверена — отвечай "
                "прямо, без оговорок."
            ),
            "options": {},
        },
    })
    nodes.append(answer_row_node(
        "c1_write_free", "Write row", [300, 0], "v1-free",
        "={{ $json.text }}", "", ""))
    nodes.append({
        "id": "c1_result_free", "name": "Result screen", "type": "n8n-nodes-base.form",
        "typeVersion": 1, "position": [540, 0],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Ответ (версия 1 — свободно)",
            "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                  "}}<br><br>Ответ: {{ $('Answer (free self-report)')"
                                  ".item.json.text }}",
            "options": {"appendAttribution": False},
        },
    })
    conn = {
        "Client question": {"main": [[
            {"node": "Answer (free self-report)", "type": "main", "index": 0}]]},
        "Answer (free self-report)": {"main": [[
            {"node": "Write row", "type": "main", "index": 0}]]},
        "Write row": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (answer, free)": {"ai_languageModel": [[
            {"node": "Answer (free self-report)", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · Кейс 1, версия 1 — отвечает свободно (самоотчёт)",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def case1_v2():
    """Версия 2 — та же модель и та же база, но решение «отвечать / отдать человеку» —
    детерминированная проверка, не самоотчёт. Структурированный вывод называет пункт
    базы (`grounded_in_item`, одно из kb1..kb10 либо пустая строка), и `IF`-узел сверяет
    это имя со списком РЕАЛЬНО существующих пунктов — модель не может «придумать»
    опору, которой нет в списке, это решает код, а не доверие к слову «уверена»."""
    path = "s9-answer-gated"
    nodes = [client_question_form(path)]
    nodes[0]["id"] = "c1_form"  # тот же id/имя, два разных workflow — коллизий нет
    nodes.append(model_node("c1_model_gated", "Model (answer, gated)", [60, 260]))
    schema = {
        "type": "object",
        "properties": {
            "answer": {"type": "string",
                       "description": "ответ клиенту по существу, 1-2 предложения"},
            "grounded_in_item": {
                "type": "string", "enum": KB_IDS + [""],
                "description": ("id пункта базы знаний (kb1..kb10), на который "
                                 "опирается ответ; если ни один пункт не покрывает "
                                 "вопрос — пустая строка, и тогда ответ передаётся "
                                 "человеку, а не клиенту"),
            },
        },
        "required": ["answer", "grounded_in_item"],
    }
    nodes.append({
        "id": "c1_extract_gated", "name": "Answer with grounding (structured)",
        "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
        "position": [60, 0],
        "parameters": {
            "text": "=" + kb_text() + "\n\nВопрос клиента: {{ $json['Вопрос'] }}",
            "schemaType": "manual",
            "inputSchema": json.dumps(schema, ensure_ascii=False, indent=2),
            "options": {},
        },
    })
    nodes.append({
        "id": "c1_grounded_if", "name": "Grounded in known KB item?",
        "type": "n8n-nodes-base.if", "typeVersion": 2.2, "position": [300, 0],
        "parameters": {"conditions": {
            "options": {"caseSensitive": True, "typeValidation": "strict"},
            "combinator": "and", "conditions": [{
                "leftValue": "={{ " + json.dumps(KB_IDS, ensure_ascii=False) +
                             ".includes($json.output.grounded_in_item) }}",
                "rightValue": True,
                "operator": {"type": "boolean", "operation": "equals"}}]}},
    })
    nodes.append(answer_row_node(
        "c1_write_answered", "Write row (answered)", [540, -80], "v2-gated",
        "={{ $json.output.answer }}", "={{ $json.output.grounded_in_item }}", "answered"))
    nodes.append({
        "id": "c1_result_answered", "name": "Result screen (answered)",
        "type": "n8n-nodes-base.form", "typeVersion": 1, "position": [780, -80],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Ответ (версия 2 — проверено)",
            # $json здесь — вывод ПРЕДЫДУЩЕГО узла `Write row (answered)` (Data Table
            # insert отдаёт вставленную строку плоскими полями `answer`/`grounded_item`),
            # не структурированный вывод модели (`output.answer`/`output.grounded_in_item`)
            # — та ссылка была реальной находкой этого прогона (скрин показал пустой
            # «Ответ:»/«опора:»; execution 612, узел `Result screen (answered)`).
            "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                  "}}<br><br>Ответ: {{ $json.answer }}<br>"
                                  "<small>опора: {{ $json.grounded_item }}</small>",
            "options": {"appendAttribution": False},
        },
    })
    nodes.append({
        "id": "c1_notify_olga", "name": "Notify Olga (escalation)",
        "type": "n8n-nodes-base.telegram", "typeVersion": 1.2, "position": [540, 160],
        "parameters": {
            "operation": "sendMessage", "chatId": TELEGRAM_CHAT_ID,
            "text": "=Клиент спросил «{{ $('Client question').item.json['Вопрос'] }}». "
                    "Модель не нашла опору в базе знаний (grounded_in_item="
                    "{{ $json.output.grounded_in_item || '—' }}) — вопрос передан вам.",
            "additionalFields": {},
        },
        "credentials": TG_CRED,
    })
    nodes.append(answer_row_node(
        "c1_write_escalated", "Write row (escalated)", [780, 160], "v2-gated",
        # $json здесь — вывод ПРЕДЫДУЩЕГО узла `Notify Olga (escalation)` (ответ Telegram
        # Bot API, не структурированный вывод модели) — та же находка, что у completion
        # message выше: именованная ссылка на узел извлечения, не проходящий `$json`.
        "", "={{ $('Answer with grounding (structured)').item.json.output"
             ".grounded_in_item }}", "escalated"))
    nodes.append({
        "id": "c1_result_escalated", "name": "Result screen (escalated)",
        "type": "n8n-nodes-base.form", "typeVersion": 1, "position": [1020, 160],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Передано сотруднику",
            "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                  "}}<br><br>Подождите, пожалуйста — ответит человек.",
            "options": {"appendAttribution": False},
        },
    })
    conn = {
        "Client question": {"main": [[
            {"node": "Answer with grounding (structured)", "type": "main", "index": 0}]]},
        "Answer with grounding (structured)": {"main": [[
            {"node": "Grounded in known KB item?", "type": "main", "index": 0}]]},
        "Grounded in known KB item?": {"main": [
            [{"node": "Write row (answered)", "type": "main", "index": 0}],
            [{"node": "Notify Olga (escalation)", "type": "main", "index": 0}],
        ]},
        "Write row (answered)": {"main": [[
            {"node": "Result screen (answered)", "type": "main", "index": 0}]]},
        "Notify Olga (escalation)": {"main": [[
            {"node": "Write row (escalated)", "type": "main", "index": 0}]]},
        "Write row (escalated)": {"main": [[
            {"node": "Result screen (escalated)", "type": "main", "index": 0}]]},
        "Model (answer, gated)": {"ai_languageModel": [[
            {"node": "Answer with grounding (structured)",
             "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · Кейс 1, версия 2 — проверка по пункту базы (детерминированно)",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


STAGES = {"vhod-s8": vhod_s8, "case1-v1": case1_v1, "case1-v2": case1_v2}


def main():
    push = "--push" in sys.argv
    existing = {}
    if push:
        existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
    for fname, fn in STAGES.items():
        wf = fn()
        (HERE / f"{fname}.json").write_text(
            json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  {fname}.json — {len(wf['nodes'])} узлов")
        if not push:
            continue
        if wf["name"] in existing:
            wid = existing[wf["name"]]
            api("PUT", f"/workflows/{wid}", wf)
            action = "обновлён"
        else:
            wid = api("POST", "/workflows", wf)["id"]
            action = "создан"
        api("POST", f"/workflows/{wid}/publish", {})
        print(f"     {action} и опубликован: {wid}")


if __name__ == "__main__":
    main()
