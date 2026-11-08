from harness2 import call_raw, cosine
import json

for txt in ["кот", "космический корабль летит к Марсу"]:
    body = {"model": "amazon/titan-embed-image-v1", "input": txt}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=60)
    vec = r["response"]["data"][0]["embedding"]
    print(txt, "first5=", vec[:5])

# повторный тест с картинками, но ПРОВЕРИМ, что data_url реально разный
from case4_measure import to_data_url
du1, l1 = to_data_url("cord_sample/receipt_00.png")
du2, l2 = to_data_url("cord_sample/receipt_15.png")
print("data urls differ:", du1 != du2, "lens", l1, l2)
print("du1 prefix", du1[:60])
print("du2 prefix", du2[:60])
