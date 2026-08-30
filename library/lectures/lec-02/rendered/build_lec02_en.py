"""
Full 35-slide build of Лекции 2 «Как работают современные большие модели» (Phase 6).

v1.8 changes (issue #156, polish pass):
- s01 hook fully replaced again: token-rainbow (too technical for a
  before-lecture slide) → human-attention hook (distracted character
  illustration) with bridge line to s13a (Раздел 3 «Механизм внимания»).
- s03: removed visible "(Лекция 1 §3.2)" §-references (forbidden scaffold).
- s07: expanded gold callout — letters (existing) + numbers/arithmetic
  tokenization consequence (GPT-4 59%/4%/0% accuracy, arXiv 2410.19730).
- s13a: title reworded ("матрица, не линейная операция" → "сверка каждого
  токена со всеми остальными" — clearer natural phrasing, same meaning).
- s24: renamed ("3 промиса Лекции 1..." → "Ответы на вопросы из начала
  лекции"), removed "Payoff Лекции 1 §5.3" gold marker (forbidden scaffold +
  §-reference), unified card badge colors (was GOLD on card 1 only —
  unintended imbalance vs cards 2-3, now MID/LIGHT/TEAL).
- s25: decision-tree redesign — fixed head-text overflow bug
  ("Интерпретируемость" wrapped into condition text), added explicit
  arrowhead connectors root→branches→else.
- s26: removed "Инженерный вывод... Лекция 1 §4.8" gold callout (forbidden
  §-reference); insight folded into right-column body text; columns grew to
  fill freed vertical space.
- s27-homework REMOVED entirely (deferred out of this deck).
- s28: no visible-body change (§-refs were already notes-only); notes cleaned.
- s29: Q&A slide redesigned to match Lec-1 s31 pattern (SURFACE background,
  "Спасибо" not "Спасибо за внимание!", contacts placeholder bottom-right).
- Deck-wide: all remaining `§[0-9]` references in visible body + speaker
  notes rewritten as natural language (frontmatter exempt).

v1.5 changes (Phase 8.8, 2026-05-14):
- s01 hook redesign: strawberry test removed (top LLMs pass it in 2026);
  replaced with token rainbow on 3 examples (EN/RU/code) showing one-meaning
  different-token-cost. Beautiful 2026-evergreen visualization.
- s05: removed «Подумайте 15 сек» retrieval moment, replaced with forward
  reference to cross-language cost (s08).
- s06: added BPE-compromise explanatory line («не из всех слов и не из
  всех букв — а из частых подпоследовательностей»).
- s10 redesign: heatmap + 2D PCA scatter side-by-side (vector illustration
  per user feedback; cosine note moved to gold callout).
- s11 REMOVED: «3 uses of embeddings» — deferred to Лекция 3.
- s12 REFORMULATED: now «Эмбеддинги — фундамент понимания LLM» — shows
  word→token→vector→LLM→vector→token→word reverse-flow + 3 «understanding»
  examples (paraphrases, synonyms, cross-lang).
- s04b NEW: «Поток данных в LLM» — pipeline overview placed after Раздел 1
  divider, before s05.
- s09a NEW: «Пространство эмбеддингов» — concept slide between s09 and s10,
  explaining dimensions, learning, projection.
- s13a NEW: «Внимание — это матрица» — 7×7 heatmap example, placed between
  s13 divider and s14, emphasizing matrix nature + multi-head + cost.
- Added stock illustrations across deck (Lucide icons): focus, languages,
  globe-2, sparkles, eye, code-2, etc.
- Slide count: 33 → 35 (28 original − 1 s11 + 4 dividers + 1 s02a + 3 new).

v1.4 changes (Phase 8.7, 2026-05-13):
- Added s02a lecture-map slide (между s02 cover и s03 recap) — mirrors Lec-1
  s02a pattern: 6 horizontal nav cards, Раздел 0 gold-outlined, без минут.
- Removed bottom roadmap_bar from s02 cover — cover остаётся clean (title +
  lecture number + subtitle + pictogram). Карта уехала на отдельный s02a.
- Total slides: 32 → 33.

v1.3 changes (Phase 8.6, 2026-05-13):
- Removed top_nav_bar from all content slides (per Lec-1 pattern: navigation
  only on section_divider slides via bottom roadmap_bar, not on content).
- Added 4 new section dividers (s04a/s08a/s17a/s22a) mirroring s13 pattern —
  large «Раздел N» (140pt gold) + sub-title + frame phrase + bottom roadmap.
- Increased vertical fill on compressed slides (s09, s11, s14, s15, s17, s19,
  s21, s24, s25, s26, s28) — body content occupies ≥60% canvas height.

Source-of-truth: deck.yaml v1.1 + chapter v1.1 (status=reviewed) +
slides/*.md (32 файлов с readable speaker notes 150-300 слов).

Pipeline pattern проверен на Лекции 1 v3.x — python-pptx direct
(вместо PowerPoint MCP) для масштаба 32 slides.

Palette: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal #028090
secondary + Gold #F0AB00 highlight (≥1× per slide).

Visual motif: «Ocean rounded box» (radius 12, surface #F4F7FA,
stroke #1C7293, padding 16pt) на каждом content slide.

Canvas: 13.333" × 7.5" (16:9). Pacing: 55 active + 8 retrieval +
7 transitions + 5 Q&A = 75 min.
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from lxml import etree

# === Palette (LOCKED v1, mirrored from deck.yaml) ===
DEEP    = RGBColor(0x21, 0x29, 0x5C)
MID     = RGBColor(0x06, 0x5A, 0x82)
LIGHT   = RGBColor(0x1C, 0x72, 0x93)
TEAL    = RGBColor(0x02, 0x80, 0x90)
SURFACE = RGBColor(0xF4, 0xF7, 0xFA)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GOLD    = RGBColor(0xF0, 0xAB, 0x00)
SLATE   = RGBColor(0x6B, 0x76, 0x85)
COVER_OUTLINE = RGBColor(0xD9, 0xE2, 0xEC)
GOLD_TINT = RGBColor(0xFE, 0xF5, 0xE0)
TEAL_TINT = RGBColor(0xE6, 0xF2, 0xF4)
SOFT_GREY = RGBColor(0xE5, 0xEA, 0xF0)
DARK_GREY = RGBColor(0x4A, 0x55, 0x6B)
SLATE_PN  = RGBColor(0x5B, 0x66, 0x78)   # page-number muted ink

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "rendered/assets"
# EN-localized diagram/illustration assets (translated <text>); charts + icons
# stay shared with the RU deck. See report note: chart PNGs remain RU (no SVG
# source, QuickChart unreachable in this environment).
ASSETS_EN = ROOT / "rendered/assets-en"
SLIDES_DIR = ROOT / "slides-en"
OUT = ROOT / "rendered/lec-02-en.pptx"
FONT_HEAD = "Arial"
FONT_BODY = "Arial"
FONT_MONO = "Liberation Mono"


# ============================================================
# Helpers
# ============================================================
def setup_pres():
    p = Presentation()
    p.slide_width = Inches(SLIDE_W_IN)
    p.slide_height = Inches(SLIDE_H_IN)
    return p


def blank(p):
    return p.slides.add_slide(p.slide_layouts[6])


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def disable_shadow(shp):
    sppr = shp._element.spPr
    for el in sppr.findall("{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, "{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst")


def text_box(slide, x, y, w, h, text, *,
             size=16, bold=False, italic=False, color=DEEP,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             font=FONT_BODY, line_spacing=1.15):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    r = p.add_run()
    r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    shrink_refs_in_frame(tf)
    return tb


def text_runs(slide, x, y, w, h, runs, *,
              align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
              line_spacing=1.15, font=FONT_BODY):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for cfg in runs:
        if cfg.get("newpara"):
            p = tf.add_paragraph()
            p.alignment = cfg.get("align", align)
            p.line_spacing = cfg.get("line_spacing", line_spacing)
        r = p.add_run()
        r.text = cfg["text"]
        r.font.name = cfg.get("font", font)
        r.font.size = Pt(cfg.get("size", 16))
        r.font.bold = cfg.get("bold", False)
        r.font.italic = cfg.get("italic", False)
        r.font.color.rgb = cfg.get("color", DEEP)
    shrink_refs_in_frame(tf)
    return tb


def ocean_box(slide, x, y, w, h, *, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5,
              radius_pt=12.0):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        adj = max(0.04, min(0.25, (radius_pt / 72.0) / max(min(w, h) / 2.0, 0.5)))
        shp.adjustments[0] = adj
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke; shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def filled_rect(slide, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0, radius=False, radius_adj=0.16):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    if radius:
        try:
            shp.adjustments[0] = radius_adj
        except Exception:
            pass
    disable_shadow(shp)
    return shp


def chip(slide, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE, size=14, bold=True):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    try:
        shp.adjustments[0] = 0.5
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(1.2)
    tf = shp.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.04); tf.margin_bottom = Inches(0.04)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.name = FONT_BODY; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    disable_shadow(shp)
    return shp


def add_image(slide, path, x, y, w=None, h=None):
    """Add a picture. Passing BOTH w and h stretches non-proportionally
    (see notes/mcp-limitations.md #73-render-1) — prefer only one of
    w/h to let python-pptx preserve the native aspect ratio.

    Bug fix (issue #156): height-only calls used to fall through to the
    "neither" branch (native image size, ignoring h entirely) because only
    a width-only branch existed. Added explicit height-only branch.
    """
    if not Path(path).exists():
        return
    if w is not None and h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
    elif h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), height=Inches(h))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def slide_title(slide, text, *, y=0.55, h=1.05, w=12.3, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.18, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=1.2,
                radius=True, radius_adj=0.12)
    text_box(slide, x=x + 0.2, y=y + 0.08, w=w - 0.4, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.25)


def teal_callout(slide, x, y, w, h, text, *, size=14, bold=False):
    filled_rect(slide, x, y, w, h, TEAL_TINT, stroke=TEAL, stroke_pt=1.0,
                radius=True, radius_adj=0.12)
    text_box(slide, x=x + 0.18, y=y + 0.08, w=w - 0.36, h=h - 0.16, text=text,
             size=size, bold=bold, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.LEFT, line_spacing=1.25)


def right_arrow(slide, x, y, w=0.6, h=0.4, fill=MID):
    """Render MSO_SHAPE.RIGHT_ARROW between stages."""
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    disable_shadow(shp)
    return shp


def speaker_notes(slide, text):
    """Write notes as readable PARAGRAPHS: blank-line-separated blocks each
    become one notes-paragraph, single newlines inside a block collapse to
    spaces. An «Источники:» block keeps its hard line-breaks (one [N] per
    line). Mirrors lec-04 _helpers.speaker_notes so the notes-PDF renders the
    source list cleanly."""
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    blocks = [b.strip() for b in re.split(r'\n\s*\n', text.strip()) if b.strip()]
    if not blocks:
        blocks = [""]
    for i, block in enumerate(blocks):
        if block.lstrip().startswith("Sources:"):
            lines = [ln.rstrip() for ln in block.split("\n")]
            para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            para.text = lines[0]
            for ln in lines[1:]:
                sub = tf.add_paragraph()
                sub.text = ln
            continue
        one = re.sub(r'\s*\n\s*', ' ', block)
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = one


# ============================================================
# Speaker notes loader from md
# ============================================================
def load_notes(slide_id):
    """Extract Speaker notes block from slide markdown."""
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding='utf-8')
    notes_match = re.search(r'## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)', md, re.DOTALL)
    notes = notes_match.group(1).strip() if notes_match else ""
    notes = re.sub(r'\n+---\s*$', '', notes)
    return notes.strip()


# ============================================================
# Reference system (ported from lec-04 _helpers.py) — issue #170:
# small superscript muted [N] markers at claims + a bottom clickable
# numbered source list. URLs come ONLY from the Лекция-2 reference registry
# (notes/research/lecture-2/reference-registry.md). Volatile sources carry
# [VFY-day-of] in the speaker-notes «Источники:» block only.
# ============================================================
URLS = {
    # --- Канонические первичные статьи (verified 2026-08-30, exact author+title) ---
    "vaswani": "https://arxiv.org/abs/1706.03762",
    "sennrich_bpe": "https://arxiv.org/abs/1508.07909",
    "mikolov_w2v": "https://arxiv.org/abs/1301.3781",
    "holtzman_topp": "https://arxiv.org/abs/1904.09751",
    "liu_lost_middle": "https://arxiv.org/abs/2307.03172",
    "lewis_rag": "https://arxiv.org/abs/2005.11401",
    "yao_react": "https://arxiv.org/abs/2210.03629",
    "counting_tok": "https://arxiv.org/abs/2410.19730",
    # --- Vendor / tooling docs ---
    "tiktoken": "https://github.com/openai/tiktoken",
    "openai_embeddings": "https://platform.openai.com/docs/guides/embeddings",
    "mcp": "https://www.anthropic.com/news/model-context-protocol",
    "hf_playground": "https://huggingface.co/playground",
    "mistral_7b": "https://mistral.ai/news/announcing-mistral-7b",
    # --- Книги / общеучебные ---
    "pearl_why": "http://bayes.cs.ucla.edu/WHY/",
}

# SLIDE_REFS entry: (num, short_name, urlkey, gloss[, volatile])
# gloss = one phrase: what the source says / why authoritative.
# volatile → «[VFY-day-of]» appended in notes only.
SLIDE_REFS = {
    "s06": [
        ("1", "Sennrich et al. (2016) — NMT of Rare Words / BPE", "sennrich_bpe",
         "BPE is a compromise: a vocabulary of frequent subsequences, not letters and not words"),
    ],
    "s07": [
        ("1", "Counting Ability of LLMs & Impact of Tokenization (2024)", "counting_tok",
         "GPT-4 without a calculator: 59%/4%/0% on 3-/4-/5-digit multiplication — the same tokenizer-cut mechanism",
         True),
    ],
    "s09": [
        ("1", "OpenAI — Embeddings API", "openai_embeddings",
         "public embeddings: text-embedding-3-small 1536, large 3072 dimensions",
         True),
        ("2", "Mikolov et al. (2013) — word2vec", "mikolov_w2v",
         "historical context: geometric closeness = closeness in meaning"),
    ],
    "s10": [
        ("1", "reproducible: all-MiniLM-L6-v2 / text-embedding-3-small",
         "openai_embeddings",
         "numbers are illustrative; cosine closeness is usage statistics, not a semantic dictionary",
         True),
    ],
    "s12": [
        ("1", "Lewis et al. (2020) — RAG", "lewis_rag",
         "an embedding captures meaning, not the string: the basis of semantic search / RAG"),
    ],
    "s14": [
        ("1", "Vaswani et al. (2017) — Attention Is All You Need", "vaswani",
         "attention outputs a weight distribution over context tokens (Sigma=1); 32-128 heads per layer"),
    ],
    "s16": [
        ("1", "Anthropic — context window of the Claude models", "mcp",
         "window growth 4k->200k->1M; the order of magnitude matters more than the exact figure", True),
    ],
    "s17": [
        ("1", "Liu et al. (2023) — Lost in the Middle", "liu_lost_middle",
         "U-shape: accuracy dips in the middle of the window; put what matters at the start/end of the prompt"),
    ],
    "s19": [
        ("1", "Holtzman et al. (2019) — nucleus sampling (top-p)", "holtzman_topp",
         "temperature and top-p control the shape of the distribution during sampling"),
    ],
    "s22": [
        ("1", "Mistral AI — Mistral 7B", "mistral_7b",
         "local open-weight models 1-13B vs cloud 200B+", True),
    ],
    "s26": [
        ("1", "Pearl (2018) — The Book of Why", "pearl_why",
         "attention captures association, not causality (3 rungs of the causal ladder)"),
    ],
    "s27": [
        ("1", "Hugging Face — Inference Playground", "hf_playground",
         "homework: observe the effect of temperature; fallback Together.ai / Ollama",
         True),
    ],
    "s28": [
        ("1", "Lewis et al. (2020) — RAG", "lewis_rag",
         "how AI goes beyond the chat: retrieval-augmented generation"),
        ("2", "Anthropic — Model Context Protocol (Nov 25, 2024)", "mcp",
         "an open standard for connecting tools to an LLM"),
        ("3", "Yao et al. (2022) — ReAct", "yao_react",
         "agent loop: act -> observe -> reflect", True),
    ],
}

_AMAIN = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
_REF_RE = re.compile(r'\[\d+(?:\s*[,–—-]\s*\d+)*\]')


def _run_props(src_run):
    f = src_run.font
    sz = f.size
    return {
        "name": f.name,
        "size_pt": (sz.pt if sz is not None else None),
        "bold": f.bold,
        "italic": f.italic,
        "color": (f.color.rgb if (f.color and f.color.type is not None) else None),
    }


def _clone_run_after(anchor_r, props, text, *, ref=False,
                     ref_frac=0.52, ref_color=LIGHT):
    new_r = etree.SubElement(anchor_r.getparent(), _AMAIN + "r")
    anchor_r.addnext(new_r)
    rpr = etree.SubElement(new_r, _AMAIN + "rPr")
    base = props["size_pt"] or 16.0
    if ref:
        rpr.set("sz", str(int(round(base * ref_frac * 100))))
        rpr.set("baseline", "30000")
        rpr.set("b", "0")
        rpr.set("i", "1")
    else:
        if props["size_pt"] is not None:
            rpr.set("sz", str(int(round(base * 100))))
        if props["bold"] is not None:
            rpr.set("b", "1" if props["bold"] else "0")
        if props["italic"] is not None:
            rpr.set("i", "1" if props["italic"] else "0")
    if props["name"]:
        for tag in ("latin", "cs", "ea"):
            el = etree.SubElement(rpr, _AMAIN + tag)
            el.set("typeface", props["name"])
    col = ref_color if ref else props["color"]
    if col is not None:
        fill = etree.SubElement(rpr, _AMAIN + "solidFill")
        clr = etree.SubElement(fill, _AMAIN + "srgbClr")
        clr.set("val", str(col))
    t = etree.SubElement(new_r, _AMAIN + "t")
    t.text = text
    return new_r


def shrink_refs_in_frame(text_frame, *, ref_frac=0.52, ref_color=LIGHT):
    """Split every [N] marker inside the frame into a small superscript muted
    run. Non-destructive to surrounding text formatting. Applied automatically
    by text_box / text_runs so baked-in [N] markers shrink without rewriting
    every call site."""
    for para in text_frame.paragraphs:
        for run in list(para.runs):
            txt = run.text
            if not txt or "[" not in txt:
                continue
            matches = list(_REF_RE.finditer(txt))
            if not matches:
                continue
            props = _run_props(run)
            run.text = txt[:matches[0].start()]
            anchor = run._r
            for i, m in enumerate(matches):
                anchor = _clone_run_after(anchor, props, m.group(),
                                          ref=True, ref_frac=ref_frac,
                                          ref_color=ref_color)
                nxt = matches[i + 1].start() if i + 1 < len(matches) else len(txt)
                between = txt[m.end():nxt]
                if between:
                    anchor = _clone_run_after(anchor, props, between, ref=False)
    return text_frame


def ref_list(slide, entries, *, y=7.10, x=0.55, w=12.3, h=0.34,
             size=8.5, color=LIGHT, line_spacing=1.02):
    """Bottom numbered clickable source list. entries: (num, name, url).
    Renders «[N] name» where name is a clickable hyperlink. Muted, italic,
    small — reads as attribution, never a text-wall. Kept to 1 visual line;
    entries separated by «   ·   »."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    p.line_spacing = line_spacing
    for i, (num, name, url) in enumerate(entries):
        rm = p.add_run()
        rm.text = f"[{num}] "
        rm.font.name = FONT_BODY; rm.font.size = Pt(size)
        rm.font.bold = True; rm.font.italic = True
        rm.font.color.rgb = MID
        rn = p.add_run()
        rn.text = name
        rn.font.name = FONT_BODY; rn.font.size = Pt(size)
        rn.font.italic = True
        rn.font.color.rgb = color
        if url:
            try:
                rn.hyperlink.address = url
            except Exception:
                pass
        if i < len(entries) - 1:
            rs = p.add_run()
            rs.text = "   ·   "
            rs.font.name = FONT_BODY; rs.font.size = Pt(size)
            rs.font.italic = True
            rs.font.color.rgb = color
    return tb


def link_run(paragraph, text, url, *, size=11, color=MID, bold=False,
             italic=False, font=FONT_BODY):
    """Add a single clickable run to an existing paragraph."""
    r = paragraph.add_run()
    r.text = text
    r.font.name = font; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    if url:
        try:
            r.hyperlink.address = url
        except Exception:
            pass
    return r


def _resolve_refs(sid):
    out = []
    for entry in SLIDE_REFS.get(sid, []):
        num, name, urlkey, gloss = entry[0], entry[1], entry[2], entry[3]
        volatile = len(entry) > 4 and entry[4]
        out.append((num, name, URLS.get(urlkey, ""), gloss, volatile))
    return out


def refs_of_slide(slide, sid, *, y=7.12, size=8.5):
    """Bottom clickable [N] list for a display slide, sourced from SLIDE_REFS.
    Skips silently if the slide has no registry entry."""
    resolved = _resolve_refs(sid)
    if not resolved:
        return None
    entries = [(num, name, url) for (num, name, url, gloss, vol) in resolved]
    sz = size if len(entries) <= 2 else 8.0
    return ref_list(slide, entries, y=y, size=sz)


def notes_sources_block(sid):
    """Build the «Источники:» block for the speaker notes: numbered [N] +
    FULL URL + one gloss phrase; volatile → [VFY-day-of]."""
    resolved = _resolve_refs(sid)
    if not resolved:
        return ""
    lines = ["Sources:"]
    for (num, name, url, gloss, vol) in resolved:
        vfy = " [VFY-day-of]" if vol else ""
        lines.append(f"[{num}] {name} — {gloss}. {url}{vfy}")
    return "\n".join(lines)


def _attach_notes_ref(body, sid):
    """Tie the visible [N] markers into the notes narrative: if the notes text
    already names the source in author-year form but has no [N] marker yet,
    append the numbered «Источники:» block. Notes narratives are already
    connected — we only add the numbered source list at the end (per task 2)."""
    block = notes_sources_block(sid)
    return f"{body}\n\n{block}" if block else body


def notes_with_sources(slide, sid):
    """Write speaker notes (paragraph-formatted) with the «Источники:» block
    appended. Single call replaces speaker_notes(slide, load_notes(sid))."""
    speaker_notes(slide, _attach_notes_ref(load_notes(sid), sid))


def page_number(slide, n, total=None, *, color=SLATE_PN):
    """Small muted page-number stamp in the bottom-right corner («N / TOTAL»),
    10pt italic, so it never overlaps the left-aligned ref-list (x=0.55) nor
    the roadmap bar. Applied to every slide by main() so all slides carry it
    without touching per-slide builders."""
    txt = f"{n} / {total}" if total else str(n)
    tb = slide.shapes.add_textbox(Inches(12.33), Inches(7.16), Inches(0.95),
                                  Inches(0.28))
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    p.line_spacing = 1.0
    r = p.add_run()
    r.text = txt
    r.font.name = FONT_BODY
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = color
    return tb


# ============================================================
# Roadmap bar (used by cover s02 + divider s13)
# ============================================================
def roadmap_bar(slide, here_idx, *, y=6.7):
    """6-section roadmap bar at bottom of slide.
    Sections: 0 Введение / 1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал.
    here_idx: 0..5 — gold highlight on current.
    """
    bar_h = 0.45
    n_cells = 6
    total_w = 12.3
    gap = 0.08
    cell_w = (total_w - gap * (n_cells - 1)) / n_cells
    start_x = 0.55
    labels = [
        "0  Intro",
        "1  Tokens",
        "2  Embeddings",
        "3  Attention",
        "4  Sampling",
        "5  Wrap-up",
    ]
    for i, label in enumerate(labels):
        x = start_x + i * (cell_w + gap)
        is_here = (i == here_idx)
        fill = GOLD if is_here else SOFT_GREY
        text_color = DEEP if is_here else SLATE
        filled_rect(slide, x, y, cell_w, bar_h, fill, radius=True, radius_adj=0.30)
        text_box(slide, x=x, y=y + 0.08, w=cell_w, h=bar_h - 0.16,
                 text=label, size=11, bold=is_here, color=text_color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


# ============================================================
# Lecture-map nav (used by s02a) — 6 horizontal cards, Lec-1 pattern.
# ============================================================
NAV_SECTIONS_LEC2 = [
    # (num, title, short description). Used in `nav_slide` below.
    ("0", "Introduction", "What a token is +\nthe central question"),
    ("1", "Tokenization", "How the model sees\nyour text"),
    ("2", "Embeddings",   "The space\nof meanings"),
    ("3", "Attention",    "What matters\nnow"),
    ("4", "Sampling",     "From distribution\nto token"),
    ("5", "Wrap-up",      "Closing,\nbridge to Lec 3"),
]


def nav_slide(slide, here_idx, title, frame_phrase=None):
    """Lecture-map navigation slide (s02a) — 6 horizontal cards.

    Mirrors Lec-1 s02a layout: title top-center, 6 equal-width cards in a row,
    active card (here_idx) gold-outlined (not filled — overview state per
    Lec-1 Fix-17 logic; map slide is not a section divider).

    here_idx     — 0..5, gold-outlined card index (Раздел 0 by default for s02a).
    title        — slide title (centered, top).
    frame_phrase — optional 1-line italic frame under title.
    """
    set_slide_bg(slide, SURFACE)
    # Title at top
    text_box(slide, x=0.55, y=0.45, w=12.25, h=0.95, text=title,
             size=30, bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.15)
    if frame_phrase:
        text_box(slide, x=0.55, y=1.45, w=12.25, h=0.55,
                 text=frame_phrase, size=18, italic=True, color=MID,
                 align=PP_ALIGN.CENTER, line_spacing=1.20)

    # 6 cards horizontal
    card_y = 2.55
    card_w = 1.95
    card_h = 3.2
    gap = 0.15
    start_x = (SLIDE_W_IN - (card_w * 6 + gap * 5)) / 2.0

    for i, (num, sec_title, desc) in enumerate(NAV_SECTIONS_LEC2):
        x = start_x + i * (card_w + gap)
        is_here = (i == here_idx)

        if is_here:
            # Highlighted card: gold-outlined, deep text (overview state)
            ocean_box(slide, x, card_y, card_w, card_h,
                      fill=WHITE, stroke=GOLD, stroke_pt=2.5)
            num_color = GOLD
            title_color = DEEP
            desc_color = MID
        else:
            # Normal card: white fill, light stroke
            ocean_box(slide, x, card_y, card_w, card_h,
                      fill=WHITE, stroke=LIGHT, stroke_pt=1.2)
            num_color = LIGHT if i < 2 else (MID if i < 4 else DEEP)
            title_color = DEEP
            desc_color = SLATE

        # Number — big at top
        text_box(slide, x=x, y=card_y + 0.30, w=card_w, h=0.85, text=num,
                 size=44, bold=True, color=num_color, align=PP_ALIGN.CENTER)
        # Section title — middle
        text_box(slide, x=x + 0.08, y=card_y + 1.30, w=card_w - 0.16, h=0.65,
                 text=sec_title, size=15, bold=True, color=title_color,
                 align=PP_ALIGN.CENTER, line_spacing=1.20)
        # Description — bottom (2 lines)
        text_box(slide, x=x + 0.08, y=card_y + 2.10, w=card_w - 0.16, h=1.00,
                 text=desc, size=11, italic=True, color=desc_color,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)


# ============================================================
# Top progress bar — DEPRECATED in v1.3 (Phase 8.6).
# Per Lec-1 nav pattern, top progress bar was removed from all content slides.
# Navigation now appears ONLY on section_divider slides via roadmap_bar at bottom
# (s02 cover, s04a/s08a/s13/s17a/s22a dividers).
# Function `top_nav_bar` kept below for backward-compat — not invoked anywhere.
# ============================================================
SECTION_OF_SLIDE = {
    # slide_idx (1-based) → section index 0..5 (DEPRECATED, not consulted)
    1: 0, 2: 0, 3: 0, 4: 0,
    5: 1, 6: 1, 7: 1, 8: 1,
    9: 2, 10: 2, 11: 2, 12: 2,
    13: 3,
    14: 3, 15: 3, 16: 3, 17: 3,
    18: 4, 19: 4, 20: 4, 21: 4, 22: 4,
    23: 5, 24: 5, 25: 5, 26: 5, 27: 5, 28: 5, 29: 5,
}

SECTION_LABELS = [
    "0  Intro",
    "1  Tokens",
    "2  Embeddings",
    "3  Attention",
    "4  Sampling",
    "5  Wrap-up",
]


def top_nav_bar(slide, here_idx):
    """Slim 6-cell progress bar at very top of content slide.
    Shows section position, gold highlight on current section. Height 0.22".
    """
    y = 0.08
    bar_h = 0.22
    n_cells = 6
    total_w = 12.3
    gap = 0.06
    cell_w = (total_w - gap * (n_cells - 1)) / n_cells
    start_x = 0.55
    for i, label in enumerate(SECTION_LABELS):
        x = start_x + i * (cell_w + gap)
        is_here = (i == here_idx)
        fill = GOLD if is_here else SOFT_GREY
        text_color = DEEP if is_here else SLATE
        filled_rect(slide, x, y, cell_w, bar_h, fill, radius=True, radius_adj=0.40)
        text_box(slide, x=x, y=y + 0.025, w=cell_w, h=bar_h - 0.05,
                 text=label, size=9, bold=is_here, color=text_color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


# ============================================================
# Slide builders
# ============================================================
def build_s01(p):
    """Opening hook — human attention, distracted character (v1.8, issue #156).

    Replaces v1.5 token-rainbow hook (too technical for a "before-lecture"
    slide). Owner feedback: simple, friendly, relatable — no AI jargon —
    with a bridge line to the attention mechanism (s13a) in Раздел 3.
    Variant B (primary recommendation): "чего вы НЕ замечаете прямо сейчас".
    """
    s = blank(p)

    # Headline — question, center
    text_box(s, x=0.55, y=0.45, w=12.3, h=1.05,
             text="As you read this sentence — what are you NOT paying attention to?",
             size=28, bold=True, color=DEEP, line_spacing=1.15,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Sub-line italic teal
    text_box(s, x=0.55, y=1.55, w=12.3, h=0.45,
             text="Every second your brain chooses what matters and what is background.",
             size=17, italic=True, color=TEAL, line_spacing=1.20,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Main visual — Ocean rounded box framing the character illustration
    # Illustration is 900x700 px (ratio 1.286); constrain by height to
    # preserve aspect ratio (see notes/mcp-limitations.md #73-render-1).
    # Resulting width at h=3.75 = 3.75*(900/700) = 4.82" — centered in box.
    box_x, box_y, box_w, box_h = 3.55, 2.15, 6.2, 4.20
    ocean_box(s, box_x, box_y, box_w, box_h)
    img_h = 3.75
    img_w = img_h * (900 / 700)
    add_image(s, ASSETS_EN / "illustrations/s01-attention-character.png",
              x=box_x + (box_w - img_w) / 2, y=box_y + 0.22, h=img_h)

    # Bridge line at bottom — small italic
    text_box(s, x=0.55, y=6.65, w=12.3, h=0.55,
             text="The mechanism we take apart inside an AI model today has exactly the same name — \"attention\". "
                  "It works in a similar spirit — but not the way yours does.",
             size=13, italic=True, color=LIGHT, line_spacing=1.25, align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s01"))


def build_s02(p):
    """Cover — clean: title + lecture number + subtitle + pictogram.

    v1.4 (Phase 8.7): removed bottom roadmap_bar — карта уехала на отдельный
    s02a slide per user feedback round 3.
    """
    s = blank(p)
    set_slide_bg(s, SURFACE)
    # Big "02" outline gold (decorative) — single digit "2" to fit
    text_box(s, x=9.5, y=0.2, w=4.0, h=5.0, text="2",
             size=420, bold=True, color=COVER_OUTLINE,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0)
    # ЛЕКЦИЯ tag
    text_box(s, x=0.7, y=1.0, w=8.0, h=0.55, text="LECTURE 2",
             size=18, bold=True, color=TEAL, align=PP_ALIGN.LEFT)
    filled_rect(s, 0.72, 1.55, 0.7, 0.05, fill=TEAL)
    # Title — line break tuned semantically (2 lines balanced)
    text_box(s, x=0.7, y=2.0, w=10.5, h=2.6,
             text="How modern large\nmodels work",
             size=48, bold=True, color=DEEP, line_spacing=1.08, align=PP_ALIGN.LEFT)
    # Subtitle / promise
    filled_rect(s, 0.7, 5.0, 0.05, 0.55, fill=TEAL)
    text_box(s, x=0.95, y=5.0, w=11.5, h=0.7,
             text="4 inference stages: tokenization · embedding · attention · sampling",
             size=20, color=MID, italic=False, align=PP_ALIGN.LEFT, line_spacing=1.25)
    # Hero pipeline icon — 4-stage simple visualization
    pipe_y = 5.85
    pipe_x = 0.95
    stages = ["Tk", "Em", "At", "Sm"]
    for i, label in enumerate(stages):
        cx = pipe_x + i * 0.85
        filled_rect(s, cx, pipe_y, 0.55, 0.55, MID, radius=True, radius_adj=0.5)
        text_box(s, x=cx, y=pipe_y + 0.05, w=0.55, h=0.45, text=label,
                 size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < 3:
            text_box(s, x=cx + 0.55, y=pipe_y + 0.05, w=0.30, h=0.45, text="→",
                     size=20, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # v1.4: roadmap_bar removed — карта переехала на s02a.
    speaker_notes(s, load_notes("s02"))


def build_s02a(p):
    """Lecture map — 6 horizontal cards, Раздел 0 gold-outlined.

    v1.4 (Phase 8.7): new slide между s02 cover и s03 recap, mirrors Lec-1
    s02a pattern. Без минут — общая карта маршрута лекции.
    """
    s = blank(p)
    nav_slide(s, here_idx=0,
              title="Lecture map — 6 sections",
              frame_phrase=None)
    speaker_notes(s, load_notes("s02a"))


def build_s03(p):
    """Recap Lec-1 — 4 layers with model highlighted."""
    s = blank(p)
    slide_title(s, "Today we zoom into the \"model\" layer of Lecture 1's four layers", size=26)

    # Left: 4 nested layers (bottom-aligned)
    cx = 0.55
    cy_base = 6.5  # bottom row baseline
    cw_start = 5.5
    ch_unit = 0.65
    # Layer 4 (top — smallest): Приложение
    # Layer 3: Агент
    # Layer 2: Чат
    # Layer 1 (bottom — largest): Модель (gold highlight)
    layers = [
        ("Application", 4.5, 1.05),
        ("Agent",       5.0, 1.7),
        ("Chat",         5.5, 2.35),
        ("Model",      6.0, 3.0),  # bottom, biggest
    ]
    # Render bottom layer (model) first then stack up
    # Model — gold highlight
    base_y = 5.85
    w, h_top = 6.0, 1.0
    ocean_box(s, cx, base_y, w, h_top, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
    text_box(s, x=cx, y=base_y + 0.30, w=w, h=0.5, text="MODEL — we zoom in today",
             size=18, bold=True, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Чат
    chat_y = base_y - 1.0
    ocean_box(s, cx + 0.3, chat_y, w - 0.6, 0.95, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=cx + 0.3, y=chat_y + 0.25, w=w - 0.6, h=0.5, text="Chat",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Агент
    agent_y = chat_y - 0.95
    ocean_box(s, cx + 0.6, agent_y, w - 1.2, 0.90, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=cx + 0.6, y=agent_y + 0.22, w=w - 1.2, h=0.5, text="Agent",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Приложение
    app_y = agent_y - 0.90
    ocean_box(s, cx + 0.9, app_y, w - 1.8, 0.85, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=cx + 0.9, y=app_y + 0.20, w=w - 1.8, h=0.5, text="Application",
             size=16, bold=True, color=MID, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=cx, y=app_y - 0.45, w=w, h=0.4,
             text="(from Lecture 1)",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Right: bridge
    rx = 6.95
    rw = 6.0
    # What we know
    ocean_box(s, rx, 1.85, rw, 2.2)
    text_box(s, x=rx + 0.25, y=2.0, w=rw - 0.5, h=0.5,
             text="What we know:",
             size=15, bold=True, color=MID)
    text_box(s, x=rx + 0.25, y=2.55, w=rw - 0.5, h=1.4,
             text="Model = stateless inference. Input is data, output is a prediction. No memory between calls.",
             size=15, color=DEEP, line_spacing=1.3)

    # What we'll learn
    ocean_box(s, rx, 4.3, rw, 2.4, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=rx + 0.25, y=4.45, w=rw - 0.5, h=0.5,
             text="What we learn today:",
             size=15, bold=True, color=DEEP)
    text_box(s, x=rx + 0.25, y=5.0, w=rw - 0.5, h=1.6,
             text="What's inside inference. 4 stages:\ntokenization -> embedding -> attention -> sampling",
             size=15, bold=False, color=DEEP, line_spacing=1.4)

    speaker_notes(s, load_notes("s03"))


def build_s04(p):
    """Central question + 3 promises."""
    s = blank(p)
    # Slide title small at top
    text_box(s, x=0.55, y=0.50, w=12.3, h=0.4,
             text="The central question of the lecture",
             size=18, bold=True, color=MID, align=PP_ALIGN.LEFT)
    # Central question — big, ocean box (semantic line break before «и» / after dash)
    ocean_box(s, 0.55, 1.05, 12.3, 1.95)
    text_box(s, x=1.0, y=1.20, w=11.4, h=1.65,
             text='"What happens inside an LLM between my request and its answer -\nand which of these mechanisms change how I use it?"',
             size=24, bold=True, color=DEEP, italic=False,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.3)

    # Gold-маркер
    filled_rect(s, 4.4, 3.25, 4.5, 0.45, GOLD_TINT, stroke=GOLD, stroke_pt=1.0, radius=True, radius_adj=0.5)
    text_box(s, x=4.4, y=3.30, w=4.5, h=0.35,
             text="3 answers — the wrap-up of the lecture",
             size=13, bold=True, color=DEEP, italic=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # 3 promise boxes
    card_y = 3.95
    card_h = 2.85
    card_w = 3.95
    gap = 0.20
    start_x = 0.55
    promises = [
        ("1", "Why does a prompt with a role\nwork better than an empty one?", "Section 3 — attention"),
        ("2", "Why is AI bad at\ncounting letters?", "Section 1 — tokenization"),
        ("3", "Why does one request\ngive different answers?", "Section 4 — sampling"),
    ]
    for i, (n, q, dest) in enumerate(promises):
        x = start_x + i * (card_w + gap)
        ocean_box(s, x, card_y, card_w, card_h)
        # Number badge — top-left
        filled_rect(s, x + 0.3, card_y + 0.3, 0.7, 0.7, MID, radius=True, radius_adj=0.5)
        text_box(s, x=x + 0.3, y=card_y + 0.32, w=0.7, h=0.65,
                 text=n, size=28, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Question — full width, below the badge (avoids narrow wrapping)
        text_box(s, x=x + 0.25, y=card_y + 1.20, w=card_w - 0.5, h=1.40,
                 text=q, size=18, bold=True, color=DEEP, line_spacing=1.30)
        # Arrow
        text_box(s, x=x + 0.25, y=card_y + 2.40, w=card_w - 0.5, h=0.5,
                 text="→ " + dest,
                 size=15, italic=True, color=MID, line_spacing=1.2)
    speaker_notes(s, load_notes("s04"))


def build_s05(p):
    """What is token — 3 examples + gold callout."""
    s = blank(p)
    slide_title(s, "A token is an id from the model's vocabulary. Not a letter and not a word.", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="A statistically frequent subsequence",
             size=15, italic=True, color=MID)

    # 3 example cards vertical
    ex_y = 2.05
    ex_h = 0.95
    ex_w = 12.3
    gap = 0.15
    examples = [
        ("Example 1.", "cat", ["cat"], "1 token / 1 id"),
        ("Example 2.", "tokenization", ["token", "ization"], "2 tokens"),
        ("Example 3.", "strawberry", ["st", "raw", "berry"], "3 tokens · o200k_base"),
    ]
    for i, (lbl, word, tokens, count_text) in enumerate(examples):
        y = ex_y + i * (ex_h + gap)
        ocean_box(s, 0.55, y, ex_w, ex_h)
        # Label
        text_box(s, x=0.75, y=y + 0.18, w=1.6, h=0.6,
                 text=lbl, size=14, bold=True, color=MID, anchor=MSO_ANCHOR.MIDDLE)
        # Word
        text_box(s, x=2.4, y=y + 0.18, w=2.5, h=0.6,
                 text=word, size=22, bold=True, color=DEEP,
                 font=FONT_MONO, anchor=MSO_ANCHOR.MIDDLE)
        # Arrow
        text_box(s, x=4.95, y=y + 0.18, w=0.5, h=0.6,
                 text="→", size=22, bold=True, color=MID,
                 anchor=MSO_ANCHOR.MIDDLE)
        # Token chips
        cur_x = 5.5
        token_colors = [MID, LIGHT, TEAL]
        for j, tok in enumerate(tokens):
            tw = max(0.8, len(tok) * 0.18 + 0.4)
            col = token_colors[j % len(token_colors)]
            chip(s, cur_x, y + 0.25, tw, 0.45, f"[{tok}]", fill=col, color=WHITE, size=14)
            cur_x += tw + 0.10
        # Count
        text_box(s, x=10.5, y=y + 0.18, w=1.7, h=0.6,
                 text=count_text, size=14, bold=True, color=DEEP,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout
    gold_callout(s, 0.55, 5.4, 12.3, 0.75,
                 "On average: 1 token ~ 4 characters in EN ~ 2 characters in RU",
                 size=18)

    # Caption — v1.5 (removed retrieval moment, replaced with forward link)
    text_box(s, x=0.55, y=6.35, w=12.3, h=0.45,
             text="For Russian, inference costs about twice as much — we'll return to this in 2 slides.",
             size=14, italic=True, color=LIGHT, line_spacing=1.30,
             align=PP_ALIGN.CENTER)
    speaker_notes(s, load_notes("s05"))


def build_s06(p):
    """BPE before/after — 2 columns. v1.5: added compromise phrase.

    v1.6 (issue #156 QA fix-pass, P0-2): the two italic subtitle lines had
    overlapping y-coordinates — line 1 (15pt, 12.3" wide, ~125 chars) wraps
    to 2 rendered lines needing ~0.50" at line_spacing 1.25, but its box was
    only 0.45" tall and line 2's box started just 0.47" below line 1's start
    — so line 2 rendered on top of line 1's wrapped second row (student-
    simulator: "текст нечитаем, буквы одна поверх другой"). Fix: box 1 given
    real height (0.45→0.62") to hold its 2 wrapped rows, box 2 pushed down to
    start after box 1 ends (1.92→2.12), and the two-column grid shifted down
    to match (2.40→2.50). Column height kept at 3.85" and the "After" list's
    per-item gap trimmed 0.60→0.58 so the 5th row still clears the box
    bottom (col bottom now 6.35", 0.05" clear of the y=6.4 gold callout).
    """
    s = blank(p)
    slide_title(s, "BPE — a compromise between an alphabet and a dictionary", size=26)
    # v1.5 explanatory line per user feedback #3
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.62,
             text="The vocabulary is not made of all words (like lemmatization) nor of all letters (like character-level) — but of frequent subsequences.[1]",
             size=15, italic=True, color=MID, line_spacing=1.25)
    # Sub-line 2: original technical detail
    text_box(s, x=0.55, y=2.12, w=12.3, h=0.30,
             text="The vocabulary is built once before training; at inference it is a lookup of ready-made rules.",
             size=13, italic=True, color=LIGHT)

    # Two columns — shifted down to clear the now-taller subtitle block above
    col_w = 5.5
    col_h = 3.85
    col_y = 2.50
    left_x = 1.0
    right_x = 6.8

    # Before
    ocean_box(s, left_x, col_y, col_w, col_h)
    text_box(s, x=left_x + 0.3, y=col_y + 0.2, w=col_w - 0.6, h=0.5,
             text="Before (training corpus)", size=17, bold=True, color=MID)
    before_items = ["low", "lower", "newest", "widest"]
    for i, item in enumerate(before_items):
        y_i = col_y + 0.95 + i * 0.65
        # Bullet
        filled_rect(s, left_x + 0.45, y_i + 0.25, 0.13, 0.13, MID, radius=True, radius_adj=0.5)
        text_box(s, x=left_x + 0.75, y=y_i, w=col_w - 1.0, h=0.55,
                 text=item, size=22, color=DEEP, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE)

    # Big arrow between columns — fill the gap with a proper RIGHT_ARROW shape
    arrow_gap_x = left_x + col_w + 0.05
    arrow_w = right_x - arrow_gap_x - 0.05
    right_arrow(s, arrow_gap_x, col_y + col_h / 2 - 0.30, w=arrow_w, h=0.60, fill=MID)

    # After
    ocean_box(s, right_x, col_y, col_w, col_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=right_x + 0.3, y=col_y + 0.2, w=col_w - 0.6, h=0.5,
             text="After (BPE vocabulary)", size=17, bold=True, color=DEEP)
    after_items = ["low", "er", "new", "est", "wid"]
    for i, item in enumerate(after_items):
        y_i = col_y + 0.95 + i * 0.58
        filled_rect(s, right_x + 0.45, y_i + 0.22, 0.13, 0.13, GOLD, radius=True, radius_adj=0.5)
        text_box(s, x=right_x + 0.75, y=y_i, w=col_w - 1.0, h=0.5,
                 text=item, size=22, color=DEEP, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout bottom
    gold_callout(s, 0.55, 6.4, 12.3, 0.65,
                 "The BPE vocabulary is built once before training. At inference it is a lookup of ready-made rules, not a runtime computation.",
                 size=15)
    # Clickable numbered source list (replaces the plain Sennrich caption)
    refs_of_slide(s, "s06")
    speaker_notes(s, load_notes("s06"))


def build_s07(p):
    """Strawberry — split + 3 consequences + expanded letters/numbers callout.

    v1.9 (issue #156 QA fix-pass, P0-4): title said "из 2-3 токенов" — a
    leftover from an earlier 2-token variant ([straw][berry]) that was
    already replaced everywhere else (frontmatter assertion, body,
    speaker notes all say "3 токена" for the actual o200k_base split
    [st][raw][berry]). "2-" was unsupported and inconsistent with the rest
    of the slide. Fixed to match: "из 3 токенов".
    """
    s = blank(p)
    slide_title(s, 'AI errs on "how many r-s in strawberry" — words are made of 3 tokens, not letters', size=23)

    # Left: strawberry split (image) — slightly reduced to make room for taller callout
    ocean_box(s, 0.55, 1.45, 6.2, 4.35)
    add_image(s, ASSETS_EN / "diagrams/s07-strawberry-split.png",
              x=0.75, y=1.58, w=5.8, h=4.10)

    # Right: 3 consequence cards
    rx = 7.0
    rw = 5.85
    cards = [
        ("Counting characters", "\"How many r-s in strawberry?\" — breaks systematically, non-obvious to the user."),
        ("Typos", "methodlogy ↦ different tokens than methodology. A small typo → a big shift in the answer."),
        ("Case and spaces", "cat, ` cat`, Cat, CAT — different tokens, different ids."),
    ]
    cy = 1.45
    ch = 1.35
    cgap = 0.11
    for i, (head, body) in enumerate(cards):
        y = cy + i * (ch + cgap)
        ocean_box(s, rx, y, rw, ch)
        text_box(s, x=rx + 0.25, y=y + 0.10, w=rw - 0.5, h=0.40,
                 text=head, size=17, bold=True, color=MID)
        text_box(s, x=rx + 0.25, y=y + 0.55, w=rw - 0.5, h=0.75,
                 text=body, size=14, color=DEEP, line_spacing=1.25)

    # Gold callout — expanded 2-point (letters + numbers), compact.
    # Nudged up slightly (5.95→5.86, 1.30→1.18) to clear the bottom ref-list.
    gy = 5.86
    gh = 1.18
    filled_rect(s, 0.55, gy, 12.3, gh, GOLD_TINT, stroke=GOLD, stroke_pt=1.5, radius=True, radius_adj=0.10)
    text_box(s, x=0.80, y=gy + 0.10, w=11.8, h=0.50,
             text="Letters: an external tool (Python, regex) or a character-by-character request. "
                  "Top 2026 models call code themselves instead of a single pass.",
             size=14, bold=True, color=DEEP, line_spacing=1.22)
    text_box(s, x=0.80, y=gy + 0.60, w=11.8, h=0.50,
             text="Numbers: also split unpredictably (1234->12+34, but 55688->556+88) → GPT-4: 59% accuracy on 3-digit "
                  "multiplication, 4% on 4-digit, 0% on 5-digit without a calculator.[1]",
             size=14, bold=True, color=DEEP, line_spacing=1.22)
    refs_of_slide(s, "s07")
    speaker_notes(s, load_notes("s07"))


def build_s08(p):
    """Cross-language tokens/char bar chart."""
    s = blank(p)
    slide_title(s, "The same text in Russian costs 2x more than in English", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Tokens per character — a consequence of the language mix in the training corpus",
             size=15, italic=True, color=MID)

    # Left: bar chart
    ocean_box(s, 0.55, 2.05, 7.5, 4.65)
    add_image(s, ASSETS_EN / "charts/s08-tokens-per-char.png",
              x=0.75, y=2.20, w=7.1, h=4.35)

    # Right: data table-like
    rx = 8.3
    rw = 4.55
    ocean_box(s, rx, 2.05, rw, 4.65)
    text_box(s, x=rx + 0.2, y=2.20, w=rw - 0.4, h=0.45,
             text="Rule of thumb: tokens/char",
             size=15, bold=True, color=MID)
    rows = [
        ("English", "0.25", LIGHT),
        ("Russian (gold)", "0.50", GOLD),
        ("Chinese", "0.80", LIGHT),
        ("Python code", "0.40", TEAL),
    ]
    for i, (lang, val, c) in enumerate(rows):
        ry = 2.85 + i * 0.85
        text_box(s, x=rx + 0.25, y=ry, w=rw * 0.55, h=0.45,
                 text=lang, size=14, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.55, y=ry, w=rw * 0.4, h=0.45,
                 text=val, size=18, bold=True, color=c,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout bottom
    gold_callout(s, 0.55, 6.85, 12.3, 0.55,
                 "API cost for RU ~ 2x EN. For batch — translate to EN where acceptable.",
                 size=15)
    speaker_notes(s, load_notes("s08"))


def build_s09(p):
    """What is embedding — token to vector."""
    s = blank(p)
    slide_title(s, "Each token maps to a vector — learned during training, fixed", size=24)

    # Top: token-to-vector visualization — v1.3 taller (3.6→4.1)
    ocean_box(s, 0.55, 1.55, 12.3, 4.10)
    add_image(s, ASSETS_EN / "diagrams/s09-token-to-vector.png",
              x=0.75, y=1.70, w=11.9, h=3.80)

    # Bottom: 2 callouts side-by-side. Nudged up (5.85→5.68, 1.55→1.42) to
    # clear the bottom ref-list.
    bw = 6.0
    by = 5.68
    bh = 1.42
    # Left — dimensions
    ocean_box(s, 0.55, by, bw, bh)
    text_box(s, x=0.75, y=by + 0.10, w=bw - 0.4, h=0.45,
             text="Dimensions (rule of thumb)[1]",
             size=15, bold=True, color=MID)
    rows_dim = [
        ("text-embedding-3-small", "1536 dim"),
        ("text-embedding-3-large", "3072 dim"),
        ("Internal embedding of a flagship LLM", "thousands dim"),
    ]
    for i, (name, val) in enumerate(rows_dim):
        y = by + 0.52 + i * 0.28
        text_box(s, x=0.85, y=y, w=bw * 0.65, h=0.28,
                 text=name, size=13, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=0.85 + bw * 0.62, y=y, w=bw * 0.32, h=0.28,
                 text=val, size=13, bold=True, color=TEAL,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Right — gold callout: "близость в пространстве = смысл"
    gold_callout(s, 7.0, by, bw, bh,
                 "Geometric closeness of vectors = semantic closeness of tokens.[2]\n\"cat\" is close to \"dog\" — learned from the corpus contexts.",
                 size=15)
    refs_of_slide(s, "s09")
    speaker_notes(s, load_notes("s09"))


def build_s10(p):
    """Sentence similarity — heatmap + scatter (v1.5).

    User feedback round 4 #4: add vector illustration (2D scatter projection)
    next to heatmap. Both subordinate to assertion line about близость.
    """
    s = blank(p)
    slide_title(s, "Closeness in the embedding space = semantic similarity", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="In 2026 this works at the sentence level, not only for words",
             size=15, italic=True, color=MID)

    # Left — heatmap (60% width)
    ocean_box(s, 0.55, 2.05, 7.55, 4.30)
    add_image(s, ASSETS_EN / "diagrams/s10-heatmap.png",
              x=0.70, y=2.18, w=7.25, h=4.05)

    # Right — 2D scatter (40% width)
    ocean_box(s, 8.25, 2.05, 4.65, 4.30)
    add_image(s, ASSETS_EN / "diagrams/s10-vector-scatter.png",
              x=8.35, y=2.18, w=4.45, h=4.05)

    # Gold callout — cosine definition
    gold_callout(s, 0.55, 6.50, 12.3, 0.55,
                 "Cosine similarity — a measure of the angle between vectors; range [-1, 1], closer to 1 = more similar. Numbers are illustrative.[1]",
                 size=14)

    # Clickable numbered source list (replaces the plain reproducibility caption)
    refs_of_slide(s, "s10")
    speaker_notes(s, load_notes("s10"))


def build_s12(p):
    """Эмбеддинги — фундамент понимания LLM (v1.5).

    User feedback round 4 #6: reformulate в понимание LLM, показать обратное
    преобразование из токенов в слова, добавить связь со схемой s04b.
    Previous version (Semantic vs full-text) removed — better fits Лекция 3.
    """
    s = blank(p)
    slide_title(s, "Embeddings — the foundation of LLM understanding", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.40,
             text="Inside, the model works only with vectors; words appear only at the input and the output.",
             size=15, italic=True, color=MID)

    # Layout: 2 columns
    # Left: vertical flow вход→LLM→выход (encoder side + decoder side)
    # Right: 3 example cards (what this gives "understanding")

    # ─── LEFT — vertical pipeline (explicit Y positions) ───
    lx = 0.55
    lw = 6.0
    ly = 2.00
    lh = 5.10
    ocean_box(s, lx, ly, lw, lh)
    text_box(s, x=lx + 0.10, y=ly + 0.08, w=lw - 0.20, h=0.32,
             text="Input → LLM → Output",
             size=14, bold=True, color=MID, align=PP_ALIGN.CENTER)

    # Layout constants for left pipeline
    label_x = lx + 0.20    # left side label (слова→, токены→, …)
    label_w = 1.30
    p_chip_x = lx + 1.65   # chip start x
    p_chip_w = lw - 1.85   # chip width
    p_step_h = 0.32
    p_arrow_h = 0.20

    # All steps as data — y-positions computed sequentially below
    # last_field None means "no arrow after this step"; "LLM_BOX" means special gold box
    pipeline = [
        ("words →", "\"Hello, world\"", LIGHT, 12, "↓ tokenization"),
        ("tokens →", "[Hel][lo][,][ world]", MID, 11, "↓ embedding lookup"),
        ("vectors →", "[vec₁, vec₂, vec₃, vec₄]", DEEP, 11, "LLM_BOX"),
        ("← vectors", "[vec_out]", DEEP, 11, "↓ distribution + sampling"),
        ("← tokens", "[Hel][lo]", MID, 11, "↓ de-tokenize"),
        ("← words", "\"Hello\"", LIGHT, 12, None),
    ]

    cy = ly + 0.48
    for label, chip_text, fill, csize, arrow_or_llm in pipeline:
        # Label (RIGHT-aligned to its area, sits beside the chip)
        text_box(s, x=label_x, y=cy, w=label_w, h=p_step_h,
                 text=label, size=11, italic=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
        # Chip with the actual content
        chip(s, p_chip_x, cy, p_chip_w, p_step_h, chip_text,
             fill=fill, color=WHITE, size=csize)
        cy += p_step_h + 0.02

        if arrow_or_llm == "LLM_BOX":
            # Gold LLM box, spans full pipeline width
            llm_h = 0.50
            filled_rect(s, lx + 0.40, cy, lw - 0.80, llm_h, GOLD_TINT,
                        stroke=GOLD, stroke_pt=2.0, radius=True, radius_adj=0.18)
            text_box(s, x=lx + 0.40, y=cy + 0.06, w=lw - 0.80, h=0.40,
                     text="LLM  (attention + forward — Section 3)",
                     size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE)
            cy += llm_h + 0.05
        elif arrow_or_llm is not None:
            # Mini arrow label
            text_box(s, x=p_chip_x, y=cy, w=p_chip_w, h=p_arrow_h,
                     text=arrow_or_llm, size=9, italic=True, color=MID,
                     align=PP_ALIGN.CENTER)
            cy += p_arrow_h + 0.02

    # ─── RIGHT — 3 example cards ───
    rx = 6.75
    rw = 6.15
    text_box(s, x=rx, y=ly + 0.12, w=rw, h=0.40,
             text="What gives it \"understanding\"",
             size=15, bold=True, color=MID)

    cards = [
        ("message-square-text", "Paraphrases",
         "\"How to set up SSL\" and \"Installing HTTPS\" → close vectors → the same answer."),
        ("globe-2", "Synonyms",
         "\"auto\" and \"car\" → close vectors → the same reaction."),
        ("languages", "Cross-lang",
         "\"klubnika\" (RU) and strawberry → close vectors → a correct answer in any language."),
    ]
    cy = ly + 0.60
    ch = 1.28
    cgap = 0.10
    for i, (icon, head, body) in enumerate(cards):
        y = cy + i * (ch + cgap)
        ocean_box(s, rx, y, rw, ch, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.2)
        # Icon left
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=rx + 0.15, y=y + 0.30, w=0.75, h=0.75)
        # Head
        text_box(s, x=rx + 1.05, y=y + 0.12, w=rw - 1.20, h=0.40,
                 text=head, size=16, bold=True, color=DEEP)
        # Body
        text_box(s, x=rx + 1.05, y=y + 0.55, w=rw - 1.20, h=0.75,
                 text=body, size=12, color=DEEP, line_spacing=1.30)

    # Gold callout snizu — nudged up (7.10→6.74) after tightening right cards,
    # so the bottom ref-list has a clear row.
    gold_callout(s, 0.55, 6.74, 12.3, 0.35,
                 "Sentence-level semantic similarity is the basis of an LLM \"understanding\" reformulations.[1]",
                 size=12)
    refs_of_slide(s, "s12", y=7.16)
    speaker_notes(s, load_notes("s12"))


def build_s13(p):
    """Section 3 divider — big number + roadmap."""
    s = blank(p)
    set_slide_bg(s, SURFACE)

    # Big "Раздел 3" outline gold
    text_box(s, x=0.55, y=1.30, w=12.3, h=2.5,
             text="Section 3",
             size=140, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    # Sub-title
    text_box(s, x=0.55, y=3.9, w=12.3, h=0.7,
             text="Attention mechanism",
             size=44, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Assertion
    text_box(s, x=0.55, y=4.75, w=12.3, h=0.5,
             text="How the model decides what matters now",
             size=20, italic=True, color=MID,
             align=PP_ALIGN.CENTER)
    # Roadmap-bar (here = section 3)
    roadmap_bar(s, here_idx=3)
    speaker_notes(s, load_notes("s13"))


def build_s14(p):
    """What is attention — flashlight metaphor + bar chart. v1.3 enlarged.

    v1.9 (issue #156 QA fix-pass, P1 Russification): "Attention" → "Внимание"
    in title (deck-wide anglicism cluster fix, see also s13a/s15/s16/s21/
    s24/s26). Chart title regenerated separately (see
    assets/charts/s14-attention-bars.png regen note).
    """
    s = blank(p)
    slide_title(s, "Attention outputs a weight distribution over all context tokens (sum = 1)", size=24)
    text_box(s, x=0.55, y=1.50, w=12.3, h=0.4,
             text="Which tokens matter now for predicting the next one[1]",
             size=15, italic=True, color=MID)

    # Left: bar chart distribution — DOMINANT, занимает большую часть слайда
    ocean_box(s, 0.55, 2.05, 8.5, 5.10)
    add_image(s, ASSETS_EN / "charts/s14-attention-bars.png",
              x=0.75, y=2.20, w=8.1, h=4.80)

    # Right column: 3 facts box (top) + bigger flashlight box (bottom)
    rx = 9.35
    rw = 3.55
    # 3 facts (top half)
    ocean_box(s, rx, 2.05, rw, 2.95)
    text_box(s, x=rx + 0.2, y=2.20, w=rw - 0.4, h=0.4,
             text="3 properties",
             size=16, bold=True, color=MID)
    facts = [
        "Input — all context tokens.",
        "Output — a distribution, Σ = 1.",
        "Recomputed at every step.",
    ]
    for i, f in enumerate(facts):
        y = 2.70 + i * 0.72
        # Number badge
        filled_rect(s, rx + 0.2, y + 0.05, 0.36, 0.36, MID, radius=True, radius_adj=0.5)
        text_box(s, x=rx + 0.2, y=y + 0.06, w=0.36, h=0.32,
                 text=str(i + 1), size=14, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + 0.65, y=y, w=rw - 0.85, h=0.65,
                 text=f, size=14, color=DEEP, line_spacing=1.30, anchor=MSO_ANCHOR.TOP)

    # Flashlight metaphor — v1.3 bigger box (1.50→2.10 h), bigger flashlight icon
    ocean_box(s, rx, 5.10, rw, 2.05)
    add_image(s, ASSETS_EN / "diagrams/s14-flashlight.png",
              x=rx + 0.15, y=5.20, w=1.85, h=1.85)
    text_box(s, x=rx + 2.05, y=5.25, w=rw - 2.20, h=1.70,
             text="Metaphor:\na flashlight in a dark\nroom — the model\n\"lights up\" some\ntokens brighter than others.",
             size=11, italic=True, color=DEEP, line_spacing=1.30, anchor=MSO_ANCHOR.MIDDLE)

    # Caption mid-bottom — kept (methodological note), refs on a separate row
    text_box(s, x=0.55, y=6.92, w=12.3, h=0.25,
             text="No formulas. Multi-head, Q/K/V — further reading.",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s14")
    speaker_notes(s, load_notes("s14"))


def build_s15(p):
    """Worked example + role effect (Part A + Part B).

    v1.9 (issue #156 QA fix-pass, P1 Russification): "attention" → "внимание"
    / "весах внимания" in title + body; "Worked example" section header →
    "Разбор примера" (matches deck's RU-only style elsewhere).
    """
    s = blank(p)
    slide_title(s, "Role tokens get elevated weight in the attention weights", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Part A — a worked example; Part B — the role effect (1st of 3 \"whys\")",
             size=15, italic=True, color=MID)

    # Part A — top, v1.3 enlarged (2.45→2.85)
    pa_y = 1.95
    pa_h = 2.85
    ocean_box(s, 0.55, pa_y, 12.3, pa_h)
    text_box(s, x=0.75, y=pa_y + 0.12, w=12.0, h=0.4,
             text="A. Worked example — where \"she\" looks",
             size=16, bold=True, color=MID)
    # Sentence text
    sent_y = pa_y + 0.70
    text_box(s, x=0.75, y=sent_y, w=12.0, h=0.6,
             text='"The cat ate the mouse, because she was hungry"',
             size=24, bold=True, color=DEEP, font=FONT_MONO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Three arrows from "она" → varying strength
    arrows = [("she → mouse", "thick · main weight", GOLD, 3.0),
              ("she → was", "medium", MID, 2.0),
              ("she → hungry", "thin", LIGHT, 1.2)]
    ar_y = sent_y + 0.95
    ar_w = 3.85
    ar_h = 0.60
    ar_gap = 0.15
    ar_x_start = (12.3 - (3 * ar_w + 2 * ar_gap)) / 2 + 0.55
    for i, (lbl, why, col, weight) in enumerate(arrows):
        ax = ar_x_start + i * (ar_w + ar_gap)
        # Arrow chip
        filled_rect(s, ax, ar_y, ar_w, ar_h, col, radius=True, radius_adj=0.4)
        text_box(s, x=ax, y=ar_y + 0.08, w=ar_w, h=0.45,
                 text=lbl, size=17, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=ax, y=ar_y + ar_h + 0.02, w=ar_w, h=0.30,
                 text=why, size=12, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Disclaimer
    text_box(s, x=0.75, y=pa_y + pa_h - 0.32, w=12.0, h=0.28,
             text="Simplification: a real attention map has hundreds of links. The model looks statistically, it does not do grammatical parsing.",
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # Part B — bottom, v1.3 enlarged (2.30→2.55)
    pb_y = 4.95
    pb_h = 2.45
    # Two columns side-by-side
    col_w = 6.0
    # Without role
    ocean_box(s, 0.55, pb_y, col_w, pb_h)
    text_box(s, x=0.75, y=pb_y + 0.12, w=col_w - 0.4, h=0.50,
             text="Without a role",
             size=22, bold=True, color=MID)
    text_box(s, x=0.75, y=pb_y + 0.75, w=col_w - 0.4, h=0.55,
             text='"Explain asynchrony"',
             size=18, color=DEEP, font=FONT_MONO,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.75, y=pb_y + 1.40, w=col_w - 0.4, h=0.95,
             text="→ a generic answer\n(low weight of role tokens in the attention weights)",
             size=17, italic=True, color=DEEP, line_spacing=1.32)
    # With role
    ocean_box(s, 6.85, pb_y, col_w, pb_h, fill=GOLD_TINT, stroke=GOLD)
    text_box(s, x=7.05, y=pb_y + 0.12, w=col_w - 0.4, h=0.50,
             text="With a role",
             size=22, bold=True, color=DEEP)
    text_runs(s, 7.05, pb_y + 0.75, col_w - 0.4, 0.60, [
        {"text": "\"You are ", "size": 17, "color": DEEP, "font": FONT_MONO},
        {"text": "a Python expert", "size": 17, "color": GOLD, "font": FONT_MONO, "bold": True},
        {"text": ". Explain asynchrony ", "size": 17, "color": DEEP, "font": FONT_MONO},
        {"text": "to a junior", "size": 17, "color": GOLD, "font": FONT_MONO, "bold": True},
        {"text": ".\"", "size": 17, "color": DEEP, "font": FONT_MONO},
    ], anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=7.05, y=pb_y + 1.40, w=col_w - 0.4, h=0.95,
             text="→ role tokens are highlighted\n(high weight in the attention weights)",
             size=17, italic=True, bold=True, color=DEEP, line_spacing=1.32)

    speaker_notes(s, load_notes("s15"))


def build_s16(p):
    """Context window 3-points bar chart."""
    s = blank(p)
    slide_title(s, "The context window — a physical limit on how much the model sees at once", size=24)
    text_box(s, x=0.55, y=1.55, w=12.3, h=0.4,
             text="Context-window evolution + the quadratic cost of attention",
             size=15, italic=True, color=MID)

    # Bar chart
    ocean_box(s, 0.55, 2.10, 8.0, 4.45)
    add_image(s, ASSETS_EN / "charts/s16-context-window.png",
              x=0.75, y=2.25, w=7.6, h=4.15)

    # Right: scaling info
    rx = 8.85
    rw = 4.0
    ocean_box(s, rx, 2.10, rw, 4.45)
    text_box(s, x=rx + 0.2, y=2.25, w=rw - 0.4, h=0.4,
             text="Evolution and cost",
             size=15, bold=True, color=MID)
    info_lines = [
        ("2022 → 2026:", "×250 growth"),
        ("Pace:", "×10 / 1-2 years"),
        ("Cost N²:", "1M ≈ 16× of 100k"),
        ("Architecture:", "base attention"),
    ]
    for i, (lbl, val) in enumerate(info_lines):
        y = 2.85 + i * 0.55
        text_box(s, x=rx + 0.25, y=y, w=rw * 0.5, h=0.4,
                 text=lbl, size=13, italic=True, color=MID,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.45, y=y, w=rw * 0.5, h=0.4,
                 text=val, size=13, bold=True, color=DEEP,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    # Big gold N² hint
    filled_rect(s, rx + 0.5, 5.15, rw - 1.0, 1.0, GOLD, radius=True, radius_adj=0.15)
    text_box(s, x=rx + 0.5, y=5.20, w=rw - 1.0, h=0.95,
             text="N²",
             size=44, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Gold callout — nudged up (6.70→6.55, 0.70→0.55) to clear the ref-list.
    # "1M ≈ 16×" here matches the speaker-notes ("в шестнадцать раз дороже") —
    # visible/notes in sync (P1 s16 resolved: 16× production-pricing, N²-теория
    # 100× as the caveat, identical in both layers).
    gold_callout(s, 0.55, 6.55, 12.3, 0.55,
                 "Attention cost grows quadratically with length. 1M ~ 16x more than 100k — production pricing with batching; pure N²-theory would give 100x.[1]",
                 size=14)
    refs_of_slide(s, "s16")
    speaker_notes(s, load_notes("s16"))


def build_s17(p):
    """Long-context fails — U-shape curve."""
    s = blank(p)
    slide_title(s, "A large context window != good use of the context", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Lost-in-the-middle effect — the model forgets the middle[1]",
             size=15, italic=True, color=MID)

    # U-shape chart
    ocean_box(s, 0.55, 2.0, 8.5, 4.5)
    add_image(s, ASSETS / "charts/s17-u-shape.png",
              x=0.75, y=2.15, w=8.1, h=4.20)

    # Right: explanation
    rx = 9.35
    rw = 3.55
    ocean_box(s, rx, 2.0, rw, 4.5)
    text_box(s, x=rx + 0.2, y=2.15, w=rw - 0.4, h=0.4,
             text="Experiment",
             size=16, bold=True, color=MID)
    text_box(s, x=rx + 0.2, y=2.60, w=rw - 0.4, h=1.6,
             text="A fact is placed at position X (start / middle / end) of a 100k context. The model answers about the fact.",
             size=14, color=DEEP, line_spacing=1.32)
    # Results
    text_box(s, x=rx + 0.2, y=4.20, w=rw - 0.4, h=0.4,
             text="Results",
             size=16, bold=True, color=MID)
    res_lines = [
        ("Start:", "~75%", GOLD),
        ("Middle:", "~50%", LIGHT),
        ("End:", "~75%", GOLD),
    ]
    for i, (lbl, val, col) in enumerate(res_lines):
        y = 4.70 + i * 0.42
        text_box(s, x=rx + 0.2, y=y, w=rw * 0.6, h=0.38,
                 text=lbl, size=14, italic=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.50, y=y, w=rw * 0.45, h=0.38,
                 text=val, size=15, bold=True, color=col,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=rx + 0.2, y=6.00, w=rw - 0.4, h=0.5,
             text="Liu et al. 2023.\nLost in the Middle.",
             size=11, italic=True, color=LIGHT, line_spacing=1.20)

    # Gold callout bottom — nudged up (6.70→6.56, 0.55→0.50) to clear the ref-list
    gold_callout(s, 0.55, 6.56, 12.3, 0.50,
                 "Engineering takeaway: put what matters at the start or the end of the prompt, not in the middle.",
                 size=14)
    refs_of_slide(s, "s17")
    speaker_notes(s, load_notes("s17"))


def build_s18(p):
    """Distribution — top-5 bar chart."""
    s = blank(p)
    slide_title(s, "At each step the model outputs a probability distribution over all tokens — and picks one", size=22)

    # Context
    filled_rect(s, 4.5, 1.45, 4.3, 0.65, GOLD_TINT, stroke=GOLD, stroke_pt=1.2, radius=True, radius_adj=0.25)
    text_box(s, x=4.5, y=1.5, w=4.3, h=0.30,
             text="Context", size=11, bold=True, color=MID,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
    text_box(s, x=4.5, y=1.70, w=4.3, h=0.35,
             text="\"Today I ate …\"", size=18, bold=True, color=DEEP,
             font=FONT_MONO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Chart
    ocean_box(s, 0.55, 2.30, 8.5, 4.05)
    add_image(s, ASSETS_EN / "charts/s18-distribution.png",
              x=0.75, y=2.45, w=8.1, h=3.75)

    # Right: top-5 table
    rx = 9.35
    rw = 3.55
    ocean_box(s, rx, 2.30, rw, 4.05)
    text_box(s, x=rx + 0.2, y=2.45, w=rw - 0.4, h=0.4,
             text="Top-5 candidates",
             size=14, bold=True, color=MID)
    rows = [
        ("apple", "0.32", GOLD),
        ("pizza",  "0.19", LIGHT),
        ("salad",  "0.14", LIGHT),
        ("a bun",  "0.11", LIGHT),
        ("cucumber","0.08", LIGHT),
    ]
    for i, (tok, p_val, col) in enumerate(rows):
        y = 2.90 + i * 0.45
        text_box(s, x=rx + 0.2, y=y, w=rw * 0.55, h=0.40,
                 text=tok, size=14, color=DEEP, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + rw * 0.55, y=y, w=rw * 0.4, h=0.40,
                 text=p_val, size=16, bold=True, color=col,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=rx + 0.2, y=5.30, w=rw - 0.4, h=0.95,
             text="… the other ~200k tokens:\neach < 0.05\nΣ = 1",
             size=12, italic=True, color=LIGHT, line_spacing=1.30)

    # Gold callout
    gold_callout(s, 0.55, 6.55, 12.3, 0.55,
                 "Sampling = the rule by which one token is picked from the distribution. Next — temperature.",
                 size=14)
    speaker_notes(s, load_notes("s18"))


def build_s19(p):
    """Temperature — 3 distributions side-by-side."""
    s = blank(p)
    slide_title(s, "Temperature: how sharp the choice will be", size=28)
    text_box(s, x=0.55, y=1.40, w=12.3, h=0.4,
             text="T = 0 (argmax)  ·  T = 1.0 (standard)  ·  T = 2.0 (chaos)",
             size=18, italic=True, color=MID)

    # 3 distributions side-by-side. Cards kept near full height (5.00→4.92) so
    # the middle card's 4-line body still fits; the teal bottom-line + ref-list
    # are made compact to share the freed bottom strip.
    card_y = 1.88
    card_h = 4.92
    card_w = 4.10
    gap = 0.10
    start_x = 0.55
    descrs = [
        ("T = 0  ·  argmax",
         "Deterministic\nchoice — apple.\n10 runs → identical.",
         "s19-T0.png", GOLD),
        ("T = 1.0  ·  standard",
         "Sampling\nproportional to P.\nNatural variability.\n(T = 0.7 — the standard choice for chat)",
         "s19-T1.png", MID),
        ("T = 2.0  ·  chaos",
         "The distribution is flattened;\nunexpected options are\noften chosen.",
         "s19-T2.png", TEAL),
    ]
    for i, (head, body, img_name, color) in enumerate(descrs):
        x = start_x + i * (card_w + gap)
        is_standard = (i == 1)
        if is_standard:
            ocean_box(s, x, card_y, card_w, card_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, x, card_y, card_w, card_h)
        # Title
        text_box(s, x=x + 0.2, y=card_y + 0.18, w=card_w - 0.4, h=0.50,
                 text=head, size=22, bold=True, color=color,
                 align=PP_ALIGN.CENTER)
        # Chart image — bigger
        img = ASSETS_EN / f"charts/{img_name}"
        if img.exists():
            add_image(s, img, x=x + 0.3, y=card_y + 0.85, w=card_w - 0.6, h=2.55)
        # Body — 14pt so the middle card's 4-line body fits inside the card
        text_box(s, x=x + 0.2, y=card_y + 3.40, w=card_w - 0.4, h=1.45,
                 text=body, size=14, color=DEEP, italic=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.24)

    # Bottom-line — compact teal callout on the freed bottom strip
    teal_callout(s, 0.55, 6.86, 12.3, 0.30,
                 "Alternative knobs: top-p (nucleus) — cuts rare tokens by Σ; top-k — by the number of candidates. T is enough to start.[1]",
                 size=12)
    refs_of_slide(s, "s19", y=7.20)
    speaker_notes(s, load_notes("s19"))


def build_s20(p):
    """4 API knobs — 5×5 matrix."""
    s = blank(p)
    slide_title(s, "4 API knobs for the task: temperature, top_p, max_tokens, system prompt", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Pick parameters for the scenario deliberately",
             size=15, italic=True, color=MID)

    # Table
    ocean_box(s, 0.55, 2.05, 12.3, 4.5)
    # Headers row
    headers = ["Scenario", "temperature", "top_p", "max_tokens", "system_prompt"]
    col_widths = [3.0, 1.7, 1.3, 1.7, 4.20]
    col_xs = [0.7]
    for w in col_widths[:-1]:
        col_xs.append(col_xs[-1] + w)

    # Header row
    header_y = 2.20
    header_h = 0.55
    for i, h in enumerate(headers):
        # Header background
        filled_rect(s, col_xs[i], header_y, col_widths[i], header_h, MID, radius=False)
        text_box(s, x=col_xs[i] + 0.05, y=header_y, w=col_widths[i] - 0.1, h=header_h,
                 text=h, size=13, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Data rows — T-coded colors
    rows = [
        ("Classification / exact extraction", "0", "—", "50–200", "Minimal, with an output schema", GOLD),
        ("Code generation", "0.2–0.3", "0.9", "1000+", "Role + repository context", LIGHT),
        ("Chat explanation to the user", "0.7", "0.9", "500–1000", "Role + audience description", LIGHT),
        ("Creative writing", "0.9–1.2", "0.95", "2000+", "Role + style description", TEAL),
    ]
    row_h = 0.85
    for r_i, row in enumerate(rows):
        scenario, t_val, p_val, mt, sp, accent = row
        ry = header_y + header_h + r_i * row_h
        # Alternating fill
        fill_col = SURFACE if r_i % 2 == 0 else WHITE
        for i, w in enumerate(col_widths):
            filled_rect(s, col_xs[i], ry, w, row_h, fill_col, stroke=LIGHT, stroke_pt=0.6)
        # Cell content
        values = [scenario, t_val, p_val, mt, sp]
        for i, v in enumerate(values):
            is_t_col = (i == 1)
            text_color = accent if is_t_col else DEEP
            bold = is_t_col
            size = 13 if i == 0 else (15 if is_t_col else 12)
            align = PP_ALIGN.LEFT if i == 0 or i == 4 else PP_ALIGN.CENTER
            text_box(s, x=col_xs[i] + 0.10, y=ry, w=col_widths[i] - 0.2, h=row_h,
                     text=v, size=size, bold=bold, color=text_color,
                     align=align, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.18)

    # Footer
    text_box(s, x=0.55, y=6.75, w=12.3, h=0.5,
             text="T = 0 makes the choice nearly deterministic; in production micro-variability from batching is possible — for most tasks it is negligible.",
             size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER, line_spacing=1.30)
    speaker_notes(s, load_notes("s20"))


def build_s21(p):
    """Autoregressive loop — 5 steps cycle."""
    s = blank(p)
    slide_title(s, "Loop: predicted a token → added it to the context → predict the next", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Autoregressive generation — a long answer from stateless calls",
             size=15, italic=True, color=MID)

    # 5 steps in horizontal flow with return arrow — v1.3 enlarged (2.6→3.65)
    step_y = 2.05
    step_h = 3.65
    n_steps = 5
    total_w = 12.3
    gap = 0.15
    step_w = (total_w - gap * (n_steps - 1)) / n_steps
    start_x = 0.55
    steps = [
        ("(1) Current\ncontext",
         "system + history\n+ request + what is\nalready generated",
         False),
        ("(2) Forward\npass",
         "tokenization →\nembedding →\nattention",
         True),  # gold
        ("(3) Distribution",
         "probabilities\nover ~200k vocabulary\ntokens",
         False),
        ("(4) Sampling",
         "one token\nby the rule\nT / top-p / top-k",
         False),
        ("(5) New token\nadded to the context",
         "...and the loop\ncontinues",
         False),
    ]
    for i, (head, body, is_gold) in enumerate(steps):
        x = start_x + i * (step_w + gap)
        if is_gold:
            ocean_box(s, x, step_y, step_w, step_h, fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.5)
        else:
            ocean_box(s, x, step_y, step_w, step_h)
        # Step head
        text_box(s, x=x + 0.1, y=step_y + 0.30, w=step_w - 0.2, h=1.40,
                 text=head, size=20, bold=True,
                 color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.20)
        # Body
        text_box(s, x=x + 0.1, y=step_y + 1.85, w=step_w - 0.2, h=1.60,
                 text=body, size=16, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.40)
        # Right arrow between steps
        if i < n_steps - 1:
            right_arrow(s, x + step_w + 0.01, step_y + step_h / 2 - 0.20, w=gap - 0.03, h=0.40, fill=MID)

    # Return arrow at bottom — v1.3 bigger (0.60→0.75)
    return_y = step_y + step_h + 0.30
    filled_rect(s, 1.0, return_y, 11.4, 0.75, SURFACE, stroke=LIGHT, stroke_pt=1.5, radius=True, radius_adj=0.3)
    text_box(s, x=1.0, y=return_y + 0.10, w=11.4, h=0.55,
             text="↺ back to step (1) — until we reach the \"end of answer\" token OR max_tokens",
             size=17, italic=True, bold=True, color=MID,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Caption
    text_box(s, x=0.55, y=7.05, w=12.3, h=0.40,
             text="Each step is stateless. The \"memory\" of one answer is carried by the context itself, not the model.",
             size=14, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.3)
    speaker_notes(s, load_notes("s21"))


def build_s22(p):
    """Local vs cloud — 2 columns parallel."""
    s = blank(p)
    slide_title(s, "Inference is the same locally and in the cloud — but model size determines quality", size=24)
    text_box(s, x=0.55, y=1.50, w=12.3, h=0.4,
             text="Architecturally it is the same pipeline. The differences are in size and environment.",
             size=16, italic=True, color=MID)

    # Two columns — trimmed 5.20→4.95 to free a bottom row for the ref-list
    col_w = 6.0
    col_h = 4.95
    col_y = 2.00
    left_x = 0.55
    right_x = 6.85

    # Local
    ocean_box(s, left_x, col_y, col_w, col_h)
    text_box(s, x=left_x + 0.3, y=col_y + 0.15, w=col_w - 0.6, h=0.55,
             text="Local (Ollama, llama.cpp, LM Studio)",
             size=19, bold=True, color=MID)
    text_box(s, x=left_x + 0.3, y=col_y + 0.80, w=col_w - 0.6, h=0.50,
             text="Size: 1–13B parameters",
             size=16, bold=True, color=DEEP)
    text_box(s, x=left_x + 0.3, y=col_y + 1.35, w=col_w - 0.6, h=1.20,
             text="• Qwen 2.5 1.5B  · Llama 3.2 1B\n• Llama 3.1 8B  · Mistral 7B[1]",
             size=15, color=DEEP, line_spacing=1.45, font=FONT_MONO)
    local_pts = [
        ("Privacy", "requests do not leave for a provider", TEAL),
        ("Speed", "slower on consumer hardware", LIGHT),
        ("Context", "a limited window", LIGHT),
        ("Price", "0 per token (your own hardware)", GOLD),
    ]
    for i, (k, v, col) in enumerate(local_pts):
        py = col_y + 2.80 + i * 0.52
        filled_rect(s, left_x + 0.3, py + 0.16, 0.26, 0.26, col, radius=True, radius_adj=0.5)
        text_box(s, x=left_x + 0.70, y=py, w=col_w * 0.32, h=0.50,
                 text=k, size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=left_x + col_w * 0.45, y=py, w=col_w * 0.55, h=0.50,
                 text=v, size=15, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    # Cloud
    ocean_box(s, right_x, col_y, col_w, col_h)
    text_box(s, x=right_x + 0.3, y=col_y + 0.15, w=col_w - 0.6, h=0.55,
             text="Cloud (OpenAI, Anthropic, Yandex, Sber)",
             size=19, bold=True, color=MID)
    text_box(s, x=right_x + 0.3, y=col_y + 0.80, w=col_w - 0.6, h=0.50,
             text="Size: 200B+ parameters",
             size=16, bold=True, color=DEEP)
    text_box(s, x=right_x + 0.3, y=col_y + 1.35, w=col_w - 0.6, h=1.20,
             text="• GPT-5, Claude 4.7\n• YandexGPT, GigaChat\n• Gemini",
             size=15, color=DEEP, line_spacing=1.45, font=FONT_MONO)
    cloud_pts = [
        ("Quality", "better on hard tasks", TEAL),
        ("Latency", "200–500 ms", LIGHT),
        ("Context", "up to 1M tokens", GOLD),
        ("Price", "pay per token, RU ~ 2x EN", LIGHT),
    ]
    for i, (k, v, col) in enumerate(cloud_pts):
        py = col_y + 2.80 + i * 0.52
        filled_rect(s, right_x + 0.3, py + 0.16, 0.26, 0.26, col, radius=True, radius_adj=0.5)
        text_box(s, x=right_x + 0.70, y=py, w=col_w * 0.32, h=0.50,
                 text=k, size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=right_x + col_w * 0.45, y=py, w=col_w * 0.55, h=0.50,
                 text=v, size=15, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    refs_of_slide(s, "s22")
    speaker_notes(s, load_notes("s22"))


def build_s23(p):
    """Pipeline recap — 4 stages horizontal flow."""
    s = blank(p)
    slide_title(s, "The 4 inference stages line up into a pipeline", size=28)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="The same black box from Lecture 1 — now unpacked",
             size=15, italic=True, color=MID)

    # 4 stages horizontal pipeline
    stage_y = 2.50
    stage_h = 3.1
    n = 4
    total_w = 12.3
    gap = 0.35
    stage_w = (total_w - gap * n) / n  # gap between + final arrow at end
    start_x = 0.55
    stages = [
        ("Tokenization", "Text → id\nfrom the vocabulary (BPE)", "binary"),
        ("Embedding", "id → vector\nfrom the trained table", "scaling"),
        ("Attention", "A distribution\nof weights over the context", "focus"),
        ("Sampling", "Distribution →\none token (T / p / k)", "sparkles"),
    ]
    for i, (head, body, icon) in enumerate(stages):
        x = start_x + i * (stage_w + gap)
        ocean_box(s, x, stage_y, stage_w, stage_h)
        # Stage number circle
        filled_rect(s, x + (stage_w - 0.85) / 2, stage_y + 0.20, 0.85, 0.85, MID, radius=True, radius_adj=0.5)
        text_box(s, x=x, y=stage_y + 0.27, w=stage_w, h=0.70,
                 text=str(i + 1), size=28, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Icon — v1.5, small under number
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + (stage_w - 0.60) / 2, y=stage_y + 1.15, w=0.60, h=0.60)
        # Head
        text_box(s, x=x + 0.1, y=stage_y + 1.85, w=stage_w - 0.2, h=0.55,
                 text=head,
                 size=20, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Body
        text_box(s, x=x + 0.1, y=stage_y + 2.45, w=stage_w - 0.2, h=0.65,
                 text=body, size=14, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)
        # Arrow between
        if i < n - 1:
            right_arrow(s, x + stage_w + 0.05, stage_y + stage_h / 2 - 0.20, w=gap - 0.10, h=0.40, fill=MID)

    # Final arrow → "следующий токен"
    final_x = start_x + n * (stage_w + gap) - gap + 0.05
    if final_x + 1.0 < 13.0:
        right_arrow(s, final_x, stage_y + stage_h / 2 - 0.20, w=0.8, h=0.40, fill=GOLD)
        text_box(s, x=final_x - 0.4, y=stage_y + stage_h + 0.15, w=1.6, h=0.4,
                 text="next token",
                 size=11, bold=True, color=DEEP, italic=True,
                 align=PP_ALIGN.CENTER)

    # Caption bottom
    text_box(s, x=0.55, y=6.85, w=12.3, h=0.4,
             text="Lecture 1 called this pipeline the \"inference model\" — a black box. Now it is no longer black.",
             size=13, italic=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.30)
    speaker_notes(s, load_notes("s23"))


def build_s24(p):
    """Answers to the 3 opening whys — 3 parallel cards (v1.8, issue #156).

    Renamed from "3 промиса Лекции 1" (forbidden §-reference + "payoff"
    scaffold phrase removed per #204). Badge colors unified to the
    MID/LIGHT/TEAL Ocean family — v1.7 used GOLD on card 1 only, which read
    as an unintended "this one is special" emphasis vs cards 2-3 (#205).
    """
    s = blank(p)
    slide_title(s, "Answers to the questions from the start of the lecture", size=28)

    # 3 boxes vertical — enlarged to fill space freed by removed gold marker bar
    box_y_start = 1.55
    box_h = 1.85
    box_gap = 0.18
    answers = [
        ("1", "Why does a prompt with a role work better than an empty one?",
         "At the attention level, role tokens get high weight — the model leans on them when choosing the next tokens.",
         MID, "focus"),  # focus — внимание/role
        ("2", "Why is AI bad at counting letters?",
         "The tokenizer merges letters into tokens. strawberry — 3 tokens, not 10 letters. The model sees tokens, not letters.",
         LIGHT, "binary"),  # binary — токены/цифры
        ("3", "Why does the same request give different answers?",
         "Sampling — a stochastic choice from the distribution when T > 0. Each run may pick a different token.",
         TEAL, "sparkles"),  # sparkles — randomness
    ]
    for i, (n, q, a, col, icon) in enumerate(answers):
        y = box_y_start + i * (box_h + box_gap)
        ocean_box(s, 0.55, y, 12.3, box_h)
        # Number badge (1.10×1.10) — unified Ocean-family color, no gold
        filled_rect(s, 0.80, y + 0.37, 1.10, 1.10, col, radius=True, radius_adj=0.5)
        text_box(s, x=0.80, y=y + 0.39, w=1.10, h=1.05,
                 text=n, size=48, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Icon — справа от номера
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=11.50, y=y + 0.52, w=0.80, h=0.80)
        # Question
        text_box(s, x=2.15, y=y + 0.25, w=9.20, h=0.60,
                 text=q, size=21, bold=True, color=DEEP)
        # Answer
        text_box(s, x=2.15, y=y + 0.90, w=9.20, h=0.90,
                 text=a, size=17, color=DEEP, italic=True, line_spacing=1.32)

    speaker_notes(s, load_notes("s24"))


def build_s25(p):
    """ML vs LLM decision tree (v1.8, issue #156 #206 — redesign).

    Fixes v1.7 overflow bug: "Интерпретируемость" head wrapped to 2 lines
    inside a 0.65"-tall box and visually collided with the condition text
    below it (spilled into "BERT" overlapping the else-pill). Redesign:
    taller head zone, explicit arrowhead connectors (root→branch,
    branch→else) via MSO_SHAPE triangles, more vertical breathing room.
    """
    s = blank(p)
    slide_title(s, "When an LLM is not the right tool: a decision tree", size=26)

    # Root
    root_y = 1.35
    root_h = 0.80
    root_w = 6.4
    root_x = (SLIDE_W_IN - root_w) / 2
    ocean_box(s, root_x, root_y, root_w, root_h,
              fill=GOLD_TINT, stroke=GOLD, stroke_pt=2.0)
    text_box(s, x=root_x, y=root_y, w=root_w, h=root_h,
             text="When is an LLM not the right tool?",
             size=19, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # 3 branches — taller head zone (0.65→0.95) to fit 2-line wraps safely
    branch_y = 2.75
    branch_h = 3.55
    branch_w = 3.95
    gap = 0.20
    start_x = 0.55
    branches = [
        ("cpu", "Fixed\nclasses",
         "Classification over a small set of categories (5–20)?",
         "→ Classical ML\nlogistic regression, XGBoost,\nLightGBM, fine-tuned BERT"),
        ("file-text", "Interpretability",
         "Interpretability needed\n(finance, medicine, insurance)?",
         "→ Transparent methods\nlogistic regression + importances,\ndecision trees, rules"),
        ("gauge", "Response\nspeed",
         "Response time < 100 ms critical\n(anti-fraud, on the users device)?",
         "→ A specialized\nsmall model\n(not an LLM ≥200 ms)"),
    ]
    for i, (icon, head, cond, action) in enumerate(branches):
        x = start_x + i * (branch_w + gap)
        cx = x + branch_w / 2
        # Connector line from root
        filled_rect(s, cx - 0.02, root_y + root_h, 0.04, branch_y - root_y - root_h - 0.14, LIGHT)
        # Arrowhead pointing down into the branch box
        arrow = s.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE,
                                    Inches(cx - 0.10), Inches(branch_y - 0.14),
                                    Inches(0.20), Inches(0.14))
        arrow.rotation = 180
        arrow.fill.solid(); arrow.fill.fore_color.rgb = LIGHT
        arrow.line.fill.background()
        disable_shadow(arrow)

        ocean_box(s, x, branch_y, branch_w, branch_h)
        # Icon — top-left
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + 0.25, y=branch_y + 0.20, w=0.95, h=0.95)
        # Head — 2-line safe zone (0.20→1.15 = 0.95" tall)
        text_box(s, x=x + 1.35, y=branch_y + 0.20, w=branch_w - 1.55, h=0.95,
                 text=head.replace("\n", " "), size=17, bold=True, color=MID,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
        # Condition
        text_box(s, x=x + 0.25, y=branch_y + 1.30, w=branch_w - 0.5, h=1.10,
                 text=cond, size=14, color=DEEP, italic=True, line_spacing=1.28)
        # Action
        text_box(s, x=x + 0.25, y=branch_y + 2.45, w=branch_w - 0.5, h=1.00,
                 text=action, size=14, bold=True, color=DEEP, line_spacing=1.26)

    # Connector from branches down to else-pill
    else_y = 6.65
    else_w = 10.9
    else_x = (SLIDE_W_IN - else_w) / 2
    mid_branches_bottom = branch_y + branch_h
    for i in range(3):
        x = start_x + i * (branch_w + gap)
        cx = x + branch_w / 2
        filled_rect(s, cx - 0.02, mid_branches_bottom, 0.04, else_y - mid_branches_bottom, TEAL)

    # Else → LLM (bottom teal pill)
    filled_rect(s, else_x, else_y, else_w, 0.65, TEAL_TINT, stroke=TEAL, stroke_pt=2.0, radius=True, radius_adj=0.5)
    text_box(s, x=else_x, y=else_y, w=else_w, h=0.65,
             text="Otherwise — an LLM fits (chat, RAG, generation, multi-step reasoning)",
             size=16, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    speaker_notes(s, load_notes("s25"))


def build_s26(p):
    """Attention vs causality — 2 columns Human vs AI.

    v1.9 (issue #156 QA fix-pass, P1 Russification): headline "Attention..."
    → "Внимание..." (this slide's title is the top-priority anglicism fix —
    it's the main headline of the slide). Card header "AI (через attention)"
    → "ИИ (через внимание)". Body "domain-эксперта или causal-методы" →
    RU equivalent.
    """
    s = blank(p)
    slide_title(s, "Attention looks at tokens statistically — it does not understand causality", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="AI counts correlations in the data, it does not build a causal graph",
             size=16, italic=True, color=MID)

    # 2 columns — trimmed 5.65→5.15 to free a bottom row for the ref-list.
    col_w = 6.0
    col_h = 5.15
    col_y = 1.95
    left_x = 0.55
    right_x = 6.85

    # Human
    ocean_box(s, left_x, col_y, col_w, col_h)
    add_image(s, ASSETS / "icons/users.png", x=left_x + 0.3, y=col_y + 0.25, w=1.15, h=1.15)
    text_box(s, x=left_x + 1.55, y=col_y + 0.25, w=col_w - 1.75, h=1.15,
             text="Human", size=28, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=left_x + 0.3, y=col_y + 1.65, w=col_w - 0.6, h=0.65,
             text='"X happened because Y"',
             size=18, bold=True, italic=True, color=MID,
             font=FONT_MONO, line_spacing=1.25)
    text_box(s, x=left_x + 0.3, y=col_y + 2.45, w=col_w - 0.6, h=0.55,
             text="A causal model — it builds mechanisms.",
             size=18, italic=True, color=DEEP)

    text_box(s, x=left_x + 0.3, y=col_y + 3.35, w=col_w - 0.6, h=1.60,
             text="Relies on physical intuition, domain knowledge, knowledge of how the world works. "
                  "For causal conclusions this experience is exactly what is needed — not statistics.",
             size=16, italic=True, color=DEEP, line_spacing=1.28)

    # AI
    ocean_box(s, right_x, col_y, col_w, col_h)
    add_image(s, ASSETS / "icons/brain.png", x=right_x + 0.3, y=col_y + 0.25, w=1.15, h=1.15)
    text_box(s, x=right_x + 1.55, y=col_y + 0.25, w=col_w - 1.75, h=1.15,
             text="AI (via attention)", size=28, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=right_x + 0.3, y=col_y + 1.65, w=col_w - 0.6, h=0.65,
             text='"X follows Y in the data"',
             size=18, bold=True, italic=True, color=MID,
             font=FONT_MONO, line_spacing=1.25)
    text_box(s, x=right_x + 0.3, y=col_y + 2.45, w=col_w - 0.6, h=0.55,
             text="A statistical correlation, not causality.[1]",
             size=18, italic=True, color=DEEP)

    text_box(s, x=right_x + 0.3, y=col_y + 3.35, w=col_w - 0.6, h=1.60,
             text="Notices the pattern \"X and Y often co-occur\" in the training data. "
                  "For causal conclusions — bring in a domain expert or causal methods.",
             size=16, italic=True, color=DEEP, line_spacing=1.28)

    refs_of_slide(s, "s26")
    speaker_notes(s, load_notes("s26"))


def build_s27(p):
    """Homework — 3 steps + bonus."""
    s = blank(p)
    slide_title(s, "Bring: 1 request × 3 temperatures × 3 runs × analysis", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="Homework for Seminar 2 — apply temperature on your own task",
             size=16, italic=True, color=MID)

    # 3 step cards
    card_y = 2.05
    card_h = 3.55
    card_w = 3.95
    gap = 0.20
    start_x = 0.55
    cards = [
        ("target", "Step 1",
         "Take a typical task from your own domain.",
         "A concrete reproducible request (not \"help me think\")."),
        ("sliders-horizontal", "Step 2",
         "Run it in a playground at 3 temperatures.",
         "T = 0  ·  T = 0.7  ·  T = 1.5\n3 runs each\n(to estimate variance)"),
        ("file-text", "Step 3",
         "Bring a one-page analysis (1 A4).",
         "What changed / stayed / which T for production."),
    ]
    for i, (icon, head, body, detail) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        ocean_box(s, x, card_y, card_w, card_h)
        # Icon
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + (card_w - 1.1) / 2, y=card_y + 0.30, w=1.1, h=1.1)
        # Head
        text_box(s, x=x + 0.2, y=card_y + 1.55, w=card_w - 0.4, h=0.5,
                 text=head, size=20, bold=True, color=MID,
                 align=PP_ALIGN.CENTER)
        # Body
        text_box(s, x=x + 0.25, y=card_y + 2.10, w=card_w - 0.5, h=0.75,
                 text=body, size=15, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.30)
        # Detail
        text_box(s, x=x + 0.25, y=card_y + 2.85, w=card_w - 0.5, h=0.65,
                 text=detail, size=13, italic=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.35)

    # Playground info — full-width box
    pg_y = 5.85
    ocean_box(s, 0.55, pg_y, 8.4, 1.40, fill=SURFACE, stroke=LIGHT)
    text_box(s, x=0.75, y=pg_y + 0.14, w=8.0, h=0.40,
             text="Playground:  Hugging Face Inference Playground",
             size=15, bold=True, color=MID)
    text_box(s, x=0.75, y=pg_y + 0.58, w=8.0, h=0.40,
             text="Model: Meta-Llama-3-8B-Instruct (apples-to-apples)",
             size=13, color=DEEP, italic=False)
    text_box(s, x=0.75, y=pg_y + 1.00, w=8.0, h=0.35,
             text="Fallback: Together.ai / Ollama locally   ·   NOT suitable: ChatGPT Free, Claude.ai",
             size=12, italic=True, color=LIGHT)

    # Bonus
    filled_rect(s, 9.15, pg_y, 3.70, 1.40, GOLD_TINT, stroke=GOLD, stroke_pt=2.0, radius=True, radius_adj=0.12)
    text_box(s, x=9.30, y=pg_y + 0.12, w=3.5, h=0.40,
             text="BONUS",
             size=16, bold=True, color=DEEP)
    text_box(s, x=9.30, y=pg_y + 0.54, w=3.5, h=0.80,
             text="How many r-s in \"strong regularization\" × 3 models. Explain via tokenization.",
             size=12, italic=True, color=DEEP, line_spacing=1.30)

    speaker_notes(s, load_notes("s27"))


def build_s28(p):
    """Bridge to Lec 3 — 4 concepts preview.
    v1.6 (Phase 8.9): Q&A block at bottom removed — dedicated s29 slide replaces it.
    Title simplified ('+ Q&A' removed). Grid centered vertically with extra breathing room.
    v1.9 (issue #156 QA fix-pass, P0-1): row 2 of the 2×2 grid overflowed the
    slide (grid_y 2.10 + cell_h 2.75 + gap 0.22 + cell_h 2.75 = 7.82" > 7.5"
    slide height) — bottom-row card text ("...инструментов (Anthropic, 2024)"
    / "...корректирует план") ran past the card edge. Fix: raised grid up
    (2.10→1.95), tightened gap (0.22→0.16), and trimmed body font 16→15pt
    per presentation-critic recommendation so both rows now fit with margin
    (row2 bottom = 1.95+2.70+0.16+2.70 = 7.51" ... still tight, so cell_h
    also trimmed 2.75→2.68 to land at 7.37", leaving ~0.13" breathing room).
    """
    s = blank(p)
    slide_title(s, "Lecture 3:  \"Agents, RAG, API — how AI goes beyond the chat\"", size=24)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.4,
             text="All 4 concepts build on top of a single inference pass",
             size=16, italic=True, color=MID)

    # 2×2 grid — trimmed (cell_h 2.68→2.48, gap 0.16→0.14) to free a bottom row
    # for the clickable ref-list. Row2 bottom = 1.95+2.48+0.14+2.48 = 7.05".
    grid_x = 0.55
    grid_y = 1.95
    cell_w = 6.0
    cell_h = 2.48
    gap = 0.14

    # v1.8 (#209): removed unjustified gold highlight on RAG card — all 4
    # concepts are equally weighted (no data-driven reason for RAG alone to
    # stand out), matches anti-pattern #21 "inconsistent gold-emphasis
    # across same-tier cards". All 4 now render as plain Ocean rounded box.
    concepts = [
        # (icon, title, sub, body)
        ("search-check", "RAG[1]",
         "Retrieval-Augmented Generation",
         "embedding similarity + LLM -> an answer from your own base"),
        ("workflow", "Tools / Function calling",
         "structured JSON",
         "the LLM generates a call → an external system executes it → the result is returned"),
        ("arrow-right-left", "MCP[2]",
         "Model Context Protocol",
         "An open standard for connecting tools (Anthropic, 2024)"),
        ("repeat-2", "Agent loop[3]",
         "act → observe → adjust",
         "the model decides an action, sees the result, adjusts the plan"),
    ]
    for i, (icon, title, sub, body) in enumerate(concepts):
        col = i % 2
        row = i // 2
        x = grid_x + col * (cell_w + gap)
        y = grid_y + row * (cell_h + gap)
        ocean_box(s, x, y, cell_w, cell_h)
        # Icon — bigger 1.10
        icon_path = ASSETS / f"icons/{icon}.png"
        if icon_path.exists():
            add_image(s, icon_path, x=x + 0.25, y=y + 0.35, w=1.10, h=1.10)
        # Title
        text_box(s, x=x + 1.50, y=y + 0.28, w=cell_w - 1.65, h=0.60,
                 text=title, size=21, bold=True, color=DEEP, line_spacing=1.15)
        # Subtitle
        text_box(s, x=x + 1.50, y=y + 0.95, w=cell_w - 1.65, h=0.38,
                 text=sub, size=14, italic=True, color=MID)
        # Body — v1.9 (P0-1): font 16→15pt + box height 1.00→1.28 so bottom-row
        # cards ("...инструментов (Anthropic, 2024)" / "...корректирует план")
        # no longer overflow the card / slide edge.
        text_box(s, x=x + 0.30, y=y + 1.58, w=cell_w - 0.55, h=0.85,
                 text=body, size=15, color=DEEP, line_spacing=1.24)

    refs_of_slide(s, "s28")
    speaker_notes(s, load_notes("s28"))


def build_s29(p):
    """Q&A — dedicated minimal final slide (v1.8, issue #156 #210).

    Redesigned to exactly match the Lec-1 s31 pattern (the approved final
    design after issue #153/#155), inspected from the rendered lec-01.pptx
    (not the markdown source, which can drift from the approved render):
    SURFACE-tinted background (not white), «Q&A» 140pt DEEP at y=1.9,
    «Спасибо» (not «Спасибо за внимание!») 36pt italic MID at y=5.4,
    contacts placeholder bottom-right 11pt italic SLATE at x=8.0,y=6.8.
    """
    s = blank(p)
    set_slide_bg(s, SURFACE)

    # Huge centered Q&A — 140pt deep, positioned per Lec-1 s31
    text_box(s, x=0.55, y=1.9, w=12.25, h=2.4,
             text="Q&A",
             size=140, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.0)

    # «Спасибо» — 36pt italic below, per Lec-1 s31
    text_box(s, x=0.55, y=5.4, w=12.25, h=0.7,
             text="Thank you",
             size=36, color=MID, align=PP_ALIGN.CENTER, italic=True)

    # Contact placeholder — bottom right, per Lec-1 s31
    text_box(s, x=8.0, y=6.8, w=4.85, h=0.4,
             text="lecturer contacts — filled in before the lecture",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.RIGHT)

    speaker_notes(s, load_notes("s29"))


# ============================================================
# New v1.5 builders (Phase 8.8) — 3 new slides per user feedback round 4.
# s04b: data flow schema (after Раздел 1 divider, before s05).
# s09a: embedding space concept (after s09, before s10).
# s13a: attention matrix (after s13 divider, before s14).
# ============================================================
def build_s04b(p):
    """Поток данных в LLM — roadmap всего inference-конвейера (v1.5).

    User feedback round 4 #6: «перед токенами не хватает схемки —
    слова в векторы, уже они в LLM, оттуда тоже вектора и они в слова».
    Placed between s04a (Раздел 1 divider) and s05 (что такое токен) —
    sets up the pipeline overview before zooming into токенизация.
    """
    s = blank(p)
    slide_title(s, "Data flow in an LLM — there and back", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.45,
             text="We'll cover each stage separately. Now — the whole map.",
             size=15, italic=True, color=MID, line_spacing=1.25)

    # Big data flow diagram (full width)
    ocean_box(s, 0.55, 2.05, 12.3, 4.55)
    add_image(s, ASSETS_EN / "diagrams/s04b-data-flow.png",
              x=0.75, y=2.20, w=11.9, h=4.30)

    # Gold callout below
    gold_callout(s, 0.55, 6.75, 12.3, 0.65,
                 "A word exists only at the boundaries. Inside the model — only vectors. Today we cover 4 stages.",
                 size=15)
    speaker_notes(s, load_notes("s04b"))


def build_s09a(p):
    """Пространство эмбеддингов — концептуальная иллюстрация (v1.5).

    User feedback round 4 #4: «нужно пояснение, может даже отдельный слайд
    до этого про пространство в котором вектора появляются, что там за
    измерения и как они проставляются у векторов». Bridges s09 (token→vector
    lookup) → s10 (sentence similarity heatmap).
    """
    s = blank(p)
    slide_title(s, "The embedding space — where the vectors live", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.40,
             text="Before comparing vectors — let's look at what space they live in.",
             size=15, italic=True, color=MID)

    # Left: 2D scatter illustration (60%)
    ocean_box(s, 0.55, 2.00, 7.50, 4.55)
    add_image(s, ASSETS_EN / "diagrams/s09a-embedding-space.png",
              x=0.70, y=2.15, w=7.20, h=4.30)

    # Right: 3 facts in motif boxes (40%)
    rx = 8.25
    rw = 4.65
    facts = [
        ("Dimensionality",
         "OpenAI text-embedding-3-small: 1536 dim.\n"
         "text-embedding-3-large: 3072 dim.\n"
         "Flagship LLM: thousands."),
        ("Learning",
         "Coordinates are not set by hand. The model learns:\n"
         "tokens in similar contexts → close vectors."),
        ("Projection",
         "To see the space — PCA or t-SNE\n"
         "reduce the dimensionality to 2D/3D.\n"
         "Some of the structure is lost."),
    ]
    fy = 2.00
    fh = 1.45
    fgap = 0.10
    for i, (head, body) in enumerate(facts):
        y = fy + i * (fh + fgap)
        ocean_box(s, rx, y, rw, fh)
        # Number badge
        filled_rect(s, rx + 0.18, y + 0.18, 0.36, 0.36, MID, radius=True, radius_adj=0.5)
        text_box(s, x=rx + 0.18, y=y + 0.19, w=0.36, h=0.34,
                 text=str(i + 1), size=14, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Head
        text_box(s, x=rx + 0.65, y=y + 0.13, w=rw - 0.80, h=0.40,
                 text=head, size=15, bold=True, color=MID)
        # Body
        text_box(s, x=rx + 0.20, y=y + 0.55, w=rw - 0.35, h=0.85,
                 text=body, size=12, color=DEEP, line_spacing=1.30)

    # Gold callout снизу
    gold_callout(s, 0.55, 6.75, 12.3, 0.55,
                 "Semantic similarity = geometric closeness of vectors. On the next slide — the measure.",
                 size=14)
    speaker_notes(s, load_notes("s09a"))


def build_s13a(p):
    """Внимание — это матрица (v1.5).

    User feedback round 4 #7: «механизм внимания — пропустили матрицу
    внимания! Механизм же не линейный а матричный!». Placed between s13
    (Раздел 3 divider) and s14 (attention as distribution) — explains the
    matrix nature of attention before discussing its softmax output.
    """
    s = blank(p)
    slide_title(s, "Attention is each token checking against every other token", size=26)
    text_box(s, x=0.55, y=1.45, w=12.3, h=0.40,
             text="Each token \"looks at\" all the others at once. At every step — N × N links.",
             size=15, italic=True, color=MID)

    # Left: 7×7 matrix heatmap (60%)
    ocean_box(s, 0.55, 2.00, 7.85, 5.10)
    add_image(s, ASSETS_EN / "diagrams/s13a-attention-matrix.png",
              x=0.70, y=2.15, w=7.55, h=4.85)

    # Right: 3 facts about matrices (40%)
    rx = 8.55
    rw = 4.35
    facts = [
        ("Dimensionality",
         "N × N, where N is the context length.\n"
         "Context 100k → a matrix of ~10 billion numbers.\n"
         "→ the quadratic cost of attention."),
        ("At every step",
         "The matrix is recomputed at every\n"
         "new generated token (not once)."),
        ("Multi-head",
         "In one layer — dozens of such matrices\n"
         "in parallel. Different \"heads\" look at\n"
         "grammar, topic, distance."),
    ]
    fy = 2.00
    fh = 1.60
    fgap = 0.10
    for i, (head, body) in enumerate(facts):
        y = fy + i * (fh + fgap)
        ocean_box(s, rx, y, rw, fh)
        # Number badge
        filled_rect(s, rx + 0.18, y + 0.18, 0.36, 0.36, MID, radius=True, radius_adj=0.5)
        text_box(s, x=rx + 0.18, y=y + 0.19, w=0.36, h=0.34,
                 text=str(i + 1), size=14, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Head
        text_box(s, x=rx + 0.65, y=y + 0.13, w=rw - 0.80, h=0.40,
                 text=head, size=14, bold=True, color=MID)
        # Body
        text_box(s, x=rx + 0.20, y=y + 0.55, w=rw - 0.35, h=1.00,
                 text=body, size=11, color=DEEP, line_spacing=1.30)

    # Gold callout снизу
    gold_callout(s, 0.55, 7.25, 12.3, 0.20,
                 "Attention is a matrix operation, not a linear one. Each token is compared with all the others.",
                 size=12)
    speaker_notes(s, load_notes("s13a"))


# ============================================================
# Section dividers (v1.3, Phase 8.6) — mirror s13 pattern.
# Pattern: large «Раздел N» (140pt gold) + sub-title (44pt deep)
# + frame phrase (20pt italic mid) + bottom roadmap_bar with gold cell.
# ============================================================
def _build_section_divider(p, *, section_n, sub_title, frame_phrase, here_idx, notes_id):
    """Shared divider renderer — exact s13 visual pattern."""
    s = blank(p)
    set_slide_bg(s, SURFACE)

    # Big "Раздел N" outline gold — 140pt centred
    text_box(s, x=0.55, y=1.30, w=12.3, h=2.5,
             text=f"Section {section_n}",
             size=140, bold=True, color=GOLD,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    # Sub-title (the section name)
    text_box(s, x=0.55, y=3.9, w=12.3, h=0.7,
             text=sub_title,
             size=44, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Assertion / frame phrase
    text_box(s, x=0.55, y=4.75, w=12.3, h=0.5,
             text=frame_phrase,
             size=20, italic=True, color=MID,
             align=PP_ALIGN.CENTER)
    # Roadmap-bar (gold cell = section we're entering)
    roadmap_bar(s, here_idx=here_idx)
    speaker_notes(s, load_notes(notes_id))


def build_s04a(p):
    """Раздел 1 divider — Токенизация (after s04, before s05)."""
    _build_section_divider(p,
        section_n=1,
        sub_title="Tokenization",
        frame_phrase="How the model sees your text",
        here_idx=1,
        notes_id="s04a")


def build_s08a(p):
    """Раздел 2 divider — Эмбеддинги (after s08, before s09)."""
    _build_section_divider(p,
        section_n=2,
        sub_title="Embeddings",
        frame_phrase="The space of meanings",
        here_idx=2,
        notes_id="s08a")


def build_s17a(p):
    """Раздел 4 divider — Сэмплинг (after s17, before s18)."""
    _build_section_divider(p,
        section_n=4,
        sub_title="Sampling",
        frame_phrase="From the distribution to a token",
        here_idx=4,
        notes_id="s17a")


def build_s22a(p):
    """Раздел 5 divider — Финал (after s22, before s23)."""
    _build_section_divider(p,
        section_n=5,
        sub_title="Wrap-up",
        frame_phrase="Closing the 3 \"whys\" + bridge to Lecture 3",
        here_idx=5,
        notes_id="s22a")


# ============================================================
# Build all 35 slides v1.8 (issue #156):
#   36 v1.6/1.7 − 1 (s27-homework removed, deferred out of this deck).
# ============================================================
def main():
    p = setup_pres()
    builders = [
        # Раздел 0 — Введение
        build_s01, build_s02, build_s02a, build_s03, build_s04,
        # Раздел 1 — Токенизация (divider + flow schema first)
        build_s04a, build_s04b, build_s05, build_s06, build_s07, build_s08,
        # Раздел 2 — Эмбеддинги (divider first; s11 removed in v1.5; s09a added)
        build_s08a, build_s09, build_s09a, build_s10, build_s12,
        # Раздел 3 — Внимание (existing divider s13 + s13a matrix slide)
        build_s13, build_s13a, build_s14, build_s15, build_s16, build_s17,
        # Раздел 4 — Сэмплинг (divider first)
        build_s17a, build_s18, build_s19, build_s20, build_s21, build_s22,
        # Раздел 5 — Финал (divider first; s29 Q&A new in v1.6; s27 removed in v1.8)
        build_s22a, build_s23, build_s24, build_s25, build_s26, build_s28, build_s29,
    ]
    print(f"Building {len(builders)} slides…")
    # Map index → slide-id for log clarity
    slide_ids = [
        "s01", "s02", "s02a", "s03", "s04",
        "s04a", "s04b", "s05", "s06", "s07", "s08",
        "s08a", "s09", "s09a", "s10", "s12",
        "s13", "s13a", "s14", "s15", "s16", "s17",
        "s17a", "s18", "s19", "s20", "s21", "s22",
        "s22a", "s23", "s24", "s25", "s26", "s28", "s29",
    ]
    assert len(slide_ids) == len(builders) == 35, (
        f"Builder/id count mismatch: {len(builders)} builders, "
        f"{len(slide_ids)} ids")
    for i, fn in enumerate(builders):
        try:
            fn(p)
            print(f"  {slide_ids[i]} OK")
        except Exception as e:
            print(f"  {slide_ids[i]} FAIL: {type(e).__name__}: {e}")
            raise
    # Footer-less render for publication (issue #176): deck-wide «N / TOTAL»
    # page-number stamping is intentionally disabled.
    total = len(builders)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    p.save(str(OUT))
    print(f"\nSaved: {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
