---
id: s30
section: "1. Still Image"
type: analitika
title: "Legal Case: Getty v. Stability — What the Court Decided, What It Didn't, and What It's Valued At"
assertion: "The same dispute is lost in two jurisdictions in two different ways. The narrow win came on the trademark — through the one channel where infringement is visible on the output. And a fiftyfold spread in the valuation comes from nothing but the choice of rate inside the classical mode"
grafa: "the genre differs from the other cases, and that's stated outright: a court ruling has neither the price of both errors in one unit, nor a classical mode, nor the name of a product-maker"
adres_osi: "RIGHTS"
source: "the High Court of England and Wales, Mrs Justice Joanna Smith, ruling November 4, 2025 · permission to appeal granted January 2026; no appellate ruling as of 27.10.2026 · stock agency price lists · label licensing agreement terms, 29.10.2025 and 25.11.2025 · denial of rehearing, US, March 2, 2026 · the EU AI Act, applicable from August 2, 2026 · Federal Law No. 243-FZ, in force since 01.09.2026"
chapter_ref: "chapter-part1d.md — the legal case, the corpus economics, the jurisdiction overview"
forma:
  - "what the court decided"
  - "what it didn't decide"
  - "how this differs from the neighboring jurisdiction"
blocks:
  - {label: "What was decided", value: "the model's weights are not an infringing copy", note: "under UK copyright law; secondary infringement wasn't proven"}
  - {label: "The plaintiff's narrow win", value: "on trademark", note: "the generated images contained artifacts of the plaintiff's watermarks", key: true}
  - {label: "The corpus: a ×50 spread from the rate", value: "12.3 million / 5.85 billion pairs · wholesale $2.50 → $30.75 million · retail $130 → $1.6 billion", note: "the real agreed rate is $0,002–0,005/generation (music); the >$9 billion ceiling is theoretical, not awarded", key: true}
ne_resheno:
  title: "What the court didn't decide — and this list matters more than what it did"
  items:
    - "whether the training itself is lawful — not decided"
    - "what would happen if the training were provably shown to have taken place in the UK — not decided"
    - "whether the finding on the weights will survive appeal — unknown: permission was granted in January 2026 (the question was deemed novel and important), and there's no appellate ruling as of 27.10.2026"
    - "exactly how much human contribution is enough for authorship — not decided here, or in the neighboring jurisdiction"
media: ""
media_needed: "the main gates of the Royal Courts of Justice in London (assets/screenshots/s30-royal-courts.jpg, Wikimedia Commons, CC0) — acquired, but the slide has nowhere to put it alongside three plates and the \"what wasn't decided\" list"
timing_min: 1.8
in_bucket: true
status: собран
---

## Visible slide text

*Payment address: RIGHTS.*

**What the court didn't decide:** the lawfulness of training · where it physically took place · the outcome of the appeal.

**Inside the corpus — 12.3 million of the plaintiff's images out of ≈5.85 billion pairs.** Wholesale $2.50 → ≈$30.75 million; retail $130 → ≈$1.6 billion. A 50-fold spread comes from one choice of rate. The actually agreed rate is three to four orders of magnitude lower.

**Five statuses for a legal news item:** suit filed · ruling handed down · settlement with no admission of guilt · law in force · law passed, not yet in effect.

## Speaker notes

This is the only detailed legal case all evening, and its genre differs from the others — a
court ruling has neither the price of both errors in one unit, nor a classical mode, nor the
name of a product-maker. So this case follows its own form: what the court decided, what it
didn't decide, how this differs from the neighboring jurisdiction. The payment address here is
rights, and the previous slide led into it with a direct chain: the model doesn't construct the
object → so it doesn't copy → so all that's left is the trademark. The court's ruling is the
second pillar of that chain, not the first.

What was decided. The High Court of England and Wales, Mrs Justice Joanna Smith, November 4,
2025: the model's weights are mathematical parameters, and they aren't an infringing copy under
UK copyright law; secondary infringement wasn't proven. The plaintiff's narrow win came on
trademark: the generated images were found to contain artifacts of its watermarks. This detail
looks technical, but it's actually this slide's engineering conclusion: the win came through
exactly the channel where infringement is visible on the output, that is, exactly where an
external check of the result is even possible — exactly as the previous slide showed: provenance
doesn't exist inside the model, the check gets pushed outward.

The list of what the court didn't decide matters more than the list of what it did. Whether the
training itself is lawful — not decided. What would happen if the training were provably shown
to have taken place within British jurisdiction — not decided. Whether the finding on the
weights will survive appeal — unknown: permission was granted in January 2026, the question was
deemed novel and important, and the plaintiff's argument was found to have a real prospect of
success; there's no appellate ruling as of the end of October 2026. And separately: exactly how
much human contribution is enough for authorship — not decided here, or in the neighboring
jurisdiction.

Why the plaintiff lost, and why that's not what everyone thinks. During the June 2025 hearings,
the plaintiff itself dropped its main claims — on training and on the model's outputs: there
wasn't enough evidence that the training took place within British jurisdiction. The UK has no
fair-use doctrine in the American sense; it has narrow exceptions, and training a commercial
model doesn't fit any of them. The same dispute is lost in two jurisdictions in two different
ways: in the US — because training on lawfully acquired material is treated as transformative
use; in the UK — because the plaintiff didn't prove where it physically took place. The
formulation "a British court found model training lawful" is wrong, and it comes up constantly:
the court never considered the lawfulness of training, the claim was dropped by the plaintiff
itself. The difference between "the court decided this is lawful" and "the court declined to
consider this" is a practical one: you can build a project on the first statement, and you can't
on the second.

The economics stand right next to the ruling, and it's useful to count it through with the
room. Inside the training corpus there turned out to be 12.3 million of the plaintiff's images
out of ≈5.85 billion pairs — a share of around 0.2%, and that number on its own says little
until a rate is attached to it. At the wholesale rate of $2.50 per image — ≈$30.75 million. At the
retail rate of $130 — ≈$1.6 billion. A fiftyfold spread comes from nothing but the choice of rate
inside the classical mode — that is, no generation at all, one line of a price list; this is the
same observation the section opened with, returning here in a legal frame. The third figure is
the one the market actually settled on: in music, after the settlements, the agreed rate came to
$0,002–0,005 per generation, three to four orders of magnitude below the stock per-unit rate; a
direct comparison isn't valid — different modalities — but the order of magnitude says what the
market values one call to the model at, when it's paying voluntarily. The fourth figure is the
statutory ceiling: the per-work statutory rate gives over $9 billion; this is arithmetic, not an
awarded claim, and on meeting a sum like that in a headline, it's worth remembering what it was
derived from.

What an engineer takes away from this. First: a model's weights and its training set are
different objects of law — the court split them explicitly. Second: the place of training
matters, and for distributed infrastructure that's a question a project has to be able to answer
with documents — a logging requirement, not a legal-department one. Third: before repeating the
size of a claim, ask what rate it was calculated at and who chose that rate. Fourth: the narrow
win came through the channel where infringement is visible on the output — which means that if
your project carries a risk of reproducing someone else's protected work, the only mechanism of
control that actually works is external: reverse image search at release time, not tuning inside
the model. And last — what's entirely absent from this accounting: not one of the named figures
answers the question of how much a specific author, whose image landed in the corpus, actually
lost. A share of the corpus isn't a share of the contribution, and there's no measured way today
to count one example's contribution to a trained model; that's not a gap in this particular
case, it's a property of the subject matter.

Tell apart five statuses when you meet a legal news item: suit filed · ruling handed down ·
settlement with no admission of guilt · law in force · law passed, not yet in effect. "Law
passed" and "law in force" differ by four months for the EU and by seven months for Russia: the
Russian framework law was signed in July 2026 and has been in force since September, while the
provisions on training and labeling take effect March 1, 2027. The practical meaning of the
Russian provision — who was given permission to train: Article 10 introduces a statutory
exception for training under an opt-out model, but only for sovereign and national large
foundation models — for everyone else, there's no exception in the law at all, and the provision
is also contested, with amendments to it under discussion since October 2026. A "settlement"
doesn't set a precedent: $1.5 billion was paid in the American book case for storing a pirated
library, while the same judge called training on lawfully purchased books transformative
use — opposite-meaning halves of one event, and usually only the first gets quoted. "Ruling
handed down" and "ruling final" differ by whether there's an appeal: in the British case, the
appeal is permitted, no ruling exists yet; in the American authorship case, the point was settled
by a denial of rehearing on March 2, 2026 — but even there, exactly how much contribution is
enough for authorship wasn't decided. A pair of Russian cases teach the same lesson within a
single legal system: the court protected a deepfake (a neural network as an auxiliary processing
tool, 500,000 ₽), and didn't protect generated images ("entering prompts is technical labor, not
creative labor"); there's no contradiction, there was source material in the first case and none
in the second. There's one skill here: before building a project on a legal claim, ask which of
the five statuses it has — a cheap check that filters out most industry headlines.

Three lines of a jurisdiction overview that don't fit the Getty storyline, but answer that same
question of status. The EU: disclosure and machine-readable labeling of synthetic content are
mandatory, with a penalty of up to €15 million or 3% of turnover; the law has been in force
since August 2, 2026 (with a transition period for systems already on the market until December
2, 2026); the high-risk-system provisions were deferred separately, and this article wasn't.
Voice: Russia has no dedicated protection — a draft Civil Code article was introduced a month
after a lost case over voice use, and the government hasn't backed it; in the US there's a
Tennessee state law and a California act, and no federal law — a divergence between
jurisdictions, not a common standard. Music: the market here settled faster than the courts — the
labels moved from lawsuits to licenses at the same $0,002–0,005-per-generation rate, while some
plaintiffs keep litigating in parallel with signed deals (29.10.2025 and 25.11.2025).

Now, the section's conclusion. Where the benefit is: the image unit got cheaper by three to four
orders of magnitude from any of the three classical baselines, and this has a measured production
consequence — 46 unique posters a month with three people, with an hour and a half of
fine-tuning on one gaming GPU and a set of forty pictures. Where the boundaries are: five are
named by mechanism, not by symptom, and none of them will close with the next version of the
model. What moves further down the cycle: selection — 30–100 generations and half an hour of
review per usable one, two-thirds of the output a miss; rights — what the model was trained on is
known only for the open ones, and a legal provision's status has to be checked against five
levels of firmness; reproducibility — a solution found by trial and error isn't reproducible six
months later without an eleven-item manifest. And separately — the risk of attributing someone
else's win to the model, shown by the bionic partition case.
