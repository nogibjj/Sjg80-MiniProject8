import requests
import pandas as pd
import io

def extract(url1="https://raw.githubusercontent.com/datasets/commodity-prices/master/data/commodity-prices.csv", 
            file_path1="/workspaces/Sjg-MiniProject6/data/commodity_prices.csv"):
              
    """"Extract a url to a file path"""
    with requests.get(url1) as r:
        df = pd.read_csv(io.StringIO(r.text))
        # rename columns
        df = df.rename(columns={"Beverage Price Index": "Index_Beverages,})
        df.to_csv(file_path1, index=False)

    return file_path1

    
