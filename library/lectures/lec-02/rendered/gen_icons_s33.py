#!/usr/bin/env python3
"""s33 (v3.0, issue #183): 4 flat column icons for the size-classes matrix —
laptop / single GPU / server rack / cloud-cluster. Own hand-authored SVG in
Ocean palette, rasterized via PyMuPDF (same pipeline as gen_assets_v3.py;
mmdc/rsvg unavailable in sandbox — notes/mcp-limitations.md [#118-1]/[#157-1]).
"""
from pathlib import Path
import pymupdf

ICONS = Path(__file__).resolve().parent / "assets/icons"
ICONS.mkdir(parents=True, exist_ok=True)


def render(svg_text: str, name: str, scale: float = 2.0):
    svg_path = ICONS / f"{name}.svg"
    png_path = ICONS / f"{name}.png"
    svg_path.write_text(svg_text, encoding="utf-8")
    doc = pymupdf.open(str(svg_path))
    pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=True)
    pix.save(str(png_path))
    print(name, png_path.stat().st_size, "bytes")


LAPTOP = """<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">
  <rect x="18" y="22" width="60" height="38" rx="4" fill="#F4F7FA" stroke="#065A82" stroke-width="5"/>
  <rect x="26" y="30" width="44" height="22" rx="2" fill="#1C7293"/>
  <path d="M10 66 L86 66 L80 74 L16 74 Z" fill="#065A82"/>
</svg>"""

GPU = """<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">
  <rect x="10" y="30" width="72" height="34" rx="5" fill="#F4F7FA" stroke="#065A82" stroke-width="5"/>
  <circle cx="36" cy="47" r="10" fill="none" stroke="#028090" stroke-width="5"/>
  <circle cx="62" cy="47" r="10" fill="none" stroke="#028090" stroke-width="5"/>
  <rect x="16" y="64" width="44" height="6" rx="2" fill="#065A82"/>
  <rect x="20" y="24" width="10" height="6" fill="#065A82"/>
  <rect x="38" y="24" width="10" height="6" fill="#065A82"/>
</svg>"""

SERVER = """<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">
  <rect x="20" y="14" width="56" height="20" rx="4" fill="#F4F7FA" stroke="#065A82" stroke-width="5"/>
  <rect x="20" y="38" width="56" height="20" rx="4" fill="#F4F7FA" stroke="#065A82" stroke-width="5"/>
  <rect x="20" y="62" width="56" height="20" rx="4" fill="#F4F7FA" stroke="#065A82" stroke-width="5"/>
  <circle cx="30" cy="24" r="4" fill="#028090"/>
  <circle cx="30" cy="48" r="4" fill="#028090"/>
  <circle cx="30" cy="72" r="4" fill="#028090"/>
  <rect x="44" y="21" width="24" height="6" rx="3" fill="#1C7293"/>
  <rect x="44" y="45" width="24" height="6" rx="3" fill="#1C7293"/>
  <rect x="44" y="69" width="24" height="6" rx="3" fill="#1C7293"/>
</svg>"""

CLOUD = """<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">
  <path d="M28 62 a14 14 0 0 1 2-27.8 a18 18 0 0 1 34.6-4.7 a13 13 0 0 1 5.4 25.1 a11 11 0 0 1-4 7.4 Z"
        fill="#FEF5E0" stroke="#F0AB00" stroke-width="5"/>
  <rect x="30" y="66" width="10" height="10" rx="2" fill="#065A82"/>
  <rect x="44" y="66" width="10" height="10" rx="2" fill="#065A82"/>
  <rect x="58" y="66" width="10" height="10" rx="2" fill="#065A82"/>
  <path d="M35 62 L35 66 M49 58 L49 66 M63 62 L63 66" stroke="#1C7293" stroke-width="4"/>
</svg>"""

if __name__ == "__main__":
    render(LAPTOP, "s33-laptop")
    render(GPU, "s33-gpu")
    render(SERVER, "s33-server")
    render(CLOUD, "s33-cloud")
