import json
import mysql.connector
from fastapi import FastAPI, Request, Response
from sqldata import *
import hashlib


class SqlAuth(SqlData):
    def __init__(self):
        super().__init__()

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

    @classmethod
    def force_logout(cls, error_code):
        user = {'force_logou': error_code, 'forced_off': error_code, 'id': "", 'role': "", 'org_id': ""}
        return user

    @classmethod
    def make_error(cls, error_code, error_description):
        return {"error_code": error_code, "error_description": error_description}

    @classmethod
    def make_key(cls, uid, password):
        hash_word = "artfin229!" + password
        hash_uid = "artfin229!" + str(uid)

        uid_hash = hashlib.md5()
        uid_hash.update(hash_uid.encode('utf-8'))
        uid_hex = uid_hash.hexdigest()

        password_hash = hashlib.md5()
        password_hash.update(hash_word.encode('utf-8'))
        password_hex = password_hash.hexdigest()

        sql = "select * from nua_pwd where h = '" + uid_hex + "' and k = '" + password_hex + "'"
        rs = SqlData.sql0(sql)
        if rs is None:
            post = {"table_name":"nua_pwd", "action": "insert", "h": uid_hex, "k": password_hex }
            i = SqlData.post(post)
            return {"id": i}
        else:
            return {"id": rs['id']}

    @classmethod
    def check_key(cls, uid, password):
        hash_word = "artfin229!" + password
        hash_uid = "artfin229!" + str(uid)

        uid_hash = hashlib.md5()
        uid_hash.update(hash_uid.encode('utf-8'))
        uid_hex = uid_hash.hexdigest()

        password_hash = hashlib.md5()
        password_hash.update(hash_word.encode('utf-8'))
        password_hex = password_hash.hexdigest()

        sql = "select * from nua_pwd where h = '" + uid_hex + "' and k = '" + password_hex + "'"
        rs = SqlData.sql0(sql)
        if rs is None:
            return SqlAuth.make_error("101", sql)
        else:
            outp = SqlAuth.make_error("0", "")
            rs2 = SqlData.sql0("select * from nua_user where id = " + str(uid))
            if rs2 is None:
                return SqlAuth.make_error("500", "Unexpected Data Error")
            else:
                outp['uid'] = rs2['id']
                outp['role'] = rs2['role']
            return outp

    @staticmethod
    def get_user(post_data):
        sql = "select * from nua_user where id = " + str(post_data['uid'])
        rs = SqlData.sql0(sql)
        if rs is None:
            user = {"forced_off": 1}
        else:
            user = rs
        return user
    @staticmethod
    def create_user(email, pwd):
        output = {}
        sql = "select * from nua_user where email = '" + email.lower() + "'"
        rs = SqlData.sql0(sql)
        if rs is None:
            post = { "table_name": "nua_user", "action": "insert", "email": email.lower }
            i = SqlData.post(post)
            return i
            SqlAuth.make_key(i, pwd)
        else:
            output['user'] = SqlAuth.make_error("200", "User Already Exists")
            return output
        return {"error": "Does exist"}

    @staticmethod
    def login(email, pwd):
        output = {}
        sql = "select * from nua_user where email = '" + email.lower() + "'"
        rs = SqlData.sql0(sql)
        if rs is None:
            output['user'] = SqlAuth.make_error("404", "User Not Found")
            return output
        else:
            if pwd == "":
                output['user'] = SqlAuth.make_error("403", "Password cannot be blank")
            else:
                output['user'] = SqlAuth.check_key(rs['id'], pwd)
                return output
        return {"error": "Does exist"}
