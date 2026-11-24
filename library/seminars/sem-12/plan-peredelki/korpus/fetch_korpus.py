"""Детерминированная загрузка корпусов A/B/C Семинара 12 (Веха 1 круг 2, issue #351).

Качает ровно то, что проверено планировщиком 2026-11-24:
  A — FUNSD целиком (zip 16,8 МБ, 199 форм; подвыборку кейса A выбирает сессия
      производства по критериям kejs-A-dokumenty.md);
  B+C — единый фотокорпус Open Images V7 по manifest-foto-BC.json (131 файл, 43 МБ,
      срезы B-* и C-*); sha256 каждого файла сверяется с манифестом — расхождение
      печатается, не замалчивается (наборы исчезают и подменяются, см. журнал).

Запуск:  python3 fetch_korpus.py [целевая_папка]   (по умолчанию ./data)
Сеть: guillaumejaume.github.io (FUNSD), open-images-dataset.s3.amazonaws.com (фото).
Повторный запуск докачивает недостающее, готовое не трогает.
"""
import hashlib, json, os, sys, urllib.request, zipfile
import concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "data")
FUNSD_URL = "https://guillaumejaume.github.io/FUNSD/dataset.zip"


def fetch_funsd():
    zpath = os.path.join(DEST, "funsd.zip")
    if not os.path.exists(os.path.join(DEST, "funsd", "dataset")):
        os.makedirs(DEST, exist_ok=True)
        if not os.path.exists(zpath):
            urllib.request.urlretrieve(FUNSD_URL, zpath)
        with zipfile.ZipFile(zpath) as z:
            z.extractall(os.path.join(DEST, "funsd"))
    n = sum(len(fs) for _, _, fs in os.walk(os.path.join(DEST, "funsd", "dataset")))
    print(f"FUNSD: файлов {n} (ожидается 796: 199 форм train+test, png+json, + копии __MACOSX)")


def fetch_foto():
    recs = json.load(open(os.path.join(HERE, "manifest-foto-BC.json")))
    jobs = []
    for r in recs:
        d = os.path.join(DEST, "foto", r["slices"][0])
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, r["id"] + ".jpg")
        if not os.path.exists(p):
            jobs.append((r, p))
    def one(j):
        r, p = j
        urllib.request.urlretrieve(r["s3_url"], p)
        sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
        return None if sha == r["sha256_downloaded"] else f"SHA MISMATCH {r['id']}"
    with cf.ThreadPoolExecutor(8) as ex:
        bad = [b for b in ex.map(one, jobs) if b]
    total = sum(len(fs) for _, _, fs in os.walk(os.path.join(DEST, "foto")))
    print(f"foto: в манифесте {len(recs)}, на диске {total}, докачано {len(jobs)}, расхождений sha256: {len(bad)}")
    for b in bad:
        print(" ", b)


if __name__ == "__main__":
    fetch_funsd()
    fetch_foto()
