import streamlit as st
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
    "",
    type=["xlsx","xls"]
  )
  
