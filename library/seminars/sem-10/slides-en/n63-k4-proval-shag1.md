---
id: n63
type: content
duration_min: 1.0
assertion: "The model the plan was counting on doesn't exist on this rig under any spelling of its id — but a replacement was found quickly"
learning_goal: "Failure, step 1 of 3: the model from the plan wasn't found; a search found a working replacement. The first third of the failure's story is an honest search, not an instant dead end. Edit per issue #311 (owner: 'slide 59 isn't clear and what's it for?'): the fix — do NOT merge with n64/n66 (SETKA-KEYSOV.md Case 4, 'Note (Case 4's internal asymmetry, the failure beats),' names outright the reason for presenting it separately: this is a sequential REFUTATION of option (b) by a live run — candidate found → how it was checked → what the check showed — not a single result snapshot that could have been shown upfront; merging would destroy that order). Instead of merging — an explicit frame BEFORE Step 1 itself: why check whether the model exists at all, rather than jumping straight to whether it works."
visual:
  pattern: content
  primary: >
    A frame tile: why this beat exists — a provider's model list is not a
    fact you can rely on in advance when planning; the only reliable check
    is a direct API call. A fact tile: the plan's model wasn't found, the
    catalog of 452 models contains no embedding models in the main
    listing; a fact tile: a working candidate was found.
  backup: >
    SETKA-KEYSOV.md Case 4, "The failure that is part of the case's
    story," Step 1, verbatim + a new frame tile added by this edit (issue
    #311).
---

# Failure, part 1: the plan's model doesn't exist

## Assertion

Embedding models live with this provider in a separate, not explicitly documented list — and this isn't a typo in the plan.

## Visual

> **Why this beat exists.** A provider's model list can't be relied on in advance when planning: the catalog changes without notice. The only reliable check is a direct API call by a specific model id; this breakdown of the failure starts with exactly that.

> **Step 1.** `voyage-multimodal-3`, the model the plan originally counted on, wasn't found on this rig's OpenRouter under any of the checked spellings of the id. The full model catalog (452 entries) contains not a single model with "voyage" or "embed" in the name at all.

> A search of real candidates found exactly one working multimodal model — `amazon/titan-embed-image-v1` — it accepts both text and a picture, and returns a vector without an error.

## Speaker notes

The second option — multimodal embedding — deserves a separate beat because it doesn't "work worse than expected." It doesn't work, and how that was discovered is a lesson worth walking through step by step: one summary line won't do here.

First step: the model built into the plan doesn't exist. `voyage-multimodal-3` wasn't found on this rig's OpenRouter under any of the checked spellings of the identifier. It's important to understand this correctly: this isn't a typo in the plan and not a misspelling of the name. In OpenRouter's full model catalog — four hundred fifty-two entries — there isn't a single model with "voyage" or "embed" in the name at all. Embedding models live with this provider in a separate, not explicitly documented list that the main catalog simply doesn't show.

The story didn't end there. A search of real candidates — a systematic check; calling it guesswork would be wrong — found exactly one working multimodal model: `amazon/titan-embed-image-v1`. It accepts both text and a picture as a data URL on input, and returns a vector without an error. At this point, if the check had stopped here, the case would have gone into the plan as working on the second attempt.

But the check didn't stop there — and that's exactly why the second, more serious finding turned up.

The search wasn't needed just from reading the provider's documentation. The model catalog at services like this gets updated often, old models are sometimes pulled from publication, and new ones get added without a wide announcement — and a plan written in advance fundamentally cannot guarantee that the model named in it will be available right at build time. The only reliable way to check this is a direct API call with a specific model name; reading the model list on the provider's website, which can go stale or not reflect the full lineup, isn't enough here.
