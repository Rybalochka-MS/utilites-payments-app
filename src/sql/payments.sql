CREATE TABLE PAYMENTS (
    payment_id INT NOT NULL,
    billing_id INT NOT NULL,
    payment_datetime VARCHAR(17) NOT NULL,
    payment_sum INT NOT NULL,
    CONSTRAINT pr_payment_id PRIMARY KEY(payment_id),
    CONSTRAINT fr_billing_id FOREIGN KEY(billing_id) REFERENCES BILLINGS(billing_id)
);