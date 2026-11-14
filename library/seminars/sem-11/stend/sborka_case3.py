#!/usr/bin/env python3
"""Стенд Семинара 11 (issue #345), Кейс 3 — классификация вопроса (jev-1.13) →
динамический вес RRF-гибрида. Демо-экран для слайдов Фазы 4 (n41-n60).

Единственный новый сценарий этого кейса на канвасе — то, что раздел главы
(`rework/section-3-klassifikatsiya-dinamicheskiy-rrf.md`, «Решение», Слой 2) честно
называет отсутствующим на момент Фазы 2: «отдельного канваса с новым named-узлом
"Classify query (jev)" на стенде не появилось... узел с таким же успехом можно именовать
и вынести отдельно на будущем слайде». Это и есть тот будущий слайд — узел назван,
вынесен отдельно, и ниже видна вся цепочка от вопроса до результата.

Цепочка узлов (линейная, одна последовательная ветка — тот же стиль, что Кейс 3 С10):

    Вопрос + корпус кандидатов (form trigger, один текстовый payload)
      -> Keyword overlap (ранжирование по словам)          — код, без модели
      -> Embed query (text-embedding-3-small)               — настоящий HTTP-вызов
      -> Cosine ranking (вектор)                             — код, без модели
      -> Классификация вопроса (jev-1.13)                   — настоящий HTTP-вызов,
         OpenRouter /api/alpha/decisions (см. measure/case3_jev_classify.py)
      -> Вес по классификации (0.75 / 0.25)                  — код, без модели
      -> RRF fusion: фиксированный вес (0.5)                 — код, без модели (рецепт С10)
      -> RRF fusion: динамический вес (jev)                  — код, без модели
      -> Result screen                                       — сравнение фикс./динам.

Корпус кандидатов (10 реальных документов SberQuAD, настоящие эмбеддинги) и оба
демо-вопроса (c3q17, c3q42) — `raw/case3-n8n-demo-payloads.json`
(`measure/case3_build_demo.py`). Реюз инфраструктуры: тот же credential OpenRouter
(`VbxiQn8TbqA4R2mw`), что С7-С10 и Кейс 5 этого занятия (`sborka_case5.py`).

Usage:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 sborka_case3.py --push
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

# Тот же список стоп-слов, что `measure/case3_build_demo.py::STOPWORDS` (python) — буквально
# тот же набор, чтобы keyword_rank_live, посчитанный на холсте, совпадал с offline-вычислением
# (замерено 2026-11-14: более короткий/другой список стоп-слов даёт другой keyword_rank —
# демо показывало бы иную, не ту самую, цепочку, что при подготовке payload).
TOKENIZE_JS = (
    "const STOPWORDS = new Set((\"а без будет будто бы был была было быть в вам вас вдруг ведь во "
    "вот все вы где да даже для до его ее ей ему если есть еще ж же за и из или их к как какой "
    "когда кто ли меня мне может мы на надо не него ней нет ни нибудь ничего но ну о он она они "
    "опять от по под потом потому раз с сам себе себя сказал со так там тебя теперь то тогда того "
    "тоже только тут ты у уж уже чего чем что чтоб этого этот я\").split(' '));\n"
    "function tokenize(text) {\n"
    "  const m = (text || '').toLowerCase().match(/[а-яёa-z0-9]+/g) || [];\n"
    "  return m.filter(t => t.length > 2 && !STOPWORDS.has(t));\n"
    "}\n"
)


def case3_dynamic_rrf_workflow():
    webhook_id = "s11-case3-dynamic-rrf"
    return {
        "name": "С11 · Кейс 3 — классификация (jev) → динамический вес RRF (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Вопрос + корпус кандидатов",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-1400, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С11 · Кейс 3 — классификация → динамический вес RRF (демо)",
                    "formDescription": "JSON: {qid, question, gold_doc_id, docs:[{id,text,embedding}], "
                                        "keyword_rank, vector_rank} — см. raw/case3-n8n-demo-payloads.json",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "kw_overlap", "name": "Keyword overlap (ранжирование по словам)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-1120, 0],
                "parameters": {
                    "jsCode": (
                        TOKENIZE_JS +
                        "const payload = JSON.parse($input.first().json.payload);\n"
                        "const qTokens = new Set(tokenize(payload.question));\n"
                        "const scored = payload.docs.map(d => {\n"
                        "  const dTokens = new Set(tokenize(d.text));\n"
                        "  let overlap = 0; for (const t of qTokens) if (dTokens.has(t)) overlap++;\n"
                        "  return {id: d.id, overlap};\n"
                        "});\n"
                        "scored.sort((a,b) => b.overlap - a.overlap);\n"
                        "return [{json: {...payload, keyword_rank_live: scored.map(s => s.id)}}];"
                    ),
                },
            },
            {
                "id": "embed_query", "name": "Embed query (text-embedding-3-small)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-840, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ JSON.stringify({model: 'openai/text-embedding-3-small', "
                                 "input: [$json.question]}) }}",
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "cosine_rank", "name": "Cosine ranking (вектор)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-560, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('Keyword overlap (ранжирование по словам)').first().json;\n"
                        "const qvec = $input.first().json.data[0].embedding;\n"
                        "function cosine(a, b) {\n"
                        "  let dot=0, na=0, nb=0;\n"
                        "  for (let i=0;i<a.length;i++) { dot += a[i]*b[i]; na += a[i]*a[i]; nb += b[i]*b[i]; }\n"
                        "  return (na && nb) ? dot/(Math.sqrt(na)*Math.sqrt(nb)) : 0;\n"
                        "}\n"
                        "const scored = d.docs.map(doc => ({id: doc.id, sim: cosine(qvec, doc.embedding)}));\n"
                        "scored.sort((a,b) => b.sim - a.sim);\n"
                        "return [{json: {...d, vector_rank_live: scored.map(s => s.id)}}];"
                    ),
                },
            },
            {
                # Тело запроса классификации собирается здесь, не инлайн-выражением на
                # httpRequest-узле: длинный JSON-литерал с кириллицей внутри `={{ }}`
                # на этом стенде ломает n8n-парсер выражений ("ExpressionError: invalid
                # syntax", замерено 2026-11-14) — обход записан в notes/mcp-limitations.md.
                "id": "classify_body", "name": "Собрать тело запроса классификации",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-280, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "const body = {\n"
                        "  model: 'typesafe/jev-1.13',\n"
                        "  state: d.question,\n"
                        "  questions: {type: {type: 'choice',\n"
                        "    instructions: 'Классифицируй вопрос по типу.',\n"
                        "    criteria: {\n"
                        "      exact_fact: 'Вопрос про точный факт — число, имя, дата, код, термин, "
                        "который либо буквально встречается в тексте документа, либо однозначно "
                        "идентифицирует искомую сущность по точному названию/идентификатору.',\n"
                        "      semantic: 'Смысловой вопрос — требует понимания смысла или пересказа "
                        "своими словами, не содержит точного термина/числа/имени из искомого "
                        "документа, которое можно было бы просто найти совпадением слов.',\n"
                        "    }}},\n"
                        "};\n"
                        "return [{json: {...d, jev_request_body: JSON.stringify(body)}}];"
                    ),
                },
            },
            {
                "id": "classify", "name": "Классификация вопроса (jev-1.13)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-0, -240],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/alpha/decisions",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ $json.jev_request_body }}",
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "weight", "name": "Вес по классификации (0.75 / 0.25)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [0, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('Cosine ranking (вектор)').first().json;\n"
                        "const jev = $input.first().json;\n"
                        "const ans = (jev.answers || {}).type || {};\n"
                        "const choice = ans.choice;\n"
                        "const confidence = ans.confidence;\n"
                        "const w_keyword = choice === 'exact_fact' ? 0.75 : (choice === 'semantic' ? 0.25 : 0.5);\n"
                        "return [{json: {...d, jev_choice: choice, jev_confidence: confidence, "
                        "jev_cost: (jev.usage || {}).cost, w_keyword}}];"
                    ),
                },
            },
            {
                "id": "rrf_fixed", "name": "RRF fusion: фиксированный вес (0.5)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [280, -120],
                "parameters": {
                    "jsCode": (
                        "function rrf(rankA, rankB, w, k=60) {\n"
                        "  const scores = {};\n"
                        "  rankA.forEach((id,i) => scores[id] = (scores[id]||0) + w * (1/(k+i+1)));\n"
                        "  rankB.forEach((id,i) => scores[id] = (scores[id]||0) + (1-w) * (1/(k+i+1)));\n"
                        "  return Object.keys(scores).sort((a,b) => scores[b]-scores[a]);\n"
                        "}\n"
                        "const d = $input.first().json;\n"
                        "const fixed_top3 = rrf(d.keyword_rank_live, d.vector_rank_live, 0.5).slice(0,3);\n"
                        "return [{json: {...d, fixed_top3}}];"
                    ),
                },
            },
            {
                "id": "rrf_dynamic", "name": "RRF fusion: динамический вес (jev)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [280, 120],
                "parameters": {
                    "jsCode": (
                        "function rrf(rankA, rankB, w, k=60) {\n"
                        "  const scores = {};\n"
                        "  rankA.forEach((id,i) => scores[id] = (scores[id]||0) + w * (1/(k+i+1)));\n"
                        "  rankB.forEach((id,i) => scores[id] = (scores[id]||0) + (1-w) * (1/(k+i+1)));\n"
                        "  return Object.keys(scores).sort((a,b) => scores[b]-scores[a]);\n"
                        "}\n"
                        "const d = $('RRF fusion: фиксированный вес (0.5)').first().json;\n"
                        "const dynamic_top3 = rrf(d.keyword_rank_live, d.vector_rank_live, d.w_keyword).slice(0,3);\n"
                        "const verdict = dynamic_top3[0] === d.fixed_top3[0] ? "
                        "'динамический вес не изменил топ-1' : "
                        "'динамический вес ПОДВИНУЛ топ-1 (' + d.fixed_top3[0] + ' -> ' + dynamic_top3[0] + ')'" + ";\n"
                        "return [{json: {...d, dynamic_top3, verdict, "
                        "top1_changed: dynamic_top3[0] !== d.fixed_top3[0], "
                        "gold_in_dynamic_top1: dynamic_top3[0] === d.gold_doc_id}}];"
                    ),
                },
            },
            {
                "id": "result", "name": "Result screen",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [600, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Фиксированный вес vs динамический вес",
                    "completionMessage": (
                        "={{ 'Вопрос: ' + $json.question + '\\n' +"
                        " 'jev: ' + $json.jev_choice + ' (confidence ' + $json.jev_confidence + ')' + '\\n' +"
                        " 'вес keyword использован: ' + $json.w_keyword + '\\n' +"
                        " 'gold: ' + $json.gold_doc_id + '\\n' +"
                        " 'фикс. топ-3: ' + $json.fixed_top3.join(', ') + '\\n' +"
                        " 'динам. топ-3: ' + $json.dynamic_top3.join(', ') + '\\n' +"
                        " $json.verdict }}"
                    ),
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Вопрос + корпус кандидатов": {"main": [[{"node": "Keyword overlap (ранжирование по словам)", "type": "main", "index": 0}]]},
            "Keyword overlap (ранжирование по словам)": {"main": [[{"node": "Embed query (text-embedding-3-small)", "type": "main", "index": 0}]]},
            "Embed query (text-embedding-3-small)": {"main": [[{"node": "Cosine ranking (вектор)", "type": "main", "index": 0}]]},
            "Cosine ranking (вектор)": {"main": [[{"node": "Собрать тело запроса классификации", "type": "main", "index": 0}]]},
            "Собрать тело запроса классификации": {"main": [[{"node": "Классификация вопроса (jev-1.13)", "type": "main", "index": 0}]]},
            "Классификация вопроса (jev-1.13)": {"main": [[{"node": "Вес по классификации (0.75 / 0.25)", "type": "main", "index": 0}]]},
            "Вес по классификации (0.75 / 0.25)": {"main": [[{"node": "RRF fusion: фиксированный вес (0.5)", "type": "main", "index": 0}]]},
            "RRF fusion: фиксированный вес (0.5)": {"main": [[{"node": "RRF fusion: динамический вес (jev)", "type": "main", "index": 0}]]},
            "RRF fusion: динамический вес (jev)": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


WORKFLOWS = {
    "case3-dynamic-rrf.json": case3_dynamic_rrf_workflow,
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
