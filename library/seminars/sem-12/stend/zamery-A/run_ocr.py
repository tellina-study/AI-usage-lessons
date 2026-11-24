import json, time
from rapidocr_onnxruntime import RapidOCR

BASE_DIR = "/tmp/s12-corpora/funsd/dataset"

def main():
    corpus = json.load(open("korpus/vyborka.json"))
    engine = RapidOCR()
    out = {}
    t_total0 = time.time()
    for o in corpus:
        fid = o["form_id"]
        path = f"{BASE_DIR}/{o['split']}/images/{o['img']}"
        t0 = time.time()
        result, elapse = engine(path)
        dt = time.time() - t0
        lines = []
        if result:
            for box, text, conf in result:
                lines.append({"box": box, "text": text, "conf": round(float(conf), 4)})
        out[fid] = {"seconds": round(dt, 3), "n_lines": len(lines), "lines": lines,
                    "text_joined": "\n".join(l["text"] for l in lines)}
        print(fid, f"{dt:.2f}s", len(lines), "строк")
    total = time.time() - t_total0
    print("ИТОГО", f"{total:.1f}s", "на", len(corpus), "форм")
    with open("raw/ocr_results.json", "w", encoding="utf-8") as fh:
        json.dump({"meta": {"engine": "rapidocr-onnxruntime", "total_seconds": round(total, 2),
                             "n_forms": len(corpus)}, "per_form": out}, fh, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
