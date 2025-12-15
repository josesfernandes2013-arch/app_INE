import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu 
st.header("Introduzindo os Elementos de Streamlit")
menu = option_menu(menu_title="Menu",
                  options=["Início", "Graficos Estátiscos", "Graficos Dinâmicos", "Widgets", "Formulário"],
                  icons=["house-fill","bar-chart-fill","bar-chart-line-fill","toggles","ui-checks"],
                  menu_icon="cast",
                  default_index=0,
                  orientation="horizontal"
  )
with st.sidebar:
  st.success("**UPLOAD DE DADOS**")
  dados = st.file_uploader(
    "Clique no botão abaixo para Carregar um ficheiro",
    type=["xlsx","xls"]
  )
  if dados:
    def carregar_dados(dados):
      try:
        df = pd.read_excel(dados)
        return df
      except FileNotFoundError:
        return pd.DataFrame()
    df = carregar_dados(dados)
    st.table(df)
        
  else:
      st.info("Carregue um ficheiro Excel para começar")
        
if menu =="Inicio":
  with st.expander("**Sobre o Instituto Nacional de Estatistica**"):
      st.write("Acesse o site www.ine.cv")
      st.image ("INE.png"
              )
if menu == "Widgets":
  bt = st.button("Dê um clique!")
  if bt:
    st.info("Clicaste num botão acima!")
  sd = st.slider("Mova o ponto do slider!", min_value=25, \
                max_value=35, value=30, step=1)
  texto = 

           
  
