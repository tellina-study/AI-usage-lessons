#!/usr/bin/env python3
"""Семинар 11 (issue #345), Кейс 1 — трансформация запроса перед поиском. Демо-экран HyDE.

Собирает на живом `https://n8n.lessons.tellian.io` МИНИМАЛЬНЫЙ реальный workflow,
показывающий механику Кейса 1, которой у Фазы 2 (`stend/README.md` §«Что осталось
открытым») не было живого скрина канваса: один дополнительный HTTP Request-узел ПЕРЕД
эмбеддингом запроса, который просит модель сочинить гипотетический ответ (HyDE), —
прямое расширение уже снятой на Семинаре 10 схемы Кейса 1 (`sem-10/stend/sborka.py::
case1_vector_workflow`, тот же узел «Simple Vector Store (cosine top-1)», тот же узел
«Answer (RAG)»-паттерн), с ОДНИМ добавленным шагом в начале:

    Форма (вопрос + корпус с эмбеддингами)
      -> HTTP Request: «Сочинить гипотетический ответ (gpt-4o-mini)»   [НОВЫЙ узел]
      -> Code: «Разбор HyDE-документа»                                  [НОВЫЙ узел]
      -> HTTP Request: «Embed HyDE-документ (text-embedding-3-small)»   [эмбеддинг — но
         теперь эмбеддится HyDE-абзац, не вопрос]
      -> Code: «Simple Vector Store (cosine top-1 по HyDE)»             [тот же код, что
         s10, другой входной вектор]
      -> HTTP Request: «Answer (RAG) по найденному куску (gpt-4o-mini)»
      -> Result screen

Почему HyDE, не multi-query, для ЭТОГО живого скрина. Рецепт главы (`rework/section-1-
transformatsiya-zaprosa.md`, «Решение», слой 2) описывает ОДИН дополнительный узел перед
эмбеддингом — «переформулировки ИЛИ, для HyDE, один связный абзац-ответ» — и называет оба
варианта равноправными примерами того же механического слота. HyDE — линейный (один
абзац, один эмбеддинг, один поиск); multi-query требует фан-аут на 3 ветки эмбеддинга и
слияние RRF, что на канвасе n8n означало бы либо три параллельные явные ветки (вчетверо
больше узлов, менее читаемый скрин на слайде), либо цикл по элементам (неочевиден на
статичном скрине). Собственный Python-замер (`measure/case1_query_transform_measure.py`,
`raw/case1-results.json`) уже покрывает multi-query числом на всех 50 вопросах; этот живой
скрин — честная иллюстрация МЕХАНИЗМА ДОБАВЛЕНИЯ ШАГА (слот «ИИ-обработка перед поиском»),
а не повтор замера.

Вопрос и корпус — РЕАЛЬНЫЕ данные, не придуманные. Вопрос — `c3q10` из основного замера
(«Какие наиболее популярные произведения были созданы на протяжении 1984-1986 гг», класс
exact_match), тот самый, что `rework/section-1-transformatsiya-zaprosa.md` называет
иллюстрацией того, как HyDE ИСПРАВЛЯЕТ baseline (ранг верного документа 2 -> 1). Корпус —
подмножество (10 документов) того самого 500-документного корпуса SberQuAD
(`corpus/corpus_case1_s10.json`): верный документ `cluster6-2`, его confusable-сосед
`cluster6-1` (тот же кластер, другая тема — звездолёты) и 8 реальных дистракторов того же
корпуса. Это ДЕМО-ПРОГОН на меньшем, чем у основного замера, корпусе (10 документов, не
500) — тот же честный приём, что `sem-10/slides/n16-k1-n8n-ekran.md` уже использовал для
демо-экрана Кейса 1 того занятия: показывает механику живого холста, не повторяет число
основного замера.

Запуск:
    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-11/stend
    python3 sborka_case1_hyde.py --push --trigger
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE / "measure"))
from harness_call import call_raw, post_form, get_execution  # noqa: E402

API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"
OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}
WEBHOOK_ID = "s11-case1-hyde"

HYDE_PROMPT_HEAD = (
    "Представь, что ты пишешь короткий (2-3 предложения) энциклопедический фрагмент текста, "
    "который мог бы содержать ответ на следующий вопрос — связный абзац в стиле статьи, "
    "а не прямой ответ одним словом. Если точных деталей не знаешь — всё равно сочини "
    "правдоподобный по стилю фрагмент (это гипотетический документ для поиска, не факт). "
    "Ответь ТОЛЬКО текстом фрагмента, без пояснений.\\n\\nВопрос: "
)


def case1_hyde_workflow():
    return {
        "name": "С11 · Кейс 1 — HyDE перед поиском (демо-экран)",
        "nodes": [
            {
                "id": "trig", "name": "Вопрос + корпус с векторами",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-900, 0], "webhookId": WEBHOOK_ID,
                "parameters": {
                    "path": WEBHOOK_ID,
                    "formTitle": "С11 · Кейс 1 — HyDE (демо)",
                    "formDescription": "JSON: {question, corpus: [{id, text, embedding}]}",
                    "formFields": {"values": [
                        {"fieldLabel": "payload", "fieldType": "textarea", "requiredField": True},
                    ]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "hyde_gen", "name": "Сочинить гипотетический ответ (gpt-4o-mini)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-620, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/chat/completions",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": (
                        "={{ JSON.stringify({\n"
                        "  model: 'openai/gpt-4o-mini',\n"
                        "  messages: [{role: 'user', content: "
                        f"'{HYDE_PROMPT_HEAD}'" + " + JSON.parse($json.payload).question }]\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "parse_hyde", "name": "Разбор HyDE-документа",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [-340, 0],
                "parameters": {
                    "jsCode": (
                        "const payload = JSON.parse($('Вопрос + корпус с векторами').first().json.payload);\n"
                        "const resp = $input.first().json;\n"
                        "let hyde_text = null;\n"
                        "try { hyde_text = resp.choices[0].message.content; } catch (e) {}\n"
                        "return [{json: {question: payload.question, corpus: payload.corpus, hyde_text}}];"
                    ),
                },
            },
            {
                "id": "embed_hyde", "name": "Embed HyDE-документ (text-embedding-3-small)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [-60, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/embeddings",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": "={{ JSON.stringify({model: 'openai/text-embedding-3-small', "
                                 "input: $json.hyde_text}) }}",
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "vec_search", "name": "Simple Vector Store (cosine top-1 по HyDE)",
                "type": "n8n-nodes-base.code", "typeVersion": 2,
                "position": [220, 0],
                "parameters": {
                    "jsCode": (
                        "const prev = $('Разбор HyDE-документа').first().json;\n"
                        "const qvec = $input.first().json.data[0].embedding;\n"
                        "function cos(a, b) {\n"
                        "  let d = 0, na = 0, nb = 0;\n"
                        "  for (let i = 0; i < a.length; i++) { d += a[i]*b[i]; na += a[i]*a[i]; nb += b[i]*b[i]; }\n"
                        "  return d / (Math.sqrt(na) * Math.sqrt(nb));\n"
                        "}\n"
                        "let best = null, bestScore = -1;\n"
                        "for (const doc of prev.corpus) {\n"
                        "  const s = cos(qvec, doc.embedding);\n"
                        "  if (s > bestScore) { bestScore = s; best = doc; }\n"
                        "}\n"
                        "return [{json: {question: prev.question, hyde_text: prev.hyde_text, "
                        "chunk: best.text, doc_id: best.id, score: bestScore}}];"
                    ),
                },
            },
            {
                "id": "answer", "name": "Answer (RAG) по найденному куску (gpt-4o-mini)",
                "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                "position": [480, 0],
                "parameters": {
                    "method": "POST",
                    "url": "https://openrouter.ai/api/v1/chat/completions",
                    "authentication": "predefinedCredentialType",
                    "nodeCredentialType": "openRouterApi",
                    "sendBody": True, "specifyBody": "json",
                    "jsonBody": (
                        "={{ JSON.stringify({\n"
                        "  model: 'openai/gpt-4o-mini',\n"
                        "  messages: [{role: 'user', content: "
                        "'Отвечай ТОЛЬКО по тексту ниже. Если ответа нет в тексте — напиши "
                        "«нет информации».\\n\\nТекст:\\n' + $json.chunk + '\\n\\nВопрос: ' + $json.question}]\n"
                        "}) }}"
                    ),
                    "options": {"response": {"response": {"neverError": True}}, "timeout": 60000},
                },
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "res", "name": "Result screen",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [740, 0],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Ответ (HyDE)",
                    "completionMessage": (
                        "={{ 'HyDE-документ: ' + $('Simple Vector Store (cosine top-1 по HyDE)').first()"
                        ".json.hyde_text + '\\n\\nНайден документ: ' + "
                        "$('Simple Vector Store (cosine top-1 по HyDE)').first().json.doc_id + "
                        "' (score ' + $('Simple Vector Store (cosine top-1 по HyDE)').first().json.score"
                        ".toFixed(3) + ')\\n\\nОтвет: ' + $json.choices[0].message.content }}"
                    ),
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Вопрос + корпус с векторами": {"main": [[{"node": "Сочинить гипотетический ответ (gpt-4o-mini)", "type": "main", "index": 0}]]},
            "Сочинить гипотетический ответ (gpt-4o-mini)": {"main": [[{"node": "Разбор HyDE-документа", "type": "main", "index": 0}]]},
            "Разбор HyDE-документа": {"main": [[{"node": "Embed HyDE-документ (text-embedding-3-small)", "type": "main", "index": 0}]]},
            "Embed HyDE-документ (text-embedding-3-small)": {"main": [[{"node": "Simple Vector Store (cosine top-1 по HyDE)", "type": "main", "index": 0}]]},
            "Simple Vector Store (cosine top-1 по HyDE)": {"main": [[{"node": "Answer (RAG) по найденному куску (gpt-4o-mini)", "type": "main", "index": 0}]]},
            "Answer (RAG) по найденному куску (gpt-4o-mini)": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
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
    wf = case1_hyde_workflow()
    (HERE / "case1-hyde.json").write_text(json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if wf["name"] in existing:
        wid = existing[wf["name"]]
        api("PUT", f"/workflows/{wid}", wf)
        print(f"обновлён: {wid}  {wf['name']}")
    else:
        wid = api("POST", "/workflows", wf)["id"]
        print(f"создан: {wid}  {wf['name']}")
    api("POST", f"/workflows/{wid}/publish", {})
    print("  опубликован")
    return wid


def build_demo_corpus():
    corpus_data = json.load(open(HERE / "corpus" / "corpus_case1_s10.json"))
    corpus = {d["id"]: d["text"] for d in corpus_data["corpus_500"]}
    ids = ["cluster6-2", "cluster6-1", "distractor-374", "distractor-62", "distractor-3",
           "distractor-266", "distractor-403", "distractor-392", "distractor-67", "distractor-152"]
    texts = [corpus[i] for i in ids]
    body = {"model": "openai/text-embedding-3-small", "input": texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=120)
    resp = r["response"] or {}
    vecs = [d["embedding"] for d in resp["data"]]
    return [{"id": i, "text": t, "embedding": v} for i, t, v in zip(ids, texts, vecs)]


def trigger():
    print("Строю демо-корпус (10 документов, реальный эмбеддинг text-embedding-3-small)...")
    corpus = build_demo_corpus()
    question = "Какие наиболее популярные произведения были созданы на протяжении 1984-1986 гг"
    payload = {"question": question, "corpus": corpus}
    resp = post_form(WEBHOOK_ID, [json.dumps(payload, ensure_ascii=False)])
    waiting = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
    print("exec_id", exec_id)
    time.sleep(6)
    ex = get_execution(exec_id)
    run = ex.get("data", {}).get("resultData", {}).get("runData", {})
    print("status:", ex.get("status"), "nodes:", list(run.keys()))
    for name in ["Simple Vector Store (cosine top-1 по HyDE)", "Result screen"]:
        if name in run:
            try:
                print(name, "->", json.dumps(run[name][0]["data"]["main"][0][0]["json"], ensure_ascii=False)[:1200])
            except Exception as e:
                print(name, "err", e)
    json.dump(ex, open(HERE / "case1-hyde-execution.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("сохранено: case1-hyde-execution.json")
    return exec_id


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--push", action="store_true")
    p.add_argument("--trigger", action="store_true")
    args = p.parse_args()
    if not args.push and not args.trigger:
        case1_hyde_workflow()
        print("write-only: используй --push и/или --trigger")
    if args.push:
        if not API or not KEY:
            raise SystemExit("N8N_API_URL/N8N_API_KEY не заданы — source credentials первым")
        push()
    if args.trigger:
        trigger()
