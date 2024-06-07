import streamlit as st
import pandas as pd
import plotly.express as px

df_data = pd.read_csv("datasets/df_pitstops.csv", index_col=0)
st.session_state["data"] = df_data


# Obter as etapas únicas
etapas = df_data['Etapa'].unique()
equipes = df_data['Equipe'].unique()

# Criar um filtro de etapas
etapas_selecionadas = st.multiselect("Selecione as etapas", etapas, default=etapas)
#equipes_selecionadas = st.multiselect("Selecione as equipes", equipes, default=etapas)

# Filtrar os dados com base nas etapas selecionadas
df_filtrado_etapa = df_data[
    df_data['Etapa'].isin(etapas_selecionadas)
     ]


# Criar o gráfico de barras
fig_etapa = px.bar(df_filtrado_etapa, x='Name', y='PT Tm', color='Etapa', barmode='group',
             title='Tempo de Pit Stop por Piloto e Etapa',
             labels={'Name': 'Piloto', 'PT Tm': 'Tempo de Pit Stop (s)', 'Etapa': 'Etapa'})

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_etapa)

#######################################################################

# Filtrar o DataFrame para incluir apenas os pilotos das equipes 'Full Time Sports' e 'Mobil Ale'
df_fulltime = df_data[
    (df_data['Equipe'].isin(['Full Time Sports', 'Mobil Ale']))&
    df_data['Etapa'].isin(etapas_selecionadas)
    ]


# Criar o gráfico no Plotly
fig_ft = px.bar(df_fulltime, x='Name', y='PT Tm', color='Equipe', text='PT Tm', barmode='group',
             title='Comparação de Tempos de Pit Stop por Piloto',
             labels={'Name': 'Piloto', 'PT Tm': 'Tempo de Pit Stop (s)', 'Team': 'Equipe'})

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_ft)