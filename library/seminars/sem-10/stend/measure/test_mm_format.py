from harness_call import call_raw
import json, base64

b64 = open("sample0_b64.txt").read()
data_url = f"data:image/png;base64,{b64}"

tests = {
    "A_data_url_string": {"model": "amazon/titan-embed-image-v1", "input": data_url},
    "B_image_url_obj": {"model": "amazon/titan-embed-image-v1",
                         "input": [{"type": "image_url", "image_url": {"url": data_url}}]},
    "C_input_image_field": {"model": "amazon/titan-embed-image-v1",
                             "input": [{"type": "image", "image": data_url}]},
}
for name, body in tests.items():
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=90)
    resp = r["response"]
    if isinstance(resp, dict) and "error" in resp:
        print(name, "ERROR:", json.dumps(resp["error"], ensure_ascii=False)[:300])
    elif isinstance(resp, dict) and "data" in resp:
        dim = len(resp["data"][0]["embedding"])
        print(name, "OK dim=", dim, "usage=", resp.get("usage"))
    else:
        print(name, "UNEXPECTED:", json.dumps(resp, ensure_ascii=False)[:300])
