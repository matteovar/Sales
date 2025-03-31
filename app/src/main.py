import pandas as pd


def read_data():
    df = pd.read_csv("app/data/input/Sales_Data.csv")

    df_prod = (
        df.groupby(["ProductName"])["SalesQuantity"]
        .sum()
        .reset_index()
        .sort_values("SalesQuantity", ascending=False)
    )
    df_products = df_prod.iloc[0]["ProductName"]
    df_products_sales = df_prod.iloc[0]["SalesQuantity"]

    df_total_discount = df["DiscountAmount"].sum()
    df_prod_disc = (
        df.groupby(["ProductName"])["DiscountAmount"]
        .sum()
        .reset_index()
        .sort_values("DiscountAmount", ascending=False)
    )
    df_prod_disc_name = df_prod_disc.iloc[0]["ProductName"]

    vendas = df.loc[df["TransactionStatus"] == "Completed", ["CustomerID"]].count()
    vendas1 = vendas.loc["CustomerID"]

    consumidores_totais = df["CustomerID"].count()

    porcentagem = (vendas1 / consumidores_totais) * 100

    most_common_gender = df["CustomerGender"].value_counts().idxmax()

    most_gender = df.loc[
        df["CustomerGender"] == most_common_gender, ["FinalSalePrice"]
    ].sum()
    most_gender_fi = most_gender.loc["FinalSalePrice"]

    df_sale_date = df.groupby(["TransactionDate"])["FinalSalePrice"].sum()

    seila = df.groupby(["Region"])["FinalSalePrice"].sum()

    nao_sei = (
        df.groupby(["ProductCategory", "ProductName"])["FinalSalePrice"]
        .sum()
        .reset_index()
    )

    df_age = df.groupby(["CustomerAge"])["CustomerID"].count().reset_index()

    loyalty_counts = df["LoyaltyProgramMember"].value_counts().reset_index()
    loyalty_counts.columns = ["LoyaltyStatus", "Count"]

    df_fees = (
        df.groupby(["Region", "CustomerLocation"])["ShippingFee"]
        .mean()
        .reset_index()
        .sort_values("ShippingFee", ascending=False)
    )

    return (
        df,
        df_products,
        df_products_sales,
        df_total_discount,
        df_prod_disc_name,
        vendas1,
        porcentagem,
        most_common_gender,
        most_gender_fi,
        df_sale_date,
        seila,
        nao_sei,
        df_age,
        loyalty_counts,
        df_fees,
    )
