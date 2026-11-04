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


def case2_chunking_workflow():
    """Сценарий 4 — демо-экран Кейса 2: четыре версии нарезки документа на РЕАЛЬНОМ
    документе SberQuAD (не придуманном тексте) — тот же документ/вопрос/ответ, что
    `measure/case2_chunking.py` использует в своём sweep (seed=7, CHUNK_SIZE=180),
    только один конкретный пример вместо агрегата по 60 документам. JS внутри
    Code-узлов — прямой порт `chunk_fixed`/`chunk_structural`/`chunk_word_boundary`/
    `chunk_fixed_overlap`/`answer_intact` из `case2_chunking.py`, не самостоятельная
    реализация (не должно расходиться с тем, что реально считалось). v3/v4 добавлены
    2026-11-02 по прямому указанию владельца курса — закрывают открытый пункт прежнего
    замера (перекрытие не проверялось) и дешёвую альтернативу голому счёту символов
    (границы слов)."""
    webhook_id = "s10-case2-chunking"
    js_chunk_fixed = (
        "function chunkFixed(text, size, overlap) {\n"
        "  const chunks = []; let i = 0;\n"
        "  while (i < text.length) {\n"
        "    const end = Math.min(i + size, text.length);\n"
        "    chunks.push({start: i, end: end, text: text.slice(i, end)});\n"
        "    if (end === text.length) break;\n"
        "    i += size - overlap;\n"
        "  }\n"
        "  return chunks;\n"
        "}\n"
    )
    js_chunk_word_boundary = (
        "function chunkWordBoundary(text, size) {\n"
        "  const re = /\\S+/g; let m; const words = [];\n"
        "  while ((m = re.exec(text)) !== null) { words.push({start: m.index, end: m.index + m[0].length, text: m[0]}); }\n"
        "  if (words.length === 0) return [{start: 0, end: text.length, text: text}];\n"
        "  const spans = []; let curStart = words[0].start, curEnd = curStart, curLen = 0;\n"
        "  for (const w of words) {\n"
        "    const added = curLen === 0 ? w.text.length : w.text.length + 1;\n"
        "    if (curLen && curLen + added > size) { spans.push([curStart, curEnd]); curStart = w.start; curLen = w.text.length; }\n"
        "    else { curLen += added; }\n"
        "    curEnd = w.end;\n"
        "  }\n"
        "  spans.push([curStart, curEnd]);\n"
        "  for (let i = 0; i < spans.length - 1; i++) spans[i][1] = spans[i + 1][0];\n"
        "  spans[spans.length - 1][1] = text.length;\n"
        "  return spans.map(([s, e]) => ({start: s, end: e, text: text.slice(s, e)}));\n"
        "}\n"
    )
    js_answer_intact = (
        "function answerIntact(chunks, aStart, aEnd) {\n"
        "  for (const c of chunks) { if (c.start <= aStart && aEnd <= c.end) return true; }\n"
        "  return false;\n"
        "}\n"
    )
    return {
        "name": "С10 · Кейс 2 — нарезка документа (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Документ целиком",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-480, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С10 · Кейс 2 — нарезка документа (демо)",
                    "formDescription": "JSON: {document, question, answer, answer_start, chunk_size}",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "fixed", "name": "Нарезка фиксированным размером",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-220, 0],
                "parameters": {
                    "jsCode": (
                        "const payload = JSON.parse($input.first().json.payload);\n"
                        "const size = payload.chunk_size || 180;\n"
                        + js_chunk_fixed + js_answer_intact +
                        "const chunks = chunkFixed(payload.document, size, 0);\n"
                        "const aStart = payload.answer_start;\n"
                        "const aEnd = aStart + payload.answer.length;\n"
                        "const intact = answerIntact(chunks, aStart, aEnd);\n"
                        "return [{json: {...payload, chunk_size: size, chunks_v1: chunks, v1_intact: intact}}];"
                    ),
                },
            },
            {
                "id": "struct", "name": "Нарезка по границам предложений",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [40, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "function chunkStructural(text, target) {\n"
                        "  const sentences = text.split(/(?<=[.!?])\\s+/);\n"
                        "  const chunks = []; let pos = 0, curStart = 0, curText = '';\n"
                        "  for (const sent of sentences) {\n"
                        "    let idx = text.indexOf(sent, pos); if (idx === -1) idx = pos;\n"
                        "    const sStart = idx, sEnd = idx + sent.length;\n"
                        "    if (curText && (curText.length + sent.length + 1 > target)) {\n"
                        "      chunks.push({start: curStart, end: pos, text: curText});\n"
                        "      curText = sent; curStart = sStart;\n"
                        "    } else {\n"
                        "      if (!curText) curStart = sStart;\n"
                        "      curText = curText ? (curText + ' ' + sent).trim() : sent;\n"
                        "    }\n"
                        "    pos = sEnd;\n"
                        "  }\n"
                        "  if (curText) chunks.push({start: curStart, end: text.length, text: curText});\n"
                        "  return chunks;\n"
                        "}\n"
                        + js_answer_intact +
                        "const chunks = chunkStructural(d.document, d.chunk_size);\n"
                        "const aStart = d.answer_start;\n"
                        "const aEnd = aStart + d.answer.length;\n"
                        "const intact = answerIntact(chunks, aStart, aEnd);\n"
                        "return [{json: {...d, chunks_v2: chunks, v2_intact: intact}}];"
                    ),
                },
            },
            {
                "id": "word", "name": "Нарезка по границам слов",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [300, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        + js_chunk_word_boundary + js_answer_intact +
                        "const chunks = chunkWordBoundary(d.document, d.chunk_size);\n"
                        "const aStart = d.answer_start;\n"
                        "const aEnd = aStart + d.answer.length;\n"
                        "const intact = answerIntact(chunks, aStart, aEnd);\n"
                        "return [{json: {...d, chunks_v3: chunks, v3_intact: intact}}];"
                    ),
                },
            },
            {
                "id": "overlap", "name": "Нарезка фиксированным размером с перекрытием",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [560, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        + js_chunk_fixed + js_answer_intact +
                        "const overlap = Math.round(d.chunk_size * 0.15);\n"
                        "const chunks = chunkFixed(d.document, d.chunk_size, overlap);\n"
                        "const aStart = d.answer_start;\n"
                        "const aEnd = aStart + d.answer.length;\n"
                        "const intact = answerIntact(chunks, aStart, aEnd);\n"
                        "return [{json: {...d, chunks_v4: chunks, v4_intact: intact, overlap_chars_v4: overlap}}];"
                    ),
                },
            },
            {
                "id": "compare", "name": "Сравнение: попал ли ответ целиком в один кусок",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [820, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "function fmt(chunks) {\n"
                        "  return chunks.map((c,i)=>`  [${i}] (${c.start}-${c.end}): \"${c.text.replace(/\\n/g,' ').slice(0,70)}"
                        "${c.text.length>70?'…':''}\"`).join('\\n');\n"
                        "}\n"
                        "function verdict(ok) { return ok ? 'ЦЕЛИКОМ в одном куске' : 'РАЗОРВАН границей куска'; }\n"
                        "const summary = `Документ (${d.document.length} симв.), размер куска = ${d.chunk_size}\\n` +\n"
                        "  `Вопрос: ${d.question}\\n` +\n"
                        "  `Эталонный ответ: \"${d.answer}\" (позиция ${d.answer_start}-${d.answer_start + d.answer.length})\\n\\n` +\n"
                        "  `v1 — фиксированный размер (${d.chunks_v1.length} куска):\\n${fmt(d.chunks_v1)}\\n` +\n"
                        "  `→ ответ ${verdict(d.v1_intact)}\\n\\n` +\n"
                        "  `v2 — по границам предложений (${d.chunks_v2.length} куска):\\n${fmt(d.chunks_v2)}\\n` +\n"
                        "  `→ ответ ${verdict(d.v2_intact)}\\n\\n` +\n"
                        "  `v3 — по границам слов (${d.chunks_v3.length} куска):\\n${fmt(d.chunks_v3)}\\n` +\n"
                        "  `→ ответ ${verdict(d.v3_intact)}\\n\\n` +\n"
                        "  `v4 — фиксированный размер с перекрытием ${d.overlap_chars_v4} симв. (${d.chunks_v4.length} куска):\\n${fmt(d.chunks_v4)}\\n` +\n"
                        "  `→ ответ ${verdict(d.v4_intact)}`;\n"
                        "return [{json: {...d, summary}}];"
                    ),
                },
            },
            {
                "id": "res", "name": "Result screen",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [1080, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Сравнение нарезки", "completionMessage": "={{ $json.summary }}",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Документ целиком": {"main": [[{"node": "Нарезка фиксированным размером", "type": "main", "index": 0}]]},
            "Нарезка фиксированным размером": {"main": [[{"node": "Нарезка по границам предложений", "type": "main", "index": 0}]]},
            "Нарезка по границам предложений": {"main": [[{"node": "Нарезка по границам слов", "type": "main", "index": 0}]]},
            "Нарезка по границам слов": {"main": [[{"node": "Нарезка фиксированным размером с перекрытием", "type": "main", "index": 0}]]},
            "Нарезка фиксированным размером с перекрытием": {"main": [[{"node": "Сравнение: попал ли ответ целиком в один кусок", "type": "main", "index": 0}]]},
            "Сравнение: попал ли ответ целиком в один кусок": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


def case3_search_workflow():
    """Сценарий 5 — демо-экран Кейса 3: keyword overlap → embedding запроса
    (OpenRouter) → cosine-ранжирование → RRF-слияние (гибрид) → LLM-реранкер
    (gpt-4o-mini) поверх top-N кандидатов. Вход — вопрос + малый РЕАЛЬНЫЙ корпус
    (документы SberQuAD из того же пула, что `measure/case3_measure.py`/
    `case3_rerank_measure.py`, включая confusable-пару cluster6-1/cluster6-2) с
    эмбеддингами документов, посчитанными заранее офлайн тем же вебхуком
    `s10-raw-openrouter` (см. `measure/trigger_case3_search.py`) — узел эмбеддинга
    в этом сценарии считает ТОЛЬКО вектор вопроса, как в `case1-vector.json`."""
    webhook_id = "s10-case3-search"
    stopwords = (
        "и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по "
        "только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли "
        "если уже или ни быть был него до вас нибудь опять уж вам сказал ведь там потом "
        "себя ничего ей может они тут где есть надо ней для мы тебя их чем была сам чтоб "
        "без будто чего раз тоже себе под будет ж тогда кто этот того потому этого какой "
        "совсем ним здесь этом один почти мой тем чтобы нее сейчас были куда зачем всех "
        "никогда можно при наконец два об другой хоть после над больше тот через эти нас "
        "про всего них какая много разве три эту моя впрочем хорошо свою этой перед иногда "
        "лучше чуть том нельзя такой им более всегда конечно всю между"
    )
    return {
        "name": "С10 · Кейс 3 — виды поиска + реранкер (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Вопрос + корпус с эмбеддингами",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-900, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С10 · Кейс 3 — виды поиска + реранкер (демо)",
                    "formDescription": "JSON: {question, gold_doc_id, query_embedding_model, corpus: [{id, text, embedding}]}",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "kw", "name": "Keyword overlap",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-620, 0],
                "parameters": {
                    "jsCode": (
                        f"const STOPWORDS = new Set((\"{stopwords}\").split(' '));\n"
                        "function tokenize(text) {\n"
                        "  const m = text.toLowerCase().match(/[а-яёa-z0-9]+/g) || [];\n"
                        "  return m.filter(t => t.length > 2 && !STOPWORDS.has(t));\n"
                        "}\n"
                        "const payload = JSON.parse($input.first().json.payload);\n"
                        "const qTokens = new Set(tokenize(payload.question));\n"
                        "const scored = payload.corpus.map(doc => {\n"
                        "  const dTokens = new Set(tokenize(doc.text));\n"
                        "  let overlap = 0; for (const t of qTokens) if (dTokens.has(t)) overlap++;\n"
                        "  return {id: doc.id, overlap};\n"
                        "});\n"
                        "scored.sort((a,b)=>b.overlap-a.overlap);\n"
                        "const keyword_rank = scored.map(s=>s.id);\n"
                        "return [{json: {...payload, keyword_rank, keyword_scores: scored}}];"
                    ),
                },
            },
            {
                "id": "embed_q", "name": "Embed query (OpenRouter)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-340, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ JSON.stringify({model: $json.query_embedding_model || "
                                 "'openai/text-embedding-3-small', input: $json.question}) }}",
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "cosine", "name": "Cosine ranking (vector)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-60, 0],
                "parameters": {
                    "jsCode": (
                        "const kw = $('Keyword overlap').first().json;\n"
                        "const qvec = $input.first().json.data[0].embedding;\n"
                        "function cos(a,b){let d=0,na=0,nb=0;for(let i=0;i<a.length;i++){"
                        "d+=a[i]*b[i];na+=a[i]*a[i];nb+=b[i]*b[i];}return d/(Math.sqrt(na)*Math.sqrt(nb));}\n"
                        "const scored = kw.corpus.map(doc => ({id: doc.id, score: cos(qvec, doc.embedding)}));\n"
                        "scored.sort((a,b)=>b.score-a.score);\n"
                        "const vector_rank = scored.map(s=>s.id);\n"
                        "return [{json: {...kw, vector_rank, vector_scores: scored}}];"
                    ),
                },
            },
            {
                "id": "rrf", "name": "RRF fusion (hybrid)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [220, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "function rrf(rankA, rankB, k=60) {\n"
                        "  const scores = {};\n"
                        "  [rankA, rankB].forEach(rank => { rank.forEach((id, i) => {\n"
                        "    scores[id] = (scores[id]||0) + 1/(k+i+1); }); });\n"
                        "  return Object.keys(scores).sort((a,b)=>scores[b]-scores[a]);\n"
                        "}\n"
                        "const hybrid_rank = rrf(d.keyword_rank, d.vector_rank, 60);\n"
                        "const TOP_N = Math.min(10, hybrid_rank.length);\n"
                        "const topIds = hybrid_rank.slice(0, TOP_N);\n"
                        "const byId = {}; d.corpus.forEach(c=>byId[c.id]=c.text);\n"
                        "const candidatesText = topIds.map((id,i)=>`${i+1}. ${byId[id]}`).join('\\n\\n');\n"
                        "return [{json: {...d, hybrid_rank, top_ids: topIds, candidates_text: candidatesText}}];"
                    ),
                },
            },
            {
                "id": "rerank", "name": "LLM-реранкер (gpt-4o-mini)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [500, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/chat/completions",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": (
                        "={{ JSON.stringify({model: 'openai/gpt-4o-mini', messages: [\n"
                        "  {role: 'system', content: 'Ты — переранжировщик результатов поиска. Тебе дан "
                        "вопрос и ' + $json.top_ids.length + ' кандидатов-отрывков, пронумерованных 1..' "
                        "+ $json.top_ids.length + '. Переупорядочи номера кандидатов от самого "
                        "релевантного вопросу к наименее релевантному. Ответь СТРОГО JSON-массивом чисел "
                        "— перестановкой всех номеров, без пояснений.'},\n"
                        "  {role: 'user', content: 'Вопрос: ' + $json.question + '\\n\\nКандидаты:\\n' "
                        "+ $json.candidates_text}\n"
                        "]}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 90000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "parse", "name": "Разбор ответа реранкера + итог",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [780, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('RRF fusion (hybrid)').first().json;\n"
                        "const resp = $input.first().json;\n"
                        "let content = null; try { content = resp.choices[0].message.content; } catch(e) {}\n"
                        "let order = null;\n"
                        "if (content) {\n"
                        "  const m = content.match(/\\[[\\d,\\s]+\\]/);\n"
                        "  if (m) { try { const parsed = JSON.parse(m[0]); const n = d.top_ids.length;\n"
                        "    const isPerm = parsed.length===n && new Set(parsed).size===n && "
                        "parsed.every(x=>x>=1&&x<=n);\n"
                        "    if (isPerm) order = parsed; } catch(e) {} }\n"
                        "}\n"
                        "let rerankedIds = d.top_ids; let parseOk = false;\n"
                        "if (order) { rerankedIds = order.map(i => d.top_ids[i-1]); parseOk = true; }\n"
                        "function rankOf(list, id) { const i = list.indexOf(id); return i===-1 ? null : i+1; }\n"
                        "const rHybrid = rankOf(d.hybrid_rank, d.gold_doc_id);\n"
                        "const rReranked = rankOf(rerankedIds, d.gold_doc_id);\n"
                        "const summary = `Вопрос: ${d.question}\\n` +\n"
                        "  `Эталонный документ: ${d.gold_doc_id}\\n\\n` +\n"
                        "  `keyword: ранг эталона = ${rankOf(d.keyword_rank, d.gold_doc_id) ?? 'не найден'} "
                        "(из ${d.keyword_rank.length})\\n` +\n"
                        "  `vector:  ранг эталона = ${rankOf(d.vector_rank, d.gold_doc_id) ?? 'не найден'} "
                        "(из ${d.vector_rank.length})\\n` +\n"
                        "  `hybrid (RRF): ранг эталона = ${rHybrid ?? 'не найден'} (из ${d.hybrid_rank.length})\\n` +\n"
                        "  `hybrid + LLM-реранкер: ранг эталона = ${rReranked ?? ('не входил в top-' + "
                        "d.top_ids.length)} (parse_ok=${parseOk})\\n\\n` +\n"
                        "  `top-${d.top_ids.length} до реранка: ${d.top_ids.join(', ')}\\n` +\n"
                        "  `top-${d.top_ids.length} после реранка: ${rerankedIds.join(', ')}`;\n"
                        "return [{json: {...d, reranked_ids: rerankedIds, parse_ok: parseOk, summary}}];"
                    ),
                },
            },
            {
                "id": "res", "name": "Result screen",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [1040, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Итог поиска", "completionMessage": "={{ $json.summary }}",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Вопрос + корпус с эмбеддингами": {"main": [[{"node": "Keyword overlap", "type": "main", "index": 0}]]},
            "Keyword overlap": {"main": [[{"node": "Embed query (OpenRouter)", "type": "main", "index": 0}]]},
            "Embed query (OpenRouter)": {"main": [[{"node": "Cosine ranking (vector)", "type": "main", "index": 0}]]},
            "Cosine ranking (vector)": {"main": [[{"node": "RRF fusion (hybrid)", "type": "main", "index": 0}]]},
            "RRF fusion (hybrid)": {"main": [[{"node": "LLM-реранкер (gpt-4o-mini)", "type": "main", "index": 0}]]},
            "LLM-реранкер (gpt-4o-mini)": {"main": [[{"node": "Разбор ответа реранкера + итог", "type": "main", "index": 0}]]},
            "Разбор ответа реранкера + итог": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


WORKFLOWS = {
    "raw-openrouter.json": raw_openrouter_workflow,
    "case1-vector.json": case1_vector_workflow,
    "case4-multimodal.json": case4_multimodal_workflow,
    "case2-chunking.json": case2_chunking_workflow,
    "case3-search.json": case3_search_workflow,
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
