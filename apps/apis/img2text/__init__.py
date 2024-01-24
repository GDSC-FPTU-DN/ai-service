from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from apps.services.foward.fw_middleware import forward_middleware, forward_request
from .models.img2text_model import Img2TextModel

router = APIRouter(prefix='/img2text')
router_base_configs = {
    "tags": ["img2text"],
    "response_class": JSONResponse
}


# Image to text
@router.post("/", **router_base_configs)
def image_to_text(
    image: Img2TextModel.image = Img2TextModel.image_default,
    fw_index: Img2TextModel.fw_index = Depends(forward_middleware)
):
    # Forward request
    fw_data = {
        "files": {"image": image.file}
    }
    fw_response = forward_request(fw_index, fw_data, '/api/img2text/')
    if fw_response is not None:
        return {"caption": fw_response["data"]["caption"]}

    return {"caption": "Image to Text model is not available in this server"}
