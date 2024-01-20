from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from apps.services.foward.fw_middleware import forward_request, forward_middleware
from .models.fd_model import FaceDetectionModel
from .controllers.fd_controller import faces_detection_controller


router = APIRouter(prefix='/fd')
router_base_configs = {
    "tags": ["fd"],
    "response_class": JSONResponse
}


# Face detection
@router.post("/", **router_base_configs)
async def faces_detection(
    image: FaceDetectionModel.image = FaceDetectionModel.image_default,
    fw_index: FaceDetectionModel.fw_index = Depends(forward_middleware)
):
    # Forward request
    fw_data = {
        "files": {"image": image.file}
    }
    fw_response = forward_request(fw_index, fw_data, '/api/fd/')
    if fw_response is not None:
        return JSONResponse({
            "faces": fw_response["data"]["faces"]
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
    detected_faces = faces_detection_controller(image_bytes)
    return JSONResponse({"faces": detected_faces})
