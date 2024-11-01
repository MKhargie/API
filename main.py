from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import json
import os

app = FastAPI()

class ActionRequest(BaseModel):
    action: str
    parameters: Optional[Dict[str, Any]] = None

@app.post("/api/action")
async def handle_action(request: ActionRequest):
    try:
        # Save the request to a JSON file
        request_data = request.dict()
        file_path = "action_requests.json"
        
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
        else:
            data = []

        data.append(request_data)

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        
        return {"message": "Action request saved successfully"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Custom GPT Action API is running"} 