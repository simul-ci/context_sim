# After each action, generate a short self-reflection summarizing the rationale
# and any expressed tastes. The output is stored in episodic memory and used
# as context for subsequent action decisions.

ACTION_REFLECTION_PROMPT = """You just performed an action while browsing a {item_type} recommender system. Reflect on it briefly.

## User Profile
- Persona: {persona}
- Preferences: {preferences}

## Action Just Taken
{action_taken}

## Context When Action Was Taken
- Time: {time_context}
- Situation: {situational_context}
- Internal State: Fatigue={fatigue}, Curiosity={curiosity}, Boredom={boredom}

## Outcome
{action_outcome}

## Task
Write a short reflection summarizing why you took this action and what it reveals about your tastes. This reflection will be stored in your memory for future reference.

## Output Format
Return a JSON object:
```json
{{
  "reflection": "<1-2 sentence explanation of why you took this action and what it says about your preferences>"
}}
```

Be concise and specific. Focus on the rationale and any taste insights, not a general summary.
"""
