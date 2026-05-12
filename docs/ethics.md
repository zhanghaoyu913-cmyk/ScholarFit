# Ethics, Privacy, and Misuse Boundaries

## Non-Negotiable Boundaries

ScholarFit must not be used for:

- admissions screening
- hiring, promotion, or elimination decisions
- clinical diagnosis
- predicting mental illness
- assigning irreversible labels such as "not PhD material"
- ranking people by a single "research potential" score

The project is developmental. Reports should be interpreted as reflective prompts, not decisions.

## User Data Principles

1. Local-first by default.
2. No required personally identifying information.
3. Behavioral evidence must be actively uploaded by the user.
4. Raw sensitive text should not be stored unless the user explicitly opts in.
5. Users must be able to delete and export their data.
6. LLM-assisted analysis must be optional and clearly labeled.
7. Report statements must be explainable through item responses and scoring rules.
8. No passive monitoring of browser history, keyboard activity, phone location, private chats, or background behavior.

## Mental Health Language

Allowed:

```text
Your responses suggest higher self-blame in research-failure scenarios. Consider building a concrete failure-review routine and real-world support system.
```

Not allowed:

```text
You are depressed.
You are psychologically unfit for a PhD.
```

## Fairness Risks

ScholarFit must be reviewed for:

- gender measurement invariance
- field and discipline measurement invariance
- undergraduate/master/PhD-stage measurement invariance
- Chinese/English measurement equivalence
- school-resource and socioeconomic confounding
- overfitting to elite-lab, top-conference, or engineering-heavy paths

## LLM Usage Rules

LLMs may assist with:

- summarizing open-ended reflections
- coding reflections using predefined rubrics
- generating report language from computed profiles
- detecting risky or diagnostic wording before release

LLMs must not directly produce final psychological conclusions without rule-based evidence and human-auditable templates.
