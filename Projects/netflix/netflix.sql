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



--9.Count the number of content items in each genre

SELECT  UNNEST(STRING_TO_ARRAY(listed_in,',')) as Genre,COUNT(show_id) AS total_content
FROM netflix
GROUP BY Genre



--10. find each year and the average numbers of content release by india on netflix.return top 5 year with highest avg content release

SELECT EXTRACT(YEAR FROM TO_DATE(date_added ,'MONTH DD,YYYY')) AS year,
COUNT(*) AS YEARLY_CONTENT ,
ROUND(COUNT(*)::numeric/(SELECT COUNT(*) FROM netflix WHERE country='India')*100::numeric,2) AS AVG_CONTENT
FROM netflix
WHERE country='India'
GROUP BY year
ORDER BY 3 DESC
LIMIT 5



--11. List all the movies that are documentaries


SELECT * 
FROM netflix
WHERE listed_in ILIKE '%documentaries%'



--12. find all content without a director


SELECT * 
FROM netflix
WHERE director IS NULL


--13. find how many movies actor 'Salman khan' appeared in last 10 years

SELECT *
FROM netflix
WHERE casts ILIKE '%Salman Khan%'
AND release_year > EXTRACT(YEAR FROM CURRENT_DATE)-10



--14. find the top 10 actors who have appeared in the highest number of movies produced in india

SELECT UNNEST(STRING_TO_ARRAY(casts,',')) as actors,COUNT(*)
FROM netflix
WHERE country ILIKE '%India%'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10


--15. categorize the content based on the presence of the keyords 'kill' and 'violence' in the description field.
------label content containing these keywords as 'bad' and all other content as 'good'. 
------count how many items fall into each category.

WITH CTE AS (
SELECT *,
		CASE
		WHEN 
			description ILIKE '%KILL%' OR
			description ILIKE '%violence%' THEN 'bad'
			ELSE 'Good'
		END category
FROM netflix
	)

SELECT category,COUNT(*) AS TOTAL_CONTENT
FROM CTE
GROUP BY 1







