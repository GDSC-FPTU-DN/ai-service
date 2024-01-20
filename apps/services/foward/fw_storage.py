from utils.local_storage import read_from_local, save_to_local


FOWARD_JSON_FILE = 'forward.json'


def get_fw_destinations() -> list:
    destinations = read_from_local(FOWARD_JSON_FILE)
    if destinations is None:
        return []
    return destinations


def append_fw_destination(url: str):
    # Remove the last / if exist
    if url[-1] == '/':
        url = url[:-1]
    # Get forward destinations
    forward_destinations = get_fw_destinations()
    # Append new destination
    forward_destinations.append({
        "tasks": 0,
        "url": url
    })
    # Save to local
    save_to_local(forward_destinations, FOWARD_JSON_FILE, False)
    # Return index
    return len(forward_destinations) - 1


def update_fw_destination(index: int, tasks: int):
    # Get forward destinations
    forward_destinations = get_fw_destinations()
    # Update destination
    forward_destinations[index]['tasks'] = tasks
    # Save to local
    save_to_local(forward_destinations, FOWARD_JSON_FILE, False)


def delete_fw_destination(index: int):
    # Get forward destinations
    forward_destinations = get_fw_destinations()
    # Delete destination
    del forward_destinations[index]
    # Save to local
    save_to_local(forward_destinations, FOWARD_JSON_FILE, False)
