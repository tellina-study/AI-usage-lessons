---
id: s09
type: comparison
section: "Section 1. Tokenization"
duration_min: 2.5
assertion: "The tokenizer cuts by frequency, not by structure: numbers are chunked in groups of 3 digits, code by whole indentation levels"
learning_goal: "Numbers and code as the second/third case where the cut diverges from structure; compact-comparison format (not a case study, to avoid duplicating s08)"
learning_outcomes: [LO6]
chapter_ref: "§1.5 [for-slide-s09]"
visual_brief: "Motivation line under the title: numbers and code are the most common 'non-text' inputs; the model's arithmetic and the token budget both depend on how they're cut. 'Numbers' column: 1000000 → [100][000][0] — chunks left-to-right ≠ place values; right-to-left cutting improves arithmetic, task-specific schemes up to +33% (gold). 'Code' column: GPT-2 — 16 tokens for a level-4 indentation; GPT-4 — whitespace in groups (the vocabulary gets fixed — but not for every task at once). Bottom — 'What to do' block: digit separators, offload computation to a tool, consistent indentation, + a line about auto-routing in off-the-shelf chat products."
---

# Visible content

## Title bar
"The tokenizer cuts by frequency, not by structure"

## Body
[Motivation line under the title]
Numbers and code are the most common "non-text" inputs: the model's arithmetic and your token budget both depend on how they're cut.

[2 columns in Ocean rounded boxes]

**Numbers**
`1000000` → `[100][000][0]`
Chunks of 3 digits left-to-right ≠ place values.
Right-to-left cutting improves arithmetic; task-specific schemes give **up to +33% accuracy** over standard cutting (gold).

**Code**
GPT-2: **16 tokens** for a level-4 indentation.
GPT-4: groups whitespace — the vocabulary gets fixed, but not for every task at once.

[Bottom — 4 tips in one line, with a group heading]
**What to do:**
**Digit separators** ("1,234,567") · **offload computation to a tool** · **consistent indentation** · **in off-the-shelf chat products, counting already routes to a code interpreter automatically — you only need to call a tool yourself in non-standard cases and in your own apps built on the API**

## Speaker notes

Why should an engineer care how numbers and code get cut: these are the most common "non-text" inputs, and how they're cut directly affects the model's arithmetic and your token budget for code. Two compact examples of how frequency-based cutting diverges from data structure.

Numbers. The cl100k_base tokenizer standardized cutting numbers into chunks of three digits left-to-right: a million turns into groups whose boundaries don't line up with place values. Humans read place values right-to-left — thousands, millions; the model gets irregular blocks — and that's a direct source of some arithmetic errors. Research confirms the diagnosis from both sides: forcing right-to-left cutting noticeably improves numerical reasoning, and task-specific number-tokenization schemes gave up to thirty-three percent more accuracy on large-number arithmetic relative to standard cutting.

Code. GPT-2 encoded every indentation space as a separate token: a line at the fourth nesting level spent sixteen tokens just on indentation. GPT-4-generation tokenizers group whitespace into single tokens, specifically targeting Python style. This is a rare case where a tokenization problem got fixed by changing the vocabulary — a useful contrast to strawberry: you can optimize the vocabulary for a frequent input class, but you can't align cutting with the structure of every task at once.

Four takeaways. Write significant numbers with digit separators — "1,234,567" instead of an unbroken string: separators align token boundaries with place values. Offload any arithmetic beyond a rough estimate to a tool — models write excellent code for calculations they can't do themselves. For code — use consistent formatting, and estimate your budget by measuring on real files: the common "four characters per token" rule of thumb is systematically wrong for code. And an important caveat for practice: in off-the-shelf chat products — ChatGPT, Claude's web interface — counting and arithmetic already route automatically to a built-in tool like a code interpreter, bypassing the model's direct forward pass; what we just covered becomes critical specifically when you call the model directly through the API — in your own apps and agents, where there's no automatic routing like that, and in non-standard cases that the off-the-shelf product didn't recognize as "needs a tool."
