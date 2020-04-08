from bottle import get, post, error, static_file, request
from src.data_base_manipulation import *
from src.lib.sql_functions import create_filter
from src.response_pages import company_name_response, billing_response, all_payments_response
from src.request_pages import new_billing_request, new_payment_request, all_payments_request


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
    billing_data = (
        request.forms.get('company_id'),
        request.forms.get('billing_name'),
        request.forms.get('billing'),
        request.forms.get('total_bill_sum'),
        request.forms.get('billing_sum')
    )
    add_new_billing(billing_data)
    response_page = billing_response()
    return response_page


@get('/add_payment')
def get_payment():
    request_page = new_payment_request()
    return request_page


@post('/add_payment')
def add_payment():
    payment_data = (
        request.forms.get('billing_id'),
        request.forms.get('payment_date'),
        request.forms.get('payment_sum')
    )
    add_new_payment(payment_data)
    upd_billing_sum(payment_data)
    return show_all()


@get('/show_all')
def show_all():
    request_page = all_payments_request()
    return request_page


@post('/show_all')
def show_all_by_filter():
    payment_date = request.forms.get('payment_date')
    payment_sum = request.forms.get('payment_sum')
    bill_sum = request.forms.get('bill_sum')
    select_filter = create_filter(payment_date, payment_sum, bill_sum)
    response_page = all_payments_response(select_filter)
    return response_page


@error(404)
def error_page(err):
    return static_file('error.html', root='./html/')
