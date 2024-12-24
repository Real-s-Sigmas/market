import uuid, psycopg2, logging

from psycopg2 import Error
from flask import jsonify, request
from typing import Union, Tuple
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from check import chek_for_admin
import check
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

#TODO: сделать
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
        photos_links = GetPhotos(photos)

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


@app.route("/items/new_item", methods=["POST"])
@chek_for_admin
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


@app.route("/items/change-item", methods=["PUT"])
@chek_for_admin
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
 

@app.route("/items/delete-item", methods=["PUT"])
@chek_for_admin
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

def NewTopic(name: str, base: str, big: str) -> str:
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
        cursor.execute(f"INSERT INTO topics(id, name, photo, big) VALUES('{id}','{name}','{link}', '{big}')")

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


@app.route("/items/new-topic", methods=["PUT"])
@chek_for_admin
def new_topic():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = NewTopic(post_data.get("name"), post_data.get("photo"), post_data.get("big")) # type: ignore

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
@chek_for_admin
def delete_topic():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = DeleteTopic(post_data.get("id"))

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


def PutTopic(id: str, name: str, link_old: str, link_new: bool, big: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        link = link_old if link_new else check.PutPhoto(check.NewLink(id, "topic-phoyos"), link_old)

        cursor.execute(f"UPDATE topics(id, name, photo, big) SET('{id}', '{name}', '{link}', '{big}')")

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


@app.route("/items/change-topic", methods=["PUT"])
@chek_for_admin
def change_topic():
    response_object = {'status': 'success'} #БаZа

    post_data = request.get_json()

    res = PutTopic(post_data.get("id"), post_data.get("name"), post_data.get("link_old"), post_data.get("link_new"), post_data.get("big"))

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

    # post_data = request.get_json()

    res = GetItems()

    if res == "Error":
        response_object["res"] = "Server Err"
        return jsonify(response_object), 500
    
    response_object["res"] = res
    return jsonify(response_object), 200


#TODO: сделать
def getItemsFil(fil: dict, start: int, end: int) -> Tuple[Union[list, str], str]:
    pass



@app.route("/items/filter-items", methods=["GET"])
def fil_item():
    response_object = {'status': 'success'} #БаZа

    start, end = int(request.args.get("start"))-1, int(request.args.get('end'))-1

    filtrs = {
        'title': request.args.get('title'),
    }

    response_object["res"], count_query = getItemsFil(filtrs, start, end)
    response_object["count"] = check.doQuery(count_query)

    return jsonify(response_object)


def getItemsTopic(fil: dict, start: int, end: int) -> Tuple[Union[list, str], str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM items WHERE topic=$${fil["topic"]}$$ ORDER BY date_create DESC LIMIT {end-start+1} OFFSET {start}")

        return_data = cursor.fetchall()

        q = cursor.fetchall()
        return_data = []

        for row in q:
            return_data.append(dict(row))


        cursor.execute(f"SELECT COUNT(*) FROM items WHERE topic=$${fil["topic"]}$$")

        count = cursor.fetchall()

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data, count



@app.route("/items/show-items", methods=["GET"])
def get_items_topic():
    response_object = {'status': 'success'} #БаZа

    start, end = int(request.args.get("start"))-1, int(request.args.get('end'))-1

    filtrs = {
        'topic': request.args.get('topic'),
    }

    response_object["res"], response_object["count"] = getItemsTopic(filtrs, start, end)

    return jsonify(response_object)

def getCategory() -> dict:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"""SELECT big, GROUP_CONCAT(name) as names
                            FROM topics
                            GROUP BY big;""")


    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data



@app.route("/items/category", methods=["GET"])
def get_items_category():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = getCategory()

    return jsonify(response_object)


def search_items(search_query: str) -> list:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Используем LIKE для поиска
        cursor.execute("SELECT * FROM items WHERE title ILIKE %s", (f'%{search_query}%',))
        results = cursor.fetchall()

        return [dict(result) for result in results]

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return []

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")


@app.route("/items/one-item", methods=['GET'])
def get_one_item():
    search_query = request.args.get('search', '')

    response_object = {'status': 'success'}

    response_object["res"] = search_items(search_query)

    return jsonify(response_object)