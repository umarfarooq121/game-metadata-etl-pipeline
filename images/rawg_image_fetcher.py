
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")


def fetch_game_image(game_title):

    url = "https://api.rawg.io/api/games"

    params = {
        "key": API_KEY,
        "search": game_title,
        "search_precise": "true",
        "page_size": 5
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    results = response.json().get("results", [])

    # Match exact game titles first
    for game in results:
        if game["name"].casefold() == game_title.casefold():
            return game.get("background_image")

    return None


if __name__ == "__main__":

    image_url = fetch_game_image("Elden Ring")

    print("Image URL:", image_url)
