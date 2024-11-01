from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    input: str

@app.get("/")
async def root():
    return {"message": "Hi Matt"}

@app.post("/submit/")
async def submit(item: Item):
    return {"message": f"{item.input} success"}