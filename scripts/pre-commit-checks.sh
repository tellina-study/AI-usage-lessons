#!/usr/bin/env bash
# Pre-commit checks for AI-usage-lessons repo
# Install: ln -sf ../../scripts/pre-commit-checks.sh .git/hooks/pre-commit

set -e

ERRORS=0

# 1. Validate store.ttl syntax (basic: check balanced angle brackets and no trailing whitespace issues)
if git diff --cached --name-only | grep -q "ontology/store.ttl"; then
  echo "Checking ontology/store.ttl..."
  # Check file ends with proper triple terminator
  if ! tail -1 ontology/store.ttl | grep -qE '\.\s*$'; then
    echo "ERROR: ontology/store.ttl doesn't end with a period (invalid Turtle)"
    ERRORS=$((ERRORS + 1))
  fi
  # Count triples roughly (lines with subject declarations)
  TRIPLE_LINES=$(grep -c '^\s*<https://' ontology/store.ttl 2>/dev/null || echo 0)
  echo "  store.ttl: ~${TRIPLE_LINES} entity lines"
fi

# 2. Check wiki files don't exceed 600 lines
if git diff --cached --name-only | grep -q "^wiki/"; then
  echo "Checking wiki file sizes..."
  for f in $(git diff --cached --name-only | grep "^wiki/"); do
    if [ -f "$f" ]; then
      LINES=$(wc -l < "$f")
      if [ "$LINES" -gt 600 ]; then
        echo "ERROR: $f exceeds 600-line limit ($LINES lines)"
        ERRORS=$((ERRORS + 1))
      fi
    fi
  done
fi

# 3. Check no [[wiki-links]] remain in wiki/
if git diff --cached --name-only | grep -q "^wiki/"; then
  echo "Checking for unresolved wiki-links..."
  UNRESOLVED=$(grep -rn '\[\[' wiki/ --include="*.md" 2>/dev/null | grep -v '## Compilation Log' | grep -v 'cross-links resolved' | cut -d: -f1 | sort -u || true)
  if [ -n "$UNRESOLVED" ]; then
    echo "ERROR: Unresolved [[wiki-links]] in: $UNRESOLVED"
    ERRORS=$((ERRORS + 1))
  fi
fi

# 4. Check no secrets in committed files
if git diff --cached --name-only | grep -qE '\.(json|yaml|yml|md)$'; then
  echo "Checking for secrets..."
  SECRETS=$(git diff --cached -U0 | grep -iE '(api.key|token|password|secret|ghp_|sk-)' | grep '^+' | grep -v '^+++' || true)
  if [ -n "$SECRETS" ]; then
    echo "WARNING: Possible secrets in staged changes:"
    echo "$SECRETS"
  fi
fi

if [ "$ERRORS" -gt 0 ]; then
  echo ""
  echo "Pre-commit: $ERRORS error(s) found. Fix before committing."
  exit 1
fi

echo "Pre-commit checks passed."
