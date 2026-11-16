---1.Coffee Consumers Count
---How many people in each city are estimated to consume coffee, given that 25% of the population does

SELECT city_name,
		ROUND((population * 0.25)/1000000,2) AS coffee_consumer_in_Millions
FROM city
ORDER BY 2 DESC

---2.Total Revenue from Coffee Sales
---What is the total revenue generated from coffee sales across all cities in the last quarter of 2023?


SELECT ci.city_name,sum(s.total) AS total_revenue
FROM sales s
JOIN customers c
ON s.customer_id=c.customer_id
join city ci
ON c.city_id=ci.city_id
WHERE 
		EXTRACT(QUARTER FROM sale_date) = 4 
		AND
		EXTRACT(YEAR FROM sale_date) =2023
GROUP BY 1


---3.Sales Count for Each Product
---How many units of each coffee product have been sold?


SELECT p.product_name,COUNT(sale_id) AS UNITS
FROM products p
JOIN sales s
ON s.product_id = p.product_id
WHERE p.product_id <=14
GROUP BY p.product_id
ORDER BY 2 DESC


---4.Average Sales Amount per City
---What is the average sales amount per customer in each city?


SELECT ci.city_name,ROUND(SUM(s.total)::numeric/ COUNT(DISTINCT c.customer_id)::numeric,2) AS avg_sales_per_customer
FROM city ci
JOIN customers c
ON c.city_id = ci.city_id
JOIN sales s
ON s.customer_id=c.customer_id
GROUP BY ci.city_name
ORDER BY 2 DESC


---5.City Population and Coffee Consumers
---Provide a list of cities along with their populations and estimated coffee consumers.
---Display city_name,total current customers in each cities and estimated coffee consumers(25%)


WITH city_table AS
(
    SELECT
        city_id,
        city_name,
        population,
        ROUND((population * 0.25) / 1000000, 2) AS coffee_consumer_in_Millions
    FROM city
),
customers_table AS
(
    SELECT
        ci.city_id,
        ci.city_name,
        COUNT(DISTINCT c.customer_id) AS unique_customer
    FROM city ci
    JOIN customers c
        ON c.city_id = ci.city_id
    GROUP BY ci.city_id, ci.city_name
)

SELECT
    ci.city_name,
    ci.population,
    ci.coffee_consumer_in_Millions,
    ct.unique_customer
FROM city_table ci
JOIN customers_table ct
    ON ci.city_id = ct.city_id;


---6.Top Selling Products by City
---What are the top 3 selling products in each city based on sales volume?


	---USING COMMON EXPRESSION TABLE---
WITH CTE AS(
			SELECT ci.city_name AS city_name,
	   			   p.product_name AS product_name,
	  		       COUNT(s.sale_id) AS sales_units,
	   			   DENSE_RANK() OVER(
									 PARTITION BY ci.city_name
									 ORDER BY COUNT(s.sale_id) DESC
	   ) AS R	   
		FROM city ci
		JOIN customers c
		ON ci.city_id = c.city_id
		JOIN sales s
		ON s.customer_id = c.customer_id
		JOIN products p
		ON p.product_id = s.product_id
		GROUP BY 1,2
		
)
 SELECT *
 FROM CTE
 WHERE R<=3

			
			--(OR)--
	--- USING SUB QUERIES---
	
SELECT * 
FROM -- table
(
	SELECT 
		ci.city_name,
		p.product_name,
		COUNT(s.sale_id) as total_orders,
		DENSE_RANK() OVER(PARTITION BY ci.city_name ORDER BY COUNT(s.sale_id) DESC) as rank
	FROM sales as s
	JOIN products as p
	ON s.product_id = p.product_id
	JOIN customers as c
	ON c.customer_id = s.customer_id
	JOIN city as ci
	ON ci.city_id = c.city_id
	GROUP BY 1, 2
) 
WHERE rank <= 3


---7.Customer Segmentation by City
---How many unique customers are there in each city who have purchased coffee products?

SELECT ci.city_name,
	   COUNT(DISTINCT c.customer_id) unique_customer
FROM city ci
LEFT JOIN customers c
ON ci.city_id=c.city_id
JOIN sales s
ON s.customer_id = c.customer_id
WHERE s.product_id<=14
GROUP BY 1
ORDER BY 2 DESC


---8.Average Sale vs Rent
---Find each city and their average sale per customer and avg rent per customer


SELECT ci.city_name,
	   ROUND(
	   		SUM(s.total)::numeric/
			   					COUNT(DISTINCT c.customer_id)::numeric,2) AS avg_sale_per_customer,
	   ROUND(
			ci.estimated_rent::numeric/
										COUNT(DISTINCT c.customer_id)::numeric,2) AS avg_rent_per_customer
FROM city ci
JOIN customers c
ON ci.city_id=c.city_id
JOIN sales s
ON s.customer_id=c.customer_id
GROUP BY 1,ci.estimated_rent


---9.Monthly Sales Growth
---Sales growth rate: Calculate the percentage growth (or decline) in sales over different time periods (monthly) by each city.

WITH monthly_sales AS(
					SELECT ci.city_name,
						   EXTRACT (MONTH FROM s.sale_date) as month,
						   EXTRACT( YEAR FROM s.sale_date) AS year,
						   SUM(s.total) AS total_sales
					FROM city ci
					JOIN customers c
					ON ci.city_id=c.city_id
					JOIN sales s
					ON s.customer_id=c.customer_id
					GROUP BY 1,2,3
					ORDER BY 1,3,2

), growth_ratio AS(
					SELECT city_name,
					month,
					year,
					total_sales  as current_month_sale,
					LAG(total_sales,1) OVER(
											PARTITION BY city_name
											ORDER BY year,month
										) AS last_month_sale
					FROM monthly_sales
)


SELECT *,
	   ROUND((current_month_sale-last_month_sale)::numeric/last_month_sale::numeric *100,2) AS growth_ratio
FROM growth_ratio
WHERE last_month_sale IS NOT NULL
	   


---10.Market Potential Analysis
---Identify top 3 city based on highest sales, return city name, total sale, total rent, total customers, estimated coffee consumer


WITH city_table
AS
(
	SELECT 
		ci.city_name,
		SUM(s.total) as total_revenue,
		COUNT(DISTINCT s.customer_id) as total_cx,
		ROUND(
				SUM(s.total)::numeric/
					COUNT(DISTINCT s.customer_id)::numeric
				,2) as avg_sale_pr_cx
		
	FROM sales as s
	JOIN customers as c
	ON s.customer_id = c.customer_id
	JOIN city as ci
	ON ci.city_id = c.city_id
	GROUP BY 1
	ORDER BY 2 DESC
),
city_rent
AS
(
	SELECT 
		city_name, 
		estimated_rent,
		ROUND((population * 0.25)/1000000, 3) as estimated_coffee_consumer_in_millions
	FROM city
)
SELECT 
	cr.city_name,
	total_revenue,
	cr.estimated_rent as total_rent,
	ct.total_cx,
	estimated_coffee_consumer_in_millions,
	ct.avg_sale_pr_cx,
	ROUND(
		cr.estimated_rent::numeric/
									ct.total_cx::numeric
		, 2) as avg_rent_per_cx
FROM city_rent as cr
JOIN city_table as ct
ON cr.city_name = ct.city_name
ORDER BY 2 DESC



/*
-- Recomendation
City 1: Pune
	1.Average rent per customer is very low.
	2.Highest total revenue.
	3.Average sales per customer is also high.

City 2: Delhi
	1.Highest estimated coffee consumers at 7.7 million.
	2.Highest total number of customers, which is 68.
	3.Average rent per customer is 330 (still under 500).

City 3: Jaipur
	1.Highest number of customers, which is 69.
	2.Average rent per customer is very low at 156.
	3.Average sales per customer is better at 11.6k.

