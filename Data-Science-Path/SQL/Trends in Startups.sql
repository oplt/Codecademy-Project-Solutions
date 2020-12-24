-- Howdy! It’s your first day as a TechCrunch reporter. 
-- # Your first task is to write an article on the rising trends in the startup world.
-- # To get you started with your research, your boss emailed you a project.sqlite file that contains a table called startups. 
-- # It is a portfolio of some of the biggest names in the industry.
-- # Write queries with aggregate functions to retrieve some interesting insights about these companies.

-- # take a look at the startups table
SELECT * FROM startups
limit 2;

-- # Calculate the total number of companies
select count(*) from startups;

-- # total value of all companies 
select sum(valuation) from startups;

-- # highest amount raised by a startup during ‘Seed’ stage
SELECT MAX(raised) FROM startups WHERE stage = 'Seed';

-- # the year that the oldest company was founded
select min(founded) from startups; 

--  the average valuation, in each category:
select round(avg(valuation), 2) as avg, category from startups 
group by category 
order by avg desc;

--  return the name of each category with the total number of companies that belong to it.
--  filter the result to only include categories that have more than three companies in them
select category, count(*) from startups
group by category
having count(*) > 3;

--  average size of a startup in each location, with average sizes above 500
SELECT location, AVG(employees) FROM startups
GROUP BY location
HAVING AVG(employees) > 500;


