#!/usr/bin/env python3
"""Стенд Семинара 10 (issue #311) — генератор n8n-сценариев.

Три сценария, которые этот файл кладёт на стенд `n8n.lessons.tellian.io`:

1. **«С10 · сырой вызов OpenRouter (универсальный)»** (вебхук `s10-raw-openrouter`) —
   швейцарский нож замера: один `httpRequest`-узел, URL и тело приходят целиком с
   python-стороны (как `sem-09/stend/zamery-k2-kesh/kesh_stend.py`), узел использует
   `authentication: predefinedCredentialType` + `nodeCredentialType: openRouterApi` —
   ключ подставляет n8n на своей стороне из credential `VbxiQn8TbqA4R2mw` ("OpenRouter
   account"), ни один вызов этого файла ключ не читает и не печатает. Этим вебхуком
   прогнаны ВСЕ измерения кейсов 1, 3, 4 (chat completions + embeddings +
   мультимодальные embeddings) — не прямые обращения к OpenRouter мимо стенда (правило
   задачи: без отдельного OPENROUTER_API_KEY измерение идёт через настоящий workflow).

2. **«С10 · Кейс 1 — векторное хранилище (демо-экран)»** (вебхук `s10-case1-vector`) —
   отдельный, "настоящий" экран для показа на слайде: `Simple Vector Store` (in-memory) +
   `Embeddings OpenRouter`-эквивалент (здесь — тот же httpRequest-паттерн, потому что
   штатный embeddings-узел n8n 2.42.7 OpenRouter как провայдера не включает — проверено
   живым вызовом, см. `README.md` §«Открытый технический риск»), RAG-шаг и ответ модели.
   Это и есть ответ на открытый флаг ARCHITECTURE.md §5/§7 п.5 для Кейса 1.

3. **«С10 · Кейс 4 — мультимодальный эмбеддинг (демо-экран)»** (вебхук `s10-case4-mm`) —
   HTTP Request → OpenRouter `/embeddings`, вход — картинка (data URL), настоящий вызов.
   **Модель — `amazon/titan-embed-image-v1`, не `voyage-multimodal-3`**: живой прогон
   (`stend/measure/debug_mm*.py`) показал, что `voyage-multimodal-3` на этом стенде в
   каталоге OpenRouter просто не существует (`"Model ... does not exist"`), а
   `amazon/titan-embed-image-v1` существует, но на реальном разрешении скана (300×450,
   ~20к символов base64) отдаёт БИТОВО ОДИНАКОВЫЙ вектор для любых двух разных картинок —
   рабочий диапазон найден вилкой только у маленьких превью (~64×96, ~6-8к символов), и
   даже там различимость слабая. Подробности и правка плана по факту замера — `README.md`
   §«Открытый технический риск» и `SETKA-KEYSOV.md` Кейс 4.

Usage:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 sborka.py --push
"""
import argparse
import json
import os
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"
OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}


def raw_openrouter_workflow():
    """Сценарий 1 — универсальный сырой вызов OpenRouter (любой endpoint)."""
    webhook_id = "s10-raw-openrouter"
    return {
        "name": "С10 · сырой вызов OpenRouter (универсальный)",
        "nodes": [
            {
                "id": "trig", "name": "Тело запроса",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-180, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С10 · замер — сырое тело запроса",
                    "formDescription": "Служебный стенд измерений, не форма студента",
                    "formFields": {"values": [
                        {"fieldLabel": "URL", "fieldType": "text", "requiredField": True},
                        {"fieldLabel": "Тело", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "http", "name": "OpenRouter raw",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [60, 0],
                "parameters": {
                    "method": "POST",
                    "url": "={{ $json['URL'] }}",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ $json['Тело'] }}",
                    "options": {"response": {"response": {"neverError": True}},
                                "timeout": 180000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "res", "name": "Result",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [300, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Готово", "completionMessage": "ok",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Тело запроса": {"main": [[{"node": "OpenRouter raw", "type": "main", "index": 0}]]},
            "OpenRouter raw": {"main": [[{"node": "Result", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


def case1_vector_workflow():
    """Сценарий 2 — демо-экран Кейса 1: эмбеддинг запроса + поиск по Simple Vector Store
    + ответ модели по найденному куску. Вход — JSON с готовым корпусом (эмбеддинги
    документов считаются заранее офлайн замером, здесь демонстрируется шаг запроса:
    вопрос → эмбеддинг → cosine top-1 среди присланных векторов (Code-узел) → промт
    только с найденным куском → модель."""
    webhook_id = "s10-case1-vector"
    return {
        "name": "С10 · Кейс 1 — векторное хранилище (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Вопрос + корпус с векторами",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-480, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С10 · Кейс 1 — векторный поиск (демо)",
                    "formDescription": "Вопрос + корпус документов с готовыми эмбеддингами (JSON)",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "embed_q", "name": "Embed query (OpenRouter)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-220, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ JSON.stringify({model: JSON.parse($json.payload).model, "
                                 "input: JSON.parse($json.payload).question}) }}",
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "pick", "name": "Simple Vector Store (cosine top-1)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [40, 0],
                "parameters": {
                    "jsCode": (
                        "const payload = JSON.parse($('Вопрос + корпус с векторами').first().json.payload);\n"
                        "const qvec = $input.first().json.data[0].embedding;\n"
                        "function cos(a,b){let d=0,na=0,nb=0;for(let i=0;i<a.length;i++){d+=a[i]*b[i];na+=a[i]*a[i];nb+=b[i]*b[i];}return d/(Math.sqrt(na)*Math.sqrt(nb));}\n"
                        "let best=null,bestScore=-1;\n"
                        "for(const doc of payload.corpus){const s=cos(qvec,doc.embedding);if(s>bestScore){bestScore=s;best=doc;}}\n"
                        "return [{json:{question:payload.question,chunk:best.text,doc_id:best.id,score:bestScore,model:payload.model}}];"
                    ),
                },
            },
            {
                "id": "model", "name": "Model (answer on retrieved chunk)",
                "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
                "position": [300, 120],
                "parameters": {"model": "openai/gpt-4o-mini", "options": {}},
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "answer", "name": "Answer (RAG)",
                "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5,
                "position": [300, 0],
                "parameters": {
                    "promptType": "define",
                    "text": "=Отвечай ТОЛЬКО по тексту ниже. Если ответа нет в тексте — напиши "
                            "«нет информации».\n\nТекст:\n{{ $json.chunk }}\n\nВопрос: {{ $json.question }}",
                },
            },
            {
                "id": "res", "name": "Result screen",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [540, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Ответ", "completionMessage": "={{ $json.text }}",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Вопрос + корпус с векторами": {"main": [[{"node": "Embed query (OpenRouter)", "type": "main", "index": 0}]]},
            "Embed query (OpenRouter)": {"main": [[{"node": "Simple Vector Store (cosine top-1)", "type": "main", "index": 0}]]},
            "Simple Vector Store (cosine top-1)": {"main": [[{"node": "Answer (RAG)", "type": "main", "index": 0}]]},
            "Model (answer on retrieved chunk)": {"ai_languageModel": [[{"node": "Answer (RAG)", "type": "ai_languageModel", "index": 0}]]},
            "Answer (RAG)": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


def case4_multimodal_workflow():
    """Сценарий 3 — демо-экран Кейса 4: мультимодальный эмбеддинг одной картинки."""
    webhook_id = "s10-case4-mm"
    return {
        "name": "С10 · Кейс 4 — мультимодальный эмбеддинг (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Скан бланка (data URL)",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-220, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С10 · Кейс 4 — мультимодальный эмбеддинг (демо)",
                    "formDescription": "JSON-тело: {model, input: [...]}, как ожидает OpenRouter /embeddings",
                    "formFields": {"values": [
                        {"fieldLabel": "body", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "http", "name": "Embed image (amazon/titan-embed-image-v1)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [60, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ $json.body }}",
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "res", "name": "Result screen",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [300, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Готово", "completionMessage": "ok",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Скан бланка (data URL)": {"main": [[{"node": "Embed image (amazon/titan-embed-image-v1)", "type": "main", "index": 0}]]},
            "Embed image (amazon/titan-embed-image-v1)": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


WORKFLOWS = {
    "raw-openrouter.json": raw_openrouter_workflow,
    "case1-vector.json": case1_vector_workflow,
    "case4-multimodal.json": case4_multimodal_workflow,
}


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def push():
    existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=250")["data"]}
    for fname, builder in WORKFLOWS.items():
        wf = builder()
        (HERE / fname).write_text(json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if wf["name"] in existing:
            wid = existing[wf["name"]]
            api("PUT", f"/workflows/{wid}", wf)
            print(f"обновлён: {wid}  {wf['name']}")
        else:
            wid = api("POST", "/workflows", wf)["id"]
            print(f"создан: {wid}  {wf['name']}")
        api("POST", f"/workflows/{wid}/publish", {})
        print("  опубликован")


def write_only():
    for fname, builder in WORKFLOWS.items():
        wf = builder()
        (HERE / fname).write_text(json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"записан {fname}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--push", action="store_true")
    args = p.parse_args()
    if args.push:
        if not API or not KEY:
            raise SystemExit("N8N_API_URL/N8N_API_KEY не заданы — source credentials первым")
        push()
    else:
        write_only()
