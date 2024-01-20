from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/img2text')
router_base_configs = {
    "tags": ["img2text"],
    "response_class": JSONResponse
}


# Image to text
@router.post("/", **router_base_configs)
def image_to_text():
    return {"caption": "Hello World"}
