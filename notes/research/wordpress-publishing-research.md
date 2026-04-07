# WordPress Publishing Research

Issue: #39
Date: 2026-04-07

## 1. Site Analysis

**URL:** https://tellian.io/
**Hosting:** WordPress.com (confirmed by wpcom references, remote login iframe, actionbar)
**Theme:** TwentySixteen
**Plan:** Paid (custom domain mapped)

### Detected plugins/features

- Jetpack (bundled with WordPress.com)
- Gutenberg block editor
- Comment Likes
- WordPress.com native features (actionbar, subscriptions, Gravatar)
- No WPML, Polylang, or TranslatePress detected

### Multilingual approach

The site uses a **manual bilingual structure within single posts** — not a plugin:

- Each post contains both EN and RU content in one document
- Language switcher at top: `<a href="#en">English</a> | <a href="#ru">Русский</a>`
- English section: `<div id="en" class="wp-block-group lang-block default">`
- Russian section: `<div id="ru" class="wp-block-group lang-block">`
- English is the default (has `default` CSS class)

This means publishing automation must construct the combined bilingual HTML.

### Content structure

- Categories: CDO, Data Architecture, Data Governance, RAG, Roles, Semantic Processing
- 40+ tags covering AI, business, data topics
- Posts are blog-style articles

## 2. API Availability

### WordPress.org REST API (`/wp-json/`)

**Not available.** Both `/wp-json/wp/v2/` and `/wp-json/wp/v2/posts` return 404. WordPress.com does not expose the self-hosted REST API endpoints by default.

### WordPress.com REST API v1.1

**Available and working.** Endpoint: `https://public-api.wordpress.com/rest/v1.1/sites/tellian.io/`

- GET posts works without auth: `GET /rest/v1.1/sites/tellian.io/posts/`
- POST (create) requires OAuth2 bearer token
- Full post objects returned with title, content, categories, tags, slug, status

### Authentication for write access

WordPress.com uses OAuth2:

1. Register app at https://developer.wordpress.com/apps/new
2. Get client_id + client_secret
3. Exchange credentials for bearer token via `grant_type=password` flow (no browser needed)
4. Use `Authorization: Bearer TOKEN` for all write requests

Create post endpoint: `POST https://public-api.wordpress.com/rest/v1.1/sites/tellian.io/posts/new`

## 3. MCP Server Options

### Option A: WordPress.com built-in MCP

- URL: `https://public-api.wordpress.com/wpcom/v2/mcp/v1`
- Uses OAuth 2.1 with PKCE
- Official WordPress.com + Anthropic partnership (Feb 2026)
- **Limitation:** Currently read-only. Cannot create, delete, or modify content. Designed for analytics, content analysis, SEO audits.
- **Verdict:** Not suitable for publishing. Read-only.

### Option B: AI Engine plugin (Meow Apps)

- Requires installing the AI Engine WordPress plugin
- Provides 87 MCP tools including post management
- Setup: `claude mcp add wp-site https://site.com/wp-json/mcp/v1/http --transport http --header "Authorization: Bearer TOKEN"`
- **Limitation:** Requires plugin installation. WordPress.com Business plan or higher needed to install plugins. May not be available on current plan.
- **Verdict:** Viable only if plugin installation is possible on the current plan.

### Option C: claudeus-wp-mcp (GitHub)

- 145 tools, self-hosted MCP server
- Requires self-hosted WordPress (not WordPress.com)
- **Verdict:** Not compatible with WordPress.com hosting.

### Option D: Royal MCP plugin

- Security-focused MCP plugin
- Same limitation as Option B — requires plugin installation
- **Verdict:** Same constraint as AI Engine.

## 4. Publishing Options Evaluation

### Option 1: WordPress.com REST API v1.1 + shell script (RECOMMENDED)

**How it works:**
1. Markdown articles in `publications/drafts/{slug}/` (already set up per #36)
2. Convert MD to HTML using pandoc
3. Wrap EN + RU HTML in bilingual div structure matching existing posts
4. POST to WordPress.com REST API v1.1 with OAuth2 token
5. Update frontmatter with wordpress_url after publishing

**Pros:**
- Works with WordPress.com hosted sites directly
- No plugins needed
- Full control over HTML output
- CLI-friendly (grant_type=password, no browser)
- Matches existing bilingual post structure
- Can be wrapped in a Claude Code skill

**Cons:**
- One-time OAuth2 app registration needed
- Token management (store in .mcp.json or env var)
- Must construct bilingual HTML wrapper manually

**Setup complexity:** Low-medium. Register app, get token, write publish script.
**Maintenance:** Low. Token refresh if expired.

### Option 2: WordPress.com MCP (built-in)

**Verdict:** Not viable — read-only, cannot create posts.

### Option 3: AI Engine MCP plugin

**Pros:**
- Rich tool set (87 functions)
- Native MCP integration with Claude Code
- Polylang support (11 functions) — though site doesn't use Polylang

**Cons:**
- Requires WordPress.com Business plan ($33/mo) to install plugins
- Plugin dependency — if AI Engine breaks, publishing breaks
- Overkill for publishing articles (87 tools when we need ~3)

**Setup complexity:** Medium. Upgrade plan + install plugin + configure MCP.
**Maintenance:** Medium. Plugin updates, compatibility.

### Option 4: wp-cli via SSH

**Verdict:** Not available on WordPress.com hosting. Only on self-hosted.

### Option 5: Manual copy-paste with documented process

**Pros:**
- Zero setup
- Works immediately
- Full visual control

**Cons:**
- Manual effort each time
- No automation possible
- Error-prone for bilingual HTML structure

**Setup complexity:** None.
**Maintenance:** High (human effort per post).

## 5. Markdown to HTML Conversion

### Recommended: pandoc

- `pandoc -f markdown -t html article.md`
- Handles code blocks, tables, headers, links, images
- Available on most Linux systems
- Can be called from shell scripts

### Alternatives

- **marked** (Node.js) — good if you prefer JS toolchain
- **showdown** (JS) — browser-compatible, less feature-rich
- **python-markdown** — if Python preferred

### Special handling needed

- Code blocks: pandoc produces proper `<pre><code>` blocks
- Images: must be uploaded to WordPress media library first, then referenced by URL
- Tables: pandoc produces HTML tables, which Gutenberg handles
- The bilingual wrapper divs must be added after conversion

## 6. Recommendation

**Use Option 1: WordPress.com REST API v1.1 + publish script.**

### Implementation plan

1. Register a WordPress.com OAuth2 app (one-time, manual)
2. Get bearer token via password grant (one-time, store in `.env` or `.mcp.json`)
3. Create `scripts/publish-to-wp.sh`:
   - Reads article-en.md and article-ru.md from a publications/drafts/{slug}/ folder
   - Converts each to HTML via pandoc
   - Wraps in bilingual div structure
   - Extracts frontmatter (title, tags, categories, slug)
   - POSTs to WordPress.com API
   - Returns the published URL
4. Create a Claude Code skill `publish-article` that orchestrates the above
5. Update publication.md template with publishing instructions

### Bilingual HTML template

```html
<a href="#en">English</a> | <a href="#ru">Русский</a>
<hr>
<div id="en" class="wp-block-group lang-block default">
{english_html}
</div>
<hr>
<div id="ru" class="wp-block-group lang-block">
{russian_html}
</div>
```

### API call structure

```bash
curl -X POST \
  "https://public-api.wordpress.com/rest/v1.1/sites/tellian.io/posts/new" \
  -H "Authorization: Bearer $WP_TOKEN" \
  -d "title=$TITLE" \
  -d "content=$BILINGUAL_HTML" \
  -d "status=draft" \
  -d "tags=$TAGS" \
  -d "categories=$CATEGORIES"
```
