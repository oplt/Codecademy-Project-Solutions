-- Hacker News is a popular website run by Y Combinator. 
-- It’s widely known by people in the tech industry as a community site for sharing news, showing off projects, asking questions, among other things.
-- In this project, you will be working with a table named hacker_news that contains stories from Hacker News since its launch in 2007.

--  the most popular Hacker News stories:
SELECT title, score FROM hacker_news
ORDER BY score DESC
LIMIT 5;

--  total score of all the stories
select sum(score) from hacker_news;

--  the individual users who have gotten combined scores of more than 200, and their combined score
SELECT user, SUM(score) FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

-- add these users’ scores together and divide by the total to get the percentage
SELECT (517 + 309 + 304 + 282) / 6366.0;

-- How many times has each offending user posted the youtube link
SELECT user, COUNT(*) FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY user
ORDER BY COUNT(*) DESC;

-- Which sites feed Hacker News the most:
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

-- the best time of the day to post a story on Hacker News
SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', timestamp) as hour, round(avg(score)) as average, count(*) as total FROM hacker_news
where timestamp is not null
GROUP BY 1
order by 1;