from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from fastapi import APIRouter

router = APIRouter()


class CarSearchQuery(BaseModel):
    make: Optional[str] = Field(
        default=None,
        description="Car manufacturer or make (e.g., Honda, Toyota)",
        examples=["Honda"],
    )
    model: Optional[str] = Field(
        default=None,
        description="Car model name (e.g., Civic, Camry)",
        examples=["Civic"],
    )
    min_price: Optional[float] = Field(
        default=None,
        ge=0,
        description="Minimum target price in USD",
        examples=[3000.0],
    )
    max_price: Optional[float] = Field(
        default=None,
        ge=0,
        description="Maximum budget/price in USD",
        examples=[10000.0],
    )
    min_year: Optional[int] = Field(
        default=None,
        ge=1990,
        description="Earliest model year to consider",
        examples=[2012],
    )
    max_year: Optional[int] = Field(
        default=None,
        ge=1990,
        description="Latest model year to consider",
        examples=[2020],
    )
    max_mileage: Optional[int] = Field(
        default=None,
        ge=0,
        description="Maximum odometer reading in miles",
        examples=[100000],
    )
    location: Optional[str] = Field(
        default=None,
        description="City, state, or region to search within",
        examples=["New York, NY"],
    )
    zip_code: Optional[str] = Field(
        default=None,
        description="5-digit ZIP code to center the search around",
        examples=["10001"],
    )
    transmission: Optional[str] = Field(
        default=None,
        description="Transmission type (e.g., Automatic, Manual)",
        examples=["Automatic"],
    )

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "make": "Honda",
                    "model": "Civic",
                    "min_price": 3000.0,
                    "max_price": 10000.0,
                    "min_year": 2012,
                    "max_year": 2020,
                    "max_mileage": 100000,
                    "location": "New York, NY",
                    "zip_code": "10001",
                    "transmission": "Automatic",
                }
            ]
        }
    )


# Ready-to-use sample instance for testing and demonstration
SAMPLE_CAR_SEARCH_QUERY = CarSearchQuery(
    make="Honda",
    model="Civic",
    min_price=3000.0,
    max_price=10000.0,
    min_year=2012,
    max_year=2020,
    max_mileage=100000,
    location="New York, NY",
    zip_code="10001",
    transmission="Automatic",
)




@router.post("/search")
async def search_cars(query: CarSearchQuery):
    create_user_preference = query.model_dump()


    return create_user_preference

    
    
    
