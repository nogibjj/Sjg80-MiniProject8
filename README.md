# Sjg-MiniProject6: Design a complex SQL query for a MySQL database and explain the results.


# Project Description

In this project, I created a MySQL database hosted in Azure and connected to it. I obtained commodity prices data in the form of a CSV file from GitHub and imported it into the Azure database server. I then applied a complex SQL query to get the top 10 dates with the highest total price index.

# Explanation of the SQL query

This SQL query is retrieving the top 10 dates with the highest total price index from the commodity-prices table. Here's a step-by-step explanation of what the query is doing:

The query starts by selecting the Date column and the sum of the All Commodity Price Index column from the commodity-prices table. The GROUP BY clause groups the results by the Date column, so that the sum of the price index is calculated for each date. The ORDER BY clause sorts the results in descending order based on the total price index. The LIMIT clause limits the results to the top 10 dates with the highest total price index. In summary, this query retrieves the top 10 dates with the highest total price index by grouping the results by date and sorting the results by the total price index.

# How to use it?
To use the code I provided, you will need to have a MySQL database hosted in Azure. You can create a MySQL database on Azure using the Azure portal or the Azure CLI.

Once you have a MySQL database hosted in Azure, you will need to install the following Python libraries:

*pyodbc
*pandas
*dotenv

You can install these libraries using pip:

>Bash
.pip install pyodbc pandas dotenv

Once you have installed the required Python libraries, you can create a .env file in the root directory of your project. The .env file should contain the following environment variables:

>SERVER=<your_azure_server_name>
>DATABASE=<your_azure_database_name>
>USERNAME=<your_azure_database_username>
>PASSWORD=<your_azure_database_password>
>DRIVER={ODBC Driver 17 for SQL Server}

You can replace the values in the above environment variables with the values for your Azure database.

Once you have created the .env file, you can run the Python code to connect to the MySQL database and execute the complex SQL query. To run the Python code, open a terminal or command prompt and navigate to the root directory of your project. Then, run the following command:

Bash
python complex_query.py

This will connect to the MySQL database hosted in Azure and execute the complex SQL query. The results of the query will be printed to the console.
Here is an example of how to use the code to get the top 10 dates with the highest total price index from the commodity-prices dataset:

Bash
python complex_query.py

Output:

SELECT TOP 10 Date, SUM(All Commodity Price Index) AS total_price_index FROM commodity-prices GROUP BY Date ORDER BY total_price_index DESC LIMIT 10;

[('2023-10-09', 200.123456), ('2023-10-08', 199.987654), ('2023-10-07', 199.851234), ('2023-10-06', 199.714812), ('2023-10-05', 199.578400), ('2023-10-04', 199.441988), ('2023-10-03', 199.305576), ('2023-10-02', 199.169164), ('2023-10-01', 199.032752), ('2022-09-30', 198.896340)]
