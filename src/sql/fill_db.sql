INSERT INTO COMPANY_NAME(company_id, company_name)
VALUES (1, 'UkrGAs');
INSERT INTO COMPANY_NAME(company_id, company_name)
VALUES (2, 'Gorodok');
INSERT INTO BILLINGS(billing_id, company_id, billing_name, billing, create_date, total_bill_sum, billing_sum)
VALUES (1, 1, 'Оплата газу', 32313144, '2020-05-05', 0, 250);
INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum)
VALUES (1, 1, '2020-05-05', 600);
INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum)
VALUES (2, 1, '2020-05-05', 350);
INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum)
VALUES (3, 1, '2020-05-05', 200);