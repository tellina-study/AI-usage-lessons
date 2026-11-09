---
id: n76
type: criteria_checklist_and_boundary
duration_min: 0.5
assertion: "An image-embedding model run locally, entirely without OpenRouter, works with no network and no provider catalog — and on this measurement is noticeably weaker than the found API candidate on both substantive metrics"
learning_goal: "The one, separate experiment — not a continuation of the candidate search inside OpenRouter (n74/n75), but a different class of solution: embedding a picture with no provider at all. The reason — the owner's remark on the session's plan: 'is there really no local embedding model for pictures?' — a fair point that CLIP (and its neighbors SigLIP, DINOv2) is the local industry standard for exactly this task, with no dependence on a provider's model list, which changes without warning (the same problem that opened the section at n61)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A table "metric · CLIP locally · API candidate (context) · perceptual
    hash (context)," an honest-conclusion tile (works, less accurate, but
    no network and no provider catalog).
  backup: >
    Numbers — stend/raw/case4_local_clip_results.json: part_A_near_dup_
    retrieval.summary (clip_hard_dup_recall_at_1, 30 scans),
    part_C_semantic_similarity_agreement.summary (clip_semantic_agreement_
    recall_at_1 and chance_level_recall_at_1, 30 scans), timing (avg_clip_
    forward_pass_s_per_image), environment (install_method, packages). The
    API-candidate and perceptual-hash columns are the same numbers already
    shown on n74/n75 (nvidia/nemotron-3.5-embed-1b:free), here only for
    context on the gap's size, not a repeat measurement.
---

# The one experiment: a model with no OpenRouter at all

## Assertion

A local CLIP model works with no network and no provider catalog — and on this measurement is noticeably weaker than the found API candidate on both metrics.

## Visual

> **A separate question from the session's plan.** A provider's model list changes without warning — the same problem that opened this section at n61. CLIP is the local industry standard for picture embedding, with no provider catalog at all. The one such experiment in this section.

| Metric, recall@1 | CLIP, locally | API (context) | phash (context) |
|---|---|---|---|
| hard duplicate (rotation) | **76.7% (23/30)** | 96.7% (29/30) | 23.3% (7/30) |
| semantic similarity | **13.3% (4/30)** | 26.7% (8/30) | 3.3% (1/30) |

> **Honest conclusion.** CLIP works locally, in seconds, with no network and no provider catalog — and on this measurement is noticeably weaker than the API candidate on both metrics. Independence and speed are its benefit; it doesn't cover accuracy.

## Speaker notes

This experiment has a different reason than the model search across the previous two beats. There, we were looking for a working candidate inside OpenRouter's catalog — same provider, different model. Here the question was put directly on the session's plan: a provider's model list changes without warning — exactly the problem that already opened the section with titan — so isn't there a way to do image embedding without any such catalog at all? There is a way, and it's the industry standard for the task: CLIP, and alongside it SigLIP and DINOv2 — models downloaded once and computed on your own machine, with no HTTP, no provider, no risk of "model not found."

The check took a ready-made CLIP ViT-B/32 model and ran it through the same measurement the working model via OpenRouter already went through: all thirty CORD scans, both substantive metrics. Under rotation with edge cropping, CLIP finds the correct original in twenty-three cases out of thirty — seventy-six point seven percent. That's noticeably weaker than the API candidate, which gets twenty-nine out of thirty, but three times more reliable than perceptual hash with its seven out of thirty. On semantic similarity, the result is relatively weaker: thirteen point three percent agreement with the text reference against twenty-six point seven for the API candidate — while still four times above pure chance level, three point four five percent.

The install took about a minute and four gigabytes of disk — the environment and the model's own weight, both in `.gitignore`, don't make it into the commit. One forward pass over a picture is a bit over a tenth of a second on an ordinary CPU, with no internet at all. Comparing that number directly to a bit over a second for a call through OpenRouter would be dishonest: that figure includes not just the model itself, but also the network round trip through the n8n webhook and polling for the result.

The conclusion from this experiment is direct: a local model works and solves the same task with no network and no dependence on a provider's catalog — but on this specific measurement, its accuracy is lower than the found API candidate's on both metrics. The local model's independence and speed have a price — accuracy, which is what you pay with. The choice between them depends on the specific task and the tolerance for error.
