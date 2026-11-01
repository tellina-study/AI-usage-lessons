from harness2 import call_raw, cosine
vecs = {}
for name in ["midA.jpg.b64", "midB.jpg.b64"]:
    b64 = open(name).read()
    data_url = f"data:image/jpeg;base64,{b64}"
    body = {"model": "amazon/titan-embed-image-v1", "input": data_url}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
    v = r["response"]["data"][0]["embedding"]
    vecs[name] = v
print("cosine midA vs midB:", cosine(vecs["midA.jpg.b64"], vecs["midB.jpg.b64"]))
