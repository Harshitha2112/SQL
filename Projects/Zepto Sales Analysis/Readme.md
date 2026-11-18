# 🛒 Zepto Sales Analysis Using SQL

## 📌 Project Overview

This project focuses on analyzing Zepto product and inventory data using SQL to extract meaningful business insights.

The analysis involves exploring product categories, identifying stock availability, examining discounts, calculating estimated revenue, and understanding inventory distribution.

PostgreSQL is used to perform data exploration, data cleaning, and business-oriented analysis through SQL queries.

## 🎯 Project Objectives

- Explore and understand the Zepto product dataset.
- Identify missing values and duplicate product records.
- Clean product pricing data.
- Analyze product availability and inventory.
- Identify products offering the highest discounts.
- Calculate estimated revenue across product categories.
- Analyze product pricing based on weight.
- Generate insights to support business decisions.

## 🛠️ Technologies Used

- **Database:** PostgreSQL
- **Language:** SQL
- **Tools:** pgAdmin 4

## 📊 Dataset Description

The dataset contains product-level information with the following attributes:

| Column | Description |
|---|---|
| sku_id | Unique product SKU identifier |
| category | Product category |
| name | Product name |
| mrp | Maximum Retail Price |
| discountPercent | Discount percentage |
| availableQuantity | Available product quantity |
| discountedSellingPrice | Discounted selling price |
| weightInGms | Product weight in grams |
| outOfStock | Stock availability status |
| Quantity | Product quantity |

## ⚙️ SQL Concepts Used

- CREATE TABLE
- SELECT and DISTINCT
- WHERE and ORDER BY
- GROUP BY and HAVING
- Aggregate Functions (COUNT, SUM, AVG)
- CASE Statements
- UPDATE and DELETE
- ROUND()
- LIMIT
- Data Cleaning
- Revenue and Inventory Analysis

## 🔍 Analysis Performed

### 1. Data Exploration
- Counted the total number of records.
- Retrieved sample product records.
- Identified distinct product categories.
- Checked missing or NULL values.
- Compared in-stock and out-of-stock products.
- Identified product names appearing multiple times.

### 2. Data Cleaning
- Identified products with zero MRP or selling price.
- Removed records with zero MRP.
- Converted product prices from paise to rupees.

### 3. Business Analysis

**Product Discount Analysis**
- Identified the top 10 products offering the highest discounts.
- Found the top 5 categories with the highest average discount percentages.

**Inventory Analysis**
- Compared in-stock and out-of-stock products.
- Identified expensive products that are out of stock.
- Calculated total inventory weight for each category.

**Revenue Analysis**
- Calculated estimated revenue for each product category using discounted selling price and available quantity.

**Product Pricing Analysis**
- Identified products with MRP greater than ₹500 and discounts below 10%.
- Calculated price per gram for products weighing at least 100 grams.
- Ranked products based on price per gram to identify better-value products.

**Product Weight Classification**
- Categorized products based on weight:
  - Low: Below 1000 grams
  - Medium: 1000–4999 grams
  - Bulk: 5000 grams and above

## 💡 Key Business Questions Answered

1. What is the total number of products in the dataset?
2. Which product categories are available?
3. How many products are in stock versus out of stock?
4. Which products have the highest discount percentages?
5. Which expensive products are currently out of stock?
6. What is the estimated revenue for each category?
7. Which categories offer the highest average discounts?
8. Which products have an MRP above ₹500 but a discount below 10%?
9. Which products offer the best price per gram?
10. What is the total inventory weight for each category?

## 📂 Project Structure

```text
Zepto-Sales-Analysis/
│
├── zepto sales analysis.sql
└── README.md
```

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Open PostgreSQL using pgAdmin 4.

3. Create a database for the project.

4. Open the SQL query tool.

5. Execute the SQL script to create the table and perform the analysis.

6. Load the Zepto dataset into the table before executing the analysis queries.

## 📈 Business Impact

This analysis helps understand product pricing strategies, discount patterns, stock availability, and category-wise estimated revenue.

The insights can help businesses:
- Identify products with attractive discounts.
- Understand inventory distribution.
- Monitor high-value out-of-stock products.
- Compare product value based on weight.
- Evaluate estimated revenue across categories.

## 👩‍💻 Author

**Harshitha U**

Aspiring Data Analyst | Aspiring Data Scientist
