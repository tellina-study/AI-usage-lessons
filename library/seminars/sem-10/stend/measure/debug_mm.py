from case4_measure import to_data_url
from harness2 import call_raw, cosine
import json

for fname in ["cord_sample/receipt_00.png", "cord_sample/receipt_15.png"]:
    data_url, ln = to_data_url(fname)
    body = {"model": "amazon/titan-embed-image-v1", "input": data_url}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
    resp = r["response"]
    vec = resp["data"][0]["embedding"]
    print(fname, "dim=", len(vec), "first5=", vec[:5], "norm=", sum(x*x for x in vec)**0.5)
