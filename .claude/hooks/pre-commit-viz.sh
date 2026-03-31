#!/bin/bash
# Pre-commit hook: regenerate ontology visualizations
# Runs both viz scripts if their source data or scripts changed

REPO_ROOT="$(git rev-parse --show-toplevel)"

# Check if any ontology or viz script files are staged
CHANGED=$(git diff --cached --name-only | grep -E '(scripts/viz-ontology|ontology/data/|ontology/schema)')

if [ -n "$CHANGED" ]; then
    echo "🔄 Regenerating ontology visualizations..."

    cd "$REPO_ROOT"

    python3 scripts/viz-ontology.py 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "  ✓ ontology-graph.html"
    else
        echo "  ✗ graph generation failed (pyvis not installed?)"
    fi

    python3 scripts/viz-ontology-table.py 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "  ✓ ontology-table.html"
    else
        echo "  ✗ table generation failed"
    fi
fi
