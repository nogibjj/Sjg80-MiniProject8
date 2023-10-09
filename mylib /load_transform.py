"""
Transforms and Loads data into Azure SQL database
"""
import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

# load the csv files from data directory and insert into Azure SQL Database
def load(dataset1='data/commodity-prices.csv'):
    """
    Transforms and Loads data into Azure SQL database
    """
    df1 = pd.read_csv(dataset1)

    load_dotenv()  # Load the environment variables from the .env file in the outer directory
    server = os.getenv("SERVER")
    database = os.getenv("DATABASE")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    driver = os.getenv("DRIVER")
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS commodity-prices")
        cursor.execute("CREATE TABLE commodity-prices (Date,All Commodity Price Index,Non-Fuel Price Index,Food and Beverage Price Index,Food Price Index,Beverage Price Index,Industrial Inputs Price Index)")
        for _, row in df1.iterrows():
            cursor.execute("INSERT INTO laliga VALUES (?,?,?,?,?,?,?)", row.tolist())
        
        cursor.close()

    return "success"
