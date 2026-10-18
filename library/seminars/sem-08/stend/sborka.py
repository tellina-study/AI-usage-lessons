#!/usr/bin/env python3
"""Собрать стадии Семинара 8 — ДОСТРОЙКА `student.json` Семинара 7, не замена.

**Статус на 2026-10-18 (второй проход): выложено и прогнано настоящими прогонами.**
Блокер первого прохода (отсутствие `N8N_API_KEY`) снят владельцем — ключ лежит в
`/home/harness/.n8n-lab-credentials` (вне репозитория, chmod 600), читается только оттуда.
Credential-узлы ниже — РЕАЛЬНЫЕ id с живого стенда, не пустые ссылки.

**Процесс (A) Кейса 3 — через OpenRouter, не через локальную Ollama.** Первая попытка этого
прохода (поднять Ollama локально + туннель cloudflared/ngrok к удалённому стенду) была
остановлена по прямому слову владельца: n8n стенд — удалённый, Ollama на агентской машине для
него недостижима без туннеля, а туннель — ровно та лишняя сложность, которую сам Кейс 1 этого
же занятия учит не создавать. На стенде уже есть работающий credential `OpenRouter account`
(`VbxiQn8TbqA4R2mw`, тот же, что использует С7 для шага extraction) — он и переиспользован для
процесса (A), моделью `qwen/qwen-2.5-7b-instruct` (подтверждена в каталоге
`https://openrouter.ai/api/v1/models`). Следов Ollama/cloudflared в этом файле не осталось.

    python3 sborka.py                                      только записать json-файлы рядом
    N8N_API_URL=... N8N_API_KEY=... python3 sborka.py --push   выложить и опубликовать

## Шесть файлов — по кейсам занятия, каждый ДОСТРАИВАЕТ стадию 4 Семинара 7

    stage-1-before.json   Кейс 1 «до»: отдельный LLM-узел сочиняет текст Telegram-уведомления
    stage-1-after.json    Кейс 1 «после»: узел подстановки переменных (шаблон) вместо модели
    stage-2.json          Кейс 2: дедупликация — механический фильтр, затем LLM на спорное
    stage-3a-model.json   Кейс 3, процесс (A): решение о возврате принимает модель (OpenRouter)
    stage-3b-code.json    Кейс 3, процесс (B): решение принимает `IF`-узел по сумме
    stage-4.json          Кейс 4: та же цепочка уведомления, плюс картинка в Telegram

Все шесть читают структуру существующих узлов из `sem-07/stend/student.json` (форма →
извлечение → справочник → таблица → экран) и ТОЛЬКО ДОБАВЛЯЮТ узлы — ни один узел С7 не
переименован и не удалён, в точности как того требует шов из `ARCHITECTURE.md` §2.

## Секреты — читаются из окружения/внешнего файла, в этот файл не вписаны

`N8N_API_URL`/`N8N_API_KEY` — из окружения (см. запуск выше). Настоящий токен Telegram-бота и
настоящий `chat_id` НЕ хардкожены здесь как секрет-значения: `TELEGRAM_CHAT_ID` — не секрет
(это просто числовой адрес чата, нужен n8n-узлу так же, как имя таблицы нужно узлу Data Table
в `student.json`), а сам токен бота живёт только в n8n-credential `kfXE6PWKNzA56vc6`,
созданном на стенде через управляющий API и никогда не попадавший в файл репозитория
(см. `README.md` «Шаг 1»).
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
S7 = HERE.parent.parent / "sem-07" / "stend"
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

STUDENT = json.loads((S7 / "student.json").read_text(encoding="utf-8"))

# Порог возврата для Кейса 3 — зафиксирован здесь как единственный источник правды для
# ГЕНЕРАТОРА; реальный стенд должен держать то же число и в промпте процесса (A), и в условии
# `IF`-узла процесса (B) — ровно нюанс №2 Кейса 3 в `SETKA-KEYSOV-S8.md`: порог не должен жить
# в двух местах, которые надеются совпасть.
REFUND_THRESHOLD = 3000  # рублей — «мелкий» возврат одобряется процессом без эскалации

# Credential-узлы — РЕАЛЬНЫЕ id с живого стенда n8n.lessons.tellian.io (проверены
# `POST /credentials/<id>/test` → {"status":"OK"} для Telegram, и уже использовались С7 для
# OpenRouter — не секреты сами по себе, только ссылки на то, где секрет хранится на стенде).
TG_CRED = {"telegramApi": {"id": "kfXE6PWKNzA56vc6", "name": "Telegram account (С8)"}}
OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}
TELEGRAM_CHAT_ID = "266536553"  # координатор, подтвердил /start боту; не секрет (ADR см. README)
NOTIFY_MODEL = "openai/gpt-4o-mini"           # та же модель, что в student.json на extraction
REFUND_MODEL = "qwen/qwen-2.5-7b-instruct"    # средне-размерная Qwen через OpenRouter

# `student.json` — файл НА ВЫНОС студенту, и `student_file()` в `sem-07/stend/sborka.py`
# намеренно снимает с узлов credential модели и ссылку на таблицу (чужой id читается как
# сломанный узел, см. docstring той функции). Для РЕАЛЬНОГО стенда — наоборот: эти ссылки
# нужно восстановить на то же, с чем и так работает стенд С7 (общая таблица `requests`).
TABLE_ID = "xlDAQCm75jLAKNom"
TABLE_NAME = "requests"


def base_nodes():
    """Шесть узлов стадии 4 С7 — копия (не ссылка), с восстановленными ссылками на
    реальный стенд, которые `student.json` снимает для студента: credential узла
    `Model` и `dataTableId` узлов записи."""
    nodes = json.loads(json.dumps(STUDENT["nodes"]))
    for n in nodes:
        if n["type"] == "@n8n/n8n-nodes-langchain.lmChatOpenRouter":
            n["credentials"] = OPENROUTER_CRED
        if n["type"] == "n8n-nodes-base.dataTable":
            n["parameters"]["dataTableId"] = {
                "__rl": True, "value": TABLE_ID, "mode": "list",
                "cachedResultName": TABLE_NAME}
    return nodes


def base_connections():
    return json.loads(json.dumps(STUDENT["connections"]))


def set_form_path(nodes, path):
    """`student.json` сбрасывает путь формы на общий `sem-07` (правильно для файла на
    вынос — у каждого студента свой импорт). На живом стенде каждая стадия С8 обязана
    получить СВОЙ путь, иначе формы разных стадий молча делят один webhook."""
    for n in nodes:
        if n["type"] == "n8n-nodes-base.formTrigger":
            n["parameters"]["path"] = path
            n["webhookId"] = path
    return nodes


def openrouter_model_node(node_id, name, pos, model=NOTIFY_MODEL):
    return {
        "id": node_id, "name": name, "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "typeVersion": 1, "position": pos,
        "parameters": {"model": model, "options": {}},
        "credentials": OPENROUTER_CRED,
    }


def telegram_text_node(node_id, name, pos, text_expr):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.telegram",
        "typeVersion": 1.2, "position": pos,
        "parameters": {
            "operation": "sendMessage",
            "chatId": TELEGRAM_CHAT_ID,
            "text": text_expr,
            "additionalFields": {},
        },
        "credentials": TG_CRED,
    }


def telegram_photo_node(node_id, name, pos, caption_expr):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.telegram",
        "typeVersion": 1.2, "position": pos,
        "parameters": {
            "operation": "sendPhoto",
            "chatId": TELEGRAM_CHAT_ID,
            "binaryData": True,
            "additionalFields": {"caption": caption_expr},
        },
        "credentials": TG_CRED,
    }


def llm_notification_node(pos):
    """Кейс 1 «до»: отдельная цепочка модели сочиняет текст «по-человечески».

    Прогнать на стенде несколько раз подряд на РАЗНЫХ заявках и сохранить хотя бы
    один реальный пример расхождения (деталь, которой не было в заявке) —
    см. README.md «Находки прогонов»."""
    return {
        "id": "notify_llm", "name": "Compose notification (LLM)",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5, "position": pos,
        "parameters": {
            "promptType": "define",
            "text": (
                "=Напиши короткое дружелюбное уведомление координатору учебного центра "
                "в Telegram о новой многотемной заявке. Имя заявителя: "
                "{{ $('Request form').item.json['Имя'] }}. Основная тема: "
                "{{ $('Vocabulary check').item.json.topic }}. Также в заявке упомянуто: "
                "{{ $('Vocabulary check').item.json.extra_topics }}. Пиши по-человечески, "
                "одно-два предложения."
            ),
            "options": {},
        },
    }


def template_notification_node(pos):
    """Кейс 1 «после»: один узел подстановки переменных, без вызова модели."""
    return {
        "id": "notify_template", "name": "Compose notification (template)",
        "type": "n8n-nodes-base.set", "typeVersion": 3.4, "position": pos,
        "parameters": {
            "mode": "manual", "includeOtherFields": True,
            "assignments": {"assignments": [{
                "id": "n1", "name": "notification_text", "type": "string",
                "value": (
                    "=Новая заявка от {{ $('Request form').item.json['Имя'] }}: тема "
                    "«{{ $('Vocabulary check').item.json.topic }}»"
                    "{{ $('Vocabulary check').item.json.extra_topics ? ', также: ' + "
                    "$('Vocabulary check').item.json.extra_topics : '' }}."
                ),
            }]},
            "options": {},
        },
    }


def stage_1_before():
    """Добавляет к стадии 4 С7: LLM-узел уведомления (+ свой Model-узел) → Telegram,
    веткой от `Write row` (параллельно с существующим `Result screen`, не вместо него)."""
    nodes = set_form_path(base_nodes(), "s8-case1-before")
    nodes.append(llm_notification_node([780, -260]))
    nodes.append(openrouter_model_node("notify_model", "Model (notification)", [780, -40]))
    nodes.append(telegram_text_node(
        "tg_notify", "Notify coordinator (Telegram)", [1020, -260],
        "={{ $json.text }}"))
    conn = base_connections()
    conn.setdefault("Write row", {"main": [[]]})
    conn["Write row"]["main"][0].append(
        {"node": "Compose notification (LLM)", "type": "main", "index": 0})
    conn["Compose notification (LLM)"] = {
        "main": [[{"node": "Notify coordinator (Telegram)", "type": "main", "index": 0}]]}
    conn["Model (notification)"] = {"ai_languageModel": [[
        {"node": "Compose notification (LLM)", "type": "ai_languageModel", "index": 0}]]}
    return {"name": "С8 · Кейс 1 (до) — LLM сочиняет уведомление",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def stage_1_after():
    """То же ветвление, но композиция уведомления — шаблоном, не моделью."""
    nodes = set_form_path(base_nodes(), "s8-case1-after")
    nodes.append(template_notification_node([780, -260]))
    nodes.append(telegram_text_node(
        "tg_notify", "Notify coordinator (Telegram)", [1020, -260],
        "={{ $json.notification_text }}"))
    conn = base_connections()
    conn.setdefault("Write row", {"main": [[]]})
    conn["Write row"]["main"][0].append(
        {"node": "Compose notification (template)", "type": "main", "index": 0})
    conn["Compose notification (template)"] = {
        "main": [[{"node": "Notify coordinator (Telegram)", "type": "main", "index": 0}]]}
    return {"name": "С8 · Кейс 1 (после) — шаблон вместо модели",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def dedup_nodes(pos0):
    """Кейс 2: механический фильтр (хэш нормализованного текста) → если не решил
    однозначно → LLM-проверка смысла (+ свой Model-узел).

    **Честное сужение этого прохода (см. README.md «Кейс 2 — что проверено по-честному,
    что упрощено»):** постоянный дизайн кейса — сверка с автоматически найденной
    недавней строкой того же контакта в Data Table. На живом стенде за разумное время
    не удалось подтвердить рабочий набор параметров узла `n8n-nodes-base.dataTable` для
    такого запроса (несколько операций дали `Cannot read properties of undefined` —
    видимо, версия узла на этом стенде ожидает другую форму параметров, не
    подтверждённую в официальной документации на момент проверки). Чтобы не гадать и не
    заявлять непроверенное работающим, сравнение здесь использует ЧЕТВЁРТОЕ поле формы
    `Предыдущее сообщение (тест)` — тестовый ввод для ЭТОЙ проверки, не часть постоянного
    дизайна; реальная автоматическая выборка — открытый пункт для Фазы production."""
    mech_filter = {
        "id": "dedup_hash", "name": "Normalize + hash", "type": "n8n-nodes-base.set",
        "typeVersion": 3.4, "position": pos0,
        "parameters": {
            "mode": "manual", "includeOtherFields": True,
            "assignments": {"assignments": [
                {"id": "d1", "name": "normalized_hash", "type": "string",
                 "value": "={{ $('Request form').item.json['Что нужно']"
                          ".toLowerCase().trim().replace(/\\s+/g, ' ') }}"},
                {"id": "d2", "name": "recent_same_contact_text", "type": "string",
                 "value": "={{ $('Request form').item.json['Предыдущее сообщение (тест)'] "
                          "|| '' }}"},
                {"id": "d3", "name": "recent_same_contact_hash", "type": "string",
                 "value": "={{ ($('Request form').item.json['Предыдущее сообщение (тест)'] "
                          "|| '').toLowerCase().trim().replace(/\\s+/g, ' ') }}"},
            ]},
            "options": {},
        },
    }
    mech_if = {
        "id": "dedup_mech_if", "name": "Exact duplicate in window?",
        "type": "n8n-nodes-base.if", "typeVersion": 2.2,
        "position": [pos0[0] + 220, pos0[1]],
        "parameters": {"conditions": {"options": {"caseSensitive": True, "typeValidation": "strict"},
                        "combinator": "and", "conditions": [{
                            "leftValue": "={{ $json.normalized_hash }}",
                            "rightValue": "={{ $json.recent_same_contact_hash }}",
                            "operator": {"type": "string", "operation": "equals"}}]}},
    }
    llm_dedup = {
        "id": "dedup_llm", "name": "Same question, reworded? (LLM)",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5,
        "position": [pos0[0] + 220, pos0[1] + 160],
        "parameters": {
            "promptType": "define",
            "text": "=Это новое сообщение: «{{ $('Request form').item.json['Что нужно'] }}». "
                    "Недавнее сообщение того же контакта: «{{ $json.recent_same_contact_text }}». "
                    "Это тот же вопрос, просто сформулированный иначе? Ответь строго "
                    "«да» или «нет».",
            "options": {},
        },
    }
    dedup_model = openrouter_model_node(
        "dedup_model", "Model (dedup)", [pos0[0] + 220, pos0[1] + 320])
    return [mech_filter, mech_if, llm_dedup, dedup_model]


def add_test_field(nodes, label, placeholder=""):
    """Добавляет необязательное тестовое поле в форму — только для ручной проверки
    на стенде (см. предупреждение в `dedup_nodes`), не часть формы студента С7."""
    for n in nodes:
        if n["type"] == "n8n-nodes-base.formTrigger":
            n["parameters"]["formFields"]["values"].append(
                {"fieldLabel": label, "placeholder": placeholder, "requiredField": False})
    return nodes


def stage_2():
    """Дедупликация встаёт МЕЖДУ справочником и записью: решение «дубль/новый»
    принимается до того, как строка попадёт в таблицу."""
    nodes = set_form_path(base_nodes(), "s8-case2")
    nodes = add_test_field(nodes, "Предыдущее сообщение (тест)",
                            "для ручной проверки дедупликации на стенде, не часть формы студента")
    nodes.extend(dedup_nodes([300, 160]))
    conn = base_connections()
    # Справочник теперь ведёт в фильтр дублей, а не прямо в запись.
    conn["Vocabulary check"] = {"main": [[
        {"node": "Normalize + hash", "type": "main", "index": 0}]]}
    conn["Normalize + hash"] = {"main": [[
        {"node": "Exact duplicate in window?", "type": "main", "index": 0}]]}
    conn["Exact duplicate in window?"] = {"main": [
        [],  # true — точный повтор, в запись не идём вовсе (обрабатывается отдельно на стенде)
        [{"node": "Same question, reworded? (LLM)", "type": "main", "index": 0}],  # false
    ]}
    conn["Same question, reworded? (LLM)"] = {"main": [[
        {"node": "Write row", "type": "main", "index": 0}]]}
    conn["Model (dedup)"] = {"ai_languageModel": [[
        {"node": "Same question, reworded? (LLM)", "type": "ai_languageModel", "index": 0}]]}
    return {"name": "С8 · Кейс 2 — дедупликация в два уровня",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def refund_base_nodes(path):
    """Общий вход для обоих процессов Кейса 3: форма заявки на возврат плюс
    извлечение суммы. Отдельный, маленький сценарий — не часть основной формы
    учебного центра (сюжет другой: не заявка на занятие, а запрос на возврат)."""
    form = {
        "id": "refund_form", "name": "Refund request", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [-180, 0], "webhookId": path,
        "parameters": {
            "path": path, "formTitle": "Запрос на возврат",
            "formDescription": "Тестовый вход Кейса 3 — не форма студента",
            "formFields": {"values": [
                {"fieldLabel": "Текст запроса", "fieldType": "textarea",
                 "placeholder": "например: прошу вернуть 2500 рублей за пропущенное занятие",
                 "requiredField": True},
            ]},
            "options": {"appendAttribution": False},
        },
    }
    extract_amount = {
        "id": "extract_amount", "name": "Extract amount",
        "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
        "position": [60, 0],
        "parameters": {
            "text": "={{ $json['Текст запроса'] }}",
            "schemaType": "manual",
            "inputSchema": json.dumps({
                "type": "object",
                "properties": {"amount_rub": {
                    "type": "number",
                    "description": "сумма возврата в рублях, указанная в тексте"}},
                "required": ["amount_rub"],
            }, ensure_ascii=False, indent=2),
            "options": {},
        },
    }
    extract_model = openrouter_model_node("extract_model", "Model (extraction)", [60, 220])
    return [form, extract_amount, extract_model]


def stage_3a_model():
    """Процесс (A): решение о пороге принимает модель через OpenRouter (Qwen2.5) —
    правило-порог живёт ТЕКСТОМ в промпте, не в условии."""
    nodes = refund_base_nodes("s8-refund-model")
    decide = {
        "id": "refund_decide_llm", "name": "Decide refund (model)",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5,
        "position": [300, 0],
        "parameters": {
            "promptType": "define",
            "text": f"=Правило: не возвращай больше {REFUND_THRESHOLD} рублей "
                    "автоматически, иначе эскалируй руководителю. Сумма запроса: "
                    "{{ $json.output.amount_rub }} рублей. Ответь строго одним словом: "
                    "«одобрить» или «эскалировать».",
            "options": {},
        },
    }
    decide_model = openrouter_model_node(
        "decide_model", "Model (decision, Qwen2.5)", [300, 220], model=REFUND_MODEL)
    result = {
        "id": "refund_result_a", "name": "Result screen (process A)",
        "type": "n8n-nodes-base.form", "typeVersion": 1, "position": [540, 0],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Решение процесса (A)",
            "completionMessage": "=Сумма: {{ $('Extract amount').item.json.output.amount_rub "
                                  "}} ₽. Решение модели: {{ $json.text }}",
            "options": {"appendAttribution": False},
        },
    }
    nodes += [decide, decide_model, result]
    conn = {
        "Refund request": {"main": [[{"node": "Extract amount", "type": "main", "index": 0}]]},
        "Extract amount": {"main": [[{"node": "Decide refund (model)", "type": "main", "index": 0}]]},
        "Decide refund (model)": {"main": [[{"node": "Result screen (process A)", "type": "main", "index": 0}]]},
        "Model (extraction)": {"ai_languageModel": [[
            {"node": "Extract amount", "type": "ai_languageModel", "index": 0}]]},
        "Model (decision, Qwen2.5)": {"ai_languageModel": [[
            {"node": "Decide refund (model)", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С8 · Кейс 3, процесс (A) — решение принимает модель",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def stage_3b_code():
    """Процесс (B): то же правило — `IF`-узел по той же извлечённой сумме,
    без модели в точке решения."""
    nodes = refund_base_nodes("s8-refund-code")
    decide = {
        "id": "refund_decide_if", "name": "Amount over threshold?",
        "type": "n8n-nodes-base.if", "typeVersion": 2.2, "position": [300, 0],
        "parameters": {"conditions": {
            "options": {"caseSensitive": True, "typeValidation": "strict"},
            "combinator": "and", "conditions": [{
                "leftValue": "={{ $json.output.amount_rub }}",
                "rightValue": REFUND_THRESHOLD,
                "operator": {"type": "number", "operation": "gt"}}]}},
    }
    result_escalate = {
        "id": "refund_result_b_esc", "name": "Result screen (escalate)",
        "type": "n8n-nodes-base.form", "typeVersion": 1, "position": [540, -80],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Решение процесса (B)",
            "completionMessage": "=Сумма: {{ $('Extract amount').item.json.output.amount_rub "
                                  "}} ₽. Решение кода: эскалировать.",
            "options": {"appendAttribution": False},
        },
    }
    result_approve = {
        "id": "refund_result_b_ok", "name": "Result screen (approve)",
        "type": "n8n-nodes-base.form", "typeVersion": 1, "position": [540, 80],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": "Решение процесса (B)",
            "completionMessage": "=Сумма: {{ $('Extract amount').item.json.output.amount_rub "
                                  "}} ₽. Решение кода: одобрить (не выше порога).",
            "options": {"appendAttribution": False},
        },
    }
    nodes += [decide, result_escalate, result_approve]
    conn = {
        "Refund request": {"main": [[{"node": "Extract amount", "type": "main", "index": 0}]]},
        "Extract amount": {"main": [[{"node": "Amount over threshold?", "type": "main", "index": 0}]]},
        "Amount over threshold?": {"main": [
            [{"node": "Result screen (escalate)", "type": "main", "index": 0}],
            [{"node": "Result screen (approve)", "type": "main", "index": 0}],
        ]},
        "Model (extraction)": {"ai_languageModel": [[
            {"node": "Extract amount", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С8 · Кейс 3, процесс (B) — решение принимает код",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def stage_4():
    """Кейс 4: та же ветка уведомления (вариант «после» — шаблон), плюс картинка.

    Картинка приходит узлом `HTTP Request` (публичный сервис-заглушка Picsum) —
    наложение текста на картинку вне n8n (ImageMagick/Pillow, см. README.md) здесь не
    собрано как часть сценария; узел ниже отправляет уже готовый файл. Это и есть
    вводный уровень, заявленный в `ARCHITECTURE.md` §6 (не генерация картинки внутри
    n8n). Эта стадия несёт обычный размер (800×450, через n8n целиком); граница
    10 МБ `sendPhoto`, подтверждённая на этом же стенде, проверена ПРЯМЫМ вызовом
    Telegram Bot API (не через этот workflow — см. README.md, почему)."""
    nodes = set_form_path(base_nodes(), "s8-case4")
    nodes.append(template_notification_node([780, -260]))
    nodes.append({
        "id": "fetch_card_image", "name": "Fetch card image (HTTP)",
        "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
        "position": [1020, -260],
        "parameters": {
            "url": "https://picsum.photos/800/450",
            "options": {"response": {"response": {"responseFormat": "file"}}},
        },
    })
    nodes.append(telegram_photo_node(
        "tg_photo", "Send card (Telegram photo)", [1260, -260],
        "={{ $json.notification_text }}"))
    conn = base_connections()
    conn.setdefault("Write row", {"main": [[]]})
    conn["Write row"]["main"][0].append(
        {"node": "Compose notification (template)", "type": "main", "index": 0})
    conn["Compose notification (template)"] = {"main": [[
        {"node": "Fetch card image (HTTP)", "type": "main", "index": 0}]]}
    conn["Fetch card image (HTTP)"] = {"main": [[
        {"node": "Send card (Telegram photo)", "type": "main", "index": 0}]]}
    return {"name": "С8 · Кейс 4 — картинка в Telegram",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


STAGES = {
    "stage-1-before": stage_1_before, "stage-1-after": stage_1_after,
    "stage-2": stage_2, "stage-3a-model": stage_3a_model,
    "stage-3b-code": stage_3b_code, "stage-4": stage_4,
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
