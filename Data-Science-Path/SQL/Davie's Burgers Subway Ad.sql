-- Davie's Burgers Subway Ad

-- What are the column names?
SELECT * FROM orders LIMIT 10;

-- Use DISTINCT to find out all the unique order_date values in this table.
SELECT DISTINCT order_date FROM orders
ORDER BY order_date DESC;

-- write a query that selects only the special_instructions column.
-- Limit the result to 20 rows.
SELECT special_instructions FROM orders LIMIT 20;

-- edit a query to return the special instructions that are not empty
SELECT special_instructions FROM orders
WHERE special_instructions IS NOT NULL;

--  sort the instructions in alphabetical order (A-Z).
SELECT special_instructions FROM orders
WHERE special_instructions IS NOT NULL
ORDER BY special_instructions;

-- search for special instructions that have the word ‘sauce
SELECT special_instructions FROM orders
WHERE special_instructions LIKE '%sauce%';

-- search for special instructions that have the word ‘door’
SELECT special_instructions FROM orders
WHERE special_instructions LIKE '%door%';

-- search for special instructions that have the word ‘box’
SELECT special_instructions FROM orders
WHERE special_instructions LIKE '%box%';

-- what are  order numbers of boxes?
-- For more readability, rename id as ‘#’ and rename special_instructions as ‘Notes’
SELECT id, special_instructions FROM orders
WHERE special_instructions LIKE '%box%';

SELECT id AS '#', special_instructions AS 'Notes'FROM orders
WHERE special_instructions LIKE '%box%';