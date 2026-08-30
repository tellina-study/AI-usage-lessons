---
id: s24
type: assertion_visual
duration_min: 2
assertion: "RIAA v. Suno/Udio (24.06.2024). UMG settled Udio 29.10.2025 (in talks with Suno). Warner settled Suno (litigating Udio). Sony — actively litigating both. Suno SJ July 2026."
learning_goal: "Case 4: licensing under litigation pressure — music"
learning_outcomes: [LO4]
chapter_ref: "§3.5 — RIAA v. Suno/Udio"
references: [riaa-suno-press, umg-udio-урегулирование]
visual:
  pattern: assertion_visual
  primary: "RIAA press release screenshot + settlement timeline (24.06.2024 → 29.10.2025 UMG → July 2026 Suno SJ) + «Lesson: licensing under litigation pressure»"
  backup: assets/backup/s24-riaa.png
---

# RIAA v. Suno/Udio — licensing under litigation pressure (Case 4)

## Assertion

RIAA v. Suno/Udio (24.06.2024). UMG settled Udio 29.10.2025 (in talks with Suno). Warner settled Suno (litigating Udio). Sony — actively litigating both. Suno SJ July 2026.

## Visual

On top, the assertion 22pt. On the left — an RIAA press release screenshot mock-up in an Ocean rounded box: "RIAA Sues AI Music Companies Suno, Udio for Mass Copyright Infringement." On the right — a settlement matrix 3×2 (3 majors × 2 defendants): UMG × Udio (green — settled, joint platform 2026); UMG × Suno (light — in talks); Warner × Suno (green — settled, royalty + equity Sep 2025); Warner × Udio (gold — litigating); Sony × Suno (gold — litigating, SJ July 2026); Sony × Udio (gold — litigating). Below — a gold "LESSON FOR THE ENGINEER": "Licensing under litigation pressure is the actual outcome: 4 of 6 lawsuit combinations are already settled or in talks. This is a new business-model layer, not 'a ban on all AI music.'"

## Speaker notes

The fourth copyright case — RIAA v. Suno and Udio. The lawsuits were filed on June 24, 2024, by the Recording Industry Association of America on behalf of the three major labels (the Big Three) — UMG, Warner, and Sony. Theory — Suno and Udio trained music-generation models on the major labels' catalogs without a license. The chronology of settlements is distributed unevenly across the 3-majors × 2-defendants matrix. On October 29, 2025, UMG settled with Udio — they formed a joint platform for 2026; UMG ↔ Suno is in talks. In September 2025, Warner signed a licensing deal with Suno (royalty plus equity), but Warner ↔ Udio — litigation continues. Sony Music — actively litigating with both defendants, pushing toward summary judgment. The Suno summary judgment hearing is scheduled for July 2026, the exact date subject to verification closer to the lecture. What this sequence means practically. This is not "all AI music banned." It is licensing under litigation pressure — a model in which initial lawsuits convert into licensing deals. Of the six lawsuit combinations (3 majors × 2 defendants), four are already settled or in talks. This is a pattern we have seen in the music industry more than once: Napster — banned, then Spotify — licensed; YouTube — initially a lawsuit with Viacom, then Content ID plus licensing. Generative AI music follows the same evolutionary path. Lesson for the engineer: licensing under litigation pressure is the actual outcome: four of six lawsuit combinations settled or in talks. This is a new business-model layer, not "a ban on all AI music." If you build a music-related AI product, expect a licensing requirement as part of the business model. This does not make the product unbuildable — it makes it more expensive and more legally compliant. Those who build without a licensing infrastructure will hit the same dead end that Suno hit at the stage of the initial RIAA lawsuit. Those who build with a licensing infrastructure from the start — follow the Adobe Firefly playbook, where a licensed corpus is a core business asset, not a nice-to-have. And most importantly — even after all the settlements, an output-similarity check remains mandatory regardless of the licensing status of the training data: licensing on the input does not release you from liability for an output that verbatim reproduces a specific protected song.
