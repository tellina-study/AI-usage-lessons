"""Контактные листы для просмотра глазами новых кандидатов (issue #351, Веха
«sto-testов») — PIL-монтаж с подписью id под каждым кадром, N кадров на лист
(по умолчанию 12, сетка 3x4). Листы — временный инструмент курации, в гит не кладутся
(см. .gitignore этой папки)."""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT_DIR = HERE / "_contact_sheets"
THUMB = 220
LABEL_H = 22
COLS = 4


def make_sheet(paths_ids, out_path):
    n = len(paths_ids)
    rows = (n + COLS - 1) // COLS
    sheet = Image.new("RGB", (COLS * THUMB, rows * (THUMB + LABEL_H)), "white")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except Exception:
        font = ImageFont.load_default()
    for idx, (path, img_id) in enumerate(paths_ids):
        r, c = divmod(idx, COLS)
        x, y = c * THUMB, r * (THUMB + LABEL_H)
        try:
            im = Image.open(path).convert("RGB")
            im.thumbnail((THUMB, THUMB))
            ox = x + (THUMB - im.width) // 2
            oy = y + (THUMB - im.height) // 2
            sheet.paste(im, (ox, oy))
        except Exception as e:
            draw.text((x + 5, y + 5), f"ERR {e}", fill="red", font=font)
        draw.text((x + 5, y + THUMB), img_id, fill="black", font=font)
    sheet.save(out_path)
    print("saved", out_path, n, "images")


DIR_FOR = {"food": "/tmp/s12-corpora/oiv7/images/C-fooddrink",
           "slides": "/tmp/s12-corpora/oiv7/images/C-slides"}


def main(cls, prefix, batch_size=12):
    manifest = json.loads((HERE / "manifest-additions-C100.json").read_text())
    ids = sorted(m["id"] for m in manifest if m["class"] == cls)
    d = Path(DIR_FOR[cls])
    files = [d / f"{i}.jpg" for i in ids]
    OUT_DIR.mkdir(exist_ok=True)
    for i in range(0, len(files), batch_size):
        batch = files[i:i + batch_size]
        items = [(p, p.stem) for p in batch]
        make_sheet(items, OUT_DIR / f"{prefix}_{i//batch_size+1:02d}.png")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 12)
