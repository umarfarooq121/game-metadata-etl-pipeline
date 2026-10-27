from urllib.parse import urlparse


def validate_image_url(image_url):

    # Check if the URL is missing or empty
    if not isinstance(image_url, str) or not image_url.strip():
        return False

    # Parse the URL into its components
    parsed_url = urlparse(image_url)

    # Check protocol and domain
    if parsed_url.scheme not in ["http", "https"]:
        return False

    if not parsed_url.hostname:
        return False

    return True
