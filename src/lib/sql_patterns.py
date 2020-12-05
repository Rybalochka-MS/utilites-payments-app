# add new company
ADD_NEW_COMPANY = "\
INSERT INTO UTILITES_PAYMENT.COMPANY_NAME(company_name) \
VALUES ('{}');\
"

# show all company names
SHOW_ALL_COMPANY = "\
SELECT company_name FROM UTILITES_PAYMENT.COMPANY_NAME;\
"

GET_ALL_COMPANY = "\
SELECT company_id, company_name FROM UTILITES_PAYMENT.COMPANY_NAME;\
"

# add new billing
ADD_NEW_BILLING = "\
INSERT INTO UTILITES_PAYMENT.BILLINGS(company_id, billing_name, billing, create_date, total_bill_sum, billing_sum) \
VALUES ({}, '{}', {}, CURDATE(), {}, {});\
"

GET_ALL_BILLINGS = "\
SELECT billing_id, billing FROM UTILITES_PAYMENT.BILLINGS;\
"

SHOW_ALL_BILLINGS = "\
SELECT company.company_name, bill.billing_name, bill.billing \
FROM UTILITES_PAYMENT.BILLINGS as bill \
LEFT JOIN UTILITES_PAYMENT.COMPANY_NAME as company \
ON bill.company_id = company.company_id;\
"

# add new payment
ADD_NEW_PAYMENT = "\
INSERT INTO UTILITES_PAYMENT.PAYMENTS(billing_id, payment_datetime, payment_sum) \
VALUES ({}, STR_TO_DATE('{}', '%Y-%m-%d'), {});\
"

# show all payments by
SHOW_ALL_PAYMENTS = "\
SELECT cn.company_name, bill.billing_name, bill.billing, \
       bill.create_date, bill.total_bill_sum, bill.billing_sum, \
       pmts.payment_datetime, pmts.payment_sum \
FROM UTILITES_PAYMENT.PAYMENTS as pmts \
LEFT JOIN UTILITES_PAYMENT.BILLINGS as bill \
ON pmts.billing_id = bill.billing_id \
LEFT JOIN UTILITES_PAYMENT.COMPANY_NAME cn \
ON bill.company_id = cn.company_id \
"

SELECT_BILLING_SUM = "\
SELECT billing_sum FROM UTILITES_PAYMENT.BILLINGS \
WHERE billing_id = {};\
"

UPDATE_BILLING_SUM = "\
UPDATE UTILITES_PAYMENT.BILLINGS \
SET total_bill_sum = {} \
WHERE billing_id = {}; \
"

