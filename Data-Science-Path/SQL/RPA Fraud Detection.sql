-- RPA Fraud Detection

-- Reputable Product Agency (RPA) has started receiving complaints from their credit card processor about fraudulent transactions. Help your finance department identify potentially risky transactions before they finish processing.

-- what are the column names of transaction_data table
SELECT * FROM transaction_data LIMIT 10;

--Find the full_names and emails of the transactions listing 20252 as the zip code.
SELECT full_name, email, zip FROM transaction_data WHERE zip = 20252;

-- The fraudsters thought it would be funny to use ‘Art Vandelay’ for their full name or add a ‘der’ for their middle name.
-- Use a query to find the names and emails associated with these transactions.
SELECT full_name, email FROM transaction_data
WHERE full_name = 'Art Vandelay'
   OR full_name LIKE '% der %';

-- any IP address beginning with ‘10.’ is reserved for internal use.
-- Find the ip_addresses and emails listed with these transactions.
SELECT ip_address, email FROM transaction_data
WHERE ip_address LIKE '10.%';

-- Find the emails in transaction_data with ‘temp_email.com’ as a domain 
SELECT email FROM transaction_data
WHERE email LIKE '%temp_email.com';

-- find the transaction occurred from an ip address starting with ‘120.’ and their full name starts with ‘John’
SELECT * from transaction_data 
WHERE ip LIKE"120.%" and full_name LIKE "John%";