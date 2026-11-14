#!/usr/bin/env python3
"""Стенд Семинара 11 (issue #345), Кейс 2 — продвинутый чанкинг. Слой 2 (n8n-демо-экран),
который `case2-README.md` (Фаза 2) честно назвал несобранным — эта сессия (Фаза 4,
слайды) собирает его.

Один сценарий, публикуемый на `https://n8n.lessons.tellian.io`, с ДВУМЯ механизмами,
которых не было в сценарии Семинара 10 (`s10-case2-chunking`, только 4 версии плоской
резки по счёту символов/слов/предложений с перекрытием):

    Документ + вопрос
      → «Нарезка иерархическая: дети + родитель»          (код, без модели)
      → «Эмбеддинг вопроса и детей» (text-embedding-3-small, реальный HTTP-вызов)
      → «Поиск top-1 ребёнка (cosine)»                     (код, без модели)
      → «Подстановка родителя»                             (код, без модели — сам приём
                                                              «единица поиска ≠ единица ответа»)
      → «Ответ модели по родителю» (gpt-4o-mini, реальный HTTP-вызов)
      → «Разбор ответа» → экран результата

    (параллельная ветка от триггера, тот же документ)
    Документ + вопрос
      → «Нарезка семантическая: предложения»                (код, без модели)
      → «Эмбеддинг предложений» (text-embedding-3-small, реальный HTTP-вызов)
      → «Разрыв смысла и порог (gap_threshold)»              (код, без модели)
      → экран результата: семантические куски

Реальный пример на входе (не выдуманный) — документ 31 той же 60-документной выборки
SberQuAD (seed=7), что `measure/case2_s11_measure.py` использовал для чисел главы и
результата: «Метромост — мост, по которому проходит линия метрополитена...», вопрос
«Что такое метромост?», эталон «мост, по которому проходит линия метрополитена.».
На ЭТОМ самом вопросе реальный прогон корпуса (`case2-results.json` → `details`, doc_idx=31)
дал: v1 (резка по предложениям, target=180, поиск по всем 60 документам) нашла верный
документ, но top-1 КУСОК — «В некоторых случаях применяют совмещённый метромост.»
(символы 169–221), не содержащий ответ → модель ответила «нет информации.» (неверно);
v2 (этот сценарий) — top-1 РЕБЁНОК (target=90) — первое предложение документа (символы
0–59, уже содержит ответ), а подстановка родителя гарантирует это НЕЗАВИСИМО от того,
какой ребёнок найден → модель отвечает «Метромост — это мост, по которому проходит линия
метрополитена.» (верно). Этот сценарий воспроизводит ЖИВЫМ вызовом то же v2-поведение на
том же документе и вопросе — не копирует текст ответа, а вызывает ту же модель заново.

Usage:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 sborka_case2.py --push
    python3 sborka_case2.py --run    # прогнать webhook на реальном документе/вопросе
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

# Реальный документ 31 выборки (measure/case2_s11_measure.py, seed=7) и реальный вопрос,
# на котором этот самый механизм (v2) исправил ошибку v1 в прогоне, давшем числа главы.
DEMO_DOCUMENT = (
    "Метромост — мост, по которому проходит линия метрополитена. Этот мост отличается "
    "от обычного повышенной прочностью, так как поезда метро создают очень сильную "
    "вибрацию. В некоторых случаях применяют совмещённый метромост. Часто такой мост "
    "двухъярусный, — на верхнем ярусе располагается автомобильная или железная дорога, "
    "а на нижнем — линия метро (яркий пример — Нижегородский метромост). Но встречаются "
    "и одноярусные совмещённые метромосты, на которых пути лини метро проложены или "
    "вдоль краёв проезжей части автодороги или, наоборот, в середине моста, а проезжие "
    "части автодороги, соответственно, слева и справа от линии метро (например, "
    "Нагатинский метромост). Также есть станции метрополитена, расположенные на "
    "метромостах, например, Воробьёвы горы в Москве или Аметьево в Казани. На сентябрь "
    "2013 года самый длинный метромост в мире эксплуатируется в городе Новосибирске "
    "между станциями Речной вокзал и Студенческая ."
)
DEMO_QUESTION = "Что такое метромост?"
DEMO_REFERENCE_ANSWER = "мост, по которому проходит линия метрополитена."


def _chunk_structural_js():
    return (
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
    )


def _split_sentences_js():
    return (
        "function splitSentencesWithSpans(text) {\n"
        "  const sentences = text.split(/(?<=[.!?])\\s+/);\n"
        "  const out = []; let pos = 0;\n"
        "  for (const sent of sentences) {\n"
        "    if (!sent.trim()) continue;\n"
        "    let idx = text.indexOf(sent, pos); if (idx === -1) idx = pos;\n"
        "    const sStart = idx, sEnd = idx + sent.length;\n"
        "    out.push({start: sStart, end: sEnd, text: sent});\n"
        "    pos = sEnd;\n"
        "  }\n"
        "  return out;\n"
        "}\n"
    )


def _cosine_js():
    return (
        "function cosine(a, b) {\n"
        "  let dot = 0, na = 0, nb = 0;\n"
        "  for (let i = 0; i < a.length; i++) { dot += a[i]*b[i]; na += a[i]*a[i]; nb += b[i]*b[i]; }\n"
        "  return dot / (Math.sqrt(na) * Math.sqrt(nb));\n"
        "}\n"
    )


def case2_hierarchical_semantic_workflow():
    webhook_id = "s11-case2-chunking"
    return {
        "name": "С11 · Кейс 2 — иерархическая и семантическая нарезка (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Документ + вопрос",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-1180, 180], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С11 · Кейс 2 — продвинутый чанкинг (демо)",
                    "formDescription": "JSON: {document, question, chunk_size_child, gap_threshold}",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            # --- ветка 1: иерархическая/parent-document ------------------------------
            {
                "id": "hier_split", "name": "Нарезка иерархическая: дети + родитель",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-900, 0],
                "parameters": {
                    "jsCode": (
                        "const payload = JSON.parse($input.first().json.payload);\n"
                        + _chunk_structural_js() +
                        "const childSize = payload.chunk_size_child || 90;\n"
                        "const children = chunkStructural(payload.document, childSize);\n"
                        "return [{json: {\n"
                        "  question: payload.question,\n"
                        "  parent_text: payload.document,\n"
                        "  children: children,\n"
                        "  child_size: childSize\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "embed_children", "name": "Эмбеддинг вопроса и детей (text-embedding-3-small)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-620, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": (
                        "={{ JSON.stringify({\n"
                        "  model: 'openai/text-embedding-3-small',\n"
                        "  input: [$json.question, ...$json.children.map(c => c.text)]\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "search_child", "name": "Поиск top-1 ребёнка (cosine)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-340, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('Нарезка иерархическая: дети + родитель').first().json;\n"
                        "const resp = $input.first().json;\n"
                        + _cosine_js() +
                        "const vecs = resp.data.map(x => x.embedding);\n"
                        "const qVec = vecs[0];\n"
                        "const childVecs = vecs.slice(1);\n"
                        "let bestIdx = 0, bestSim = -1;\n"
                        "childVecs.forEach((v, i) => { const s = cosine(qVec, v); if (s > bestSim) { bestSim = s; bestIdx = i; } });\n"
                        "return [{json: {\n"
                        "  question: d.question,\n"
                        "  parent_text: d.parent_text,\n"
                        "  top1_child: d.children[bestIdx],\n"
                        "  top1_child_similarity: bestSim,\n"
                        "  n_children: d.children.length\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "substitute_parent", "name": "Подстановка родителя",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-60, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "// единица поиска (top1_child) и единица ответа (parent_text) — не один и тот же объект;\n"
                        "// модель получает ВЕСЬ документ, не найденный мелкий кусочек.\n"
                        "return [{json: {\n"
                        "  question: d.question,\n"
                        "  found_child_text: d.top1_child.text,\n"
                        "  found_child_similarity: d.top1_child_similarity,\n"
                        "  context_for_answer: d.parent_text\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "answer_llm", "name": "Ответ модели по родителю (gpt-4o-mini)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [220, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/chat/completions",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": (
                        "={{ JSON.stringify({\n"
                        "  model: 'openai/gpt-4o-mini',\n"
                        "  temperature: 0,\n"
                        "  messages: [\n"
                        "    {role: 'system', content: 'Отвечай ТОЛЬКО по тексту ниже, коротко (1 предложение). "
                        "Если ответа нет в тексте — напиши «нет информации».'},\n"
                        "    {role: 'user', content: 'Текст:\\n' + $json.context_for_answer + "
                        "'\\n\\nВопрос: ' + $json.question}\n"
                        "  ]\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "parse_answer", "name": "Разбор ответа",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [500, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('Подстановка родителя').first().json;\n"
                        "const resp = $input.first().json;\n"
                        "let content = null; try { content = resp.choices[0].message.content; } catch(e) {}\n"
                        "return [{json: {\n"
                        "  question: d.question,\n"
                        "  found_child_text: d.found_child_text,\n"
                        "  model_answer: content\n"
                        "}}];"
                    ),
                },
            },
            # --- такт 2 (та же цепочка, последовательно, не параллельная ветка — у n8n
            # form-completion webhook только ОДИН слот ответа, вторая параллельная
            # completion-нода на том же триггере оставляет execution в "waiting"
            # навсегда, это проверено живым прогоном и записано в mcp-limitations) ---
            {
                "id": "sem_split", "name": "Нарезка семантическая: предложения",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [780, 0],
                "parameters": {
                    "jsCode": (
                        "const hier = $input.first().json;\n"
                        "const payload = JSON.parse($('Документ + вопрос').first().json.payload);\n"
                        + _split_sentences_js() +
                        "const sentences = splitSentencesWithSpans(payload.document);\n"
                        "return [{json: {\n"
                        "  question: hier.question,\n"
                        "  found_child_text: hier.found_child_text,\n"
                        "  model_answer: hier.model_answer,\n"
                        "  gap_threshold: (payload.gap_threshold !== undefined) ? payload.gap_threshold : 0.15,\n"
                        "  sentences: sentences\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "embed_sentences", "name": "Эмбеддинг предложений (text-embedding-3-small)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [1060, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": (
                        "={{ JSON.stringify({\n"
                        "  model: 'openai/text-embedding-3-small',\n"
                        "  input: $json.sentences.map(s => s.text)\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "gap_cut", "name": "Разрыв смысла и порог (gap_threshold)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [1340, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('Нарезка семантическая: предложения').first().json;\n"
                        "const resp = $input.first().json;\n"
                        + _cosine_js() +
                        "const vecs = resp.data.map(x => x.embedding);\n"
                        "const sentences = d.sentences;\n"
                        "const threshold = d.gap_threshold;\n"
                        "const gaps = [];\n"
                        "for (let i = 0; i < vecs.length - 1; i++) { gaps.push(1 - cosine(vecs[i], vecs[i+1])); }\n"
                        "const chunks = []; let curStart = sentences[0].start, curEnd = sentences[0].end, curN = 1;\n"
                        "for (let i = 0; i < sentences.length - 1; i++) {\n"
                        "  const gap = gaps[i];\n"
                        "  if (gap > threshold) {\n"
                        "    chunks.push({start: curStart, end: curEnd, n_sentences: curN, cut_after_gap: gap});\n"
                        "    curStart = sentences[i+1].start; curEnd = sentences[i+1].end; curN = 1;\n"
                        "  } else {\n"
                        "    curEnd = sentences[i+1].end; curN += 1;\n"
                        "  }\n"
                        "}\n"
                        "chunks.push({start: curStart, end: curEnd, n_sentences: curN, cut_after_gap: null});\n"
                        "return [{json: {\n"
                        "  question: d.question,\n"
                        "  found_child_text: d.found_child_text,\n"
                        "  model_answer: d.model_answer,\n"
                        "  gap_threshold: threshold,\n"
                        "  n_sentences: sentences.length,\n"
                        "  gaps: gaps.map(g => Math.round(g * 10000) / 10000),\n"
                        "  n_chunks: chunks.length,\n"
                        "  chunks: chunks\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "res_final", "name": "Результат",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [1620, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Иерархическая резка + семантическая резка — один прогон",
                    "completionMessage": (
                        "={{ 'Иерархическая резка — найденный ребёнок: ' + $json.found_child_text + '\\n'"
                        " + 'Ответ модели (контекст — весь родительский документ): ' + $json.model_answer + '\\n\\n'"
                        " + 'Семантическая резка — порог gap_threshold=' + $json.gap_threshold + ': '"
                        " + $json.n_sentences + ' предложений -> ' + $json.n_chunks + ' куска(ов)\\n'"
                        " + 'Разрывы между предложениями: ' + JSON.stringify($json.gaps) }}"
                    ),
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Документ + вопрос": {"main": [[
                {"node": "Нарезка иерархическая: дети + родитель", "type": "main", "index": 0}]]},
            "Нарезка иерархическая: дети + родитель": {"main": [[
                {"node": "Эмбеддинг вопроса и детей (text-embedding-3-small)", "type": "main", "index": 0}]]},
            "Эмбеддинг вопроса и детей (text-embedding-3-small)": {"main": [[
                {"node": "Поиск top-1 ребёнка (cosine)", "type": "main", "index": 0}]]},
            "Поиск top-1 ребёнка (cosine)": {"main": [[
                {"node": "Подстановка родителя", "type": "main", "index": 0}]]},
            "Подстановка родителя": {"main": [[
                {"node": "Ответ модели по родителю (gpt-4o-mini)", "type": "main", "index": 0}]]},
            "Ответ модели по родителю (gpt-4o-mini)": {"main": [[
                {"node": "Разбор ответа", "type": "main", "index": 0}]]},
            "Разбор ответа": {"main": [[
                {"node": "Нарезка семантическая: предложения", "type": "main", "index": 0}]]},
            "Нарезка семантическая: предложения": {"main": [[
                {"node": "Эмбеддинг предложений (text-embedding-3-small)", "type": "main", "index": 0}]]},
            "Эмбеддинг предложений (text-embedding-3-small)": {"main": [[
                {"node": "Разрыв смысла и порог (gap_threshold)", "type": "main", "index": 0}]]},
            "Разрыв смысла и порог (gap_threshold)": {"main": [[
                {"node": "Результат", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


WORKFLOWS = {
    "case2-chunking-hier-semantic.json": case2_hierarchical_semantic_workflow,
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


def run_demo():
    """Прогнать webhook на реальном документе 31 / вопросе — тот же документ и вопрос,
    на которых реальный прогон корпуса (case2-results.json, doc_idx=31) дал v1=неверно,
    v2=верно. Печатает formWaitingUrl execution id для получения результата через API."""
    import urllib.parse
    payload = {
        "document": DEMO_DOCUMENT,
        "question": DEMO_QUESTION,
        "chunk_size_child": 90,
        # p90 корпуса (случай "v3a — щадящий порог" из измерения, case2-results.json ->
        # method.semantic_threshold_percentiles.v3a_p90) — тот же порог, на котором
        # построен главный разбор главы, не произвольное число для демо.
        "gap_threshold": 0.8677755857817189,
    }
    boundary = "----s11case2boundary"
    body = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"field-0\"\r\n\r\n"
        f"{json.dumps(payload, ensure_ascii=False)}\r\n--{boundary}--\r\n"
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{HOST}/form/s11-case2-chunking", data=body, method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        out = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--push", action="store_true")
    p.add_argument("--run", action="store_true")
    args = p.parse_args()
    if args.push:
        if not API or not KEY:
            raise SystemExit("N8N_API_URL/N8N_API_KEY не заданы — source credentials первым")
        push()
    elif args.run:
        run_demo()
    else:
        write_only()
