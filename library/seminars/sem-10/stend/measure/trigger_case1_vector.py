import json, time, urllib.parse, urllib.request, os
from harness_call import post_form, get_execution

data = json.load(open("corpus_case1_embedded.json"))
needle = [d for d in data["corpus_200"] if d["is_needle"]][:10]
q = data["questions"][0]  # q1
payload = {
    "model": "openai/text-embedding-3-small",
    "question": q["question"],
    "corpus": [{"id": d["id"], "text": d["text"], "embedding": d["embedding"]} for d in needle],
}
resp = post_form("s10-case1-vector", [json.dumps(payload, ensure_ascii=False)])
waiting = resp.get("formWaitingUrl", "")
exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
print("exec_id", exec_id)
time.sleep(4)
ex = get_execution(exec_id)
run = ex.get("data", {}).get("resultData", {}).get("runData", {})
print("nodes with data:", list(run.keys()))
print("status:", ex.get("status"), "finished:", ex.get("finished"))
if "Answer (RAG)" in run:
    try:
        print("ANSWER:", run["Answer (RAG)"][0]["data"]["main"][0][0]["json"])
    except Exception as e:
        print("err reading answer", e, json.dumps(run["Answer (RAG)"][0], ensure_ascii=False)[:1000])
if "Simple Vector Store (cosine top-1)" in run:
    print("RETRIEVED:", run["Simple Vector Store (cosine top-1)"][0]["data"]["main"][0][0]["json"])
json.dump(ex, open("case1_vector_execution.json","w", encoding="utf-8"), ensure_ascii=False, indent=2)
