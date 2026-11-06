import json
from pathlib import Path

from ai.description_loader import load_game_descriptions
from ai.game_enricher import enrich_game

def test_game_enrichment():
    descriptions = load_game_descriptions()

    record = descriptions[0]

    print("Enriching:", record["title"], flush=True)

    suggestions = enrich_game(record["description"])

    result = {
        "platform": record["platform"],
        "source_id": record["source_id"],
        "title": record["title"],
        "description": record["description"],
        "description_source": record["description_source"],
        "ai_suggestions": suggestions,
    }

    print(json.dumps(result, indent=4))    
    output_path = Path("logs/output/ai_enrichment_sample.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    print(f"Saved: {output_path}")
    


if __name__ == "__main__":
    test_game_enrichment()