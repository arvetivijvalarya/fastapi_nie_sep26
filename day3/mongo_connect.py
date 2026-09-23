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