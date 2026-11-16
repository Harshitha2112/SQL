# ☕ Coffee Sales Analysis Using SQL (PostgreSQL)

## 📌 Project Overview

This project focuses on analyzing coffee sales data using **PostgreSQL** to identify sales trends, customer behavior, product performance, and city-wise market potential.

The main objective is to extract meaningful business insights from coffee sales data and help businesses make data-driven decisions regarding product sales, customer segmentation, revenue growth, and market expansion.

The analysis uses SQL queries, joins, aggregate functions, Common Table Expressions (CTEs), subqueries, and window functions to solve real-world business problems.

## 🎯 Project Objectives

- Analyze estimated coffee consumers across different cities.
- Calculate total revenue generated from coffee sales.
- Identify the best-selling coffee products.
- Measure average sales per customer in each city.
- Compare city populations with existing customers.
- Identify the top-selling products in each city.
- Analyze customer distribution across cities.
- Compare average sales and rent per customer.
- Calculate monthly sales growth by city.
- Identify cities with the highest market potential.

## 🛠️ Tools & Technologies

- **Database:** PostgreSQL
- **Query Language:** SQL
- **Database Management Tool:** pgAdmin 4
- **Dataset:** Coffee Sales Database

## 🗂️ Database Tables

| Table Name | Description |
|---|---|
| `city` | Contains city details, population, and estimated rent |
| `customers` | Contains customer information and city references |
| `products` | Contains coffee product details |
| `sales` | Contains sales transactions and revenue information |

## 📊 Business Questions & SQL Analysis

### 1. Coffee Consumers Count

**Business Question:** How many people in each city are estimated to consume coffee, assuming 25% of the population drinks coffee?

**SQL Concepts:** Mathematical calculations, `ROUND()`, `ORDER BY`.

### 2. Total Revenue from Coffee Sales

**Business Question:** What is the total revenue generated from coffee sales across all cities in the last quarter of 2023?

**SQL Concepts:** `JOIN`, `SUM()`, `EXTRACT()`, `GROUP BY`, `WHERE`.

### 3. Sales Count for Each Product

**Business Question:** How many units of each coffee product have been sold?

**SQL Concepts:** `JOIN`, `COUNT()`, `GROUP BY`, `ORDER BY`.

### 4. Average Sales Amount per City

**Business Question:** What is the average sales amount per customer in each city?

**SQL Concepts:** Multiple `JOINs`, `SUM()`, `COUNT(DISTINCT)`, `ROUND()`.

### 5. City Population and Coffee Consumers

**Business Question:** Display each city's name, population, estimated coffee consumers, and total current customers.

**SQL Concepts:** CTEs, `JOIN`, `COUNT(DISTINCT)`, `ROUND()`.

### 6. Top-Selling Products by City

**Business Question:** What are the top three selling coffee products in each city based on sales volume?

**SQL Concepts:**
- Common Table Expressions (CTEs)
- Subqueries
- `DENSE_RANK()`
- Window Functions
- `PARTITION BY`

Both CTE and subquery approaches are implemented to solve this problem.

### 7. Customer Segmentation by City

**Business Question:** How many unique customers in each city have purchased coffee products?

**SQL Concepts:** `LEFT JOIN`, `JOIN`, `COUNT(DISTINCT)`, `WHERE`, `GROUP BY`.

### 8. Average Sales vs Rent

**Business Question:** Find each city's average sales per customer and average rent per customer.

**SQL Concepts:** Aggregate functions, `JOIN`, `ROUND()`, type casting, `GROUP BY`.

### 9. Monthly Sales Growth

**Business Question:** Calculate the monthly percentage growth or decline in sales for each city.

**SQL Concepts:**
- CTEs
- `SUM()`
- `EXTRACT()`
- `LAG()`
- `PARTITION BY`
- Window Functions
- Percentage calculations

### 10. Market Potential Analysis

**Business Question:** Identify the top three cities based on sales performance and evaluate their market potential.

The analysis includes:

- Total revenue
- Total rent
- Total customers
- Estimated coffee consumers
- Average sales per customer
- Average rent per customer

**SQL Concepts:** Multiple CTEs, `JOIN`, aggregate functions, `ROUND()`, type casting, business analysis.

## 💡 Key Business Insights & Recommendations

Based on the analysis, the following cities were identified as promising markets:

### 🥇 1. Pune

- Highest total revenue.
- Very low average rent per customer.
- High average sales per customer.

**Recommendation:** Pune is a strong market for business expansion because of its revenue performance and relatively low rent per customer.

### 🥈 2. Delhi

- Highest estimated coffee consumer population (7.7 million).
- Highest number of customers (68).
- Average rent per customer is approximately 330.

**Recommendation:** Delhi offers significant market potential because of its large estimated coffee-consuming population and existing customer base.

### 🥉 3. Jaipur

- High customer count (69).
- Low average rent per customer (156).
- Average sales per customer of approximately 11.6K.

**Recommendation:** Jaipur is a promising market due to its customer base, affordable rent per customer, and good average sales performance.

## 📚 SQL Skills Demonstrated

- SELECT, WHERE, ORDER BY
- GROUP BY and HAVING
- INNER JOIN and LEFT JOIN
- Aggregate Functions: `SUM()`, `COUNT()`, `AVG()`
- `COUNT(DISTINCT)`
- Mathematical calculations and `ROUND()`
- Date and Time Functions: `EXTRACT()`
- Type Casting
- Common Table Expressions (CTEs)
- Subqueries
- Window Functions
- `DENSE_RANK()`
- `LAG()`
- `PARTITION BY`
- Monthly Sales Growth Analysis
- Business Insights and Data-Driven Recommendations

## 📝 Conclusion

This project demonstrates how SQL can be used to transform raw coffee sales data into meaningful business insights.

Through revenue analysis, product performance evaluation, customer segmentation, monthly growth calculations, and market potential analysis, the project identifies promising cities for potential business expansion.

It also demonstrates practical SQL skills by solving business-oriented analytical problems using PostgreSQL.

---

**Project Type:** SQL Data Analysis  
**Domain:** Coffee Sales and Retail Business Analytics  
**Database:** PostgreSQL
