from fastapi import File, UploadFile


class FaceDetectionModel:
    image = UploadFile | None
    image_default = File(
        None, description="Image for face detection", example="image.jpg")
    fw_index = int | None
