"""Качает 40 снимков корпуса B (`razmetka.json`, in_corpus=true) в
`corpus-cache/<id>.jpg` — локальный кэш, в гит не кладётся (`.gitignore`),
кроме снимков, которые дойдут до кадров деки (копируются туда отдельно).
sha256 каждого файла сверяется с `korpus/manifest-foto-BC.json`.

Запуск:  python3 fetch_corpus_b.py
"""
import hashlib
import json
import os
import urllib.request
import concurrent.futures as cf
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEST = HERE / "corpus-cache"
RAZMETKA = HERE / "razmetka.json"


def main():
    DEST.mkdir(exist_ok=True)
    doc = json.loads(RAZMETKA.read_text(encoding="utf-8"))
    recs = [e for e in doc["entries"] if e["in_corpus"]]
    print(f"в разметке in_corpus=true: {len(recs)}")

    def one(r):
        p = DEST / f"{r['id']}.jpg"
        if p.exists():
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            if sha == r["sha256_downloaded"]:
                return (r["id"], "cached-ok")
            return (r["id"], f"cached-MISMATCH {sha[:12]}")
        try:
            req = urllib.request.Request(r["s3_url"], headers={"User-Agent": "curl/8"})
            data = urllib.request.urlopen(req, timeout=30).read()
        except Exception as e:
            return (r["id"], f"ОШИБКА {e}")
        sha = hashlib.sha256(data).hexdigest()
        if sha != r["sha256_downloaded"]:
            p.with_suffix(".jpg.badsha").write_bytes(data)
            return (r["id"], f"SHA MISMATCH ожид {r['sha256_downloaded'][:12]} получ {sha[:12]}")
        p.write_bytes(data)
        return (r["id"], f"ok {len(data)} байт")

    with cf.ThreadPoolExecutor(8) as ex:
        results = list(ex.map(one, recs))

    ok = [r for r in results if r[1].startswith("ok") or r[1] == "cached-ok"]
    bad = [r for r in results if r not in ok]
    print(f"скачано/в кэше успешно: {len(ok)}/{len(recs)}")
    for i, s in bad:
        print(" ", i, "->", s)
    if bad:
        raise SystemExit(f"{len(bad)} снимков не скачались — см. список выше")


if __name__ == "__main__":
    main()
