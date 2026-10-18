#!/usr/bin/env python3
"""Собрать стадии Семинара 8 — ДОСТРОЙКА `student.json` Семинара 7, не замена.

**Статус на 2026-10-18: НЕ ВЫЛОЖЕНО И НЕ ПРОГНАНО.** Этот генератор написан по образцу
`sem-07/stend/sborka.py` (та же форма узлов, та же функция `api()`, тот же флаг `--push`),
но ни один из шести файлов ниже не был создан на живом стенде и ни один узел не был
запущен настоящим прогоном. Причина — блокер, зафиксированный в
`../SETKA-KEYSOV-S8.md` «Состояние стенда»: `N8N_API_KEY` для `https://n8n.lessons.tellian.io`
нигде в среде этой сессии не присутствует (единственный найденный документ,
`attachments/*n8n-lab-agent-handover.md`, — незаполненный шаблон, который сам говорит:
«Nothing in workain/infra can mint the API key for you»). Запуск этого файла БЕЗ `--push`
безопасен и детерминирован (не ходит в сеть, только пишет json рядом); запуск С `--push`
упадёт на первом вызове `api()` с 401, как и прямая проверка `curl` в этой же сессии.

    python3 sborka.py              только записать json-файлы рядом (сделано в этой сессии)
    source ~/.n8n-lab.env && python3 sborka.py --push     выложить и опубликовать (НЕ сделано)

## Шесть файлов — по кейсам занятия, каждый ДОСТРАИВАЕТ стадию 4 Семинара 7

    stage-1-before.json   Кейс 1 «до»: отдельный LLM-узел сочиняет текст Telegram-уведомления
    stage-1-after.json    Кейс 1 «после»: узел подстановки переменных (шаблон) вместо модели
    stage-2.json          Кейс 2: дедупликация — механический фильтр, затем LLM на спорное
    stage-3a-model.json   Кейс 3, процесс (A): решение о возврате принимает модель (Ollama)
    stage-3b-code.json    Кейс 3, процесс (B): решение принимает `IF`-узел по сумме
    stage-4.json          Кейс 4: та же цепочка уведомления, плюс картинка в Telegram

Все шесть читают структуру существующих узлов из `sem-07/stend/student.json` (форма →
извлечение → справочник → таблица → экран) и ТОЛЬКО ДОБАВЛЯЮТ узлы — ни один узел С7 не
переименован и не удалён, в точности как того требует шов из `ARCHITECTURE.md` §2.

## Credential-узлы — ссылки, не секреты, и в этой сессии ПУСТЫЕ ссылки

Telegram-узлы ниже несут `credentials: {telegramApi: {id: "", name: "Telegram account (С8)"}}`
— пустой `id`, потому что credential на стенде никогда не создавался (это тоже требует
`N8N_API_KEY` или логина в UI). Настоящий токен бота, который дал оркестратор для этой
сессии, НЕ записан ни в этот файл, ни в какой-либо другой файл репозитория — он был
использован РОВНО ОДИН РАЗ, напрямую через Telegram Bot API (`getMe`, `getUpdates`), чтобы
проверить, что бот жив, и результат этой проверки — в `README.md` рядом. Это не нарушает
правило `PODNYAT-N8N.md` про credential-тип `Telegram`: правило о том, что токен не должен
оказаться в ПАРАМЕТРАХ узла или в URL внутри сценария, который потом живёт в репозитории
или уходит студенту, — именно это не произошло ни разу.

Узел модели Ollama (Кейс 3, процесс A) несёт `credentials: {ollamaApi: {id: "", name:
"Ollama account (локально, без ключа)"}}` по той же причине — Ollama не поднят в этой
сессии (см. README.md), credential создавать было не на чём.
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
# ГЕНЕРАТОРА; реальный стенд (когда будет собран) должен держать то же число и в промпте
# процесса (A), и в условии `IF`-узла процесса (B) — ровно нюанс №2 Кейса 3 в
# `SETKA-KEYSOV-S8.md`: порог не должен жить в двух местах, которые надеются совпасть.
REFUND_THRESHOLD = 3000  # рублей — «мелкий» возврат одобряется процессом без эскалации
TG_CRED = {"telegramApi": {"id": "", "name": "Telegram account (С8, не создан на стенде)"}}
OLLAMA_CRED = {"ollamaApi": {"id": "", "name": "Ollama account (локально, не поднят)"}}


def base_nodes():
    """Шесть узлов стадии 4 С7, скопированные как есть (копия, не ссылка — каждая
    функция ниже достраивает СВОЮ копию, не делит объекты между стадиями)."""
    return json.loads(json.dumps(STUDENT["nodes"]))


def base_connections():
    return json.loads(json.dumps(STUDENT["connections"]))


def telegram_text_node(node_id, name, pos, text_expr):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.telegram",
        "typeVersion": 1.2, "position": pos,
        "parameters": {
            "operation": "sendMessage",
            "chatId": "={{ $json.coordinator_chat_id }}",
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
            "chatId": "={{ $json.coordinator_chat_id }}",
            "binaryData": True,
            "additionalFields": {"caption": caption_expr},
        },
        "credentials": TG_CRED,
    }


def llm_notification_node(pos):
    """Кейс 1 «до»: отдельная цепочка модели сочиняет текст «по-человечески».

    Это и есть узел, который на стенде нужно прогнать несколько раз подряд на
    РАЗНЫХ заявках и сохранить хотя бы один реальный пример расхождения (деталь,
    которой не было в заявке) — см. README.md «Чего здесь не хватает»."""
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
    """Добавляет к стадии 4 С7: LLM-узел уведомления → Telegram, веткой от
    `Write row` (параллельно с существующим `Result screen`, не вместо него)."""
    nodes = base_nodes()
    nodes.append(llm_notification_node([780, -260]))
    nodes.append(telegram_text_node(
        "tg_notify", "Notify coordinator (Telegram)", [1020, -260],
        "={{ $json.text }}"))
    conn = base_connections()
    conn.setdefault("Write row", {"main": [[]]})
    conn["Write row"]["main"][0].append(
        {"node": "Compose notification (LLM)", "type": "main", "index": 0})
    conn["Compose notification (LLM)"] = {
        "main": [[{"node": "Notify coordinator (Telegram)", "type": "main", "index": 0}]]}
    return {"name": "С8 · Кейс 1 (до) — LLM сочиняет уведомление",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def stage_1_after():
    """То же ветвление, но композиция уведомления — шаблоном, не моделью."""
    nodes = base_nodes()
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
    """Кейс 2: механический фильтр (хэш нормализованного текста + контакт в
    окне времени) → если не решил однозначно → LLM-проверка смысла.

    Механическая часть — выражением, без отдельного узла кода (курс избегает
    кода, см. `ARCHITECTURE.md` С7 §7): нормализация и сравнение со свежими
    строками той же таблицы делается в `Set`, сравнение — в `IF`."""
    mech_filter = {
        "id": "dedup_hash", "name": "Normalize + hash", "type": "n8n-nodes-base.set",
        "typeVersion": 3.4, "position": pos0,
        "parameters": {
            "mode": "manual", "includeOtherFields": True,
            "assignments": {"assignments": [{
                "id": "d1", "name": "normalized_hash", "type": "string",
                "value": "={{ $('Request form').item.json['Что нужно']"
                         ".toLowerCase().trim().replace(/\\s+/g, ' ') }}",
            }]},
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
    return [mech_filter, mech_if, llm_dedup]


def stage_2():
    """Дедупликация встаёт МЕЖДУ справочником и записью: решение «дубль/новый»
    принимается до того, как строка попадёт в таблицу."""
    nodes = base_nodes()
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
    extract_model = {
        "id": "extract_model", "name": "Model (extraction)",
        "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
        "position": [60, 220],
        "parameters": {"model": "openai/gpt-4o-mini", "options": {}},
        "credentials": {"openRouterApi": {"id": "", "name": "OpenRouter account (как в С7)"}},
    }
    return [form, extract_amount, extract_model]


def stage_3a_model():
    """Процесс (A): решение о пороге принимает модель через Ollama — правило-порог
    живёт ТЕКСТОМ в промпте, не в условии."""
    nodes = refund_base_nodes("s8-refund-model")
    decide = {
        "id": "refund_decide_llm", "name": "Decide refund (Ollama)",
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
    ollama_model = {
        "id": "ollama_model", "name": "Model (Ollama, Qwen2.5)",
        "type": "@n8n/n8n-nodes-langchain.lmChatOllama", "typeVersion": 1,
        "position": [300, 220],
        "parameters": {"model": "qwen2.5:7b-instruct", "options": {}},
        "credentials": OLLAMA_CRED,
    }
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
    nodes += [decide, ollama_model, result]
    conn = {
        "Refund request": {"main": [[{"node": "Extract amount", "type": "main", "index": 0}]]},
        "Extract amount": {"main": [[{"node": "Decide refund (Ollama)", "type": "main", "index": 0}]]},
        "Decide refund (Ollama)": {"main": [[{"node": "Result screen (process A)", "type": "main", "index": 0}]]},
        "Model (extraction)": {"ai_languageModel": [[
            {"node": "Extract amount", "type": "ai_languageModel", "index": 0}]]},
        "Model (Ollama, Qwen2.5)": {"ai_languageModel": [[
            {"node": "Decide refund (Ollama)", "type": "ai_languageModel", "index": 0}]]},
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

    Наложение текста на картинку — вне n8n (ImageMagick/Pillow, см. README.md),
    картинка попадает в сценарий как бинарные данные через отдельный вызов, узел
    ниже только отправляет уже готовый файл — это и есть вводный уровень,
    заявленный в `ARCHITECTURE.md` §6 (не генерация картинки внутри n8n)."""
    nodes = base_nodes()
    nodes.append(template_notification_node([780, -260]))
    nodes.append({
        "id": "fetch_card_image", "name": "Read card image (binary)",
        "type": "n8n-nodes-base.readWriteFile", "typeVersion": 1,
        "position": [1020, -260],
        "parameters": {"operation": "read", "fileSelector": "/tmp/s8-case4-card.png"},
    })
    nodes.append(telegram_photo_node(
        "tg_photo", "Send card (Telegram photo)", [1260, -260],
        "={{ $json.notification_text }}"))
    conn = base_connections()
    conn.setdefault("Write row", {"main": [[]]})
    conn["Write row"]["main"][0].append(
        {"node": "Compose notification (template)", "type": "main", "index": 0})
    conn["Compose notification (template)"] = {"main": [[
        {"node": "Read card image (binary)", "type": "main", "index": 0}]]}
    conn["Read card image (binary)"] = {"main": [[
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
        print(f"  {fname}.json — {len(wf['nodes'])} узлов (НЕ прогнано)")
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
