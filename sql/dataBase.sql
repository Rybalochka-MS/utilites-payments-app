DROP DATABASE IF EXISTS UTILITES_PAYMENT;
CREATE DATABASE UTILITES_PAYMENT;
USE UTILITES_PAYMENT;

CREATE TABLE COMPANY_NAME (
    company_id INT NOT NULL AUTO_INCREMENT,
    company_name VARCHAR(100),
    CONSTRAINT pr_company_name PRIMARY KEY(company_id)
);

CREATE TABLE BILLINGS (
    billing_id INT NOT NULL AUTO_INCREMENT,
    company_id INT NOT NULL,
    billing_name VARCHAR(150),
    billing INT NOT NULL,
    create_date DATE,
    total_bill_sum INT NOT NULL DEFAULT 0,
    billing_sum INT NOT NULL,
    CONSTRAINT pr_billing_id PRIMARY KEY(billing_id),
    CONSTRAINT fr_company_id FOREIGN KEY(company_id) REFERENCES COMPANY_NAME(company_id)
);

CREATE TABLE PAYMENTS (
    payment_id INT NOT NULL AUTO_INCREMENT,
    billing_id INT NOT NULL,
    payment_datetime datetime NOT NULL,
    payment_sum INT NOT NULL,
    CONSTRAINT pr_payment_id PRIMARY KEY(payment_id),
    CONSTRAINT fr_billing_id FOREIGN KEY(billing_id) REFERENCES BILLINGS(billing_id)
);

INSERT INTO COMPANY_NAME(company_id, company_name)
VALUES (1, 'UkrGAs');
INSERT INTO COMPANY_NAME(company_id, company_name)
VALUES (2, 'Gorodok');

INSERT INTO BILLINGS(billing_id, company_id, billing_name, billing, create_date, total_bill_sum, billing_sum)
VALUES (1, 1, 'Оплата газу', 32313144, get_format(datetime , curdate()), 0, 250);

INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum)
VALUES (1, 1, curdate(), 600);
INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum)
VALUES (2, 1, curdate(), 350);
INSERT INTO PAYMENTS(payment_id, billing_id, payment_datetime, payment_sum)
VALUES (3, 1, curdate(), 200);