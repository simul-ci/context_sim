# Score how well a candidate persona explains a user's interaction history.
# Returns a 0.0–1.0 consistency score with a per-dimension breakdown
# (demographics, personality, habits, preferences) to select the best-fit persona.

PERSONA_CONSISTENCY_SCORING_PROMPT = """You are evaluating how well a candidate persona explains a user's interaction history.

## Candidate Persona
{persona}

## User Interaction History
{interaction_history}

## Task
Score how consistently this persona explains the observed behavior on a scale of 0.0 to 1.0.

## Evaluation Criteria
1. **Demographic Fit (0-0.25)**: Does the age/occupation align with item preferences and timing?
2. **Personality Fit (0-0.25)**: Do the Big Five traits explain choice patterns?
   - High openness → diverse categories, experimental choices
   - High conscientiousness → consistent quality preferences, planned purchases
   - High extraversion → social/trending items, frequent engagement
   - High agreeableness → mainstream choices, positive ratings
   - High neuroticism → variable ratings, impulsive patterns
3. **Behavioral Coherence (0-0.25)**: Are there contradictions between persona and history?
4. **Predictive Power (0-0.25)**: Could this persona reliably predict future behavior?

## Output Format
Return a JSON object:
```json
{{
  "consistency_score": <float 0.0-1.0>,
  "breakdown": {{
    "demographic_fit": <float 0.0-0.25>,
    "personality_fit": <float 0.0-0.25>,
    "behavioral_coherence": <float 0.0-0.25>,
    "predictive_power": <float 0.0-0.25>
  }},
  "contradictions": ["<list any persona-history conflicts>"],
  "strengths": ["<list strong alignments>"]
}}
```

Be rigorous. Most personas should score 0.4-0.7. Only exceptionally fitting personas score above 0.8.
"""
