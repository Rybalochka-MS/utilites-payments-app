from src.data_base_manipulation import *
from src.lib.web_formater import *
from src.lib.utilites import read_file


# Send response page after add new company
def company_name_response():
    all_companies = show_all_company()
    rows = company_table_formatter(all_companies)
    page = read_file('./src/html/view_companies.html')
    page = page.replace('{}', rows)
    return page


# Send response page after add new billing
def billing_response():
    all_billing_data = select_billing_list()
    rows = billing_table_formatter(all_billing_data)
    page = read_file('./src/html/view_bills.html')
    page = page.replace("{}", rows)
    return page


# Create response page for view all utilities payments
def all_payments_response(select_filter):
    all_payments = show_all_payments(select_filter)
    all_payments_list = all_payments_formatter(all_payments)
    page = read_file("./src/html/show_all.html")
    page = page.replace("{}", all_payments_list)
    return page
