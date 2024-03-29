from typing import Any, Literal
import requests
from fastapi import HTTPException
from .fw_storage import get_fw_destinations, update_fw_destination


def verify_fw_resources(url: str) -> bool:
    # Verify forward destination resources logger
    print("Verifying resources on", url)
    try:
        response = requests.get(url + '/health')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


async def forward_middleware(fw: str = None):
    # Verify forward destination index
    try:
        if fw != 'auto' and fw is not None:
            fw = int(fw)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Invalid forward destination")

    # If forward destination is auto, get the destination with the least tasks
    fw_destinations = get_fw_destinations()
    if fw == 'auto':
        if len(fw_destinations) != 0:
            # Sort resources by tasks
            fw_destinations.sort(key=lambda x: x['tasks'])
            # Verify forward destination resources
            fw = None
            for i in range(0, len(fw_destinations)):
                is_resource_available = verify_fw_resources(
                    fw_destinations[i]['url'])
                if is_resource_available:
                    fw = i
                    break
            # Update forward destination tasks
            if fw is not None:
                update_fw_destination(fw, fw_destinations[fw]['tasks'] + 1)
        else:
            fw = None
    # If forward destination is not auto, update forward destination tasks
    else:
        if fw is not None:
            update_fw_destination(fw, fw_destinations[fw]['tasks'] + 1)
    return fw


def forward_request(fw_index: int, data: Any, endpoint: str = '', method: Literal['GET', 'POST', 'PUT', 'DELETE'] = 'POST'):
    # Logger
    # Return None if fw_index is None
    if fw_index is None:
        return None
    # Get forward destination url
    print("Forwarding request to", fw_index, endpoint)
    fw_destinations = get_fw_destinations()
    fw_url = fw_destinations[fw_index]['url'] + endpoint
    # Call request
    try:
        if method == 'GET':
            response = requests.get(fw_url)
        elif method == 'POST':
            response = requests.post(fw_url, **data)
        elif method == 'PUT':
            response = requests.put(fw_url, **data)
        elif method == 'DELETE':
            response = requests.delete(fw_url, **data)
        else:
            raise HTTPException(
                status_code=400, detail="Invalid request method on forwarding request")
    except Exception as e:
        print("Forwarding Error: ", e)
        response = None
    if response is not None and response.status_code != 200:
        response = None
    # Update forward destination tasks
    update_fw_destination(fw_index, fw_destinations[fw_index]['tasks'] - 1)
    # Return response
    return response.json() if response is not None else None
