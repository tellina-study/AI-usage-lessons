---
id: n48
type: answer_breakdown_table
duration_min: 2.0
assertion: "Cards 1 and 2 close the mechanical requirement with code; card 3 closes the semantic one, and there's no step for it in the chain today; card 4 closes neither — and that's exactly what happened in the scene"
learning_goal: "Breakdown of question n47, repurposed by the owner's 2026-10-20 edit (issue #274): the two requirement classes are now named in the n46 footer, so this screen no longer introduces them — it resolves the four cards against the already-named requirements and bridges to how the first two points get implemented technically (n49 layer 1, n50 layer 2)."
visual:
  pattern: answer_breakdown_table
  primary: >
    A four-row table: card · which requirement it closes · closed today or
    not. Below it a paragraph-example about a technically sound file with
    the wrong content, and a short bridge to the next two screens.
  backup: >
    Before the owner's 2026-10-20 edit (issue #274), this slide itself
    introduced the two requirement classes with a "class · example · who
    checks" table — that table was moved into the statement's footer
    (`n46-k4-stsena.md`), at the owner's direct request ("move the
    requirement class into the statement"). The slide wasn't deleted (it
    didn't become redundant): question n47 still needs a breakdown
    immediately after itself (canon §3 A1), and a card-by-card breakdown
    is content that n46's footer doesn't have and shouldn't have (the
    statement's footer formulates the REQUIREMENT, it doesn't resolve
    the vote). The card wording and the hosting-error-page example are
    the same as they were here before, word for word from
    SETKA-KEYSOV-S8-part2.md, section "Card in Telegram," with no added
    detail.
---

# Which check closes which requirement

## Assertion

Four cards — not four equal answers. Two of them close the same requirement, one closes the other, and there's no tool for it in the chain today, and the last one closes nothing.

## Visual

| Card | Which requirement it closes | Closed today? |
|---|---|---|
| check the file's size and format before sending | mechanical | yes — in code, deterministically, before sending |
| check that the picture opens without errors | mechanical (same class) | yes — the same way |
| check that the picture actually shows what's needed | semantic / content-based | no — there's no step in the chain today that can do this |
| don't check anything | neither | no — this is exactly what happened in the case scene |

> A technically sound file (right size, right format) can still show the wrong thing — for example if the node fetching the picture got a hosting error page instead of the actual picture: the format and size would pass the mechanical check, and the content would be wrong.

Next — how the first two points get implemented technically: a tool-agnostic architecture, then the actual configuration in n8n.

## Speaker notes

The question's four cards aren't four equal answers — they're a breakdown against the two requirements we just named in the scene: mechanical and semantic.

The first and second cards — check size and format, check that the file opens without errors — both close the mechanical requirement: a file has numeric, enumerable properties, and a program can compare them against a condition just as deterministically as the IF node in "Refund approval" compared an amount against a threshold. This is code, and only code: a model isn't needed here and adds nothing.

The third card — check that the picture actually shows what's needed — closes the semantic requirement, and here the honest answer is different: there's no such step in our chain today. The only tool that's even capable of judging what's in the picture is a vision model, and that level isn't covered at all today.

The fourth card — don't check anything — closes neither requirement, and that's exactly what happened in the case scene: the run is green, the sending node got a positive response, and the result didn't match what the recipient expected.

A separate example, for why these two requirements can't be substituted for each other. A technically sound file — right size, right format — can still show the wrong thing: for instance, if the node fetching the picture by its link got a hosting error page instead of the actual picture. The error page's format and size could easily pass the mechanical check, while the content is nothing like what was required. This is the same lesson we already saw in "Notifications" and in Zillow, carried over to a picture: a mechanical requirement on a file is a job for code; a requirement on content is a job that needs a model, not the absence of a job at all.

The table's first row and second row are one and the same class, closed today. The third row is a class that's named but not closed: next we'll look at what an architecture that at least accounts for it looks like, and then an honestly assembled chain where it isn't there yet.
