---
id: n49
type: measured_outcome_table
duration_min: 0.75
assertion: "The hybrid does NOT win in a SINGLE one of the three question groups on its own — its aggregate result comes from nowhere being the worst"
learning_goal: "Case 3's summary beat, continuing n48: a breakdown of recall@1 by the same three groups the previous beat (n46) named — the same verbatim group structure. The systematic finding (C4): the hybrid doesn't win in ANY single group by recall@1. Part 2 of 2. Letter-suffix inserted before deck-wide renumbering (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: measured_outcome_table
  primary: >
    A 3×3 table (group · recall@1 for three methods, with the group's
    winner highlighted) · a systematic-finding tile (C4).
  backup: >
    The breakdown by group — recomputed from stend/raw/case3-results.json
    `details` by `lexical_class` from stend/corpus/case3_questions.json
    (a field on each question), tallied across three classes × three
    methods × recall@1: lexical_gap keyword 4/16=0.25 vector 15/16=0.94
    hybrid 11/16=0.69; exact_match keyword 16/16=1.00 vector 13/16=0.81
    hybrid 15/16=0.94; neutral keyword 17/18=0.94 vector 15/18=0.83 hybrid
    16/18=0.89. These numbers are NOT printed in either SETKA-KEYSOV.md or
    `raw/case3-results.json::summary` (only the aggregate is there) —
    recomputed by this edit with a direct pass over the `details` of the
    same file, the same methodology as measure/case3_measure.py, with no
    new measurement run.
---

# Recall@1 by the three question groups

## Assertion

The aggregate hides a finding: in each of the three question groups, the hybrid has a stronger specialist.

## Visual

**A summary across the same three groups the previous beat named (recall@1):**

| Question group | words | meaning | hybrid |
|---|---|---|---|
| Lexical gap (16) | 0.25 | **0.94** | 0.69 |
| Exact match (16) | **1.00** | 0.81 | 0.94 |
| Neutral (18) | **0.94** | 0.83 | 0.89 |

> **A systematic finding: the hybrid does NOT win in a SINGLE one of the three groups on its own.** Its aggregate result (0.84) comes not from being the best anywhere, but from nowhere being the worst.

## Speaker notes

The aggregate from the previous frame hides something important, visible only in the breakdown across the same three groups the test-structure beat named. Let's recompute recall@1 separately for lexical-gap questions, exact-match questions, and neutral ones.

On the lexical gap, semantic search is almost flawless — ninety-four percent, and the merge is noticeably weaker — only sixty-nine. On exact match, words win with a score of one hundred percent, and once again the merge trails — ninety-four. On neutral questions, words lead again — ninety-four against eighty-nine for the merge.

The systematic finding: the hybrid doesn't win in any of the three groups on its own. Its aggregate result — eighty-four percent — comes not from being the best somewhere, but from nowhere being the worst: in each group there's a specialist that performs better, and the hybrid pays away part of that specialist's advantage for stability across a stream of questions of unknown composition ahead of time. This is exactly the price of averaging: a win on the mixed stream at the cost of losing inside each separate question class, where a stronger specialist already exists.

A practical conclusion for Olga's training center: if it's known ahead of time that requesters mostly ask one type of question — say, almost always retelling things in their own words — a specialized method may turn out more profitable than the hybrid, despite the hybrid looking more attractive in the averaged table. The choice of method is tied to the specific stream of questions — there is no general "what's best overall" ranking here.

This is the same lesson that already came up in the first case of this session, about keyword's recall@1 not changing as the base grew: an average aggregate figure is a convenient number for comparison, but it systematically hides a method's behavior on individual classes of input — and that is exactly where the decisions that actually change practice are hiding.

Next — a breakdown of what each of the three signals does and why.
