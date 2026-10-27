from validators.game_validator import validate_game

bad_game = {
    "title": "",
    "genre": "RPG",
    "release_date": "2026-15-45",
    "source_id": None,
    "platform": "Steam",
    "price": -19.99,
    "currency": "XYZ",
    "user_rating": 8.5
}

errors = validate_game(bad_game)

for error in errors:
    print(error)

