import psycopg2, logging

from psycopg2 import Error
from flask import jsonify, request
from typing import Union
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG


#TODO: редис
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)


def AddItemToBasket(id_item: str, id_user: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"UPDATE users
                        SET basket = COALESCE(basket, '{id_item}') || ARRAY[?]
                        WHERE id_user =$${id_user}$$;")

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


@app.route("/basket/add-item", methods=['POST'])
@chek_for_user
def add_item():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = AddItemToBasket(post_data.get("id"), session.get("id"))

    return jsonify(response_object)



def DeleteItemToBasket(id_item: str, id_user: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"UPDATE users
                        SET basket = array_remove(basket, {id_item})
                        WHERE id_user =$${id_user}$$;")

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


@app.route("/basket/delete-item", methods=['POST'])
@chek_for_user
def delete_item():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = DeleteItemToBasket(post_data.get("id"), session.get("id"))

    return jsonify(response_object)



def ShowwItemFromBasket(id_user: str) -> Union[str, list]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT basket FROM users WHERE id_user=$${id_user}$$")

        return_data = cursor.fetchall()

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route("/basket/show-basket", methods=['POST'])
@chek_for_user
def delete_item():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = ShowwItemFromBasket(session.get("id"))

    return jsonify(response_object)