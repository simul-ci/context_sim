# Evaluate each item on the current recommendation page and produce
# [WATCH] or [SKIP] intentions based on alignment with the user's
# persona, context, preferences, and episodic memory.

ITEM_SCREENING_PROMPT = """You are a user browsing a {item_type} recommendation page. Screen the items on this page.

## User Profile
- Persona: {persona}
- Preferences: {preferences}
- Current Goals: {goals}

## Current Context
- Time: {time_context}
- Location: {location_context}
- Situation: {situational_context}
- Constraints: {constraint_context}

## Current Page
{page_content}

## Relevant Memory
{episodic_memory}

## Task
For each item on the current page, estimate its alignment with your persona, your current context, and your past interactions from memory. Then assign a [WATCH] (interested, would consider engaging further) or [SKIP] (not interested) intention.

## Instructions
- Use ONLY the items visible on the current page.
- Use the item identifiers exactly as written in the page content.
- For each item, briefly explain how it aligns or conflicts with your persona, context, or memory.
- Be selective — a realistic user skips most items.

## Output Format
ITEM-DECISIONS:
- <item_id>: [WATCH] <reason grounded in persona, context, or memory>
- <item_id>: [SKIP] <reason grounded in persona, context, or memory>
CANDIDATES: <comma-separated item_ids of [WATCH] items, or NONE>
"""
