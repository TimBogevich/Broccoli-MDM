"""
This script runs the broccoli_mdm application using a development server.
"""

from os import environ
from broccoli_mdm import app
from werkzeug.serving import run_simple

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    run_simple(HOST, PORT, threaded=True)
