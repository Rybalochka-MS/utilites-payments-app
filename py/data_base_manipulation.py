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
from py import load_properties
from py.sql_functions import *

# connect to DataBase
hst, usr, password = load_properties.get_db_credentials()
data_base_connection = mysql.connector.connect(host=hst, user=usr, passwd=password)


# add new company
def add_new_company(company_name):
    insert_new_company(data_base_connection, company_name)


# add new billing
def add_new_billing(billing_data):
    insert_new_billing(data_base_connection, billing_data)


# add new payment
def add_new_payment(payment_data):
    insert_new_payment(data_base_connection, payment_data)


# show all payments
def show_all_payments():
    select = select_all_payments(data_base_connection)
    for row in select:
        print(row)


# by date
def show_all_payments_by_date(date):
    select = select_all_payments_by_date(data_base_connection, date)
    for row in select:
        print(row)


# total payment sum
def show_all_payments_by_sum(payment_sum):
    select = select_all_payments_by_sum(data_base_connection, payment_sum)
    for row in select:
        print(row)


# total billed sum
def show_all_payments_by_bill_sum(bill_sum):
    select = select_all_payments_by_bill_sum(data_base_connection, bill_sum)
    for row in select:
        print(row)
