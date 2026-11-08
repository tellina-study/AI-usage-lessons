"""Общие функции замера Семинара 10 — через вебхук s10-raw-openrouter (харнесс
sborka.py), ключ OpenRouter остаётся на стороне n8n. Импортирует harness_call.call_raw."""
import json
import time

from harness_call import call_raw

CHAT_MODEL = "openai/gpt-4o-mini"
EMBED_MODEL = "openai/text-embedding-3-small"
MM_MODEL = "amazon/titan-embed-image-v1"


def llm_answer(question, context_text, timeout=90):
    body = {
        "model": CHAT_MODEL,
        "messages": [
            {"role": "system", "content": "Отвечай ТОЛЬКО по тексту(ам) ниже, коротко (1 предложение). "
                                            "Если ответа нет в тексте — напиши «нет информации»."},
            {"role": "user", "content": f"Текст:\n{context_text}\n\nВопрос: {question}"},
        ],
        "usage": {"include": True},
    }
    r = call_raw("https://openrouter.ai/api/v1/chat/completions", body, timeout=timeout)
    resp = r["response"] or {}
    try:
        answer = resp["choices"][0]["message"]["content"]
    except Exception:
        answer = None
    usage = resp.get("usage", {})
    return {
        "exec_id": r["exec_id"], "wall_s": r["wall_s"], "node_ms": r["node_ms"],
        "answer": answer, "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"), "cost": usage.get("cost"),
        "raw_error": resp.get("error"),
    }


def embed_batch(texts, model=EMBED_MODEL, timeout=120):
    body = {"model": model, "input": texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
    resp = r["response"] or {}
    if "data" not in resp:
        raise RuntimeError(f"embed_batch failed: {json.dumps(resp, ensure_ascii=False)[:500]}")
    vecs = [d["embedding"] for d in resp["data"]]
    usage = resp.get("usage", {})
    return vecs, {"wall_s": r["wall_s"], "cost": usage.get("cost"), "prompt_tokens": usage.get("prompt_tokens")}


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def contains_answer(model_answer, reference_answer):
    if not model_answer:
        return False
    ma = model_answer.lower().strip()
    ra = reference_answer.lower().strip()
    return ra in ma
