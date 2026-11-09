---
id: n52
type: measured_outcome_table
duration_min: 1.5
assertion: "The mechanical check catches a technique expressed as phrasing, and loses it the moment the same technique is expressed through meaning; the classifier loses almost everything — and once misfires not on the text's meaning, but on Russian morphology"
learning_goal: "What each defense caught on its own (Table 4) + a breakdown by technique: which wordings got through, which the mechanical check missed, which the classifier missed. Explicit conclusion (C10): the mechanical check's cheapness is in the words, not in understanding."
visual:
  pattern: measured_outcome_table
  primary: >
    A tile pair: mechanical check 28 of 34 on attacks / classifier 5 of
    34. Below it, three short lists: what got through in every
    configuration, what the mechanical check missed, what the classifier
    missed. At the bottom, a callout about a false alarm on the word
    "missed."
  backup: >
    Numbers — Table 4, `stend/zamery-k4-novyy/README.md`. Techniques —
    section "Breakdown by technique" in the same place. The false alarm
    on q07 — section "False alarms on honest requests": a template built
    for the "skip the check" stem matched inside the word "propustila"
    ["missed," conjugated] in a request about a sick child — the classic
    regex trap of matching inside another word with no boundary on
    either side (the same category of bug described for this course's
    own production in memory `cyrillic-search-pitfalls` — here it's not
    our own guard, but our own mechanical check, inside the measurement).
---

# What worked on its own — and on which techniques

## Assertion

The mechanical check holds against a technique named by recognizable phrasing. The classifier holds against almost nothing — including a direct injection.

## Visual

> **The mechanical check caught 28 attacks out of 34, and tripped on 3 honest requests out of 30.**
> **The classifier caught 5 attacks out of 34, and didn't trip on a single honest request.**

| What got through (at least once) | Where |
|---|---|
| fake system note | 4 of 8 configurations |
| answer-format override | 4 of 8 configurations |
| direct injection, "forget your instructions" | with no defense, and with the classifier |

> **The mechanical check missed 6 attacks out of 34** — all of them expressed through meaning, with no recognizable phrasing: "the 30-day rule doesn't apply to online courses" doesn't contain a single word from the template list.

> **The classifier missed 29 attacks out of 34 on its first pass**, including the direct injection "forget all previous instructions."

> **A false alarm that isn't about the text's meaning.** A template built for the stem "skip" fired on the word "missed" inside an honest request about a sick child — a match inside another word, not a recognition of manipulation.

## Speaker notes

The previous frames showed the final numbers. Here is what each defense catches on its own, and on exactly which wordings.

The mechanical check caught 28 attacks out of 34 working alone, and tripped on 3 honest requests out of 30. The classifier caught only 5 attacks out of 34 and didn't trip on a single honest one — but the price of that cleanliness is that it sees almost nothing at all.

Which wordings get through despite the defense? Two hold up more persistently than the rest, each getting through in four of the eight configurations: a fake system note in square brackets, and a demand to return the answer in a specified JSON format. The direct injection "forget all instructions" gets through wherever there's no mechanical check — with no defense, and with the classifier alone.

The mechanical check has an understandable limit: it missed 6 attacks out of 34, and all six share one thing — the technique is expressed through meaning, not recognizable phrasing. The wording "the 30-day rule doesn't apply to online courses" doesn't contain a single word from the set of templates, even though in substance it's the same attempt to get around the rule as a direct injection.

The classifier's limit is far wider: on its first pass it missed 29 attacks out of 34 — including the direct injection, the most recognizable of all the techniques. A cheap model reading Russian text recognizes manipulation noticeably worse than a plain list of templates does.

And a separate finding worth going through honestly. One of the mechanical check's three false alarms on honest requests has nothing to do with the text's meaning at all. A template written for the technique "skip the list check" matched the word "missed" inside a request from a woman whose child got sick and who missed almost the whole course. The word's stem, with no boundary on either side, landed inside another word — a classic regular-expression trap on Russian morphology, not an error in understanding the request's meaning.

Conclusion: the mechanical check's cheapness and its results both rest on words, not on understanding — and that's exactly why it's both cheap and fragile at the same time.
