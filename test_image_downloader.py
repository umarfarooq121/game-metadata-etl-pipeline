from images.rawg_image_fetcher import fetch_game_image
from images.image_downloader import download_image


game_title = "Elden Ring"

# Step 1: Retrieve real image URL from RAWG
image_url = fetch_game_image(game_title)

print("RAWG Image URL:", image_url)

# Step 2: Download the image
if image_url:

    saved_path = download_image(
        image_url=image_url,
        game_id="elden-ring-test",
        platform="Steam"
    )

    print("Saved image:", saved_path)

else:
    print("No matching image found")
