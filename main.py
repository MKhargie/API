from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any


app = FastAPI()

class ActionRequest(BaseModel):
    action: str
    parameters: Optional[Dict[str, Any]] = None


@app.post("/api/action")
async def handle_action(request: ActionRequest):
    try:
        # Convert the request to a dictionary
        request_data = request.dict()
        
        # Return a custom message with the request data
        return {"message": f"Great I got the request {request_data}"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Custom GPT Action API is running"} 