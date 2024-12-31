import logging, psycopg2, check

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from psycopg2 import extras, Error
from typing import Union, Optional, Tuple
from check import chek_for_admin, chek_for_user

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("admin.py have connected")


def AllOrders() -> Union[list, str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders ORDER BY date_create")

        data_ = cursor.fetchall()
        return_data = []
        for row in data_:
            a = dict(row)
            cursor.execute(f"SELECT phonenumber FROM users where id = $${a["id_user"]}$$")
            a["phonenumber"] = cursor.fetchone()[0]
            return_data.append(dict(row))


        logging.info('Все заказы показаны')

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route('/admin/orders', methods=['GET'])
@chek_for_admin
def all_orders():
    responce_object = {'status': 'success'}

    responce_object['res'] = AllOrders()


    return jsonify(responce_object)


def OneOrder(id: str) -> Union[list, str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders WHERE id = $${id}$$")
        # logging.info(f"SELECT * FROM orders WHERE id = $${id_user}$$")
        data_ = cursor.fetchall()
        return_data = []
        for row in data_:
            a = dict(row)
            cursor.execute(f"SELECT phonenumber FROM users where id = $${a["id_user"]}$$")
            a["phonenumber"] = cursor.fetchone()[0]
            return_data.append(dict(row))

        logging.info('Все заказы показаны')

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route('/admin/order', methods=['GET'])
@chek_for_admin
def one_order():
    responce_object = {'status': 'success'}

    responce_object['res'] = OneOrder(request.args.get('id'))

    return jsonify(responce_object)



def ChangeStatus(status: str, id: str)->str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"UPDATE orders SET status = $${status}$$ WHERE id = $${id}$$")
        pg.commit()

        logging.info(f"Статус заказа {id} изменен на {status}")
        return_data = "ok"

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route('/admin/change-status', methods=["PUT"])
@chek_for_admin
def change_status():
    responce_object = {'status': 'success'}
    post_data = request.get_json()

    status = post_data.get("status")
    id = post_data.get("id")
    if status == "NEW" or status == "END" or status == "PROCESS" or status == "WAITING" or status == "END":
        responce_object["res"] = ChangeStatus(status, id)
    else:
        responce_object["res"] = "Bad stus of order"

    return jsonify(responce_object)


def GetArch(id: str)->Union[str, list]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders WHERE status = 'END' and id_user=$${id}$$")
        data_ = cursor.fetchall()
        return_data = []
        for row in data_:
            return_data.append(dict(row))
        logging.info(f"Архив {id} отображен")

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route('/admin/get-arc', methods=["GET"])
@chek_for_user
def get_arc():
    responce_object = {'status': 'success'}

    responce_object["res"] = GetArch(session.get("id"))

    return jsonify(responce_object)
