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
        # Handle different action types
        if request.action == "greet":
            return {"message": f"Hello! Parameters received: {request.parameters}"}
        elif request.action == "calculate":
            # Example of handling a calculation action
            if not request.parameters or "numbers" not in request.parameters:
                raise HTTPException(status_code=400, detail="Missing numbers parameter")
            numbers = request.parameters["numbers"]
            return {"result": sum(numbers)}
        else:
            raise HTTPException(status_code=400, detail=f"Unknown action: {request.action}")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Custom GPT Action API is running"} 