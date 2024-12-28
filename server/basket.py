import psycopg2, logging, check

from check import chek_for_admin, chek_for_user
from psycopg2 import Error
from flask import jsonify, request
from typing import Union
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, session

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

        # Используем параметризованный запрос для безопасности
        cursor.execute("""
            UPDATE users
            SET basket = COALESCE(basket, '{}')::text[] || %s::text[]
            WHERE id = %s;
        """, ([id_item], id_user))

        pg.commit()
        return_data = "Ok"

    except (Exception, Error) as error:
        logging.error(f'DB: {error}')
        return_data = "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()

    return return_data




@app.route("/basket/add-item", methods=['POST'])
@chek_for_user
def add_item():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = AddItemToBasket(post_data.get("id"), session.get("id"))

    return jsonify(response_object)



def DeleteSingleItemFromBasket(id_item: str, id_user: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Получаем текущий массив basket
        cursor.execute("SELECT basket FROM users WHERE id = %s;", (id_user,))
        current_basket = cursor.fetchone()

        if current_basket and current_basket[0]:
            # Преобразуем массив в список
            basket_list = list(current_basket[0])

            # Удаляем только одно вхождение id_item
            if id_item in basket_list:
                basket_list.remove(id_item)

            # Обновляем массив в базе данных
            cursor.execute("""
                UPDATE users
                SET basket = %s
                WHERE id = %s;
            """, (basket_list, id_user))

            pg.commit()
            return_data = "Ok"
        else:
            return_data = "Item not found in basket"

    except (Exception, Error) as error:
        logging.error(f'DB: {error}')
        return_data = "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")

    return return_data




@app.route("/basket/delete-item", methods=['DELETE'])
@chek_for_user
def delete_item_():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = DeleteSingleItemFromBasket(post_data.get("id"), session.get("id"))

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

        # Использование параметризованного запроса
        cursor.execute("SELECT basket FROM users WHERE id = %s", (id_user,))
        
        return_data = cursor.fetchone()  # Получаем один результат (так как id уникален)

        # Преобразование результата в массив, если данные найдены
        if return_data and return_data[0] is not None:
            basket_array = return_data[0]  # basket уже является массивом
        else:
            basket_array = []  # Пустой массив, если данные отсутствуют

        return basket_array

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            # return return_data


@app.route("/basket/show-basket", methods=['GET'])
@chek_for_user
def delete_item__():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = ShowwItemFromBasket(session.get("id"))

    return jsonify(response_object)


def modify_fav_item(user_id: str, item_id: str, action: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if action == 'add':
            cursor.execute("""
                UPDATE users 
                SET favs = array_append(favs, %s) 
                WHERE id = %s
            """, (item_id, user_id))
        elif action == 'delete':
            cursor.execute("""
                UPDATE users 
                SET favs = array_remove(favs, %s) 
                WHERE id = %s
            """, (item_id, user_id))

        pg.commit()
        return "Success"

    except (Exception, Error) as error:
        logging.error(f'DB: {error}')
        return "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")


@app.route("/basket/add-fav", methods=['POST'])
def add_fav():
    item_id = request.get_json().get('id')
    user_id = session.get("id")

    if user_id and item_id:
        result = modify_fav_item(user_id, item_id, 'add')
        return jsonify({'status': result}), 200

    return jsonify({'status': 'bad request'}), 400

def DeleteSingleFavItem(user_id: str, item_id: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Получаем текущий массив favs
        cursor.execute("SELECT favs FROM users WHERE id = %s;", (user_id,))
        current_favs = cursor.fetchone()

        if current_favs and current_favs[0]:
            # Преобразуем массив в список
            favs_list = list(current_favs[0])

            # Удаляем только одно вхождение item_id
            if item_id in favs_list:
                favs_list.remove(item_id)

                # Обновляем массив в базе данных
                cursor.execute("""
                    UPDATE users
                    SET favs = %s
                    WHERE id = %s;
                """, (favs_list, user_id))

                pg.commit()
                return "Ok"
            else:
                return "Item not found in favorites"
        else:
            return "No favorites found"

    except (Exception, Error) as error:
        logging.error(f'DB: {error}')
        return "Error"

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")

@app.route("/basket/delete-fav", methods=['DELETE'])
def delete_fav():
    item_id = request.get_json().get('id')
    user_id = session.get("id")

    if user_id and item_id:
        result = DeleteSingleFavItem(user_id, item_id)
        return jsonify({'status': result}), 200

    return jsonify({'status': 'bad request'}), 400

@app.route("/basket/show-favs", methods=['GET'])
def show_fav():
    user_id = session.get("id")

    if user_id:
        try:
            pg = psycopg2.connect(f"""
                host={HOST_PG}
                dbname=postgres
                user={USER_PG}
                password={PASSWORD_PG}
                port={PORT_PG}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Извлекаем массив избранных элементов
            cursor.execute("SELECT favs FROM users WHERE id = %s;", (user_id,))
            favs = cursor.fetchone()

            if favs and favs[0]:
                return jsonify({'status': 'success', 'favs': favs[0]}), 200
            else:
                return jsonify({'status': 'success', 'favs': []}), 200  # Пустой массив, если нет избранных

        except (Exception, Error) as error:
            logging.error(f'DB: {error}')
            return jsonify({'status': 'error', 'message': 'Database error'}), 500

        finally:
            if pg:
                cursor.close()
                pg.close()
                logging.info("Соединение с PostgreSQL закрыто")

    return jsonify({'status': 'bad request'}), 400
