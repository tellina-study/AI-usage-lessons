"""Ступень 3 кейса C — «наш ли материал на экране»: сличение с собственной
библиотекой слайдов курса (239 снимков, sem-02/03/04), не детекция предмета.

Позитивы — наши же кадры в том виде, в каком путешествует утечка (пережатие q30,
обрезка 4%, double-screenshot — снимок экрана со снимка). Трудные негативы — наши
ДРУГИЕ кадры (соседний слайд той же деки, тот же шаблон/палитра/сетка) + чужие слайды
с экранов Open Images (C-slides). Методы: перцептивный хэш (imagehash.phash, 64-бит)
против эмбеддинга (SigLIP, косинус). Метрика: recall@1 + доля коллизий (чужой/соседний
кадр ближе своего).

Граница, прямо: настоящих фотографий наших слайдов с экрана в зале у нас нет —
перспектива, блик, частичное перекрытие НЕ измерены этим скриптом. Измерены только
три цифровых артефакта утечки (пережатие/обрезка/double-screenshot).
"""
import io
import json
import random
import sys
from pathlib import Path

import imagehash
import torch
from PIL import Image, ImageOps
from transformers import AutoProcessor, AutoModel

sys.path.insert(0, str(Path(__file__).parent))

RANDOM_SEED = 20261124
LIB_DIRS = {
    "sem-02": "../../../sem-02/rendered/snapshots",
    "sem-03": "../../../sem-03/rendered/snapshots",
    "sem-04": "../../../sem-04/rendered/snapshots",
}
HERE = Path(__file__).parent
FOREIGN_DIR = Path("/tmp/s12-corpora/oiv7/images/C-slides")

OUT_DIR = HERE / "raw"
OUT_DIR.mkdir(exist_ok=True)


def library_items():
    items = []
    for deck, rel in LIB_DIRS.items():
        p = (HERE / rel).resolve()
        for f in sorted(p.glob("*.png")):
            items.append((deck, f.stem, f))
    return items


def degrade_recompress(im, q=30):
    buf = io.BytesIO()
    im.convert("RGB").save(buf, format="JPEG", quality=q)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def degrade_crop4(im):
    w, h = im.size
    return im.crop((int(w * 0.04), int(h * 0.04), int(w * 0.96), int(h * 0.96))).convert("RGB")


def degrade_double_screenshot(im):
    """Снимок экрана со снимка: тёмная рамка (борт монитора) + лёгкий поворот +
    JPEG-пережатие дважды подряд — два отдельных re-encode, не один с другим q."""
    im = im.convert("RGB")
    bordered = ImageOps.expand(im, border=40, fill=(18, 18, 20))
    rotated = bordered.rotate(1.5, expand=True, fillcolor=(18, 18, 20))
    once = degrade_recompress(rotated, q=60)
    twice = degrade_recompress(once, q=45)
    return twice


DEGRADATIONS = {
    "recompress_q30": degrade_recompress,
    "crop4": degrade_crop4,
    "double_screenshot": degrade_double_screenshot,
}


def phash(im):
    return imagehash.phash(im, hash_size=8)


def main():
    random.seed(RANDOM_SEED)
    lib = library_items()
    print(f"library size = {len(lib)}", flush=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = AutoProcessor.from_pretrained("google/siglip-base-patch16-224")
    model = AutoModel.from_pretrained("google/siglip-base-patch16-224").to(device).eval()

    def embed(im):
        inputs = processor(images=im, return_tensors="pt").to(device)
        with torch.no_grad():
            out = model.get_image_features(**inputs)
        feat = out.pooler_output if hasattr(out, "pooler_output") else out
        return (feat / feat.norm(p=2, dim=-1, keepdim=True)).squeeze(0)

    print("computing library hashes + embeddings...", flush=True)
    lib_hash, lib_emb = {}, {}
    for deck, sid, path in lib:
        im = Image.open(path).convert("RGB")
        lib_hash[(deck, sid)] = phash(im)
        lib_emb[(deck, sid)] = embed(im)

    emb_matrix = torch.stack([lib_emb[k] for k in lib_emb.keys()])
    emb_keys = list(lib_emb.keys())

    sample_n = 30
    queries = random.sample(lib, sample_n)
    print(f"sampled {sample_n} true slides as query sources", flush=True)

    results = []
    for deck, sid, path in queries:
        orig = Image.open(path).convert("RGB")
        for degname, degfn in DEGRADATIONS.items():
            qimg = degfn(orig)
            qhash = phash(qimg)
            qemb = embed(qimg)

            hash_dists = {k: (qhash - h) for k, h in lib_hash.items()}
            best_hash_key = min(hash_dists, key=hash_dists.get)
            best_hash_dist = hash_dists[best_hash_key]
            true_hash_dist = hash_dists[(deck, sid)]

            sims = (emb_matrix @ qemb).tolist()
            sim_map = dict(zip(emb_keys, sims))
            best_emb_key = max(sim_map, key=sim_map.get)
            best_emb_sim = sim_map[best_emb_key]
            true_emb_sim = sim_map[(deck, sid)]

            results.append({
                "true_deck": deck, "true_sid": sid, "degradation": degname,
                "hash_top1_deck": best_hash_key[0], "hash_top1_sid": best_hash_key[1],
                "hash_top1_dist": int(best_hash_dist), "hash_true_dist": int(true_hash_dist),
                "hash_recall1": best_hash_key == (deck, sid),
                "emb_top1_deck": best_emb_key[0], "emb_top1_sid": best_emb_key[1],
                "emb_top1_sim": round(best_emb_sim, 4), "emb_true_sim": round(true_emb_sim, 4),
                "emb_recall1": best_emb_key == (deck, sid),
            })

    # чужие слайды (Open Images C-slides) — должны НЕ сличиться с нашей библиотекой
    # (ни одного совпадения top-1 с нашим слайдом при разумном пороге)
    foreign_results = []
    if FOREIGN_DIR.exists():
        for f in sorted(FOREIGN_DIR.glob("*.jpg")):
            im = Image.open(f).convert("RGB")
            qhash = phash(im)
            qemb = embed(im)
            hash_dists = {k: (qhash - h) for k, h in lib_hash.items()}
            best_hash_key = min(hash_dists, key=hash_dists.get)
            sims = (emb_matrix @ qemb).tolist()
            sim_map = dict(zip(emb_keys, sims))
            best_emb_key = max(sim_map, key=sim_map.get)
            foreign_results.append({
                "id": f.stem,
                "hash_top1_deck": best_hash_key[0], "hash_top1_sid": best_hash_key[1],
                "hash_top1_dist": int(hash_dists[best_hash_key]),
                "emb_top1_deck": best_emb_key[0], "emb_top1_sid": best_emb_key[1],
                "emb_top1_sim": round(sim_map[best_emb_key], 4),
            })

    with (OUT_DIR / "stage3_results.json").open("w") as f:
        json.dump({"queries": results, "foreign": foreign_results,
                   "library_size": len(lib)}, f, ensure_ascii=False, indent=2)
    print("done.", flush=True)


if __name__ == "__main__":
    main()
