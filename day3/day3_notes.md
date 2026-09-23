# Trainer Repo Link:

`https://github.com/neelmyna/fastapi_nie_sep26`

## Day2 CRUD operation on In-Memory data

### List of Entities

Flight
id : int
airline : str
source : int
destination : str
fare : float
Employee
id : int
name : str
designation : str
experience : int
technology : str
phone_number: int

C:\Program Files\MongoDB\Server\7.0\bin

range(10)
[0, 10)
range(1, 20)
[1, 19)
range(1, 20, 2)
range(30, 2, -4)

Why no ++ -- operators in Python?
Why no function overloading in Python ?
What you mean by Python is Dynamically typed language.
What are the 7 Arithmetic operators in Python?
Howmany numeric DTs are there in core Python ?
Can we perform long-circult/cut and and or (& and |) as we can do in C/C++/Java ?
What is the difference between == and is?
what is the difference between sorted() and sort()
What is the difference between find() and index() from str class?
What is 

---

## FAstAPI MongoDb CRUD operations

### Step1: Imports

```
	from fastapi import FastAPI, HTTPException, Depends
	from pydantic import BaseModel

	from pymongo import MongoClient
	from bson import ObjectId

	import jwt
	from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
	from pwdlib import PasswordHash
	from datetime import datetime, timedelta, timezone
```

Steps to Install the Modules:
```
pip install fastapi uvicorn pymongo
pip install "pwdlib[argon2]"
pip install python-multipart
```
---
## Connect to MongoDb via FastAPI (mongo_connect.py)

```
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
```
---
```
# pydantic 
class TicketCreate(BaseModel):
    title : str 
    description : str 
    category : str 
    status : str 

class TicketResponse(TicketCreate):
    id : str 
```
---
``` 
# helper (mongo to python)
def ticket_helper(ticket):
    return {
        "id" : str(ticket["_id"]),
        "title" : ticket["title"],        
        "description" : ticket["description"],
        "category" : ticket["category"],
        "status" : ticket["status"]       
    }
```
---
```
# api end points
@app.post("/tickets", status_code=201, response_model=TicketResponse)
def tickets_create(payload : TicketCreate):
    ticket_dict = payload.model_dump()
    result = ticket_collection.insert_one(ticket_dict)
    new_ticket = ticket_collection.find_one({"_id" : result.inserted_id})
    return ticket_helper(new_ticket)
```