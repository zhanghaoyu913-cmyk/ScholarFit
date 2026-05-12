"""Transparent v0.1 rule scoring for ScholarFit item banks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass
class ScoreResult:
    """Accumulated construct scores plus audit metadata."""

    scores: dict[str, float] = field(default_factory=dict)
    evidence_count: dict[str, int] = field(default_factory=dict)
    unscored_items: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add(self, construct: str, value: float) -> None:
        self.scores[construct] = self.scores.get(construct, 0.0) + float(value)
        self.evidence_count[construct] = self.evidence_count.get(construct, 0) + 1

    def merge(self, other: "ScoreResult") -> "ScoreResult":
        for construct, value in other.scores.items():
            self.scores[construct] = self.scores.get(construct, 0.0) + value
        for construct, count in other.evidence_count.items():
            self.evidence_count[construct] = self.evidence_count.get(construct, 0) + count
        self.unscored_items.extend(other.unscored_items)
        self.warnings.extend(other.warnings)
        return self


def _add_weights(result: ScoreResult, weights: Mapping[str, Any], multiplier: float = 1.0) -> None:
    for construct, value in weights.items():
        if isinstance(value, (int, float)):
            result.add(construct, value * multiplier)


def score_item(item: Mapping[str, Any], response: Any) -> ScoreResult:
    """Score one item response.

    This intentionally stays simple and auditable. It does not normalize scores
    or infer psychological conclusions.
    """

    result = ScoreResult()
    item_id = str(item.get("id", "<unknown>"))
    item_type = item.get("type")
    scoring = item.get("scoring", {}) or {}

    if item_type == "situational_judgment":
        option_scores = scoring.get(str(response))
        if not isinstance(option_scores, Mapping):
            result.warnings.append(f"{item_id}: no scoring rule for response {response!r}")
            return result
        _add_weights(result, option_scores)
        return result

    if item_type == "ranking":
        if not isinstance(response, list):
            result.warnings.append(f"{item_id}: ranking response must be a list")
            return result
        position_weights = scoring.get("position_weights", [])
        option_weights = scoring.get("options", {})
        for idx, option in enumerate(response):
            if idx >= len(position_weights):
                break
            weights = option_weights.get(str(option), {})
            if isinstance(weights, Mapping):
                _add_weights(result, weights, float(position_weights[idx]))
        return result

    if item_type == "slider":
        try:
            numeric_response = float(response)
        except (TypeError, ValueError):
            result.warnings.append(f"{item_id}: slider response must be numeric")
            return result
        min_value = float(scoring.get("min", 1))
        max_value = float(scoring.get("max", 5))
        midpoint = (min_value + max_value) / 2
        left = scoring.get("left", {})
        right = scoring.get("right", {})
        if numeric_response < midpoint and isinstance(left, Mapping):
            _add_weights(result, left, midpoint - numeric_response)
        elif numeric_response > midpoint and isinstance(right, Mapping):
            _add_weights(result, right, numeric_response - midpoint)
        return result

    if item_type == "behavior_evidence":
        if isinstance(response, str):
            selected = [response]
        elif isinstance(response, list):
            selected = response
        else:
            result.warnings.append(f"{item_id}: behavior evidence response must be a string or list")
            return result
        option_weights = scoring.get("options", {})
        for option in selected:
            weights = option_weights.get(str(option), {})
            if isinstance(weights, Mapping):
                _add_weights(result, weights)
        return result

    if item_type == "reflection":
        result.unscored_items.append(item_id)
        return result

    result.warnings.append(f"{item_id}: unsupported item type {item_type!r}")
    return result


def score_items(items: list[Mapping[str, Any]], responses: Mapping[str, Any]) -> ScoreResult:
    """Score a list of items against an item-id keyed response mapping."""

    total = ScoreResult()
    for item in items:
        item_id = str(item.get("id", ""))
        if item_id not in responses:
            continue
        total.merge(score_item(item, responses[item_id]))
    return total


def summarize_constructs(result: ScoreResult) -> dict[str, dict[str, float | int | str]]:
    """Return transparent construct summaries with simple confidence labels."""

    summary: dict[str, dict[str, float | int | str]] = {}
    for construct, score in sorted(result.scores.items()):
        count = result.evidence_count.get(construct, 0)
        if count >= 6:
            confidence = "high"
        elif count >= 3:
            confidence = "medium"
        else:
            confidence = "low"
        summary[construct] = {
            "raw_score": round(score, 3),
            "evidence_count": count,
            "confidence": confidence,
        }
    return summary
