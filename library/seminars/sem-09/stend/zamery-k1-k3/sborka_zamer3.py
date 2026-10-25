#!/usr/bin/env python3
"""Собрать стенд Замера 2 (Кейс 3) — issue #299, цикл генератор—проверяющий—переделка.

Четыре сценария, все с именем, начинающимся на «С9 · замер K3 ·», и вебхуком, начинающимся
на `s9-m3-`:

    s9-m3-once         один вызов модели, без цикла — база сравнения.
    s9-m3-judge        цикл: годность ответа оценивает ТА ЖЕ модель (судья), лимит 3 попытки.
    s9-m3-code         цикл: годность проверяет КОД (те же требования, формальной проверкой),
                       лимит 3 попытки, явная ветка «не сошлось».
    s9-m3-judge-check  отдельный, разовый вызов судьи-модели НАД уже готовым ответом (и уже
                       известным кодовым вердиктом) — чтобы получить несущее число кейса:
                       сколько раз судья признал годным то, что код забраковал.

Задача для модели — ответ клиенту по одному известному пункту базы (переиспользован `KB_ITEMS`
из `stend/sborka.py`, импортом модуля, не копией), который ОБЯЗАН:
  1. быть не длиннее 280 символов;
  2. явно называть ключевую деталь пункта базы;
  3. указывать, куда обращаться дальше (администратор / личный кабинет / преподаватель /
     сотрудник / руководитель);
  4. не содержать чисел, которых нет в этом пункте базы;
  5. быть целиком на русском языке (без латиницы и иероглифов — находка 2 Замера 1 этой же
     сессии показала живой случай переключения языка на этом же стенде).

Проверка (1)-(5) кодируется ОДНОЙ и той же логикой в двух местах: как промт для судьи-модели
(`judge_criteria_text()`) и как JS в Code-узле `Code check` (`code_check_node()`) — чтобы
сравнение «судья против кода» проверяло одно и то же определение годности, а не два разных.

Ключи — только из переменных окружения (`N8N_API_URL`, `N8N_API_KEY`), см. задачу/README.
Модель — существующий credential `OpenRouter account` (`VbxiQn8TbqA4R2mw`), без новой инфры.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

import importlib.util as _ilu  # noqa: E402

# Имя модуля "sborka" уже занято внутри stend/sborka.py (который сам импортирует
# sem-08/stend/sborka.py под этим именем) — обычный sys.path-импорт столкнётся с этим и
# получит частично инициализированный модуль (круговая коллизия имён). Загружаем файл под
# отдельным именем, без конфликта.
_spec = _ilu.spec_from_file_location("sem09_stend_sborka", str(HERE.parent / "sborka.py"))
s9 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(s9)

OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}
ANSWER_MODEL = "qwen/qwen-2.5-7b-instruct"

S9_TABLE_NAME = "s9_case3_measurements"
MAX_ATTEMPTS = 3

KB_BY_ID = {kid: (title, body) for kid, title, body in s9.KB_ITEMS}

CONTACT_PHRASES = ["администратор", "личный кабинет", "преподавател", "сотрудник",
                   "руководител"]

# 6 вопросов Замера 2 — все ВНУТРИ базы (это замер про ФОРМУ ответа, не про допуск/отказ,
# который уже разобран Замером 1); разные пункты базы для разнообразия.
TEST_QUESTIONS = [
    {"question": "Можно ли перенести занятие, если я заболел?", "kb_id": "kb2",
     "keyword": "24 час"},
    {"question": "Когда мне вернут деньги за отменённый курс?", "kb_id": "kb4",
     "keyword": "10 рабочих дней"},
    {"question": "Как мне попасть на пересдачу занятия, которое я пропустил?", "kb_id": "kb5",
     "keyword": "вторую субботу"},
    {"question": "Когда появится сертификат после курса?", "kb_id": "kb7",
     "keyword": "5 рабочих дней"},
    {"question": "Хочу перейти на другой курс, как это сделать?", "kb_id": "kb8",
     "keyword": "перевод"},
    {"question": "Как связаться с преподавателем по курсу?", "kb_id": "kb10",
     "keyword": "Сообщения"},
]


def kb_numbers(kb_id):
    _, body = KB_BY_ID[kb_id]
    return sorted(set(re.findall(r"\d+", body)))


for q in TEST_QUESTIONS:
    q["kb_text"] = f"{q['kb_id']} · {KB_BY_ID[q['kb_id']][0]}: {KB_BY_ID[q['kb_id']][1]}"
    q["numbers"] = kb_numbers(q["kb_id"])

QMAP_JS = ",\n".join(
    "    {match: %s, kb_id: %s, kb_text: %s, kb_keyword: %s, kb_numbers: %s}" % (
        json.dumps(q["question"][:24], ensure_ascii=False),  # устойчивый обрывок для includes()
        json.dumps(q["kb_id"], ensure_ascii=False),
        json.dumps(q["kb_text"], ensure_ascii=False),
        json.dumps(q["keyword"], ensure_ascii=False),
        json.dumps(q["numbers"], ensure_ascii=False),
    ) for q in TEST_QUESTIONS
)

CONTACTS_JS = json.dumps(CONTACT_PHRASES, ensure_ascii=False)

def judge_criteria_text(keyword_expr):
    """`keyword_expr` — готовое n8n-выражение вида "{{ ... }}", вставляемое ВНУТРЬ текста
    промта как есть (не как JS-конкатенация строк — промты судьи в двух сценариях читают
    `kb_keyword` из разных узлов, поэтому выражение параметризовано, не зашито один раз)."""
    return (
        "1. Не длиннее 280 символов.\n"
        "2. Явно упоминает деталь «" + keyword_expr + "».\n"
        "3. Указывает, куда обращаться дальше (администратор / личный кабинет / "
        "преподаватель / сотрудник / руководитель).\n"
        "4. Не содержит чисел, которых нет в приведённом пункте базы.\n"
        "5. Полностью на русском языке — без латиницы и без иероглифов."
    )

# ---------------------------------------------------------------------------------------
# Общие узлы
# ---------------------------------------------------------------------------------------


def form_trigger(path):
    return {
        "id": "q_form", "name": "Client question", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [-260, 0], "webhookId": path,
        "parameters": {
            "path": path, "formTitle": "Замер K3 — вопрос",
            "formDescription": "Измерительный стенд Семинара 9, не форма студента",
            "formFields": {"values": [
                {"fieldLabel": "Вопрос", "fieldType": "textarea", "requiredField": True},
            ]},
            "options": {"appendAttribution": False},
        },
    }


def pick_kb_item_node(pos):
    """Идемпотентный узел: и ПЕРВЫЙ вход (из формы), и ВХОД ПЕТЛИ ПЕРЕДЕЛКИ (из `Prepare
    retry`) ведут сюда же — разбирает по `question`, какой пункт базы нужен, и несёт вперёд
    счётчик попытки/предыдущий ответ/причину отказа, если это не первый проход."""
    js = (
        "const inp = $input.item.json;\n"
        "const question = inp.question || inp['Вопрос'] || '';\n"
        "const MAP = [\n" + QMAP_JS + "\n];\n"
        "let picked = null;\n"
        "for (const m of MAP) { if (question.includes(m.match)) { picked = m; break; } }\n"
        "if (!picked) picked = MAP[0];\n"
        "return { json: {\n"
        "  question,\n"
        "  kb_id: picked.kb_id, kb_text: picked.kb_text, kb_keyword: picked.kb_keyword,\n"
        "  kb_numbers: picked.kb_numbers,\n"
        "  attempt: inp.attempt || 1,\n"
        "  prev_answer: inp.prev_answer || '', reason: inp.reason || '',\n"
        "} };\n"
    )
    return {
        "id": "pick_kb", "name": "Pick KB item", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": pos,
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript", "jsCode": js},
    }


def model_node(node_id, name, pos):
    return {
        "id": node_id, "name": name, "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "typeVersion": 1, "position": pos,
        "parameters": {"model": ANSWER_MODEL, "options": {}},
        "credentials": OPENROUTER_CRED,
    }


def generate_answer_node(pos):
    prompt = (
        "=Ты — ассистент поддержки учебного центра. Вот точный пункт базы знаний, на "
        "который должен опираться ответ:\n\n{{ $json.kb_text }}\n\nВопрос клиента: "
        "{{ $json.question }}\n\nНапиши короткий ответ клиенту. СТРОГИЕ требования:\n"
        "1. Не длиннее 280 символов.\n"
        "2. Явно включи деталь: «{{ $json.kb_keyword }}».\n"
        "3. Укажи, куда обращаться дальше — администратор, личный кабинет, преподаватель, "
        "сотрудник или руководитель.\n"
        "4. Не используй никаких чисел, кроме тех, что есть в приведённом пункте базы.\n"
        "5. Пиши полностью на русском языке — никакой латиницы и иероглифов.\n\n"
        "{{ $json.prev_answer ? ('Предыдущая попытка не прошла проверку: «' + "
        "$json.prev_answer + '». Причина: ' + $json.reason + '. Исправь именно эту "
        "проблему, остальные требования сохрани.') : '' }}"
    )
    return {
        "id": "generate", "name": "Generate answer",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5, "position": pos,
        "parameters": {"promptType": "define", "text": prompt, "options": {}},
    }


def judge_verdict_node(pos):
    schema = {
        "type": "object",
        "properties": {
            "ok": {"type": "boolean", "description": "true, если ответ проходит все 5 правил"},
            "reason": {"type": "string",
                       "description": "если ok=false — какое правило нарушено и почему"},
        },
        "required": ["ok", "reason"],
    }
    text = (
        "=Пункт базы знаний:\n{{ $('Pick KB item').item.json.kb_text }}\n\n"
        "Вопрос клиента: {{ $('Pick KB item').item.json.question }}\n\n"
        "Ответ, который нужно проверить: {{ $('Generate answer').item.json.text }}\n\n"
        "Проверь ответ по правилам:\n" + judge_criteria_text(
            "{{ $('Pick KB item').item.json.kb_keyword }}") + "\n\n"
        "Если нарушено хоть одно правило — ok=false и назови правило."
    )
    return {
        "id": "judge", "name": "Judge verdict",
        "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
        "position": pos,
        "parameters": {
            "text": text, "schemaType": "manual",
            "inputSchema": json.dumps(schema, ensure_ascii=False, indent=2),
            "options": {},
        },
    }


def code_check_node(pos):
    js = (
        "const kb = $('Pick KB item').item.json;\n"
        "const answer = $('Generate answer').item.json.text || '';\n"
        "const reasons = [];\n"
        "if (answer.length > 280) reasons.push('длиннее 280 символов');\n"
        "if (!answer.toLowerCase().includes(kb.kb_keyword.toLowerCase()))\n"
        "  reasons.push('нет детали «' + kb.kb_keyword + '»');\n"
        "const contacts = " + CONTACTS_JS + ";\n"
        "if (!contacts.some(c => answer.toLowerCase().includes(c)))\n"
        "  reasons.push('не указано, куда обращаться дальше');\n"
        "const nums = answer.match(/\\d+/g) || [];\n"
        "const allowed = new Set(kb.kb_numbers);\n"
        "const badNums = nums.filter(n => !allowed.has(n));\n"
        "if (badNums.length) reasons.push('числа не из базы: ' + badNums.join(','));\n"
        "if (/[A-Za-z]/.test(answer)) reasons.push('есть латиница');\n"
        "if (/[\\u4e00-\\u9fff]/.test(answer)) reasons.push('есть иероглифы');\n"
        "const ok = reasons.length === 0;\n"
        "return { json: { output: { ok, reason: reasons.join('; ') } } };\n"
    )
    return {
        "id": "code_check", "name": "Code check", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": pos,
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript", "jsCode": js},
    }


def retry_if_node(pos):
    return {
        "id": "retry_if", "name": "Retry or finish?", "type": "n8n-nodes-base.if",
        "typeVersion": 2.2, "position": pos,
        "parameters": {"conditions": {
            "options": {"caseSensitive": True, "typeValidation": "strict"},
            "combinator": "and", "conditions": [{
                "leftValue": "={{ $json.output.ok === true || "
                             "$('Pick KB item').item.json.attempt >= " + str(MAX_ATTEMPTS)
                             + " }}",
                "rightValue": True,
                "operator": {"type": "boolean", "operation": "equals"}}]}},
    }


def converged_if_node(pos):
    return {
        "id": "converged_if", "name": "Converged?", "type": "n8n-nodes-base.if",
        "typeVersion": 2.2, "position": pos,
        "parameters": {"conditions": {
            "options": {"caseSensitive": True, "typeValidation": "strict"},
            "combinator": "and", "conditions": [{
                "leftValue": "={{ $json.output.ok === true }}",
                "rightValue": True,
                "operator": {"type": "boolean", "operation": "equals"}}]}},
    }


def prepare_retry_node(pos):
    js = (
        "return { json: {\n"
        "  question: $('Pick KB item').item.json.question,\n"
        "  attempt: $('Pick KB item').item.json.attempt + 1,\n"
        "  prev_answer: $('Generate answer').item.json.text,\n"
        "  reason: $json.output.reason,\n"
        "} };\n"
    )
    return {
        "id": "prepare_retry", "name": "Prepare retry", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": pos,
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript", "jsCode": js},
    }


def write_row_node(node_id, name, pos, variant, converged_expr, check_ok_expr, reason_expr):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.dataTable",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "operation": "insert",
            "dataTableId": {"__rl": True, "value": "", "mode": "id",
                             "cachedResultName": S9_TABLE_NAME},
            "columns": {
                "mappingMode": "defineBelow",
                "value": {
                    "variant": variant,
                    "question": "={{ $('Pick KB item').item.json.question }}",
                    "attempt": "={{ $('Pick KB item').item.json.attempt }}",
                    "answer": "={{ $('Generate answer').item.json.text }}",
                    "check_ok": check_ok_expr,
                    "reason": reason_expr,
                    "converged": converged_expr,
                },
                "matchingColumns": [], "schema": [],
            },
            "options": {},
        },
    }


def result_screen_node(node_id, name, pos, title, message):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.form", "typeVersion": 1,
        "position": pos,
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": title, "completionMessage": message,
            "options": {"appendAttribution": False},
        },
    }


def set_table_id(wf, table_id):
    for n in wf["nodes"]:
        if n["type"] == "n8n-nodes-base.dataTable":
            n["parameters"]["dataTableId"] = {
                "__rl": True, "value": table_id, "mode": "list",
                "cachedResultName": S9_TABLE_NAME}
    return wf


# ---------------------------------------------------------------------------------------
# s9-m3-once — база сравнения, один вызов без цикла
# ---------------------------------------------------------------------------------------

def case3_once():
    path = "s9-m3-once"
    nodes = [
        form_trigger(path),
        pick_kb_item_node([-20, 0]),
        model_node("m_once", "Model (once)", [200, 180]),
        generate_answer_node([200, 0]),
        code_check_node([420, 0]),
        write_row_node("write_once", "Write row", [640, 0], "once",
                        "", "={{ $json.output.ok }}", "={{ $json.output.reason }}"),
        result_screen_node("result_once", "Result screen", [860, 0],
                            "Ответ (без цикла)",
                            "=Вопрос: {{ $('Pick KB item').item.json.question }}<br><br>"
                            "Ответ: {{ $('Generate answer').item.json.text }}"),
    ]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Generate answer", "type": "main", "index": 0}]]},
        "Generate answer": {"main": [[{"node": "Code check", "type": "main", "index": 0}]]},
        "Code check": {"main": [[{"node": "Write row", "type": "main", "index": 0}]]},
        "Write row": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (once)": {"ai_languageModel": [[
            {"node": "Generate answer", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · без цикла (once)", "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


# ---------------------------------------------------------------------------------------
# s9-m3-judge — цикл, проверяющий — та же модель (судья), лимит 3 попытки
# ---------------------------------------------------------------------------------------

def case3_judge():
    path = "s9-m3-judge"
    nodes = [
        form_trigger(path),
        pick_kb_item_node([-20, 0]),
        model_node("m_gen", "Model (generate)", [200, 180]),
        generate_answer_node([200, 0]),
        model_node("m_judge", "Model (judge)", [420, 180]),
        judge_verdict_node([420, 0]),
        retry_if_node([640, 0]),
        prepare_retry_node([640, 220]),
        converged_if_node([860, -80]),
        write_row_node("write_ok", "Write row (ok)", [1080, -160], "judge",
                        "true", "true", "''"),
        result_screen_node("result_ok", "Result screen (ok)", [1300, -160],
                            "Ответ (цикл с судьёй-моделью)",
                            "=Вопрос: {{ $('Pick KB item').item.json.question }}<br><br>"
                            "Ответ: {{ $('Generate answer').item.json.text }}"),
        write_row_node("write_notconv", "Write row (not converged)", [1080, 0], "judge",
                        "false", "false", "={{ $json.output.reason }}"),
        result_screen_node("result_notconv", "Result screen (не сошлось)", [1300, 0],
                            "Не сошлось за 3 попытки",
                            "=Не удалось за 3 попытки получить ответ, прошедший проверку "
                            "судьи-модели — вопрос передан сотруднику."),
    ]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Generate answer", "type": "main", "index": 0}]]},
        "Generate answer": {"main": [[{"node": "Judge verdict", "type": "main", "index": 0}]]},
        "Judge verdict": {"main": [[{"node": "Retry or finish?", "type": "main", "index": 0}]]},
        "Retry or finish?": {"main": [
            [{"node": "Converged?", "type": "main", "index": 0}],
            [{"node": "Prepare retry", "type": "main", "index": 0}],
        ]},
        "Prepare retry": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Converged?": {"main": [
            [{"node": "Write row (ok)", "type": "main", "index": 0}],
            [{"node": "Write row (not converged)", "type": "main", "index": 0}],
        ]},
        "Write row (ok)": {"main": [[
            {"node": "Result screen (ok)", "type": "main", "index": 0}]]},
        "Write row (not converged)": {"main": [[
            {"node": "Result screen (не сошлось)", "type": "main", "index": 0}]]},
        "Model (generate)": {"ai_languageModel": [[
            {"node": "Generate answer", "type": "ai_languageModel", "index": 0}]]},
        "Model (judge)": {"ai_languageModel": [[
            {"node": "Judge verdict", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · цикл с судьёй-моделью", "nodes": nodes,
            "connections": conn, "settings": {"executionOrder": "v1"}}


# ---------------------------------------------------------------------------------------
# s9-m3-code — цикл, проверяющий — код, лимит 3 попытки, явная ветка «не сошлось»
# ---------------------------------------------------------------------------------------

def case3_code():
    path = "s9-m3-code"
    nodes = [
        form_trigger(path),
        pick_kb_item_node([-20, 0]),
        model_node("m_gen2", "Model (generate)", [200, 180]),
        generate_answer_node([200, 0]),
        code_check_node([420, 0]),
        retry_if_node([640, 0]),
        prepare_retry_node([640, 220]),
        converged_if_node([860, -80]),
        write_row_node("write_ok_c", "Write row (ok)", [1080, -160], "code",
                        "true", "true", "''"),
        result_screen_node("result_ok_c", "Result screen (ok)", [1300, -160],
                            "Ответ (цикл с кодовой проверкой)",
                            "=Вопрос: {{ $('Pick KB item').item.json.question }}<br><br>"
                            "Ответ: {{ $('Generate answer').item.json.text }}"),
        write_row_node("write_notconv_c", "Write row (not converged)", [1080, 0], "code",
                        "false", "false", "={{ $json.output.reason }}"),
        result_screen_node("result_notconv_c", "Result screen (не сошлось)", [1300, 0],
                            "Не сошлось за 3 попытки",
                            "=Не удалось за 3 попытки получить ответ, прошедший кодовую "
                            "проверку — вопрос передан сотруднику (не отдаём последнюю "
                            "непрошедшую версию молча)."),
    ]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Generate answer", "type": "main", "index": 0}]]},
        "Generate answer": {"main": [[{"node": "Code check", "type": "main", "index": 0}]]},
        "Code check": {"main": [[{"node": "Retry or finish?", "type": "main", "index": 0}]]},
        "Retry or finish?": {"main": [
            [{"node": "Converged?", "type": "main", "index": 0}],
            [{"node": "Prepare retry", "type": "main", "index": 0}],
        ]},
        "Prepare retry": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Converged?": {"main": [
            [{"node": "Write row (ok)", "type": "main", "index": 0}],
            [{"node": "Write row (not converged)", "type": "main", "index": 0}],
        ]},
        "Write row (ok)": {"main": [[
            {"node": "Result screen (ok)", "type": "main", "index": 0}]]},
        "Write row (not converged)": {"main": [[
            {"node": "Result screen (не сошлось)", "type": "main", "index": 0}]]},
        "Model (generate)": {"ai_languageModel": [[
            {"node": "Generate answer", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · цикл с кодовой проверкой", "nodes": nodes,
            "connections": conn, "settings": {"executionOrder": "v1"}}


# ---------------------------------------------------------------------------------------
# s9-m3-judge-check — разовая проверка судьёй-моделью НАД уже готовым ответом + кодовым
# вердиктом, который он уже получил (для несущего числа кейса — где они расходятся)
# ---------------------------------------------------------------------------------------

def case3_judge_check():
    path = "s9-m3-judge-check"
    form = {
        "id": "jc_form", "name": "Client question", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [-260, 0], "webhookId": path,
        "parameters": {
            "path": path, "formTitle": "Замер K3 — судья проверяет готовый ответ",
            "formDescription": "Измерительный стенд Семинара 9",
            "formFields": {"values": [
                {"fieldLabel": "Вопрос", "fieldType": "textarea", "requiredField": True},
                {"fieldLabel": "Ответ", "fieldType": "textarea", "requiredField": True},
                {"fieldLabel": "КодСказал", "fieldType": "text", "requiredField": True},
            ]},
            "options": {"appendAttribution": False},
        },
    }
    pick_js = (
        "const inp = $input.item.json;\n"
        "const question = inp['Вопрос'] || '';\n"
        "const answer = inp['Ответ'] || '';\n"
        "const codeSaid = inp['КодСказал'] || '';\n"
        "const MAP = [\n" + QMAP_JS + "\n];\n"
        "let picked = null;\n"
        "for (const m of MAP) { if (question.includes(m.match)) { picked = m; break; } }\n"
        "if (!picked) picked = MAP[0];\n"
        "return { json: {\n"
        "  question, answer, code_said: codeSaid,\n"
        "  kb_id: picked.kb_id, kb_text: picked.kb_text, kb_keyword: picked.kb_keyword,\n"
        "  kb_numbers: picked.kb_numbers,\n"
        "} };\n"
    )
    pick = {
        "id": "pick_kb_jc", "name": "Pick KB item", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": [-20, 0],
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript",
                        "jsCode": pick_js},
    }
    schema = {
        "type": "object",
        "properties": {
            "ok": {"type": "boolean"},
            "reason": {"type": "string"},
        },
        "required": ["ok", "reason"],
    }
    judge_text = (
        "=Пункт базы знаний:\n{{ $('Pick KB item').item.json.kb_text }}\n\n"
        "Вопрос клиента: {{ $('Pick KB item').item.json.question }}\n\n"
        "Ответ, который нужно проверить: {{ $('Pick KB item').item.json.answer }}\n\n"
        "Проверь ответ по правилам:\n" + judge_criteria_text(
            "{{ $('Pick KB item').item.json.kb_keyword }}") + "\n\n"
        "Если нарушено хоть одно правило — ok=false и назови правило."
    )
    judge = {
        "id": "judge_jc", "name": "Judge verdict",
        "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
        "position": [200, 0],
        "parameters": {
            "text": judge_text, "schemaType": "manual",
            "inputSchema": json.dumps(schema, ensure_ascii=False, indent=2),
            "options": {},
        },
    }
    model = model_node("m_jc", "Model (judge-check)", [200, 180])
    write = {
        "id": "write_jc", "name": "Write row", "type": "n8n-nodes-base.dataTable",
        "typeVersion": 1, "position": [420, 0],
        "parameters": {
            "operation": "insert",
            "dataTableId": {"__rl": True, "value": "", "mode": "id",
                             "cachedResultName": S9_TABLE_NAME},
            "columns": {
                "mappingMode": "defineBelow",
                "value": {
                    "variant": "judge-check",
                    "question": "={{ $('Pick KB item').item.json.question }}",
                    "attempt": 1,
                    "answer": "={{ $('Pick KB item').item.json.answer }}",
                    "check_ok": "={{ $json.output.ok }}",
                    "reason": "=код: {{ $('Pick KB item').item.json.code_said }} / "
                              "судья: {{ $json.output.reason }}",
                    "converged": "",
                },
                "matchingColumns": [], "schema": [],
            },
            "options": {},
        },
    }
    result = result_screen_node("result_jc", "Result screen", [640, 0],
                                 "Сверка судьи и кода",
                                 "=Судья: {{ $json.output.ok }} ({{ $json.output.reason "
                                 "}}) / код сказал: {{ $('Pick KB item').item.json"
                                 ".code_said }}")
    nodes = [form, pick, model, judge, write, result]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Judge verdict", "type": "main", "index": 0}]]},
        "Judge verdict": {"main": [[{"node": "Write row", "type": "main", "index": 0}]]},
        "Write row": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (judge-check)": {"ai_languageModel": [[
            {"node": "Judge verdict", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · судья проверяет готовый ответ", "nodes": nodes,
            "connections": conn, "settings": {"executionOrder": "v1"}}


STAGES = {
    "case3-once": case3_once, "case3-judge": case3_judge, "case3-code": case3_code,
    "case3-judge-check": case3_judge_check,
}


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def ensure_table():
    tables = api("GET", "/data-tables")["data"]
    for t in tables:
        if t["name"] == S9_TABLE_NAME:
            return t["id"]
    created = api("POST", "/data-tables", {
        "name": S9_TABLE_NAME,
        "projectId": tables[0]["projectId"] if tables else None,
        "columns": [
            {"name": "variant", "type": "string"},
            {"name": "question", "type": "string"},
            {"name": "attempt", "type": "number"},
            {"name": "answer", "type": "string"},
            {"name": "check_ok", "type": "string"},
            {"name": "reason", "type": "string"},
            {"name": "converged", "type": "string"},
        ],
    })
    return created["id"]


def main():
    push = "--push" in sys.argv
    table_id = None
    existing = {}
    if push:
        table_id = ensure_table()
        existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
    for fname, fn in STAGES.items():
        wf = fn()
        if push:
            wf = set_table_id(wf, table_id)
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
