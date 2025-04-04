import pandas as pd
import plotly.express as px
import streamlit as st
from src.main import read_data
from src.utils.cards import create_cards

st.set_page_config(page_title="Sales", layout="wide")

(
    df,
    total_sales,
    total_orders,
    store,
    df_sale_date,
    region_values,
    df_top10_por_ano,
    top_10_categories,
) = read_data()

cols_card = st.columns(4)

with cols_card[0]:
    create_cards("Produto Mais Vendido", f"R$ {total_sales:,.2f}")
with cols_card[1]:
    create_cards("Valor Total De Vendas", f"{total_orders:,}")
with cols_card[2]:
    create_cards("Media dos pedidos", f"R$ {(total_sales/total_orders):,.2f}")
with cols_card[3]:
    create_cards(
        "Loja com mais produtor vendido",
        f"{store}",
    )

col_first = st.columns(2)


def sale_date():
    st.markdown(
        """
        ### Vendas por Mes
        """
    )
    fig_month = px.bar(
        df_sale_date, x="YearMonth", y="FinalSalePrice", color="FinalSalePrice"
    )
    st.plotly_chart(fig_month)


with col_first[0]:
    sale_date()

with col_first[1]:
    st.markdown(
        """
        ### Valor Total Vendido de Produtos por Região
                """
    )
    fig_regions = px.pie(
        region_values, names="Region", values="FinalSalePrice", color="Region"
    )
    fig_regions.update_traces(hole=0.4)
    st.plotly_chart(
        fig_regions,
    )


cols = st.columns(2)

with cols[0]:

    st.markdown(
        """
        ###  Produtos mais Comprados
                """
    )

    fig_prod = px.bar(
        df_top10_por_ano,
        x="ProductName",
        y="SalesQuantity",
        color="SalesQuantity",
    )

    st.plotly_chart(fig_prod)

with cols[1]:
    st.markdown(
        """
        ###  Categorias mais Compradas
        """
    )
    fig_cat = px.bar(
        top_10_categories,
        x="ProductCategory",
        y="SalesQuantity",
        color="SalesQuantity",
    )

    st.plotly_chart(fig_cat)
