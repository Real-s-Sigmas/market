import random, uuid, psycopg2, smtplib, logging, hashlib

from app import HOST_PG, USER_PG, PASSWORD_PG, PORT_PG, PASSWORD_EMAIL, EMAIL, app
from psycopg2 import Error
from flask import jsonify, request, session
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
from typing import Union, Optional, Tuple
from email.message import EmailMessage


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


def ChangePasswordEmail(password: str, email: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''UPDATE users
                        SET password=$${hash_password(password)}$$
                        WHERE email=$${email}$$;
                        ''')
        pg.commit()
        return_data = "ok"
        logging.info(f'Пароль изменен на {email}')



    except (Exception, Error) as error:
        logging.error(f"Ошибка получения данных: {error}" )
        return_data = "Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
        
def SendCode(email: str) -> str:
    message_1 = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
        <style>
        * {
            margin: 0;
            font-family: "Rubik", system-ui;
        }

        @media (max-width: 500px) {
            .window {
            width: 370px;
            }

            h1 {
            font-size: 21px;
            }

            p {
            font-size: 10px;
            }

            h2 {
            font-size: 22px;
            width: 30px;
            }
        }
        
        
        </style>
    </head>"""

    sender = EMAIL
    send_password = PASSWORD_EMAIL
    code_pas = ""
    
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    code_pas = str(a) + str(b) + str(c) + str(d)

    message_2 = f"""    <body style="width: 100%">
        <div style="width: 100%; height: 450px; text-align: center; font-family: 'Rubik', system-ui;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <h1 style="color: #ff813c; border-bottom: 3px solid #ff813c; padding-bottom: 20px; margin-bottom: 20px; text-align: center; width: 500px;">С.и.Р</h1>
                    </td>
                </tr>
            </table>
            <p style="color: #ff813c; font-weight: 600; font-size: 13px; margin-bottom: 60px;">Здравствуйте!</p>
            <p style="color: #ff813c; font-weight: 600; font-size: 13px; margin-bottom: 40px;">Для смены пароля введите в поле этот код:</p>
            <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:20px;">
                <tr>
                    <td align="center">
                        <table width="20%" border="0" cellspacing="0" cellpadding="0"" style="border: 2px solid black; border-radius: 8px; padding:16px 10px; background-color: #fff2e2">
                            <tr>
                                <td align="center">
                                    <td align="center"><h2>{a}</h2></td> <td align="center"><h2>{b}</h2></td> <td align="center"><h2>{c}</h2></td> <td align="center"><h2>{d}</h2></td>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <p style="color: #ff813c; font-weight: 600; font-size: 13px; text-align: center;">
                            Пожалуйста! Обратите внимание, кто-то пытается сменить пароль на вашем аккаунте. <br>
                            Если это были не вы, никому не сообщайте данный код! <br>
                        </p>

                        <p style="border-top: 3px solid #ff813c; padding-top: 20px; color: #ff813c; font-weight: 600; font-size: 13px; text-align: center; width: 500px; margin-top: 30px;">
                            Спасибо, что остаетесь с нами! <br> С заботой о Вас, магазин строительства и ремонта СИР
                        </p>
                    </td>
                </tr>
            </table>
        </div>
    </body>
</html>"""

    msg = EmailMessage()

    msg["Subject"] = "Ваш код"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content("Код для подтверждения регистрации")
    msg.add_alternative(message_1 + message_2, subtype="html")
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, send_password)
        server.send_message(msg)
        logging.info("Email sent successfully!")

    except smtplib.SMTPRecipientsRefused:
        logging.info("Error: Recipient's email does not exist.")
        return "err"

    finally:
        server.quit()
        # держим пароль в сессии
        session['code'] = str(code_pas)
        session.modified = True

        logging.info(f'Пароль {code_pas} отправлен на почту {email}')

        return str(code_pas)

def IsEmail(email: str) -> Union[bool, str]:
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
        cnt = cursor.fetchall()[0][0]
        logging.info(cnt)
        return_data = True if cnt != 0 else False

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route("/user/check-email-code", methods=["POST"])
def CheckEmailCode():
    if False:
        return jsonify({"message": "Forbidden"}), 403

    response_object = {'status': 'success'}
    post_data = request.get_json()

    logging.info(session.get("code"))
    if session.get("code") == str(post_data.get("code")):
        response_object["res"] = "True"
        session["isVerif"] = True
        session.modified = True
        session.pop("code")
        session.modified = True
    else:
        response_object["res"] = "False"

    return jsonify(response_object)

@app.route('/user/change-password-email', methods=['POST', 'PUT'])
def change_password_email():
    if False:
        return jsonify({"message": "Forbidden"}), 403

    response_object = {'status': 'success'}
    post_data = request.get_json()
    logging.info(post_data.get("email"))
    if IsEmail(post_data.get("email")) is True:
        res = SendCode(post_data.get("email"))

        match res:
            case "err":
                response_object["res"] = "Bad email"
            case _:
                response_object["res"] = "ok"
    else: response_object["res"] = "0 email"
    return jsonify(response_object)

@app.route("/user/new-pass", methods=["POST"])
def new_password():
    if False:
        return jsonify({"message": "Forbidden"}), 403

    response_object = {'status': 'success'}
    post_data = request.get_json()

    if session.get("isVerif") is True:
        response_object["res"] = ChangePasswordEmail(post_data.get("password"), post_data.get("email"))
    else:
        response_object["res"] = "not veref"

    return jsonify(response_object)