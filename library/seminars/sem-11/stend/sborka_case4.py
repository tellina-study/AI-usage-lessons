#!/usr/bin/env python3
"""Стенд Семинара 11 (issue #345), Кейс 4 — семантическое размытие поиска на масштабе.

Один сценарий, публикуемый на `https://n8n.lessons.tellian.io` — минимальный, но НАСТОЯЩИЙ
демонстрационный экран скоупинга по домену (`04-semantic-dilution-at-scale.md`, SETKA-KEYSOV.md
Кейс 4, «Решение»):

    Вопрос + объединённый индекс курсов (2 документа: свой курс + протёкший «чужой»)
          → Embed query + оба документа (openai/text-embedding-3-small, та же модель замера)
          → Поиск БЕЗ скоупинга (cosine top-1 по ВСЕМ документам индекса)
          → Поиск СО скоупингом (тот же cosine top-1, но ПЕРЕД ранжированием кандидаты
            отфильтрованы по полю course_id — чужой курс даже не входит в сравнение)
          → Result screen — обе цифры на одном экране

Документы в демо — НЕ выдуманный текст: это РЕАЛЬНАЯ пара из находки собственного замера этого
кейса (`case4-README.md` §«Находка» + `case4-results.json`, anchor_id=anchor-new3,
track=D_adversarial): вопрос «С помощью чего губка переваривает пищу?» (ответ — «с помощью
археоцитов»), свой документ — абзац статьи Википедии о губках с этим ответом, и протёкший
документ `Dc-1063` — ДРУГОЙ абзац ТОЙ ЖЕ статьи (тоже про археоцитов, но без ключевых слов
фильтра «биология»), который в живом замере на N=28 обошёл свой документ (cosine 0,4297 против
0,4178 — gold_cosine/best_rival_cosine из `case4-results.json`, details, anchor-new3,
growth_step=20). Эта живая демонстрация — не повтор всего замера (300 документов на экран не
влезает и не нужно), а минимальный живой прогон ТОЙ ЖЕ пары документов и ТОГО ЖЕ вопроса,
показывающий механику решения (скоупинг), а не пересчитывающий саму находку с нуля.

Usage:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 sborka_case4.py --push
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

EMBED_MODEL = "openai/text-embedding-3-small"


def _cos_js():
    return (
        "function cos(a,b){let d=0,na=0,nb=0;"
        "for(let i=0;i<a.length;i++){d+=a[i]*b[i];na+=a[i]*a[i];nb+=b[i]*b[i];}"
        "return d/(Math.sqrt(na)*Math.sqrt(nb));}\n"
    )


def case4_scoping_workflow():
    webhook_id = "s11-case4-scoping"
    return {
        "name": "С11 · Кейс 4 — скоупинг по домену (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Вопрос + объединённый индекс курсов",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-900, 0], "webhookId": webhook_id,
                "parameters": {
                    "path": webhook_id,
                    "formTitle": "С11 · Кейс 4 — скоупинг по домену (демо)",
                    "formDescription": "JSON: {question, course_id, docs: [{id, text, course_id}]}",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "embed_all", "name": f"Embed query + оба документа ({EMBED_MODEL})",
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
                        f"  model: '{EMBED_MODEL}',\n"
                        "  input: (() => { const p = JSON.parse($json.payload); "
                        "return [p.question, p.docs[0].text, p.docs[1].text]; })()\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "unscoped", "name": "Поиск без скоупинга (весь объединённый индекс)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-340, 0],
                "parameters": {
                    "jsCode": (
                        _cos_js() +
                        "const payload = JSON.parse($('Вопрос + объединённый индекс курсов')"
                        ".first().json.payload);\n"
                        "const resp = $input.first().json;\n"
                        "const qvec = resp.data[0].embedding;\n"
                        "const docs = payload.docs.map((d, i) => ({...d, "
                        "embedding: resp.data[i + 1].embedding}));\n"
                        "const scored = docs.map(d => ({...d, cosine: cos(qvec, d.embedding)}))"
                        ".sort((a, b) => b.cosine - a.cosine);\n"
                        "const top = scored[0];\n"
                        "return [{json: {\n"
                        "  question: payload.question, course_id: payload.course_id, "
                        "docs, qvec,\n"
                        "  unscoped_top_id: top.id, unscoped_top_course: top.course_id, "
                        "unscoped_cosine: Number(top.cosine.toFixed(4)),\n"
                        "  unscoped_n_candidates: docs.length\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "scoped", "name": "Поиск со скоупингом (фильтр course_id перед ранжированием)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-60, 0],
                "parameters": {
                    "jsCode": (
                        _cos_js() +
                        "const d = $input.first().json;\n"
                        "// Единственное отличие от узла «без скоупинга»: фильтр по course_id\n"
                        "// применён ДО ранжирования — чужой курс даже не входит в кандидатов.\n"
                        "const scopedDocs = d.docs.filter(doc => doc.course_id === d.course_id);\n"
                        "const scored = scopedDocs.map(doc => ({...doc, cosine: cos(d.qvec, "
                        "doc.embedding)})).sort((a, b) => b.cosine - a.cosine);\n"
                        "const top = scored[0];\n"
                        "return [{json: {...d, docs: undefined, qvec: undefined,\n"
                        "  scoped_top_id: top.id, scoped_top_course: top.course_id,\n"
                        "  scoped_cosine: Number(top.cosine.toFixed(4)),\n"
                        "  scoped_n_candidates: scopedDocs.length\n"
                        "}}];"
                    ),
                },
            },
            {
                "id": "res", "name": "Result screen — обе цифры рядом",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [220, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Без скоупинга vs со скоупингом",
                    "completionMessage": (
                        "={{ 'Вопрос: ' + $json.question "
                        "+ '\\n\\nБЕЗ скоупинга (' + $json.unscoped_n_candidates + ' кандидата): top-1 = ' "
                        "+ $json.unscoped_top_id + ' (курс ' + $json.unscoped_top_course + '), cosine=' "
                        "+ $json.unscoped_cosine "
                        "+ '\\n\\nСО скоупингом (' + $json.scoped_n_candidates + ' кандидат, курс ' "
                        "+ $json.course_id + '): top-1 = ' + $json.scoped_top_id + ' (курс ' "
                        "+ $json.scoped_top_course + '), cosine=' + $json.scoped_cosine }}"
                    ),
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Вопрос + объединённый индекс курсов": {"main": [[
                {"node": f"Embed query + оба документа ({EMBED_MODEL})", "type": "main", "index": 0}]]},
            f"Embed query + оба документа ({EMBED_MODEL})": {"main": [[
                {"node": "Поиск без скоупинга (весь объединённый индекс)", "type": "main", "index": 0}]]},
            "Поиск без скоупинга (весь объединённый индекс)": {"main": [[
                {"node": "Поиск со скоупингом (фильтр course_id перед ранжированием)",
                 "type": "main", "index": 0}]]},
            "Поиск со скоупингом (фильтр course_id перед ранжированием)": {"main": [[
                {"node": "Result screen — обе цифры рядом", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


WORKFLOWS = {
    "case4-scoping.json": case4_scoping_workflow,
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
