-- Twitch is the world’s leading live streaming platform for gamers, with 15 million unique daily visitors. Using data to understand its users and products is one of the main responsibilities of the Twitch Science Team.
-- In this project, you will be working with two training tables that contain Twitch users’ stream viewing data and chat room usage data.
-- Stream viewing data: stream table
-- Chat usage data:chat table
-- The Twitch Science Team provided this practice dataset. You can download the .csv files (800,000 rows) from GitHub.

-- Select the first 20 rows from each of the table
select * from chat limit 20;
select * from stream limit 20;

-- unique games in the stream table
select distinct game from stream;

-- unique channels in the stream table
select distinct channel from stream;

-- the most popular games in the stream table
select game, count(game) from stream
group by game
order by count(game) desc;

-- Create a list of countries and their number of LoL viewers using WHERE and GROUP BY
select country, count(country) from stream
where game = 'League of Legends'
group by country
order by count(country) desc;

-- Create a list of players and their number of streamers
select player, count(player) from stream
group by 1 order by 2 desc;

-- Create a new column named genre for each of the games.
-- Group the games into their genres
select game, 
case 
when game = "League of Legends" then "MOBA"
when game = "Dota 2" then "MOBA"
when game = "Heroes of the Strom" then "MOBA"
when game = "Counter-Strike: Global Offensive" then "FPS"
when game = "DayZ" then "Survival"
else "Other"
end as "genre", 
count(game) from stream
group by game
order by count(game) desc;

-- look at the time column from the stream table
SELECT time FROM stream LIMIT 10;

-- return the seconds, SS, of the timestamp column
SELECT time, strftime('%S', time) FROM stream
GROUP BY 1
LIMIT 20;

-- return the hours of the time column and the view count for each hour
-- Lastly, filter the result with only the users in your country 
select strftime("%H", time), count(1) from stream
where country = "US"
group by 1;

-- join the stream table and the chat table on device_id column
select * from stream join chat 
on stream.device_id = chat.device_id;










