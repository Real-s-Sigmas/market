import logging, psycopg2, check, uuid

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from psycopg2 import extras, Error
from typing import Union, Optional, Tuple
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("admin.py have connected")


def AddComment(id_user: str, id_item: str, content: str, stars: int) -> str:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''INSERT INTO comments(id, id_user, id_item, content, stars, data_c) 
                        VALUES (
                        '{uuid.uuid4().hex}', 
                        '{id_user}',
                        '{id_item}'
                        '{check.EscapeQuotes(content)}',
                        '{stars}'
                        '{datetime.now().isoformat()}'
                        )''')
        pg.commit()

        return_data = "ok"

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route('/comments/add-comment', methods=['POST'])
def add_comment():
    responce_object = {'status': 'success'}

    data = request.get_json()

    if check.IsInSession():
        if request.args.get('stars') >= 1 and request.args.get('stars') <= 5:
            responce_object['res'] = AddComment(
                                        data.get('id_user'), 
                                        data.get('id_item'), 
                                        data.get('content'), 
                                        data.get('stars')
                                    )
        else:
            responce_object['res'] = 'Incorrect data'
    else:
        responce_object["res"] = "Not in session"

    return jsonify(responce_object)


def GetComments(id_item: str) -> Union[list, str]:
    return


@app.route('/comments/show-comments', methods=['GET'])
def get_comments():
    responce_object = {'status': 'success'}

    if check.IsInSession():
        responce_object['res'] = GetComments(request.args.get('id'))
    else:
        responce_object["res"] = "Not in session"

    return jsonify(responce_object)