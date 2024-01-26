from fastapi import APIRouter
from .rembg import router as rembg_router
from .img2text import router as img2text_router
from .chats import router as chats_router
from .fd import router as fd_router
from .vqa import router as vqa_router

router = APIRouter(prefix='/api')

# Register routes
router.include_router(rembg_router)
router.include_router(img2text_router)
router.include_router(chats_router)
router.include_router(fd_router)
router.include_router(vqa_router)
