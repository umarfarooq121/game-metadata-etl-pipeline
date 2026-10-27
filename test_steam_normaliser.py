from parsers.steam_parser import parse_steam
from normalisers.steam_normaliser import normalise_steam

feed_info, games = parse_steam()

for game in games[:3]:  # Limit to first 3 games for testing
    normalised_game = normalise_steam(game)
    print(normalised_game)