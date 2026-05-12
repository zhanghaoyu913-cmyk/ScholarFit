# Web App Usage

ScholarFit includes a no-backend static web version for normal users.

## Local Use

Open:

```text
index.html
```

This opens a branded landing page with a ScholarFit logo and two launch buttons:

- `快速版测评`: 20 items, recommended for first-time users.
- `完整版测评`: 80 items, recommended for full self-reflection.

The actual app lives at:

```text
web/index.html
```

Direct mode links:

```text
web/index.html?mode=quick
web/index.html?mode=full
```

The app loads the bundled item bank from:

```text
web/items.generated.js
```

Responses are saved in the current browser's localStorage. No answer is uploaded anywhere by this static version.

## Hosted Use

Recommended: put the contents of `scholarfit/` in a standalone GitHub repository, then host that repository with GitHub Pages.

You can also host the whole `scholarfit/` directory on any static host:

- GitHub Pages
- Cloudflare Pages
- Netlify
- Vercel static deployment
- university or lab static server

The public entry should point to the site root:

```text
/
```

Users will see the logo landing page and click `开始测评`.

If you embed ScholarFit under another site, link directly to:

```text
/scholarfit/index.html
```

## Updating Questions

After editing files in `item_bank/`, regenerate the browser bundle:

```bash
python tools/export_web_items.py
```

Then reload the web page.

## Why Not Require a Backend?

The first web version is static by design:

- lower friction for users
- no database setup
- lower privacy risk
- easy GitHub Pages deployment
- still compatible with later backend or mini-program versions

## PWA Wrapper

The web app includes:

- `web/assets/logo.svg`
- `web/manifest.webmanifest`
- `web/sw.js`

On HTTPS hosting, modern browsers can treat it like an installable lightweight web app. The service worker only caches static app files; it does not upload responses.

## Mini-Program Path

A WeChat mini-program or mobile app can reuse the same three layers:

- `item_bank/*.json` as content source
- `scholarfit/scoring/rules.py` logic ported to TypeScript
- report template from `web/app.js`

For a serious public launch, build the static web version first, validate item wording and scoring, then port the stable interaction model to a mini-program.
