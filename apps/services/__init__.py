from fastapi import APIRouter
from .foward import router as foward_router

router = APIRouter(prefix='/service')

# Register routes
router.include_router(foward_router)
