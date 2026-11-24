"""Разовый поиск-кандидатов для доведения Кейса C до 100+ кадров/класс (issue #351,
Веха «sto-testov»). Ищет по val+test human-imagelabels CSV OIV7 человеческие пометки
(Confidence==1) классов Eating/Drinking (еда) и Presentation/Projection screen (экран),
исключает id, уже скачанные в C-fooddrink/C-slides, сверяет с candidates_meta.json
(лицензия CC BY 2.0 — уже проверена объединением с *-images-with-rotation.csv в Вехе 1
круга 2, см. korpusa.md §2.1). Печатает JSON-список кандидатов с license/author/landing/
s3_url — руками не трогать, докачка через download_candidates_C100.py."""
import csv
import json
from pathlib import Path

OIV7 = Path("/tmp/s12-corpora/oiv7")
IMAGES = OIV7 / "images"

LABELS = {
    "food": {"/m/01f5gx": "Eating", "/m/0hjbz": "Drinking"},
    "slides": {"/m/02y3rj": "Presentation", "/m/06ycgh": "Projection screen"},
}

CSVS = [
    ("validation", OIV7 / "oidv7-val-annotations-human-imagelabels.csv"),
    ("test", OIV7 / "oidv7-test-annotations-human-imagelabels.csv"),
]


def already_have(dirname):
    d = IMAGES / dirname
    if not d.is_dir():
        return set()
    return {p.stem for p in d.glob("*.jpg")}


def scan():
    hits = {cls: {code: [] for code in codes} for cls, codes in LABELS.items()}
    wanted_codes = {code for codes in LABELS.values() for code in codes}
    for subset, path in CSVS:
        with open(path, newline="") as f:
            r = csv.DictReader(f)
            for row in r:
                code = row["LabelName"]
                if code not in wanted_codes:
                    continue
                try:
                    conf = float(row["Confidence"])
                except ValueError:
                    continue
                if conf < 1:
                    continue
                for cls, codes in LABELS.items():
                    if code in codes:
                        hits[cls][code].append((subset, row["ImageID"]))
    return hits


def main():
    meta = json.load(open(OIV7 / "candidates_meta.json"))
    existing_food = already_have("C-fooddrink")
    existing_slides = already_have("C-slides")

    hits = scan()
    print("--- сырой счёт по CSV (до вычета уже скачанных и до фильтра метаданных) ---")
    for cls, codes in hits.items():
        for code, rows in codes.items():
            print(f"{cls} {code} ({LABELS[cls][code]}): {len(rows)}")

    out = {}
    for cls, existing in [("food", existing_food), ("slides", existing_slides)]:
        seen = set()
        cands = []
        for code, rows in hits[cls].items():
            for subset, img_id in rows:
                if img_id in existing or img_id in seen:
                    continue
                m = meta.get(img_id)
                if not m:
                    continue  # нет метаданных (лицензия/автор) — не берём без проверки
                seen.add(img_id)
                cands.append({
                    "id": img_id, "label_code": code, "label_name": LABELS[cls][code],
                    "subset": subset, "license": m["license"], "author": m["author"],
                    "landing": m["landing"],
                    "s3_url": f"https://open-images-dataset.s3.amazonaws.com/{subset}/{img_id}.jpg",
                })
        out[cls] = cands
        print(f"{cls}: новых кандидатов с метаданными = {len(cands)} "
              f"(уже скачано ранее: {len(existing)})")
        non_ccby = [c for c in cands if "by/2.0" not in c["license"] and "by/4.0" not in c["license"]]
        if non_ccby:
            print(f"  ВНИМАНИЕ: {len(non_ccby)} кандидатов с лицензией НЕ CC BY — исключить руками")

    Path(OIV7 / "candidates_C100.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print("записано:", OIV7 / "candidates_C100.json")


if __name__ == "__main__":
    main()
