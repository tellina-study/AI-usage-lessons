"""
Aspect-ratio-safe crop helper (issue #340, owner round "preserve aspect ratios").

Root-cause bug found in prior round: s08b/s17/s20/s25 each place two photos into
fixed-size boxes via add_image(..., w=BOX_W, h=BOX_H) — python-pptx stretches the
source image non-uniformly whenever the source aspect ratio does not exactly equal
BOX_W/BOX_H. The prior round's "-crop.jpg" files were all cropped to one generic
~1.675 ratio regardless of each slide's own box aspect (box heights differ:
s08b/s20 PANEL_H=3.5, s17 PANEL_H=2.3, s25 PANEL_H=3.35 — all share PANEL_W=5.95),
so only s08b's crop happened to land close (1.6754 vs box 1.7292, ~3% stretch);
s17's box aspect is 2.6743 vs crop 1.6754 — a ~60% vertical squash, the worst case.

Fix: re-crop the ORIGINAL (pre-crop) source photos directly to each slide's own
exact box aspect ratio, via a centered crop (cut pixels off the long dimension,
centered on the frame) — never resize width/height independently. Overwrites the
existing "-crop.jpg" filenames in place so no downstream code changes are needed
(the add_image() calls already pass the box's own w/h, which will now exactly
match the re-cropped file's own aspect ratio).
"""
from pathlib import Path
from PIL import Image

PHOTOS = Path(__file__).resolve().parent / "assets" / "photos"


def center_crop_to_aspect(src_path: Path, dst_path: Path, target_ratio: float, quality: int = 92):
    im = Image.open(src_path)
    w, h = im.size
    src_ratio = w / h
    if abs(src_ratio - target_ratio) < 1e-4:
        # Already matches — just copy/re-save, no crop needed.
        im.convert("RGB").save(dst_path, quality=quality)
        return w, h, 1.0
    if src_ratio > target_ratio:
        # Source wider than target → crop width, keep full height, center horizontally.
        new_w = round(h * target_ratio)
        new_h = h
        left = round((w - new_w) / 2)
        top = 0
    else:
        # Source taller/narrower than target → crop height, keep full width, center vertically.
        new_w = w
        new_h = round(w / target_ratio)
        left = 0
        top = round((h - new_h) / 2)
    box = (left, top, left + new_w, top + new_h)
    cropped = im.crop(box).convert("RGB")
    cropped.save(dst_path, quality=quality)
    return new_w, new_h, new_w / new_h


# (original source file, output "-crop" file, slide box aspect ratio, slide id)
JOBS = [
    ("p08b-corn-seedlings-rows.jpg", "p08b-corn-seedlings-rows-crop.jpg", 1.7292, "s08b"),
    ("p08b-soy-seedling.jpg", "p08b-soy-seedling-crop.jpg", 1.7292, "s08b"),
    ("p17-rostselmash-torum-combine.jpg", "p17-rostselmash-torum-combine-crop.jpg", 2.6743, "s17"),
    ("p17-combine-dust-cloud.jpg", "p17-combine-dust-cloud-crop.jpg", 2.6743, "s17"),
    ("p20-farmwise-titan.jpg", "p20-farmwise-titan-crop.jpg", 1.7292, "s20"),
    ("p20-dusty-field-tillage.jpg", "p20-dusty-field-tillage-crop.jpg", 1.7292, "s20"),
    ("p22-cow-eartag-milking-robot.jpg", "p22-cow-eartag-milking-robot-crop.jpg", 1.8100, "s25"),
    ("p25-tiestall-anbindehaltung.jpg", "p25-tiestall-anbindehaltung-crop.jpg", 1.8100, "s25"),
    ("p10b-aerofarms-exterior.jpg", "p10b-aerofarms-exterior-crop.jpg", 1.85, "s10"),
    ("p10b-kalera-led-interior.jpg", "p10b-kalera-led-interior-crop.jpg", 2.00, "s10"),
    ("p10b-tobrfv-panelG.jpg", "p10b-tobrfv-virus-crop.jpg", 1.20, "s10"),
    ("p16b-laserweeder-module-render.jpg", "p16b-laserweeder-module-crop.jpg", 2.20, "s16b"),
]


def extract_tobrfv_panel_g():
    """Deterministic extraction of panel G (mottled-fruit symptoms) out of the
    8-panel composite figure 'ToBRFV Tomato Symptoms01.jpg' (Luria et al., CC
    BY-SA 4.0). Grid boundaries found via column/row near-white-pixel runs on
    the 960x720 reference thumbnail (see notes/decisions or iteration-log for
    the detection script) — panel G is column 2 of the bottom row.
    """
    src = PHOTOS / "p10b-tobrfv-virus-symptoms-full.jpg"
    out = PHOTOS / "p10b-tobrfv-panelG.jpg"
    im = Image.open(src)
    w, h = im.size
    sx, sy = w / 960.0, h / 720.0
    x0, x1 = 188 * sx, 437 * sx
    y0, y1 = 340 * sy, 695 * sy  # y1 trims the "G" caption label below the panel
    im.crop((int(x0), int(y0), int(x1), int(y1))).convert("RGB").save(out, quality=95)
    print(f"s10: extracted panel G -> {out.name}  {im.crop((int(x0), int(y0), int(x1), int(y1))).size}")


if __name__ == "__main__":
    extract_tobrfv_panel_g()
    for src_name, dst_name, ratio, slide in JOBS:
        src = PHOTOS / src_name
        dst = PHOTOS / dst_name
        if not src.exists():
            print(f"MISSING SOURCE: {src}")
            continue
        new_w, new_h, out_ratio = center_crop_to_aspect(src, dst, ratio)
        print(f"{slide}: {src_name} -> {dst_name}  {new_w}x{new_h}  ratio={out_ratio:.4f} (target {ratio})")
