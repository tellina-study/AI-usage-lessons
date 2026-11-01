from harness2 import call_raw

for name in ["black", "white"]:
    b64 = open(f"{name}_b64.txt").read()
    body = {"model": "amazon/titan-embed-image-v1", "input": b64}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
    resp = r["response"]
    if "data" in resp:
        print(name, "first5=", resp["data"][0]["embedding"][:5])
    else:
        print(name, "ERR", resp)
