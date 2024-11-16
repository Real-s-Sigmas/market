import logging, psycopg2, check, uuid

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from psycopg2 import extras, Error
from typing import Union, Optional, Tuple
from datetime import datetime
from check import chek_for_user

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("comments.py have connected")


#====ReuseCompInThisFile==================================================================================================================================================================

def IsTrueUser(id_comment: str) -> bool:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT id_user FROM comments WHERE id = $${id_comment}$$ ORDER BY data")

        true_user = cursor.fetchall()[0][0]

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return true_user==session.get('id')

#========================================================================================================================================================================================


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
@chek_for_user
def add_comment():
    responce_object = {'status': 'success'}

    data = request.get_json()

    if request.args.get('stars') >= 1 and request.args.get('stars') <= 5:
        responce_object['res'] = AddComment(
                                    data.get('id_user'), 
                                    data.get('id_item'), 
                                    data.get('content'), 
                                    data.get('stars')
                                )
    else:
        responce_object['res'] = 'Incorrect data'


    return jsonify(responce_object)


def GetComments(id_item: str) -> Union[list, str]:
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM orders WHERE id_item = $${id_item}$$ ORDER BY data")

        data_ = cursor.fetchall()
        return_data = []
        for row in data_:
            return_data.append(dict(row))

        logging.info('Все коментарии показаны')

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close()
            pg.close()
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route('/comments/show-comments', methods=['GET'])
@chek_for_user
def get_comments():
    responce_object = {'status': 'success'}

    responce_object['res'] = GetComments(request.args.get('id'))

    return jsonify(responce_object)


def DeleteComment(id_comment: str) -> str:
    try:       
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f'''DELETE FROM vr WHERE id=$${id_comment}$$''')
        
        pg.commit()
        return_data = 'Success'
    except (Exception, Error) as error:
        logging.error(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        return return_data


@app.route('/comments/delete-comment', methods=['DELETE'])
@chek_for_user
def delete_comment():
    responce_object = {'status': 'success'}

    if IsTrueUser(request.args.get('id')):
        responce_object['res'] = DeleteComment(request.args.get('id'))

    return jsonify(responce_object)
        

def ChangeComment(id_comment: str, content: str, stars: int):
    try:
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"""UPDATE comments
                           SET content=$${content}$$, stars=$${stars}$$ 
                           WHERE id=$${id_comment}$$;""")
        pg.commit()

        return_data = "Success"
        logging.info('Данные о коментарии обновлены')

    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = f"Error"

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route('/coomments/change-comment', methods=['PUT'])
@chek_for_user
def change_comment():
    responce_object = {'status': 'success'}

    data = request.get_json()
    
    if IsTrueUser(request.args.get('id')):
        responce_object['res'] = ChangeComment(
                                    data.get('id'),
                                    data.get('content'),
                                    data.get('stars')
                                )
    else:
        responce_object["res"] = "From another user"

    return jsonify(responce_object)