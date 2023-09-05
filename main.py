from fastapi import FastAPI, Request, Response, HTTPException
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://protectivesecurity.org",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers in the request
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/router/")
async def process_api(request: Request):
    try:
        post_data = await request.json()
        if post_data['q'] == '/sadmin':
            return {"result": post_data['q']}
        elif post_data['q'] == 'do-something':
            return {"result": post_data['q']}
        else:
            return {"result": "nothing"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing POST data: {str(e)}")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
