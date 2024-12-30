import psycopg2, logging, check

from check import chek_for_admin, chek_for_user
from psycopg2 import Error
from flask import jsonify, request
from typing import Union
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, session

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

PASSWORD_PG = os.getenv('PASSWORD_PG')
PORT_PG = os.getenv('PORT_PG')
USER_PG = os.getenv('USER_PG')
HOST_PG = os.getenv('HOST_PG')

def UpdateBasket(id_user: str, id_item: str, count: int) -> str:
    return_data = 'Success'
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if count == 0:
            cursor.execute("DELETE FROM basket WHERE id_user = %s and id_item = %s", (id_user, id_item))
        elif count >0:
            cursor.execute("""
                INSERT INTO basket (id_user, id_item, count)
                VALUES (%s, %s, %s)
                ON CONFLICT (id_user, id_item)
                DO UPDATE SET count = %s;
            """, (id_user, id_item, count, count))
        else:
            return_data = "count < 0"

        pg.commit()
        logging.info('Корзина обновлена')

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if cursor:
            cursor.close()
        if pg:
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            
    return return_data


@app.route("/basket/update-item", methods=['PUT'])
@chek_for_user
def add_item():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = UpdateBasket(session.get("id"), post_data.get("id"), post_data.get('count'))

    return jsonify(response_object)





print(UpdateBasket("9bcf470a-548b-4949-995e-d4ca7eac6980", "41c0b0e4-7cba-4a81-b590-23edabe6637b", 6))