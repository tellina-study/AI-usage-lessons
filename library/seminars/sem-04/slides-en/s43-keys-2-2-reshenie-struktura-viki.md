---
id: s43
type: code_artifact
duration_min: 1.5
assertion: "The ADR practice: one decision — one numbered file, and the link between decisions is a line in the Status section that the tool writes in both directions at once"
learning_goal: "The solution for case 2.2: not an invented structure but a documented practice of architecture decision records (ADR, Nygard 2011; the adr-tools tooling) applied to signup-landing — with an honest note on the strength of evidence"
visual:
  pattern: code_structure_illustrative
  primary: "On the left — the doc/adr/ directory with numbered decision files and a generated README.md table of contents; under the listing, a gold line saying that record 0031 came over from case 2.1 rather than being set up a second time. On the right — the November record in full, following the adr-tools template: a heading with the number, the date, a Status section with the Amends link line, then Context / Decision / Consequences. At the bottom — the adr new command with the link flag and a line saying that the tool wrote the back-link into the September record. Caption: the source of the practice and an honest strength of evidence."
  backup: "The content of the records is illustrative — the 0031/0187 numbers and the matching Amends / Amended by pair. A capture of the demo repository does exist (the doc/adr/ directory, commit 3b4b289), but not of this scene: it holds three records, there are no cross-links between them, and adr-tools is not installed there — the table of contents was written by hand. The structure, section names, link format and behavior of the command follow the adr-tools template and sources — they are not invented."
---

# One decision — one file, and the tool writes the link

## Assertion

The ADR practice ("Architecture Decision Record"): one decision — one numbered file, and the link between decisions is a line in the `Status` section that the tool writes in both directions at once.

## Visual

On the left — the decisions directory:

```
doc/adr/
  0001-record-architecture-decisions.md
  ...
  0031-storonnie-vidzhety-ne-dobavlyaem.md
  ...
  0187-antispam-honeypot-bez-kapchi.md
  README.md   ← the table of contents, printed by `adr generate toc`

  0031 — the same record as in case 2.1:
  it moved here out of DECISIONS.md
```

On the right — the November record in full, following the template:

```markdown
# 187. Anti-spam — a honeypot field, no captcha

Date: 2026-11-28

## Status

Accepted

Amends [31. No third-party widgets in the form]
       (0031-storonnie-vidzhety-ne-dobavlyaem.md)

## Context
The form started getting spam. A captcha is a third-party widget,
banned by decision 31, and it drops the form's conversion.

## Decision
A hidden honeypot field. We still add no third-party widgets.

## Consequences
No third parties in the form, conversion does not suffer.
It cuts off primitive bots; targeted spam, no.
```

A band at the bottom, in a gold frame:

> `adr new -l "31:Amends:Amended by" …` — and a matching line appeared in file 31: `Amended by [187. Anti-spam — a honeypot field, no captcha](0187-antispam-honeypot-bez-kapchi.md)`. Both links were written by the tool, not by the author of the record.

Source caption: "The Architecture Decision Record practice — Michael Nygard, 2011; the template, the sections and the commands — `adr-tools`. Thoughtworks Technology Radar: the Adopt ring since 2016. Strength of evidence: a documented and widely used practice **for humans**; there is no controlled measurement that 'ADRs help a coding agent'. The content of the records is illustrative."

## Speaker notes

"We did not invent the structure here — we took a ready-made one. Architecture decision records, ADRs, were described by Michael Nygard in 2011, and the practice has a reference set of commands — `adr-tools`. The arrangement is exactly what you see on the slide.

One decision — one file: a four-digit sequential number plus a hyphenated title. Inside — a heading with the number, the date and four sections: `Status`, `Context` (what forced the decision), `Decision` (what was decided), `Consequences` (what gets easier and what gets harder).

The key part for our case is the `Status` section: besides the status, it holds links to other decisions. The November record carries `Amends` — it amends the earlier one — and a link to the September record; in the September record the tool added the matching `Amended by` line. And that is exactly what the flat log did not have: an agent that opens the September decision no longer has to read the file to the end — the link to the November amendment sits right there in it.

The key words are 'the tool added': the link in both directions is placed by a command, not by the author's discipline. The `-s` flag means 'supersedes' and moves the old record from `Accepted` to 'superseded by such-and-such record'; the `-l` flag simply links, leaving the status alone. Ours is the second case — the November decision does not cancel the September one, it amends it for one question. The table of contents is not hand-written either: `adr generate toc` prints the list of all records with links, and that goes into `README.md`.

Honestly about the strength of evidence: this is a practice for humans. It has been documented since 2011 and is widely used — a 2026 study collected more than four and a half thousand ADRs from seven hundred and fifty projects out of open repositories. But there is not a single controlled measurement that 'ADRs help a coding agent'. The content of our two records is illustrative. A snapshot of the demo repository does exist — the `doc/adr/` directory, commit `3b4b289` — but it shows a different scene: it holds three records, there is no `Amends` / `Amended by` pair between them, and `adr-tools` was never installed there, so the table of contents was written by hand. The structure, the sections and the format of the link line come from the `adr-tools` template and sources — they are not invented."
