import pandas as pd

def read_data():
    df = pd.read_csv('app/data/input/Sales_Data.csv')
    
    df_prod = df.groupby(["ProductID"])["SalesQuantity"].sum().reset_index().sort_values("SalesQuantity", ascending = False)
    df_products = df_prod.iloc[0]["ProductID"]
    df_products_sales = df_prod.iloc[0]["SalesQuantity"]
    return df, df_products,df_products_sales