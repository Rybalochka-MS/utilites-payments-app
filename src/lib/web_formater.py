# Format array from DataBase to HTML
def company_table_formatter(company_names):
    rows = ""
    for row in company_names:
        rows = rows + "<tr>\n   <td>{}</td>\n</tr>\n".format(row[0])
    return rows


# Create list all companies
def create_company_list(company_id_and_name):
    company_list = ""
    for item in company_id_and_name:
        company_list = company_list + "<option value={}>{}</option>\n"\
            .format(item[0], item[1])
    return company_list
