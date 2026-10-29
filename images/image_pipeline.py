from pathlib import Path

from images.rawg_image_fetcher import fetch_game_image
from images.image_downloader import download_image
from images.image_manifest import (
    load_image_manifest,
    save_image_manifest,
)


def process_game_images(valid_games):
    manifest = load_image_manifest()

    successful = 0
    failed = 0

    for game in valid_games:
        title = game["title"]
        platform = game["platform"]
        source_id = game["source_id"]

        manifest_key = f"{platform}:{source_id}"

        print(f"\nProcessing image: {title} ({platform})")

        image_folder = Path("images/downloads") / platform.lower()

        existing_images = [
            path for path in image_folder.glob(f"{source_id}.*")
            if path.suffix.lower() in {".jpg", ".png", ".webp"}
        ]

        # Reuse an existing image and restore its saved URL
        if existing_images:
            game["local_image_path"] = str(existing_images[0])

            saved_metadata = manifest.get(manifest_key, {})
            saved_url = saved_metadata.get("resolved_image_url")

            if saved_url:
                game["resolved_image_url"] = saved_url
                print("Restored image URL from manifest")
            else:
                print("Existing image has no saved URL in manifest")

            print(f"Image already exists: {existing_images[0]}")
            continue

        try:
            # Find artwork using RAWG
            image_url = fetch_game_image(title)

            if not image_url:
                print("No image found")
                failed += 1
                continue

            # Download the image
            saved_path = download_image(
                image_url=image_url,
                game_id=source_id,
                platform=platform,
            )

            if saved_path:
                game["resolved_image_url"] = image_url
                game["local_image_path"] = saved_path

                # Remember metadata for future runs
                manifest[manifest_key] = {
                    "resolved_image_url": image_url,
                    "local_image_path": saved_path,
                }

                save_image_manifest(manifest)

                successful += 1
                print(f"Saved: {saved_path}")

            else:
                failed += 1

        except Exception as error:
            failed += 1
            print(f"Image processing failed: {error}")

    return {
        "successful": successful,
        "failed": failed,
    }
