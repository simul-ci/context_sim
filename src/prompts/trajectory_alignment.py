# Trajectory Alignment — generate a self-reflection explaining why the user's
# chosen action is preferred over K alternatives, grounded in persona and context.
# The output is collected into D_TA and used for SFT training.

TRAJECTORY_ALIGNMENT_PROMPT = """You are a reasoning system that explains why a user's choice is optimal given alternatives.

## User Profile
- Persona: {persona}
- Preferences: {preferences}
- Current Goals: {goals}

## Current Context
- Time: {time_context}
- Location: {location_context}
- Situation: {situational_context}
- Constraints: {constraint_context}

## Current State
{current_state}

## Interaction History (this session)
{session_history}

## User's Choice
{expert_action}

## Alternative Actions Available
{alternative_actions}

## Task
Generate a first-person self-reflection explaining why this choice is best for THIS user in THIS context. The reflection must:
1. State the user's current situation and immediate need.
2. Explain why each alternative does not fit as well — be specific, reference persona or context.
3. Explain why the chosen action optimally satisfies the current need, aligned with persona and history.
4. Conclude with a clear statement of optimality.

## Output Format
Return a JSON object:
```json
{{
  "self_reflection": "<first-person reasoning, 80-150 words>"
}}
```

Example style: "Let me think through the best choice here. I'm currently [context/situation] and looking for [goal]. [Alternative 1] doesn't fit well because [specific reason tied to persona/preferences]. [Alternative 2] is not ideal because [reason]. [Chosen action] is the best option because [alignment with persona, preferences, and current context]. Therefore, [chosen action] is optimal."

CRITICAL: The reflection must explicitly compare alternatives, not just justify the choice. Ground every comparison in the user's persona, preferences, history, or current context.
"""
