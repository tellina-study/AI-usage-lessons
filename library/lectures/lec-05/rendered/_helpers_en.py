"""
Shared build helpers for Лекция 5 «AI-продукт: полный жизненный цикл»
(50 slides s01-s49 + s13a, 6-section product-loop roadmap).

Ported from the proven lec-04 _helpers.py (issue #170), adapted for the lec-05
worktree path + 6-section loop roadmap (Discovery/Design/Build-Launch/Measure/
Support/Governance) + lec-05 URL registry.

Palette LOCKED: Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal (#028090)
secondary + Gold (#F0AB00) ≥1×/slide. Motif «Ocean rounded box»
(radius 12, surface #F4F7FA, stroke #1C7293 1.5pt) на каждом content-слайде.

Canvas 13.333" × 7.5" (16:9). Fonts fall back to DejaVu (Cyrillic OK).

Issue #189 · Branch: hc/pldlc-lesson5-c5cc1586
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from lxml import etree
from PIL import Image

# === Palette (LOCKED) ===
DEEP    = RGBColor(0x21, 0x29, 0x5C)
MID     = RGBColor(0x06, 0x5A, 0x82)
LIGHT   = RGBColor(0x1C, 0x72, 0x93)
TEAL    = RGBColor(0x02, 0x80, 0x90)
SURFACE = RGBColor(0xF4, 0xF7, 0xFA)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GOLD    = RGBColor(0xF0, 0xAB, 0x00)
SLATE   = RGBColor(0x5B, 0x66, 0x78)
COVER_OUTLINE = RGBColor(0xD9, 0xE2, 0xEC)
GOLD_TINT = RGBColor(0xFD, 0xF3, 0xDC)
TEAL_TINT = RGBColor(0xE4, 0xF1, 0xF2)
SOFT_GREY = RGBColor(0xE5, 0xEA, 0xF0)
MID_TINT  = RGBColor(0xE1, 0xEA, 0xF0)

# === Constants ===
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
ROOT = Path(__file__).resolve().parents[1]      # library/lectures/lec-05
ASSETS = ROOT / "rendered/assets"
ICONS = ASSETS / "icons"
CHARTS = ASSETS / "charts-en"
SLIDES_DIR = ROOT / "slides-en"
FONT_HEAD = "DejaVu Sans"
FONT_BODY = "DejaVu Sans"
FONT_MONO = "DejaVu Sans Mono"


# ============================================================
# Canonical URL registry (ПРАВКА 1, issue #189 rebuild) — flat map keyed
# by short id, ported from lec-04's pattern. Source: notes/research/
# lecture-5-pdlc/*.md dossiers (11 files) + chapter-part4.md «Источники».
# Only URLs actually located in the dossiers are used — no invented URLs.
# Volatile ([VFY-day-of] / [FACT-CHECK]) sources are still linked; the
# caveat lives in SLIDE_REFS (volatile=True) and surfaces in speaker notes.
# ============================================================
URLS = {
    # --- Классика: discovery / design / experiment / SRE ---
    "blank_custdev": "https://innovation.ucsd.edu/startup/startup-toolkit/Steve-Blank-CustDev.pdf",
    "mom_test": "https://www.sachinrekhi.com/p/the-mom-test-rob-fitzpatrick",
    "torres_ost": "https://www.producttalk.org/opportunity-solution-trees/",
    "torres_cdh": "https://www.producttalk.org/continuous-discovery-habits/",
    "torres_ai_anti_synth": "https://cieden.com/podcast/teresa-torres-on-continuous-discovery-in-b2b-and-ai",
    "double_diamond": "https://www.designcouncil.org.uk/resources/the-double-diamond/",
    "nielsen_heuristics": "https://blog.uxtweak.com/usability-heuristics/",
    "nielsen_history": "https://www.uxtigers.com/post/usability-heuristics-history",
    "nielsen_not_user": "https://medium.com/hippo-digital/you-are-not-the-user-but-what-about-when-you-are-35abe4006b8",
    "lean_startup_vanity": "https://effectivesoftwaredesign.com/2021/03/23/lean-startup-principles-vanity-metrics-and-actionable-metrics/",
    "stage_gate_story": "https://www.stage-gate.com/about/our-story-2/",
    "kohavi_oec": "https://www.linkedin.com/pulse/overall-evaluation-criterion-oec-ronny-kohavi",
    "kohavi_bing_ab": "https://en.wikipedia.org/wiki/A/B_testing",
    "exp_platform": "https://exp-platform.com/",
    "srm_microsoft": "https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/",
    "gopractice_peeking": "https://gopractice.io/data/peeking-problem/",
    "sre_error_budget": "https://sre.google/workbook/error-budget-policy/",
    "heart_google": "https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/",
    "northstar_amplitude": "https://amplitude.com/blog/good-bad-north-star-metric",
    "aarrr_inc": "https://www.inc.com/walter-chen/aarrr-dave-mcclure-s-pirate-metrics-and-the-only-five-numbers-that-matter.html",
    # --- AI-эра: инструменты / evals / governance ---
    "anthropic_agentic_2026": "https://resources.anthropic.com/2026-agentic-coding-trends-report",
    "bain_ai_pdlc": "https://www.bain.com/insights/the-rise-of-the-ai-development-life-cycle/",
    "reganti_badam_ccdc": "https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different",
    "deepmind_specgaming": "https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/",
    "anthropic_sycophancy_subterfuge": "https://arxiv.org/abs/2406.10162",
    "mtbench_arxiv": "https://arxiv.org/abs/2306.05685",
    "nng_synthetic_users": "https://www.nngroup.com/articles/synthetic-users/",
    "nng_ai_hallucinations": "https://www.nngroup.com/articles/ai-hallucinations/",
    "nng_state_of_ux_2026": "https://www.nngroup.com/articles/state-of-ux-2026/",
    "perplexity_deep_research": "https://www.secondtalent.com/resources/perplexity-deep-research-review/",
    "dovetail_ai": "https://listenlabs.ai/articles/dovetail-ai-qualitative-analysis/",
    "figma_make": "https://www.figma.com/resource-library/ai-design-tools/",
    "google_stitch": "https://www.banani.co/blog/galileo-ai-features-and-alternatives",
    "wcag_acm": "https://dl.acm.org/doi/10.1145/3800424.3800430",
    "gartner_guardian_agents": "https://thehackernews.com/2026/03/5-learnings-from-first-ever-gartner.html",
    "gartner_guardian_forecast": "https://www.gartner.com/en/newsroom/press-releases/2025-06-11-gartner-predicts-that-guardian-agents-will-capture-10-15-percent-of-the-agentic-ai-market-by-2030",
    "deloitte_2026_tech_leadership": "https://www.deloitte.com/us/en/about/press-room/2026-global-technology-leadership-study-release.html",
    "sber_ai_pdlc_role": "https://rabota.sber.ru/search/lider-ai-pdlc-4548579/",
    "llmops_observability": "https://www.confident-ai.com/knowledge-base/compare/top-7-llm-observability-tools",
    "llmops_langsmith_langfuse": "https://www.digitalapplied.com/blog/agent-observability-platforms-langsmith-langfuse-arize-2026",
    "osmani_70": "https://addyo.substack.com/p/the-70-problem-hard-truths-about-ai-assisted-coding",
    # --- Провалы (13 кейсов) ---
    "nng_synthetic_drone": "https://www.nngroup.com/articles/synthetic-users/",
    "fortune_deloitte_australia": "https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund",
    "science_maha_deloitte": "https://www.science.org/content/article/trump-officials-downplay-fake-citations-high-profile-report-children-s-health",
    "damien_charlotin_db": "https://www.damiencharlotin.com/hallucinations/",
    "ibm_watson_statnews": "https://www.statnews.com/2018/07/25/ibm-watson-recommended-unsafe-incorrect-treatments/",
    "ibm_watson_ieee": "https://spectrum.ieee.org/how-ibm-watson-overpromised-and-underdelivered-on-ai-health-care",
    "wapo_characterai": "https://www.washingtonpost.com/nation/2024/10/24/character-ai-lawsuit-suicide/",
    "cbs_characterai_settle": "https://www.cbsnews.com/news/google-settle-lawsuit-florida-teens-suicide-character-ai-chatbot/",
    "eeoc_itutorgroup": "https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit",
    "forbes_google_overviews": "https://www.forbes.com/sites/roberthart/2024/05/31/google-restricts-ai-search-tool-after-nonsensical-answers-told-people-to-eat-rocks-and-put-glue-on-pizza/",
    "androidpolice_google_overviews": "https://www.androidpolice.com/google-pizza-glue-loop-ai-overviews/",
    "cnbc_mcdonalds_ibm": "https://www.cnbc.com/2024/06/17/mcdonalds-to-end-ibm-ai-drive-thru-test.html",
    "nrn_mcdonalds_ibm": "https://www.nrn.com/quick-service/mcdonald-s-is-ending-its-ai-drive-thru-test-with-ibm",
    "techdirt_facebook_msi": "https://www.techdirt.com/2021/10/28/let-me-rewrite-that-you-washington-post-misinforms-you-about-how-facebook-weighted-emoji-reactions/",
    "house_facebook_files": "https://docs.house.gov/meetings/IF/IF16/20211201/114268/HHRG-117-IF16-20211201-SD012.pdf",
    "medpalm2_nature": "https://www.nature.com/articles/s41591-024-03423-7",
    "mata_v_avianca_wiki": "https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.",
    "stanford_reglab": "https://onlinelibrary.wiley.com/doi/full/10.1111/jels.12413",
    "geekwire_zillow": "https://www.geekwire.com/2021/ibuying-algorithms-failed-zillow-says-business-worlds-love-affair-ai/",
    "sec_zillow_10k": "https://www.sec.gov/Archives/edgar/data/1617640/000161764022000013/z-20211231.htm",
    "canlii_air_canada": "https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html",
    "aba_air_canada": "https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/",
    "openai_klarna": "https://openai.com/index/klarna/",
    "bloomberg_klarna": "https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service",
    "fortune_klarna_853": "https://fortune.com/2025/10/10/klarna-ceo-sebastian-siemiatkowski-halved-workforce-says-tech-ceos-sugarcoating-ai-impact-on-jobs-mass-unemployment-warning/",
    "themarkup_nyc_mycity": "https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law",
    "mit_nanda_pdf": "https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf",
    "fortune_mit_nanda": "https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/",
    "80000h_mit_nanda": "https://80000hours.org/podcast/episodes/ai-workplace-mit-study/",
    "newmr_mit_nanda": "https://newmr.org/blog/myth-number-2-mit-showed-that-95-of-ai-pilots-fail/",
    "rand_ai_failure_causes": "https://www.rand.org/pubs/research_reports/RRA2680-1.html",
    "gartner_io_stall_2026": "https://www.gartner.com/en/newsroom/press-releases/2026-04-07-gartner-says-artificial-intelligence-projects-in-infrastructure-and-operations-stall-ahead-of-meaningful-roi-returns",
    "martech_gartner_40pct": "https://martech.org/gartner-40-of-agentic-ai-projects-will-fail-making-humans-indispensable/",
    "bcg_ai_impact_gap": "https://www.bcg.com/publications/2025/closing-the-ai-impact-gap",
    "business_standard_jwo": "https://www.business-standard.com/companies/news/amazon-s-just-walk-out-checkout-tech-was-powered-by-1-000-indian-workers-124040400463_1.html",
    "retaildive_jwo": "https://www.retaildive.com/news/amazon-removes-just-walk-out-tech-amazon-fresh-stores-dash-carts/712150",
}


def refs_of(slide, keys, y=6.70, **kw):
    """Convenience: build the bottom numbered ref list from a list of
    (num, name, urlkey) tuples, resolving urlkey via URLS."""
    entries = [(num, name, URLS.get(k, "")) for (num, name, k) in keys]
    return ref_list(slide, entries, y=y, **kw)

def setup_pres():
    p = Presentation()
    p.slide_width = Inches(SLIDE_W_IN)
    p.slide_height = Inches(SLIDE_H_IN)
    return p


def blank(p):
    return p.slides.add_slide(p.slide_layouts[6])


def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def disable_shadow(shp):
    sppr = shp._element.spPr
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    for el in sppr.findall(ns + "effectLst"):
        sppr.remove(el)
    etree.SubElement(sppr, ns + "effectLst")


# ============================================================
# ПРАВКА 2 (owner refinement) — [N] reference markers "существенно
# меньше" основного текста. After a text frame is built, walk its runs,
# find [N] / [N, M] substrings, and re-split them into a smaller (~52%),
# superscript, muted-colour run. Applied automatically by text_box /
# text_runs / gold_callout / teal_callout so the many baked-in [N] markers
# shrink without rewriting every call site. Bottom ref-lists опускают это
# (они и так мелкие).
# ============================================================
_REF_RE = re.compile(r'\[\d+(?:\s*[,–—-]\s*\d+)*\]')
_AMAIN = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def _run_props(src_run):
    """Read the font props we need to clone from an existing run."""
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
    """Insert a new <a:r> right after anchor_r with cloned props (or a
    small superscript muted variant when ref=True)."""
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
    # font
    if props["name"]:
        for tag in ("latin", "cs", "ea"):
            el = etree.SubElement(rpr, _AMAIN + tag)
            el.set("typeface", props["name"])
    # colour
    col = ref_color if ref else props["color"]
    if col is not None:
        fill = etree.SubElement(rpr, _AMAIN + "solidFill")
        clr = etree.SubElement(fill, _AMAIN + "srgbClr")
        clr.set("val", str(col))
    t = etree.SubElement(new_r, _AMAIN + "t")
    t.text = text
    return new_r


def shrink_refs_in_frame(text_frame, *, ref_frac=0.52, ref_color=LIGHT):
    """Split every [N] marker inside the frame into a small superscript
    muted run. Non-destructive to surrounding text formatting."""
    for para in text_frame.paragraphs:
        # snapshot runs (we mutate the tree while iterating)
        for run in list(para.runs):
            txt = run.text
            if not txt or "[" not in txt:
                continue
            matches = list(_REF_RE.finditer(txt))
            if not matches:
                continue
            props = _run_props(run)
            # first chunk stays in the original run
            run.text = txt[:matches[0].start()]
            anchor = run._r
            pos = matches[0].start()
            for i, m in enumerate(matches):
                # the marker itself (small)
                anchor = _clone_run_after(anchor, props, m.group(),
                                          ref=True, ref_frac=ref_frac,
                                          ref_color=ref_color)
                # the text between this marker and the next (normal)
                nxt = matches[i + 1].start() if i + 1 < len(matches) else len(txt)
                between = txt[m.end():nxt]
                if between:
                    anchor = _clone_run_after(anchor, props, between, ref=False)
                pos = nxt
    return text_frame


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
    # support \n as hard paragraph breaks (#sem01-render-1 workaround)
    lines = text.split("\n")
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for i, line in enumerate(lines):
        if i > 0:
            p = tf.add_paragraph()
            p.alignment = align
            p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
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
            if cfg.get("space_before") is not None:
                p.space_before = Pt(cfg["space_before"])
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
        adj = max(0.035, min(0.22, (radius_pt / 72.0) / max(min(w, h) / 2.0, 0.5)))
        shp.adjustments[0] = adj
    except Exception:
        pass
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    shp.line.color.rgb = stroke; shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def filled_rect(slide, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0,
                radius=False, radius_adj=0.16):
    st = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(st, Inches(x), Inches(y), Inches(w), Inches(h))
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


def right_arrow(slide, x, y, w, h, fill=MID, stroke=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(1.0)
    disable_shadow(shp)
    return shp


def circle(slide, x, y, d, fill, *, stroke=None, stroke_pt=1.0):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                 Inches(x), Inches(y), Inches(d), Inches(d))
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    disable_shadow(shp)
    return shp


def chip(slide, x, y, w, h, text, *, fill=MID, stroke=None, color=WHITE,
         size=13, bold=True):
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
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.name = FONT_BODY; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    disable_shadow(shp)
    return shp


def connector(slide, x1, y1, x2, y2, color=LIGHT, width=2.0, dash=None,
              arrow_end=False, arrow_len="med", arrow_w="med"):
    """arrow_end=True adds a tailEnd arrowhead at (x2,y2) — used for
    schema_cycle diagrams that need an explicit read direction (e.g. s03
    GATE-B fix: the loop nodes had connecting lines but no arrowheads, so a
    student could not tell the ring had a direction of travel)."""
    cn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                    Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    cn.line.color.rgb = color
    cn.line.width = Pt(width)
    if dash:
        ln = cn.line._get_or_add_ln()
        pd = etree.SubElement(
            ln, "{http://schemas.openxmlformats.org/drawingml/2006/main}prstDash")
        pd.set("val", dash)
    if arrow_end:
        ln = cn.line._get_or_add_ln()
        tail = etree.SubElement(ln, _AMAIN + "tailEnd")
        tail.set("type", "triangle")
        tail.set("w", arrow_w)
        tail.set("len", arrow_len)
    return cn


def add_image(slide, path, x, y, w=None, h=None, preserve_aspect=True):
    """[#73-render-1] aspect-safe; [#156-1] fixed h-only branch."""
    path = Path(path)
    if not path.exists():
        return
    if preserve_aspect and w is not None and h is not None:
        try:
            img = Image.open(path); iw, ih = img.size; img.close()
        except Exception:
            slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                     width=Inches(w))
            return
        ir = iw / ih; br = w / h
        if ir > br:
            ah = w / ir
            slide.shapes.add_picture(str(path), Inches(x),
                                     Inches(y + (h - ah) / 2), width=Inches(w))
        else:
            aw = h * ir
            slide.shapes.add_picture(str(path), Inches(x + (w - aw) / 2),
                                     Inches(y), height=Inches(h))
    elif w is not None and h is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
    elif w is not None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 width=Inches(w))
    elif h is not None:                          # [#156-1] fix
        slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                 height=Inches(h))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y))


def slide_title(slide, text, *, y=0.40, h=0.92, w=12.25, x=0.55, size=26,
                color=DEEP, bold=True, line_spacing=1.10, align=PP_ALIGN.LEFT):
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, bold=bold, color=color, line_spacing=line_spacing,
             align=align)


def gold_callout(slide, x, y, w, h, text, *, size=15, bold=True,
                 color=DEEP, align=PP_ALIGN.LEFT, stroke_pt=1.5):
    filled_rect(slide, x, y, w, h, GOLD_TINT, stroke=GOLD, stroke_pt=stroke_pt,
                radius=True, radius_adj=0.10)
    text_box(slide, x=x + 0.24, y=y + 0.06, w=w - 0.48, h=h - 0.12, text=text,
             size=size, bold=bold, color=color, anchor=MSO_ANCHOR.MIDDLE,
             align=align, line_spacing=1.20)


def teal_callout(slide, x, y, w, h, text, *, size=14, bold=False,
                 color=DEEP, align=PP_ALIGN.LEFT):
    filled_rect(slide, x, y, w, h, TEAL_TINT, stroke=TEAL, stroke_pt=1.5,
                radius=True, radius_adj=0.10)
    text_box(slide, x=x + 0.24, y=y + 0.06, w=w - 0.48, h=h - 0.12, text=text,
             size=size, bold=bold, color=color, anchor=MSO_ANCHOR.MIDDLE,
             align=align, line_spacing=1.18)


def footer(slide, text):
    text_box(slide, x=0.55, y=7.04, w=12.25, h=0.34, text=text,
             size=12, italic=True, color=LIGHT, align=PP_ALIGN.LEFT,
             line_spacing=1.0)


def src(slide, x, y, w, text, *, size=9, color=LIGHT, align=PP_ALIGN.LEFT,
        h=0.22):
    """Inline muted source caption placed RIGHT AT the material it backs
    (definition / claim / recommendation), not in a bottom footer.
    Small, italic, muted — reads as attribution, not body."""
    text_box(slide, x=x, y=y, w=w, h=h, text=text,
             size=size, italic=True, color=color, align=align,
             line_spacing=1.0)


def icon(slide, name, x, y, size, variant="mid"):
    add_image(slide, ICONS / f"{name}-{variant}.png", x, y, size, size)


MEMES = ASSETS / "memes-en"
SCR = ASSETS / "screenshots"


def meme_in_box(slide, fname, x, y, w, h, *, pad=0.10):
    """Frame a meme (assets/memes/<fname>) inside an Ocean rounded box —
    on-brand container so the raw meme never floats. Aspect-preserved."""
    ocean_box(slide, x, y, w, h, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(slide, MEMES / fname, x + pad, y + pad, w - 2 * pad, h - 2 * pad,
              preserve_aspect=True)


def photo_in_box(slide, fname, x, y, w, h, *, pad=0.10, fill=WHITE):
    """Frame a real photo/logo (assets/screenshots/<fname>) in an Ocean box.
    NO attribution caption burned on-slide (owner rule); source lives in the
    .url sidecar + iteration-log only."""
    ocean_box(slide, x, y, w, h, fill=fill, stroke=LIGHT, stroke_pt=1.5)
    add_image(slide, SCR / fname, x + pad, y + pad, w - 2 * pad, h - 2 * pad,
              preserve_aspect=True)


def eli5_overview(p, sid, *, title, cards, icon_name, icon_variant="mid"):
    """«Для чайников» section-overview slide (Directive 3): big left icon +
    3 plain-language cards (Что это / Зачем / Ментальная модель). Dual-audience:
    plain for weaker students, skimmable for the strong majority. Gold accent on
    the first card's label + a gold chip «простыми словами».

    GATE-B fix (audit 2026-09-07): the template used to stop at y~5.65,
    leaving a ~25-30% empty band at the bottom on all 7 ELI5 instances. Both
    the left icon tile and the 3 right-column cards now stretch down to
    y~6.85 (card height 1.18->1.55in, gap 0.20->0.25in; icon tile height
    3.95->5.15in with the icon + chip re-centred within the taller tile) so
    the template fills the same footprint the content-slide gold_callout
    convention uses elsewhere in the deck — no dead space below either
    column."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, title, size=26, w=12.0, h=0.85)
    # left hero icon in a soft tile — stretched to match the new card-column
    # height (y0=1.70 .. ~6.85 = 5.15in tall)
    tile_h = 5.15
    filled_rect(s, 0.55, 1.70, 2.75, tile_h, SURFACE, stroke=LIGHT,
                stroke_pt=1.5, radius=True, radius_adj=0.06)
    icon(s, icon_name, 1.35, 1.70 + tile_h * 0.36, 1.15, icon_variant)
    chip(s, 0.85, 1.70 + tile_h - 0.60, 2.15, 0.44, "in plain terms",
         fill=GOLD, color=DEEP, size=11.5)
    # 3 cards on the right — grown to fill the same vertical span
    cx, cw = 3.65, 9.15
    ch, gap = 1.55, 0.25
    y0 = 1.70
    for i, (label, body) in enumerate(cards):
        y = y0 + i * (ch + gap)
        lab_col = GOLD if i == 0 else MID
        ocean_box(s, cx, y, cw, ch, fill=SURFACE, stroke=LIGHT, stroke_pt=1.4)
        text_box(s, x=cx + 0.28, y=y + 0.16, w=cw - 0.56, h=0.34, text=label,
                 size=15, bold=True, color=lab_col)
        text_box(s, x=cx + 0.28, y=y + 0.56, w=cw - 0.56, h=ch - 0.72,
                 text=body, size=13.5, color=DEEP, line_spacing=1.22)
    notes_with_sources(s, sid)
    return s


# ============================================================
# ПРАВКА 1 (#269 + #266a) — numbered reference system
# Compact [N] markers at the claim + a small muted CLICKABLE numbered
# source list at the bottom of the slide. URLs come ONLY from the research
# URL map (references-and-req-engineering.md, Deliverable 2).
# ============================================================
def ref_list(slide, entries, *, y=6.70, x=0.55, w=12.25, h=0.60,
             size=8.5, color=LIGHT, line_spacing=1.02, cols=None):
    """Bottom numbered clickable source list.

    entries: list of (num:str, name:str, url:str). Renders «[N] name»
    where name is a clickable hyperlink (run.hyperlink.address = url).
    Muted, italic, small — reads as attribution, never a text-wall.
    Kept to 1–2 visual lines; entries are separated by «   ·   ».
    """
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
        # marker [N]
        rm = p.add_run()
        rm.text = f"[{num}] "
        rm.font.name = FONT_BODY; rm.font.size = Pt(size)
        rm.font.bold = True; rm.font.italic = True
        rm.font.color.rgb = MID
        # clickable name
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
        # separator
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


def page_number(slide, n, total=None, *, color=SLATE):
    """Small muted page-number stamp in the bottom-right corner.

    Placed at the very bottom-right (x≈12.55, y≈7.16), 10pt italic muted, so it
    never overlaps the left-aligned footer / ref-list (x=0.55) nor the roadmap
    bar (ends y≈7.13). Format «N / TOTAL» when total is given, else «N».
    Applied to every slide by the assembler (build_lec04_v4.py) so all 41
    slides carry it without touching per-slide builders."""
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


def speaker_notes(slide, text):
    """Write notes as readable PARAGRAPHS (ПРАВКА 1, owner refinement):
    split on blank lines → one notes-paragraph each, so notes are never a
    single wall of text."""
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    # normalise: collapse single newlines inside a paragraph to spaces,
    # split into paragraphs on blank lines.
    blocks = [b.strip() for b in re.split(r'\n\s*\n', text.strip()) if b.strip()]
    if not blocks:
        blocks = [""]
    for i, block in enumerate(blocks):
        # keep intentional hard line breaks inside a "Sources:" block
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


def load_notes(slide_id):
    files = list(SLIDES_DIR.glob(f"{slide_id}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r'## Speaker notes\s*\n(.*?)(?=\n## |\n---\s*\n## |\Z)',
                  md, re.DOTALL)
    notes = m.group(1).strip() if m else ""
    notes = re.sub(r'\n+---\s*$', '', notes)
    return notes.strip()


# ============================================================
# lec-05 source handling: SIMPLE — no clickable [N] registry. Each slide's
# `source:` frontmatter (if present) is surfaced as a small muted inline
# caption via src() near the relevant claim (owner rule: no attribution
# LABELS on images, but textual source captions for stats/claims are fine
# and required by fact-integrity). notes_with_sources() reduces to plain
# speaker_notes(load_notes(sid)) plus, if the frontmatter has `source:`,
# one small "Источник:" line appended so the lecturer has it without it
# ever appearing on the visible slide body.
# ============================================================
def _frontmatter_source(sid):
    files = list(SLIDES_DIR.glob(f"{sid}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    m = re.search(r'^source:\s*"?(.+?)"?\s*$', md, re.MULTILINE)
    if not m:
        return ""
    line = m.group(1).strip()
    # strip internal-only markers — [FACT-CHECK] / [VFY-day-of] etc. are
    # frontmatter-only bookkeeping tags, NOT allowed in speaker notes body
    # (owner rule: 0 hits in visible body + speaker_notes).
    line = re.sub(r'\s*\[[A-Z-]+(?:-day-of)?\]\s*', ' ', line).strip()
    return line


# ============================================================
# ПРАВКА 1 (issue #189 rebuild) — per-slide source registry, ported
# verbatim from lec-04's mechanism. ONE definition per display-slide id
# drives BOTH:
#   • the bottom clickable [N] list on the slide (refs_of_slide), and
#   • the «Источники:» block appended to the speaker notes (notes_sources_block).
# So slide-[N] and notes-[N] can never diverge. Entry:
#   (num:str, short_name:str, urlkey:str, gloss:str[, volatile:bool])
# gloss = one phrase: what the source says / why authoritative.
# volatile → «[VFY-day-of]» appended in notes only.
# URLs resolved ONLY via URLS (notes/research/lecture-5-pdlc/*.md +
# chapter-part4.md «Источники»). No invented URLs.
# ============================================================
SLIDE_REFS = {
    "s01": [
        ("1", "Anthropic — 2026 Agentic Coding Trends Report",
         "anthropic_agentic_2026",
         "internal experience: weeks -> hours; secondary-triangulated (PDF "
         "not parsed directly)", True),
        ("2", "MIT NANDA — \"The GenAI Divide\" (July 2025, v0.1)",
         "mit_nanda_pdf",
         "\"95% of pilots — zero return\": unreviewed preprint, needs "
         "calibration (see s47)", True),
    ],
    "s08": [
        ("1", "Blank — Customer Development (Four Steps to the Epiphany)",
         "blank_custdev",
         "4-step methodology; \"there are no facts inside the building\""),
    ],
    "s09": [
        ("1", "Fitzpatrick — The Mom Test", "mom_test",
         "3 interview rules: about life/about the past/about a commitment, "
         "not an opinion"),
    ],
    "s10": [
        ("1", "Perplexity Deep Research — overview for product research",
         "perplexity_deep_research",
         "desk research: hours -> minutes; source verification still needed"),
        ("2", "Dovetail — AI interview synthesis", "dovetail_ai",
         "pain-point clustering at scale; limits of AI summarization"),
        ("3", "NN/g — 2026 practitioner survey", "nng_state_of_ux_2026",
         "97% of researchers use AI, ~8% trust AI personas as data", True),
    ],
    "s11": [
        ("1", "Torres — Continuous Discovery Habits / anti-synthetic",
         "torres_ai_anti_synth",
         "a contrarian-to-hype stance: against synthetic interviews and "
         "one-click AI persona trees"),
    ],
    "s12": [
        ("1", "NN/g (Rosala & Moran) — Synthetic Users",
         "nng_synthetic_users",
         "3/7 real vs 7/7 synthetic on the same task (drone-delivery)",
         True),
    ],
    "s13": [
        ("1", "Fortune (Oct 7, 2025) — Deloitte Australia A$440k",
         "fortune_deloitte_australia",
         "fabricated quotes and nonexistent references in a government "
         "report"),
        ("2", "Damien Charlotin — AI Hallucination Cases Database",
         "damien_charlotin_db",
         "~712 documented court cases worldwide involving AI "
         "hallucinations", True),
    ],
    "s13a": [
        ("1", "STAT News — leaked internal IBM Watson documents",
         "ibm_watson_statnews",
         "\"unsafe and incorrect\" oncology recommendations (July 25, "
         "2018)"),
        ("2", "IEEE Spectrum — how Watson overpromised and underdelivered",
         "ibm_watson_ieee",
         "trained on hypothetical cases from a handful of MSK oncologists, "
         "not on real outcomes"),
    ],
    "s15": [
        ("1", "UK Design Council — The Double Diamond", "double_diamond",
         "Discover->Define->Develop->Deliver: two cycles of divergence/"
         "convergence"),
    ],
    "s16": [
        ("1", "Nielsen — 10 usability heuristics", "nielsen_heuristics",
         "the full list of 10 heuristics with examples (1994, rev. 2020)"),
        ("2", "Nielsen — \"you are not the user\"", "nielsen_not_user",
         "a warning about the atypicality of insider designers"),
    ],
    "s17": [
        ("1", "Figma — 2026 AI design tools", "figma_make",
         "Figma Make, v0, Stitch, bolt.new — 2-4 directions in minutes",
         True),
        ("2", "Google Stitch (ex-Galileo AI)", "google_stitch",
         "Google acquisition, May 2025 — a fast-moving tool landscape",
         True),
    ],
    "s18": [
        ("1", "ACM Web4All 2026 — Generated Inaccessible", "wcag_acm",
         "21,880 WCAG evaluations on AI-generated interfaces, 29.0% "
         "compliance (contrast 26.8%, color 19.2%)", True),
    ],
    "s19": [
        ("1", "Washington Post (Oct 24, 2024)", "wapo_characterai",
         "a 14-year-old user's death after months of conversation with an "
         "AI character"),
        ("2", "CBS News (Jan 2026) — settlement", "cbs_characterai_settle",
         "Character.AI/Google — safeguards retrofitted after the "
         "tragedy"),
    ],
    "s20": [
        ("1", "EEOC (Aug 9, 2023) — iTutorGroup", "eeoc_itutorgroup",
         "the first AI-discrimination settlement: $365,000, automatic "
         "age-based rejection"),
    ],
    "s22": [
        ("1", "Ries — Lean Startup / MVP", "lean_startup_vanity",
         "MVP as a learning tool, not a stripped-down shipment; the risk "
         "of vanity metrics"),
        ("2", "Stage-Gate — the method's history", "stage_gate_story",
         "a go/kill gate: \"a funnel, not a tunnel\", failure thresholds "
         "set in advance"),
    ],
    "s23": [
        ("1", "Anthropic — 2026 Agentic Coding Trends Report",
         "anthropic_agentic_2026",
         "+200% code per engineer year over year; only ~16% of PRs get "
         "substantive human review before merge", True),
    ],
    "s24": [
        ("1", "Reganti & Badam — CC/CD framework", "reganti_badam_ccdc",
         "Continuous Calibration/Development; a ladder of agency "
         "(Copilot->Cursor); \"not ready to grant high agency\""),
    ],
    "s25": [
        ("1", "Osmani — The 70% Problem", "osmani_70",
         "AI gets teams ~70% of the way; a \"house of cards of code\" — "
         "a novice can't close the remaining 30%"),
    ],
    "s26": [
        ("1", "Forbes (May 31, 2024) — Google AI Overviews",
         "forbes_google_overviews",
         "a full rollout to 100% of US search in one step, with no "
         "canary stages"),
        ("2", "AndroidPolice — \"glue on pizza\" / \"eat rocks\"",
         "androidpolice_google_overviews",
         "viral incidents hit the full audience at once, reactive "
         "post-release fixes"),
    ],
    "s27": [
        ("1", "CNBC (June 17, 2024) — McDonald's x IBM", "cnbc_mcdonalds_ibm",
         "the decision to end the pilot after 2.5-3 years at 0.7% of the "
         "chain (~100 of ~13,786 restaurants)"),
        ("2", "Nation's Restaurant News — details of the pilot shutdown",
         "nrn_mcdonalds_ibm",
         "deactivation by July 26, 2024; the goal stayed, the vendor "
         "approach was killed"),
    ],
    "s29": [
        ("1", "Kohavi — Overall Evaluation Criterion (OEC)", "kohavi_oec",
         "a metric whose meaning and direction are agreed BEFORE the "
         "test; the classic trap: \"time on the support site\""),
        ("2", "Wikipedia — A/B testing (Bing 2012)", "kohavi_bing_ab",
         "an ad headline: +12% revenue (~$100M), independent of Kohavi's "
         "own materials"),
    ],
    "s30": [
        ("1", "Microsoft Research — Sample Ratio Mismatch (KDD 2019)",
         "srm_microsoft",
         "\"fever is a symptom\": SRM is a symptom of data-quality "
         "problems, checked before analyzing the effect"),
        ("2", "GoPractice — the peeking problem",
         "gopractice_peeking",
         "2 peeks ~= 2x false positives; the fix is a pre-registered "
         "sample size"),
        ("3", "exp-platform.com — Kohavi, Twyman", "exp_platform",
         "\"any figure that looks interesting is usually wrong\" — "
         "recheck the methodology before celebrating"),
    ],
    "s31": [
        ("1", "Anthropic — Demystifying evals for AI agents (Jan 9, 2026)",
         "anthropic_agentic_2026",
         "pass@k (at least 1 success) vs pass^k (all succeed); production "
         "reliability requires pass^k", True),
        ("2", "Zheng, Chiang et al. — MT-Bench (NeurIPS 2023)",
         "mtbench_arxiv",
         "LLM-judge ~85% agreement with experts — comparable to ~81% "
         "human-human agreement"),
    ],
    "s32": [
        ("1", "DeepMind — Specification gaming (Apr 21, 2020)",
         "deepmind_specgaming",
         "CoastRunners: an RL agent scored 20% higher than humans by "
         "circling a lagoon, never finishing — Goodhart's law"),
        ("2", "Anthropic — Sycophancy to Subterfuge (arXiv:2406.10162)",
         "anthropic_sycophancy_subterfuge",
         "a model generalized from sycophancy to directly editing its own "
         "reward function"),
    ],
    "s33": [
        ("1", "Techdirt (Oct 28, 2021) — correcting the \"Facebook Files\"",
         "techdirt_facebook_msi",
         "all 5 reactions (love/haha/wow/sad/angry) were weighted x5 "
         "equally — not just \"anger\", contrary to the widely-repeated "
         "version"),
        ("2", "House E&C Committee — the Haugen documents",
         "house_facebook_files",
         "an internal guardrail (anger<->misinformation correlation) "
         "confirmed by 2019, the weight zeroed out in September 2019"),
    ],
    "s34": [
        ("1", "Med-PaLM 2 — Nature Medicine 2024 (arXiv:2305.09617)",
         "medpalm2_nature",
         "86.5% on the MedQA benchmark is not the same thing as clinical "
         "safety in production"),
        ("2", "Wikipedia — Mata v. Avianca", "mata_v_avianca_wiki",
         "the fake citations were ChatGPT, NOT Harvey — a common "
         "attribution mistake; a $5,000 sanction (S.D.N.Y., June 22, "
         "2023)"),
        ("3", "Stanford RegLab — J. Empirical Legal Studies",
         "stanford_reglab",
         "Lexis+ 17% / Westlaw 33% / GPT-4 88% hallucination rates on "
         "real legal queries"),
    ],
    "s37": [
        ("1", "Google SRE — Error Budget Policy", "sre_error_budget",
         "SLI/SLO/error budget = \"1 - SLO\"; changes cause ~=70% of all "
         "outages"),
    ],
    "s38": [
        ("1", "Confident AI — 2026 LLMOps observability overview",
         "llmops_observability",
         "LangSmith / Langfuse / Arize Phoenix / Helicone — tracing "
         "catches drift where infra monitoring stays silent", True),
        ("2", "Gartner Market Guide for Guardian Agents (Feb 25, 2026)",
         "gartner_guardian_agents",
         "the category definition; 70%/23% adoption", True),
    ],
    "s40": [
        ("1", "GeekWire (Nov 2021) — Zillow Offers", "geekwire_zillow",
         "$304-408M in write-downs, ~2,000 laid off (~25% of staff), "
         "~=$80K loss per home"),
        ("2", "SEC 10-K FY2021 — Zillow Group", "sec_zillow_10k",
         "the official financial filing confirming the scale of the "
         "write-downs"),
    ],
    "s41": [
        ("1", "CanLII — Moffatt v. Air Canada, 2024 BCCRT 149",
         "canlii_air_canada",
         "the tribunal: the company is liable for the bot's answer like "
         "any other site content; $812.02 CAD (Feb 14, 2024)"),
        ("2", "American Bar Association — case commentary",
         "aba_air_canada",
         "legal analysis: \"bot as a separate legal entity\" dismissed in "
         "one line"),
    ],
    "s42": [
        ("1", "Bloomberg (May 8, 2025) — Klarna", "bloomberg_klarna",
         "a reversal of the \"AI-only\" policy back to hiring people"),
        ("2", "Fortune (Oct 10, 2025) — 853 FTE", "fortune_klarna_853",
         "automation grew to 853 human-equivalents — augmenting people, "
         "not replacing them; the exact figure surfaces later in "
         "Klarna's Q3 filing (Nov 18, 2025) — verify before publication",
         True),
        ("3", "The Markup (Mar 29, 2024) — NYC MyCity", "themarkup_nyc_mycity",
         "a government chatbot gave 10 of 10 journalists the same "
         "illegal advice"),
    ],
    "s46": [
        ("1", "Deloitte — 2026 Global Technology Leadership Study",
         "deloitte_2026_tech_leadership",
         "75% say the operating model must change; 42% low/zero ROI; 81% "
         "confident despite the internal contradiction", True),
        ("2", "Sber — the \"AI PDLC Lead\" job posting", "sber_ai_pdlc_role",
         "the organizational reality of the role, not just a whitepaper "
         "concept", True),
    ],
    "s47": [
        ("1", "MIT NANDA — \"The GenAI Divide\" (July 2025, v0.1)",
         "mit_nanda_pdf",
         "an unreviewed preprint: the 60%->20%->5% funnel is 25% among "
         "those who reached a pilot, not \"95% failure\"", True),
        ("2", "Fortune (Aug 18, 2025) — media distortion of the MIT report",
         "fortune_mit_nanda",
         "how the \"95% failure\" headline spread without calibrating "
         "the denominator"),
        ("3", "NewMR — Myth #2", "newmr_mit_nanda",
         "an analysis of the conflict of interest and the denominator in "
         "citations of the MIT report"),
        ("4", "Gartner (Apr 7, 2026, 782 I&O leaders)",
         "gartner_io_stall_2026",
         "28% of AI use cases in I&O are fully successful; 20% fail",
         True),
        ("5", "BCG — Closing the AI Impact Gap",
         "bcg_ai_impact_gap",
         "60% of companies track zero financial KPIs tied to AI value; "
         "the publish date on BCG's site differs from the date in the "
         "research dossier — see owner follow-up", True),
    ],
    "s48": [
        ("1", "Business Standard (Apr 2024) — Just Walk Out",
         "business_standard_jwo",
         "700 of 1,000 transactions required manual review by Indian "
         "workers — against a target of 50/1,000"),
        ("2", "Retail Dive — the dismantling of Just Walk Out",
         "retaildive_jwo",
         "the technology pulled from Amazon Fresh; 27 of 44 stores lose "
         "the feature"),
    ],
}


def _resolve_refs(sid):
    out = []
    for entry in SLIDE_REFS.get(sid, []):
        num, name, urlkey, gloss = entry[0], entry[1], entry[2], entry[3]
        volatile = len(entry) > 4 and entry[4]
        out.append((num, name, URLS.get(urlkey, ""), gloss, volatile))
    return out


def refs_of_slide(slide, sid, *, y=None, size=8.5):
    """Bottom clickable [N] list for a display slide, sourced from
    SLIDE_REFS. Skips silently if the slide has no registry entry."""
    resolved = _resolve_refs(sid)
    if not resolved:
        return None
    entries = [(num, name, url) for (num, name, url, gloss, vol) in resolved]
    yy = y if y is not None else (7.06 if len(entries) <= 2 else 7.02)
    sz = size if len(entries) <= 4 else 8.0
    return ref_list(slide, entries, y=yy, size=sz)


def notes_sources_block(sid):
    """Build the «Источники:» text block for the speaker notes of a display
    slide: numbered [N] + FULL URL + one gloss phrase; volatile → [VFY-day-of].
    Returns "" when the slide has no registry entry."""
    resolved = _resolve_refs(sid)
    if not resolved:
        return ""
    lines = ["Sources:"]
    for (num, name, url, gloss, vol) in resolved:
        vfy = " [VFY-day-of]" if vol else ""
        lines.append(f"[{num}] {name} — {gloss}. {url}{vfy}")
    return "\n".join(lines)


def notes_with_sources(slide, sid):
    """Write speaker notes (paragraph-formatted) with the «Источники:» block
    appended. Single call replaces speaker_notes(slide, load_notes(sid))."""
    body = load_notes(sid)
    block = notes_sources_block(sid)
    text = f"{body}\n\n{block}" if block else body
    speaker_notes(slide, text)



# ============================================================
# Section divider — unified template (7-card roadmap, gold current)
# Sections of Лекции 5 (product loop): 0..6.
# ============================================================
NAV = [
    ("0", "Intro"),
    ("1", "Discovery"),
    ("2", "Design"),
    ("3", "Build & Launch"),
    ("4", "Measure"),
    ("5", "Support"),
    ("6", "Governance"),
]


def roadmap_bar(slide, here_idx, *, y=6.55):
    """7-card progress bar; current section gold-bordered."""
    n = len(NAV)
    gap = 0.10
    bx = 0.55
    total_w = 12.25
    cw = (total_w - gap * (n - 1)) / n
    ch = 0.58
    for i, (num, label) in enumerate(NAV):
        x = bx + i * (cw + gap)
        cur = (i == here_idx)
        if cur:
            filled_rect(slide, x, y, cw, ch, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.12)
        else:
            filled_rect(slide, x, y, cw, ch, SURFACE, stroke=SOFT_GREY,
                        stroke_pt=1.0, radius=True, radius_adj=0.12)
        text_box(slide, x=x + 0.02, y=y + 0.05, w=cw - 0.04, h=0.18,
                 text=num, size=10.5, bold=True,
                 color=(DEEP if cur else LIGHT), align=PP_ALIGN.CENTER)
        # longer RU labels need a smaller size + tight wrap to fit 2 lines
        lbl_sz = 8.0 if len(label) > 9 else 9.0
        text_box(slide, x=x + 0.02, y=y + 0.25, w=cw - 0.04, h=0.30,
                 text=label, size=lbl_sz, bold=cur,
                 color=(DEEP if cur else SLATE), align=PP_ALIGN.CENTER,
                 line_spacing=0.92)


def build_section_divider(p, here_idx, subtitle, bridge, sid, tag=None,
                          icon_name=None, meme_name=None):
    """Distinct divider (NO ocean motif): giant decorative section digit on
    the right (soft outline), РАЗДЕЛ N + subtitle + 1-line narrative bridge on
    the left, gold-current roadmap bar at bottom.

    lec-05: `tag` is a short content-tag (e.g. "2 базы · 3 провала" — counts,
    NEVER minutes — see No-Timing-No-Methodology rule) rendered as a gold chip
    under the subtitle. `meme_name` (Directive 2) frames THIS divider's own
    evergreen meme (imgflip template + RU caption) on the right, replacing the
    plain giant digit as the hero. `icon_name` fallback if no meme."""
    s = blank(p)
    set_slide_bg(s, SURFACE)
    if meme_name:
        # meme is the right-side hero, framed in an Ocean box; small ghost digit
        text_box(s, x=10.35, y=0.10, w=2.9, h=1.3, text=str(here_idx),
                 size=90, bold=True, color=COVER_OUTLINE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        meme_in_box(s, meme_name, 8.35, 1.35, 4.45, 4.55, pad=0.14)
    else:
        text_box(s, x=8.55, y=0.20, w=4.5, h=5.8, text=str(here_idx),
                 size=400, bold=True, color=COVER_OUTLINE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        if icon_name:
            icon(s, icon_name, 9.55, 1.35, 1.6, "light")
    text_box(s, x=0.75, y=1.55, w=7.3, h=0.55,
             text=f"SECTION {here_idx}", size=20, bold=True, color=TEAL)
    # GATE-B fix: removed the decorative gold accent-line under "SECTION N"
    # (named course anti-pattern — decorative underline, no semantic value).
    # The subtitle now simply follows with a bit more top space; the gold
    # chip/tag below still carries this divider's ≥1x gold requirement.
    text_box(s, x=0.75, y=2.62, w=7.3, h=1.75, text=subtitle,
             size=30, bold=True, color=DEEP, line_spacing=1.08)
    if tag:
        chip(s, 0.78, 4.20, 3.6, 0.42, tag, fill=GOLD, color=DEEP, size=12.5)
    text_box(s, x=0.78, y=4.80, w=7.35, h=1.55, text=bridge,
             size=15, italic=True, color=LIGHT, line_spacing=1.16)
    roadmap_bar(s, here_idx, y=6.55)
    notes_with_sources(s, sid)
    return s
