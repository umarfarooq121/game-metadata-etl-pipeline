from images.rawg_image_fetcher import fetch_game_image
from images.image_downloader import download_image
from pathlib import Path


def process_game_images(valid_games):

    successful = 0
    failed = 0
    

    for game in valid_games:

        title = game["title"]
        platform = game["platform"]
        source_id = game["source_id"]

        print(f"\nProcessing image: {title} ({platform})")
        image_folder = Path("images/downloads") / platform.lower()
        existing_images = [
                path for path in image_folder.glob(f"{source_id}.*")
                if path.suffix.lower() in {".jpg", ".png", ".webp"}
            ]
        
        if existing_images:
            game["local_image_path"] = str(existing_images[0])
            print(f"Image already exists: {existing_images[0]}")
            continue

        try:
            # Step 1: Get real image URL from RAWG
            image_url = fetch_game_image(title)

            if not image_url:
                print("No image found")
                failed += 1
                continue

            # Step 2: Download and save image
            saved_path = download_image(
                image_url=image_url,
                game_id=source_id,
                platform=platform
            )

            if saved_path:
                game["resolved_image_url"] = image_url
                game["local_image_path"] = saved_path

                successful += 1
                print(f"Saved: {saved_path}")

            else:
                failed += 1

        except Exception as error:
            failed += 1
            print(f"Image processing failed: {error}")

    return {
        "successful": successful,
        "failed": failed
    }
