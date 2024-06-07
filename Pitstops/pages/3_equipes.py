import streamlit as st
import pandas as pd
import plotly.express as px

df_data = pd.read_csv("datasets/df_pitstops.csv", index_col=0)
st.session_state["data"] = df_data

# Obter as etapas únicas
equipes = df_data['Equipe'].unique()

# Criar um filtro de etapas
equipes_selecionadas = st.multiselect("Selecione a equipe", equipes, default=equipes)

# Filtrar os dados com base nas etapas selecionadas
df_filtrado_equipe = df_data[df_data['Equipe'].isin(equipes_selecionadas)]

# Criar o gráfico de barras
fig_equipe = px.bar(df_filtrado_equipe, x='Equipe', y='PT Tm', color='Equipe', barmode='group',
             title='Tempo de Pit Stop por Equipe e Etapa',
             labels={'Name': 'Piloto', 'PT Tm': 'Tempo de Pit Stop (s)', 'Equipe': 'Equipe'})

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_equipe)