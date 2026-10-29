from database.db_connection import get_connection


def insert_game(game):
    query = """
        INSERT INTO public.games (
            source_id, platform, title, genre,
            developer, publisher, release_date,
            price, currency, user_rating, age_rating,
            image_url, resolved_image_url, local_image_path
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s
        )
        ON CONFLICT (platform, source_id) DO NOTHING
        RETURNING id;
    """

    values = (
        game["source_id"],
        game["platform"],
        game["title"],
        game["genre"],
        game["developer"],
        game["publisher"],
        game["release_date"],
        game["price"],
        game["currency"],
        game["user_rating"],
        game["age_rating"],
        game["image_url"],
        game.get("resolved_image_url"),
        game.get("local_image_path"),
    )

    with get_connection() as conn:
        result = conn.execute(query, values).fetchone()
        game_id = result[0] if result else None

    return game_id