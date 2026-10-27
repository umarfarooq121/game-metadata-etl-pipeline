
from normalisers.game_model import create_game


def normalise_xbox(game):

    # Convert numeric strings into numbers
    try:
        price = float(game["price"]) if game.get("price") else None
    except (ValueError, TypeError):
        price = None

    try:
        user_rating = (
            float(game["user_rating"])
            if game.get("user_rating") else None
        )
    except (ValueError, TypeError):
        user_rating = None

    return create_game(
        title=game.get("name"),
        genre=game.get("genre"),
        developer=game.get("developer"),
        publisher=game.get("publisher"),
        release_date=game.get("release_date"),
        image_url=game.get("image_url"),

        # New fields
        source_id=game.get("sku"),
        platform="Xbox",
        price=price,
        currency=game.get("currency"),
        user_rating=user_rating,
        age_rating=game.get("age_rating")
    )
