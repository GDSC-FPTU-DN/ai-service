import numpy as np
import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path='resources/fd_model.tflite')
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)


def format_detections(detection_result):
    faces = []
    for detection in detection_result.detections:
        face = {
            "bbox": {
                "x": detection.bounding_box.origin_x,
                "y": detection.bounding_box.origin_y,
                "width": detection.bounding_box.width,
                "height": detection.bounding_box.height,
            },
        }
        faces.append(face)
    return faces


def faces_detection_controller(image: bytes):
    cv_image = cv.imdecode(np.frombuffer(image, np.uint8), cv.IMREAD_COLOR)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv_image)
    # Process image
    detection_result = detector.detect(mp_image)
    return format_detections(detection_result)
