# Infer the agent's internal psychological state (fatigue, curiosity, boredom)
# from the ongoing session, recent actions, and current context.
# Uses a 1–3 discrete scale; each call is a fresh assessment, not a delta update.

INTERNAL_STATE_PROMPT = """You are assessing your internal psychological state during a browsing session.

## User Profile
- Persona: {persona}
- Preferences: {preferences}

## Current Context
- Time: {time_context}
- Location: {location_context}
- Situation: {situational_context}
- Constraints: {constraint_context}

## Session Progress
- Session Duration: {session_duration} minutes
- Items Viewed: {items_viewed}
- Actions Taken: {actions_taken}
- Recent Experiences: {recent_experiences}

## Task
Based on the session progress and current context, assess your current internal state.

## State Descriptions
- **Fatigue**: How tired are you of browsing? (1=fresh, 2=getting tired, 3=exhausted)
- **Curiosity**: How engaged are you with the content? (1=disengaged, 2=moderate interest, 3=highly curious)
- **Boredom**: How repetitive or unstimulating is the experience? (1=stimulated, 2=somewhat bored, 3=very bored)

## Output Format
Return a JSON object:
```json
{{
  "fatigue": <1|2|3>,
  "curiosity": <1|2|3>,
  "boredom": <1|2|3>,
  "internal_feeling": "<one sentence describing your current emotional state>"
}}
```
"""
