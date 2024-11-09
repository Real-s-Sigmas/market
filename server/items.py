import uuid, psycopg2, logging

from psycopg2 import Error
from flask import jsonify, request
from typing import Union
from app import *

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)


def GetPhotos(photos: list) -> list:
    pass

def PostItem(title: str, description: str, price: int, photos: list, topic: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        photos_links = getPhotos(photos)

        id = uuid.uuid4().hex
        cursor.execute(f"INSERT INTO itemes(id, title, description, price, photos, topic) VALUES('{id}', '{title}', '{description}', '{price}', '{photos_links}', '{topic}')")

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

#TODO: декоратор проверки на админа
@app.route("/items/new_item", methods=["POST"])
def new_item():
    response_object = {'status': 'success'} #БаZа
    
    post_data = request.get_json()

    res = PostItem(post_data.get("title"), post_data.get("description"), post_data.get("price"), post_data.get("topic"))

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


def PutItem(title: str, description: str, price: int, photos: list, topic: str, id: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        photos_links = GetPhotos(photos)

        cursor.execute(f"UPDATE itemes(id, title, description, price, photos, topic) SET('{id}', '{title}', '{description}', '{price}', '{photos_links}', '{topic}')")

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


#TODO: декоратор проверки на админа
@app.route("/items/change-item", methods=["PUT"])
def change_item():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = PutItem(post_data.get("title"), post_data.get("description"), post_data.get("price"), post_data.get("topic"), post_data.get("id"))

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


def DeleteItem(id: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"DELETE * FROM items WHERE id=$${id}$$")

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
 

#TODO: декоратор проверки на админа
@app.route("/items/delete-item", methods=["PUT"])
def delete_item():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = DeleteItem(post_data.get("id")) # type: ignore

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


#TODO: /items/show-items?category=

def NewTopic(name: str, base: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        id = uuid.uuid4().hex
        link = check.AddPhoto(base, "topic-phoyos", id)
        cursor.execute(f"INSERT INTO topics(id, name, photo) VALUES('{id}','{name}','{link}')")

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


#TODO: декоратор проверки на админа
@app.route("/items/new-topic", methods=["PUT"])
def new_topic():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = NewTopic(post_data.get("name"), post_data.get("photo")) # type: ignore

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


def DeleteTopic(id: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"DELETE * FROM topic WHERE id=$${id}$$")

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


@app.route("/items/delete-topic", methods=["PUT"])
def delete_topic():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = DeleteTopic(post_data.get("id"))

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


def PutTopic(id: str, name: str, link_old: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        link = link_old if link_new=="" else check.PutPhoto(check.NewLink(id, "topic-phoyos"), link_old)

        cursor.execute(f"UPDATE itemes(id, title, description, price, photos, topic) SET('{id}', '{name}', '{link}')")

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


#TODO: декоратор проверки на админа
@app.route("/items/change-item", methods=["PUT"])
def change_topic():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = PutTopic(post_data.get("id"), post_data.get("name"), post_data.get("link_old"))

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


def GetItems() -> Union[list, str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"SELECT title FROM topic")

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


@app.route("/items/get-topics", methods=["PUT"])
def get_topics():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = GetItems()

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200