import random, uuid, psycopg2, smtplib, logging, hashlib

from app import HOST_PG, USER_PG, PASSWORD_PG, PORT_PG, app
from psycopg2 import Error
from flask import jsonify, request, session
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
from typing import Union, Optional, Tuple


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("user.py have connected")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    return stored_hash == hash_password(password)

def check_password_hash(stored_hash, input_password):
    return verify_password(stored_hash, input_password)


def SignUp(name: str, surname: str, phonenumber, password: str, email: str) -> str:
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
        # cursor.execute(f"SELECT COUNT(*) FROM users WHERE username=$${name}$$")
        # send_user.append(cursor.fetchone())

        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${email}$$")
        send_user.append(cursor.fetchone())

        cursor.execute(f"SELECT COUNT(*) FROM users WHERE phonenumber=$${phonenumber}$$")
        send_user.append(cursor.fetchone())
        # Проверка существует ли такой пользователь
        if send_user[0][0] == 0 and send_user[1][0] == 0:
            cursor.execute(f'''INSERT INTO users(id, username, surname, phonenumber, password, email, admin, date_create) 
                                VALUES (
                                '{uuid.uuid4().hex}', 
                                '{name}',
                                '{surname}',  -- Добавлена запятая здесь
                                '{phonenumber}',
                                '{hash_password(password)}',
                                '{email}',
                                false,
                                '{datetime.now().isoformat()}'
                                )''')

            
            pg.commit()
            logging.info("Пользователь зарегестрирован!")
            return_data = "ok"
        else:
            return_data = "Пользователь с таким именем или почтой уже существует!"
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
    return 0

@app.route('/user/sign-up', methods=['POST'])
def sign_up():
    responce_object = {'status': 'success'}

    data = request.get_json()

    if len(data.get('password')) >= 8:
        responce_object['res'] = SignUp(
                                    data.get('name'),
                                    data.get('surname'),
                                    data.get('phonenumber'),
                                    data.get('password'),
                                    data.get('email')
                                )
    else:
        responce_object["res"] = "Password length too small"

    return jsonify(responce_object)


def SignIn(phonenumber: str, password: str):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT COUNT(*) FROM users WHERE email=$${phonenumber}$$")

        # Проверка есть ли такой пользователь
        if cursor.fetchall()[0][0]==1:

            cursor.execute(f"SELECT * FROM users WHERE email=$${phonenumber}$$")
            user = dict(cursor.fetchone())

            # Проверка пароля
            if verify_password(user["password"], password):
                logging.info(f"Login to: {user["id"]}")
                return_data = ['ok', user["id"]]

            else:
                logging.warning("Incorrect Password")
                return_data = 'Incorrect Password'
        else:
            logging.warning("Account Doesn`t Exist")
            return_data = "Account Doesn`t Exist"

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route('/user/sign-in', methods=['POST'])
def sign_in():
    responce_object = {'status': 'success'}

    data = request.get_json()
    
    smth = SignIn(data.get('email'), data.get('password'))

    if smth[0] == 'ok':
        session['id'] = smth[1]
        session.permanent = True
        session.modified = True
        responce_object['res'] = 'ok'

    else: responce_object['res'] = smth

    return jsonify(responce_object)


@app.route('/user/sign-out', methods=['GET'])
def sign_out():
    responce_object = {'status': 'success'}
    responce_object['res'] = session.get('id')
    session.pop('id', None)
    return jsonify(responce_object)


def Profile(id: str) -> Union[list, str]:
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

        all_states = dict(cursor.fetchall()[0])
        logging.info('Инфа есть')
        return_data={}

        for key in all_states:
            if key != "password":
                return_data[key] = all_states[key]

        return_data['date_create'] = datetime.strftime(return_data['date_create'], '%d %B %Y')
        logging.info(f'User info {id} displayed')
    
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
    return 0

@app.route('/user/profile', methods=['GET'])
def profiler():
    responce_object = {'status': 'success'}

    responce_object['res'] = Profile(session.get('id'))

    return jsonify(responce_object)

def check_admin_status(user_id: str) -> bool:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor()
        cursor.execute("SELECT admin FROM users WHERE id = %s;", (user_id,))
        result = cursor.fetchone()

        if result and result[0]:
            return True
        return False

    except (Exception, psycopg2.Error) as error:
        logging.error('DB error: %s', error)
        return False

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")

@app.route('/user/activate-admin', methods=['GET'])
def activate_admin():
    user_id = session.get('id')

    if not user_id:
        return jsonify({'message': 'Unauthorized'}), 401

    if check_admin_status(user_id):
        session['isAdmin'] = True
        session.permanent = True
        session.modified = True
        return jsonify({'message': 'Admin access granted'})

    return jsonify({'message': 'No admin access'})
