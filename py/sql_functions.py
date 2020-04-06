from py.sql_patterns import *


# add new company
def insert_new_company(connection, values):
    cursor = connection.cursor()
    print(ADD_NEW_COMPANY.format(values))
    cursor.execute(ADD_NEW_COMPANY.format(values))
    connection.commit()


# show all company names
def select_all_company(connection):
    cursor = connection.cursor()
    cursor.execute(SHOW_ALL_COMPANY)
    return cursor.fetchall()


# add new billing
def insert_new_billing(connection, values):
    cursor = connection.cursor()
    cursor.execute(ADD_NEW_BILLING.format(values))
    connection.commit()


# add new payment
def insert_new_payment(connection, values):
    cursor = connection.cursor()
    cursor.execute(ADD_NEW_PAYMENT.format(values))
    connection.commit()


# show all payments by
def select_all_payments(connection):
    cursor = connection.cursor()
    cursor.execute(SHOW_ALL_PAYMENTS)
    return cursor.fetchall()


# date
def select_all_payments_by_date(connection, values):
    cursor = connection.cursor()
    cursor.execute(SHOW_ALL_PAYMENTS_BY_DATETIME.format(values))
    return cursor.fetchall()


# total payment sum
def select_all_payments_by_sum(connection, values):
    cursor = connection.cursor()
    cursor.execute(SHOW_ALL_PAYMENTS_BY_SUM.format(values))
    return cursor.fetchall()


# total billed sum
def select_all_payments_by_bill_sum(connection, values):
    cursor = connection.cursor()
    cursor.execute(SHOW_ALL_PAYMENTS_BY_BILL_SUM.format(values))
    return cursor.fetchall()
