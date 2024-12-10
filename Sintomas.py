import streamlit as st
from pathlib import Path
import base64

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

    # Adicionando a imagem de fundo
    add_bg_from_local("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Fundo_Health_Analyzer.png")

    # Estilos personalizados com CSS global
    st.markdown("""
        <style>
        /* Estiliza a barra lateral inteira */
        section[data-testid="stSidebar"] {
            background-color: #007199; /* Cor de fundo */
            padding: 20px; /* Espaçamento interno */
            border-right: 1px solid #DDD; /* Linha divisória */
        }

        /* Estiliza botões na sidebar */
        section[data-testid="stSidebar"] div.stButton > button {
            background-color: white; /* Fundo branco */
            color: #007199; /* Texto azul */
            border: 1px solid #007199; /* Borda azul */
            border-radius: 20px; /* Bordas arredondadas */
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            width: 100%; /* Largura completa dentro da sidebar */
            margin-top: 25px;
        }
        section[data-testid="stSidebar"] div.stButton > button:hover {
            background-color: #D0E8FF; /* Fundo azul claro ao passar o mouse */
            color: #005f73; /* Texto azul mais escuro */
        }
        h1 {
            font-size: 36px;
            color: #007199;
            margin-top: -50px;
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
            margin-top: 50px
        }
        div.stButton > button:hover {
            background-color: #005f73; /* Fundo mais escuro ao passar o mouse */
        }
        input[type="text"], textarea, .stTextArea textarea {
            border: 1px solid #007199;
            border-radius: 8px;
            padding: 8px;
            box-sizing: border-box;
        }
        </style>
    """, unsafe_allow_html=True)

# Sidebar
    with st.sidebar:
        st.image(
            "C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/MARCA-PORTFOLIO-TECH-MONO.png",
            width=150,
        )
        if st.button("Cadastro"):
            navigate("Info")

        if st.button("Histórico", key="sidebar-historico"):
            navigate("chat_historico")


    # Título da Página
    st.title("Health Analyzer")

    # Inicializar valores de sessão
    session_vars = [
        "nome", "sobrenome", "data_nascimento","peso", "altura", "sexo", "cpf", 
        "temperatura", "rg", "matricula", "sintomas"
        "comorbidade", "alergias", "observacoes"
    ]
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = ""

    # Layout dos campos
    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.image("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Avatar.png", width=100, caption="Paciente")
    with col2:
        st.text_input("Nome", value=st.session_state["nome"], key="nome")
        st.text_input("Sobrenome", value=st.session_state["sobrenome"], key="sobrenome")
    with col3:
        st.text_input("CPF",value=st.session_state["cpf"], key="cpf")
        st.text_input("Matricula", value=st.session_state["matricula"], key="matricula")

   # Releatar Sintomas
    st.text_area("Poderia nos descrever o que está sentindo?", value=st.session_state["sintomas"], key="sintomas", height=120)

    # Botões de ação com navegação
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Prosseguir"):
            navigate("chat_paciente")


