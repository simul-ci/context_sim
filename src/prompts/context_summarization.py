# Summarize 30 days of simulated daily life into a short context description.
# Covers 5 dimensions (temporal patterns, locations, situations, goals, constraints)
# and is appended to the persona for the ContextSim(sum) variant.

CONTEXT_SUMMARIZATION_PROMPT = """You are summarizing a user's daily life patterns for recommendation personalization.

## User Profile
- Persona: {persona}

## 30-Day Activity Log
{activity_log}

## Task
Summarize this user's lifestyle patterns that are relevant for {item_type} recommendation timing and context. The summary will be appended to the user's persona for all subsequent interactions.

## Analysis Dimensions
1. **Temporal patterns**: When do they typically engage with {item_type} recommendations? (time of day, day of week)
2. **Spatial patterns**: Where are they when engaging? (home, commuting, work, etc.)
3. **Situational patterns**: What activities, moods, or energy levels typically precede engagement?
4. **Goal patterns**: What are typical reasons for seeking {item_type} recommendations?
5. **Constraint patterns**: What limits their engagement? (time budget, spending budget)

## Output Format
Return a JSON object:
```json
{{
  "context_summary": "<4-6 sentence natural language summary covering the above dimensions>"
}}
```

Focus on recurring patterns, not individual events. Be specific and grounded in the activity log.
"""
