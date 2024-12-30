import logging, psycopg2, check

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from psycopg2 import extras, Error
from typing import Union, Optional, Tuple
from check import chek_for_admin

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


def OneOrder(id_user: str) -> Union[list, str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders WHERE id_user = $${id_user}$$ ORDER BY data")

        data_ = cursor.fetchall()
        return_data = []
        for row in data_:
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
