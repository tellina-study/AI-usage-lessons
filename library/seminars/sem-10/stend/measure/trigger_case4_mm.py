import json, time, urllib.parse
from harness_call import post_form, get_execution

b64 = open("tinyA.png.b64").read()
data_url = f"data:image/png;base64,{b64}"
body = json.dumps({"model": "amazon/titan-embed-image-v1", "input": data_url}, ensure_ascii=False)
resp = post_form("s10-case4-mm", [body])
waiting = resp.get("formWaitingUrl", "")
exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
print("exec_id", exec_id)
time.sleep(3)
ex = get_execution(exec_id)
run = ex.get("data", {}).get("resultData", {}).get("runData", {})
print("nodes:", list(run.keys()))
if "Embed image (voyage-multimodal-3)" in run:
    out = run["Embed image (voyage-multimodal-3)"][0]["data"]["main"][0][0]["json"]
    print("dim:", len(out["data"][0]["embedding"]) if "data" in out else out)
json.dump(ex, open("case4_mm_execution.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
