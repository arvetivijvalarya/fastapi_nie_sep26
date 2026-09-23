from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# mongo 
URL = "mongodb://127.0.0.1:27017"
client = MongoClient(URL)
db = client["tickets_db"] # reference to the db
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

@app.get("/tickets", response_model=list[TicketResponse])
def tickets_read_all():
    tickets_result = ticket_collection.find()
    tickets = [ticket_helper(ticket) for ticket in tickets_result]
    return tickets

@app.get("/tickets/{id}", response_model=TicketResponse)
def ticket_read_by_id(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ticket ID format")
    ticket_result = ticket_collection.find_one({"_id": ObjectId(id)})
    if not ticket_result:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket_helper(ticket_result)

@app.put("/tickets/{id}", response_model=TicketResponse)
def ticket_update(id: str, payload : TicketCreate):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ticket ID format")
    result = ticket_collection.update_one({"_id": ObjectId(id)}, {"$set": payload.model_dump()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")
    new_ticket = ticket_collection.find_one({"_id" : ObjectId(id)})
    return ticket_helper(new_ticket)

@app.delete("/tickets/{id}")
def ticket_delete(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ticket ID format")
    result = ticket_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message" : "ticket deleted successfully"}