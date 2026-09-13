import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
try:
    from backend.models import CarListing, CarSearchQuery
except ImportError:
    from models import CarListing, CarSearchQuery

app = FastAPI(
    title="Cheap Cars API",
    description="API for searching and discovering cheap car deals",
    version="0.1.0",
)
