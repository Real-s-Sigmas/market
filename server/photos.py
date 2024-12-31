import os, base64, logging, re, base64

from app import app, PASSWORD_PG, PORT_PG, USER_PG, HOST_PG, MEDIA, AVATAR
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from functools import wraps
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

load_dotenv()
PATTERN = os.getenv('PATTERN')
API_URL = os.getenv('API_URL')

logging.info("photos.py have connected")


def AddPhoto(base: str, type: str, id: str) -> str:
    mime_type = "."+base[len("data:image/"):base.find(";base64")]
    base=base[base.find(',')+1:]
    decoded_bytes = base64.b64decode(base)
    name = type+'_'+id+mime_type
    with open(os.path.join(MEDIA, name), "wb") as file:
        file.write(decoded_bytes)
    return API_URL+name

def DeletePhotoS(links: list) -> str:
    for link in links:
        name = link[link.find(API_URL)+len(API_URL):]
        if os.path.exists(os.path.join(MEDIA, name)):
            logging.info(name)
            os.remove(os.path.join(MEDIA, name))

@app.route('/items/<path:filename>')
def serve_file(filename):
    path = filename
    # if not os.path.exists('{}/{}'.format('avatar/', filename)):
    #     logging.info({'error': 'File not found'}, 404)
    #     return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory='items/', path=path)
