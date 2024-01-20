from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request

router = APIRouter(prefix='/chats')
router_base_configs = {
    "tags": ["chats"],
    "response_class": JSONResponse
}


# Message
@router.post("/:conversation_id", **router_base_configs)
def message():
    return {"message": "Hello World"}


# Get conversations
@router.get("/get", **router_base_configs)
def get_conversations():
    return {"conversations": "Hello World"}


# Create conversation
@router.post("/create", **router_base_configs)
def create_conversation():
    return {"conversation_id": "Hello World"}


# Delete conversation
@router.delete("/delete", **router_base_configs)
def delete_conversation():
    return {"conversation": "Hello World"}
