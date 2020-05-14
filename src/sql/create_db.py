import sqlite3
from os import listdir
from src.lib.utilites import read_file
from src.sql.fill_db import fill_db


def db_already_exist() -> bool:
    directory = listdir("./")
    for item in directory:
        if item == "utilitiesPayment.sqlite3":
            return True
    return False


def create_db():
    if db_already_exist() is not True:
        connection = sqlite3.connect("utilitiesPayment.sqlite3")
        cursor = connection.cursor()
        company_name_table = read_file("src/sql/company_name.sql")
        billings_table = read_file("src/sql/billings.sql")
        payments_table = read_file("src/sql/payments.sql")
        cursor.execute(company_name_table)
        cursor.execute(billings_table)
        cursor.execute(payments_table)
        cursor.close()
        connection.close()
        fill_db()
