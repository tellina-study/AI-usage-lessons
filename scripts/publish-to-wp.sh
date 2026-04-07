#!/usr/bin/env bash
# publish-to-wp.sh — Publish a bilingual blog article to tellian.io
# via WordPress.com REST API v1.1
# Usage: ./scripts/publish-to-wp.sh <slug> [--publish]
# Requires: pandoc, curl, WP_TOKEN env var (or .env file)
# Issue: #39

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="tellian.io"
API_BASE="https://public-api.wordpress.com/rest/v1.1/sites/${SITE}"

# --- Load token ---
if [ -z "${WP_TOKEN:-}" ]; then
  if [ -f "$REPO_ROOT/.env" ]; then
    # shellcheck source=/dev/null
    source "$REPO_ROOT/.env"
  fi
fi

if [ -z "${WP_TOKEN:-}" ]; then
  echo "ERROR: WP_TOKEN not set. Export it or add to .env file." >&2
  echo "  Get a token: https://developer.wordpress.com/docs/api/getting-started/" >&2
  exit 1
fi

# --- Parse args ---
if [ $# -lt 1 ]; then
  echo "Usage: $0 <slug> [--publish]" >&2
  echo "  slug      — folder name under publications drafts directory" >&2
  echo "  --publish — set status to 'publish' (default: 'draft')" >&2
  exit 1
fi

SLUG="$1"
STATUS="draft"
if [ "${2:-}" = "--publish" ]; then
  STATUS="publish"
fi

# Try multiple possible draft locations
DRAFT_DIR=""
for candidate in \
  "$REPO_ROOT/publications/blog/drafts/$SLUG" \
  "$REPO_ROOT/publications/drafts/$SLUG" \
  "$REPO_ROOT/blog/drafts/$SLUG"; do
  if [ -d "$candidate" ]; then
    DRAFT_DIR="$candidate"
    break
  fi
done

if [ -z "$DRAFT_DIR" ]; then
  echo "ERROR: Draft directory not found for slug: $SLUG" >&2
  echo "  Looked in: publications/blog/drafts/, publications/drafts/, blog/drafts/" >&2
  exit 1
fi

echo "Using draft directory: $DRAFT_DIR"

# --- Check for article files ---
EN_FILE="$DRAFT_DIR/article-en.md"
RU_FILE="$DRAFT_DIR/article-ru.md"

if [ ! -f "$EN_FILE" ]; then
  echo "ERROR: English article not found: $EN_FILE" >&2
  exit 1
fi

if [ ! -f "$RU_FILE" ]; then
  echo "ERROR: Russian article not found: $RU_FILE" >&2
  exit 1
fi

# --- Check pandoc ---
if ! command -v pandoc &>/dev/null; then
  echo "ERROR: pandoc not installed. Install with: sudo apt install pandoc" >&2
  exit 1
fi

# --- Extract frontmatter from EN file (primary) ---
extract_frontmatter() {
  local file="$1"
  local key="$2"
  sed -n '/^---$/,/^---$/p' "$file" \
    | grep "^${key}:" | head -1 \
    | sed "s/^${key}:[[:space:]]*//" \
    | sed 's/^"\(.*\)"$/\1/' \
    | sed "s/^'\(.*\)'$/\1/"
}

TITLE=$(extract_frontmatter "$EN_FILE" "title")
TAGS_RAW=$(extract_frontmatter "$EN_FILE" "tags")
CATEGORIES_RAW=$(extract_frontmatter "$EN_FILE" "categories")

if [ -z "$TITLE" ]; then
  TITLE=$(grep -m1 '^# ' "$EN_FILE" | sed 's/^# //')
fi

if [ -z "$TITLE" ]; then
  echo "ERROR: Could not extract title from $EN_FILE" >&2
  exit 1
fi

echo "Title: $TITLE"
echo "Slug: $SLUG"
echo "Status: $STATUS"

# --- Convert MD to HTML ---
strip_frontmatter() {
  local file="$1"
  if head -1 "$file" | grep -q '^---$'; then
    tail -n +2 "$file" | sed '1,/^---$/d' | sed '1{/^$/d}'
  else
    cat "$file"
  fi
}

EN_HTML=$(strip_frontmatter "$EN_FILE" | pandoc -f markdown -t html --no-highlight)
RU_HTML=$(strip_frontmatter "$RU_FILE" | pandoc -f markdown -t html --no-highlight)

# --- Build bilingual content ---
CONTENT=$(cat <<HTMLEOF
<!-- wp:paragraph -->
<p><a href="#en">English</a> | <a href="#ru">Русский</a></p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:group {"className":"lang-block default"} -->
<div id="en" class="wp-block-group lang-block default">
${EN_HTML}
</div>
<!-- /wp:group -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:group {"className":"lang-block"} -->
<div id="ru" class="wp-block-group lang-block">
${RU_HTML}
</div>
<!-- /wp:group -->
HTMLEOF
)

# --- Clean tags (strip YAML array syntax) ---
clean_list() {
  echo "$1" | tr -d '[]' \
    | sed 's/,/\n/g' \
    | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' \
    | grep -v '^$' \
    | paste -sd',' -
}

TAGS=""
if [ -n "${TAGS_RAW:-}" ]; then
  TAGS=$(clean_list "$TAGS_RAW")
  echo "Tags: $TAGS"
fi

CATEGORIES=""
if [ -n "${CATEGORIES_RAW:-}" ]; then
  CATEGORIES=$(clean_list "$CATEGORIES_RAW")
  echo "Categories: $CATEGORIES"
fi

# --- Publish via API ---
echo ""
echo "Publishing to ${SITE}..."

RESPONSE=$(curl -s -X POST "${API_BASE}/posts/new" \
  -H "Authorization: Bearer ${WP_TOKEN}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "title=${TITLE}" \
  --data-urlencode "slug=${SLUG}" \
  --data-urlencode "content=${CONTENT}" \
  --data-urlencode "status=${STATUS}" \
  --data-urlencode "tags=${TAGS}" \
  --data-urlencode "categories=${CATEGORIES}" \
  --data-urlencode "format=standard")

# --- Check response ---
POST_URL=$(echo "$RESPONSE" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('URL',''))" \
  2>/dev/null || true)
POST_ID=$(echo "$RESPONSE" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('ID',''))" \
  2>/dev/null || true)
ERROR=$(echo "$RESPONSE" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('error',''))" \
  2>/dev/null || true)

if [ -n "$ERROR" ] && [ "$ERROR" != "" ] && [ "$ERROR" != "None" ]; then
  ERROR_MSG=$(echo "$RESPONSE" | python3 -c \
    "import sys,json; d=json.load(sys.stdin); print(d.get('message','Unknown error'))" \
    2>/dev/null || true)
  echo "ERROR: API returned error: $ERROR — $ERROR_MSG" >&2
  echo "Full response:" >&2
  echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE" >&2
  exit 1
fi

if [ -n "$POST_URL" ] && [ "$POST_URL" != "" ] && [ "$POST_URL" != "None" ]; then
  echo ""
  echo "SUCCESS!"
  echo "  Post ID: $POST_ID"
  echo "  URL: $POST_URL"
  echo "  Status: $STATUS"

  # Update frontmatter in both files with wordpress_url
  sed -i "s|^wordpress_url:.*|wordpress_url: \"${POST_URL}\"|" "$EN_FILE"
  if [ -f "$RU_FILE" ]; then
    sed -i "s|^wordpress_url:.*|wordpress_url: \"${POST_URL}\"|" "$RU_FILE"
  fi

  echo "  Updated frontmatter in article files with wordpress_url"
else
  echo "WARNING: Could not extract URL from response. Full response:" >&2
  echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE" >&2
fi
