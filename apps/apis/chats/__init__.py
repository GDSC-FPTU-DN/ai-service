from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from .models.chats_model import ChatsModel
from .controllers.conversation_storage import is_conversation_storage_exist, get_conversation_storage, create_conversation_storage, delete_conversation_storage, update_conversation_storage
from .controllers.openai_controller import send_message, send_message_conversation
from apps.services.foward.fw_middleware import forward_request, forward_middleware

router = APIRouter(prefix='/chats')
router_base_configs = {
    "tags": ["chats"],
    "response_class": JSONResponse
}


# Message
@router.post("/", **router_base_configs)
def message(data: ChatsModel, fw_index=Depends(forward_middleware)):
    # Forward request
    fw_data = {
        "json": {"prompt": data.prompt}
    }
    fw_response = forward_request(fw_index, fw_data, '/api/chats/')
    if fw_response is not None:
        return {"message": fw_response["data"]["message"]}

    response = send_message(data.prompt, data.histories or [])
    return {"message": response}


# Message to conversation
@router.post("/{cid}", **router_base_configs)
def conversation(cid: str, data: ChatsModel, fw_index=Depends(forward_middleware)):
    is_exist = is_conversation_storage_exist(cid)
    if not is_exist:
        raise HTTPException(status_code=404, detail="Conversation not found")

    # Forward request
    fw_data = {
        "data": {"prompt": data.prompt, "conversation": get_conversation_storage(cid)}
    }
    fw_response = forward_request(fw_index, fw_data, f'/api/chats/{cid}')
    if fw_response is not None:
        # Update conversation
        update_conversation_storage(cid, "user", data.prompt)
        update_conversation_storage(
            cid, "assistant", fw_response["data"]["message"])
        return {"message": fw_response["data"]["message"]}

    response = send_message_conversation(cid, data.prompt)
    return {"message": response}


# Get conversation by id
@router.get("/{cid}", **router_base_configs)
def get_conversation(cid: str):
    is_exist = is_conversation_storage_exist(cid)
    if not is_exist:
        raise HTTPException(status_code=404, detail="Conversation not found")

    conversation = get_conversation_storage(cid)
    return {"conversation": conversation}


# Create conversation
@router.get("/create", **router_base_configs)
def create_conversation():
    cid = create_conversation_storage()
    return {"conversation_id": cid}


# Delete conversation
@router.delete("/delete/{cid}", **router_base_configs)
def delete_conversation(cid: str):
    delete_conversation_storage(cid)
    return {"conversation_id": cid}
