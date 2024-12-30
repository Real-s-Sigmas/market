import logging, psycopg2, check

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from psycopg2 import extras, Error
from typing import Union, Optional, Tuple

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

logging.info("other.py have connected")

@app.route('/other/session', methods=['GET'])
def sessionr():
    responce_object = {'status': 'success'}
    responce_object['res'] = check.IsInSession()
    return jsonify(responce_object)

@app.route('/other/id', methods=['GET'])
def idr():
    responce_object = {'status': 'success'}
    responce_object['res'] = check.GetId()
    return jsonify(responce_object)

@app.route('/other/is-admin', methods=['GET'])
def is_admin():
    responce_object = {'status': 'success'}
    responce_object['res'] = check.IsAdminSession()
    return jsonify(responce_object)

@app.route('/other/get-avatar', methods=['GET'])
def get_avatar():
    responce_object = {'status': 'success'}
    return jsonify(responce_object)
