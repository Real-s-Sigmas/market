import psycopg2, logging, json, os, smtplib

from psycopg2 import Error
from flask import jsonify, request, session
from typing import Union
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, EMAIL, PASSWORD_EMAIL
from check import chek_for_user, getEmail, chek_for_admin
from datetime import datetime
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

ABOUT_US = os.getenv('ABOUT_US')

def GetOrderHistory(id_user: str) -> Union[str, list]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders WHERE id_user=$${id_user}$$ AND status='ENDED' ORDER BY date DESC")

        data_ = cursor.fetchall()
        return_data = []
        for row in data_:
            return_data.append(dict(row))

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route("/order/history", methods=["GET"])
@chek_for_user
def get_order_history():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = GetOrderHistory(session.get("id"))

    return jsonify(response_object)


def GetOrders(id_user: str) -> Union[str, list]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders WHERE id_user = $${id_user}$$")
        res = cursor.fetchall()

        return_data = []

        for i in res:
            return_data.append(dict(i))

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route("/order/get-orders", methods=["GET"])
@chek_for_user
def get_orders():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = GetOrders(session.get("id"))

    return jsonify(response_object)


def SendEmailNew(email: str) -> str:
    sender = EMAIL
    send_password = PASSWORD_EMAIL
    logging.info(f"will send to: {email}")
    Emailmsg = "Спасибо за заказ! Мы уже его собираем и по готовности, вам придет сообщение."

    msg = EmailMessage()

    msg["Subject"] = "Заказ оформлен"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content(Emailmsg)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, send_password)
        server.sendmail(sender, email, msg.as_string())
        logging.info("Email sent successfully!")

    except smtplib.SMTPRecipientsRefused:
        logging.info("Error: Recipient's email does not exist.")
        return "err"

    finally:
        server.quit()
        logging.info(f'Письмо об оформлении заказа отправлено на {email}')

        return 'ok'
    
def SendEmailWaiting(email: str, id_order: str) -> str:
    sender = EMAIL
    send_password = PASSWORD_EMAIL

    Emailmsg = f"""Ваш заказ готов, код заказа: {id_order[-8:]}. 
Подробную информацию о получении заказа.
A так же о пункте выдачи вы можете посмотреть тут: {ABOUT_US}"""

    msg = EmailMessage()

    msg["Subject"] = "Заказ готов"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content(Emailmsg)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, send_password)
        server.sendmail(sender, email, msg.as_string())
        logging.info("Email sent successfully!")

    except smtplib.SMTPRecipientsRefused:
        logging.info("Error: Recipient's email does not exist.")
        return "err"

    finally:
        server.quit()
        logging.info(f'Письмо о готовности заказа отправлено на {email}')

        return 'ok'




def sendEmail(id_user: str, type: str, id_order: str) -> str:
    if type == "NEW":
        return SendEmailNew(getEmail(id_user))
    elif type == "WAITING":
        return SendEmailWaiting(getEmail(id_user), id_order)
    return "Error type"


def AddOrder(id_user: str, id_items: list) -> Union[str, list]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Преобразуем каждый словарь в JSON и затем в jsonb
        ids_items = [json.dumps(item) for item in id_items]
        id = uuid.uuid4().hex
        insert_query = """
            INSERT INTO orders (id, ids_items, id_user, status, date_create)
            VALUES (%s, %s::jsonb[], %s, %s, %s)
        """

        cursor.execute(insert_query, (id, ids_items, id_user, "NEW", datetime.now()))
        
        pg.commit()

        email = sendEmail(id_user, 'NEW', id)

        if email != 'ok': return_data = "Failed to send email"
        else: return_data = id

    except (Exception, Error) as error:
        logging.error(f'DB Error: {error}')
        return_data = "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route("/order/add-order", methods=["POST"])
@chek_for_user
def add_order():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()
    response_object["res"] = AddOrder(session.get("id"), post_data.get("ids"))

    return jsonify(response_object)

def DeleteOrder(id_order: str):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"DELETE FROM oders WHERE id=$${id_order}$$")

        pg.commit()

        return_data = "Ok"


    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data



@app.route("/order/delete-order", methods=["DELETE"])
@chek_for_user
def delete_order():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()
    response_object["res"] = DeleteOrder(post_data.get("id"))

    return jsonify(response_object)


def get_orders_by_id(last_eight: str) -> dict:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        res = []
        if last_eight != "":
            cursor.execute("SELECT * FROM orders WHERE RIGHT(id::text, 8) = %s", (last_eight,))
            result = cursor.fetchall()
            for row in result:
                a = dict(row)
                cursor.execute(f"SELECT phonenumber FROM users where id = $${a["id_user"]}$$")
                a["phonenumber"] = cursor.fetchone()[0]
                # a['date_create'] = datetime.strftime(a['date_create'], '%d %B %Y')
                res.append(a)
        else:
            cursor.execute("SELECT * FROM orders")
            result = cursor.fetchall()
            for row in result:
                a = dict(row)
                cursor.execute(f"SELECT phonenumber FROM users where id = $${a["id_user"]}$$")
                a["phonenumber"] = cursor.fetchone()[0]
                # a['date_create'] = datetime.strftime(a['date_create'], '%d %B %Y')
                res.append()

        return res
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return "Err"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")


@app.route("/orders/search", methods=['GET'])
@chek_for_admin
def show_orders():
    order_id = request.args.get('id')

    response_object = {'status': 'success'}

    if not order_id is None:
        response_object["res"] = get_orders_by_id(order_id)
        num = 200
        if response_object["res"] == "Err": 
            num = 500
        return jsonify(response_object), num
    
    else:
        response_object["status"] = 'bad request'
        response_object["message"] = "Missing order ID"

        return jsonify(response_object), 400

