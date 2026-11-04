from harness2 import call_raw
from case4_measure import to_data_url
import json

for fname in ["cord_sample/receipt_00.png", "cord_sample/receipt_15.png"]:
    data_url, ln = to_data_url(fname)
    raw_b64 = data_url.split(",", 1)[1]
    body = {"model": "amazon/titan-embed-image-v1", "input": raw_b64}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
    resp = r["response"]
    if "data" in resp:
        vec = resp["data"][0]["embedding"]
        print(fname, "OK first5=", vec[:5])
    else:
        print(fname, "ERROR", json.dumps(resp, ensure_ascii=False)[:300])
