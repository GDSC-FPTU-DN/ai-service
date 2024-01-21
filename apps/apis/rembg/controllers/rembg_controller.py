import requests
import rembg
import io


async def rembg_controller(image: bytes):
    # Remove background
    image = rembg.remove(image)
    # Return image
    return io.BytesIO(image)


def download_image(image_url: str):
    # Download image
    return io.BytesIO(requests.get(image_url).content)
