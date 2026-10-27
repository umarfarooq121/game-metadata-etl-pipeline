import json
from pathlib import Path
from datetime import datetime, date


def save_validation_results(valid_games, rejected_games):

    # Create the output folder if it doesn't exist
    output_folder = Path("logs/output")
    output_folder.mkdir(parents=True, exist_ok=True)

    # Convert date objects into strings for JSON
    def json_converter(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError(f"Cannot serialize {type(obj)}")

    # Prepare individual error records
    validation_errors = []

    for record in rejected_games:
        for error in record["errors"]:
            validation_errors.append({
                "source_file": record.get("source_file"),
                "platform": record.get("platform"),
                "source_id": record.get("source_id"),
                "title": record.get("title"),
                "error": error
            })

    # Save three JSON files
    files = {
        "valid_games.json": valid_games,
        "rejected_games.json": rejected_games,
        "validation_errors.json": validation_errors
    }

    for filename, data in files.items():
        file_path = output_folder / filename

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
                default=json_converter
            )

        print(f"Saved: {file_path}")
