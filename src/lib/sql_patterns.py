# add new company
ADD_NEW_COMPANY = "\
INSERT INTO COMPANY_NAME(company_id, company_name) \
VALUES ({}, '{}');\
"

# select count row from table
SELECT_COUNT = "SELECT COUNT(*) FROM {}"

# show all company names
SHOW_ALL_COMPANY = "\
SELECT company_name FROM COMPANY_NAME;\
"

GET_ALL_COMPANY = "\
SELECT company_id, company_name FROM COMPANY_NAME;\
"

# add new billing
ADD_NEW_BILLING = "\
INSERT INTO BILLINGS(billing_id, company_id, billing_name, billing, create_date, total_bill_sum, billing_sum) \
VALUES ({}, {}, '{}', {}, date(), {}, {});\
"

GET_ALL_BILLINGS = "\
SELECT billing_id, billing FROM BILLINGS;\
"

SHOW_ALL_BILLINGS = "\
SELECT company.company_name, bill.billing_name, bill.billing \
FROM BILLINGS as bill \
LEFT JOIN COMPANY_NAME as company \
ON bill.company_id = company.company_id;\
"

# add new payment
ADD_NEW_PAYMENT = "\
INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum) \
VALUES ({}, {}, strftime('%Y-%m-%d', '{}'), {});\
"

# show all payments by
SHOW_ALL_PAYMENTS = "\
SELECT cn.company_name, bill.billing_name, bill.billing, \
       bill.create_date, bill.total_bill_sum, bill.billing_sum, \
       pmts.payment_datetime, pmts.payment_sum \
FROM PAYMENTS as pmts \
LEFT JOIN BILLINGS as bill \
ON pmts.billing_id = bill.billing_id \
LEFT JOIN COMPANY_NAME cn \
ON bill.company_id = cn.company_id \
"

SELECT_BILLING_SUM = "\
SELECT billing_sum FROM BILLINGS \
WHERE billing_id = {};\
"

UPDATE_BILLING_SUM = "\
UPDATE BILLINGS \
SET total_bill_sum = {} \
WHERE billing_id = {}; \
"
