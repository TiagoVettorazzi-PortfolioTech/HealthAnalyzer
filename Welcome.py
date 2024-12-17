import streamlit as st
import base64
from pathlib import Path
import json

def show(navigate):
    def load_user_data(matricula):
        """
        Carrega os dados do usuário com base na matrícula.
        """
        try:
            with open("user_data.json", "r") as file:  
                dados = json.load(file)
                return dados.get(matricula, {})  # Retorna os dados do usuário ou um dicionário vazio
        except FileNotFoundError:
            st.error("Arquivo de dados não encontrado.")
        except json.JSONDecodeError:
            st.error("Erro ao ler os dados.")
        return {}

    # Função para adicionar uma imagem de fundo a partir de um arquivo local
    def add_bg_from_local(image_file):
        """
        Adiciona uma imagem de fundo ao aplicativo Streamlit a partir de um arquivo local.
        Args:
        image_file (str): Caminho para o arquivo de imagem local.
        """
        with Path(image_file).open("rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{encoded_string});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # Chamando a função para adicionar o fundo
    add_bg_from_local("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Fundo_Health_Analyzer.png")

    # Estilos personalizados com CSS para cores e design do layout
    st.markdown("""
        <style>
        h1 {
            font-size: 36px;
            color: #0D47A1; /* Azul escuro para o título */
            margin-top: -70px; /* Ajustei a margem para puxar mais para cima */
        }
 
        /* Estiliza botões do Streamlit */
        div.stButton > button {
            background-color: #007199; /* Fundo azul */
            color: white !important; /* Texto branco */
            border: none; /* Remover borda */
            border-radius: 15px; /* Bordas arredondadas */
            padding: 10px 20px; /* Espaçamento interno */
            font-size: 16px; /* Tamanho do texto */
            font-weight: bold; /* Texto em negrito */
            cursor: pointer; /* Alterar cursor para ponteiro */
            width: 200px;
            margin-top: 100px
        }
        div.stButton > button:hover {
            background-color: #005f73; /* Fundo mais escuro ao passar o mouse */
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        input[type="text"], textarea, .stTextArea textarea {
            border: 1px solid #03738C;
            border-radius: 8px;
            padding: 8px;
            box-sizing: border-box;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 50px;
        }

        /* Ajustando o botão com mais especificidade */
        div.stButton > button {
            background-color: #007199; /* Fundo azul */
            color: white !important; /* Garantir que o texto seja branco */
            border: none; /* Remover borda */
            border-radius: 15px; /* Bordas arredondadas */
            padding: 10px 20px; /* Espaçamento interno */
            font-size: 16px; /* Tamanho do texto */
            font-weight: bold; /* Texto em negrito */
            cursor: pointer; /* Alterar cursor para ponteiro */
            width: 200px;
            display: block; /* Garantir que o botão seja tratado como bloco */
            margin: 0 auto; /* Centraliza horizontalmente */
        }
        div.stButton > button:hover {
            background-color: #005f73; /* Fundo mais escuro ao passar o mouse */
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho
    st.markdown("<h1>Health Analyzer</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
        # Título de boas-vindas e campos de login
        st.markdown("<h2>Bem-vindo ao seu <span style='color:#0D47A1;'>Health Analyzer</span></h2>", unsafe_allow_html=True)
        # matricula = st.text_input("Matrícula", value="", max_chars=11, key="login_matricula")
        # senha = st.text_input("Senha", value="", type="password", key="login_senha")
    
    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
        matricula = st.text_input("Matrícula", value="", max_chars=11, key="login_matricula")

        if st.button("Entrar"):
            user_data = load_user_data(matricula)  # Carrega os dados com base na matrícula
            if user_data:
                # Armazenando os dados no session_state
                for key, value in user_data.items():
                    st.session_state[key] = value
                navigate("Info")  
            else:
                st.error("Matrícula não encontrada ou dados inválidos.")
    with col3:
        # Imagem à direita
        st.image('C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Figura_tela_inicial.png')


