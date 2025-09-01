import os
from datetime import datetime
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from functions.start_call import start_call




load_dotenv()

API_KEY = os.getenv("API_KEY")




app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=True)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API Key")



@app.post("/start-call")
def start_call(api_key: str = Depends(get_api_key)):
    
    if not start_call():
        return JSONResponse(content={"success": False}, status_code=400)


    return JSONResponse(content={"success": True}, status_code=200)





@app.get("/")
def read_root():
    return {"message": "API, V1.1.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("cg-api:app", host="0.0.0.0", port=8006, reload=True)# dev
    # uvicorn.run(app, host="0.0.0.0", port=8006)# prod
