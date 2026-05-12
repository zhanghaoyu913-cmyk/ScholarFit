# Local One-Click Launcher

ScholarFit can run as a local static web app without asking users to type commands.

## Windows

Double-click:

```text
Start-ScholarFit.cmd
```

It will:

1. start a hidden local static server on `127.0.0.1`
2. choose port `8765` or the next available port
3. open the landing page in the default browser
4. save runtime state in `.runtime/`

To stop the local server, double-click:

```text
Stop-ScholarFit.cmd
```

## Fallback

If Python is not installed, the launcher opens `index.html` directly. The app still works because all questions and scripts are local static files. Service-worker offline caching only works under `http://` or `https://`, so the local server path is preferred.

## Public Sharing

For public users, GitHub Pages is still the best distribution mode:

```text
https://<username>.github.io/ScholarFit/
```

The launcher is mainly for offline demos, classroom use, or local testing.
