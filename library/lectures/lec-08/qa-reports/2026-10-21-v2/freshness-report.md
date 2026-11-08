# Freshness Report — Lecture 8 chapter — 2026-10-21

Companion to `library/lectures/lec-08/chapter-critique-v2-facts.md` (full fact-check). This file
tracks only time-sensitive claims per the Freshness Pre-Flight protocol: AI benchmark/tool pricing
(weekly cadence), market-share/usage stats (quarterly), tool feature lists/recent releases
(monthly), conceptual claims (yearly+). All claims below checked on 2026-10-21; delivery date of
Lecture 8 was not found in `catalog/manifests/lectures.yaml` (still `status: draft` for this
rework — prior produced entry is the superseded May 2026 version) — treat every item below as
**verify again on the actual day of delivery**, whenever that is scheduled.

## Top items needing re-verification on day of lecture

| # | Fact | Source date | Cadence | Verify-on-day-of-lecture |
|---|---|---|---|---|
| 1 | Midjourney V8.1/V8.2, Adobe Firefly Image 5 pricing (~$0.03–0.05/image) | 2026-10 (WaveSpeed, ToolColumn) | monthly | **YES** |
| 2 | Suno pricing (~$0.015–0.02/song) | 2026-10 (CostBench) | monthly | **YES** |
| 3 | ElevenLabs pricing (~$0.04–0.20/min) | 2026-10 (FelloAI, OakGen) | monthly | **YES** |
| 4 | Sora fully shut down (web/app Apr 26 2026, API Sept 24 2026), no successor named | confirmed live 2026-10-21 | monthly | **YES** — check OpenAI's deprecations page for a successor announcement |
| 5 | Kling 4.0 "current flagship" (Oct 15 2026) / Veo 3.1 / Kandinsky 6.0 Video | 2026-10 | monthly | **YES** — this category of claim (named current flagship) is explicitly the one that broke the May 2026 version of this lecture (Sora) |
| 6 | Getty Images bankruptcy/restructuring status ($533M capital, $270M debt write-off, going private) | announced literally the same day as this chapter (2026-10-21) | monthly (active corporate action) | **YES, urgently** — this is the single freshest, least-settled fact in the entire chapter; restructuring terms can still change before court confirmation |
| 7 | Getty v Stability AI (US) litigation status (motion to dismiss mostly denied, no trial date) | 2026-04 ruling, no update since | monthly (active litigation) | **YES** |
| 8 | Getty v Stability AI (UK) appeal (permission granted Jan 2026, outcome pending) | 2026-01 | monthly (active litigation) | **YES** |
| 9 | NYT v OpenAI summary judgment status (no ruling yet) | ongoing as of 2026-10 | monthly (active litigation) | **YES** |
| 10 | RIAA v Suno/Udio matrix (Warner settled both; UMG settled Udio only; Sony suing both; second Suno V6 suit Sept 2026) | 2026-09 | monthly (active litigation) | **YES** |
| 11 | Checkr "Hiring Hoax 2026" survey (40% vs 31% YoY fraud encounter rate) | Sept 2026 | quarterly (survey) | next check due ~Dec 2026; flag if lecture lands after that |
| 12 | Upwork "In-Demand Skills 2026" (+109%/+329%/+95% YoY) | Feb 2026 report, FY2025 data | quarterly | next official update expected ~Feb 2027; stable until then but note it is already 8+ months old relative to this chapter's own write date |
| 13 | Checkr/FBI deepfake-hiring advisory (eleven-nation, 31.07.2026; FBI repeat warning 14.10.2026) | Oct 2026 | monthly (active/evolving threat reporting) | **YES** |

## Lower-priority / stable items (yearly+ or settled)

- CDPA legal reasoning, Carlini et al. 2023 memorization research, LAION-5B dataset mechanics,
  C2PA/Content Credentials standard — conceptual/architectural, yearly+ cadence, no action needed
  before next major legal development.
- CNET 2023, Sports Illustrated 2023–2024, Coca-Cola/Toys "R" Us 2024–2025 sentiment data — closed
  historical episodes, stable.
- News Corp × OpenAI $250M/5yr deal (May 2024) — closed deal, stable.

## Single most important freshness risk

**Getty Images' bankruptcy restructuring (item #6)** was announced on the exact date this chapter
was written (2026-10-21) and is the freshest fact in the entire document — fresher than the
chapter itself. Any gap between chapter finalization and lecture delivery carries real risk that
court confirmation, creditor objections, or a competing bid could change the $533M/$270M terms
before the lecture is given. This is also the chapter's own strongest, most pedagogically valuable
beat (the self-correction narrative, §5.3) — recommend the lecturer specifically re-pull Getty's
own investor-relations page and PetaPixel/Bloomberg coverage within 48 hours of delivery, not just
trust the October 21 snapshot in the chapter.

## Verdict

NEEDS-REFRESH-ON-DAY-OF-LECTURE for items 1–10 and 13 (11 of 13 tracked items). This is expected
and appropriately flagged already in the chapter's own frontmatter (`verify_day_of` list in
`chapter.md`), which correctly names items 1–3, 4 (Sora), and 11 (Checkr) — but does **not**
currently name items 5–10 (tool-flagship status beyond Sora, and all four litigation threads,
including the Getty bankruptcy itself). Recommend expanding the frontmatter `verify_day_of` list to
cover the full litigation/corporate-status set above, not just pricing and the Sora/Checkr items
already listed.
