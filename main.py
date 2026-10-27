from parsers.steam_parser import parse_steam
from parsers.xbox_parser import parse_xbox
from parsers.playstation_parser import parse_playstation

from normalisers.steam_normaliser import normalise_steam
from normalisers.xbox_normaliser import normalise_xbox
from normalisers.playstation_normaliser import normalise_playstation

from validators.game_validator import validate_game


def main():

    # Step 1: Parse source feeds
    steam_info, steam_games = parse_steam()
    xbox_info, xbox_games = parse_xbox()
    playstation_games = parse_playstation()

    # Step 2: Normalise each platform
    steam_normalised = [
        normalise_steam(game) for game in steam_games
    ]

    xbox_normalised = [
        normalise_xbox(game) for game in xbox_games
    ]

    playstation_normalised = [
        normalise_playstation(game) for game in playstation_games
    ]

    # Step 3: Combine datasets
    all_games = (
        steam_normalised
        + xbox_normalised
        + playstation_normalised
    )

    

    # Step 4: Validate with source tracking

    valid_games = []
    rejected_games = []
    seen_games = set()

    source_files = {
        "Steam": "steam_games.json",
        "Xbox": "xbox_games.xml",
        "PlayStation": "playstation_games.xlsx"
    }

    for game in all_games:

        errors = validate_game(game)

        platform = game.get("platform")
        source_id = game.get("source_id")
        
        # Create a unique identifier for each listing
        game_key = (platform, str(source_id))

        # Check for duplicates
        if source_id is not None and str(source_id).strip():

            if game_key in seen_games:
                errors.append("Duplicate game record")
            else:
                seen_games.add(game_key)

        # Separate accepted and rejected records
        if not errors:
            valid_games.append(game)
        else:
            rejected_games.append({
                "source_file": source_files.get(platform),
                "platform": platform,
                "source_id": source_id,
                "title": game.get("title"),
                "errors": errors
        })

    # Step 5: Display results

    print("\n--- VALIDATION SUMMARY ---")
    print("Total records:", len(all_games))
    print("Valid records:", len(valid_games))
    print("Rejected records:", len(rejected_games))

    for record in rejected_games:
        print("\n----------------------------")
        print("Source File:", record["source_file"])
        print("Platform:", record["platform"])
        print("Source ID:", record["source_id"])
        print("Game:", record["title"])
        print("Errors:", record["errors"])


if __name__ == "__main__":
    main()