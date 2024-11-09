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

logging.info("admin.py have connected")

@app.route('/other/session', methods=['GET'])
def all_orders():
    responce_object = {'status': 'success'}
    responce_object['res'] = check.IsInSession()
    return jsonify(responce_object)

@app.route('/other/id', methods=['GET'])
def all_orders():
    responce_object = {'status': 'success'}
    responce_object['res'] = check.GetId()
    return jsonify(responce_object)

@app.route('/other/is-admin', methods=['GET'])
def all_orders():
    responce_object = {'status': 'success'}
    responce_object['res'] = check.IsAdminSession()
    return jsonify(responce_object)

@app.route('/other/get-avatar', methods=['GET'])
def get_avatar():
    responce_object = {'status': 'success'}
    return jsonify(responce_object)

@app.route('/topic/<path:filename>')
def serve_file(filename):
    path = filename
    # if not os.path.exists('{}/{}'.format('avatar/', filename)):
    #     logging.info({'error': 'File not found'}, 404)
    #     return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory='topic-photo/', path=path)

@app.route('/item/<path:filename>')
def serve_file(filename):
    path = filename
    # if not os.path.exists('{}/{}'.format('avatar/', filename)):
    #     logging.info({'error': 'File not found'}, 404)
    #     return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory='items-photo/', path=path)