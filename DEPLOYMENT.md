# Deploy ScholarFit

ScholarFit is a static site. The recommended public user path is:

```text
index.html -> web/index.html?mode=quick
```

Users should normally enter from the root page and click one of:

- `快速版测评`: 20 items, recommended.
- `完整版测评`: 80 items.

## Option A: Standalone GitHub Repository

Use this when ScholarFit should be its own project.

1. Create a new GitHub repository, for example `scholarfit`.
2. Push the contents of this `scholarfit/` directory as the repository root.
3. In GitHub, open `Settings -> Pages`.
4. Set `Source` to `GitHub Actions`.
5. Push to `main`.
6. Open the Pages URL shown by the deployment.

Expected URL shape:

```text
https://<username>.github.io/scholarfit/
```

The included workflow is:

```text
.github/workflows/pages.yml
```

## Option B: Subfolder Under an Existing GitHub Pages Site

Use this if you keep ScholarFit inside an existing site repository.

1. Commit the `scholarfit/` folder to the existing Pages repository.
2. Keep the repository's normal Pages configuration.
3. Visit:

```text
https://<username>.github.io/scholarfit/
```

If the existing repo is not `<username>.github.io`, the URL may be:

```text
https://<username>.github.io/<repo-name>/scholarfit/
```

## Updating the Item Bank

After editing `item_bank/*.json`, regenerate the browser bundle:

```bash
python tools/export_web_items.py
```

Then commit both the changed item bank files and:

```text
web/items.generated.js
```

## Pre-Publish Checks

Run:

```bash
node --check web/app.js
node --check web/sw.js
python -m unittest discover tests
```

Open locally:

```bash
python -m http.server 8765
```

Then visit:

```text
http://127.0.0.1:8765/
```

## Privacy Note

The current static version stores answers only in the user's browser localStorage. It does not upload responses to a server.
