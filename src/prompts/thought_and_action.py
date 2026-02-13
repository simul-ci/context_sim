# Generate an internal thought weighing available actions against persona, context,
# preferences, and prior interactions, then select the next action.
# Outputs a THOUGHT (reasoning trace) followed by the chosen ACTION.

THOUGHT_AND_ACTION_PROMPT = """You are a user interacting with a {item_type} recommender system. Decide your next action.

## User Profile
- Persona: {persona}
- Preferences: {preferences}
- Current Goals: {goals}

## Current Context
- Time: {time_context}
- Location: {location_context}
- Situation: {situational_context}
- Constraints: {constraint_context}

## Internal State
- Fatigue: {fatigue}
- Curiosity: {curiosity}
- Boredom: {boredom}

## Current Page
{current_page}

## Screening Results
{screening_results}

## Session History
{session_history}

## Relevant Memory
{episodic_memory}

## Available Actions
{available_actions}

## Task
First, think through your options. Then select the best action for your current situation.

## Instructions
1. Consider your goals and how each available action advances them.
2. Factor in your internal state (high fatigue or boredom may push toward exiting).
3. Evaluate your constraints (time, budget).
4. Think about what a person with your persona would naturally do next.
5. Choose one action from the available actions.

## Output Format
Return a JSON object:
```json
{{
  "thought": "<first-person deliberation weighing the options, 50-80 words>",
  "action": "<action from available_actions>",
  "action_parameters": {{}}
}}
```

The thought should sound like natural internal speech and must lead logically to the chosen action.
"""
