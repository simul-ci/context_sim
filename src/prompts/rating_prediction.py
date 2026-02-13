# Predict the rating r_ui for an unseen item given the agent's persona,
# context, interaction history, and relevant past experiences.
# Returns the rating on the domain's native scale with a brief justification.

RATING_PREDICTION_PROMPT = """You are predicting your rating for a {item_type} you haven't fully experienced yet.

## User Profile
- Persona: {persona}
- Preferences: {preferences}

## Current Context
- Time: {time_context}
- Location: {location_context}
- Situation: {situational_context}
- Constraints: {constraint_context}

## Item Information
- Name: {item_name}
- Category: {item_category}
- Attributes: {item_attributes}
- Description: {item_description}

## Relevant History
{relevant_history}

## Your Past Rating Distribution
{rating_distribution}

## Task
Predict the rating you would give this {item_type} on a scale of {rating_scale}.

## Reasoning Steps
1. How well does this {item_type} match your known preferences?
2. How does it compare to similar {item_type}s you have rated before?
3. How does your current context (time, location, situation) influence your perception?
4. Which specific attributes of this {item_type} would you enjoy or dislike?
5. Given all the above, what rating is consistent with your past rating pattern?

## Output Format
Return a JSON object:
```json
{{
  "thought": "<first-person reasoning through the steps above, 40-80 words>",
  "predicted_rating": <integer on {rating_scale}>
}}
```

Important: Your rating should be consistent with your past rating distribution. If you typically rate most {item_type}s between 3 and 4, do not suddenly give a 5 without strong justification.
"""
