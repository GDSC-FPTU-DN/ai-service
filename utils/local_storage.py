from typing import Any
import os
import json
from threading import Timer
from .constants import TEMP_DIR, APP_DOMAIN


def parse_filename(filename: str):
    filename = filename.replace(' ', '_')
    filename = filename.replace('(', '')
    filename = filename.replace(')', '')
    filename = filename.replace('[', '')
    filename = filename.replace(']', '')
    filename = filename.replace('{', '')
    filename = filename.replace('}', '')
    filename = filename.replace('<', '')
    filename = filename.replace('>', '')
    filename = filename.replace(';', '')
    filename = filename.replace(':', '')
    filename = filename.replace('"', '')
    filename = filename.replace("'", '')
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    filename = filename.replace('|', '')
    filename = filename.replace('?', '')
    filename = filename.replace('*', '')
    # If file is exist, add number to filename
    if os.path.isfile(os.path.join(TEMP_DIR, filename)):
        filename = filename.split('.')
        filename = f"{filename[0]}_1.{filename[1]}"
    return filename


def save_to_local(file: bytes | Any, filename: str, is_parse_filename: bool = True):
    # Parse filename
    if is_parse_filename:
        filename = parse_filename(filename)
    # Get type of file
    file_extension = filename.split('.')[-1]
    # Get write mode
    if file_extension == 'json':
        mode = 'w'
    else:
        mode = 'wb'
    # Save file
    with open(os.path.join(TEMP_DIR, filename), mode) as f:
        if file_extension == 'json':
            json.dump(file, f)
        else:
            f.write(file)
    # Return access link
    return f"{APP_DOMAIN}/static/{filename}"


def read_from_local(filename: str):
    # Get type of file
    file_extension = filename.split('.')[-1]
    # Get read mode
    if file_extension == 'json':
        mode = 'r'
    else:
        mode = 'rb'
    # If file is exist, return file
    if os.path.isfile(os.path.join(TEMP_DIR, filename)):
        with open(os.path.join(TEMP_DIR, filename), mode) as f:
            if file_extension == 'json':
                return json.load(f)
            return f.read()


def remove_from_local(filename: str):
    # If file is exist, add number to filename
    if os.path.isfile(os.path.join(TEMP_DIR, filename)):
        os.remove(os.path.join(TEMP_DIR, filename))


def remove_from_local_with_expire(filename: str, expire: int):
    # Remove file after expire time
    if expire is not None and expire > 0:
        t = Timer(expire, remove_from_local, args=[filename])
        t.start()
