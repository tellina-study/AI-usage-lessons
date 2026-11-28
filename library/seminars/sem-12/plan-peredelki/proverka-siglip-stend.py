"""Проверка стенда для кейса D (С12, issue #351): запускается ли кросс-модальный
поиск текст -> картинка на локальном SigLIP, и как отличается русский запрос от
английского. Это НЕ замер кейса — только проверка запуском, что метод из плана
работает на этой машине (PEREDELKA-2026-11-24.md §8).

Картинки: 3 скана чеков (фотографический материал) + 3 отрисованные схемы занятия
(заведомо другой класс изображения). Запросы: пары RU/EN одного смысла.
Ожидание осмысленного результата: английский запрос про чек ставит чеки выше схем
и наоборот; по русскому запросу смотрим честно, что выйдет.
"""
import torch
from pathlib import Path
from PIL import Image
from transformers import AutoProcessor, AutoModel

ROOT = Path(__file__).resolve().parents[3]  # .../library
IMAGES = [
    ("receipt_00", ROOT / "seminars/sem-10/stend/corpus/cord_sample/receipt_00.jpg"),
    ("receipt_07", ROOT / "seminars/sem-10/stend/corpus/cord_sample/receipt_07.jpg"),
    ("receipt_19", ROOT / "seminars/sem-10/stend/corpus/cord_sample/receipt_19.jpg"),
    ("fig_cascade", ROOT / "seminars/sem-12/rendered/figures/k1-cascade-diagram.png"),
    ("fig_encoders", ROOT / "seminars/sem-12/rendered/figures/case2-two-encoders.png"),
    ("fig_pairs", ROOT / "seminars/sem-12/rendered/figures/case2-image-pairs.png"),
]
QUERIES = [
    ("EN чек", "a photo of a paper shop receipt"),
    ("RU чек", "фотография бумажного кассового чека"),
    ("EN схема", "a diagram with colored boxes and arrows"),
    ("RU схема", "схема с цветными блоками и стрелками"),
]

MODEL_ID = "google/siglip-base-patch16-224"
model = AutoModel.from_pretrained(MODEL_ID)
processor = AutoProcessor.from_pretrained(MODEL_ID)
model.eval()

pils = [Image.open(p).convert("RGB") for _, p in IMAGES]
with torch.no_grad():
    img_in = processor(images=pils, return_tensors="pt")
    img_out = model.get_image_features(**img_in)
    # в этой версии transformers метод возвращает BaseModelOutputWithPooling —
    # вектор лежит в .pooler_output (та же находка, что zamery-k3/README.md)
    img_vecs = img_out if isinstance(img_out, torch.Tensor) else img_out.pooler_output
    img_vecs = img_vecs / img_vecs.norm(dim=-1, keepdim=True)

    txt_in = processor(
        text=[q for _, q in QUERIES], padding="max_length", return_tensors="pt"
    )
    txt_out = model.get_text_features(**txt_in)
    txt_vecs = txt_out if isinstance(txt_out, torch.Tensor) else txt_out.pooler_output
    txt_vecs = txt_vecs / txt_vecs.norm(dim=-1, keepdim=True)

sims = txt_vecs @ img_vecs.T  # [queries x images]

names = [n for n, _ in IMAGES]
print(f"model={MODEL_ID}, images={len(names)}, queries={len(QUERIES)}")
print("cosine текстового вектора запроса с вектором каждой картинки:")
header = " " * 22 + "  ".join(f"{n:>12}" for n in names)
print(header)
for (label, q), row in zip(QUERIES, sims):
    vals = "  ".join(f"{v.item():12.4f}" for v in row)
    top = names[int(row.argmax())]
    print(f"{label:>20}  {vals}   top1={top}")
