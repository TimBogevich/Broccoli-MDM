from os import environ
from broccoli_mdm import app # NOQA
import broccoli_mdm.models # NOQA
import broccoli_mdm.init_models # NOQA
import broccoli_mdm.views # NOQA
import broccoli_mdm.views_api # NOQA
from werkzeug.serving import run_simple


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    run_simple(hostname=HOST, port=PORT, application=app, threaded=True)
