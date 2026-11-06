import json
import pathlib


def load_game_descriptions():
    file_path = pathlib.Path("feeds/game_descriptions.json")

    with open(file_path, "r", encoding="utf-8") as file:
        descriptions = json.load(file)

    return descriptions


if __name__ == "__main__":
    descriptions = load_game_descriptions()

    print(f"Descriptions loaded: {len(descriptions)}")

    for record in descriptions:
        print(record["title"], " - ", record["source_id"])