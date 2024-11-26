import base64
from pathlib import Path
import streamlit as st

def show(navigate):
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

    # Adiciona a imagem de fundo chamando a função
    add_bg_from_local("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/bg_teste.png")

    # Estilos personalizados com CSS para cores e design do layout
    st.markdown("""
        <style>
        h1 {
            font-size: 36px;
            color: #0D47A1; /* Azul escuro para o título */
        }
        h2 {
            font-size: 28px;
            color: #000000; /* Preto para o texto principal */
        }
        p {
            font-size: 18px;
            color: #606060; /* Cinza para o subtítulo */
        }
        .login-button {
            background-color: #01579B; /* Azul escuro para o botão */
            color: white;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            margin-top: 20px;
        }
        .login-button:hover {
            background-color: #0277BD;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título da página
    st.markdown("<h1>Health Analyzer</h1>", unsafe_allow_html=True)

    # Texto de boas-vindas e subtítulo
    st.markdown("<h2>Bem-vindo ao seu <span style='color:#0D47A1;'>Health Analyzer</span></h2>", unsafe_allow_html=True)
    st.markdown("<p>Otimize seu pronto atendimento iniciando sua triagem do local onde você estiver.</p>", unsafe_allow_html=True)

    # Botão de login que, ao clicar, navega para a página 'welcome'
    if st.button("Fazer login", key="login_button"):
        navigate("Welcome")  # Navega para a página de boas-vindas

    # Exibe a imagem (use o caminho correto da imagem)
    st.image('C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/Figura_tela_inicial.png')
