from harness_call import call_raw
import json

for model in ["openai/text-embedding-3-small", "voyage/voyage-3-lite", "voyage/voyage-3"]:
    r = call_raw("https://openrouter.ai/api/v1/embeddings",
                  {"model": model, "input": "тестовый текст для проверки эмбеддинга"})
    resp = r["response"]
    if isinstance(resp, dict) and "error" in resp:
        print(model, "ERROR:", json.dumps(resp["error"], ensure_ascii=False)[:300])
    elif isinstance(resp, dict) and "data" in resp:
        dim = len(resp["data"][0]["embedding"])
        print(model, "OK dim=", dim, "usage=", resp.get("usage"))
    else:
        print(model, "UNEXPECTED:", json.dumps(resp, ensure_ascii=False)[:300])
