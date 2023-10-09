# Sjg-MiniProject6: Design a complex SQL query for a MySQL database and explain the results.


# Project Description

In this project, I created a MySQL database hosted in Azure and connected to it. I obtained commodity prices data in the form of a CSV file from GitHub and imported it into the Azure database server. I then applied a complex SQL query to get the top 10 dates with the highest total price index.

# Explanation of the SQL query

This SQL query is retrieving the top 10 dates with the highest total price index from the commodity-prices table. Here's a step-by-step explanation of what the query is doing:

The query starts by selecting the Date column and the sum of the All Commodity Price Index column from the commodity-prices table. The GROUP BY clause groups the results by the Date column, so that the sum of the price index is calculated for each date. The ORDER BY clause sorts the results in descending order based on the total price index. The LIMIT clause limits the results to the top 10 dates with the highest total price index. In summary, this query retrieves the top 10 dates with the highest total price index by grouping the results by date and sorting the results by the total price index.
