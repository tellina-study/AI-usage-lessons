---
# MANDATORY CONTENT FIX (#301, Section 5 overhaul work order, item "s85 — this is TWO
# different events"), not a form fix. Source: research/F-sverka-pervoistochnikov.md, finding
# F1 + "Orchestrator appendix." Was: a single "Nikon Z6III camera signature," September 2025,
# multi-exposure. BECAME: two SEPARATE discoveries by one researcher (David Buchanan,
# blog da.vidbuchanan.co.uk, "C2PA Cameras Do Not Survive Contact With Reality") — August 25,
# 2026 (the StrongBox exploit, root REQUIRED) and October 2, 2026 (a hole in the C2PA
# specification itself, root NOT required). Mixing them is forbidden: the events have
# different conditions, and merging them yields a claim stronger than one source and weaker
# than the other (see `research/F-sverka-pervoistochnikov.md`, finding F1).
#
# FINDING (not fixed by this round, fixing the chapter is not my territory): chapter-part3e.md
# § 5.18 never names the camera brand at all ("a camera manufacturer," no make/model) and
# carries a mechanism that matches NEITHER of Buchanan's two events (multi-exposure, firmware,
# September 2025 — neither the root exploit nor the spec hole). "Nikon Z6III" existed only in
# the frame layer and never appears in the chapter — looks like an unverified addition made
# during slide production. The chapter now diverges from the frame; fixing it is outside the
# scope of the overhaul and outside my section (book-editor); it is only named here as a finding.
# CONSOLIDATION (#301, Section 5 overhaul): merged with the former s85a ("What broke here and
# what didn't") — that frame was a second two-column breakdown of the SAME case (what held up /
# what failed), split out into a separate file only during the fix for the first render. A full
# merge into a single two-column form with four columns at once is not possible (the
# `comparison` form holds exactly one pair of columns) — the second pair becomes `itog`, the
# same phrase `s85a` closed with: the section's lever, checked verbatim against the audio track
# and the chapter (`STROENIE-IZ-ZAPISEY-part4.md` §2.3). The rest of `s85a`'s content (what held
# up / what failed) already goes verbatim into the notes of both frames — carried over without
# loss. Minutes added (0.5+0.5=1.0). The old `s85a` was removed as a separate file.
id: s85
local_id: "s85"
section: "5. Recognition and Provenance"
type: comparison
title: "Bypassing a camera signature: an exploit and a hole in the specification"
assertion: "Two separate discoveries by one researcher, and they must not be mixed: on August 25, 2026 — bypassing a Google Pixel camera signature via a root exploit (CVE-2026-43499, an ordinary Linux kernel vulnerability), where an attacker with root makes the protected StrongBox module sign arbitrary data with the same key as the real camera; Google acknowledged the vulnerability with a 'Won't fix' status, paying $7,500. On October 2, 2026 — a hole in the C2PA specification itself, and here root is not needed at all: the entire file can be excluded from the hash, so the signature and timestamp stand over an empty string. The August finding requires root, and an honest formulation must say so; the October one requires nothing, and only it earns the strong formulation 'a camera signature is worth nothing'"
source: "David Buchanan (retr0id), 'C2PA Cameras Do Not Survive Contact With Reality,' personal researcher blog, August 25, 2026 (first discovery) and October 2, 2026 (second); CVE-2026-43499; an independent writeup of the second discovery — workos.com, quoting the primary source"
chapter_ref: "chapter-part3e.md §§ 5.17–5.18 (the chapter still carries the earlier storyline, which does not match this fix — see the finding above)"
media: ""
media_needed: "no image of a camera/verification app was sourced for this storyline in this round: this is a forms overhaul, not illustration production (the 6-tier sourcing process is the designer's job). There was a photo of the Nikon Z6III on the neighboring frame s85a — removed as factually incompatible with the fix (the storyline is no longer about Nikon)"
columns:
  left:
    head: "August 25, 2026 — the StrongBox exploit"
    items:
      - "requires root on the device — CVE-2026-43499, an ordinary Linux kernel vulnerability, not camera-specific"
      - "with root, the attacker signs arbitrary data with the real camera's key"
      - "victim — Pixel Camera, C2PA Level 2 certification — a model case, not a weak one"
      - "Google: 'Won't fix (infeasible),' $7,500 — a fix would mean rebuilding the pipeline to run entirely inside the enclave"
  right:
    head: "October 2, 2026 — a hole in the specification"
    items:
      - "root and device access not needed — it's the format that breaks, not the phone"
      - "'excludable byte ranges': the hash excludes the file — the signature and timestamp stand over an empty string"
      - "example: a lottery ticket photographed, the numbers written in AFTER the drawing — the signature still claims the shot predates the drawing"
      - "Neal Krawetz warned in June 2025: neither the specification nor the vendor has been fixed"
timing_min: 1.0
in_bucket: true
method_steps: ["boundary of the method", "two documented failures, kept separate", "what held up and what failed", "lesson"]
form: []
vfy: true
status: собран
itog:
  yarlyk: "Conclusion"
  text: "a signature attests WHO signed — not WHAT was in front of the lens"
---

## Visible slide text

**Two discoveries by one researcher, and they cannot be merged into one:** one needs root on the device, the other needs only the file itself.

**In both, the cryptography worked as promised:** the signature is genuine, the hash checks out. What failed is what the signature doesn't cover.

## Speaker notes

The industry talks about image provenance in two opposite ways: a signature outside the file and a watermark inside the pixels. A signature outside — a manifest is embedded in the file: who the author is, what created it, what was applied — and it's signed with a certificate; the binding is fragile by construction, a screenshot or re-compression tears it. A watermark inside lives in the pixels and survives that kind of processing, but it has its own limit — it weakens where there's almost nothing to choose from. Both discoveries in this frame are about the first method, the signature outside, and both are about the fact that the cryptography in them never broke, not once.

The first discovery, August 25, 2026. Researcher David Buchanan (handle retr0id) showed on his own blog a way to bypass a Google Pixel camera signature with no re-photographing of a screen at all. The condition — root on the device, obtained through a known local privilege-escalation exploit (CVE-2026-43499, a Linux kernel vulnerability, a use-after-free in rtmutex — an ordinary operating-system bug, in no way specific to cameras). With root, the attacker doesn't steal the key: he asks the hardware-protected StrongBox module to sign arbitrary data, including a fully generated image, with the same key the genuine camera signs with. The affected application — Pixel Camera — at the time of the finding carried the highest trust certification of the C2PA Conformance program, Assurance Level 2: what breaks is not a weak case but a model one. Google acknowledged the vulnerability, paid seven thousand five hundred dollars, and closed the report with the status "won't fix, infeasible" — a fix would mean rebuilding the entire image-processing pipeline to run entirely inside the secure enclave.

The second discovery, five weeks later, October 2, 2026 — and this is NOT the same thing, even though the researcher is the same and the topic is the same. Here what's broken is not one manufacturer's phone but the C2PA specification itself, and it's broken with no root, no exploit, no device access at all. The mechanism — "excludable byte ranges," provided for by the specification itself: from what the hash and signature cover, an arbitrary section of the file can be excluded, and nothing stops excluding it entirely. The signature and timestamp in such a file stand literally over an empty string — a mathematically correct signature attests nothing of substance. The illustration the writeup itself gives: photograph a real lottery ticket before the drawing, then write into the already-signed shot the numbers announced after the drawing — the signature keeps asserting that the shot was taken before the drawing. There was advance warning of this: independent researcher Neal Krawetz wrote about too broad an excludable range back in June 2025 — a year before the finding nothing had changed, and as of the writeup's publication date neither a specification fix nor a vendor fix has been announced.

Why they must not be glued into one "camera-signature bypass." The events have different entry conditions, and that is not a formality. The August one can only be honestly stated with the caveat "root required" — without it, the audience will hear "a camera signature is worth nothing," which is false for the August case: without root, there's no attack. The October one, by contrast, earns exactly that strong formulation, because it needs nothing — no root, no device access, only the file itself. Combined without their conditions, the two discoveries form a claim stronger than one source and weaker than the other — exactly the kind of precision error the course calls out separately.

What the two share, despite different conditions. The cryptography in both cases performed exactly as documented: the signature is genuine, the chain is intact, the math checks out. What failed was not the encryption — what failed was an assumption that everyone around the mechanism held in their head and no one wrote down: "if the file is signed, the signer vouches for the content." The August case breaks this assumption by substituting the data that a legitimate key signs. The October one breaks it even more radically: there doesn't even need to be anything substantive to sign.

From this comes a formulation worth taking away from the section whole: a signature attests WHO (and with what) signed, not WHAT was in front of the lens, and in the October case — not even that there was anything to sign at all. This is the same class of error the course already examined with constrained decoding in the lecture on language models: the mechanism did exactly what it promised, and what it promised was not what people expected of it. When checking any attestation mechanism, it's worth asking the same question — exactly what claim does it make checkable — and for both discoveries in this frame the honest answer is one: checkable is who holds the key; not checkable is what was in the frame.

A second boundary of the same kind, and it's structural. A language model's answer, equipped with document search, has a citation: the system found a passage, placed it in context, and can name where it came from — checking is possible, open the document. A generated image has no citation and can't have one. A detail in the frame — say, the shape of a coat's clasp — wasn't taken from any specific training image: it was arrived at by denoising, step by step, until a shape plausible for this prompt formed in that spot. There's no one to ask "where is this clasp from," nowhere to insert a ground truth into the denoising process; the prompt suggests a shape and contains no truth at all. The conclusion that follows matters for judging the technology as a whole: "document search for pictures" is an error in how the problem is framed, not a missing feature that will eventually get built. Checking a generated image stays outside the model: cross-referencing a ground truth, a blueprint, physics, a person who saw the object.

A shared thought that closes both halves of the section. The line between what was shot and what was synthesized was blurred by an ordinary working pipeline and a hole in the specification itself, not by a villain's attack out of a hacker movie. A frame coming out of real-time neural-network graphics was not shot or drawn by anyone — fifteen out of every sixteen pixels on screen are generated by a network, and there's no malicious intent in it at all, it's a quality setting in a game. A file with a signed forgery carries a genuine signature from a genuine key and depicts something that was never in front of a lens — and in the October case, this doesn't even need root, just knowledge of the format.

For practice, this raises a question worth asking of any authenticity-verification system: exactly what does it attest, and what assumption links the attested fact to what you actually care about. Here, what's attested is who (and with what) signed; what's cared about is what happened in front of the lens; the assumption linking them is exactly what both discoveries break — one with root, the other without any at all.
