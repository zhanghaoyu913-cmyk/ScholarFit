# Release Checklist

Use this before publishing a public ScholarFit build.

## Static Site

- Root `index.html` opens and shows the logo landing page.
- `web/index.html?mode=quick` loads the 20-item quick version.
- `web/index.html?mode=full` loads the 80-item full version.
- The report can be generated before and after all questions are complete.
- Markdown report copy works on HTTPS hosting.
- JSON export works in browser.

## Measurement Safety

- The page states it is not for admissions, hiring, elimination, or diagnosis.
- The report avoids "suitable / unsuitable for PhD" conclusions.
- Reflection items are saved but not automatically diagnosed.
- Draft validation status is visible in docs.

## Content

- `item_bank/*.json` are valid JSON.
- `web/items.generated.js` has been regenerated after item changes.
- Quick-version item IDs exist in the full item bank.
- No protected-class stereotypes or clinical labels were introduced.

## Engineering

- `node --check web/app.js` passes.
- `node --check web/sw.js` passes.
- `python -m unittest discover tests` passes.
- GitHub Pages deployment is configured if using a standalone repository.
