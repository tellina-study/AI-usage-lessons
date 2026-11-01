from harness2 import call_raw, cosine
for name in ["tinyA.png.b64", "tinyB.png.b64"]:
    b64 = open(name).read()
    data_url = f"data:image/png;base64,{b64}"
    body = {"model": "amazon/titan-embed-image-v1", "input": data_url}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
    resp = r["response"]
    v = resp["data"][0]["embedding"]
    print(name, "first5=", v[:5])
    globals()[name] = v
print("cosine tinyA vs tinyB:", cosine(globals()["tinyA.png.b64"], globals()["tinyB.png.b64"]))
