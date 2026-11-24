"""Нулевой выстрел по словам — `google/siglip-base-patch16-224` (HF `transformers`
5.24.0, локально, без сети после первой загрузки весов). Модель и настройки (С5):
EN-подсказки (основной прогон) + одна пара RU-подсказок на класс (цена языка, один
прогон, №7 brifинга). `.pooler_output` у обеих башен (#351-3, transformers 5.22+) —
нормировано L2 вручную, не argmax по logits_per_image (нужны непрерывные скоры для
полосы неопределённости, не только лучший класс)."""
import json
import sys
from pathlib import Path

import torch
from PIL import Image
from transformers import AutoProcessor, AutoModel

sys.path.insert(0, str(Path(__file__).parent))
from corpus import all_unique_images

MODEL_NAME = "google/siglip-base-patch16-224"

PROMPTS = {
    # Короткие шаблоны «a person doing X» вместо развёрнутых предложений — проверено
    # (эта сессия, пилот на 4 кадрах): длинное предложение топит скор даже на чистых
    # позитивах (pos_clear=0,038); короткий шаблон «a person smoking a cigarette» даёт
    # разделение и, важно, НЕ путает предмет без человека со сценой (ведро окурков:
    # 0,0001 против 0,15-0,37 у позитивов) — остальные короткие варианты («a photo of
    # smoking», голое «smoking») эту путаницу как раз повторяют. Естественный язык
    # топит SigLIP, не просто «короче» — предметная формулировка сцены обязательна.
    "smoking": {
        "en": ("a person smoking a cigarette", "a person not smoking"),
        "ru": ("человек курит сигарету", "человек не курит"),
    },
    "food_drink": {
        "en": ("a person eating or drinking", "a person not eating or drinking"),
        "ru": ("человек ест или пьёт", "человек не ест и не пьёт"),
    },
    "screen_present": {
        "en": ("a presentation screen or projector in the room", "no screen or projector in the room"),
        "ru": ("экран или проектор в комнате", "нет экрана и проектора в комнате"),
    },
}

OUT = Path(__file__).parent / "raw" / "siglip_results.jsonl"
OUT.parent.mkdir(exist_ok=True)


def l2(t):
    return t / t.norm(p=2, dim=-1, keepdim=True)


def get_text_features(model, processor, texts, device):
    inputs = processor(text=texts, padding="max_length", truncation=True, max_length=64,
                       return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.get_text_features(**inputs)
    feat = out.pooler_output if hasattr(out, "pooler_output") else out
    return l2(feat)


def get_image_features(model, processor, image, device):
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.get_image_features(**inputs)
    feat = out.pooler_output if hasattr(out, "pooler_output") else out
    return l2(feat)


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME).to(device).eval()

    text_feats = {}
    for cls, langs in PROMPTS.items():
        for lang, (pos, neg) in langs.items():
            text_feats[(cls, lang)] = get_text_features(model, processor, [pos, neg], device)

    items = all_unique_images()
    print(f"running SigLIP zero-shot on {len(items)} images", flush=True)
    with OUT.open("w") as f:
        for n, (d, i) in enumerate(items):
            path = f"{d}/{i}.jpg"
            try:
                img = Image.open(path).convert("RGB")
                img_feat = get_image_features(model, processor, img, device)
            except Exception as e:
                f.write(json.dumps({"dir": d, "id": i, "error": str(e)}) + "\n")
                continue
            scores = {}
            for (cls, lang), tf in text_feats.items():
                logits = (model.logit_scale.exp() * img_feat @ tf.t() + model.logit_bias).squeeze(0)
                probs = torch.sigmoid(logits)
                scores[f"{cls}_{lang}_pos"] = round(float(probs[0]), 4)
                scores[f"{cls}_{lang}_neg"] = round(float(probs[1]), 4)
            rec = {"dir": d, "id": i, **scores}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if n % 40 == 0:
                print(f"{n+1}/{len(items)}", flush=True)
    print("done.", flush=True)


if __name__ == "__main__":
    main()
