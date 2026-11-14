#!/usr/bin/env python3
"""Стенд Семинара 11 (issue #345), Кейс 5 — самокоррекция поиска (CRAG-форма).

Один сценарий, публикуемый на `https://n8n.lessons.tellian.io` — **минимальная CRAG-форма**,
прямой слепок механики реального проекта Dharshiny5 (`05-self-correcting-rag-crag.md` §2):

    Запрос → поиск top-1 по источнику А (keyword, без модели)
          → LLM-грейдер релевантности (CORRECT / AMBIGUOUS / INCORRECT)
          → условная ветка:
               CORRECT    → использовать чанк как есть                   (tag: источник-1)
               AMBIGUOUS  → сигнал «нужна переформулировка» (retry-флаг)   (tag: источник-1, refined)
               INCORRECT  → откат на источник Б (keyword, top-1)          (tag: источник-2)

**Чем это отличается от реального проекта и почему это честно, не подмена.** У Dharshiny5
внешний счётчик повторов (max 2 на подвопрос) живёт в Main Agent Workflow, которая вызывает
Agentic Retrieval Sub-workflow как инструмент. Здесь ровно та же раздельность: этот n8n-сценарий
играет роль retrieval-sub-workflow (один поиск + один грейд + одна ветка за вызов, без
собственного цикла внутри воркфлоу), а роль агента со счётчиком итераций играет python-драйвер
`measure/case5_crag_driver.py` — он вызывает этот webhook повторно при вердикте AMBIGUOUS, с
явным лимитом 2 повторов на вопрос (то же число, что в реальном случае и в официальном примере
LangGraph, §2 брифа). Разделение ответственности («воркфлоу решает ОДИН шаг, агент считает
попытки») не ослабление механики — это тот же паттерн, который реальный проект использует.

Корпус — НЕ выдуманный текст: пять документов SberQuAD из кластера «Сибирь» (cluster3-1..5,
`corpus/corpus_case1_s10.json`, тот же корпус, что Кейсы 1/3 Семинара 10) как источник А, и
четыре документа из кластера «Дилан» (cluster5-1..4) как источник Б — два топически разных,
внутренне связных набора, по аналогии с CONC/SYSC у Dharshiny5 (два разных регуляторных
раздела), без подгонки под желаемый ответ грейдера.

Usage:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 sborka_case5.py --push
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

STOPWORDS = (
    "и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по "
    "только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли "
    "если уже или ни быть был него до вас нибудь опять уж вам сказал ведь там потом "
    "себя ничего ей может они тут где есть надо ней для мы тебя их чем была сам чтоб "
    "без будто чего раз тоже себе под будет ж тогда кто этот того потому этого какой "
    "совсем ним здесь этом один почти мой тем чтобы нее сейчас были куда зачем всех "
    "никогда можно при наконец два об другой хоть после над больше тот через эти нас "
    "про всего них какая много разве три эту моя впрочем хорошо свою этой перед иногда "
    "лучше чуть том нельзя такой им более всегда конечно всю между это этот эта"
)


def _tokenize_js():
    return (
        f"const STOPWORDS = new Set((\"{STOPWORDS}\").split(' '));\n"
        "function tokenize(text) {\n"
        "  const m = (text || '').toLowerCase().match(/[а-яёa-z0-9]+/g) || [];\n"
        "  return m.filter(t => t.length > 2 && !STOPWORDS.has(t));\n"
        "}\n"
        "function keywordTop1(question, docs) {\n"
        "  const qTokens = new Set(tokenize(question));\n"
        "  const scored = docs.map(doc => {\n"
        "    const dTokens = new Set(tokenize(doc.text));\n"
        "    let overlap = 0; for (const t of qTokens) if (dTokens.has(t)) overlap++;\n"
        "    return {id: doc.id, text: doc.text, overlap};\n"
        "  });\n"
        "  scored.sort((a,b) => b.overlap - a.overlap);\n"
        "  return {top: scored[0], all: scored};\n"
        "}\n"
    )


def case5_crag_workflow():
    webhook_id = "s11-case5-crag"
    grader_system_prompt = (
        "Ты — грейдер релевантности для RAG-системы (Corrective RAG). Тебе даны ВОПРОС "
        "пользователя и ОДИН извлечённый фрагмент текста. Оцени: отвечает ли фрагмент ПО "
        "СУЩЕСТВУ на вопрос (не просто касается той же общей темы). Верни СТРОГО JSON без "
        "пояснений вне JSON: {\\\"verdict\\\": \\\"CORRECT\\\"|\\\"AMBIGUOUS\\\"|\\\"INCORRECT\\\", "
        "\\\"reason\\\": \\\"одна короткая фраза\\\"}. CORRECT — фрагмент прямо и по существу "
        "отвечает на вопрос. AMBIGUOUS — фрагмент касается темы вопроса, но не даёт прямого "
        "ответа на заданную формулировку (пересказан другими словами, отвечает лишь частично "
        "или на смежный вопрос). INCORRECT — фрагмент не относится к вопросу по существу, даже "
        "если упоминает похожие слова."
    )
    return {
        "name": "С11 · Кейс 5 — CRAG грейдер + условная ветка (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Вопрос + источники А и Б",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-900, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С11 · Кейс 5 — CRAG (демо)",
                    "formDescription": "JSON: {question, source_a: [{id,text}], source_b: [{id,text}], "
                                        "iteration, reformulated}",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "retrieve_a", "name": "Поиск top-1 в источнике А (keyword)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-620, 0],
                "parameters": {
                    "jsCode": (
                        _tokenize_js() +
                        "const payload = JSON.parse($input.first().json.payload);\n"
                        "const {top} = keywordTop1(payload.question, payload.source_a);\n"
                        "return [{json: {\n"
                        "  question: payload.question,\n"
                        "  source_a: payload.source_a,\n"
                        "  source_b: payload.source_b,\n"
                        "  iteration: payload.iteration || 1,\n"
                        "  reformulated: payload.reformulated || false,\n"
                        "  top_doc_id: top.id, top_doc_text: top.text, top_overlap: top.overlap,\n"
                        "  retrieval_source: 'А'\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "grade", "name": "LLM Relevance Grader (gpt-4o-mini)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-340, 0],
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
                        f"    {{role: 'system', content: \"{grader_system_prompt}\"}},\n"
                        "    {role: 'user', content: 'Вопрос: ' + $json.question + '\\n\\nФрагмент:\\n' "
                        "+ $json.top_doc_text}\n"
                        "  ]\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "parse_grade", "name": "Разбор вердикта грейдера",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-60, 0],
                "parameters": {
                    "jsCode": (
                        "const d = $('Поиск top-1 в источнике А (keyword)').first().json;\n"
                        "const resp = $input.first().json;\n"
                        "let content = null; try { content = resp.choices[0].message.content; } catch(e) {}\n"
                        "let verdict = 'INCORRECT';\n"
                        "let reason = 'не удалось разобрать ответ грейдера — применён безопасный дефолт "
                        "(fail-closed, см. бриф §2)';\n"
                        "if (content) {\n"
                        "  const m = content.match(/\\{[\\s\\S]*\\}/);\n"
                        "  if (m) {\n"
                        "    try {\n"
                        "      const parsed = JSON.parse(m[0]);\n"
                        "      if (['CORRECT','AMBIGUOUS','INCORRECT'].includes(parsed.verdict)) {\n"
                        "        verdict = parsed.verdict; reason = parsed.reason || '';\n"
                        "      }\n"
                        "    } catch(e) {}\n"
                        "  }\n"
                        "}\n"
                        "return [{json: {...d, grader_verdict: verdict, grader_reason: reason, "
                        "grader_raw: content}}];"
                    ),
                },
            },
            {
                "id": "if_correct", "name": "Вердикт = CORRECT?",
                "type": "n8n-nodes-base.if", "typeVersion": 2.2,
                "position": [220, 0],
                "parameters": {
                    "conditions": {
                        "options": {"caseSensitive": True, "typeValidation": "strict"},
                        "combinator": "and",
                        "conditions": [{
                            "leftValue": "={{ $json.grader_verdict }}",
                            "rightValue": "CORRECT",
                            "operator": {"type": "string", "operation": "equals"},
                        }],
                    },
                },
            },
            {
                "id": "if_incorrect", "name": "Вердикт = INCORRECT?",
                "type": "n8n-nodes-base.if", "typeVersion": 2.2,
                "position": [220, 240],
                "parameters": {
                    "conditions": {
                        "options": {"caseSensitive": True, "typeValidation": "strict"},
                        "combinator": "and",
                        "conditions": [{
                            "leftValue": "={{ $json.grader_verdict }}",
                            "rightValue": "INCORRECT",
                            "operator": {"type": "string", "operation": "equals"},
                        }],
                    },
                },
            },
            {
                "id": "branch_correct", "name": "Использовать как есть (источник-1)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [480, -120],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "return [{json: {...d, final_tag: 'источник-1', final_text: d.top_doc_text, "
                        "needs_retry: false}}];"
                    ),
                },
            },
            {
                "id": "branch_incorrect", "name": "Откат на источник Б (keyword, top-1)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [480, 360],
                "parameters": {
                    "jsCode": (
                        _tokenize_js() +
                        "const d = $input.first().json;\n"
                        "const {top} = keywordTop1(d.question, d.source_b);\n"
                        "return [{json: {...d, final_tag: 'источник-2', final_text: top.text, "
                        "fallback_doc_id: top.id, fallback_overlap: top.overlap, needs_retry: false}}];"
                    ),
                },
            },
            {
                "id": "branch_ambiguous", "name": "Переформулировать и повторить (источник-1, refined)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [480, 120],
                "parameters": {
                    "jsCode": (
                        "const d = $input.first().json;\n"
                        "return [{json: {...d, final_tag: 'источник-1, refined', final_text: null, "
                        "needs_retry: true}}];"
                    ),
                },
            },
            {
                "id": "res_correct", "name": "Result screen (CORRECT)",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [740, -120],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "CORRECT — использован как есть",
                    "completionMessage": "={{ $json.final_tag + ': ' + $json.final_text }}",
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "res_ambiguous", "name": "Result screen (AMBIGUOUS)",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [740, 120],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "AMBIGUOUS — нужна переформулировка",
                    "completionMessage": "={{ 'итерация ' + $json.iteration + ': ' + $json.grader_reason }}",
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "res_incorrect", "name": "Result screen (INCORRECT)",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [740, 360],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "INCORRECT — откат на источник Б",
                    "completionMessage": "={{ $json.final_tag + ': ' + $json.final_text }}",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Вопрос + источники А и Б": {"main": [[{"node": "Поиск top-1 в источнике А (keyword)", "type": "main", "index": 0}]]},
            "Поиск top-1 в источнике А (keyword)": {"main": [[{"node": "LLM Relevance Grader (gpt-4o-mini)", "type": "main", "index": 0}]]},
            "LLM Relevance Grader (gpt-4o-mini)": {"main": [[{"node": "Разбор вердикта грейдера", "type": "main", "index": 0}]]},
            "Разбор вердикта грейдера": {"main": [[{"node": "Вердикт = CORRECT?", "type": "main", "index": 0}]]},
            "Вердикт = CORRECT?": {"main": [
                [{"node": "Использовать как есть (источник-1)", "type": "main", "index": 0}],
                [{"node": "Вердикт = INCORRECT?", "type": "main", "index": 0}],
            ]},
            "Вердикт = INCORRECT?": {"main": [
                [{"node": "Откат на источник Б (keyword, top-1)", "type": "main", "index": 0}],
                [{"node": "Переформулировать и повторить (источник-1, refined)", "type": "main", "index": 0}],
            ]},
            "Использовать как есть (источник-1)": {"main": [[{"node": "Result screen (CORRECT)", "type": "main", "index": 0}]]},
            "Откат на источник Б (keyword, top-1)": {"main": [[{"node": "Result screen (INCORRECT)", "type": "main", "index": 0}]]},
            "Переформулировать и повторить (источник-1, refined)": {"main": [[{"node": "Result screen (AMBIGUOUS)", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


WORKFLOWS = {
    "case5-crag.json": case5_crag_workflow,
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
