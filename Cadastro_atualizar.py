import streamlit as st
from pathlib import Path
import base64
import json

# Caminho para o arquivo JSON de persistência
JSON_FILE_PATH = "user_data.json"

# Função para carregar dados do JSON
def load_data():
    if Path(JSON_FILE_PATH).exists():
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
    return {}

# Função para salvar dados no JSON
def save_data(data):
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def show(navigate):
    # Função para adicionar uma imagem de fundo a partir de um arquivo local
    def add_bg_from_local(image_file):
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
    st.markdown("""<style>
        /* Estilos personalizados aqui */
        </style>
    """, unsafe_allow_html=True)
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
        h1 {
            font-size: 36px;
            color: #007199;
            margin-top: -50px;
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
            navigate("Cadastro")
        if st.button("Histórico", key="sidebar-historico"):
            navigate("chat_historico")

    # Título da Página
    st.title("Health Analyzer")

    # Carregar dados persistentes
    user_data = load_data()

    # Inicializar valores de sessão
    session_vars = [
        "nome", "sobrenome", "data_nascimento", "peso", "altura", "sexo", "cpf",
        "temperatura", "rg", "matricula", "queixas", "comorbidade", "alergias", "observacoes"
    ]
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = ""

    # Layout dos campos
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Avatar.png", width=100, caption="Paciente")
    with col2:
        st.text_input("xNome", value=st.session_state["nome"], key="nome")
        st.text_input("Sobrenome", value=st.session_state["sobrenome"], key="sobrenome")

    st.write("### Informações de Saúde")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text_input("Data de Nascimento", value=st.session_state["data_nascimento"], key="data_nascimento")
        st.text_input("Sexo", value=st.session_state["sexo"], key="sexo")
    with col2:
        st.text_input("Altura (m)", value=st.session_state["altura"], key="altura")
        st.text_input("CPF", value=st.session_state["cpf"], key="cpf")
    with col3:
        st.text_input("Peso (Kg)", value=st.session_state["peso"], key="peso")
        st.text_input("RG", value=st.session_state["rg"], key="rg")
    with col4:
        st.text_input("Idade", value=st.session_state["temperatura"], key="temperatura")
        matricula = st.text_input("Matrícula", value=st.session_state["matricula"], key="matricula")

    st.text_area("Comorbidades", value=st.session_state["comorbidade"], key="comorbidade", height=88)
    st.text_area("Alergias", value=st.session_state["alergias"], key="alergias", height=88)
    st.text_area("Observações", value=st.session_state["observacoes"], key="observacoes", height=88)

    if matricula:
        if matricula not in user_data:
            user_data[matricula] = {}

        for var in session_vars:
            user_data[matricula][var] = st.session_state[var]

        save_data(user_data)

    # Botões de ação com navegação
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Voltar"):
            navigate("Sintomas")
    with col3:
        if st.button("Concluir"):
            navigate("Sintomas")

# # Função de navegação (mock)
# def navigate(page_name):
#     st.write(f"Redirecionando para a página: {page_name}")