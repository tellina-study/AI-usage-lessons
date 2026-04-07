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

The site uses a **manual bilingual structure within single posts** -- not a plugin:

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

### WordPress.org REST API (/wp-json/)

**Not available.** Both /wp-json/wp/v2/ and /wp-json/wp/v2/posts return 404. WordPress.com does not expose the self-hosted REST API endpoints by default.

### WordPress.com REST API v1.1

**Available and working.** Endpoint: https://public-api.wordpress.com/rest/v1.1/sites/tellian.io/

- GET posts works without auth
- POST (create) requires OAuth2 bearer token
- Full post objects returned with title, content, categories, tags, slug, status

### Authentication for write access

WordPress.com uses OAuth2:

1. Register app at https://developer.wordpress.com/apps/new
2. Get client_id + client_secret
3. Exchange credentials for bearer token via grant_type=password flow (no browser needed)
4. Use Authorization: Bearer TOKEN for all write requests

Create post endpoint: POST https://public-api.wordpress.com/rest/v1.1/sites/tellian.io/posts/new

## 3. MCP Server Options

### Option A: WordPress.com built-in MCP

- URL: https://public-api.wordpress.com/wpcom/v2/mcp/v1
- Official WordPress.com + Anthropic partnership (Feb 2026)
- **Limitation:** Currently read-only. Cannot create, delete, or modify content.
- **Verdict:** Not suitable for publishing.

### Option B: AI Engine plugin (Meow Apps)

- Requires installing the AI Engine WordPress plugin
- Provides 87 MCP tools including post management
- **Limitation:** WordPress.com Business plan ($33/mo) or higher needed to install plugins.
- **Verdict:** Viable only if plugin installation is possible on the current plan.

### Option C: claudeus-wp-mcp (GitHub)

- 145 tools, self-hosted MCP server
- **Verdict:** Not compatible with WordPress.com hosting.

### Option D: Royal MCP plugin

- Security-focused MCP plugin
- **Verdict:** Same constraint as AI Engine -- requires plugin installation.

## 4. Publishing Options Evaluation

### Option 1: WordPress.com REST API v1.1 + shell script (RECOMMENDED)

**Pros:**

- Works with WordPress.com hosted sites directly
- No plugins needed
- Full control over HTML output
- CLI-friendly (grant_type=password, no browser)
- Matches existing bilingual post structure
- Can be wrapped in a Claude Code skill

**Cons:**

- One-time OAuth2 app registration needed
- Token management (store in .env)
- Must construct bilingual HTML wrapper manually

**Setup complexity:** Low-medium.
**Maintenance:** Low. Token refresh if expired.

### Option 2: WordPress.com MCP (built-in)

**Verdict:** Not viable -- read-only, cannot create posts.

### Option 3: AI Engine MCP plugin

**Verdict:** Requires WordPress.com Business plan ($33/mo). Overkill.

### Option 4: wp-cli via SSH

**Verdict:** Not available on WordPress.com hosting.

### Option 5: Manual copy-paste

**Pros:** Zero setup. **Cons:** Manual effort, error-prone.

## 5. Markdown to HTML Conversion

### Recommended: pandoc

Install: sudo apt install pandoc
Usage: pandoc -f markdown -t html article.md

### Special handling needed

- Images: upload to WordPress media library first, then reference by URL
- Bilingual wrapper divs must be added after conversion

## 6. Recommendation

**Use Option 1: WordPress.com REST API v1.1 + publish script.**

Script at scripts/publish-to-wp.sh, Claude Code skill publish-article orchestrates.

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
