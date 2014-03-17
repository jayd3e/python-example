from pyramid.view import view_config


@view_config(route_name='index',
             renderer='string')
def hello_world(request):
    return 'hello world'
