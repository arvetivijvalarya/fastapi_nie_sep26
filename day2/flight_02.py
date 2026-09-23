from fastapi import FastAPI

app = FastAPI()

flights = { # Think of 'flights' as our temporary database. The key is the flight ID: 1 → indigo, 2 → airindia 
    1: {
        "id": 1,
        "name": "indigo",
        "source": "bengaluru",
        "destination": "chandigarh",
        "fare" : 7800
    },
    2: {
        "id": 1,
                "name": "airindia",
                "source": "chennai",
                "destination": "jaipur",
                "fare" : 7100
    }
}

# GET /
@app.get("/")
def home():
    return {"message": "Flight Management API"}

# GET /flights
@app.get("/flights")
def get_all_flights():
    return list(flights.values())
