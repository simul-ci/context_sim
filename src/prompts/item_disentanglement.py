# Item Disentanglement — generate a first-person chain-of-thought explaining
# why a user's rating aligns with their persona, preferences, history, and context.
# The output is collected into D_ID and used for SFT training.

ITEM_DISENTANGLEMENT_PROMPT = """You are a reasoning system that explains why a user's rating aligns with their preferences.

## User Profile
- Persona: {persona}
- Preferences: {preferences}
- Interaction History: {history_summary}

## Current Context
- Time: {time_context}
- Location: {location_context}
- Situation: {situational_context}
- Current Goal: {goal_context}
- Constraints: {constraint_context}

## Item Information
- Item: {item_name}
- Category: {item_category}
- Attributes: {item_attributes}
- Description: {item_description}

## User's Rating: {rating} (scale: {rating_scale})

## Task
Generate a first-person internal thought explaining WHY this user gave this rating to this item. The thought must:
1. Reference specific aspects of the user's persona and preferences that connect to this item.
2. Relate to the user's past interaction patterns — is this rating consistent or a departure?
3. Attribute the rating to concrete item features (not vague qualities).
4. Consider how the current context (time, location, situation, goal) may have influenced the rating.

## Output Format
Return a JSON object:
```json
{{
  "thought": "<first-person internal monologue, 50-100 words, grounded in the above factors>"
}}
```

Example style: "I gave this a high rating because it matches my usual preference for [specific feature]. Given that I'm [context], this really appeals to me. It reminds me of [past item] which I also enjoyed because [reason]."

Do NOT produce generic reasoning. Every claim must trace back to a specific element from the user profile, history, item, or context.
"""
