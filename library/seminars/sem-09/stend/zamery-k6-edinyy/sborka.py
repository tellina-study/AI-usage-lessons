#!/usr/bin/env python3
"""Собрать стенд «единый вызов» для Задания З3 (Кейс 6, Семинар 9) — issue #299.

Владелец курса (расшифровка комментариев С9, 49:11–50:39): «если у тебя не осиар, не
классическая модель распознавания, а мультимодальная — тогда шаг непонятен, надо
объединять... надо прогнать тесты на едином, общем вызове». Шаг чтения на стенде —
мультимодальная модель (`qwen/qwen3-vl-8b-instruct`, тот же `VISION_MODEL`, что
`../zamery-k5-k6/sborka.py`), не классический OCR — см. README этой папки, раздел
«Расхождения с декой». Этот файл собирает ОДИН сценарий: в единственном HTTP-вызове к
модели уходят СРАЗУ фотография квитанции И текст заявки клиента (с суммой, которую клиент
указал сам), модель читает фотографию и возвращает одновременно: прочитанную сумму,
прочитанную дату, прочитанную из заявки сумму и вердикт «совпало / не совпало».

Сравнивается с существующим «двухшаговым» устройством `../zamery-k5-k6/sborka.py` (функция
`k6_read`, сценарий `s9-m6-read`): там шаг 1 — та же модель читает ТОЛЬКО фотографию, шаг
2 — код (не модель) сравнивает прочитанное число с суммой из заявки. Здесь оба действия —
чтение и сверка — модель делает за один вызов.

Три узла, зеркально устройству `k6_read` (чтобы расхождение числ объяснялось именно
слитием шагов, а не другой механикой вызова):

    1. Webhook (`s9-m6-edinyy`) — принимает `image_base64` (уже закодированное
       прогонщиком, та же механика, что `k6_read`, см. README `../zamery-k5-k6/README.md`
       § «Методическое упрощение»), `mime_type`, `receipt_id`, и — НОВОЕ относительно
       `k6_read` — уже полностью собранный Python-стороной `prompt_text` (весь текст
       инструкции модели, включая вставленную в заявку сумму). N8N здесь не интерполирует
       число в текст сам: текст приходит готовым, узел только подставляет его в тело
       HTTP-запроса. Так проще держать текст промта идентичным тому, что проверяет
       `proverka_protechki.py`, и не плодить два разных места, где могла бы отличаться
       подстановка.
    2. Build vision request (`set`) — то же самое, что в `k6_read`: модель + data_url
       (`data:<mime>;base64,<...>`) + текст из тела запроса.
    3. HTTP Request к `POST https://openrouter.ai/api/v1/chat/completions` — прямой вызов
       (не узел `OpenRouter Chat Model`, который не отдаёт `usage`, см.
       `notes/mcp-limitations.md` [#303-1]), `response_format: json_object`,
       `temperature: 0.2` — СОВПАДАЕТ со значением в `k6_read` (не 0): задание просило
       «температура 0, как в существующем замере», но прямое чтение `../zamery-k5-k6/
       sborka.py` (функция `k6_read`, узел `k6_http`, поле `temperature`) показывает 0.2,
       не 0 — расхождение между тем, что написано в задании, и тем, что реально стоит в
       коде базового замера. Для честного «один вызов против двух» важнее совпадение с
       РЕАЛЬНЫМ бейзлайном, чем с пересказом задания; расхождение зафиксировано в README
       этой папки отдельно.

## Ключи и зона

    python3 sborka.py                                      только записать json рядом
    N8N_API_URL=... N8N_API_KEY=... python3 sborka.py --push   выложить и опубликовать

`OpenRouter account` (`VbxiQn8TbqA4R2mw`) — тот же credential, что везде на стенде С9,
без новой инфраструктуры.
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

# Тот же приём, что `../zamery-k5-k6/sborka.py`: импорт по пути под отдельным именем
# модуля — обычный `import sborka` коллизирует через `sys.modules['sborka']`, потому что
# и `stend/sborka.py`, и `stend/zamery-k5-k6/sborka.py` называются одинаково.
_spec = importlib.util.spec_from_file_location(
    "sem09_sborka_edinyy", str((STEND / "sborka.py").resolve()))
s9 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(s9)

OPENROUTER_CRED = s9.OPENROUTER_CRED
VISION_MODEL = "qwen/qwen3-vl-8b-instruct"  # тот же VISION_MODEL, что ../zamery-k5-k6 —
# сравнение «1 вызов против 2» обязано идти на одной и той же модели, иначе это сравнение
# моделей, а не устройств вызова.


def k6_edinyy():
    path = "s9-m6-edinyy"
    nodes = [{
        "id": "k6e_webhook", "name": "Receipt + claim", "type": "n8n-nodes-base.webhook",
        "typeVersion": 2, "position": [-180, 0],
        "webhookId": path,
        "parameters": {
            "httpMethod": "POST", "path": path, "responseMode": "lastNode",
            "options": {},
        },
    }]
    nodes.append({
        "id": "k6e_build_body", "name": "Build vision request", "type": "n8n-nodes-base.set",
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
                {"id": "b4", "name": "text", "type": "string",
                 "value": "={{ $json.body.prompt_text }}"},
            ]},
            "options": {},
        },
    })
    nodes.append({
        "id": "k6e_http", "name": "Read + sverka (OpenRouter vision, единый вызов)",
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
                "      { type: 'text', text: $json.text },\n"
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
        "Receipt + claim": {"main": [[{"node": "Build vision request", "type": "main", "index": 0}]]},
        "Build vision request": {"main": [[
            {"node": "Read + sverka (OpenRouter vision, единый вызов)", "type": "main", "index": 0}]]},
    }
    return {"name": "С9 · замер K6 — единый вызов (чтение+сверка)",
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


def main():
    push = "--push" in sys.argv
    existing = {}
    if push:
        existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
    wf = k6_edinyy()
    (HERE / "k6-edinyy.json").write_text(
        json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  k6-edinyy.json — {len(wf['nodes'])} узлов")
    if not push:
        return
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
