# Per-domain settings for the 4 supported datasets (MovieLens, AmazonBook, Steam, OPeRA).
# These configs supply values for placeholders like {item_type}, {rating_scale},
# and {available_actions} across all prompt templates.

RECOMMENDATION_ACTIONS = [
    "[NEXT_PAGE]",
    "[PREVIOUS_PAGE]",
    "[CLICK_ITEM:<item_id>]",
    "[SEARCH]",
    "[RATE]",
    "[EXIT]",
]

DOMAIN_CONFIGS = {
    "movielens": {
        "name": "MovieLens",
        "item_type": "movie",
        "rating_scale": "1-5 stars",
        "rating_guidelines": (
            "1 star: Terrible, regret watching\n"
            "2 stars: Poor, significant flaws\n"
            "3 stars: Average, neither good nor bad\n"
            "4 stars: Good, enjoyed it\n"
            "5 stars: Excellent, highly recommend"
        ),
        "available_actions": RECOMMENDATION_ACTIONS,
        "item_attributes": ["title", "year", "genre", "director", "cast", "runtime"],
        "example_categories": ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Documentary"],
    },
    "amazonbook": {
        "name": "AmazonBook",
        "item_type": "book",
        "rating_scale": "1-5 stars",
        "rating_guidelines": (
            "1 star: Did not finish, waste of time\n"
            "2 stars: Struggled through, few redeeming qualities\n"
            "3 stars: Okay read, nothing special\n"
            "4 stars: Good read, would recommend to right audience\n"
            "5 stars: Outstanding, must-read"
        ),
        "available_actions": RECOMMENDATION_ACTIONS,
        "item_attributes": ["title", "author", "genre", "publication_year", "page_count"],
        "example_categories": ["Fiction", "Non-Fiction", "Mystery", "Biography", "Self-Help", "Science", "History"],
    },
    "steam": {
        "name": "Steam",
        "item_type": "video game",
        # Steam uses recommend/not-recommend + text reviews natively.
        # The paper reports RMSE/MAE, implying numeric conversion.
        "rating_scale": "recommend / not recommend",
        "rating_guidelines": (
            "recommend: You would recommend this game to others\n"
            "not recommend: You would not recommend this game"
        ),
        "available_actions": RECOMMENDATION_ACTIONS,
        "item_attributes": ["title", "developer", "genre", "release_date", "price"],
        "example_categories": ["Action", "RPG", "Strategy", "Indie", "Simulation", "Sports", "Puzzle"],
    },
    "opera": {
        "name": "OPeRA",
        "item_type": "product",
        "rating_scale": "1-5 stars",
        "rating_guidelines": (
            "1 star: Defective or useless\n"
            "2 stars: Poor quality, not as described\n"
            "3 stars: Meets basic expectations\n"
            "4 stars: Good product, minor issues\n"
            "5 stars: Excellent, exceeded expectations"
        ),
        # OPeRA uses its own action space (semantic IDs for interactive
        # elements) extended with navigation actions.
        # See: wang2025opera for the full action definition.
        "available_actions": RECOMMENDATION_ACTIONS,
        "item_attributes": ["name", "brand", "category", "price", "rating", "reviews_count"],
        "example_categories": ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Toys", "Office"],
        "note": "OPeRA actions follow the OPeRA dataset action space, extended with navigation actions.",
    },
}
