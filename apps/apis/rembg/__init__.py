from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from apps.services.foward.fw_middleware import forward_middleware, forward_request
from .models.rembg_model import RembgModel
from .controllers.rembg_controller import rembg_controller, download_image
from utils.local_storage import save_to_local, remove_from_local_with_expire

router = APIRouter(prefix='/rembg')
router_base_configs = {
    "tags": ["rembg"],
    "response_class": JSONResponse,
}


# Remove background
@router.post("/", **router_base_configs)
async def remove_background(
    image: RembgModel.image = RembgModel.image_default,
    stream: RembgModel.stream = RembgModel.stream_default,
    expire: RembgModel.expire = RembgModel.expire_default,
    fw_index: RembgModel.fw_index = Depends(forward_middleware)
):
    # Forward request
    fw_data = {
        "files": {"image": image.file}
    }
    fw_response = forward_request(fw_index, fw_data, '/api/rembg/')
    if fw_response is not None:
        if RembgModel.stream_parser(stream):
            # Read image
            image_bytes = download_image(fw_response["data"]['image'])
            return StreamingResponse(image_bytes, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment;filename={image.filename}"})
        return JSONResponse({
            "message": "Image is processed successfully",
            "access_link": fw_response["data"]['image']
        })

    # Check if image is None
    if image is None:
        raise HTTPException(status_code=400, detail="Image is required")
    # Check if image is empty
    if image.filename == '':
        raise HTTPException(status_code=400, detail="Image is empty")
    # Read image
    image_bytes = await image.read()
    # Process image
    processed_image = await rembg_controller(image_bytes)
    # If stream is True, return StreamingResponse
    if RembgModel.stream_parser(stream):
        return StreamingResponse(processed_image, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment;filename={image.filename}"})
    # If stream is False, save locally and return access link
    local_path = save_to_local(processed_image.read(), image.filename)
    # Automatic delete file
    remove_from_local_with_expire(local_path, expire)
    # Return access link
    return JSONResponse({
        "message": "Image is processed successfully",
        "access_link": local_path
    })
