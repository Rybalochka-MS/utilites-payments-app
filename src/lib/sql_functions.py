from src.lib.sql_patterns import *


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


# show all company names and id companies
def get_all_company(connection):
    cursor = connection.cursor()
    cursor.execute(GET_ALL_COMPANY)
    return cursor.fetchall()


# add new billing
def insert_new_billing(connection, values):
    cursor = connection.cursor()
    cursor.execute(ADD_NEW_BILLING
                   .format(int(values[0]), str(values[1]), int(values[2]), int(values[3]), int(values[4])))
    connection.commit()


# show all company bill and id
def get_all_bill(connection):
    cursor = connection.cursor()
    cursor.execute(GET_ALL_BILLINGS)
    return cursor.fetchall()


def select_billing(connection):
    cursor = connection.cursor()
    cursor.execute(SHOW_ALL_BILLINGS)
    return cursor.fetchall()


# add new payment
def insert_new_payment(connection, values):
    cursor = connection.cursor()
    cursor.execute(ADD_NEW_PAYMENT.format(int(values[0]), str(values[1]), int(values[2])))
    connection.commit()


# show all payments by
def select_all_payments(connection, value):
    cursor = connection.cursor()
    if len(value) == 0:
        cursor.execute(SHOW_ALL_PAYMENTS)
    else:
        cursor.execute(SHOW_ALL_PAYMENTS + value)
    return cursor.fetchall()


def create_filter(payment_date, payment_sum, bill_sum):
    select_filter = "WHERE "
    if len(payment_date) > 0:
        select_filter = select_filter + "payment_datetime = STR_TO_DATE('{}', '%Y-%m-%d')".format(payment_date)
    if len(payment_sum) > 0:
        if len(select_filter) > 6:
            select_filter += " AND "
        select_filter = select_filter + "payment_sum = {}".format(payment_sum)
    if len(bill_sum) > 0:
        if len(select_filter) > 6:
            select_filter += " AND "
        select_filter = select_filter + "billing_sum = {}".format(bill_sum)
    if len(select_filter) <= 6:
        return ""
    else:
        return select_filter


def select_billing_sum(connection, billing_id):
    cursor = connection.cursor()
    cursor.execute(SELECT_BILLING_SUM.format(billing_id))
    return cursor.fetchall()


def update_billing_sum(connection, billing_id, billing_sum):
    cursor = connection.cursor()
    print(UPDATE_BILLING_SUM.format(billing_sum, billing_id))
    cursor.execute(UPDATE_BILLING_SUM.format(billing_sum, billing_id))
    connection.commit()

