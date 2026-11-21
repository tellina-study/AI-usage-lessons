"""Семинар 11, Кейс 4 — общие функции замера (эмбеддинг + косинус), тонкая
копия sem-10/stend/measure/harness2.py (другая модель не нужна: этот кейс
меряет деградацию ТОЧНОГО поиска по эмбеддингам, не LLM-ответ — llm_answer
этому кейсу не нужен, в отличие от sem-10 Кейса 1)."""
import json

from harness_call import call_raw

EMBED_MODEL = "openai/text-embedding-3-small"


def embed_batch(texts, model=EMBED_MODEL, timeout=180):
    body = {"model": model, "input": texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
    resp = r["response"] or {}
    if "data" not in resp:
        raise RuntimeError(f"embed_batch failed: {json.dumps(resp, ensure_ascii=False)[:800]}")
    vecs = [d["embedding"] for d in resp["data"]]
    usage = resp.get("usage", {})
    return vecs, {"exec_id": r["exec_id"], "wall_s": r["wall_s"], "cost": usage.get("cost"),
                  "prompt_tokens": usage.get("prompt_tokens")}


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0
