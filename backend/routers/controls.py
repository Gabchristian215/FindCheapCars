from fastapi import APIRouter, status, HTTPException
from backend.agent import Runner
from backend.scrape import final_list
from backend.models.car import CarSearchQuery

router = APIRouter()


@router.post("/search", status_code=status.HTTP_201_CREATED)
async def search_cars(query: CarSearchQuery):
   if not query.location:
      raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Location cannot be empty")   
   return final_list(**query.model_dump())
   

   

    
