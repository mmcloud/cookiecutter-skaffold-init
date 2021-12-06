"""
A sample server.
"""
import os
import socket


from flask import Flask, render_template

import socket


from flask import Flask, render_template


# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def home():
    host = socket.gethostname()
    return render_template('index.html',
        host=host)


@app.route('/health')
def health():
    return "Healthy"

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')