# Scoring Model

## v0.1 Rule Scoring

ScholarFit v0.1 uses transparent rule scoring. Each selected option contributes weighted points to one or more constructs.

```json
"B": {
  "research_self_efficacy.debugging": 2,
  "conscientiousness.systematicity": 2,
  "emotional_stability.failure_recovery": 1
}
```

## No Single Total Score

Do not collapse results into a single PhD-fit score. Output separate profiles:

- Research Motivation
- Research Self-Efficacy
- Research Behavior
- Personality-in-Research
- Research Direction Fit
- Advisor/Lab Fit
- Stress and Recovery
- Academic Integrity
- Growth Recommendations

## Supported Item Scoring

### Situational Judgment

The selected option maps directly to construct weights.

### Ranking

Each ranked option has construct weights. A position-weight vector converts priority into score contribution.

Default for five options:

```json
[2, 1, 0, -1, -2]
```

### Slider

A 1-5 response is interpreted as a preference between two anchors. The center point is neutral.

### Reflection

No automatic psychological conclusion. Reflection items are exported for human or optional LLM coding.

### Behavior Evidence

Selected evidence items add calibration points. They should not dominate profile scores because opportunity and resource access vary across users.

## Confidence

Report confidence separately from score.

Confidence may use:

- number of answered items per construct
- response consistency
- presence of behavior evidence
- reflection coding completeness
- item validation status

## Future Scoring

Later versions may add:

- Thurstonian IRT
- multidimensional forced-choice IRT
- Bayesian pairwise preference models
- measurement-invariance-aware scoring
- computer adaptive testing

Raw responses should be preserved to enable future rescoring.
