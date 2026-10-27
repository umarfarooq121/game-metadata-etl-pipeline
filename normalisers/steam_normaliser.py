
from normalisers.game_model import create_game


def normalise_steam(game):

    price_info = game.get("price_overview") or {}

    # Steam prices are stored in cents
    price_cents = price_info.get("final")

    price = (
        price_cents / 100
        if isinstance(price_cents, (int, float))
        and not isinstance(price_cents, bool)
        else None
    )

    rating = game.get("review_score_pct")

    user_rating = (
        rating / 20
        if isinstance(rating, (int, float))
        and not isinstance(rating, bool)
        else None
    )

    return create_game(
        title=game.get("name"),
        genre=(game.get("genres") or [None])[0],
        developer=(game.get("developers") or [None])[0],
        publisher=(game.get("publishers") or [None])[0],
        release_date=game.get("release_date"),
        image_url=game.get("header_image"),

        # New fields
        source_id=game.get("source_id"),
        platform="Steam",
        price=price,
        currency=price_info.get("currency"),
        user_rating=user_rating,
        age_rating=game.get("required_age_label")
    )

