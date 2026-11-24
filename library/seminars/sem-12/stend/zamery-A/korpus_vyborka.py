import json, os, re, sys
from collections import Counter
from PIL import Image

# Веха 1 (issue #351, 2026-11-24): расширение с одного среза (testing_data, 50 форм) на
# ОБА среза датасета FUNSD, одним общим проходом, тем же классификатором (CATS/classify)
# и той же логикой "edge". Каждая строка результата несёт "split", чтобы
# build_korpus.py/run_ocr.py/measure_vision.py знали, из какого каталога брать картинку.
BASE_DIR = "/tmp/s12-corpora/funsd/dataset"
SPLITS = ["testing_data", "training_data"]

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

def scan_split(split):
    ann_dir = os.path.join(BASE_DIR, split, "annotations")
    img_dir = os.path.join(BASE_DIR, split, "images")
    rows = []
    files = sorted(os.listdir(ann_dir))
    for fn in files:
        form_id = fn.replace(".json", "")
        d = json.load(open(os.path.join(ann_dir, fn)))
        pairs = extract_pairs(d["form"])
        img_path = os.path.join(img_dir, form_id + ".png")
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
            "form_id": form_id, "split": split, "w": w, "h": h,
            "n_fields": len(classified), "cats": cats_present,
            "fields": classified,
        })
    return rows

def main():
    rows = []
    for split in SPLITS:
        rows.extend(scan_split(split))
    # Проверка программно, не предположением (Веха 1, задание §1): коллизий form_id
    # между testing_data и training_data быть не должно (разные формы, разные id) —
    # если найдутся, это ломает "split"-based построение пути к картинке ниже.
    ids = [r["form_id"] for r in rows]
    dupes = sorted(k for k, v in Counter(ids).items() if v > 1)
    if dupes:
        raise RuntimeError(
            f"form_id коллизии между testing_data и training_data: {dupes} — "
            "это значит одно и то же имя файла существует в обоих срезах с (возможно) "
            "разным содержимым; построение пути по 'split' станет неоднозначным."
        )
    return rows

if __name__ == "__main__":
    rows = main()
    print(f"всего форм (оба среза): {len(rows)}, "
          f"по срезам: {dict(Counter(r['split'] for r in rows))}")
    pool = [r for r in rows if r["n_fields"] >= 3]
    print(f"пригодный пул (>=3 целевых поля, тот же порог, что в оригинале): "
          f"{len(pool)}, по срезам: {dict(Counter(r['split'] for r in pool))}")
    rows_sorted = sorted(rows, key=lambda r: (-len(r["cats"]), -r["n_fields"]))
    for r in rows_sorted[:60]:
        print(r["form_id"], r["split"], r["n_fields"], r["cats"])
