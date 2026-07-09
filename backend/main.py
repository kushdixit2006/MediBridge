from fastapi import FastAPI

from backend.api.chat import (
    router as chat_router,
)

from backend.api.upload import (
    router as upload_router,
)

app = FastAPI(
    title="MediBridge API",
    description="AI Medical Report Assistant",
    version="1.0.0",
)

app.include_router(
    upload_router,
    prefix="/api",
    tags=["Upload"],
)

app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"],
)


@app.get("/")
async def root():

    return {
        "message": "Welcome to MediBridge API"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }