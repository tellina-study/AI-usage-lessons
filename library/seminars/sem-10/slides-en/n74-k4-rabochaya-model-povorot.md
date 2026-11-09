---
id: n74
type: criteria_checklist_and_boundary
duration_min: 0.75
assertion: "Under rotation — right where n72 named perceptual hash's boundary — a working multimodal model tells a duplicate and a stranger receipt apart reliably: 96.7% against 23.3% across all 30 scans"
learning_goal: "Follow-up pass 2026-11-04 (issue #311), the owner's direct instruction: 'let's try to actually make a working case out of this after all.' n73 honestly promised: a different model or provider might behave differently, and the only way to find out is to repeat the same controlled test. The repeat was done: OpenRouter's catalog `/v1/embeddings/models` (40 models, 9 accepting a picture) was checked with the same margin test that told titan apart (n63/n64) — 3 of 5 candidates formally tell two random images apart but fail the margin test (don't tell a recompressed duplicate apart from a stranger document). The working candidate — `nvidia/nemotron-3.5-embed-1b:free`. Part 1 of 2 (n75 — semantic similarity, the other role of the same version 2): split, because the 15pt floor font size leaves no room for two tables and a conclusion on one frame."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A table "soft duplicate · hard duplicate (rotation)" for the working
    model and perceptual hash across all 30 CORD scans, a tile with n72's
    boundary.
  backup: >
    Numbers — stend/raw/case4_mm_full_retrieval.json::part_A_near_dup_retrieval
    (`nvidia/nemotron-3.5-embed-1b:free`, recall@1 across all 30 scans, not
    the sample of 6 as in n72's near_duplicate_injection_test). The
    model's choice — stend/raw/case4_working_mm_results.json, steps 1-2 (a
    margin test on 3 receipts: nemotron-3.5-embed-1b avg margin 0.593;
    voyage-multimodal-3.5, gemini-embedding-2, cohere-embed-5-fast —
    margin ≈ 0, formally tell pictures apart, but useless for retrieval).
    Methodology — the same origin as stend/README.md "Case 4, follow-up
    pass 2026-11-04."
---

# The repeat test found a working model

## Assertion

Under rotation, a working multimodal model tells a duplicate and a stranger receipt apart reliably — exactly where perceptual hash mixes them up.

## Visual

> **Found by a discipline of selection.** OpenRouter's catalog gave 9 candidates accepting a picture. 3 of 5 formally told two random images apart, but failed the margin test — a recompressed duplicate and a stranger document came out at almost the same distance for them. `nvidia/nemotron-3.5-embed-1b:free` passed both checks reliably.

| Method (all 30 CORD scans) | soft duplicate, recall@1 | hard duplicate (rotation), recall@1 |
|---|---|---|
| Working model (nemotron-3.5-embed-1b) | 100% (30/30) | **96.7% (29/30)** |
| Perceptual hash | 96.7% (29/30) | **23.3% (7/30)** |

> **n72's boundary got a numerical answer.** Under rotation, across all 30 scans — 96.7% correct hits for the working model against 23.3% for the fingerprint.

## Speaker notes

n72 honestly named the boundary: perceptual hash confidently catches soft near-duplicates, but weakens under rotation — in half of the six checked receipts, the distance to the rotated duplicate turned out comparable to the distance to a random stranger receipt. n73 promised: a different model or provider might behave differently right here, and the only honest way to find out is to repeat the same controlled test. The repeat was done after the session, and it had a result that wasn't known in advance — it could well have been the same failure.

First, it had to be found what to even try. OpenRouter's main model catalog doesn't contain embedding models at all — they live on a separate, not explicitly documented endpoint. Forty models turned up there, and nine of them accept both text and a picture on input.

The simple check — whether two random images are told apart from each other — passed for eight of the nine: only the already-known `amazon/titan-embed-image-v1` stayed broken. But that's not enough: telling two random images apart and being fit for similarity search are different requirements. The stricter margin test checked something else: must a soft near-duplicate of a document end up CLOSER to the original than a random stranger document. Three of the five models checked by the margin test, including a direct successor to the originally planned `voyage-multimodal-3`, formally passed the first check and failed this one — they didn't tell a recompressed duplicate apart from a stranger document at all. This is the same lesson already heard with titan: an error-free response doesn't mean the model uses the input's content. The one that turned out working and stable across three different receipts was `nvidia/nemotron-3.5-embed-1b:free` — a free NVIDIA model.

The result on the full thirty CORD scans — wider than the sample of six the earlier near-dup test was checked on — is a direct answer to n72's boundary. On the soft duplicate, both models work about equally well. Under rotation with edge cropping, the gap opens up: the working multimodal model finds the correct original in twenty-nine cases out of thirty — ninety-six point seven percent — while the fingerprint manages only seven cases out of thirty — twenty-three point three percent. This is exactly the architectural prediction already voiced at n66/n71 — comparing pictures in their own numeric representation — and it now has a working realization on this rig.

This finding closes exactly one question: detecting similar and rotated duplicates. The second question — whether a scan looks similar by meaning to another, different document — is the other role of the same version 2, and there the result is different. Next.
