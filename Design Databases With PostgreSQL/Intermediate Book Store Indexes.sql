-- Intermediate Book Store Indexes

-- look at the first 10 rows in each table:
SELECT * FROM customers LIMIT 10;
SELECT * FROM orders LIMIT 10;
SELECT * FROM books  LIMIT 10;

--Examine the indexes that already exist on the  tables:
SELECT * FROM pg_Indexes WHERE tablename = 'customers';
SELECT * FROM pg_Indexes WHERE tablename = 'books';
SELECT * FROM pg_Indexes WHERE tablename = 'orders';

-- how long select statement took without an index:
EXPLAIN ANALYZE SELECT quantity FROM orders WHERE quantity > 18;

--build an index to improve the search :
CREATE INDEX order_quantity_idx ON orders (quantity);

-- check the analysis time again:
EXPLAIN ANALYZE SELECT quantity FROM orders WHERE quantity > 18;

-- add primary key and index on customers table:
ALTER TABLE customers
ADD PRIMARY KEY (customer_id);

CREATE INDEX customers_idx ON customers (customer_id);

-- To check the effectiveness of this index, write a query: 
EXPLAIN ANALYZE SELECT * FROM customers
WHERE customer_id < 100;

-- Use  primary key to order system in the database physically by customer_id:
CLUSTER customers USING customers_idx;
SELECT * FROM customers LIMIT 10;

-- build a multicolumn index:
CREATE INDEX order_multi_idx ON orders (customer_id, book_id);

-- drop the index:
DROP INDEX IF EXISTS order_multi_idx;

-- build a better working index:
CREATE INDEX books_multi_idx ON books (author, title);

-- build a query on orders with constraing:
EXPLAIN ANALYZE SELECT * FROM orders
WHERE quantity * price_base > 100;

-- Create an index to speed this query:
CREATE INDEX orders_shipping_delay_idx ON orders ((ship_date - order_date));


-- check what indexes currently exist: 
SELECT * FROM pg_indexes
WHERE tablename IN ('customers', 'books', 'orders')
ORDER BY tablename, indexname;






