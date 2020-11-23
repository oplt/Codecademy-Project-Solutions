-- look at the first 10 rows in each table; 
SELECT * FROM customers LIMIT 10;
SELECT * FROM orders LIMIT 10;
SELECT * FROM books LIMIT 10;

--Examine the indexes that already exist on the three tables:
SELECT * FROM pg_Indexes WHERE tablename = 'customers';
SELECT * FROM pg_Indexes WHERE tablename = 'orders';
SELECT * FROM pg_Indexes WHERE tablename = 'books';

--check the runtime of a query searching:
EXPLAIN ANALYZE SELECT original_language, title, sales_in_millions 
from books 
where original_language = 'French';

-- get the size of the books table:
SELECT pg_size_pretty (pg_total_relation_size('books'));

-- Create an index:
CREATE INDEX multindex_idx ON books (original_language, title, sales_in_millions);

--Delete the multicolumn index:
DROP INDEX IF EXISTS multindex_idx;

-- bulk insert orders from a file:
SELECT NOW();
\COPY orders 
FROM 'orders_add.txt' DELIMITER ',' CSV HEADER;
 
SELECT NOW();







