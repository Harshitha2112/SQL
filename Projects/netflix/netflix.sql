DROP TABLE IF EXISTS netflix;
CREATE TABLE netflix
(
	show_id	VARCHAR(10),
	type	VARCHAR(10),
	title	VARCHAR(150),
	director	VARCHAR(208),
	casts	VARCHAR(1000),
	country	VARCHAR(150),
	date_added	VARCHAR(50),
	release_year	INT,
	rating	VARCHAR(10),
	duration	VARCHAR(15),
	listed_in	VARCHAR(100),
	description VARCHAR(250)
);

SELECT * FROM netflix
LIMIT 5

SELECT COUNT(*) AS total_content FROM netflix


SELECT DISTINCT type FROM netflix



--- PROBLEMS & SOLUTIONS

--1. Count the number of movies vs TV shows

SELECT type ,COUNT(*) AS total_count
FROM netflix
GROUP BY type


--2. find the most common rating for movies and tv shows
WITH rating_counts AS (
    SELECT
        type,
        rating,
        COUNT(*) AS total
    FROM netflix
    WHERE rating IS NOT NULL
    GROUP BY type, rating
),
ranked_ratings AS (
    SELECT
        type,
        rating,
        total,
        ROW_NUMBER() OVER (
            PARTITION BY type
            ORDER BY total DESC
        ) AS rn
    FROM rating_counts
)
SELECT type, rating, total
FROM ranked_ratings
WHERE rn = 1;


--3. list all movies released in a specific year (e.g., 2020)

SELECT *
FROM netflix
WHERE type='Movie' AND release_year='2020'


--4. Find the top 5 countries with the most content on netflix

SELECT UNNEST(STRING_TO_ARRAY(country,',')) AS New_country,
	   COUNT(show_id) AS total_content
FROM netflix
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5


--5.Identify the longest movie


SELECT title,duration
FROM netflix
WHERE type='Movie'
AND duration = (
		SELECT MAX(duration)
		FROM netflix
)



--6. find content added in the last 6 years
SELECT *
FROM netflix
WHERE TO_DATE(date_added, 'Month DD, YYYY')
      >= CURRENT_DATE - INTERVAL '6 YEARS';



--7. find all the movies/tv shows by director 'Rajiv chilaka'

SELECT *
FROM netflix
WHERE director ILIKE '%Rajiv Chilaka%'


--8. List all the TV shows with more than 5 seasons


SELECT * 
FROM netflix
WHERE SPLIT_PART(duration,' ',1)::numeric > 5 
AND type= 'TV Show'

--SPLIT_PART()
SELECT SPLIT_PART('APPLE BANANA MANGO',' ',1)



--9.












