import streamlit as st
st.header("Introduzindo os Elementos de Streamlit")
menu = option_menu(menu_title="Menu",
                  options=["Início", "Graficos Estátiscos", "Graficos Dinâmicos", "Widgets", "Formulário"],
                  icons=["house","bar-chart","bar-chart-line","toggles","bar-chart"],
                  menu_icon="cast",
                  default_index=0,
                  orientation="horizontal"
  )
