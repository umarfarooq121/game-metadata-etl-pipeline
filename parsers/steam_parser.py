import json

def parse_steam():

    with open("feeds/steam_games.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    feed_info = {
        "feed_name": data["feed_name"],
        "generated_on": data["generated_on"],
        "note": data["note"]
    }

    games = data["games"]

    return feed_info, games


if __name__ == "__main__":

    feed_info, games = parse_steam()

    print(feed_info)
    print(f"Games found: {len(games)}")

    for game in games:
        print(game["name"])
        print(game["genres"])
        print(game["release_date"])