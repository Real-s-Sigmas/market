from app import *
# from app import HOST_PG, USER_PG, PASSWORD_PG, PORT_PG
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory

import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime
from dotenv import load_dotenv

import logging


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("user.py have connected")


def login_user(email, pas):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")

        # Проверка есть ли такой пользователь
        if cursor.fetchall()[0][0] == 1 and check_pass(email, pas):
            pass
        else:
            logging.warning("Аккаунта с такой почтой не существует!")
            return_data = "Аккаунта с такой почтой не существует!"

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

def add_user_todb(email, pas):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        send_user = []

        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")
        send_user.append(cursor.fetchone())
        # Проверка существует ли такой пользователь
        if send_user[0][0] == 0 and check_pass(email, pas):
            cursor.execute(f"""INSERT INTO users(id, email, data_c) VALUES ({uuid.uuid4().hex}, '{email}', {datetime.now().isoformat()})""")

            pg.commit()

            logging.info("Пользователь зарегестрирован!")
            return_data = 'Ok'

        else:
            return_data = "Пользователь с такой почтой уже существует!"
            logging.warning(return_data)

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


def check_pass(email, pas):
    pass

def send_code(email):
    sender = "upfollow835@gmail.com"
    send_password = "zwrx qgne arwj jblp"

    code_pas = ""

    # ------------------------Улучшить бы----------------------------------------------------
    for _ in range(4):
        a = random.randint(0, 9) # А че тут улучшать? (Без негатива, от febolo)
        code_pas += str(a)
    #-----------------------------------------------------------------------------------------

    msg = MIMEText(f"Ваш код для изменения пароля: {code_pas}. Не сообщайте его никому!")
    msg["Subject"] = "Ваш код"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, send_password)

    server.sendmail(sender, email, msg.as_string())

    # держим пароль в сессии
    session['code'] = str(code_pas)
    session.modified = True
    session['email'] = str(email)
    session.modified = True

    logging.info(f'Пароль {code_pas} отправлен на почту {email}')

    return 0


# показ всего о юзере
def show_user_info(id):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from users WHERE id=$${id}$$")

        return_data = dict(cursor.fetchall()[0])

        logging.info(f'Инофрмация профиля {id} отображена')
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route('/user/profile', methods=['GET'])
def user_info():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = show_user_info(request.args.get('id'))

    return jsonify(response_object)

@app.route('user/sign-in', methods=['POST'])
def login():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    response_object["res"] = login_user(post_data.get('email'), post_data.get('pass'))

    return jsonify(response_object)

@app.route('user/sign-up', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'} #БаZа


