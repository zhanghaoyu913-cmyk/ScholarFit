# Item Design Guide

## Item Types

| Type | Purpose |
| --- | --- |
| `situational_judgment` | Most likely action in a realistic research scenario |
| `ranking` | Priority order under tradeoffs |
| `slider` | Continuous research style preference |
| `reflection` | Metacognition and failure-review evidence |
| `behavior_evidence` | Real-world calibration of self-report |

## Writing Rules

1. Write the construct first, then the scenario.
2. Make every option plausible.
3. Avoid obvious virtue signaling.
4. Avoid diagnosing or moralizing.
5. Separate behavior tendency from ability worth.
6. Do not overfit to one field such as ML/AI unless the item is in a field-specific module.
7. Prefer concrete research situations over abstract personality claims.

## Good vs Weak Item

Weak:

```text
Do you persist when research is difficult?
```

Better:

```text
You have spent three days reproducing a published result. The code runs, but your score is 20% lower than reported. What is your next step?
```

## Construct Mapping

Each option may map to multiple constructs.

```json
"B": {
  "research_self_efficacy.debugging": 2,
  "conscientiousness.systematicity": 2,
  "research_maturity.failure_review": 1
}
```

Do not score a whole item as simply right/wrong unless it is explicitly a knowledge check.

## Reflection Coding Rubric

| Dimension | Description |
| --- | --- |
| attribution | Does the user identify controllable factors or global self-blame? |
| specificity | Does the reflection identify concrete causes? |
| strategy_change | Did the user change behavior afterward? |
| emotional_regulation | Did the user recover and continue productively? |
| research_maturity | Did the user extract reusable lessons? |

LLM coding must remain auditable and overrideable.
