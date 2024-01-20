from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/fd')
router_base_configs = {
    "tags": ["fd"],
    "response_class": JSONResponse
}


# Face detection
@router.post("/", **router_base_configs)
def faces_detection():
    return {"faces": "Hello World"}
