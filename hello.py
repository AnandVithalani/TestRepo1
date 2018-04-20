# hello.py

import socket
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello():
    text = 'Hello WORLD from: {0}\n'.format(socket.gethostname())
    resp = Response(text, mimetype='text/plain')
    resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = 0
    return resp

