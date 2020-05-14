CREATE TABLE BILLINGS (
    billing_id INT NOT NULL,
    company_id INT NOT NULL,
    billing_name VARCHAR(150),
    billing INT NOT NULL,
    create_date VARCHAR(10),
    total_bill_sum INT NOT NULL DEFAULT 0,
    billing_sum INT NOT NULL,
    CONSTRAINT pr_billing_id PRIMARY KEY(billing_id),
    CONSTRAINT fr_company_id FOREIGN KEY(company_id) REFERENCES COMPANY_NAME(company_id)
);