"""
A sample Hello World server.
"""
import os
import requests
import socket


from flask import Flask, render_template

import ms_pb2
import ms_pb2_grpc
import grpc

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    host = socket.gethostname()
    return render_template('index.html',
        host=host)


@app.route('/health')
def health():
    return "Healthy"

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')