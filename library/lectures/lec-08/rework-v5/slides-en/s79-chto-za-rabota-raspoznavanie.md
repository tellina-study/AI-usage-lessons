---
# Source: chapter/chapter-part3d.md §§ 5.1 (industry terms), 5.2 (three questions),
# 5.3 (three families of methods), 5.4 (what decision, and why it's last), 5.5 (the classical mode).
# Six parts of the stage description in canonical order.
# The baseline of the classical mode for editorial fact-checking (40–61% with ≈2% corrected)
# stands HERE, before the case studies: without it, the numbers in s86 read incorrectly.
#
# CONSOLIDATION (#301, Section 5 overhaul): merged with the former s79a ("Three questions about
# provenance and four classical ways to answer them") — both frames carried the same narrative
# arc beat, "general description of the stage, the classical mode with its baseline," and were
# split into two frames only during the fix for the first render (height). Numbers,
# plates, and the diagram carried over UNCHANGED; minutes added (0.4+0.4=0.8), the section's
# total untouched. The old `s79a` was removed as a separate file.
id: s79
local_id: "s79"
section: "5. Recognition and Provenance"
type: assertion_visual
title: "What this work is, and how it was done without a model"
assertion: "The stage makes two binary decisions — 'release or not' and 'treat as authentic or not' — both irreversible in their consequences; the input is a finished artifact, and the first thing an engineer must be able to do is distinguish three different questions that are constantly conflated: what is depicted here, how it was made, and who is accountable for it, and none of the three answers the question 'is this true'; there are four families of classical ways to answer, and a trained model has entered two of them, while the third — editorial and expert procedures — it has not entered and cannot"
source: "independent audits of newspaper accuracy"
chapter_ref: "chapter-part3d.md §§ 5.1–5.5"
media: "assets/screenshots/s79-piaggio-machine-1756.jpg"
media_needed: ""
media_note: "Wikimedia Commons, File:Abbot Piaggios machine Device-to-unroll-papyri 1756 Vatican.jpg, public domain. Tier 2 (Wikimedia Commons). Abbot Piaggio's machine, 1756, the Vatican — a device for physically unrolling charred papyri, that is, literally the classical mode of one of the four jobs listed here, and the very one that destroys the object. No source caption on the slide"
blocks:
  - {label: "Editorial fact-checking — classical mode", value: "40–61% of articles — with an error", note: "independent accuracy audits; this is an ordinary newsroom, with no model at all"}
  - {label: "Of these, publicly corrected", value: "about 2%", note: "that is, every other article has an error, and about one in fifty admits it", key: true}
  - {label: "Authenticity expertise and manual restoration", value: "weeks and months, no cost figure", note: "the practice is documented, figures are not published — no multiplier relative to expertise is counted anywhere in the section"}
blocks_per_row: 3
# Overhaul (#301): the `dorozhki` diagram "three questions / four families" (former
# s79a) was DROPPED from the visible layer — measurement showed [height] overflow of the body
# with media+blocks+diagram on one frame ("primitives ate the frame," −1.24"), and the image
# cannot be dropped (illustrations are not to be touched, work order of round #301). The diagram's
# content was not lost: it stands in full in the notes below, in the same wording as before.
timing_min: 0.8
in_bucket: false
method_steps: ["general description of the stage", "classical mode with baseline", "three questions"]
form: []
vfy: false
status: собран
---

## Visible slide text

**Without a model, every other article has an error; it is admitted in every fiftieth.** None of the three questions answers "is this true": a genuine photo can lie, a generated one can tell the truth.

## Speaker notes

The industry calls this stage by different names depending on the trade, and it's worth reconciling them, because from here on they will appear interchangeably. In a newsroom it is fact-checking and source confirmation. In museum and archival work it is attribution and authenticity expertise. In technical literature it is recognition, as opposed to generation, and provenance — that is, traceable origin. On platforms it is moderation and disclosure. The task is the same for all of them: given a finished work, answer a question about it, generating nothing new.

Why the stage comes last. First, by the order of production: it works on the finished thing. Second — and this is more interesting — it has the inverse economics relative to all four previous modalities: one forward pass against dozens of denoising steps. Third, this is where the evening's third payment address closes out. As long as a signature, a voice, a face, and an origin confirmed themselves, the stage was cheap and nearly invisible. Once they stopped confirming themselves, people started paying for it.

The numbers for the classical mode are worth repeating slowly, because without them the case studies that follow read incorrectly. Independent audits of newspaper accuracy put the figure at forty to sixty-one percent of articles containing at least one error. About two percent are publicly corrected. That is, an ordinary newsroom, with no trained model at all, errs in roughly every other article and admits it in roughly one in fifty. This pair is worth reading twice — it is the baseline against which both of the section's editorial breakdowns will be read.

For the other two classical modes — authenticity expertise and manual restoration — there are no numbers. The practice is documented, timeframes are given in weeks and months, but the sources give no cost figures. So no multiplier relative to expertise is counted anywhere in this section, and that is a decision, not a gap in preparation.

The stage makes two decisions, and both are binary, and both are irreversible in their consequences. The first — "release or not": in a newsroom, on a platform, in distribution. The second — "treat as authentic or not": in a museum, in court, in an archive. What's been released cannot be unreleased: a retraction is read by a smaller share of those who read the original material. An attribution is withdrawn by scandal, not by order, and the reputational cost of the withdrawal falls on whoever assigned it. It is exactly this irreversibility that explains why the time norm for a check matters so much here — not just the tool's accuracy.

The first thing an engineer in this field must be able to do is distinguish three different questions that are constantly conflated into one. Question one: what is depicted or written here. This is content recognition: reading damaged material, attribution, archive search, automatic labeling, translation, speech recognition. The answer is checkable — a transcribed text can be cross-checked against another source, a found image can be looked at. Question two: how was it made — shot by a camera or synthesized, written by a human or a model. The answer is probabilistic and extremely sensitive to whether the recognizer has ever seen the model that produced it. Question three: who is accountable for it. This is provenance: the chain from shooting to publication, signatures, rights, the responsible editor. The answer is not about the content at all — it's about people and organizations.

None of the three answers the question "is this true," and this is worth remembering as a criterion. A detector says how it was made; provenance says who is accountable; the truth of a statement follows from neither one. Swapping one question for another is the single most common error in discussions of this topic, and it occurs even among people who understand how the mechanism works.

Data for judgment is obtained by three families of methods, and the first has nothing to do with machine learning at all. Physical methods answer about the material independent of what people think about the object: tomography, X-ray fluorescence analysis, infrared reflectography, which reveals the underdrawing beneath the paint, ultraviolet light, pigment spectral analysis, radiocarbon dating, dendrochronology. Digital traces — file metadata, edit history, checksums, reverse image search; the cheapest and most fragile family, because any re-save, re-compression, or screenshot destroys the traces completely. Editorial and expert procedures — a call to the source, a second independent source, cross-checking against the primary document, a subject-matter expert, a collegial decision; the most expensive family in terms of time and the only one that answers the third question. Machine learning has entered the first family as a way to read what instruments measured, and the second as a recognizer. It has not entered the third, and cannot: the question of accountability is not a technical question at all.

For practice, this breakdown yields a rule for choosing a tool, one that should be applied before any technical question. First, determine which of the three questions you are answering. If the first — the task has a checkable answer, so you can demand a number and measure it on your own data. If the second — the answer is probabilistic and extremely sensitive to the origin of the material, so a vendor's number does not apply to your data until you have re-measured it. If the third — technique will only help partially, because it is a question about people, contracts, and procedures, and a trained model does not enter into it and cannot.
