import uuid, psycopg2, logging

from psycopg2 import Error
from flask import jsonify, request
from typing import Union
from app import *
from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from check import chek_for_admin
import check
import redis

#TODO: редис
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)


def AddItemToBasket(id_item: str, id_u: str) -> str:
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)

        r.set(id_u, id_item)
        # print(value.decode('utf-8'))
        return_data = "Ok"

    except (redis.RedisError, Exception) as e:
        print(f"Ошибка: {e}")
        return_data


@app.route("/basket/add-item", methods=['POST'])
@chek_for_user
def add_item():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = AddItemToBasket(post_data.get("id"), session.get("id"))

    return jsonify(response_object)



def DeleteItemToBasket(id_item: str, id_u: str) -> str:
    pass


@app.route("/basket/delete-item", methods=['POST'])
@chek_for_user
def delete_item():
    response_object = {'status': 'success'} #БаZа
    post_data = request.get_json()

    response_object["res"] = DeleteItemToBasket(post_data.get("id"), session.get("id"))

    return jsonify(response_object)



def ShowwItemFromBasket(id_item: str, id_u: str) -> str:
    pass


@app.route("/basket/get-item", methods=['POST'])
@chek_for_user
def delete_item():
    response_object = {'status': 'success'} #БаZа

    response_object["res"] = ShowwItemFromBasket(request.args.get('id'))

    return jsonify(response_object)