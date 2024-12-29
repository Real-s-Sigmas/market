import random, uuid, psycopg2, smtplib, logging, hashlib, check

from app import HOST_PG, USER_PG, PASSWORD_PG, PORT_PG, app
from psycopg2 import Error
from flask import jsonify, request, session
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
from typing import Union, Optional, Tuple
from check import chek_for_admin, chek_for_user

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

#TODO: сделать
def GetPhotos(photos: list) -> list:
    return []

def PostItem(title: str, description: str, price: float, photos: list, topic: str, category: str = None, small_category: str = None) -> str:
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

        if not photos_links:
            photos_links = []

        id = uuid.uuid4().hex
        date_create = datetime.now()

        cursor.execute(
            """
            INSERT INTO items(id, title, descriptions, price, photos, characteristics, date_create, category, small_category) 
            VALUES(%s, %s, %s, %s, %s::text[], %s, %s, %s, %s)
            """,
            (id, title, description, price, photos_links, topic, date_create, category, small_category)
        )

        pg.commit()
        return_data = "Ok"
        logging.info(return_data)

    except (Exception, Error) as error:
        logging.error(f'DB Error: {error}')
        return_data = "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
    
    return return_data


@app.route("/items/new-item", methods=["POST"])
@chek_for_admin
def new_item():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    if not post_data:
        response_object['status'] = 'error'
        response_object['message'] = 'No data provided.'
        return jsonify(response_object), 400

    res = PostItem(
        title=post_data.get("title"),
        description=post_data.get("description"),
        price=post_data.get("price"),
        photos=post_data.get("photos", []),
        topic=post_data.get("characteristics"),
        category=post_data.get("category"),
        small_category=post_data.get("small_category")
    )

    if res == "Ok":
        response_object['message'] = 'Item created successfully.'
    else:
        response_object['status'] = 'error'
        response_object['message'] = 'Error creating item.'

    logging.info(response_object)

    return jsonify(response_object)





def PutItem(title: str, description: str, price: float, photos: list, topic: str, id: str, category: str = None, small_category: str = None) -> str:
    # Проверка на корректность входных данных
    if not title or not description or price is None or not isinstance(price, (int, float)) or not topic or not id:
        return "Error: Invalid input values"

    # Получаем ссылки на фотографии
    photos_links = GetPhotos(photos)  # Убедитесь, что эта функция возвращает корректные ссылки

    # # Проверяем, что photos_links не пустой
    # if photos_links is None:
    #     return "Error: photos_links is empty"

    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Используем параметризованный запрос для обновления
        cursor.execute("""
            UPDATE items
            SET title = %s, descriptions = %s, price = %s, photos = %s, characteristics = %s, category = %s, small_category = %s
            WHERE id = %s
        """, (title, description, price, photos_links, topic, category, small_category, id))

        pg.commit()
        return "Ok"

    except (Exception, Error) as error:
        logging.error(f'DB: {error}')
        return "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")


@app.route("/items/change-item", methods=["PUT"])
@chek_for_admin
def change_item():
    response_object = {'status': 'success'}  # База

    post_data = request.get_json()

    res = PutItem(
        title=post_data.get("title"),
        description=post_data.get("description"),
        price=post_data.get("price"),
        photos=post_data.get("photos"),
        topic=post_data.get("characteristics"),
        id=post_data.get("id"),
        category=post_data.get("category"),
        small_category=post_data.get("small_category")
    )

    if res == "Error":
        response_object["res"] = "Server Err"

    return jsonify(response_object)


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


# def getItemsTopic(fil: dict, start: int, end: int) -> Tuple[Union[list, str], str]:
#     try:
#         pg = psycopg2.connect(f"""
#             host={HOST_PG}
#             dbname=postgres
#             user={USER_PG}
#             password={PASSWORD_PG}
#             port={PORT_PG}
#         """)

#         cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

#         cursor.execute(f"SELECT * FROM items WHERE topic=$${fil["topic"]}$$ ORDER BY date_create DESC LIMIT {end-start+1} OFFSET {start}")

#         return_data = cursor.fetchall()

#         q = cursor.fetchall()
#         return_data = []

#         for row in q:
#             return_data.append(dict(row))


#         cursor.execute(f"SELECT COUNT(*) FROM items WHERE topic=$${fil["topic"]}$$")

#         count = cursor.fetchall()

#     except (Exception, Error) as error:
#         logging.error(f'DB: ', error)
#         return_data = f"Error"

#     finally:
#         if pg:
#             cursor.close()
#             pg.close()
#             logging.info("Соединение с PostgreSQL закрыто")
#             return return_data, count



# @app.route("/items/show-items", methods=["GET"])
# def get_items_topic():
#     response_object = {'status': 'success'} #БаZа

#     start, end = int(request.args.get("start"))-1, int(request.args.get('end'))-1

#     filtrs = {
#         'topic': request.args.get('topic'),
#     }

#     response_object["res"], response_object["count"] = getItemsTopic(filtrs, start, end)

#     return jsonify(response_object)

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


@app.route("/items/search", methods=['GET'])
def search():
    search_query = request.args.get('search', '')

    response_object = {'status': 'success'}

    response_object["res"] = search_items(search_query)

    return jsonify(response_object)


def getAllItems(category: str, small_category: str):
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
        cursor.execute(f"SELECT * FROM items WHERE category=$${category}$$ and small_category=$${small_category}$$")
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



@app.route("/items/show-items", methods=["GET"])
def get_items_topic():
    response_object = {'status': 'success'} #БаZа
    post_data = request.args

    response_object["res"] = getAllItems(post_data.get("category"), post_data.get("small_category"))
    return jsonify(response_object)


def OneItem(id: str) -> Union[list, str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * from items WHERE id=$${id}$$")

        all_states = dict(cursor.fetchall()[0])
        logging.info('Инфа есть')
        return_data = {}

        for key in all_states:
            return_data[key] = all_states[key]

        return_data['date_create'] = datetime.strftime(return_data['date_create'], '%d %B %Y')
        logging.info(f'Item info {id} displayed')

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data
    return 0

@app.route("/items/one-item", methods=['GET'])
def get_one_item():
    item_id = request.args.get('id')

    response_object = {'status': 'success'}

    response_object["res"] = OneItem(item_id)

    return jsonify(response_object)