from bottle import get, post, error, static_file, request
from py.data_base_manipulation import *


@get('/')
def menu():
    return static_file('index.html', root='./html/')


@get('/add_company')
def add_company():
    return static_file('add_company.html', root='./html/')


@post('/add_company')
def save_new_company():
    name = request.forms.get('company_name')
    add_new_company(name)
    return "<p>Success</p>"


@get('/add_bill')
def add_bill():
    return "Wait update"


@get('/add_payment')
def add_payment():
    return "Wait update"


@get('/show_all')
def show_all():
    return "Wait update"


@error(404)
def error_page(err):
    return static_file('error.html', root='./html/')
