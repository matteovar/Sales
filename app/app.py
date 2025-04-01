import pandas as pd
import plotly.express as px
import streamlit as st
from src.main import read_data
from src.utils.cards import create_cards

st.set_page_config(page_title="Sales", layout="wide")

(
    df,
    df_products,
    df_products_sales,
    df_total_discount,
    df_prod_disc_name,
    vendas1,
    porcentagem,
    most_common_gender,
    most_gender,
    df_sale_date,
    seila,
    nao_sei,
    df_age,
    loyalty_counts,
    df_fees,
) = read_data()

cols_card = st.columns(4)

with cols_card[0]:
    create_cards(
        "Produto Mais Vendido",
        df_products,
        f"Quantidade de Vendas: {df_products_sales}",
    )
with cols_card[1]:
    create_cards(
        "Valor Total de Desconto",
        f"R$ {df_total_discount:.2f}",
        f"Produto com Maior Desconto: {df_prod_disc_name} ",
    )
with cols_card[2]:
    create_cards(
        "Consumidores com Transações Completas",
        vendas1,
        f"Porcentagem sobre o Tota: {porcentagem}%",
    )
with cols_card[3]:
    create_cards(
        "Gênero Predominante entre Consumidores",
        most_common_gender,
        f"Maior Gasto Feito por {most_common_gender}: R$ {most_gender:.2f}",
    )


def sale_date():
    st.markdown(
        """
        ### Valor Total Vendido de Produtos no Dia
        """
    )
    st.line_chart(df_sale_date)


sale_date()

cols = st.columns(2)

with cols[0]:
    st.markdown(
        """
        ### Valor Total Vendido de Produtos por Região
                """
    )
    st.bar_chart(seila)
with cols[1]:
    st.markdown(
        """
        ###  Valor Vendido de Produtos por Categoria
                """
    )
    seleciona_cat = st.selectbox(
        "Selecione uma categoria",
        options=nao_sei["ProductCategory"].unique(),
        placeholder="Selecione",
    )

    filter_cat = nao_sei[nao_sei["ProductCategory"] == seleciona_cat]
    df_filtered = filter_cat.drop(columns=["ProductCategory"])

    st.bar_chart(df_filtered, x="ProductName", y="FinalSalePrice")

cols_customer = st.columns(2)

with cols_customer[0]:
    st.markdown(
        """
        ### Quantidade de Pessoas por Faixa Etária
                """
    )
    fig = px.histogram(
        df_age,
        y="CustomerID",
        x="CustomerAge",
        log_y=True,
        color_discrete_sequence=["indianred"],
        text_auto=True,
    )

    st.plotly_chart(fig)

with cols_customer[1]:
    st.markdown(
        """
        ###  Programa de Membros com Fidelidade x Nao Fidelidade
                """
    )
    fig2 = px.pie(loyalty_counts, names="LoyaltyStatus", values="Count")
    st.plotly_chart(fig2)


def fees_region():
    st.markdown(
        """
        ###    Top 10 Maiores Taxas de Frete por Localização

                """
    )
    select_region = st.selectbox(
        "Selecione uma regiao",
        options=df["Region"].unique(),
        index=0,
    )

    df_shipping_top10 = df_fees[df_fees["Region"] == select_region].nlargest(
        10, "ShippingFee"
    )

    fig3 = px.bar(
        df_shipping_top10,
        x="CustomerLocation",
        y="ShippingFee",
        color="CustomerLocation",
        labels={
            "ShippingFee": "Frete Médio (R$)",
            "CustomerLocation": "Local do Cliente",
        },
        text_auto=".2f",
    )
    st.plotly_chart(fig3, use_container_width=True)


fees_region()
