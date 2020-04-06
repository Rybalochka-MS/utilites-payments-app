from bottle import get, post, error, static_file, request
from py.data_base_manipulation import *


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
    rows = ""
    for row in all_companies:
        rows = rows + "<tr>\n   <td>{}</td>\n</tr>\n".format(row[0])
    page_file = open('./html/view_companies.html', 'r', encoding='utf-8')
    buf = page_file.read()
    page_file.close()
    page = buf.replace('{}', rows)
    return page


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
