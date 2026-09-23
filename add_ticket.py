from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

# mongo 
URL = "mongodb://127.0.0.1:27017"
connection = MongoClient(URL)
db = connection["tickets_db"] # reference to the db
ticket_collection = db["tickets"] # reference to the collection

# pydantic 
class TicketCreate(BaseModel):
    title : str 
    description : str 
    category : str 
    status : str 

class TicketResponse(TicketCreate):
    id : str 

# helper (mongo to python)
def ticket_helper(ticket):
    return {
        "id" : str(ticket["_id"]),
        "title" : ticket["title"],        
        "description" : ticket["description"],
        "category" : ticket["category"],
        "status" : ticket["status"]       
    }

# api end points
@app.post("/tickets", status_code=201, response_model=TicketResponse)
def tickets_create(payload : TicketCreate):
    ticket_dict = payload.model_dump()
    result = ticket_collection.insert_one(ticket_dict)
    new_ticket = ticket_collection.find_one({"_id" : result.inserted_id})
    return ticket_helper(new_ticket)
