
from normalisers.game_model import create_game
from datetime import datetime, date


def normalise_playstation(game):

    # Convert Excel date objects into YYYY-MM-DD
    release_date = game.get("release_date")

    if isinstance(release_date, (datetime, date)):
        release_date = release_date.strftime("%Y-%m-%d")

    return create_game(
        title=game.get("name"),
        genre=game.get("genre"),
        developer=game.get("developer"),
        publisher=game.get("publisher"),
        release_date=release_date,
        image_url=game.get("image_url"),

        # New fields
        source_id=game.get("id"),
        platform="PlayStation",
        price=game.get("price"),
        currency=game.get("currency"),
        user_rating=game.get("user_rating"),
        age_rating=game.get("age_rating")
    )