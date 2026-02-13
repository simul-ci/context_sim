# Infer a user's recent goals from their prior interaction sessions.
# Goals explain *why* the user is browsing (e.g., "find a weekend movie",
# "research a birthday gift"), not just *what* they interacted with.

GOAL_INFERENCE_PROMPT = """You are inferring a user's recent goals from their interaction sessions.

## User Persona
{persona}

## Recent Sessions
{recent_sessions}

## Task
Infer the user's recent goals when engaging with the {item_type} platform. Goals explain *why* they are browsing, not just *what* they interact with.

## Goal Categories
- **Immediate needs**: Specific item search, urgent requirement
- **Exploration**: Browsing for discovery, no specific target
- **Comparison**: Evaluating alternatives before decision
- **Entertainment**: Passing time, casual browsing
- **Research**: Gathering information for future decision
- **Social**: Gift shopping, shared activity planning

## Output Format
Return a JSON object:
```json
{{
  "primary_goal": {{
    "type": "<goal category>",
    "description": "<specific goal description>",
    "confidence": <float 0.0-1.0>,
    "evidence": ["<supporting observations from sessions>"]
  }},
  "secondary_goals": [
    {{
      "type": "<goal category>",
      "description": "<specific goal description>",
      "confidence": <float 0.0-1.0>
    }}
  ]
}}
```

Ground all inferences in observable session patterns.
"""
