from fastapi import APIRouter
from backend.agent import Runner
from backend.scrape import final_list
from backend.models.car import CarSearchQuery

router = APIRouter()


@router.post("/search")
async def search_cars(query: CarSearchQuery):
   return final_list(**query.model_dump())
   

   

    
