# Validation Plan

ScholarFit v0.1 is exploratory. Validation is required before any claim of reliability, validity, or fairness.

## Stage 1: Content Validity

- Recruit reviewers: PhD students, postdocs, PIs, psychometricians, and research-methods educators.
- Review each item for construct clarity, realism, option plausibility, cultural bias, and safety.
- Track item-level change history.

## Stage 2: Cognitive Interviews

- Ask users to explain how they interpreted scenarios and options.
- Identify ambiguous wording, obvious answer keys, culture-specific assumptions, and hidden prerequisites.
- Revise before broad data collection.

## Stage 3: Pilot Data

Minimum pilot targets:

- 100-200 users for initial item diagnostics.
- 300-500 users for early factor analysis.
- Larger and more diverse samples before cross-group comparison.

## Stage 4: Reliability

Evaluate:

- internal consistency: Cronbach's alpha and McDonald's omega
- test-retest reliability: 2-4 week interval
- inter-rater agreement: human vs LLM coding of reflection items
- branch stability: whether alternate story paths still measure intended constructs

## Stage 5: Validity Evidence

Collect evidence for:

- content validity
- structural validity: EFA and CFA
- convergent validity: correlation with IPIP, research self-efficacy, and motivation scales
- discriminant validity: constructs should not collapse into one general desirability factor
- criterion validity: relation to research behavior, sustained engagement, satisfaction, and self-regulation
- incremental validity: whether SJT/story items add value beyond ordinary self-report

## Stage 6: Fairness and Measurement Invariance

Before comparing group means, test whether constructs have equivalent measurement meaning across groups.

Recommended sequence:

1. configural invariance
2. metric invariance
3. scalar invariance
4. residual invariance where appropriate
5. differential item functioning review

Groups to examine:

- gender
- discipline or research field
- education stage
- language version
- school/resource background
- cultural background

## Stage 7: Release Labels

Every release should state validation status:

- `experimental`: item bank and scoring under development
- `pilot-validated`: content review and initial pilot complete
- `research-validated`: reliability and validity evidence published
- `restricted-use`: known limitations prevent broad interpretation

No release should claim high-stakes suitability without independent validation.
