# String templates that render the RS environment state as text for the agent.
# Two formats: recommendation domains (MovieLens, AmazonBook, Steam) and
# web-shopping (OPeRA). These are NOT LLM prompts — they feed into
# {page_content} / {current_page} placeholders in interaction prompts.

# Recommendation Domains
RECOMMENDATION_PAGE_FORMAT = """PAGE {page_number}
CONTEXT: {user_context}
{item_rows}
"""

# Each item row follows this pattern:
RECOMMENDATION_ITEM_ROW = """<- {item_title} -> <- History ratings: {item_rating} -> <- Summary: {item_description} ->"""

# Web-Shopping Domains (OPeRA)
SHOPPING_PAGE_FORMAT = """PAGE {page_number}
USER CONTEXT: {user_context}
CONTEXT: {page_context}
PRODUCTS:
{product_rows}
INTERACTIVE ELEMENTS (semantic IDs):
{semantic_ids}
"""

# Each product row follows this pattern:
SHOPPING_PRODUCT_ROW = """<- {product_title} -> <- Price: {price} -> <- Details: {short_description} ->"""
