# Format array from DataBase to HTML
def company_table_formatter(company_names):
    rows = ""
    for row in company_names:
        rows = rows + "<tr>\n   <td>{}</td>\n</tr>\n".format(row[0])
    return rows


# Format array from DataBase to HTML
def billing_table_formatter(all_bills_data):
    rows = ""
    for row in all_bills_data:
        rows = rows + "<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>\n".format(row[0], row[1], row[2])
    return rows


# Format array from DataBase to HTML
def all_payments_formatter(all_payments_data):
    rows = ""
    for row in all_payments_data:
        rows = rows + "<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n" \
                      "<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>\n"\
            .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    return rows


# Create list all companies
def create_list(id_and_name):
    company_list = ""
    for item in id_and_name:
        company_list = company_list + "<option value={}>{}</option>\n"\
            .format(item[0], item[1])
    return company_list
