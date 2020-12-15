--Database Normalization at Fred's Furniture

-- Write a query to select the first 10 rows:
SELECT * FROM store LIMIT 10;

-- Have any customers made more than one order? how many distinct customers are there in the table?
SELECT COUNT(DISTINCT(order_id)) 
FROM store;
SELECT COUNT(DISTINCT(customer_id )) 
FROM store;

-- inspect some of the repeated data in this table: 
SELECT customer_id, customer_email, customer_phone FROM store
WHERE customer_id = 1;

SELECT item_1_id, item_1_name, item_1_price
FROM store
WHERE item_1_id = 4;

-- build customer table from store table:
CREATE TABLE customers AS
SELECT DISTINCT customer_id, customer_phone, customer_email FROM store;

-- designate the customer_id column as the primary key:
ALTER TABLE customers 
ADD PRIMARY KEY (customer_id);

-- create the items table described in the normalized schema: 
CREATE TABLE items AS
SELECT DISTINCT item_1_id as item_id, item_1_name as name, item_1_price as price 
FROM store
UNION
SELECT DISTINCT item_2_id as item_id, item_2_name as name, item_2_price as price
FROM store
WHERE item_2_id IS NOT NULL
UNION
SELECT DISTINCT item_3_id as item_id, item_3_name as name, item_3_price as price
FROM store
WHERE item_3_id IS NOT NULL;

-- Designate the item_id column as the primary key:
ALTER TABLE items
ADD PRIMARY KEY (item_id);

-- create the orders_items table:
CREATE TABLE orders_items AS
SELECT order_id, item_1_id as item_id 
FROM store
UNION ALL
SELECT order_id, item_2_id as item_id
FROM store
WHERE order_id IS NOT NULL
UNION ALL
SELECT order_id, item_3_id as item_id
FROM store
WHERE order_id IS NOT NULL;

--create the orders table described in the normalized schema :
CREATE TABLE orders AS
SELECT order_id, order_date,	customer_id
FROM store;

-- Designate the order_id as the primary key.
ALTER TABLE orders
ADD PRIMARY KEY (order_id);

-- designate  foreign keys:
ALTER TABLE orders
ADD FOREIGN KEY (customer_id) 
REFERENCES customers(customer_id);

ALTER TABLE orders_items
ADD FOREIGN KEY (item_id) 
REFERENCES items(item_id);

ALTER TABLE orders_items 
ADD FOREIGN KEY (order_id) 
REFERENCES orders(order_id);

-- Query the original store table with constraing:
SELECT customer_email
FROM store
WHERE order_date > '2019-08-25';

--query the emails of all customers who made an order after July 25, 2019:
SELECT customer_email
FROM customers, orders
WHERE customers.customer_id = orders.customer_id
AND orders.order_date >'2019-07-25';

-- Query the original store table to return the number of orders containing each unique item
WITH all_items AS (
SELECT item_1_id as item_id 
FROM store
UNION ALL
SELECT item_2_id as item_id
FROM store
WHERE item_2_id IS NOT NULL
UNION ALL
SELECT item_1_id as item_id
FROM store
WHERE item_1_id IS NOT NULL
)
SELECT item_id, COUNT(*)
FROM all_items
GROUP BY item_id;

-- Query normalized database tables to return the number of orders containing each unique item:
SELECT item_id, COUNT(*)
FROM orders_items
GROUP BY item_id;