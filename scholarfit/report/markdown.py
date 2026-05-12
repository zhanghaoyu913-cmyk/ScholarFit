"""Markdown report rendering for transparent v0.1 profiles."""

from __future__ import annotations

from collections import defaultdict
from typing import Mapping

PROFILE_PREFIXES = {
    "motivation": "Research Motivation",
    "research_self_efficacy": "Research Self-Efficacy",
    "research_behavior": "Research Behavior",
    "personality": "Personality-in-Research",
    "conscientiousness": "Personality-in-Research",
    "emotional_stability": "Personality-in-Research",
    "agreeableness": "Personality-in-Research",
    "direction_interest": "Research Direction Fit",
    "advisor_fit": "Advisor/Lab Fit",
    "help_seeking": "Advisor/Lab Fit",
    "stress_recovery": "Stress and Recovery",
    "academic_integrity": "Academic Integrity",
    "research_maturity": "Growth Recommendation Signals",
    "growth": "Growth Recommendation Signals",
}


def _profile_for_construct(construct: str) -> str:
    for prefix, profile in PROFILE_PREFIXES.items():
        if construct.startswith(prefix + ".") or construct == prefix:
            return profile
    return "Other Signals"


def render_markdown_report(
    summary: Mapping[str, Mapping[str, object]],
    *,
    title: str = "ScholarFit Report",
) -> str:
    grouped: dict[str, list[tuple[str, Mapping[str, object]]]] = defaultdict(list)
    for construct, stats in summary.items():
        grouped[_profile_for_construct(construct)].append((construct, stats))

    lines = [
        f"# {title}",
        "",
        "This report is for self-reflection only. It is not a diagnosis, selection decision, or PhD suitability verdict.",
        "",
    ]
    for profile in dict.fromkeys(PROFILE_PREFIXES.values()):
        entries = grouped.get(profile, [])
        if not entries:
            continue
        lines.append(f"## {profile}")
        lines.append("")
        for construct, stats in entries:
            lines.append(
                f"- `{construct}`: raw score {stats.get('raw_score')}, "
                f"evidence count {stats.get('evidence_count')}, "
                f"confidence {stats.get('confidence')}"
            )
        lines.append("")

    if grouped.get("Other Signals"):
        lines.append("## Other Signals")
        lines.append("")
        for construct, stats in grouped["Other Signals"]:
            lines.append(f"- `{construct}`: {stats}")
        lines.append("")

    lines.extend(
        [
            "## Interpretation Boundary",
            "",
            "Scores reflect response patterns in this item bank. They should be interpreted together with context, opportunity, resources, and real-world constraints.",
        ]
    )
    return "\n".join(lines) + "\n"
