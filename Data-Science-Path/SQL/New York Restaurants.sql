-- SQL Queries

-- New York Restaurants

-- Select the columns of "nomnom"
SELECT * FROM nomnom;

-- find the distinct neighborhood
SELECT DISTINCT neighborhood FROM nomnom;

-- find the distinct cuisine types
SELECT DISTINCT cuisine FROM nomnom;

-- What are our options of chinese cuisine
SELECT * FROM nomnom WHERE cuisine = 'Chinese';

-- Return all the restaurants with reviews of 4 and above.
SELECT * FROM nomnom WHERE review >= 4;

--Return all the restaurants that are Italian and $$$
SELECT * FROM nomnom WHERE cuisine = 'Italian' AND price = '$$$';

-- find the restaurants with name containing the word ‘meatball’
SELECT * FROM nomnom WHERE name LIKE '%meatball%';

-- Find all the close by spots in Midtown, Downtown or Chinatown
SELECT * FROM nomnom
WHERE neighborhood = 'Midtown'
   OR neighborhood = 'Downtown'
   OR neighborhood = 'Chinatown';

-- Find all the health grade pending restaurants (empty values)
SELECT * FROM nomnom WHERE health IS NULL;

-- Create a Top 10 Restaurants Ranking based on review
SELECT * FROM nomnom ORDER BY review DESC LIMIT 10;

-- Use a CASE statement to change the rating system to: review > 4.5 is Extraordinary,review > 4 is Excellent, review > 3 is Good, review > 2 is Fair, and Everything else is Poor
SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;