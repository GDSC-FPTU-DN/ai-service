from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from apps.services.foward.fw_middleware import forward_middleware, forward_request
from .models.vqa_model import VQAModel


router = APIRouter(prefix='/vqa')
router_base_configs = {
    "tags": ["vqa"],
    "response_class": JSONResponse
}


@router.post("/", **router_base_configs)
async def vision_question_answer(
    image: VQAModel.image = VQAModel.image_default,
    question: VQAModel.question = VQAModel.question_default,
    fw_index: VQAModel.fw_index = Depends(forward_middleware)
):
    # Forward request
    fw_data = {
        "files": {"image": image.file},
        "data": {"question": question}
    }
    fw_response = forward_request(fw_index, fw_data, '/api/vqa/')
    if fw_response is not None:
        return {"answer": fw_response}

    return {"answer": "VQA model is not available in this server"}
