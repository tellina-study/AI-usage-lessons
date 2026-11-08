from harness_call import call_raw
import json

candidates = [
    "jinaai/jina-embeddings-v3",
    "jinaai/jina-clip-v2",
    "amazon/titan-embed-image-v1",
    "google/multimodalembedding",
    "cohere/embed-v4.0",
    "voyage/voyage-multimodal-3.0",
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
