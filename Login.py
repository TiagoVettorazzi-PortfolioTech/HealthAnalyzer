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
    add_bg_from_local("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Fundo_Health_Analyzer.png")

    # Estilos personalizados com CSS para cores e design do layout
    st.markdown("""
        <style>
        /* Estilo para o título (h1) */
        h1 {
            font-size: 36px;
            color: #0D47A1; /* Azul escuro para o título */
        }
        # /* Estilo para o subtítulo (h2) */
        p {
            font-size: 18px;
            color: #000000; /* Cor para o subtítulo */
        }

        /* Estiliza botões do Streamlit */
        div.stButton > button {
            background-color: #007199; /* Fundo azul */
            color: white; /* Texto branco */
            border: none; /* Remover borda */
            border-radius: 15px; /* Bordas arredondadas */
            padding: 10px 20px; /* Espaçamento interno */
            font-size: 16px; /* Tamanho do texto */
            font-weight: bold; /* Texto em negrito */
            cursor: pointer; /* Alterar cursor para ponteiro */
            width: 200px;
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
        </style>
    """, unsafe_allow_html=True)

    # Título da página
    st.markdown("<h1>Health Analyzer</h1>", unsafe_allow_html=True)

    # Texto de boas-vindas e subtítulo
    st.markdown("<h2>Bem-vindo ao seu <span style='color:#0D47A1;'>Health Analyzer</span></h2>", unsafe_allow_html=True)
    st.markdown("<p>Otimize seu pronto atendimento iniciando sua triagem do local onde você estiver.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
    # Botão de login que, ao clicar, navega para a página 'welcome'
        if st.button("Fazer login"):
            navigate("Welcome")
    with col3:        
        if st.button("Cadastre-se"):
            navigate("Cadastro")

    # Exibe a imagem (use o caminho correto da imagem)
    st.image('C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Figura_tela_inicial.png')
