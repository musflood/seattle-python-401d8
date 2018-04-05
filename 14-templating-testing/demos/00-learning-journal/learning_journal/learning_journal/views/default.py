from pyramid.view import view_config
from ..sample_data import MOCK_ENTRIES


@view_config(
    route_name='home',
    renderer='../templates/base.jinja2',
    request_method='GET')
def home_view(request):
    return {}


@view_config(
    route_name='auth',
    renderer='../templates/auth.jinja2',
    request_method='GET')
def auth_view(request):
    return {}


@view_config(
    route_name='detail',
    renderer='../templates/detail.jinja2',
    request_method='GET')
def detail_view(request):
    return {}


@view_config(
    route_name='entries',
    renderer='../templates/entries.jinja2',
    request_method='GET')
def entries_view(request):
    return {
        'entries': MOCK_ENTRIES,  # 'entries' is the reference we use in the template
        'message': 'Hello world'}


@view_config(
    route_name='new',
    renderer='../templates/new.jinja2',
    request_method='GET')
def new_view(request):
    return {}


