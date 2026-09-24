#!/usr/bin/env python3
"""EN render driver for Семинар 4 — thin driver over the untouched RU builder.

Design (EN-TRACK-BRIEF.md, decision D1: "parameterize, don't fork")
-------------------------------------------------------------------
This file is **not** a fork of ``build_sem04.py``. It imports it as a module,
repoints two module-level paths, and monkey-patches its text sinks so that every
visible string is translated *on entry*, before the real layout code sees it::

    slides-en/*.md ──┐
                     ├─► build_sem04.py (UNCHANGED, 2552 lines) ─► sem-04-en.pptx
    sem-04.strings.en.json ─┘

Why a driver and not a fork:

* The RU builder is live, not stale — it produced the current v6 render — so the
  sem-01/sem-02 approach of substituting runs over a finished PPTX
  (``tools/seminar-render/pptx_i18n.py``) is unnecessary here, and would have
  silently kept **RU-sized boxes** around longer EN text.
* lec-03 forked its builder because its EN deck genuinely differs visually.
  Seminar 4 does not: same icons, same charts, same layout. A 2552-line copy
  would drift the first time the RU deck is revised.
* The RU render stays byte-identical *by construction*: the RU script is never
  edited, and ``sem-04.pptx`` is never written by this file (there is an explicit
  guard against that — see ``_save``, and notes/mcp-limitations.md [#201-5]
  for why that guard exists).

Two properties of the RU builder make this possible, both verified by reading it
and re-verified mechanically by ``--selftest``:

1. Every visible run funnels through exactly two functions — ``text_box()`` and
   ``multipara_box()`` (via each paragraph dict's ``"text"``) — plus
   ``speaker_notes()`` for the notes. ``grep -n 'add_run\\|\\.text = '`` over the
   RU builder returns those three sites and nothing else.
2. The ~57 ``build_sNN`` functions call those sinks as *module globals*, resolved
   at call time, so rebinding them on the module object is enough — no call site
   holds an early reference.

Length-driven geometry is patched too, not just the sinks
--------------------------------------------------------
A sink-only patch would compute every box from the *Russian* string and then put
English into it. So the five places that measure text before emitting it are
patched as well, each translating its own argument and then delegating to the
original:

* ``auto_header``   — picks title font size (22 … 12pt) and header height from
  ``len(title)``; also returns the y where content may start. **Real geometry.**
* ``question_slide`` — picks the gold question-box height from ``len(question)``
  (1.3 / 1.1 / 0.85in) and offsets everything below it. **Real geometry.**
* ``terminal_card`` — estimates monospace line count from ``len(text)`` per line
  to print ``OVERFLOW WARNING`` (16 call sites). Diagnostic.
* ``_fits``        — the generic overflow estimator (8 call sites: ``table_card``,
  ``numbered_card``, ``failure_card``, ``criterion_plate``, ``basket_row``,
  ``criteria_slide``, ``scenario_pain_slide``). Diagnostic.
* ``option_row``   — the one caller that measures a *flattened* label while the
  sink receives that label's individual lines, so it is translated line by line.
  Diagnostic. **Currently dead code in the RU builder** (0 call sites —
  ``question_slide`` builds its option cards inline instead); patched
  defensively, as is the ``code_card`` alias of ``terminal_card`` (also 0 call
  sites, and bound at def-time, so rebinding ``terminal_card`` alone would miss
  it).

Verified, not assumed: ``--selftest`` proves the sinks are reached and are
transparent, and the geometry patches were checked by translating one title
154 -> 35 chars (``auto_header`` re-picked 14.5pt -> 22.0pt and the content below
it moved up) and one question 138 -> 227 chars (``question_slide`` re-picked
0.85in -> 1.30in). The RU build emits 0 ``OVERFLOW WARNING`` lines; deliberately
overlong EN strings made ``_fits``/``terminal_card`` emit 32 of them.

So the EN build re-runs the real layout logic on English text: ``auto_header``
re-picks its font size for a longer EN title, and the overflow estimators print
genuine warnings for EN.

Translation is idempotent
-------------------------
Nested helpers hand their (already translated) strings down to the sinks, so
every string is looked up twice. A lookup with no entry returns the string
unchanged, which makes the second lookup a harmless miss.

Completeness guard
------------------
The property ``pptx_i18n.apply`` provided by refusing partial tables: every
string that still contains Cyrillic after lookup is collected with the slide it
appeared on, and the build **fails without saving** rather than shipping a
half-Russian deck. Two kinds are reported separately, because they have
different fixes: a ``body`` miss means ``sem-04.strings.en.json`` needs an entry,
a ``notes`` miss means a ``slides-en/sNN-*.md`` is still Russian.

A second, non-fatal sweep reports any emitted string that still carries RU
guillemets (decision D5 -- EN uses ``"..."``, with ``'...'`` for a nested
quotation). It is a warning, not a failure: the guard's own contract is Cyrillic.

Modes
-----
``extract``     run the RU build with the sinks recording, and write/merge
                ``sem-04.strings.en.json``. Reads RU ``slides/`` (so it works
                before ``slides-en/`` is complete). Writes no PPTX.
``--selftest``  run this same patched harness with an **identity** table over
                RU ``slides/``, into a temp file, and compare it against the
                committed ``sem-04.pptx`` slide by slide. Proves the harness is
                transparent — that it changes nothing except the strings.
``(no args)``   render ``sem-04-en.pptx`` from ``slides-en/`` + the string table.
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

import build_sem04 as B                       # noqa: E402  (needs sys.path first)

SEM_DIR = HERE.parent
SLIDES_RU = SEM_DIR / "slides"
SLIDES_EN = SEM_DIR / "slides-en"
STRINGS = HERE / "sem-04.strings.en.json"
OUT_EN = HERE / "sem-04-en.pptx"
RU_PPTX = HERE / "sem-04.pptx"

CYRILLIC = re.compile("[Ѐ-ӿ]")
DECIMAL_COMMA = re.compile(r"\d,\d")          # D3: "p<0,001" → "p<0.001"

# ============================================================
# Translation state
# ============================================================

MODE = "build"            # "build" | "extract"
TABLE = {}                # ru -> en
RECORDS = {}              # ru -> table entry (insertion-ordered = build order)
NOTES_STRINGS = []        # notes blobs seen, in build order (NOT part of TABLE)
NOTES_EMPTY = []          # slides whose speaker notes came back empty
MISSING = []              # (slide_id, where, string) still containing Cyrillic
GUILLEMETS = []           # (slide_id, where, string) emitted with RU-style "" quotes
CURRENT = "s00"           # slide currently being built
COUNTS = {"body": 0, "notes": 0, "translated": 0}
_PER_SLIDE = {}           # slide_id -> running body index, for entry ids


def translate(s, where="body", *, record=True):
    """Translate one string through the table.

    `record=False` is used by the length-driven geometry wrappers: they sit
    *upstream* of the sinks, so recording there would double-count every string
    in `extract` and double-report it in the completeness guard.
    """
    if not isinstance(s, str) or not s.strip():
        return s
    if record:
        COUNTS[where] += 1
    if MODE == "extract":
        if record:
            if where == "notes":
                NOTES_STRINGS.append(s)
            else:
                _record(s)
        return s
    en = TABLE.get(s)
    if en:
        if record:
            COUNTS["translated"] += 1
        return en
    if record and CYRILLIC.search(s):
        MISSING.append((CURRENT, where, s))
    if record and ("\u00ab" in s or "\u00bb" in s):
        GUILLEMETS.append((CURRENT, where, s))   # D5, reported as a warning
    return s                                  # pass-through: idempotent


def _record(s):
    if s in RECORDS:                          # dedupe by source string
        return
    n = _PER_SLIDE.get(CURRENT, 0) + 1
    _PER_SLIDE[CURRENT] = n
    # A string a translator never needs to look at: no Cyrillic and no RU
    # decimal comma (D3 localizes "0,001" → "0.001", so those stay open).
    passthrough = not CYRILLIC.search(s) and not DECIMAL_COMMA.search(s)
    RECORDS[s] = {
        "id": f"{CURRENT}.body.{n:03d}",
        "slide": CURRENT,
        "where": "body",
        "ru": s,
        "en": s if passthrough else "",
        "passthrough": passthrough,
    }


# ============================================================
# Monkey-patches — text sinks (translate + record)
# ============================================================

_O = {}                   # original callables, kept for the transparency check


def _arg(args, kwargs, name, pos, fn):
    """Apply `fn` to argument `name`, whether it was passed by keyword or at
    positional index `pos`. Returns the new (args, kwargs)."""
    if name in kwargs:
        kwargs = dict(kwargs)
        kwargs[name] = fn(kwargs[name])
    elif len(args) > pos:
        args = args[:pos] + (fn(args[pos]),) + args[pos + 1:]
    return args, kwargs


def _patch_sinks():
    _O["text_box"] = B.text_box
    _O["multipara_box"] = B.multipara_box
    _O["speaker_notes"] = B.speaker_notes

    def text_box(*a, **kw):
        a, kw = _arg(a, kw, "text", 5, translate)
        return _O["text_box"](*a, **kw)

    def multipara_box(*a, **kw):
        def tr(paras):
            out = []
            for cfg in paras:
                cfg = dict(cfg)               # never mutate the caller's dict
                cfg["text"] = translate(cfg.get("text", ""))
                out.append(cfg)
            return out
        a, kw = _arg(a, kw, "paragraphs", 5, tr)
        return _O["multipara_box"](*a, **kw)

    def speaker_notes(*a, **kw):
        def tr(text):
            if not (isinstance(text, str) and text.strip()):
                # load_notes() returns "" when slides-en/sNN-*.md is absent
                NOTES_EMPTY.append(CURRENT)
            return translate(text, "notes")
        a, kw = _arg(a, kw, "text", 1, tr)
        return _O["speaker_notes"](*a, **kw)

    B.text_box = text_box
    B.multipara_box = multipara_box
    B.speaker_notes = speaker_notes


# ============================================================
# Monkey-patches — length-driven geometry (translate, do NOT record)
# ============================================================

def _soft(s):
    return translate(s, record=False)


def _patch_geometry():
    _O["auto_header"] = B.auto_header
    _O["question_slide"] = B.question_slide
    _O["terminal_card"] = B.terminal_card
    _O["_fits"] = B._fits
    _O["option_row"] = B.option_row

    def auto_header(slide, section_label, title):
        # size / header height / content-start y all come from len(title)
        return _O["auto_header"](slide, section_label, _soft(title))

    def question_slide(*a, **kw):
        # question-box height comes from len(question)
        a, kw = _arg(a, kw, "question", 99, _soft)   # keyword-only in the RU builder
        return _O["question_slide"](*a, **kw)

    def terminal_card(*a, **kw):
        def tr(lines):
            return [(_soft(t),) + tuple(rest) for t, *rest in lines]
        a, kw = _arg(a, kw, "lines", 5, tr)
        a, kw = _arg(a, kw, "title", 99, lambda t: _soft(t) if t else t)
        return _O["terminal_card"](*a, **kw)

    def _fits(*a, **kw):
        a, kw = _arg(a, kw, "text", 0, _soft)
        return _O["_fits"](*a, **kw)

    def option_row(*a, **kw):
        # measures label.replace("\n", " ") while the sink gets the lines, so
        # translate line by line to keep its _fits() call honest for EN
        def tr(options):
            return ["\n".join(_soft(ln) for ln in lab.split("\n")) for lab in options]
        a, kw = _arg(a, kw, "options", 5, tr)
        return _O["option_row"](*a, **kw)

    B.auto_header = auto_header
    B.question_slide = question_slide
    B.terminal_card = terminal_card
    B._fits = _fits
    B.option_row = option_row
    B.code_card = terminal_card           # def-time alias of terminal_card


def _install():
    """Idempotent on purpose: a second _patch_sinks() would capture the already
    patched wrapper as its own "original" and recurse until the stack blows."""
    if _O:
        return
    _patch_sinks()
    _patch_geometry()


def _assert_patched():
    """The patches must actually be the ones the builder resolves."""
    for name in ("text_box", "multipara_box", "speaker_notes", "auto_header",
                 "question_slide", "terminal_card", "_fits", "option_row"):
        assert getattr(B, name) is not _O[name], f"{name} not patched"
    assert B.code_card is B.terminal_card, "code_card alias not rebound"


# ============================================================
# Build driver
# ============================================================

def _run_build():
    """B.main()'s own three lines, minus the save -- saving is ours, and it must
    happen only after the completeness guard has passed."""
    global CURRENT
    p = B.setup_pres()
    for sid in B.SEQ:
        CURRENT = sid
        getattr(B, f"build_{sid}")(p)
    return p


def _save(p, out_path):
    out_path = Path(out_path).resolve()
    # notes/mcp-limitations.md [#201-5]: never let an EN run touch RU output
    for ru in (RU_PPTX, RU_PPTX.with_suffix(".pdf")):
        if out_path == ru.resolve():
            sys.exit(f"REFUSING to write the RU artifact {ru}")
    p.save(str(out_path))


def _guard():
    """Refuse to ship a half-Russian deck."""
    if not MISSING:
        return
    body = [m for m in MISSING if m[1] == "body"]
    notes = [m for m in MISSING if m[1] == "notes"]
    print("")
    print(f"UNTRANSLATED: {len(MISSING)} string(s) still contain Cyrillic "
          f"({len(body)} body, {len(notes)} notes) — NOT saving.")
    def uniq(items):
        """First slide each distinct string appeared on, in build order."""
        seen = {}
        for sid, _, s in items:
            seen.setdefault(s, sid)
        return seen
    if body:
        u = uniq(body)
        print(f"\n  {len(u)} distinct body string(s) ({len(body)} occurrences) "
              f"have no entry in {STRINGS.name}:")
        for s, sid in u.items():
            print(f"    [{sid}] {s[:160]!r}")
    if notes:
        u = uniq(notes)
        print(f"\n  {len(u)} speaker-notes blob(s) are still Russian — fix the "
              f"matching slides-en/sNN-*.md (notes are not table-driven):")
        for s, sid in u.items():
            print(f"    [{sid}] {s[:120]!r}...")
    sys.exit(1)


# ============================================================
# Mode: extract
# ============================================================

def _merge(fresh):
    """Carry over every `en` already filled in for a matching `ru`."""
    kept = stale = 0
    if STRINGS.exists():
        old = {e["ru"]: e for e in json.loads(STRINGS.read_text(encoding="utf-8"))}
        for entry in fresh:
            prev = old.pop(entry["ru"], None)
            if prev and prev.get("en"):
                if prev["en"] != entry["en"]:
                    kept += 1
                entry["en"] = prev["en"]
        stale = len([e for e in old.values() if e.get("en")])
        if stale:
            print(f"NOTE: {stale} previously translated entr(y/ies) no longer "
                  f"appear in the build and were dropped:")
            for e in list(old.values())[:5]:
                if e.get("en"):
                    print(f"    {e['ru'][:80]!r}")
    return kept, stale


def do_extract():
    global MODE
    MODE = "extract"
    B.SLIDES_DIR = SLIDES_RU              # extract reads the RU notes
    _install()
    _assert_patched()
    _run_build()                          # no PPTX written
    assert COUNTS["body"] > 0 and COUNTS["notes"] > 0, "sinks were never reached"

    fresh = list(RECORDS.values())
    kept, _ = _merge(fresh)
    STRINGS.write_text(json.dumps(fresh, ensure_ascii=False, indent=1) + "\n",
                       encoding="utf-8")

    passthrough = [e for e in fresh if e["passthrough"]]
    cyr = [e for e in fresh if CYRILLIC.search(e["ru"])]
    comma = [e for e in fresh if not e["passthrough"] and not CYRILLIC.search(e["ru"])]
    todo = [e for e in fresh if not e["en"]]
    print("")
    print(f"body sink calls       : {COUNTS['body']}")
    print(f"unique body strings   : {len(fresh)}  -> {STRINGS.name}")
    print(f"  passthrough (en=ru) : {len(passthrough)}")
    print(f"  need translation    : {len(cyr)}  (contain Cyrillic)")
    print(f"  D3 decimal comma    : {len(comma)}  (no Cyrillic, en left empty)")
    print(f"  still empty en      : {len(todo)}")
    print(f"  en carried over     : {kept}")
    print(f"notes sink calls      : {COUNTS['notes']}  "
          f"({len(set(NOTES_STRINGS))} unique) — EXCLUDED from the table "
          f"(notes come from slides-en/*.md)")


# ============================================================
# Mode: selftest
# ============================================================

def _digest(path):
    """Extracted content, not zip bytes (python-pptx rewrites zip metadata)."""
    prs = Presentation(str(path))
    out = []
    for slide in prs.slides:
        shapes, runs = [], []
        for sh in slide.shapes:
            shapes.append(str(sh.shape_type))
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    for run in para.runs:
                        runs.append(run.text)
        notes = (slide.notes_slide.notes_text_frame.text
                 if slide.has_notes_slide else None)
        out.append({"shapes": shapes, "runs": runs, "notes": notes})
    return out


def do_selftest():
    """Run the EN harness with an identity table over the RU slides and compare
    the result against the committed RU render, slide by slide."""
    global MODE, TABLE, MISSING, COUNTS, RECORDS, NOTES_STRINGS, _PER_SLIDE

    if not RU_PPTX.exists():
        sys.exit(f"selftest needs the committed {RU_PPTX}")

    # Pass 1 — collect every string the build emits (body + notes).
    MODE = "extract"
    B.SLIDES_DIR = SLIDES_RU
    _install()
    _assert_patched()
    _run_build()
    identity = {s: s for s in RECORDS}
    identity.update({s: s for s in NOTES_STRINGS})
    seen_body, seen_notes = COUNTS["body"], COUNTS["notes"]
    print(f"selftest: identity table = {len(identity)} strings "
          f"({len(RECORDS)} body + {len(set(NOTES_STRINGS))} notes)")

    # Pass 2 — real translate path, every en == ru.
    MODE = "build"
    TABLE = identity
    MISSING = []
    COUNTS = {"body": 0, "notes": 0, "translated": 0}
    RECORDS, NOTES_STRINGS, _PER_SLIDE = {}, [], {}
    NOTES_EMPTY.clear()
    tmp = Path(tempfile.mkdtemp(prefix="sem04en-selftest-")) / "identity.pptx"
    _save(_run_build(), tmp)
    print(f"selftest: {COUNTS['body']} body + {COUNTS['notes']} notes sink calls, "
          f"{COUNTS['translated']} table hits, {len(MISSING)} untranslated")

    ok = True
    if (COUNTS["body"], COUNTS["notes"]) != (seen_body, seen_notes):
        print("FAIL: sink call counts differ between the two passes")
        ok = False
    if MISSING:
        print(f"FAIL: identity table missed {len(MISSING)} string(s), "
              f"first: {MISSING[0][2][:80]!r}")
        ok = False
    if COUNTS["translated"] != COUNTS["body"] + COUNTS["notes"]:
        print(f"FAIL: only {COUNTS['translated']} of "
              f"{COUNTS['body'] + COUNTS['notes']} strings went through the table")
        ok = False

    got, want = _digest(tmp), _digest(RU_PPTX)
    if len(got) != len(want):
        print(f"FAIL: slide count {len(got)} != {len(want)}")
        ok = False
    for i, (g, w) in enumerate(zip(got, want), 1):
        for key in ("shapes", "runs", "notes"):
            if g[key] != w[key]:
                ok = False
                print(f"FAIL: slide {i} {key} differ "
                      f"({len(g[key] or '')} vs {len(w[key] or '')})")
                if isinstance(g[key], list):
                    for a, b in zip(g[key], w[key]):
                        if a != b:
                            print(f"       EN-harness: {a[:90]!r}")
                            print(f"       committed : {b[:90]!r}")
                            break
    tmp.unlink()
    tmp.parent.rmdir()
    if ok:
        print(f"SELFTEST PASS: {len(got)} slides, identical shape types, run "
              f"texts and speaker notes vs {RU_PPTX.name} — the harness is "
              f"transparent.")
        return 0
    print("SELFTEST FAIL")
    return 1


# ============================================================
# Mode: build
# ============================================================

def do_build():
    global TABLE
    if not STRINGS.exists():
        sys.exit(f"missing {STRINGS} — run: python3 {Path(__file__).name} extract")
    entries = json.loads(STRINGS.read_text(encoding="utf-8"))
    TABLE = {e["ru"]: e["en"] for e in entries if e.get("en")}
    blank_en = [e for e in entries if not e.get("en")]
    if not SLIDES_EN.is_dir():
        sys.exit(f"missing {SLIDES_EN} — EN speaker notes live there")

    B.SLIDES_DIR = SLIDES_EN
    B.OUT = OUT_EN                        # keep the module consistent with us
    _install()
    _assert_patched()
    p = _run_build()                      # build, then warn, then guard, then save
    if GUILLEMETS:
        # D5: EN artifacts use "..." / '...'; no RU guillemets survive. A
        # warning, not a failure -- the completeness guard's contract is
        # Cyrillic only.
        print(f"WARNING (D5): {len(GUILLEMETS)} emitted string(s) still contain "
              f"\u00ab or \u00bb:")
        for sid, where, s in GUILLEMETS[:10]:
            print(f"    [{sid}/{where}] {s[:120]!r}")
    if NOTES_EMPTY:
        print(f"WARNING: {len(NOTES_EMPTY)} of {len(B.SEQ)} slides got EMPTY "
              f"speaker notes — no {SLIDES_EN.name}/sNN-*.md, or no "
              f"'## Speaker notes' section in it: "
              f"{', '.join(NOTES_EMPTY)}")
    if blank_en:
        print(f"WARNING: {len(blank_en)} table entr(y/ies) have an empty `en` "
              f"and were passed through unchanged (none contained Cyrillic).")
    _guard()                              # exits non-zero, saving nothing
    _save(p, OUT_EN)
    print(f"Saved {OUT_EN} — {len(p.slides._sldIdLst)} slides "
          f"({COUNTS['translated']} strings translated, "
          f"{COUNTS['body']} body + {COUNTS['notes']} notes sink calls)")


def main(argv):
    if argv[:1] == ["extract"]:
        do_extract()
        return 0
    if argv[:1] == ["--selftest"]:
        return do_selftest()
    if argv:
        sys.exit(__doc__)
    do_build()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
