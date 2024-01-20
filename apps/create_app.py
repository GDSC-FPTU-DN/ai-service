from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from utils.metadata import DOC_SWAGGER


def create_app():
    app = FastAPI(**DOC_SWAGGER)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    app.mount("/static", StaticFiles(directory="temp"), name="static")
    return app
