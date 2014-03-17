import os

from pyramid.config import Configurator
from paste.deploy import loadapp
from waitress import serve


def main(global_config, **settings):
    '''Main config function'''

    config = Configurator(settings=settings)

    # routes
    config.add_route('index', '/')

    # views
    config.scan('.views')

    return config.make_wsgi_app()


def web():
    port = int(os.environ['PORT'])

    app = loadapp('config:production.ini', relative_to='.')
    serve(app, host='0.0.0.0', port=port)
