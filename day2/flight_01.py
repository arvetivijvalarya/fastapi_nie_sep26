from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def start_app():
    return {"message" : "Welcome to Flight Management FastAPI"}

