import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
        
if menu == "Início":
    with st.expander("**Sobre o Instituto Nacional de Estatística**"):
        st.write("Acesse o site www.ine.cv")
        st.image("INE.png")

if menu == "Widgets":
  bt = st.button("Dê um clique!")
  if bt:
    st.info("Clicaste num botão acima!")
  sd = st.slider("Mova o ponto do slider!", min_value=25, \
                max_value=35, value=30, step=1)
  texto = f"Eu tenho {sd} anos!"
  st.success(texto)
  
if menu == "Graficos Estátiscos":
  col1, col2, col3 = st.columns([0.3, 0.1, 0.6])
  with col1:
    st.subheader("Coluna 1")
    dados_hist = [3,9,5,12,6,7,5,10,6,10]
    fig, ax =plt.subplots()
    ax.hist (dados_hist, bins=5, color="skyblue", edgecolor="black")
    ax.set_title("Histograma")
    st.pyplot(fig)
  with col2:
    st.subheader("Coluna 2")
    lab = ["Python", "Java", "C++", "JavaScript"]
    pop = [45,25,15,15]
    fig, ax = plt.subplots()
    ax.pie(pop, labels=lab, autopct="%1.1f%%",startangle=90)
    ax.set_title("Grafico Circular"
    ax.axis("equal")
    st.pyplot(fig)
  

           
  
