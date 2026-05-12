"""Command line entry point for v0.1 scoring."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from scholarfit.report import render_markdown_report
from scholarfit.scoring import score_items, summarize_constructs


def load_items(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "items" in payload:
        return list(payload["items"])
    if isinstance(payload, list):
        return payload
    raise ValueError(f"Unsupported item file format: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score ScholarFit item responses.")
    parser.add_argument("--items", required=True, type=Path, help="Path to an item bank JSON file")
    parser.add_argument("--responses", required=True, type=Path, help="Path to response JSON")
    parser.add_argument("--report", type=Path, help="Optional output markdown path")
    args = parser.parse_args()

    items = load_items(args.items)
    response_payload = json.loads(args.responses.read_text(encoding="utf-8"))
    responses = response_payload.get("responses", response_payload)
    result = score_items(items, responses)
    summary = summarize_constructs(result)
    report = render_markdown_report(summary)

    if result.unscored_items:
        report += "\n## Unscored Reflection Items\n\n"
        for item_id in result.unscored_items:
            report += f"- `{item_id}` requires human or optional LLM rubric coding.\n"
    if result.warnings:
        report += "\n## Scoring Warnings\n\n"
        for warning in result.warnings:
            report += f"- {warning}\n"

    if args.report:
        args.report.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
