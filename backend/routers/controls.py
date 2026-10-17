from fastapi import APIRouter
from agents import Runner
from backend.scrape import ScrapeCar
from backend.models.car import CarSearchQuery
from backend.agent import watcher, matcher

router = APIRouter()


@router.post("/search")
async def search_cars(query: CarSearchQuery):
   return ScrapeCar(**query.model_dump())
   

   

    
