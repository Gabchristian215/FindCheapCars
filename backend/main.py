
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import controls


app = FastAPI(
    title="Cheap Cars API",
    description="API for searching and discovering cheap car deals",
    version="0.1.0",
)

app.include_router(controls.router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "version": app.version,
    }