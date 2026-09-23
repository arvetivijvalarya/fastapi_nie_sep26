flights = { # Think of 'flights' as our temporary database. The key is the student ID: 1 → Ravi, 2 → Arun 
    1: {
        "id": 1,
        "name": "indigo",
        "source": "bengaluru",
        "destination": "chandigarh",
        "fare" : 7800
    },
    2: {
        "id": 2,
                "name": "airindia",
                "source": "chennai",
                "destination": "jaipur",
                "fare" : 7100
    }
}
print(type(flights))
print(type(flights[1]))