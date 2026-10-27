def create_game(
    title,
    genre,
    developer,
    publisher,
    release_date,
    image_url,
    source_id=None,
    platform=None,
    price=None,
    currency=None,
    user_rating=None,
    age_rating=None
):
    return {
        "title": title,
        "genre": genre,
        "developer": developer,
        "publisher": publisher,
        "release_date": release_date,
        "image_url": image_url,
        "source_id": source_id,
        "platform": platform,
        "price": price,
        "currency": currency,
        "user_rating": user_rating,
        "age_rating": age_rating
    }
