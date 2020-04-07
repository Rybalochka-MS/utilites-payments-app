from bottle import get, post, error, static_file, request
from src.data_base_manipulation import *
from src.lib.utilites import read_file
from src.lib.web_formater import *


@get('/')
def menu():
    return static_file('index.html', root='./html/')


@get('/add_company')
def company_page():
    return static_file('add_company.html', root='./html/')


@post('/add_company')
def add_company():
    add_new_company(request.forms.get('company_name'))
    all_companies = show_all_company()
    rows = company_table_formatter(all_companies)
    page = read_file('./src/html/view_companies.html')
    page = page.replace('{}', rows)
    return page


@get('/add_bill')
def get_bill():
    return "Wait update"


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
