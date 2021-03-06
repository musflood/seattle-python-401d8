# from pyramid.response import Response
from pyramid.view import view_config
import requests

from ..sample_data import MOCK_ENTRIES
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest


API_URL = 'https://api.iextrading.com/1.0'


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2',
    request_method='GET')
def my_home_view(request):
    return {}


@view_config(
    route_name='auth',
    renderer='../templates/auth.jinja2'
    )
def my_auth_view(request):
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}'.format(username, password))

            return HTTPFound(location=request.route_url('portfolio'))

        except KeyError:
            return {}

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Pass: {}, Email: {}'.format(username, password,
                                                     email))

        return HTTPFound(location=request.route_url('portfolio'))

    return HTTPNotFound()


@view_config(
    route_name='portfolio',
    renderer='../templates/portfolio.jinja2',
    request_method='GET')
def my_portfolio_view(request):
    return {
        'entries': MOCK_ENTRIES
    }


@view_config(
    route_name='stock',
    renderer='../templates/stock-add.jinja2')
def my_stock_view(request):
    if request.method == 'POST':
        fields = ['companyName', 'symbol']

        if not all([field in request.POST for field in fields]):
            return HTTPBadRequest()

        try:
            stock = {
                'companyName': request.POST['companyName'],
                'symbol': request.POST['symbol'],
                'exchange': request.POST['exchange'],
                'website': request.POST['website'],
                'CEO': request.POST['CEO'],
                'industry': request.POST['industry'],
                'sector': request.POST['sector'],
                'issueType': request.POST['issueType'],
                'description': request.POST['description'],
            }
        except KeyError:
            pass

        MOCK_ENTRIES.append(stock)
        return HTTPFound(location=request.route_url('portfolio'))

    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']
        except KeyError:
            return {}

        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        data = response.json()
        return {'company': data}

    else:
        raise HTTPNotFound()


@view_config(
    route_name='detail',
    renderer='../templates/stock-detail.jinja2',
    request_method='GET')
def my_detail_view(request):
    symbol = request.matchdict['symbol']
    for stock in MOCK_ENTRIES:
        if stock['symbol'] == symbol:
            return {'stock': stock}
    return {}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid_scaffold_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
