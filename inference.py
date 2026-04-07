from fastapi import FastAPI
from pydantic import BaseModel
import torch
# Import your Agent/Warehouse logic here

app = FastAPI()

# This is what the "OpenEnv Reset" check is looking for!
@app.post("/reset")
async def reset():
    print("START")
    # Reset your environment/model logic here
    return {"status": "success", "message": "Environment Reset"}

@app.post("/step")
async def step(action: dict):
    print("STEP")
    # Your PyTorch logic to process the action
    return {"observation": "some_data", "reward": 0, "done": False}

@app.get("/state")
async def state():
    return {"status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
