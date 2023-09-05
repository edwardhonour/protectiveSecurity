import json
import mysql.connector
from fastapi import FastAPI, Request, Response


class Db:
    def __init__(self):
        pass

    @classmethod
    def connect(cls):
        connection_vault_path = '/Users/user/pwd.json'

        try:
            with open(connection_vault_path, 'r') as connection_file:
                connection_dict = json.load(connection_file)
            return mysql.connector.connect(
                host=connection_dict['host'],
                user=connection_dict['user'],
                password=connection_dict['password'],
                database=connection_dict['database']
            )
        except FileNotFoundError:
            print(f"File '{connection_vault_path}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


class SqlData(Db):

    def __init__(self):
        super().__init__()

    # execute any query and return the results.

    @staticmethod
    def sql(s):
        conn = Db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(s)
        records = cursor.fetchall()
        return records

    @staticmethod
    def sql0(s):
        conn = Db.connect()
        cursor = conn.cursor()
        cursor.execute(s)
        records = cursor.fetchone()[0]
        return records

    @staticmethod
    def execute(s):
        conn = Db.connect()
        cursor = conn.cursor()
        cursor.execute(s)
        return

    @staticmethod
    def post(my_dict):
        if 'id' not in my_dict:
            my_id = 0
        else:
            my_id = my_dict['id']

        if 'action' not in my_dict:
            my_action = "insert"
        else:
            my_action = my_dict['action']

        if 'table_name' not in my_dict:
            return 900
        else:
            table_name = my_dict['table_name']

        conn = Db.connect()
        cursor = conn.cursor()
        if my_action == 'insert' or my_action == 'update':
            if my_id == 0 or my_id == '':
                sql = "insert into " + table_name + "(create_timestamp) values (now())"
                print(sql)
                cursor.execute(sql)
                cursor.execute("SELECT LAST_INSERT_ID()")
                my_id = cursor.fetchone()[0]
            for key in my_dict:
                if key != 'table_name' and key != 'id' and key != 'action':
                    cursor = conn.cursor()
                    sql = "update " + table_name + " set " + key + " = %s where id = %s"
                    print(sql)
                    v = (my_dict[key], my_id)
                    print(v)
                    cursor.execute(sql, v)
            conn.commit()
        if my_action == 'delete':
            sql = "delete from " + table_name + " where id = " + my_id
            cursor.execute(sql)

        return my_id

    @staticmethod
    def insert(table_name, json_data):
        my_dict = json.loads(json_data)
        conn = Db.connect()
        cursor = conn.cursor()

        sql = "insert into " + table_name
        cols = " (create_timestamp"
        vals = " (now()"
        values = []
        for key, value in my_dict.items():
            if cols == " (":
                cols += key
            else:
                cols += " ," + key

            if vals == " (":
                vals += "%s"
            else:
                vals += ", %s"

            values.append(value)

        cols += ")"
        vals += ")"
        sql += cols + vals
        print(sql)

        cursor.execute(sql, values)
        cursor.execute("SELECT LAST_INSERT_ID()")
        my_id = cursor.fetchone()[0]

        return my_id
