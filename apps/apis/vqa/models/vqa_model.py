from fastapi import File, UploadFile, Form


class VQAModel:
    image = UploadFile | None
    image_default = File(None, description="Image to answer question")
    question = str | None
    question_default = Form(None, description="Question to answer")
    fw_index = int | None
