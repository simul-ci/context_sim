# Determine whether the agent should engage with the RS at the current time slot.
# Given the user's persona, schedule, and current context, returns YES/NO with a
# contextual scenario (time, location, situation, goal, constraints) if engaging.

ENGAGEMENT_CHECK_PROMPT = """You are deciding whether to engage with a {item_type} recommender system right now.

## User Profile
- Persona: {persona}
- Preferences: {preferences}

## Current Life Context
- Time: {current_time}
- Day: {day_of_week}
- Location: {location}
- Current Activity: {current_activity}
- Mood: {mood}
- Energy Level: {energy}
- Need Level: {need_level}
- Recent Activities: {recent_activities}

## Task
Decide whether this is a natural moment to engage with the {item_type} platform, given your current situation.

## Decision Factors
1. Is this an appropriate time based on your schedule and current activity?
2. Are there higher-priority needs to address first?
3. Does your current mood and energy support engagement?
4. Is there a specific reason to engage now?

## Output Format
Return a JSON object:
```json
{{
  "should_engage": true|false,
  "reasoning": "<why or why not, 20-40 words>",
  "goal_if_engaging": "<what you would look for, or null if not engaging>"
}}
```

Be realistic. Most moments in life are NOT times to engage with a {item_type} platform.
"""
