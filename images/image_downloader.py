import requests
from pathlib import Path
from io import BytesIO
from PIL import Image


def download_image(image_url, game_id, platform):

    if not image_url:
        return None

    # Create a platform-specific folder
    folder = Path("images/downloads") / platform.lower()
    folder.mkdir(parents=True, exist_ok=True)

    try:
        # Download the image
        response = requests.get(image_url, timeout=20)
        response.raise_for_status()

        # Check that the response is an image
        content_type = response.headers.get("Content-Type", "")

        if not content_type.lower().startswith("image/"):
            print("Invalid image content type")
            return None

        # Verify and decode image bytes
        with Image.open(BytesIO(response.content)) as image:
            image.load()
            image_format = image.format

            # Allow common image formats
            if image_format not in ["JPEG", "PNG", "WEBP"]:
                print("Unsupported image format")
                return None

            extension = {
                "JPEG": ".jpg",
                "PNG": ".png",
                "WEBP": ".webp"
            }[image_format]

            # Save the image using a standard format
            safe_id = "".join(
                c for c in str(game_id)
                if c.isalnum() or c in "-_"
            )

            if not safe_id:
                return None

            file_path = folder / f"{safe_id}{extension}"

            image.save(file_path)

        return str(file_path)

    except (requests.RequestException, OSError, ValueError) as error:
        print(f"Image download failed: {error}")
        return None
