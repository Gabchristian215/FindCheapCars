
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import car
   

app = FastAPI(
    title="Cheap Cars API",
    description="API for searching and discovering cheap car deals",
    version="0.1.0",
)

app.include_router(car.router)