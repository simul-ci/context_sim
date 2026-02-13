# Infer natural-language preference descriptions from persona and interaction history.
# Produces a short summary of the user's tastes (liked/disliked patterns, genre leanings)
# that is stored in the agent's profile for downstream prompts.

PREFERENCE_INFERENCE_PROMPT = """You are inferring a user's preferences from their interaction history.

## User Persona
{persona}

## Interaction History
{interaction_history}

## Task
Generate a short natural-language description that summarizes this user's tastes. This summary will be stored as part of the user's profile and used to predict their future behavior.

## Instructions
1. Analyze which categories, genres, or item attributes the user consistently engages with or rates highly.
2. Note what the user tends to avoid or rate poorly.
3. Ground every observation in concrete evidence from the interaction history.
4. Keep the summary concise (3-5 sentences) and specific — avoid generic statements like "enjoys popular items."

## Output Format
Return a JSON object:
```json
{{
  "preference_summary": "<3-5 sentence natural language description of the user's tastes>"
}}
```
"""
