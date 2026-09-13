from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict


class CarListing(BaseModel):
    title: str = Field(
        ...,
        description="Headline title of the car listing",
        examples=["2015 Honda Civic LX"],
    )
    price: float = Field(
        ...,
        ge=0,
        description="Asking price in USD",
        examples=[8500.0],
    )
    year: Optional[int] = Field(
        default=None,
        ge=1900,
        description="Model manufacturing year",
        examples=[2015],
    )
    make: Optional[str] = Field(
        default=None,
        description="Car make or manufacturer",
        examples=["Honda"],
    )
    model: Optional[str] = Field(
        default=None,
        description="Car model name",
        examples=["Civic"],
    )
    mileage: Optional[int] = Field(
        default=None,
        ge=0,
        description="Odometer mileage reading in miles",
        examples=[95000],
    )
    location: Optional[str] = Field(
        default=None,
        description="City and state where the vehicle is located",
        examples=["New York, NY"],
    )
    description: Optional[str] = Field(
        default="Clean title, well-maintained vehicle in good running condition.",
        description="Seller notes or listing description",
        examples=["Clean title, single owner, regular maintenance, excellent condition."],
    )

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "2015 Honda Civic LX",
                    "price": 8500.0,
                    "year": 2015,
                    "make": "Honda",
                    "model": "Civic",
                    "mileage": 95000,
                    "location": "New York, NY",
                    "description": "Clean title, single owner, regular maintenance, excellent condition.",
                }
            ]
        }
    )


# Ready-to-use sample car listing for testing and demonstration
SAMPLE_CAR_LISTING = CarListing(
    title="2015 Honda Civic LX",
    price=8500.0,
    year=2015,
    make="Honda",
    model="Civic",
    mileage=95000,
    location="New York, NY",
    description="Clean title, single owner, regular maintenance, excellent condition.",
)


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
    transmission="Automatic",
)



print("CarSearchQuery schema:", CarSearchQuery.model_json_schema())
    
