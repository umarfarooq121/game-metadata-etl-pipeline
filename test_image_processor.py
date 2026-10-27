from images.image_processor import validate_image_url

test_urls = [
    "https://example.com/images/elden-ring.jpg",
    "not-a-valid-url",
    "",
    None,
    "ftp://example.com/image.png"
]

for url in test_urls:
    result = validate_image_url(url)
    print(f"{url} -> {result}")
