import json, os, re, sys
from PIL import Image

ANN_DIR = "/tmp/s12-corpora/funsd/dataset/testing_data/annotations"
IMG_DIR = "/tmp/s12-corpora/funsd/dataset/testing_data/images"

CATS = {
    "phone": re.compile(r"(PHONE|TELEPHONE|FAX|VOICE NUMBER|TEL\b)", re.I),
    "name": re.compile(r"^(TO|FROM|NAME|ATTN|SENDER|RECIPIENT\(S\)|MESSAGE TO|CASE NAME|NAME OF ACCOUNT|NAME OF GUEST)\b", re.I),
    "date": re.compile(r"^DATE\b", re.I),
    "count": re.compile(r"(NO\.? OF|NUMBER OF|# ?REPS?|PAGES|NO\. IN PARTY)", re.I),
}
# Порядок категорий значим: "phone" проверяется первым, потому что GT-вопрос вида
# «Sender Voice Number» одновременно начинается с имени-ключа (SENDER) и несёт
# телефонный номер по смыслу — классифицируем по содержанию поля (это номер), не по
# первому слову подписи.

def classify(qtext):
    t = qtext.strip()
    for cat, pat in CATS.items():
        if pat.search(t):
            return cat
    return None

def entities_by_id(form):
    return {e["id"]: e for e in form}

def extract_pairs(form):
    byid = entities_by_id(form)
    pairs = []
    for e in form:
        if e["label"] != "question":
            continue
        for link in e.get("linking", []):
            a, b = link
            other_id = b if a == e["id"] else a
            other = byid.get(other_id)
            if other and other["label"] == "answer" and other["text"].strip():
                pairs.append({
                    "q_id": e["id"], "q_text": e["text"].strip(),
                    "q_box": e["box"], "a_id": other["id"],
                    "a_text": other["text"].strip(), "a_box": other["box"],
                })
    return pairs

def main():
    rows = []
    files = sorted(os.listdir(ANN_DIR))
    for fn in files:
        form_id = fn.replace(".json", "")
        d = json.load(open(os.path.join(ANN_DIR, fn)))
        pairs = extract_pairs(d["form"])
        img_path = os.path.join(IMG_DIR, form_id + ".png")
        with Image.open(img_path) as im:
            w, h = im.size
        classified = []
        for p in pairs:
            cat = classify(p["q_text"])
            if cat:
                edge = p["a_box"][3] > 0.92 * h or p["a_box"][1] > 0.92 * h
                classified.append({**p, "cat": cat, "edge": edge, "img_w": w, "img_h": h})
        cats_present = sorted(set(c["cat"] for c in classified))
        rows.append({
            "form_id": form_id, "w": w, "h": h,
            "n_fields": len(classified), "cats": cats_present,
            "fields": classified,
        })
    return rows

if __name__ == "__main__":
    rows = main()
    rows_sorted = sorted(rows, key=lambda r: (-len(r["cats"]), -r["n_fields"]))
    for r in rows_sorted[:60]:
        print(r["form_id"], r["n_fields"], r["cats"])
