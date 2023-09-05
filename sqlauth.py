import json
import mysql.connector
from fastapi import FastAPI, Request, Response
from sqldata import *


class SqlAuth:
    def __init__(self):
        pass

    @classmethod
    def read_auth_cookie(cls):
        app = FastAPI()

    @classmethod
    def read_cookie(cls, request: Request):
        cookie_value = request.cookies.get("uid")
        if cookie_value:
            return cookie_value
        else:
            return '0'

    @classmethod
    def write_cookie(cls, response: Response, uid):
        response.set_cookie(key="uid", value=uid)
        return

    @staticmethod
    def login(uid, pwd):
        pass

