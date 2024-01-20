import rembg
import io


async def rembg_controller(image: bytes):
    # Remove background
    image = rembg.remove(image)
    # Return image
    return io.BytesIO(image)
