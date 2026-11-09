---
id: s44
local_id: s3-05
section: "3. Design and new capabilities"
type: case_study
title: "Example: the AIFS and AIGEFS AI weather-forecast models"
assertion: "AIFS computes a 10-day forecast in 2.5 minutes instead of hours on a supercomputer — but does not do its own data assimilation"
source: "[ECMWF (arXiv 2406.01465, GMD Copernicus 2026)](https://arxiv.org/abs/2406.01465) · [NOAA (NWS SCN 25-89)](https://www.weather.gov/media/notification/pdf_2025/scn25-89_AIGFS_AIGEFS_and_HGEFS.pdf)"
media: "assets/razdel-3/aifs-aigefs/ecmwf-aifs-forecasting-system-diagram.jpg"
media_needed: "already downloaded (Tier 1, ECMWF). A hero scale was tried (issue #317, task A) — the same structural conflict as `s31`/`s32`/`s42`: hero narrows this slide's column of 4 plates below the working width of `PLATES`, and the blocking `[width]`/`[height]` do not go away even at a target below the 40% hero threshold. The previous side size is kept."
graf: "a"
blocks:
  - {label: "Classical mode (IFS / GEFSv12)", value: "hours on a supercomputer", note: "more than a thousand processors, a 10-16 day forecast"}
  - {label: "Model (AIFS, ECMWF)", value: "~2.5 minutes on one A100", note: "AIFS-SUBS (46 days) — ~920x faster, ~200x less energy", key: true}
  - {label: "Model (AIGEFS, NOAA, based on GraphCast)", value: "<4 minutes on one A100", note: "~0.3% of operational GFS compute cost"}
  - {label: "Honest boundary", value: "they do not do their own data assimilation", note: "without classical 4D-Var/GDAS, which folds observations into a picture of the atmosphere, the models simply have no input"}
in_bucket: true
status: draft
---

## Visible slide text

**What moved over.** NOAA doesn't choose between the models — it combines them: 31 runs of AIGEFS + 31 of GEFSv12 = the hybrid **HGEFS** ensemble, 62 members.

**An honest ceiling nearby.** Pangu-Weather is good "on average," weaker at the extremes — exactly where a forecast matters most.

## Speaker notes

Classical physical computation — the IFS model (ECMWF) and GEFSv12 (NOAA) — is precise, but requires more than a thousand supercomputer processors and several hours for a single forecast.

Both models' architecture is encoder–processor–decoder: the "encoder" translates the raw data grid into a compact representation, the "processor" is the main part, where the attention mechanism or message-passing does the work (the design is broken down on the previous slide), the "decoder" translates the representation back into a forecast. AIFS (ECMWF) is a graph transformer, with a 16-layer transformer processor using a sliding attention window; trained on 38 years of ERA5 reanalysis data plus 8 years of operational analyses. AIGEFS (NOAA, based on DeepMind's GraphCast) is a message-passing graph network, a 16-layer processor, around 36.7 million parameters.

An important honest detail, shared by both models: neither AIFS nor AIGEFS does its own data assimilation — both take an already-prepared analysis of the atmosphere from a classical system (4D-Var for AIFS, GDAS for AIGEFS). Without classical assimilation, neither forecast model exists. Result: AIFS delivers a 10-day forecast in ~2.5 minutes on a single processor against hours on a supercomputer; AIGEFS, under four minutes, ~0.3% of GFS's compute cost. Both have been operational since 2025 at different weather services.

What moved over: the freed-up compute budget turned out to be so large that NOAA does not choose between the old and the new model, but combines them in the hybrid HGEFS ensemble — 31 runs of AIGEFS plus 31 runs of the classical GEFSv12, 62 members. An honest ceiling nearby: China's Pangu-Weather is good "on average," but weaker exactly where an accurate forecast matters most — at the extremes. Three selection conditions are met with the strongest evidentiary grade in the section.
