import pandas as pd


def read_data():
    df = pd.read_csv("app/data/input/Sales_Data.csv")

    total_sales = df["FinalSalePrice"].sum()

    total_orders = df["SalesQuantity"].sum()

    store = df.groupby(["StoreLocation"])["FinalSalePrice"].sum().idxmax()

    def month():
        df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

        # Criar coluna com o ano e mês
        df["YearMonth"] = df["TransactionDate"].dt.to_period("M").astype(str)

        # Agrupar por YearMonth e somar as vendas
        df_sale_month = df.groupby("YearMonth")["FinalSalePrice"].sum().reset_index()

        # Ordenar pela data
        df_sale_month["YearMonth"] = pd.to_datetime(df_sale_month["YearMonth"])
        df_sale_month = df_sale_month.sort_values("YearMonth")

        # Opcional: formatar para exibir como "Jan 2023"
        df_sale_month["YearMonth"] = df_sale_month["YearMonth"].dt.strftime("%b %Y")

        return df_sale_month

    month()

    region_values = df.groupby(["Region"])["FinalSalePrice"].sum().reset_index()

    df_top10_por_ano = (
        df.groupby("ProductName")["SalesQuantity"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    ).head(10)

    top_10_categories = (
        df.groupby("ProductCategory")["SalesQuantity"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return (
        df,
        total_sales,
        total_orders,
        store,
        month(),
        region_values,
        df_top10_por_ano,
        top_10_categories,
    )
