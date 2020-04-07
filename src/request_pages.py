from src.data_base_manipulation import *
from src.lib.web_formater import *
from src.lib.utilites import read_file


# Create request page for add new billing for company
def new_billing_request():
    all_company = get_company_list()
    company_list = create_list(all_company)
    page = read_file("./src/html/add_billing.html")
    page = page.replace("{}", company_list)
    return page


# Create request page for add new utilities payment
def new_payment_request():
    all_bills = get_bill_list()
    bill_list = create_list(all_bills)
    page = read_file("./src/html/add_payment.html")
    page = page.replace("{}", bill_list)
    return page


# Create request page for view all utilities payments
def all_payments_request():
    all_payments = show_all_payments()
    all_payments_list = all_payments_formatter(all_payments)
    page = read_file("./src/html/show_all.html")
    page = page.replace("{}", all_payments_list)
    return page
