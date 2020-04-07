# Format array from DataBase to HTML
def company_table_formatter(company_names):
    rows = ""
    for row in company_names:
        rows = rows + "<tr>\n   <td>{}</td>\n</tr>\n".format(row[0])
    return rows
