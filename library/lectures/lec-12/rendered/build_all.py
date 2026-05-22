#!/usr/bin/env python3
"""Master builder for lec-12. Combines build_lec12 + build_lec12_part2."""
import re
import sys
from pathlib import Path

# Add this directory to sys.path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build_lec12 import (
    setup_pres, blank, set_bg, add_notes, OUT, ROOT,
    s01_hero, s02_cover, s03_lecture_map, s04_keystone,
    s05_div, s06_kritzinger, s07_four_layers, s08_market, s09_port_failure, s10_data_audit,
    s11_div, s12_vision, s13_pdm, s14_a0_limits,
)
from build_lec12_part2 import (
    s15_div, s16_mes, s17_plc_copilot, s18_engineer_in_loop,
    s19_div, s20_yokogawa, s21_twin_sandbox, s22_sim_real_gap, s23_rl_limits_mpc,
    s24_div, s25_a3_cases,
    s26_div, s27_port_intro, s28_ten_criteria, s29_pharma_fda, s30_gartner, s31_vendor_questions,
    s32_div, s33_seven_layers, s34_opcua, s35_lighthouse,
    s36_div, s37_russian, s38_career,
    s39_closing,
)


def apply_md_notes(pres):
    """Read slides/*.md and replace generated notes with full chapter-derived notes."""
    slides_dir = ROOT.parent / "slides"
    if not slides_dir.exists():
        return
    md_files = sorted(slides_dir.glob("s*.md"))
    for i, slide in enumerate(pres.slides):
        if i >= len(md_files):
            break
        md = md_files[i].read_text(encoding="utf-8")
        m = re.search(r"## Speaker notes\s*\n(.*?)(?:\n##|\Z)", md, re.S)
        if m:
            notes = m.group(1).strip()
            paragraphs = [p.strip().replace("\n", " ") for p in notes.split("\n\n") if p.strip()]
            notes_text = "\n\n".join(paragraphs)
            try:
                slide.notes_slide.notes_text_frame.text = notes_text
            except Exception as e:
                print(f"Notes apply fail slide {i+1}: {e}")


if __name__ == "__main__":
    pres = setup_pres()
    # Section 0 — Cover + keystone
    s01_hero(pres)
    s02_cover(pres)
    s03_lecture_map(pres)
    s04_keystone(pres)
    # Section 1 — DT 2026
    s05_div(pres)
    s06_kritzinger(pres)
    s07_four_layers(pres)
    s08_market(pres)
    s09_port_failure(pres)
    s10_data_audit(pres)
    # Section 2 — A0
    s11_div(pres)
    s12_vision(pres)
    s13_pdm(pres)
    s14_a0_limits(pres)
    # Section 3 — A1
    s15_div(pres)
    s16_mes(pres)
    s17_plc_copilot(pres)
    s18_engineer_in_loop(pres)
    # Section 4 — A2
    s19_div(pres)
    s20_yokogawa(pres)
    s21_twin_sandbox(pres)
    s22_sim_real_gap(pres)
    s23_rl_limits_mpc(pres)
    # Section 4.5 — A3
    s24_div(pres)
    s25_a3_cases(pres)
    # Section 5 — НЕ AI
    s26_div(pres)
    s27_port_intro(pres)
    s28_ten_criteria(pres)
    s29_pharma_fda(pres)
    s30_gartner(pres)
    s31_vendor_questions(pres)
    # Section 6 — OT/IT
    s32_div(pres)
    s33_seven_layers(pres)
    s34_opcua(pres)
    s35_lighthouse(pres)
    # Section 7 — RU + Career
    s36_div(pres)
    s37_russian(pres)
    s38_career(pres)
    # Closing
    s39_closing(pres)

    print(f"Slides built: {len(pres.slides)}")
    apply_md_notes(pres)
    pres.save(str(OUT))
    print(f"Saved: {OUT}")
