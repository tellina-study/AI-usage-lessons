#!/usr/bin/env python3
"""
Phase 11 — focused re-render of s01 + s37 ONLY.

Per consistency-checker P0 findings:
- P0-1: s01 PPTX Galactica date «15 ноября 2022» → canonical «15 ноября launch + 17 ноября retraction (3 days public)»
- P0-2: s37 PPTX fabricated RU institutional narrative → canonical AIRI(independent)/Sber AI Lab(climate+energy)/Yandex Research(YaLM+RuGPT)

Strategy:
  1. Build a fresh 39-slide PPTX (deterministic — identical to current except s01 + s37 updated).
  2. Save to lec-15.pptx — preserves slide order, all metadata.

Alternative (in-place edit) considered but rejected: removing slide via XML rels-manipulation is fragile;
clean rebuild is safer since all 37 other slide builders are deterministic + unchanged.

Run: python3 rerender_s01_s37.py
"""
from pathlib import Path
from build_lec15 import setup_pres, OUT
from build_lec15_slides import (
    s01_hero_alphafold_galactica, s02_cover, s03_lecture_map,
    s04_glossary, s05_central_question, s06_section1_divider,
    s07_we1_grant_idea_tree, s08_sakana_ai_scientist,
    s09_coscientist_vs_co_scientist, s10_sakana_cherry_pick,
    s11_bo_gp_alternative,
)
from build_lec15_slides2 import (
    s12_section2_divider, s13_alphafold_timeline, s14_alphafold_db,
    s15_boltz_open_source, s16_gnome_alab, s17_palgrave_critique,
    s18_aurora_ecmwf, s19_alphaproof_imo, s20_section3_divider,
    s21_exoplanet_cnn, s22_allen_microns, s23_ligo_ml,
    s24_alphafold_idp, s25_we_tess,
)
from build_lec15_slides3 import (
    s26_section4_divider, s27_notebooklm_elicit, s28_we2_bibliography,
    s29_frontiers_rat, s30_neurips_fake_citations, s31_icmje_policies,
    s32_section5_divider, s33_four_criteria, s34_we3_catalyst,
    s35_alternatives_matrix, s36_vendor_questions_framework,
    s37_ru_context, s38_qa, s39_closing_hero,
)


def main():
    p = setup_pres()

    slides_to_build = [
        s01_hero_alphafold_galactica,  # P0-1 FIX
        s02_cover,
        s03_lecture_map,
        s04_glossary,
        s05_central_question,
        s06_section1_divider,
        s07_we1_grant_idea_tree,
        s08_sakana_ai_scientist,
        s09_coscientist_vs_co_scientist,
        s10_sakana_cherry_pick,
        s11_bo_gp_alternative,
        s12_section2_divider,
        s13_alphafold_timeline,
        s14_alphafold_db,
        s15_boltz_open_source,
        s16_gnome_alab,
        s17_palgrave_critique,
        s18_aurora_ecmwf,
        s19_alphaproof_imo,
        s20_section3_divider,
        s21_exoplanet_cnn,
        s22_allen_microns,
        s23_ligo_ml,
        s24_alphafold_idp,
        s25_we_tess,
        s26_section4_divider,
        s27_notebooklm_elicit,
        s28_we2_bibliography,
        s29_frontiers_rat,
        s30_neurips_fake_citations,
        s31_icmje_policies,
        s32_section5_divider,
        s33_four_criteria,
        s34_we3_catalyst,
        s35_alternatives_matrix,
        s36_vendor_questions_framework,
        s37_ru_context,  # P0-2 FIX
        s38_qa,
        s39_closing_hero,
    ]

    for i, build_fn in enumerate(slides_to_build, 1):
        try:
            build_fn(p)
            print(f"  s{i:02d} ✓ {build_fn.__name__}")
        except Exception as e:
            print(f"  s{i:02d} FAIL {build_fn.__name__}: {e}")
            raise

    p.save(str(OUT))
    print(f"\nSaved: {OUT}")
    print(f"Total slides: {len(p.slides)}")


if __name__ == "__main__":
    main()
