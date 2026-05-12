# ScholarFit / 学术罗盘

A story-based PhD fit and research potential assessment toolkit.

ScholarFit is an open-source, developmental assessment system for research self-understanding. It uses situational judgment tasks, contextualized personality items, research self-efficacy prompts, motivation profiling, research-interest mapping, advisor/lab fit scenarios, stress-recovery prompts, and behavioral evidence to help users reason about their current readiness for doctoral training and the environments where they may thrive.

## Project Positioning

ScholarFit is not a PhD talent detector. It is a reflective planning toolkit.

The system helps users answer questions like:

- What kinds of research problems energize me?
- What research behaviors have I already practiced?
- What advisor and lab environments fit my working style?
- Where are my current preparation gaps?
- What can I improve over the next three months?

## Safety Boundaries

ScholarFit must not be used for:

- admissions screening
- hiring or elimination decisions
- clinical diagnosis
- judging mental illness
- irreversible labels about ability, personality, or career worth

Current status: `exploratory / developmental`. Scores and reports are for self-reflection only.

## Repository Layout

```text
scholarfit/
├── docs/
│   ├── theory.md
│   ├── ethics.md
│   ├── validation.md
│   ├── item_design.md
│   ├── scoring.md
│   └── references.bib
├── item_bank/
├── scholarfit/
│   ├── scoring/
│   ├── validation/
│   ├── report/
│   ├── llm_assist/
│   └── privacy/
├── schemas/
├── examples/
├── tests/
└── tools/
```

## Quick Start

### Web Version

For ordinary users, use the static web app first:

```text
index.html
```

Open [index.html](index.html) in a browser. This landing page has a ScholarFit logo and two launch buttons:

- `快速版测评`: 20 items, recommended for first-time users.
- `完整版测评`: 80 items, recommended for full self-reflection.

The actual app lives at [web/index.html](web/index.html). Modes are selected with query parameters:

```text
web/index.html?mode=quick
web/index.html?mode=full
```

The page runs fully in the browser and stores responses in localStorage. It does not require a server for basic use because the item bank is bundled into `web/items.generated.js`.

For hosted use, publish the `scholarfit/` directory with GitHub Pages or any static file host, then link users to the site root or `/web/index.html`.

The web app includes:

- branded landing page
- SVG logo
- web app manifest
- optional service-worker offline cache on HTTPS/static hosting
- local response storage and JSON export

If the item bank changes, regenerate the browser bundle:

```bash
python tools/export_web_items.py
```

### Publish to GitHub Pages

Recommended public setup:

1. Create a standalone GitHub repo such as `scholarfit`.
2. Push the contents of this directory as the repo root.
3. In GitHub, set `Settings -> Pages -> Source` to `GitHub Actions`.
4. Push to `main`.
5. Open the generated Pages URL.

This repo includes a ready workflow:

```text
.github/workflows/pages.yml
```

Full deployment notes are in [DEPLOYMENT.md](DEPLOYMENT.md).

### CLI Version

The CLI is retained for developers, validation work, and batch scoring.

Run a sample scoring pass:

```bash
python -m scholarfit.cli --items item_bank/chapter_3_experiment_ruins.json --responses examples/sample_responses.json
```

Run tests:

```bash
python -m unittest
```

## Design Principles

1. No diagnosis: do not infer mental illness or clinical risk.
2. No elimination: avoid outputs like "you are not suited for a PhD".
3. No MBTI-style determinism: Jung/MBTI language can be used only as narrative metaphor, not as a predictive core.
4. Developmental feedback: report strengths, risks, fit conditions, and growth actions.
5. Evidence-based iteration: item banks, scoring rules, and reports require reliability, validity, fairness, and privacy review before high-stakes use.

## License

MIT. See [LICENSE](LICENSE).
