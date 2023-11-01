import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lena Salgados")

with st.container():
    st.subheader("Salgados e Doces - Para Festas ou Consumo Próprio")
    st.title("Lena Salgados")
    st.write("Fotos de Salgados !!! [Clique Aqui](https://buffetilhadotesouro.com.br/encomenda-de-salgados-fritos-em-santos/)")

with st.container():
    st.write("---")
    st.write("MENU - Produtos e Valores")
    df = pd.DataFrame(
    [
        {"Salgados & Doces": "Coxinha", "Valor Unitário": "¥ 250", "Valor Cento": "¥ 6.500"},
        {"Salgados & Doces": "Risólis", "Valor Unitário": "¥ 250", "Valor Cento": "¥ 6.500"},
        {"Salgados & Doces": "Esfiha", "Valor Unitário": "¥ 300", "Valor Cento": "¥ 6.500"},
    ]
)

st.dataframe(df, use_container_width=True)
