# main.py
# The main program for the fastapi http listener.
# If you are changing this program, you are most likely in the wrong.
#
from fastapi import FastAPI, APIRouter, Request, Response, HTTPException
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.openapi.utils import get_openapi
# import json
# import mysql.connector
from sqlrouter import *
# Uncomment to deploy
# from starlette.middleware.wsgi import WSGIMiddleware
import logging

origins = [
    "http://localhost:4200",
    "https://protectivesecurity.org",
]

log_file_path = "app.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(file_handler)

app = FastAPI()
router = APIRouter()
app.include_router(router, prefix="/fastapi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers in the request
)


@app.post("/")
async def process_api(request: Request):
    try:
        # The data will come in as a JSON POST.
        post_data = await request.json()
        logging.info(post_data)
        # The router determines what actions need to be taken.
        return Router.test(post_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing POST data: {str(e)}")


