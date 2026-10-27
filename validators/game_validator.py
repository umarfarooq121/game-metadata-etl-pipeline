from images.image_processor import validate_image_url
from datetime import datetime
import math


def validate_game(game):

    errors = []

    # Rule 1: Title
    if not isinstance(game.get("title"), str) or not game["title"].strip():
        errors.append("Missing or invalid game title")

    # Rule 2: Genre
    if not isinstance(game.get("genre"), str) or not game["genre"].strip():
        errors.append("Missing or invalid genre")

    # Rule 3: Release date
    release_date = game.get("release_date")

    if not release_date:
        errors.append("Missing release date")
    else:
        try:
            datetime.strptime(str(release_date), "%Y-%m-%d")

            if not isinstance(release_date, str) or \
               release_date != datetime.strptime(
                   release_date, "%Y-%m-%d"
               ).strftime("%Y-%m-%d"):
                errors.append("Invalid release date format")

        except (ValueError, TypeError):
            errors.append("Invalid release date")

    # Rule 4: Source ID
    source_id = game.get("source_id")

    if source_id is None or isinstance(source_id, str) and not source_id.strip():
        errors.append("Missing source ID")

    # Rule 5: Platform
    if game.get("platform") not in ["Steam", "Xbox", "PlayStation"]:
        errors.append("Invalid platform")

    # Rule 6: Price
    price = game.get("price")

    if price is None:
        errors.append("Missing or invalid price")
    elif isinstance(price, bool) or not isinstance(price, (int, float)):
        errors.append("Price must be numeric")
    elif not math.isfinite(price) or price < 0:
        errors.append("Invalid price")

    # Rule 7: Currency
    if game.get("currency") not in ["USD", "EUR", "GBP", "PLN"]:
        errors.append("Unsupported currency")

    # Rule 8: User rating
    rating = game.get("user_rating")

    if rating is not None:
        if isinstance(rating, bool) or not isinstance(rating, (int, float)):
            errors.append("Rating must be numeric")
        elif not math.isfinite(rating) or not 0 <= rating <= 5:
            errors.append("Rating must be between 0 and 5")
    # Rule 9: Image URL validation
    image_url = game.get("image_url")

    if not validate_image_url(image_url):
        errors.append("Missing or invalid image URL")

    return errors

