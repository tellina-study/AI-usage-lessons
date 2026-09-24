---
id: s14b
type: schema_matrix
section: "Section 2. Architecture — before code, and it must be managed"
duration_min: 3
assertion: "Each of the four architecture-management practices has a concrete artifact in the repository and a concrete build step that goes red when it is violated: an ADR record, a test invariant, a textual C4 model, and a gate that holds the previous three together"
learning_goal: "Ground the abstract matrix of the four practices (s15) in real files: the student should see what an ADR, a fitness function, a C4 DSL and an architectural gate look like in code"
learning_outcomes: [LO1, LO7]
chapter_ref: "§2.2–§2.5 [for-slide-s13], [for-slide-s14], [for-slide-s15]"
references: [nygard-adr, ford-fitness-functions, brown-c4, evolutionary-architectures]
verify_day_of: false
visual_brief: >
  schema_matrix, 4 columns — the same icons and colors as on the previous slide (gavel/MID, shield-check/TEAL,
  layout-grid/MID, refresh-cw/TEAL), so the link reads instantly. Each column: a colored header plate →
  the file path in small monospace → a white box with the artifact snippet in monospace →
  a caption card "what is human here / what breaks on violation". Gold callout below — the criterion
  "you can tell a practice by its artifact". The same code-snippet style as on the requirements-visualization
  slide (white box, SOFT_GREY outline, monospace text).
interaction: none
---

# Visible content

## Title bar
Every practice is a concrete file in the repository

The same four practices as on the previous slide — not as a description, but as the artifact that sits in the repository and is checked by the build.

## Body

[Column 1 — ADR] `docs/adr/0007-event-queue.md`

```
# ADR-0007. Queue instead of
# direct warehouse calls
Status: accepted · 2026-03-12
Context: on warehouse outage
  orders are lost silently
Decision: orders go through
  an event queue
Consequences: + we survive
  a warehouse outage;
  − confirmation 2 s
  instead of instant
```

The human chose and signed the fork — AI could write the text. The record is immutable: an outdated one is replaced, not edited.

[Column 2 — Fitness function] `tests/architecture/test_layers.py`

```
# invariant 1: module bounds
def test_payment_not_ui():
    assert not depends_on(
        "payment", "ui")

# invariant 2: 200 ms budget
def test_checkout_p95():
    assert p95("/checkout") < 200
```

Which invariant is critical is the human's call — it is their definition of 'good'. Violated on a commit — the build goes red.

[Column 3 — C4 / arch-as-code] `docs/architecture/workspace.dsl`

```
workspace {
 model {
  eng = person "Engineer"
  app = softwareSystem "Booking" {
    api = container "API"
    db  = container "Bookings DB"
  }
  eng -> api "books a room"
 }
}
```

Text, not a picture: it is diffed and reviewed in the same merge request as the code; checking the model against the code catches drift.

[Column 4 — Evolutionary arch.] `.github/workflows/architecture.yml`

```
# gate: three practices together
- adr-lint docs/adr/
  # no fork without a record
- pytest tests/architecture
  # invariants hold
- structurizr-cli drift
  # model and code agree
# a red step blocks
# merging the change
```

It has no artifact of its own — it has the gate that holds the previous three together on every change. The human sets the direction.

[Gold callout]
You can tell a practice by its artifact: if you cannot show a file in the repository and a red build step when it is violated, it is not yet a practice, only an intention.

## Speaker notes

The previous slide listed the four practices in words; here they are as files that actually sit in the repository. That is the strength test: a practice for which you cannot open a concrete file and point at a build step that goes red when it is violated remains an intention.

An ADR is a short, half-a-page record for one architectural fork: the context (what problem we are solving, what forces are at play), the decision in the affirmative, the status, and the consequences, including the negative ones [1]. Nygard insisted precisely on the lightness of the format: large documents are never kept current, small modular ones at least have a chance. The record is immutable — an outdated decision is not rewritten but marked as superseded by a new record. For an agent that has no memory between runs, the ADR turns out to be the one place where the "why" is stored: the code shows what changed, the version history shows when and by whom, and nothing else holds the rationale.

A fitness function translates that "why" into a machine check on every commit: the direction of dependencies between modules, the latency budget of a critical path, contract coverage [2]. Its value is exactly equal to the value of the invariant the human put into it — a trivial always-green gate gives only the appearance of oversight.

Architecture-as-code is the same logic applied to the model of the system itself: a textual description language that is versioned and diffed next to the code, so AI reads and generates it equally well, and checking the described model against the actual code catches drift before the merge [3].

The fourth column is not a separate artifact but an assembly of the previous three: an evolutionary architecture is made up of incremental change, explicit fitness functions and a designed ability to change the system [4]. In the repository that looks like a single pipeline running the three checks together.
