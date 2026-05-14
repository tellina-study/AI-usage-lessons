# Tools — Lec-2 production observations

## Git infrastructure brittleness (BIG issue)

**Setup:** parallel sessions Лекция 2 (mine) + Лекция 4 (other Claude/agent) sharing single `.git` folder in `/home/levko/AI-usage-lessons`.

**Symptoms:**
- `git branch --show-current` returned `issue-73-lec-04-medicine-production` 7+ times mid-session (when I'd just been on issue-74).
- Lec-04 cherry-picks landed on issue-74 branch ref (commits `9529839`, `aa4567d`, `6d91e26` were lec-04 work но на issue-74 ref).
- 3 of 5 Phase 7 critics reported «slides/*.md / chapter.md / deck.yaml missing» — files existed on disk но в branch state they could see they weren't tracked.

**Recovery patterns that worked:**
1. `git update-ref refs/heads/issue-74-lec-02-llm-internals <my-real-commit>` — manually point branch ref to my work (без destructive `git reset --hard`)
2. `git worktree add --detach /tmp/lec02-wt <commit>` — separate working dir с own HEAD, immune to parallel session

**Recovery patterns that didn't work:**
- Agent `isolation: "worktree"` parameter — creates worktree from default base (probably main), NOT from current branch's HEAD. Phase 8 attempt в isolated worktree had no lec-02 files.
- Re-spawning agent after branch corruption — agent often saw stale view

**Action:** worktree isolation as DEFAULT для multi-lecture parallel production. Document в tools/lecture-production/README.md + CLAUDE.md.

## PowerPoint MCP vs python-pptx direct

**Phase 6 builder agent chose python-pptx direct over PowerPoint MCP** для full-deck builds. Reasons stated:
- Avoid MCP `update_shape_position` limitation
- Avoid MCP 4:3 default ratio issue
- Faster batch operations at 28-36 slide scale
- Bypass JSON serialization-deserialization overhead

This pattern (python-pptx direct + libreoffice convert + pdftoppm snapshots) worked reliably через Phase 6-8.9. Should be canonical approach for full-deck builds; MCP for quick spike / individual slide tweaks.

**Update note `mcp-limitations.md`:** add explicit recommendation «for full-deck builds (>20 slides + multiple visual elements) → python-pptx direct; reserve MCP for incremental edits».

## tiktoken availability

**Used tiktoken to empirically verify strawberry split** during Phase 3 P0 fix. `python3 -m pip install --quiet --break-system-packages tiktoken` worked.

This validated:
- `strawberry` in `o200k_base` (GPT-4o) → `['st', 'raw', 'berry']` = 3 tokens
- `strawberry` in `cl100k_base` (GPT-4) → `['str', 'aw', 'berry']` = 3 tokens

Fact-checker should use tiktoken for token-related verification вместо relying on documentation.

## QuickChart + rsvg-convert + libreoffice

Render toolchain worked reliably:
- QuickChart API for bar charts / distributions / U-shape graphs
- mermaid CLI was blocked (Chrome missing on WSL) — used rsvg-convert for custom SVG instead
- libreoffice headless для PPTX→PDF
- pdftoppm 130dpi для PNG snapshots

**No new limitations encountered** beyond previously documented (см. notes/mcp-limitations.md).

## Worktree branch sync — FF via update-ref

**Worktree commits propagate to main `.git` automatically** (shared git database). After each phase commit in `/tmp/lec02-wt` (on detached HEAD branch `phase-8-revision-v11`) → `git update-ref refs/heads/issue-74-lec-02-llm-internals <new-commit-sha>` from main repo updated issue-74 ref без needing main worktree checkout.

This pattern allowed me to keep accumulating commits на issue-74 без disturbing parallel lec-04 work.

---

## Action

→ improvements.md P0-5 (worktree policy), P2-1 (lecture-prod-status skill).
