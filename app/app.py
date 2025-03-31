import streamlit as st
import pandas as pd
from src.main import read_data
from src.utils.cards import create_cards

st.set_page_config(page_title="Billaboard Top Songs", layout="wide")

df, df_products,df_products_sales = read_data()

cols_card = st.columns(4)

with cols_card[0]:
    create_cards("Produto mais vendido", df_products,f'Quantidade de vendas: {df_products_sales}')
st.dataframe(df)    