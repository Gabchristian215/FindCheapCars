from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


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
    location: Optional[str] = Field(
        default=None,
        description="City, state, or region to search within",
        examples=["newyork"],
    )
    
   

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "make": "Honda",
                    "model": "Civic",
                    "max_price": 10000.0,
                    "min_year": 2012,
                    "location": "newyork",
                }
            ]
        }
    )


# Ready-to-use sample instance for testing and demonstration
SAMPLE_CAR_SEARCH_QUERY = CarSearchQuery(
    make="Honda",
    model="Civic",
    max_price=10000.0,
    min_year=2012,
    location="newyork",

)


