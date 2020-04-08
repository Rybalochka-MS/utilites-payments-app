"""
    Program for work with DataBase. DataBase store utilities payments.
    DB store: company name, payment name, company billings with payments details.

    DataBase (MySQL) structure:
        CompanyName table (company_id, company_name)
        Billings table (billing_id, company_id, billing_name, billing, create_date,
                        total_bill_sum, billing_sum)
        Payments table (payment_id, billing_id, payment_datetime, payment_sum)
"""
import mysql.connector
from src import load_properties
from src.lib.sql_functions import *

# connect to DataBase
hst, usr, password = load_properties.get_db_credentials()
data_base_connection = mysql.connector.connect(host=hst, user=usr, passwd=password)


# add new company
def add_new_company(company_name):
    insert_new_company(data_base_connection, company_name)


# show all company names
def show_all_company():
    select = select_all_company(data_base_connection)
    return select


# get all company names and id companies
def get_company_list():
    select = get_all_company(data_base_connection)
    return select


# add new billing
def add_new_billing(billing_data):
    insert_new_billing(data_base_connection, billing_data)


def select_billing_list():
    select = select_billing(data_base_connection)
    return select


# get all company bills and bills id
def get_bill_list():
    select = get_all_bill(data_base_connection)
    return select


# add new payment
def add_new_payment(payment_data):
    insert_new_payment(data_base_connection, payment_data)


# show all payments
def show_all_payments(where):
    select = select_all_payments(data_base_connection, where)
    return select


def upd_billing_sum(payment_data):
    billing_sum = select_billing_sum(data_base_connection, int(payment_data[0]))
    new_billing_sum = int(billing_sum[0][0]) + int(payment_data[2])
    update_billing_sum(data_base_connection, int(payment_data[0]), new_billing_sum)
