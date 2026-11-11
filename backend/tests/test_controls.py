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

    

 
