# add new company
ADD_NEW_COMPANY = "\
INSERT INTO utilites_payment.company_name(company_name) \
VALUES ('{}');\
"

# show all company names
SHOW_ALL_COMPANY = "\
SELECT company_name FROM utilites_payment.company_name;\
"

GET_ALL_COMPANY = "\
SELECT company_id, company_name FROM utilites_payment.company_name;\
"

# add new billing
ADD_NEW_BILLING = "\
INSERT INTO utilites_payment.billings(company_id, billing_name, billing, create_date, total_bill_sum, billing_sum) \
VALUES ('{}, {}, {}, CURDATE(), {}, {}');\
"

GET_ALL_BILLINGS = "\
SELECT billing_id, billing FROM utilites_payment.billings;\
"

# add new payment
ADD_NEW_PAYMENT = "\
INSERT INTO utilites_payment.payments(billing_id, payment_datetime, payment_sum) \
VALUES ('{}, STR_TO_DATE({}, 'dd-mm-yyyy'), {}');\
"

# show all payments by
SHOW_ALL_PAYMENTS = "\
SELECT cn.company_name, bill.billing_name, bill.billing, \
       bill.create_date, bill.total_bill_sum, bill.billing_sum, \
       pmts.payment_datetime, pmts.payment_sum \
FROM utilites_payment.payments as pmts \
LEFT JOIN utilites_payment.billings as bill \
ON pmts.billing_id = bill.billing_id \
LEFT JOIN utilites_payment.company_name cn \
ON bill.company_id = cn.company_id; \
"

# date
SHOW_ALL_PAYMENTS_BY_DATETIME = "\
SELECT cn.company_name, bill.billing_name, bill.billing, \
       bill.create_date, bill.total_bill_sum, bill.billing_sum, \
       pmts.payment_datetime, pmts.payment_sum \
FROM utilites_payment.payments as pmts \
LEFT JOIN utilites_payment.billings as bill \
ON pmts.billing_id = bill.billing_id \
LEFT JOIN utilites_payment.company_name cn \
ON bill.company_id = cn.company_id \
WHERE payment_datetime = STR_TO_DATE('{}', 'dd-mm-yyyy'); \
"

# total payment sum
SHOW_ALL_PAYMENTS_BY_SUM = " \
SELECT cn.company_name, bill.billing_name, bill.billing, \
       bill.create_date, bill.total_bill_sum, bill.billing_sum, \
       pmts.payment_datetime, pmts.payment_sum \
FROM utilites_payment.payments as pmts \
LEFT JOIN utilites_payment.billings as bill \
ON pmts.billing_id = bill.billing_id \
LEFT JOIN utilites_payment.company_name cn \
ON bill.company_id = cn.company_id \
WHERE payment_sum = '{}'; \
"

# total billed sum
SHOW_ALL_PAYMENTS_BY_BILL_SUM = "\
SELECT cn.company_name, bill.billing_name, bill.billing, \
       bill.create_date, bill.total_bill_sum, bill.billing_sum, \
       pmts.payment_datetime, pmts.payment_sum \
FROM utilites_payment.payments as pmts \
LEFT JOIN utilites_payment.billings as bill \
ON pmts.billing_id = bill.billing_id \
LEFT JOIN utilites_payment.company_name cn \
ON bill.company_id = cn.company_id \
WHERE billing_sum = '{}'; \
"
