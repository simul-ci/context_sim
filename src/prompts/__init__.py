# ContextSim Prompts — all prompt templates organized by pipeline stage.

# Persona Initialization
from .persona_candidate_generation import PERSONA_CANDIDATE_GENERATION_PROMPT
from .persona_consistency_scoring import PERSONA_CONSISTENCY_SCORING_PROMPT
from .preference_inference import PREFERENCE_INFERENCE_PROMPT
from .goal_inference import GOAL_INFERENCE_PROMPT

# Thought Synthesis (SFT training data)
from .item_disentanglement import ITEM_DISENTANGLEMENT_PROMPT
from .trajectory_alignment import TRAJECTORY_ALIGNMENT_PROMPT

# Life Simulation & Context
from .context_summarization import CONTEXT_SUMMARIZATION_PROMPT
from .engagement_check import ENGAGEMENT_CHECK_PROMPT

# RS Interaction Loop
from .item_screening import ITEM_SCREENING_PROMPT
from .internal_state import INTERNAL_STATE_PROMPT
from .thought_and_action import THOUGHT_AND_ACTION_PROMPT
from .action_reflection import ACTION_REFLECTION_PROMPT
from .rating_prediction import RATING_PREDICTION_PROMPT

# Evaluation
from .post_interview import POST_INTERVIEW_PROMPT
from .believability_evaluator import BELIEVABILITY_CHECK_PROMPT, LLM_EVALUATOR_PROMPT

# Environment Configuration
from .page_formats import (
    RECOMMENDATION_PAGE_FORMAT,
    RECOMMENDATION_ITEM_ROW,
    SHOPPING_PAGE_FORMAT,
    SHOPPING_PRODUCT_ROW,
)
from .domain_configs import DOMAIN_CONFIGS, RECOMMENDATION_ACTIONS
