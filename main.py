# Google Developer Student Clubs - FPT University Da Nang
import os
import uvicorn
from apps.create_app import create_app
# Import routers
from apps.apis import router as api_router
from apps.services import router as service_router

app = create_app()

# Register apps routes
app.include_router(api_router)
app.include_router(service_router)

# Config uvicorn
if os.environ.get("ENV", "production") == 'development':
    uvicorn.run(app, port=8000)
