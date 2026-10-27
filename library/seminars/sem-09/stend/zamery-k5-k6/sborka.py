#!/usr/bin/env python3
"""Собрать стенд Замеров 3-4 (Кейсы 5 и 6) Семинара 9 — issue #299.

Четыре сценария, все с именем, начинающимся на «С9 · замер K5 »/«С9 · замер K6 », и с
вебхуком, начинающимся на `s9-m5-`/`s9-m6-` — правило зоны этой сессии, не затрагивает ни
один узел С7/С8/С9-производства.

    k5-repeat.json    Замер 3.1 — копия процесса Кейса 1 версии 1 (свободный ответ,
                       `chainLlm`, база знаний целиком в промте), с явной Sampling
                       Temperature=0 — тот же узел, которого в найденном исходнике нет
                       возможности пином зафиксировать (`research/03`, Находка 8), только
                       температура. 25 одинаковых запросов читают, сколько уникальных
                       ответов получится и совпадают ли они по СУТИ (не по формулировке).
    k5-order-a.json    Замер 3.2, схема А — структурированный вывод, поле `answer` ПЕРВЫМ,
                       `reasoning` вторым.
    k5-order-b.json    Замер 3.2, схема Б — то же, но `reasoning` ПЕРВЫМ, `answer` вторым
                       (порядок полей — единственное отличие от схемы А; дословно про это
                       Находка 4 `research/03`: порядок полей переворачивает знак эффекта).
    k6-read.json       Замер 4 — чтение фотографии квитанции. Вместо Form Trigger с полем
                       загрузки файла (где конвертация бинарных данных в base64 внутри
                       n8n-выражений — зыбкая, непроверенная механика, см. README §
                       «Методическое упрощение») узел `Webhook` принимает уже закодированное
                       `image_base64` от прогонщика (тот же файл на диске, что уйдёт в
                       модель — прогонщик не меняет байты, только кодирует их в base64 перед
                       HTTP-телом, это не «подделка», а перенос одного механического шага из
                       n8n в Python, см. README). Дальше — настоящий `HTTP Request` к
                       `POST https://openrouter.ai/api/v1/chat/completions` с vision-
                       сообщением (прямой вызов API, единственный путь, которым узел
                       `OpenRouter Chat Model` не является, см. `research/03`, Находка 8) —
                       структурированный JSON-ответ `{sum_rub, date, raw_text_seen}`
                       возвращается как ответ вебхука (`responseMode: lastNode`) и читается
                       прогонщиком и напрямую из `GET /executions`.

## Ключи и зона

Ключи — только из /home/harness/.n8n-lab-credentials через окружение.

    python3 sborka.py                                      только записать json рядом
    N8N_API_URL=... N8N_API_KEY=... python3 sborka.py --push   выложить и опубликовать

`OpenRouter account` (`VbxiQn8TbqA4R2mw`) — существующий credential стенда, переиспользован
без новой инфраструктуры. Новых Data Table и таблиц не создано — замеры читаются напрямую
через `GET /executions/<id>?includeData=true` (тот же приём, что `sem-08/stend/
run_refund_test.py` использует для Кейса 3 С8), это не создаёт дополнительной
инфраструктуры, которую потом нужно было бы объяснять отдельно от самого замера.
"""
import importlib.util
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
STEND = HERE.parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

# Импорт модулем по пути, НЕ через `sys.path.insert` + `import sborka` — оба файла в этой
# цепочке (sem-09/stend/sborka.py, sem-08/stend/sborka.py и этот файл) называются одинаково
# `sborka.py`; обычный `import sborka` коллизирует через общий ключ `sys.modules['sborka']`
# (sem-09/stend/sborka.py сам импортирует sem-08 под тем же именем «sborka» — при вложенном
# импорте подставился бы недогруженный сам себя). `importlib` грузит файл под отдельным
# именем `sem09_sborka`, коллизии нет.
_spec = importlib.util.spec_from_file_location(
    "sem09_sborka", str((STEND / "sborka.py").resolve()))
s9 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(s9)

OPENROUTER_CRED = s9.OPENROUTER_CRED
ANSWER_MODEL = s9.ANSWER_MODEL
VISION_MODEL = "qwen/qwen3-vl-8b-instruct"  # дешёвая мультимодальная модель, та же семья
# qwen, что и текстовая модель остального стенда — не новая категория инфраструктуры.
# `research/07` предлагал `qwen/qwen2.5-vl-7b-instruct`, но прогон (execution 658, этот
# заход) показал, что OpenRouter эту конкретную строку больше не числит валидным id модели
# ("qwen/qwen2.5-vl-7b-instruct is not a valid model ID") — проверено `GET
# https://openrouter.ai/api/v1/models` 2026-10-25: в списке есть qwen3-vl-8b-instruct
# ($0,25/$0,75 за млн токенов, prompt/completion) и qwen2.5-vl-72b-instruct (втрое дороже,
# другой размер), но не qwen2.5-vl-7b-instruct — модельный ряд провайдера сдвинулся вперёд
# за время между исследованием и замером; взял ближайшую по цене и назначению.


# ---------------------------------------------------------------------------------------
# Замер 3.1 — Кейс 5: 25 повторов одного вопроса при T=0 (копия процесса Кейса 1, версия 1)
# ---------------------------------------------------------------------------------------

def k5_repeat():
    path = "s9-m5-repeat"
    nodes = [s9.client_question_form(path)]
    nodes.append({
        "id": "k5_model", "name": "Model (T=0)",
        "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
        "position": [60, 220],
        "parameters": {"model": ANSWER_MODEL, "options": {"temperature": 0}},
        "credentials": OPENROUTER_CRED,
    })
    nodes.append({
        "id": "k5_answer", "name": "Answer (free, T=0)",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5,
        "position": [60, 0],
        "parameters": {
            "promptType": "define",
            "text": (
                "=Ты — ассистент поддержки учебного центра. Ниже база знаний, которой "
                "можно пользоваться для ответа.\n\n" + s9.kb_text() + "\n\nВопрос клиента: "
                "{{ $json['Вопрос'] }}\n\nОтветь по существу и по-русски, коротко (2-4 "
                "предложения). Если ответа в базе знаний нет и ты не уверена — честно "
                "напиши, что не знаешь, и что ответит сотрудник. Если уверена — отвечай "
                "прямо, без оговорок."
            ),
            "options": {},
        },
    })
    nodes.append({
        "id": "k5_result", "name": "Result screen", "type": "n8n-nodes-base.form",
        "typeVersion": 1, "position": [300, 0],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Ответ (замер K5 — повторы T=0)",
            "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                  "}}<br><br>Ответ: {{ $('Answer (free, T=0)')"
                                  ".item.json.text }}",
            "options": {"appendAttribution": False},
        },
    })
    conn = {
        "Client question": {"main": [[{"node": "Answer (free, T=0)", "type": "main", "index": 0}]]},
        "Answer (free, T=0)": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (T=0)": {"ai_languageModel": [[
            {"node": "Answer (free, T=0)", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K5 — повторы одного вопроса при T=0",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


# ---------------------------------------------------------------------------------------
# Замер 3.2 — Кейс 5: порядок полей структурированного вывода (А — ответ первым,
# Б — рассуждение первым), 10 арифметических вопросов на каждую схему
# ---------------------------------------------------------------------------------------

def _order_schema(answer_first):
    answer_field = ("answer", {"type": "number",
                     "description": "итоговая сумма возврата в рублях, только число"})
    reasoning_field = ("reasoning", {"type": "string",
                        "description": "объясни вычисление коротко, шаг за шагом"})
    pair = [answer_field, reasoning_field] if answer_first else [reasoning_field, answer_field]
    return {
        "type": "object",
        "properties": dict(pair),
        "required": [k for k, _ in pair],
    }


def _k5_order_workflow(answer_first, path, label):
    nodes = [s9.client_question_form(path)]
    nodes[0]["id"] = "k5o_form"
    nodes.append({
        "id": "k5o_model", "name": "Model (order test)",
        "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
        "position": [60, 220],
        "parameters": {"model": ANSWER_MODEL, "options": {}},
        "credentials": OPENROUTER_CRED,
    })
    schema = _order_schema(answer_first)
    node_name = "Extract (answer-first)" if answer_first else "Extract (reasoning-first)"
    nodes.append({
        "id": "k5o_extract", "name": node_name,
        "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
        "position": [60, 0],
        "parameters": {
            "text": "=Вопрос клиента учебного центра: {{ $json['Вопрос'] }}",
            "schemaType": "manual",
            "inputSchema": json.dumps(schema, ensure_ascii=False, indent=2),
            "options": {},
        },
    })
    nodes.append({
        "id": "k5o_result", "name": "Result screen", "type": "n8n-nodes-base.form",
        "typeVersion": 1, "position": [300, 0],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": f"Ответ (замер K5 — порядок полей, {label})",
            "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                  "}}<br><br>answer: {{ $json.output.answer }}<br>"
                                  "reasoning: {{ $json.output.reasoning }}",
            "options": {"appendAttribution": False},
        },
    })
    conn = {
        "Client question": {"main": [[{"node": node_name, "type": "main", "index": 0}]]},
        node_name: {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (order test)": {"ai_languageModel": [[
            {"node": node_name, "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": f"С9 · замер K5 — порядок полей, {label}",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def k5_order_a():
    return _k5_order_workflow(True, "s9-m5-order-a", "ответ первым")


def k5_order_b():
    return _k5_order_workflow(False, "s9-m5-order-b", "рассуждение первым")


# ---------------------------------------------------------------------------------------
# Замер 4 — Кейс 6: чтение фотографии квитанции (сумма, дата) через прямой HTTP Request
# к OpenRouter (vision), webhook принимает уже готовый base64 от прогонщика
# ---------------------------------------------------------------------------------------

def k6_read():
    path = "s9-m6-read"
    nodes = [{
        "id": "k6_webhook", "name": "Receipt photo", "type": "n8n-nodes-base.webhook",
        "typeVersion": 2, "position": [-180, 0],
        "webhookId": path,
        "parameters": {
            "httpMethod": "POST", "path": path, "responseMode": "lastNode",
            "options": {},
        },
    }]
    nodes.append({
        "id": "k6_build_body", "name": "Build vision request", "type": "n8n-nodes-base.set",
        "typeVersion": 3.4, "position": [60, 0],
        "parameters": {
            "mode": "manual", "includeOtherFields": False,
            "assignments": {"assignments": [
                {"id": "b1", "name": "model", "type": "string", "value": VISION_MODEL},
                {"id": "b2", "name": "data_url", "type": "string",
                 "value": "={{ 'data:' + $json.body.mime_type + ';base64,' + "
                          "$json.body.image_base64 }}"},
                {"id": "b3", "name": "receipt_id", "type": "string",
                 "value": "={{ $json.body.receipt_id }}"},
            ]},
            "options": {},
        },
    })
    # НЕ подставлять сюда конкретное число-пример для sum_rub (протечка найдена и исправлена
    # 2026-10-27, issue #299 — см. README «Протечка промта обнаружена и исправлена»):
    # исходная версия промта содержала `например 18990.00`, что было РЕАЛЬНОЙ суммой
    # receipt-01 — единственной квитанции, на которой строится это измерение. Модели не
    # нужно было читать фотографию, достаточно было скопировать число из своей же
    # инструкции; это полностью объясняет 100% точность суммы даже на 53×64px, где
    # глазом не видно ни одной цифры. Формат описывается без числового примера — по тому
    # же образцу, что уже стоит у даты ниже (там примера-значения никогда не было).
    prompt_text = (
        "На фотографии — квитанция об оплате курса учебного центра, снятая телефоном "
        "(возможны перекос, шум, нерезкость). Прочитай с неё СУММУ платежа и ДАТУ. "
        "Ответь СТРОГО в формате JSON без markdown-разметки и пояснений вокруг: "
        '{"sum_rub": <число без пробелов и валюты>, '
        '"date": "<дата в формате ДД.ММ.ГГГГ как написана на квитанции>", '
        '"raw_text_seen": "<что именно ты прочитал в строке суммы, дословно>"}. '
        "Если строку суммы или даты невозможно разобрать уверенно — всё равно верни "
        "лучшую догадку в sum_rub/date, а в raw_text_seen честно напиши, что не уверена."
    )
    nodes.append({
        "id": "k6_http", "name": "Read receipt (OpenRouter vision)",
        "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2, "position": [300, 0],
        "parameters": {
            "method": "POST", "url": "https://openrouter.ai/api/v1/chat/completions",
            "authentication": "predefinedCredentialType",
            "nodeCredentialType": "openRouterApi",
            "sendBody": True, "specifyBody": "json",
            "jsonBody": (
                "={{ JSON.stringify({\n"
                "  model: $json.model,\n"
                "  messages: [{\n"
                "    role: 'user',\n"
                "    content: [\n"
                "      { type: 'text', text: " + json.dumps(prompt_text, ensure_ascii=False) + " },\n"
                "      { type: 'image_url', image_url: { url: $json.data_url } }\n"
                "    ]\n"
                "  }],\n"
                "  response_format: { type: 'json_object' },\n"
                "  temperature: 0.2\n"
                "}) }}"
            ),
            "options": {},
        },
        "credentials": OPENROUTER_CRED,
    })
    conn = {
        "Receipt photo": {"main": [[{"node": "Build vision request", "type": "main", "index": 0}]]},
        "Build vision request": {"main": [[
            {"node": "Read receipt (OpenRouter vision)", "type": "main", "index": 0}]]},
    }
    return {"name": "С9 · замер K6 — чтение фотографии квитанции",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def api(method, path, body=None):
    import urllib.request
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


STAGES = {
    "k5-repeat": k5_repeat, "k5-order-a": k5_order_a, "k5-order-b": k5_order_b,
    "k6-read": k6_read,
}


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
