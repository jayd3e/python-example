from pyramid.config import Configurator


def main(global_config, **settings):
    '''Main config function'''

    config = Configurator(settings=settings)

    # routes
    config.add_route('index', '/')

    # views
    config.scan('.views')

    return config.make_wsgi_app()
