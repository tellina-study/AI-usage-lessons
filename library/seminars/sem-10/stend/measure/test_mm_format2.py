from harness_call import call_raw
import json

b64 = open("tiny_b64.txt").read()
data_url = f"data:image/png;base64,{b64}"
body = {"model": "amazon/titan-embed-image-v1", "input": data_url}
r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=90)
print(json.dumps(r["response"], ensure_ascii=False)[:1500])
