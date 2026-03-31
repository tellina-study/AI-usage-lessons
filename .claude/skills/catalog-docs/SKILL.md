# catalog-docs

Catalog exported documents into structured manifests.

## Steps
1. Scan `catalog/exports/` for new/modified files
2. Extract metadata (title, type, date, owner)
3. Update appropriate manifest in `catalog/manifests/`
4. Create RDF triples for new entities in Oxigraph
5. Report cataloged items
