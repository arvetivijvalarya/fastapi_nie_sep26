from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class FlightCreate(BaseModel):
    airline : str
    source  : str
    destination : str
    fare : float

class Flight(FlightCreate):
    id : int

# class Flight extends BaseModel {}
# java syntax

flights = { # Think of 'flights' as our temporary database. The key is the student ID: 1 → Ravi, 2 → Arun 
    1: {
        "id": 1,
        "airline": "indigo",
        "source": "bengaluru",
        "destination": "chandigarh",
        "fare" : 7800
    },
    2: {
        "id": 2,
        "airline": "airindia",
        "source": "chennai",
        "destination": "jaipur",
        "fare" : 7100
    }
}

# GET /flights
@app.get("/flights")
def get_all_flights():
    return list(flights.values())

# GET /flights/1
# GET /flights/100 -> {"detail": "Flight not found"}
@app.get("/flights/{flight_id}")
def get_flight(flight_id: int):
    if flight_id not in flights:
        raise HTTPException(detail="Flight not found", status_code=404)
    # raise HTTPException("Flight not found", 404)
    return flights[flight_id]

@app.post("/flights", response_model=Flight, status_code=201)
def add_Flight(flight : FlightCreate):
    new_id = max(flights.keys(), default=0) + 1
    new_flight = {
        "id" : new_id,
        **flight.model_dump()
    }
    flights[new_id] = new_flight
    return new_flight

@app.put("/flights/{flight_id}", response_model=Flight)
def update_flight(flight_id : int, flight : FlightCreate):
    if flight_id not in flights:
        raise HTTPException(status_code=404, detail=f'Flight with id {flight_id} not found')
    flights[flight_id] = {
        "id" : flight_id,
        **flight.model_dump()
    }
    return flights[flight_id]

@app.delete("/flights/{flight_id}")
def delete_flight(flight_id: int):
    if flight_id not in flights:
        raise HTTPException(detail="Flight not found", status_code=404)
    # raise HTTPException("Flight not found", 404)
    deleted_flight = flights[flight_id]
    del flights[flight_id]
    return deleted_flight
# return {"message" : "Flight deleted"}