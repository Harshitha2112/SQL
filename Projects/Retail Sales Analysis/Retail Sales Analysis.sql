-----RETAIL SALES ANALYSIS-----

CREATE DATABASE retail_db;

-- CREATING TABLE
CREATE TABLE retail_sales_tb(
			transactions_id	INT PRIMARY KEY,
			sale_date	DATE,
			sale_time	TIME,
			customer_id	INT,
			gender	VARCHAR(15),
			age	INT,
			category VARCHAR(15),	
			quantity	INT,
			price_per_unit	FLOAT,
			cogs	FLOAT,
			total_sale FLOAT
		)

SELECT * FROM retail_sales_tb
LIMIT 10;


-----DATA CLEANING-----
--DISPLAYING ROWS WITH NULL VALUES 
SELECT * FROM retail_sales_tb
WHERE 
	transactions_id IS NULL
	OR
	sale_time IS NULL
	OR
	sale_date IS NULL
	OR
	customer_id IS NULL
	OR
	gender IS NULL
	OR
	age IS NULL
	OR
	category IS NULL
	OR
	quantity IS NULL
	OR
	price_per_unit IS NULL
	OR
	cogs IS NULL
	OR
	total_sale IS NULL;


--DELETING ROWS WITH NULL VALUES
DELETE  FROM retail_sales_tb
WHERE 
	transactions_id IS NULL
	OR
	sale_time IS NULL
	OR
	sale_date IS NULL
	OR
	customer_id IS NULL
	OR
	gender IS NULL
	OR
	age IS NULL
	OR
	category IS NULL
	OR
	quantity IS NULL
	OR
	price_per_unit IS NULL
	OR
	cogs IS NULL
	OR
	total_sale IS NULL;


-----DATA EXPLORATION-----
--HOW MANY SALES WE HAVE?
SELECT COUNT(*) AS total_sale FROM retail_sales_tb

--HOW MANY CUSTOMERS DO WE HAVE?
SELECT COUNT(DISTINCT customer_id) AS total_customer FROM retail_sales_tb


-----DATA ANALYSIS-----
--1. Write a SQL query to retrieve all columns for sales on '2022-11-05'
SELECT * FROM retail_sales_tb
WHERE sale_date= '2022-11-05';


--2. Write a SQL query to retrieve all transactions where the category is 'clothing' and the quantity sold is more than 3 in the month of nov-2022
SELECT * FROM retail_sales_tb
WHERE 
	category = 'Clothing'
	AND
	quantity >=3
	AND
	TO_CHAR(sale_date , 'yyyy-mm')= '2022-11';

--3. Write a SQL query to calculate the total sales for each category
SELECT SUM(total_sale),category FROM retail_sales_tb
GROUP BY category;


--4. Write a SQL query to find the average age of customers who purhased items from the 'Beauty' category
SELECT ROUND(AVG(age),2) AS avg_age FROM retail_sales_tb
WHERE category ='Beauty';


--5. Write a SQL query to find all transactions where the total_sales is greater than 1000
SELECT * FROM retail_sales_tb
WHERE total_sale>1000;


--6. Write a SQL query to find the total number of transactions made by each gender in each category
SELECT category,gender ,COUNT(*) AS total_trans FROM retail_Sales_tb
GROUP BY category,gender
ORDER BY 1;


--7. Write a SQL query to calculate the average sale for each month .find out best selling month in each year
SELECT * FROM 
(	SELECT 
		   EXTRACT(YEAR FROM sale_date) AS year,
		   EXTRACT(MONTH FROM sale_date) AS month,
		   AVG(total_sale) AS avg_sale ,
		   RANK() OVER(
				PARTITION BY EXTRACT(YEAR FROM sale_date)
				ORDER BY AVG(total_sale) DESC
		   ) AS rank 
	FROM retail_sales_tb
	GROUP BY 1,2
) AS table1
WHERE rank = 1;


--8. Write a SQL query to find the top 5 Customers based on the highest total sales
SELECT customer_id,SUM(total_sale) as sale from retail_sales_tb
GROUP BY customer_id
ORDER BY sale DESC
LIMIT 5;


--9. Write a SQL query to find the number of customers who purchased items from each category
SELECT category,COUNT(customer_id) FROM retail_sales_tb
GROUP BY 1


--10. Write a SQL query to find the number of UNIQUE customers who purchased items from each category
SELECT category,COUNT(DISTINCT customer_id) FROM retail_sales_tb
GROUP BY 1


--11. Write a SQL query to create each shift and number of orders (Example morning <=12,Afternoon Between 12 & 17 , Evening>17)
WITH hourly_sales
AS
(SELECT *,
	CASE
		WHEN EXTRACT(HOUR FROM sale_time) <12 THEN 'morning'
		WHEN EXTRACT(HOUR FROM sale_time) BETWEEN 12 AND 17 THEN 'Afternoon'
		ELSE 'Evening'
	END AS shift
	FROM retail_sales_tb
	)
SELECT shift,COUNT(*) AS total_orders FROM hourly_sales
GROUP BY shift

----END OF DATA ANALYSIS----
