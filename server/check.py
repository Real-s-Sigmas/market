import os, uuid, psycopg2, base64, logging

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from flask_cors import CORS
from datetime import datetime
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("reuse_func.py have connected")


def IsAdmin(id: str) -> bool:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT admin FROM users WHERE id = $${id}$$")

        return_data = cursor.fetchall()[0][0]

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
        
def IsAdminSession() -> bool:
    return session.get('admin')

def IsInSession() -> bool:
    return 'id' in session

def GetId() -> str:
    return session.get('id')

def AddPhoto(base: str, type: str, id: str) -> str:
    return

def DeletePhoto(link: str) -> str:
    return

def PutPhoto(link_old: str, link_new: str) -> str:
    return

def NewLink(id: str, type: str) -> str:
    return

def EscapeQuotes(text):
    return text.replace("'", "''")

def UnescapeQuotes(text):
    return text.replace("''", "'")

def chek_for_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("isAdmin") == True:
            func(*args, **kwargs)
        else: return jsonify({"status": "success", "res": "Not Admin"}), 400
    return wrapper

def chek_for_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "id" in session:
            func(*args, **kwargs)
        else: return jsonify({"status": "success", "res": "Not in session"}), 400
    return wrapper