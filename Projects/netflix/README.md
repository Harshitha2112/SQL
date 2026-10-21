# 🎬 Netflix Data Analysis using SQL

## 📌 Project Overview

This project focuses on analyzing Netflix movies and TV shows using **PostgreSQL**. The goal is to explore Netflix's content catalog, identify trends, and answer business questions using SQL queries.

The project involves data cleaning preparation, data exploration, aggregation, string manipulation, date functions, subqueries, Common Table Expressions (CTEs), and window functions to extract meaningful insights from the dataset.

## 🎯 Objectives

- Analyze the distribution of Movies and TV Shows on Netflix.
- Identify the most common content ratings.
- Explore content released in specific years.
- Find countries contributing the most content.
- Identify the longest movies and TV shows with multiple seasons.
- Analyze content added to Netflix over time.
- Explore directors, actors, genres, and Indian content.
- Categorize content based on keywords in descriptions.

## 🛠️ Tools & Technologies

- **Database:** PostgreSQL
- **Query Language:** SQL
- **Database Client:** pgAdmin 4
- **Dataset:** Netflix Movies and TV Shows
- **Version Control:** Git and GitHub




| File | Description |
|---|---|
| `netflix.sql` | SQL table creation, data exploration, and analysis queries |
| `netflix_titles.csv` | Dataset containing Netflix movie and TV show information |
| `README.md` | Project documentation |

## 🗃️ Dataset Description

The dataset contains information about Netflix titles, including movies and TV shows.

| Column | Description |
|---|---|
| `show_id` | Unique identifier for each title |
| `type` | Movie or TV Show |
| `title` | Name of the title |
| `director` | Director name(s) |
| `casts` | Cast members |
| `country` | Country of production |
| `date_added` | Date the title was added to Netflix |
| `release_year` | Original release year |
| `rating` | Content classification |
| `duration` | Movie runtime or number of TV show seasons |
| `listed_in` | Genres or categories |
| `description` | Short description of the title |

## 🔍 SQL Analysis & Business Questions

The project answers the following 15 questions:

1. **Movies vs. TV Shows:** Count the number of movies and TV shows available on Netflix.
2. **Most Common Ratings:** Identify the most common content rating for Movies and TV Shows separately.
3. **Content Released in a Specific Year:** List all movies released in 2020.
4. **Top 5 Countries:** Find the five countries with the highest number of titles.
5. **Longest Movie:** Identify the movie with the longest duration.
6. **Recently Added Content:** Find titles added to Netflix within the last six years.
7. **Director Analysis:** Find movies and TV shows directed by Rajiv Chilaka.
8. **TV Shows with More Than Five Seasons:** Identify TV shows with more than five seasons.
9. **Genre Analysis:** Count the number of titles in each genre.
10. **Indian Content Trends:** Analyze yearly Netflix additions associated with India and identify the top five years by the calculated content percentage.
11. **Documentary Movies and Shows:** Find titles categorized as documentaries.
12. **Missing Director Information:** Identify titles without director information.
13. **Salman Khan Movies:** Find movies featuring Salman Khan released within the last ten years.
14. **Top Indian Actors:** Find the ten actors appearing most frequently in titles associated with India.
15. **Description-Based Categorization:** Categorize content as `Bad` or `Good` based on the presence of the keywords "kill" and "violence" in descriptions.

## 🧠 SQL Concepts Practiced

- **DDL:** `CREATE TABLE`, `DROP TABLE`
- **Data Exploration:** `SELECT`, `DISTINCT`, `COUNT()`
- **Filtering:** `WHERE`, `ILIKE`, `IS NULL`
- **Aggregation:** `GROUP BY`, `ORDER BY`, `HAVING`
- **String Functions:** `STRING_TO_ARRAY()`, `UNNEST()`, `SPLIT_PART()`
- **Date Functions:** `TO_DATE()`, `EXTRACT()`, `CURRENT_DATE`, `INTERVAL`
- **Conditional Logic:** `CASE WHEN`
- **Common Table Expressions:** `WITH` and CTEs
- **Window Functions:** `ROW_NUMBER()`
- **Subqueries:** Scalar and nested queries
- **Type Casting:** `::numeric`

## ⚙️ How to Run the Project

### Prerequisites

- PostgreSQL installed on your system.
- pgAdmin 4 or another PostgreSQL client.
- The Netflix CSV dataset.

### Steps

1. Clone or download this repository.
2. Open pgAdmin 4 and connect to your PostgreSQL server.
3. Create a database named `netflix`.
4. Open the Query Tool and execute the table creation statements from `netflix.sql`.
5. Import `netflix_titles.csv` into the `public.netflix` table, ensuring that the CSV **Header** option is enabled.
6. Execute the data exploration and analysis queries in `netflix.sql`.
7. Review the result tables to understand the findings.

**Note:** Run the table creation statements before importing the dataset. Since `DROP TABLE IF EXISTS` removes an existing table and its data, avoid rerunning that statement after importing unless you intend to recreate the table.

## 📊 Key Learnings

- Writing SQL queries to answer real-world business questions.
- Analyzing structured data using filtering and aggregation.
- Working with dates, strings, and comma-separated values.
- Using subqueries, CTEs, and window functions.
- Handling missing values and interpreting query results.
- Organizing SQL analysis in a version-controlled project.

## 🚀 Future Improvements

- Create visual dashboards using Power BI.
- Compare movie and TV show trends over time.
- Perform deeper analysis of country, genre, and rating distributions.
- Improve data quality by standardizing missing values and data types.
- Document important findings with charts and summary statistics.

## 👩‍💻 Author

**Harshitha U**

GitHub: [Harshitha2112](https://github.com/Harshitha2112)

---
