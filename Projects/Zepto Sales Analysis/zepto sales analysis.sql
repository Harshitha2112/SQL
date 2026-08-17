
CREATE TABLE zepto(
sku_id SERIAL PRIMARY KEY,
category VARCHAR(120),
name VARCHAR(150) NOT NULL,
mrp NUMERIC(8,2),
discountPercent NUMERIC(5,2),
availableQuantity INTEGER,
discountedSellingPrice NUMERIC(8,2),
weightInGms Integer,
outOfStock Boolean,
Quantity integer
);


--data exploration--

SELECT COUNT(*) FROM zepto;

--sample data

SELECT * FROM zepto
limit 10;

--null values
SELECT * FROM zepto
WHERE name IS NULL
OR category IS NULL
OR mrp IS NULL
OR discountpercent IS NULL
OR availablequantity IS NULL
OR discountedsellingprice IS NULL
OR weightingms IS NULL
OR outofstock IS NULL
OR quantity IS NULL;

--Different product category

SELECT DISTINCT category FROM zepto
ORDER BY category;

--Product in stock vs out of stock
SELECT outofstock ,COUNT(sku_id)
FROM zepto
GROUP BY outofstock;

--Product names occuring multiple times
SELECT name ,COUNT(sku_id) as "Number of SKU's"
FROM zepto
GROUP BY name
HAVING COUNT(sku_id)>1
ORDER BY COUNT(sku_id) DESC;

--Data cleaning

--products with price=0
SELECT * FROM zepto
WHERE mrp=0 OR discountedsellingprice =0;

DELETE FROM zepto
WHERE mrp=0;

--convert paise to ruppees
UPDATE zepto
set mrp = mrp/100.0,
discountedsellingprice = discountedsellingprice/100.0;

SELECT mrp,discountedsellingprice FROM zepto;

--find the top 10 best-value products based on the discount percentage
SELECT DISTINCT name , mrp,discountpercent
FROM zepto
ORDER BY discountpercent DESC
LIMIT 10;

--what are the products with high MRP but out of stock
SELECT DISTINCT name,mrp
FROM zepto
WHERE outofstock = TRUE AND mrp>300
ORDER BY mrp DESC;

--calculate Estimated Revenue for each category
SELECT category,SUM(discountedsellingprice * availablequantity) AS total_revenue
FROM zepto
GROUP BY category
ORDER BY total_revenue;

--find all products where MRP is greater than 500 and discount is less than 10%
SELECT DISTINCT name,mrp,discountpercent FROM zepto
WHERE mrp>500 AND discountpercent<10
ORDER BY mrp DESC,discountpercent DESC;

--Identify the top 5 categories offering the highest average discount percentage
SELECT category,ROUND(AVG(discountpercent),2) AS avg_discountpercent
FROM zepto
GROUP BY category
ORDER BY avg_discountpercent DESC
LIMIT 5;

--Find the price per gram for products above 100g and sort by best value
SELECT DISTINCT name ,weightingms,discountedsellingprice,ROUND(discountedsellingprice/weightingms,2) AS price_per_gram
FROM zepto
WHERE weightingms >=100
ORDER BY price_per_gram;

--group the products into categories like low,medium,bulk
SELECT DISTINCT name ,weightingms,
CASE
	WHEN weightingms <1000 THEN 'Low'
	WHEN weightingms <5000 THEN 'Medium'
	ELSE 'Bulk'
	END AS category_level
FROM zepto;

--what is the total inventory weight per category
SELECT category, SUM(weightingms * availablequantity) AS total_weight
FROM zepto
GROUP BY category 
ORDER BY total_weight;