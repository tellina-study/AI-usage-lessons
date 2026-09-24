---
id: s05
type: case_study
assertion: "A 4.2 GB archive — and the formats came apart"
learning_goal: "Fact-only intro, no conclusions — just a new detail and a question, doesn't hint at the direction of the answer"
learning_outcomes: [LO1]
references: []
visual:
  pattern: scattered_formats_cards_plus_question
---

# Supplier documents

## Assertion

"A 4.2 GB archive — and the formats came apart"

## Visual

Four sample-invoice cards in different formats: (1) a plain table like in the
setup, (2) a table with differently named fields and a different column order,
(3) a scan-like document with fields scattered through free text, (4) a document
entirely in English. On the right — a question: "Does this change your answer?"

## Visual — quote

"Team, I pulled the archive like you asked, a 4.2 GB ZIP. Inside it's a mix:
scanned reconciliation acts, contracts, and the invoices themselves — I didn't
sort anything, just zipped up the folder as it's sat for the past year. Two of
our biggest suppliers are actually connected through EDI and send invoices
already as structured XML files, no parsing needed there. The rest are scans
from the old scanners at the warehouse, they output 200dpi and are already
compressed. By the way, accounting is separately moving to EDI with the tax
authority for invoicing documents, but that's a different project, not about
supplier invoices."

## Speaker notes

Read the accountant's quote. A direct signal, not flagged by intonation:
inside the archive it's a mix of scanned reconciliation acts, contracts, and the
invoices themselves, nothing was pre-sorted. Indirect signals worth calling out
explicitly: part of the flow (the two biggest suppliers, via EDI) already
arrives as structured XML — that chunk doesn't need LLM extraction at all; and
the scan quality (200dpi from old scanners) is a hard lower bound on OCR
accuracy if the solution goes through image recognition. Accounting's move to
EDI with the tax authority is a decoy fact: it sounds related, but it's a
separate process about tax invoicing, unrelated to parsing supplier invoices.
The slide shows several sample invoices from the archive — the formats are no
longer as uniform as the first two documents: one looks like a plain table, in
the second the fields are named and arranged differently, the third has free
text instead of a clear table, and the fourth is in English because one of the
suppliers is foreign. This is the same archive, just now we're seeing all of it.
Ask the room: does this change your answer? And if you argued for a clean
parser with no AI — what do you think now, seeing this spread of formats? And
what about the share of the flow that comes through EDI and doesn't need
parsing at all? During the debrief, ask: which facts from the quote actually
shaped your choice, and which didn't?
