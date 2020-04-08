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
    all_billing_data = get_bill_list()
    rows = billing_table_formatter(all_billing_data)
    page = read_file('./src/html/view_bills.html')
    page = page.replace("{}", rows)
    return page
