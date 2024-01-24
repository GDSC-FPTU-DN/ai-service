from fastapi import File, UploadFile


class Img2TextModel:
    image = UploadFile | None
    image_default = File(None, description="Image file")
    fw_index = int | None
