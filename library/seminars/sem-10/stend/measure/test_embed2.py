from harness_call import call_raw
import json

candidates = [
    "voyageai/voyage-multimodal-3",
    "voyage-multimodal-3",
    "voyage/voyage-multimodal-3",
    "voyageai/voyage-3-large",
    "openai/text-embedding-3-large",
    "google/text-embedding-004",
    "cohere/embed-multilingual-v3.0",
    "mistralai/mistral-embed",
]
for model in candidates:
    r = call_raw("https://openrouter.ai/api/v1/embeddings",
                  {"model": model, "input": "test"})
    resp = r["response"]
    if isinstance(resp, dict) and "error" in resp:
        print(model, "ERROR:", json.dumps(resp["error"], ensure_ascii=False)[:200])
    elif isinstance(resp, dict) and "data" in resp:
        dim = len(resp["data"][0]["embedding"])
        print(model, "OK dim=", dim)
    else:
        print(model, "UNEXPECTED:", json.dumps(resp, ensure_ascii=False)[:200])
