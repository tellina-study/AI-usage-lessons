# publish-article

Publish a bilingual blog article to tellian.io via WordPress.com REST API v1.1.

## Trigger

/publish-article <slug>

## Prerequisites

- pandoc installed (sudo apt install pandoc)
- WP_TOKEN set in .env (WordPress.com OAuth2 bearer token)
- Article files exist: article-en.md and article-ru.md in the slug folder
- Both files have YAML frontmatter with at least title field

## Steps

1. **Validate** -- check that article-en.md and article-ru.md exist in the slug folder
2. **Preview** -- show the user the title, tags, categories extracted from frontmatter
3. **Run script** -- execute scripts/publish-to-wp.sh {slug} (publishes as draft by default)
4. **Verify** -- check the response for success, show the WordPress URL
5. **Update status** -- update frontmatter status: published and wordpress_url in both article files
6. **Copy to published** -- copy the slug folder to the published directory
7. **Report** -- show the published URL to the user

## Publish as live (not draft)

Add --publish flag: scripts/publish-to-wp.sh {slug} --publish

Only do this after the user explicitly confirms.

## Token setup (one-time)

1. Go to https://developer.wordpress.com/apps/new and register an app
2. Set redirect URL to https://tellian.io/
3. Note the client_id and client_secret
4. Get token:
   ```
   curl -X POST https://public-api.wordpress.com/oauth2/token \
     -d "client_id=YOUR_CLIENT_ID" \
     -d "client_secret=YOUR_CLIENT_SECRET" \
     -d "grant_type=password" \
     -d "username=YOUR_WPCOM_USERNAME" \
     -d "password=YOUR_APP_PASSWORD"
   ```
5. Add to .env: WP_TOKEN=the_returned_access_token
