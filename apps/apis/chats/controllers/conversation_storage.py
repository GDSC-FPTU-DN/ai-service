import uuid
from utils.local_storage import read_from_local, save_to_local, remove_from_local
from utils.constants import DATA_DIR


def is_conversation_storage_exist(id: str) -> bool:
    # Check if conversation exist
    return read_from_local(f"{id}.json", DATA_DIR) is not None


def get_conversation_storage(id: str) -> list:
    # Get conversation
    conversation = read_from_local(f"{id}.json", DATA_DIR)
    # Return conversation
    return conversation


def create_conversation_storage() -> str:
    # Generate conversation id
    conversation_id = str(uuid.uuid4())
    # Save to local
    save_to_local([], f"{conversation_id}.json", False, DATA_DIR)
    # Return conversation id
    return conversation_id


def update_conversation_storage(id: str, role: str, message: str) -> list:
    # Get conversation
    conversation = get_conversation_storage(id)
    # Append new message
    conversation.append({
        "role": role,
        "content": message
    })
    # Save to local
    save_to_local(conversation, f"{id}.json", False, DATA_DIR)
    # Return conversation
    return conversation


def delete_conversation_storage(id: str):
    # Delete conversation
    remove_from_local(f"{id}.json", DATA_DIR)
