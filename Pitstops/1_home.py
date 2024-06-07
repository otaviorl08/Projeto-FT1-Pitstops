import streamlit as st
import pandas as pd
import emoji
import webbrowser

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/df_pitstops.csv", index_col=0)
    st.session_state["data"] = df_data
    
st.write("# STOCK CAR PRO SERIES 2024🏁\n # TEMPOS PIT STOPS :racing_car:⛽")
st.sidebar.markdown("Desenvolvido por Otavio Rocha")

st.sidebar.markdown("Projeto de conclusão do curso: Bootcamp: Software para análise de dados da F1 - ESSS ")

st.sidebar.markdown("Professor: Fabio Mori")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/otaviolino/stock-car-pro-series-brazil-pit-stops-2024")
    
    
st.write("1ª Etapa: \n Realização de processo de ETL com dados da AudaceTech, disponibilizados no site: <a href='https://www.chronon.com.br/resultados/stock-car/stock-pro-series-2024/'>Resultados</a> e criação de um dataframe consolidado com os dados de interesse. \n O dataframe foi salvo no Kaggle para melhor compartilhamento com a comunidade.", unsafe_allow_html=True )

st.write("2ª Etapa: \n Criação de aplicativo com Streamlit para visualização de tempos e quantidade de Pit-Stops realizado por cada equipe em cada etapa da Stock Car em 2024. ")