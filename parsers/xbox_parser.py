
import xml.etree.ElementTree as ET

def parse_xbox():

    tree = ET.parse("feeds/xbox_games.xml")
    root = tree.getroot()

    feed_info = {
        "feed_version": root.get("feedVersion"),
        "generated_on": root.get("generatedOn"),
        "dataset": root.get("dataset")
    }

    games = []

    for product in root.findall("Product"):

        game = {
            "sku": product.get("sku"),
            "name": product.findtext("ProductName"),
            "genre": product.findtext("Category"),
            "developer": product.findtext("Studio"),
            "publisher": product.findtext("Distributor"),
            "release_date": product.findtext("LaunchDate"),
            "image_url": product.findtext("Artwork"),
            "price": product.findtext("RetailPrice"),
            "currency": product.findtext("CurrencyCode"),
            "user_rating": product.findtext("CustomerScore"),
            "age_rating": product.findtext("AgeClassification"),

        }

        games.append(game)

    return feed_info, games


if __name__ == "__main__":

    feed_info, games = parse_xbox()

    print(feed_info)
    print(f"Games found: {len(games)}")

    for game in games[:3]:
        print(game)
