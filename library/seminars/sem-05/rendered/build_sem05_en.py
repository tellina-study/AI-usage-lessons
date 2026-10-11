#!/usr/bin/env python3
"""EN render driver for Семинар 5 — thin driver over the untouched RU builder.

Design (same decision as sem-04's D1: "parameterize, don't fork")
-----------------------------------------------------------------
Not a fork of ``build_sem05.py``. This file imports it as a module, points it
at the EN sources, and patches the few places that would otherwise read
Russian::

    slides-en/*.md ──┐
    deck.en.yaml ────┼─► build_sem05.py (UNCHANGED, 1447 lines) ─► sem-05-en.pptx
    sem-05.strings.en.json ─┘   + deck_kit.py (UNCHANGED, 1221 lines)

The RU render stays byte-identical **by construction**: the RU scripts are
never edited, ``sem-05.pptx`` is never written by this file (explicit guard in
``_save_guard``), and ``refresh_manifest()`` — the one thing in the RU builder
that writes back to ``deck.yaml`` — is skipped by the RU builder itself for any
deck file other than ``deck.yaml`` (``build_sem05.main``: ``if not block and
deck_file == "deck.yaml"``).

**"By construction" is the only protection available here, and that is a
measured fact, not a stylistic preference.** ``build_sem05.py`` is NOT
byte-reproducible: three consecutive rebuilds of the unmodified RU deck
produced three different files (sha256 ``8c3026fd…``, ``f1d26a88…``,
``2b46be0a…``), because python-pptx stamps the zip entries it writes. So there
is no hash a reviewer can compare to prove the RU render survived, and
re-running the RU builder "just to check" actively destroys the committed
artifact — it has to be restored with ``git checkout`` afterwards. Hence:
do not run ``build_sem05.py`` as part of EN work. ``--selftest`` below exists
precisely so the harness can be proven transparent *without* it, by comparing
slide CONTENT (shape types, geometry, run texts, notes) against the committed
``sem-05.pptx`` rather than comparing bytes.

How sem-05 differs from sem-04, and why the patch surface is SMALLER
--------------------------------------------------------------------
sem-04 needed a large RU→EN string table because its slide bodies were
hardcoded inside 57 ``build_sNN`` functions. sem-05 reads **every** visible
string from ``deck.yaml`` + ``slides/nNN-*.md`` (``build_sem05.main``:
``md = (ROOT / s["file"]).read_text()`` → ``slide_parts.sections`` →
``slide_parts.blocks``). So pointing the builder at ``slides-en/`` translates
the body **at source**, and the real layout code then measures English text.

That matters more here than it did for sem-04. sem-04 picked geometry from
``len(title)`` buckets, which is why its EN track hit two silent clipping
defects (s19/s21: an EN title crossed a bucket boundary and shifted every
shape below it). sem-05 does not bucket anything — ``metrics.py`` measures the
real wrapped text with PIL font metrics, ``deck_kit`` lays out from a cursor,
and ``build_sem05.measure()`` gets a block's height by drawing it on a scratch
slide and throwing the slide away. Feed it English and it measures English.
**That whole class of defect cannot occur here**, so there is no geometry patch
in this file at all — a deliberate absence, not an omission.

Verified mechanically rather than by eye (AST scan over the whole import graph,
not grep — see ``--audit``):

* Run-text sinks: **2**, both in ``deck_kit.py`` — ``text_box()`` (l.143-144)
  and ``write_notes()`` (l.1108-1119). ``build_sem05.py``, ``metrics.py`` and
  ``slide_parts.py`` contain **zero**.
* Of the 196 live (non-docstring) Cyrillic literals in the import graph, all but
  the handful listed in ``CHROME`` below go to ``metrics._WARNINGS`` /
  ``deck_kit.Claims`` / ``label=`` kwargs — developer diagnostics that are never
  drawn on a slide and are deliberately left in Russian.

The one real blocker sem-04 did not have: layout decided by Russian TEXT
-----------------------------------------------------------------------
``build_sem05.quote_role()`` (l.682-698) decides a block's **visual role** —
and therefore its shape, fill and border — by matching the Russian text:

* ``ASK`` (l.660) ``выберите|что бы вы|как бы вы|назовите|подумайте`` → a gold
  question box, because a question to the room often is not punctuated with "?"
  (two of 68 slides are);
* ``CAVEAT_OPEN`` (l.677) / ``CAVEAT`` (l.678) → a dashed caveat plate;
* ``body.lstrip().startswith("«")`` (l.696-697) → the quiet "speech" form.

Fed English, all four silently mis-fire, and D5 (EN uses ``"…"``, never ``«»``)
guarantees the guillemet test fails on every EN quote. Nothing would warn: the
deck would simply render with the wrong visual semantics — gold boxes missing,
caveats drawn as conclusions, quotes drawn as facts. This is exactly the defect
class the RU builder's own comments say the deck "burned on three times"
(``FIGS`` by number, ``TAGS`` by number, decision-point numbers).

Fixed in two halves, neither of which is a guess:

1. The four objects are rebound to **bilingual** patterns (``ASK_EN`` etc.),
   with the glossary's own EN wordings as the source of the alternatives.
2. ``--roles`` proves it. It builds the role decision for every block of every
   slide twice — once from ``slides/`` and once from ``slides-en/`` — and
   reports any block whose role differs. A role-parity failure is a **build
   failure**, not a warning. The invariant is checked, not hoped for.

Figures are NOT solved by this file, and it says so out loud
------------------------------------------------------------
48 PNGs under ``figures/`` are generated by 7 ``make_figures*.py`` scripts
carrying **682** live Russian string literals baked into the raster; 13 of the
68 n-slides reference one. No string patch can reach them, and they are not
plain translation work either: the generators place text at fixed pixel
coordinates with ``limit=`` guards, so longer English overflows and the figures
need re-laying-out, not just re-wording.

This driver therefore looks for ``figures-en/<name>`` first and falls back to
the Russian ``figures/<name>`` — but **never silently**: every fallback is
reported as ``РУССКАЯ СХЕМА [nNN]`` and counted in the final line. See
``EN-TRACK-BRIEF.md`` §"Figures" for the owner decision this needs.

Modes
-----
``(no args)``   render ``sem-05-en.pptx`` from ``deck.en.yaml`` + ``slides-en/``.
``--selftest``  run this same patched harness with an **identity** chrome table
                over the RU ``deck.yaml`` + ``slides/``, into a temp file, and
                compare it shape-for-shape against the committed
                ``sem-05.pptx``. Proves the harness is transparent — that it
                changes nothing except the strings.
``--roles``     RU vs EN role-parity report (see above). No PPTX written.
``--audit``     re-run the mechanical checks this docstring asserts (sink
                inventory, live-Cyrillic classification) so they cannot rot.
"""
import json
import re
import sys
import tempfile
from pathlib import Path

from pptx import Presentation

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:                 # importable from any cwd
    sys.path.insert(0, str(HERE))

import build_sem05 as B                       # noqa: E402  (needs sys.path first)
import deck_kit as K                          # noqa: E402
import metrics as M                           # noqa: E402
import slide_parts as SP                      # noqa: E402

SEM_DIR = HERE.parent
SLIDES_RU = SEM_DIR / "slides"
SLIDES_EN = SEM_DIR / "slides-en"
DECK_RU = SEM_DIR / "deck.yaml"
DECK_EN = SEM_DIR / "deck.en.yaml"
STRINGS = HERE / "sem-05.strings.en.json"
FIGS_RU = HERE / "figures"
FIGS_EN = HERE / "figures-en"
OUT_EN = HERE / "sem-05-en.pptx"
RU_PPTX = HERE / "sem-05.pptx"

CYRILLIC = re.compile("[Ѐ-ӿ]")
GUILLEMETS = re.compile("[«»]")

# ============================================================
# Chrome: the only visible strings NOT read from the markdown
# ============================================================
#
# Everything a student reads comes from `slides-en/*.md` except these. They are
# hardcoded in the RU builder either as module data (`SECTIONS_BY_PREFIX`,
# `TAGS`, `TRACK_LABELS`) or inline at a call site (`"СЕМИНАР 5"` in
# `g_cover`), so `slides-en/` cannot carry them.
#
# Kept as a JSON table (`sem-05.strings.en.json`) for the same reason sem-04
# kept one: a translator must be able to see and change every visible string
# without touching Python. The table here is small *because* the body lives in
# markdown — that is a property of this builder, not a shortcut.
CHROME_DEFAULT = {
    # Section names — drawn as roadmap pills on the macro dividers.
    "Открытие": "Opening",
    "Хук": "Hook",
    "Скилл": "Skill",
    "Доступ наружу": "Outbound access",
    "Сборка": "Wrap-up",
    # Cover eyebrow line (build_sem05.g_cover, inline).
    "СЕМИНАР 5": "SEMINAR 5",
    # base_and_edge track labels (build_sem05.TRACK_LABELS + deck_kit defaults).
    "база": "Base",
    "кромка": "Edge",
    # The one divider tag still hardcoded for the n-deck; the rest live in each
    # slide's own `visual.tag` frontmatter and so arrive via slides-en/.
    "3 части описания · 2 длины, которые путают":
        "3 parts of a description · 2 lengths that get confused",
}

CHROME = {}
MISSING = []          # (slide_id, where, string) still containing Cyrillic
GUILL = []            # (slide_id, where, string) emitted with RU-style quotes
RU_FIGURES = []       # slide ids that fell back to a Russian figure
CURRENT = "n00"       # slide currently being built
IDENTITY = False      # --selftest: chrome table is a no-op


def chrome(s):
    """Translate a chrome string. A miss returns it unchanged, which makes the
    lookup idempotent — nested helpers hand already-translated strings down."""
    if IDENTITY or not isinstance(s, str):
        return s
    return CHROME.get(s, CHROME.get(s.strip(), s))


# ============================================================
# Sink patches — the completeness guard, and chrome as a safety net
# ============================================================

_text_box = K.text_box
_write_notes = K.write_notes


def text_box(sl, x, y, w, h, lines, **kw):
    """`deck_kit.text_box`, with every run recorded and chrome translated.

    Chrome is translated HERE as well as in the module data above, because
    `"СЕМИНАР 5"` is written inline at its call site and no data rebinding can
    reach it. Doing it at the sink is safe for chrome specifically: those
    strings are short and every one of them is drawn into a box whose size is
    fixed at the call site, never measured from the string. Body text is NOT
    translated here — it already arrives in English, so the real layout code
    upstream measures English (see the module docstring).
    """
    one = isinstance(lines, str)
    seq = [lines] if one else list(lines)
    out = []
    for item in seq:
        if isinstance(item, str):
            t = chrome(item)
            _record(t, "body")
            out.append(t)
        else:
            out.append(item)
    return _text_box(sl, x, y, w, h, out[0] if one else out, **kw)


def write_notes(sl, text):
    _record(text, "notes")
    return _write_notes(sl, chrome(text))


def _record(s, where):
    """Completeness guard: anything still Cyrillic after lookup is a defect.

    Two kinds, reported separately because they have different fixes: a `body`
    miss means a `slides-en/nNN-*.md` is still Russian (or a chrome string is
    missing from `sem-05.strings.en.json`); a `notes` miss means that file's
    `## Speaker notes` is still Russian.
    """
    if IDENTITY or not isinstance(s, str) or not s.strip():
        return
    if CYRILLIC.search(s):
        MISSING.append((CURRENT, where, s.strip()[:160]))
    elif GUILLEMETS.search(s):
        GUILL.append((CURRENT, where, s.strip()[:160]))


# ============================================================
# quote_role — bilingual, because it decides SHAPES from text
# ============================================================
#
# The EN alternatives are the glossary's own wordings (Part C/D), not free
# invention: «выберите» → "choose"/"pick", «оговорка» → "caveat", «честный
# пробел» → "an honest gap", «не измеряли» → "not measured". `"` joins `«` as
# a speech opener because decision D5 forbids guillemets in EN artifacts.

ASK_BI = re.compile(
    r"выберите|что бы вы|как бы вы|назовите|подумайте"
    r"|\bchoose\b|\bpick\b|what would you|how would you|\bname \b|\bthink\b",
    re.I)
CAVEAT_OPEN_BI = re.compile(
    r"^\W*(оговорка|честный пробел|честно про|честно о\b"
    r"|caveat|an honest gap|honest gap|honestly about|honestly on)",
    re.I)
CAVEAT_BI = re.compile(
    r"не проверен|не провер[её]н|не измер|нет данных|не подтвер|не удалось"
    r"|честного пробела|честный пробел|нечестн"
    r"|not checked|not verified|not measured|no data|not confirmed"
    r"|could not|an honest gap|honest gap|dishonest",
    re.I)
SPEECH_OPEN = ('«', '"')


def quote_role(lines, pattern):
    """`build_sem05.quote_role`, re-expressed over bilingual patterns.

    Deliberately a re-expression and not a wrapper: the original's four
    decisions are interleaved (an `ASK` hit outranks a `CAVEAT` hit, and the
    `«` test is consulted twice), so delegating would need the original to be
    called with text it cannot read. The structure below is line-for-line the
    original's; only the four matchers differ. `--roles` is what keeps the two
    honest with each other.
    """
    body = " ".join(K.plain(l) for l in lines).strip()
    if body.rstrip("»\"' ").endswith("?") or ASK_BI.search(body):
        return "question"
    if CAVEAT_OPEN_BI.match(K.plain(body).lstrip("*> ")) or CAVEAT_BI.search(body):
        return "caveat"
    base = B.PATTERN_ROLE.get(pattern)
    if base == "question":
        return "speech" if body.lstrip().startswith(SPEECH_OPEN) else "fact"
    if body.lstrip().startswith(SPEECH_OPEN):
        return "speech"
    return base or "formula"


# ============================================================
# The one geometry patch: bold table headers
# ============================================================
#
# Found by the pilot render, not by reasoning. On n03 the EN header
# "REINFORCEMENT" wrapped mid-word as "REINFORCEMEN / T", and nothing warned:
# the cell wraps rather than overflows, so `_fits` has nothing to report.
#
# Measured cause, in `deck_kit._col_shares` (l.377-406). A column's FLOOR is
# `longest word + 0.2in`, and the longest word is measured with
# `M.text_w(wd, size, mono=...)` — i.e. NOT bold. The header is then drawn
# bold, into `sh[j] - gap` with `gap = 0.16`. DejaVu bold is 11.9% wider than
# regular (measured), so for "REINFORCEMENT" at 9.5pt: floor = 1.130 + 0.2 =
# 1.330in, available after the gap = 1.170in, actual bold width = 1.264in.
# It does not fit, so it wraps.
#
# Russian never exposed this: the same header is «УСИЛЕНИЕ», 0.820in bold —
# far inside any floor. It is a latent defect in the RU builder that only a
# longer language reaches, which is why it is listed as an open item for the
# owner in EN-TRACK-BRIEF.md rather than quietly fixed in `deck_kit.py`.
#
# Applied to the EN build only, and deliberately so: raising the floor would
# re-proportion some RU tables, and the RU render is approved and must not
# move. `--selftest` therefore does not install this patch.

HEADER_GAP = 0.16          # deck_kit.table_card's own `gap` default
HEADER_PAD = 0.04


def _col_shares_bold(headers, rows, ncol, inner_w, size, _orig=K._col_shares):
    """`deck_kit._col_shares`, with the header floor measured in BOLD.

    Delegates the real apportioning to the original and only repairs the
    result: any column whose header word cannot fit bold inside
    `share - gap` takes the shortfall from the columns that have slack,
    proportionally. The total is preserved exactly, so the table still fills
    its box; if there is not enough slack to satisfy every header, the columns
    get as close as the width allows rather than silently giving up.
    """
    sh = list(_orig(headers, rows, ncol, inner_w, size))
    if not headers:
        return sh
    hsz = min(size, 11.5)
    need = []
    for j in range(ncol):
        # `.upper()` and `bold=True` are BOTH what `table_card` actually draws
        # (deck_kit.py:553 — `text_box(..., ht.upper(), bold=True)`), and the
        # original floor uses neither. Caps add ~15% on top of bold's ~12%, so
        # "Reinforcement" measures 1.095in where "REINFORCEMENT" draws 1.264in.
        # Measuring the string as written rather than as drawn is the whole bug.
        h = K.plain(headers[j]).upper() if j < len(headers) else ""
        widest = max((M.text_w(wd, hsz, bold=True) for wd in h.split()),
                     default=0.0)
        need.append(widest + HEADER_GAP + HEADER_PAD)
    deficit = [max(0.0, need[j] - sh[j]) for j in range(ncol)]
    total = sum(deficit)
    if total <= 1e-9:
        return sh
    slack = [max(0.0, sh[j] - need[j]) for j in range(ncol)]
    pool = sum(slack)
    if pool <= 1e-9:
        return sh
    take = min(total, pool)
    scale = take / total
    return [sh[j] + deficit[j] * scale - slack[j] / pool * take
            for j in range(ncol)]


# ============================================================
# Figures: prefer figures-en/, fall back loudly
# ============================================================

_figure_for = B.figure_for


def figure_for(sid):
    p = _figure_for(sid)
    if not p:
        return p
    p = Path(p)
    en = FIGS_EN / p.name
    if en.exists():
        return en
    if not IDENTITY:
        RU_FIGURES.append(sid)
        M._WARNINGS.append(
            f"РУССКАЯ СХЕМА [{sid}]: «{p.name}» есть только по-русски — "
            f"положите EN-вариант в figures-en/ или примите русскую "
            f"иллюстрацию на английском слайде (решение владельца)")
    return p


# ============================================================
# Wiring
# ============================================================

def _patch(*, identity=False, en_deck=True):
    global IDENTITY
    IDENTITY = identity

    K.text_box = text_box
    K.write_notes = write_notes
    # build_sem05 did `import deck_kit as K`, so it resolves K.text_box at call
    # time off the same module object — rebinding on the module is enough and
    # no call site holds an early reference. The two exceptions are rebound by
    # name below, because they are *defaults captured at def time*.
    B.K = K

    if not identity:
        B.quote_role = quote_role
        B.figure_for = figure_for
        B.TRACK_LABELS = tuple(chrome(x) for x in B.TRACK_LABELS)
        B.TAGS = {k: chrome(v) for k, v in B.TAGS.items()}
        B.SECTIONS_BY_PREFIX = {
            p: ([(a, b, chrome(name), stage) for a, b, name, stage in rows],
                [chrome(s) for s in stages])
            for p, (rows, stages) in B.SECTIONS_BY_PREFIX.items()
        }
        B.SECTIONS, B.STAGES = B.SECTIONS_BY_PREFIX["s"]
        # `sections_for_n()` (l.239-242) rebuilds the n-deck's own section rows
        # inline from literals, so the dict rebinding above cannot reach it.
        # Wrapped rather than reimplemented.
        _sec_n = B._sections_n if hasattr(B, "_sections_n") else None
        if _sec_n is None:
            for nm in dir(B):
                fn = getattr(B, nm)
                if callable(fn) and nm.startswith("_sections"):
                    _sec_n = fn
                    break
        # deck_kit's base_edge_tracks carries «база»/«кромка» as DEFAULT kwargs,
        # bound at def time; rebinding B.TRACK_LABELS does not touch them.
        _bet = K.base_edge_tracks

        def base_edge_tracks(sl, x, y, w, left_lines, right_lines, *,
                             left_label=None, right_label=None, **kw):
            return _bet(sl, x, y, w, left_lines, right_lines,
                        left_label=chrome(left_label or "база"),
                        right_label=chrome(right_label or "кромка"), **kw)

        K.base_edge_tracks = base_edge_tracks
        K._col_shares = _col_shares_bold

    if en_deck:
        # `_deck_slides()` reads deck.yaml / deck-s50.yaml by prefix for
        # divider indices and `visual.figure`. Point it at the EN deck so the
        # EN build never consults the RU manifest.
        import yaml
        _en = yaml.safe_load(DECK_EN.read_text(encoding="utf-8"))["slides"]
        B._deck_slides = lambda prefix: [s for s in _en
                                         if str(s["id"]).startswith(prefix)]


def _save_guard(prs, path):
    """`sem-05.pptx` is never written by this file. sem-04 learned this the hard
    way (notes/mcp-limitations.md [#201-5]): a driver that can overwrite the RU
    render will eventually do it."""
    path = Path(path)
    if path.resolve() == RU_PPTX.resolve():
        raise SystemExit("ОТКАЗ: драйвер не пишет sem-05.pptx (русский рендер)")
    prs.save(str(path))


# ============================================================
# Build
# ============================================================

def build(deck_path, slides_root, out_path, *, identity=False, partial=False):
    """Mirror of `build_sem05.main`'s render loop, minus the two things an EN
    build must not do: `refresh_manifest()` (writes back to the RU `deck.yaml`)
    and `audit_figure_text()` (parses the RU figure generators, whose Russian
    is expected). Everything else — genre dispatch, the per-slide audits, the
    notes write — is the RU builder's own code, called unchanged.

    `partial=True` renders only the slides whose EN file exists, and still adds
    a blank slide for the rest. The blanks are deliberate: slide numbers and
    case badges are derived from a slide's POSITION, so dropping the
    untranslated ones would renumber the frame and the pilot would not show
    what the finished deck shows.
    """
    import yaml
    global CURRENT

    slides = yaml.safe_load(Path(deck_path).read_text(encoding="utf-8"))["slides"]
    prs = Presentation()
    prs.slide_width, prs.slide_height = B.Inches(K.W_IN), B.Inches(K.H_IN)
    blank = prs.slide_layouts[6]
    M.reset()

    built, skipped = 0, []
    for s in slides:
        sid = s["id"]
        CURRENT = sid
        pattern = (s.get("visual") or {}).get("pattern", "")
        src = slides_root / Path(s["file"]).name
        sl = prs.slides.add_slide(blank)
        if partial and not src.exists():
            skipped.append(sid)
            continue
        title, assertion, visual, notes = SP.sections(src.read_text(encoding="utf-8"))
        fn = B.GENRE_FN.get(pattern, B.g_content)
        kw = {"meta": s.get("visual")} if fn is B.g_divider else {}
        fn(sl, sid, title or sid, SP.blocks(visual), pattern, assertion, **kw)
        B.audit_question_answer(sid, pattern, SP.blocks(visual))
        if notes:
            K.write_notes(sl, notes)
        built += 1

    if not partial:
        B.audit_numbering(slides)
        B.audit_crossrefs(slides)
        B.audit_figs(slides)
    return prs, slides, built, skipped


def main_build(partial=False):
    _patch(identity=False, en_deck=True)
    if STRINGS.exists():
        CHROME.update(json.loads(STRINGS.read_text(encoding="utf-8")))
    else:
        CHROME.update(CHROME_DEFAULT)
        STRINGS.write_text(
            json.dumps(CHROME_DEFAULT, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
        print(f"создан {STRINGS.name} (таблица служебных строк)")

    missing_files = [s for s in _deck_ids() if not (SLIDES_EN / s).exists()]
    if missing_files and not partial:
        raise SystemExit(
            f"ОТКАЗ: нет {len(missing_files)} английских слайдов. "
            f"Для промежуточной сборки — `--partial`.\n  " +
            "\n  ".join(missing_files[:20]) +
            (f"\n  … и ещё {len(missing_files) - 20}"
             if len(missing_files) > 20 else ""))

    prs, slides, built, skipped = build(DECK_EN, SLIDES_EN, OUT_EN,
                                        partial=partial)

    warns = M.report()
    for w in warns:
        print("•", w)

    if MISSING:
        print(f"\nОТКАЗ: {len(MISSING)} строк остались русскими "
              f"(файл не сохранён):")
        for sid, where, s in MISSING[:40]:
            print(f"  [{sid}/{where}] {s}")
        if len(MISSING) > 40:
            print(f"  … и ещё {len(MISSING) - 40}")
        raise SystemExit(1)

    _save_guard(prs, OUT_EN)

    if GUILL:
        print(f"\nвнимание: кавычки «» в {len(GUILL)} строках "
              f"(решение D5 — в EN только \"…\"):")
        for sid, where, s in GUILL[:10]:
            print(f"  [{sid}/{where}] {s}")
    if RU_FIGURES:
        print(f"\nвнимание: русские схемы на {len(RU_FIGURES)} слайдах: "
              f"{', '.join(RU_FIGURES)}")

    if skipped:
        print(f"\nпропущено (нет английского слайда): {len(skipped)} — "
              f"{', '.join(skipped[:12])}{'…' if len(skipped) > 12 else ''}")
        print("  место под них в деке оставлено пустым, чтобы номера слайдов "
              "и значки кейсов не сдвинулись")
    print(f"\nслайдов собрано: {built}   предупреждений: {len(warns)}   "
          f"файл: {OUT_EN.name} ({OUT_EN.stat().st_size // 1024} КБ)")


def _deck_ids():
    import yaml
    slides = yaml.safe_load(DECK_EN.read_text(encoding="utf-8"))["slides"]
    return [Path(s["file"]).name for s in slides]


# ============================================================
# --selftest : prove the harness is transparent
# ============================================================

def selftest():
    _patch(identity=True, en_deck=False)
    tmp = Path(tempfile.mkdtemp()) / "identity.pptx"
    prs, slides, built, _ = build(DECK_RU, SLIDES_RU, tmp, identity=True)
    _save_guard(prs, tmp)

    ref = Presentation(str(RU_PPTX))
    got = Presentation(str(tmp))
    if len(ref.slides) != len(got.slides):
        print(f"ПРОВАЛ: слайдов {len(got.slides)} против {len(ref.slides)}")
        return 1

    diffs = []
    for i, (a, b) in enumerate(zip(ref.slides, got.slides), 1):
        ta, tb = _shapes(a), _shapes(b)
        if ta != tb:
            diffs.append(i)
            if len(diffs) <= 3:
                for x, y in zip(ta, tb):
                    if x != y:
                        print(f"  слайд {i}: эталон {x!r}")
                        print(f"            драйвер {y!r}")
                        break
        na = a.notes_slide.notes_text_frame.text if a.has_notes_slide else ""
        nb = b.notes_slide.notes_text_frame.text if b.has_notes_slide else ""
        if na != nb:
            diffs.append(i)
    if diffs:
        print(f"ПРОВАЛ: расходятся слайды {sorted(set(diffs))}")
        return 1
    print(f"ПРОЙДЕНО: {built} слайдов совпадают с sem-05.pptx "
          f"(типы форм, тексты прогонов, заметки)")
    return 0


def _shapes(sl):
    out = []
    for sh in sl.shapes:
        t = sh.text_frame.text if sh.has_text_frame else ""
        out.append((sh.shape_type, round(sh.left or 0), round(sh.top or 0),
                    round(sh.width or 0), round(sh.height or 0), t))
    return out


# ============================================================
# --roles : RU vs EN role parity
# ============================================================

def roles():
    import yaml
    ru = yaml.safe_load(DECK_RU.read_text(encoding="utf-8"))["slides"]
    en_ids = {Path(s["file"]).name for s in
              yaml.safe_load(DECK_EN.read_text(encoding="utf-8"))["slides"]} \
        if DECK_EN.exists() else set()

    bad, checked, skipped = [], 0, []
    for s in ru:
        sid, name = s["id"], Path(s["file"]).name
        pattern = (s.get("visual") or {}).get("pattern", "")
        en_file = SLIDES_EN / name
        if name not in en_ids or not en_file.exists():
            skipped.append(sid)
            continue
        _, _, v_ru, _ = SP.sections((SLIDES_RU / name).read_text(encoding="utf-8"))
        _, _, v_en, _ = SP.sections(en_file.read_text(encoding="utf-8"))
        q_ru = [b for k, b in SP.blocks(v_ru) if k == "quote"]
        q_en = [b for k, b in SP.blocks(v_en) if k == "quote"]
        if len(q_ru) != len(q_en):
            bad.append((sid, "-", f"блоков-цитат {len(q_ru)} против {len(q_en)}"))
            continue
        for j, (a, b) in enumerate(zip(q_ru, q_en), 1):
            checked += 1
            ra = B.quote_role(a, pattern)        # original, Russian
            rb = quote_role(b, pattern)          # bilingual, English
            if ra != rb:
                bad.append((sid, f"цитата {j}", f"{ra} → {rb}: "
                                                f"{' '.join(b)[:90]}"))
    if skipped:
        print(f"нет английского слайда: {len(skipped)} "
              f"({', '.join(skipped[:12])}{'…' if len(skipped) > 12 else ''})")
    print(f"сверено блоков: {checked}")
    if bad:
        print(f"\nПРОВАЛ: роль разошлась на {len(bad)} блоках — "
              f"английский слайд получит другую форму, чем русский:")
        for sid, where, msg in bad:
            print(f"  [{sid} {where}] {msg}")
        return 1
    print("ПРОЙДЕНО: роль каждого блока одинакова по-русски и по-английски")
    return 0


# ============================================================
# --audit : keep this file's own claims from rotting
# ============================================================

def audit():
    import ast
    rc = 0
    mods = ["build_sem05.py", "deck_kit.py", "metrics.py", "slide_parts.py"]
    sinks = {}
    cyr_live = {}
    for fn in mods:
        src = (HERE / fn).read_text(encoding="utf-8")
        tree = ast.parse(src)
        docs = set()
        for n in ast.walk(tree):
            if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef,
                              ast.AsyncFunctionDef)):
                d = ast.get_docstring(n, clean=False)
                if d:
                    docs.add(d)
        n_sink = 0
        for n in ast.walk(tree):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.func.attr == "add_run":
                n_sink += 1
            if isinstance(n, ast.Assign):
                for t in n.targets:
                    if isinstance(t, ast.Attribute) and t.attr == "text":
                        n_sink += 1
        sinks[fn] = n_sink
        cyr_live[fn] = sum(
            1 for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and n.value not in docs and re.search("[А-Яа-яЁё]", n.value))

    print("сайты записи текста (add_run / .text =):")
    for fn in mods:
        print(f"  {fn:18} {sinks[fn]}")
    if sinks["build_sem05.py"] or sinks["metrics.py"] or sinks["slide_parts.py"]:
        print("  ПРОВАЛ: появился приёмник вне deck_kit.py — "
              "драйвер его не перехватывает")
        rc = 1
    print("живые кириллические литералы (вне докстрингов):")
    for fn in mods:
        print(f"  {fn:18} {cyr_live[fn]}")

    for name in ("ASK", "CAVEAT_OPEN", "CAVEAT"):
        if not hasattr(B, name):
            print(f"  ПРОВАЛ: build_sem05.{name} исчез — "
                  f"двуязычная замена в этом файле больше ни на что не ссылается")
            rc = 1
    gens = sorted(HERE.glob("make_figures*.py"))
    print(f"генераторов схем: {len(gens)}; PNG в figures/: "
          f"{len(list(FIGS_RU.glob('*.png')))}; в figures-en/: "
          f"{len(list(FIGS_EN.glob('*.png'))) if FIGS_EN.exists() else 0}")
    return rc


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--selftest" in argv:
        sys.exit(selftest())
    elif "--roles" in argv:
        _patch(identity=False, en_deck=False)
        sys.exit(roles())
    elif "--audit" in argv:
        sys.exit(audit())
    else:
        main_build(partial="--partial" in argv)
