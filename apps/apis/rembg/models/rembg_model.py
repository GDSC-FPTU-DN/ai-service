from fastapi import UploadFile, File, Form


class RembgModel:
    image = UploadFile | None
    image_default = File(
        None, description="Image to remove background", example="image.jpg")
    stream = str | None
    stream_default = Form(
        None, description="Is return a streaming or access json", example="false")
    expire = int | None
    expire_default = Form(
        None, description="Expire time of access link", example=3600)
    fw_index = int | None
    fw_index_default = Form(
        None, description="Forward destination index", example=0)

    def stream_parser(x): return False if x == 'false' or x == 0 else True
