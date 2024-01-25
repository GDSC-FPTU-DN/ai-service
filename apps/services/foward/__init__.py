from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models.fw_model import CreateFwDestinationModel, DeleteFwDestinationModel
from .fw_storage import get_fw_destinations, append_fw_destination, delete_fw_destination


router = APIRouter(prefix='/fw')
router_base_configs = {
    "tags": ["fw"],
    "response_class": JSONResponse
}


# Create foward destination
@router.post("/", **router_base_configs)
async def create_forward_destination(data: CreateFwDestinationModel):
    index = append_fw_destination(data.url)
    return {"fw_index": index}


# Delete foward destination
@router.delete("/", **router_base_configs)
async def delete_forward_destination(data: DeleteFwDestinationModel):
    delete_fw_destination(data.index)
    return {"fw_index": data.index}


# Get foward destinations
@router.get("/", **router_base_configs)
async def get_forward_destinations():
    return {"fw": get_fw_destinations()}
