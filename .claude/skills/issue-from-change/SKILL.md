# issue-from-change

Create a GitHub Issue when a document change is detected.

## Steps
1. Receive change details (source, type, affected entities)
2. Run impact assessment via Oxigraph queries
3. Fill `templates/issue-change-template.md`
4. Create GitHub Issue via github-mcp-server
5. Apply labels per `workflows/issue-triage.md`
6. Add to project board
