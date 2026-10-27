from parsers.xbox_parser import parse_xbox
from normalisers.xbox_normaliser import normalise_xbox

feed_info, games = parse_xbox()

print("Feed information:", feed_info)

for game in games[:3]:
    normalised_game = normalise_xbox(game)
    print(normalised_game)