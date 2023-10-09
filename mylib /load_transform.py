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
        cursor.execute("DROP TABLE IF EXISTS laliga")
        cursor.execute("CREATE TABLE laliga (Date varchar(255), HomeTeam varchar(255), AwayTeam varchar(255), home_goals int, away_goals int, result varchar(255), home_goals_half_time int, away_goals_half_time int, result_half_time varchar(255), home_shots int, away_shots int, home_shots_on_target int, away_shots_on_target int, home_fouls int, away_fouls int, home_corners int, away_corners int, home_yellow_cards int, away_yellow_cards int, home_red_cards int, away_red_cards int)")
        for _, row in df1.iterrows():
            cursor.execute("INSERT INTO laliga VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.tolist())
        cursor.execute("DROP TABLE IF EXISTS epl")
        cursor.execute("CREATE TABLE epl (Date varchar(255), HomeTeam varchar(255), AwayTeam varchar(255), home_goals int, away_goals int, result varchar(255), home_goals_half_time int, away_goals_half_time int, result_half_time varchar(255), home_shots int, away_shots int, home_shots_on_target int, away_shots_on_target int, home_fouls int, away_fouls int, home_corners int, away_corners int, home_yellow_cards int, away_yellow_cards int, home_red_cards int, away_red_cards int)")
        for _, row in df2.iterrows():
            cursor.execute("INSERT INTO epl VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.tolist())
        
        cursor.close()

    return "success"
