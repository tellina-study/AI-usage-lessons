# Issue Triage Rules

## Labels

- `normative` — change in normative/regulatory documents
- `lecture` — affects lecture content
- `slides` — affects slide decks
- `diagram` — affects diagrams
- `infrastructure` — repo/tooling/MCP setup
- `blocked` — waiting on external input

## Priority

1. **Critical** — normative change that cascades to multiple lectures
2. **High** — single lecture or deck needs update before next session
3. **Normal** — improvement or addition, no deadline
4. **Low** — nice-to-have, backlog

## Triage Flow

1. New issue arrives (auto-created or manual)
2. `issue-manager` assigns labels based on affected entities
3. Run `impact-check` to determine cascade scope
4. Set priority based on scope and upcoming deadlines
