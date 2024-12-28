import os
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
import base64
import logging

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

PASSWORD_PG = os.getenv('PASSWORD_PG')
PORT_PG = os.getenv('PORT_PG')
USER_PG = os.getenv('USER_PG')
HOST_PG = os.getenv('HOST_PG')
MEDIA = os.getenv('MEDIA')
AVATAR = os.getenv('AVATAR')
PASSWORD_EMAIL = os.getenv('PASSWORD_EMAIL')
EMAIL = os.getenv('EMAIL')



app = Flask(__name__)

app.secret_key = "/zxc/"
app.permanent_session_lifetime = 60 * 60 * 24 * 28
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True  # Установите True для использования HTTPS


# enable CORS
CORS(app, resources={r"*": {"origins": "*", 'supports_credentials': True}})

#Главная страница
@app.route('/', methods=['GET'])
def home():

    response_object = {'status': 'success'} #БаZа
    response_object['message'] = session.get('id')
    logging.warning('1')
    # logging.info(session.get('id')) #debug
    logging.warning(response_object)
    session.pop('id', None)
    return jsonify(response_object)

def add_tables():
    try:
        pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"""create table if not exists users(
                        id uuid ,
                        username text,
                        surname text,
                        phonenumber text,
                        password text,
                        email text,
                        admin bool,
                        date_create timestamp,
                        basket text[]
                    )""")
        
        cursor.execute(f"""create table if not exists items(
                        id uuid UNIQUE,
                        title VARCHAR(30),
                        descriptions text,
                        price float,
                        photos text[],
                        topic text, 
                        date_create timestamp
                    )""")
        

        cursor.execute(f"""create table if not exists orders (
                        id uuid UNIQUE,
                        ids_items text[],
                        id_user uuid,
                        comment VARCHAR(100),
                        contacts VARCHAR(50),
                        status text,
                        date_create timestamp
                    )""")
        
        cursor.execute(f"""create table if not exists comments(
                        id uuid UNIQUE,
                        id_user uuid,
                        id_item uuid,
                        content VARCHAR(333),
                        stars TINYINT,
                        date_create timestamp
                    )""")

        #TODO: orders table
        pg.commit()
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error" 

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
    

from user import * 
from other import *
from admin import *
from comments import *
from items import *
from basket import *

if __name__ == '__main__':
      add_tables()
      app.run(host='0.0.0.0', port=80)


