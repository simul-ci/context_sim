# Generate diverse candidate personas from a user's interaction history.

PERSONA_CANDIDATE_GENERATION_PROMPT = """You are a user profiling system for a {item_type} recommendation platform.

## Task
Given a user's interaction history, generate {num_candidates} distinct candidate personas that could plausibly explain these behavioral patterns.

## User Interaction History
{interaction_history}

## Instructions
1. Analyze the patterns in the interaction history (item types, timing, ratings, categories).
2. Generate {num_candidates} diverse candidate personas that could produce this behavior.
3. Each persona must include ALL of the following attributes:

### Required Attributes
- **age**: Integer (18-80)
- **occupation**: Specific job title or "student" | "retired" | "unemployed"
- **personality**: Big Five traits, each scored 1-3 (1=low, 2=medium, 3=high)
  - openness: Curiosity, creativity, preference for novelty
  - conscientiousness: Organization, dependability, self-discipline
  - extraversion: Sociability, assertiveness, positive emotions
  - agreeableness: Cooperation, trust, helpfulness
  - neuroticism: Emotional instability, anxiety, moodiness

### Derivation Guidelines
- Age: Infer from item preferences (e.g., nostalgic items → older, trending items → younger)
- Occupation: Infer from activity timing patterns and item categories
- Personality: Infer from diversity of choices (openness), consistency (conscientiousness), social items (extraversion), mainstream vs niche (agreeableness), rating variance (neuroticism)

## Output Format
Return a JSON array of {num_candidates} persona objects:
```json
[
  {{
    "candidate_id": 1,
    "age": <int>,
    "occupation": "<string>",
    "personality": {{
      "openness": <1|2|3>,
      "conscientiousness": <1|2|3>,
      "extraversion": <1|2|3>,
      "agreeableness": <1|2|3>,
      "neuroticism": <1|2|3>
    }},
    "reasoning": "<brief explanation of why this persona fits the history>"
  }},
  ...
]
```

Generate exactly {num_candidates} diverse candidates. Do not include any text outside the JSON.
"""
