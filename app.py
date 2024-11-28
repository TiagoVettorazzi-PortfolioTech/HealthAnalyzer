import streamlit as st
import Login
import Welcome
import Info
import chat_paciente
import chat_atendimento

# Inicializar o estado de sessão
if 'page' not in st.session_state:
 st.session_state.page = 'Login'  # Defina a página inicial

# Função para mudar a página
def navigate(page_name):
 st.session_state.page = page_name

# Roteador de páginas
if st.session_state.page == 'Login':
    Login.show(navigate)
elif st.session_state.page == 'Welcome':
    Welcome.show(navigate)
elif st.session_state.page == 'Info':
    Info.show(navigate)
elif st.session_state.page == 'chat_paciente':
    chat_paciente.show(navigate)
elif st.session_state.page == 'chat_atendimento':
    chat_atendimento.show(navigate)
