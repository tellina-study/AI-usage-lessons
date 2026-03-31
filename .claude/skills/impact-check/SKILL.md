# impact-check

Analyze impact of recent changes across the knowledge base.

## Steps
1. Query Oxigraph for recently updated entities
2. Trace dependency chains (depends_on, cites, covers, illustrates)
3. Identify cascade: which lectures, decks, diagrams are affected
4. Run orphan checks (unlinked diagrams, unreferenced requirements)
5. Generate impact report
6. Create/update GitHub Issues for unresolved impacts
