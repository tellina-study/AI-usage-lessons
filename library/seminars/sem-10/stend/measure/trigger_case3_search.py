"""Прогоняет демо-сценарий «С10 · Кейс 3 — виды поиска + реранкер (демо-экран)»
(`sborka.py::case3_search_workflow`, id `xAFFyyTJLYzZSvk8`) на РЕАЛЬНОМ, небольшом
подмножестве корпуса Кейса 1/3 (`corpus/corpus_case1.json`, 500 документов SberQuAD) —
не придуманных текстах. Вопрос и gold-документ — реальная пара `c3q10` из
`corpus/case3_questions.json` (используется в самом замере `case3_rerank_measure.py`,
где hybrid_rerank поднимает её на 1-е место): «Какие наиболее популярные произведения
были созданы на протяжении 1984-1986 гг», gold = `cluster6-2`.

Корпус демо-прогона — 8 документов: сама confusable-пара `cluster6-1`/`cluster6-2`
(обе делят редкую сущность «Звёздный» — одна про звездолёты, другая про песню
«Звёздный сюжет», ровно та путаница, из-за которой пара заведена в разметку корпуса),
плюс 6 реальных дистракторов из того же пула. Эмбеддинги документов считаются здесь
заранее (как в `case1-vector.json`), одним вызовом через `s10-raw-openrouter`
(`harness2.embed_batch`) — узел «Embed query (OpenRouter)» в самом сценарии считает
только вектор вопроса, механика эта не новая.

Числа этого прогона — ИЛЛЮСТРАЦИЯ механики на маленьком корпусе (8 документов), не
повтор измерения на 500 документах: `SETKA-KEYSOV.md`/`README.md` числа Кейса 3
(`raw/case3-results.json`, `raw/case3-rerank-results.json`) этим не трогаются и не
пересчитываются.
"""
import json
import time
import urllib.parse

from harness2 import embed_batch
from harness_call import post_form, get_execution

CORPUS_PATH = "../corpus/corpus_case1.json"
DOC_IDS = [
    "cluster6-1", "cluster6-2",            # confusable-пара на сущности "Звёздный"
    "distractor-374", "distractor-62", "distractor-3",
    "distractor-266", "distractor-403", "cluster5-1",
]
QUESTION = "Какие наиболее популярные произведения были созданы на протяжении 1984-1986 гг"
GOLD_DOC_ID = "cluster6-2"

data = json.load(open(CORPUS_PATH, encoding="utf-8"))
by_id = {c["id"]: c for c in data["corpus_500"]}
docs = [{"id": cid, "text": by_id[cid]["text"]} for cid in DOC_IDS]
assert GOLD_DOC_ID in DOC_IDS

texts = [QUESTION] + [d["text"] for d in docs]
vecs, meta = embed_batch(texts)
print(f"embedded {len(texts)} texts (1 вопрос + {len(docs)} документов): "
      f"wall={meta['wall_s']}s cost={meta['cost']}")
for d, v in zip(docs, vecs[1:]):
    d["embedding"] = v

payload = {
    "question": QUESTION,
    "gold_doc_id": GOLD_DOC_ID,
    "query_embedding_model": "openai/text-embedding-3-small",
    "corpus": docs,
}

resp = post_form("s10-case3-search", [json.dumps(payload, ensure_ascii=False)])
waiting = resp.get("formWaitingUrl", "")
exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
print("exec_id", exec_id)
time.sleep(5)
ex = get_execution(exec_id)
run = ex.get("data", {}).get("resultData", {}).get("runData", {})
print("nodes with data:", list(run.keys()))
print("status:", ex.get("status"), "finished:", ex.get("finished"))
node = "Разбор ответа реранкера + итог"
if node in run:
    try:
        out = run[node][0]["data"]["main"][0][0]["json"]
        print(out["summary"])
    except Exception as e:
        print("err reading", e, json.dumps(run[node][0], ensure_ascii=False)[:2000])
else:
    for n, entries in run.items():
        err = entries[0].get("error")
        if err:
            print(f"ERROR in node {n}: {json.dumps(err, ensure_ascii=False)[:800]}")
json.dump(ex, open("case3_search_execution.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
