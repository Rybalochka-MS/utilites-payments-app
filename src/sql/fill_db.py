import sqlite3
from src.lib.utilites import read_file


def fill_db():
    connection = sqlite3.connect("utilitiesPayment.sqlite3")
    cursor = connection.cursor()
    fill_data = read_file("src/sql/fill_db.sql")
    insert_list = fill_data.split(';')
    for insert in insert_list:
        cursor.execute(insert)
        connection.commit()
    cursor.close()
    connection.close()
