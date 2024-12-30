import psycopg2, logging

from psycopg2 import Error
from flask import jsonify, request
from typing import Union
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG
from check import chek_for_user


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

        cursor.execute(f"")
        #NOTE: probably status IN SHOP in futere 

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

        cursor.execute(
            """
            INSERT INTO orders(id, orders, status, id_user)
            VALUES (
                ?,
                (COALESCE(basket, '{}') || ?::text[]),
                ?,
                ?
            );
            """,
            (uuid.uuid4().hex, id_items, "NEW", id_user)
        )

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



@app.route("/order/add-order", methods=["DELETE"])
@chek_for_user
def delete_order():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()
    response_object["res"] = DeleteOrder(post_data.get("id"))

    return jsonify(response_object)


def get_orders_by_id(order_id: str) -> dict:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        result = cursor.fetchone()

        if result:
            return dict(result)
        else:
            return {}

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return {}

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")


@app.route("/orders/show-orders", methods=['GET'])
def show_orders():
    order_id = request.args.get('id')

    response_object = {'status': 'success'}

    if order_id:
        response_object["res"] = get_orders_by_id(order_id)
    else:
        response_object["status"] = 'bad request'
        response_object["message"] = "Missing order ID"

    return jsonify(response_object)