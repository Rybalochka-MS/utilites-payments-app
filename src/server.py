from bottle import get, post, error, static_file, request
from src.data_base_manipulation import *
from src.response_pages import company_name_response
from src.request_pages import new_billing_request


@get('/')
def menu():
    return static_file('index.html', root='./src/html/')


@get('/add_company')
def company_page():
    return static_file('add_company.html', root='./src/html/')


@post('/add_company')
def add_company():
    add_new_company(request.forms.get('company_name'))
    response_page = company_name_response()
    return response_page


@get('/add_bill')
def get_bill():
    request_page = new_billing_request()
    return request_page


@post('/add_bill')
def add_bill():
    return ""


@get('/add_payment')
def get_payment():
    return "Wait update"


@post('/add_payment')
def add_payment():
    return ""


@get('/show_all')
def show_all():
    return "Wait update"


@error(404)
def error_page(err):
    return static_file('error.html', root='./html/')
