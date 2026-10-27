from parsers.playstation_parser import parse_playstation
from normalisers.playstation_normaliser import normalise_playstation

games = parse_playstation()

print(f"total games found: {len(games)}")

for game in games[:3]:  # Limit to first 3 games for testing
    normalised_game = normalise_playstation(game)
    print(normalised_game)
