from src.data_base_manipulation import *
from src.lib.web_formater import *
from src.lib.utilites import read_file


# Create request page for add new billing for company
def new_billing_request():
    all_company = get_company_list()
    company_list = create_company_list(all_company)
    page = read_file("./src/html/add_billing.html")
    page = page.replace("{}", company_list)
    return page
