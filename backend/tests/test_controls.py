from fastapi import FastAPI
from fastapi.testclient import TestClient
from backend.routers.controls import router


app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_missing_location():
    response = client.post("/search",
    json={
        "make": "Honda",
        "model": "Civic",
        "max_price": 10000.0,
        "min_year": 2012
    }
    )
    assert response.status_code == 422


def test_car_response():
    response = client.post("/search",
        json={
            "location": "newyork",
            "make": "Honda",
            "model": "Civic",
            "max_price": 10000.0,
            "min_year": 2012
        }
        )

    data = response.json()

    assert response 
    assert "title" in data
    assert "price" in data
    assert "location" in data
    assert "link" in data
    assert response.status_code == 201

    
    
 
    

 
