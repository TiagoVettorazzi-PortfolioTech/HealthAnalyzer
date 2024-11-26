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
    add_bg_from_local("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/bg_teste.png")

    # Estilos personalizados com CSS
    st.markdown("""
        <style>
        /* Estiliza a barra lateral inteira (inclui área de expansão) */
        section[data-testid="stSidebar"] {
            background-color: #007199; /* Cor de fundo */
            padding: 20px; /* Espaçamento interno */
            border-right: 1px solid #DDD; /* Linha divisória */
        }

        /* Estiliza botões na sidebar */
        section[data-testid="stSidebar"] .sidebar-button {
            background-color: #F1EDF2; /* Cor padrão dos botões */
            color: #007199;
            border: 1px solid #007199;
            border-radius: 20px;
            padding: 10px;
            text-align: center;
            cursor: pointer;
            margin-bottom: 20px; /* Espaçamento entre botões */
        }
        section[data-testid="stSidebar"] .button-container {
            margin-top: 50px; /* Distância do topo para empurrar os botões para baixo */
        }
        section[data-testid="stSidebar"] .sidebar-button:hover {
            background-color: #D0E8FF; /* Azul claro ao passar o mouse */
        }
        section[data-testid="stSidebar"] .sidebar-button:hover {
            background-color: #D0E8FF; /* Azul claro quando selecionado */
            font-weight: bold;
        }
        /* Estiliza textos dentro da barra lateral */
        section[data-testid="stSidebar"] p {
            color: white;
            font-size: 16px;
            margin-bottom: 15px;
        }

        /* Ajusta o layout principal */
        .main {
            background-color: #FFFFFF; 
            padding: 5px;
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
        st.image("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/MARCA-PORTFOLIO-TECH-MONO.png", width=150)
        
        # Contêiner para deslocar os botões
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-button selected">Atendimentos</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-button">Histórico</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Título da Página
    st.title("Health Analyzer")

    # Inicializar valores de sessão
    session_vars = [
        "paciente", "data_nascimento", "peso", "altura", "pressao_s", "pressao_d", 
        "temperatura", "local_medicao", "oxigenacao", "pressao_dif", "queixas", 
        "comorbidade", "alergias", "observacoes"
    ]
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = ""

    # Layout dos campos
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/Grupo Portfolio/Kanban - Planner/Imagens/TIAGOVETTORAZZI.jpg", width=100, caption="Paciente")
    with col2:
        st.text_input("Paciente", value=st.session_state["paciente"], key="paciente")
        st.text_input("Data de Nascimento", value=st.session_state["data_nascimento"], key="data_nascimento")

    st.write("### Informações de Saúde")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text_input("Peso", value=st.session_state["peso"], key="peso")
        st.text_input("Pressão Arterial Sistólica", value=st.session_state["pressao_s"], key="pressao_s")
    with col2:
        st.text_input("Altura (m)", value=st.session_state["altura"], key="altura")
        st.text_input("Pressão Arterial Diastólica", value=st.session_state["pressao_d"], key="pressao_d")
    with col3:
        st.text_input("Temperatura", value=st.session_state["temperatura"], key="temperatura")
        st.text_input("Local de Medição", value=st.session_state["local_medicao"], key="local_medicao")
    with col4:
        st.text_input("Oxigenação", value=st.session_state["oxigenacao"], key="oxigenacao")
        st.text_input("Pressão Arterial Diferencial", value=st.session_state["pressao_dif"], key="pressao_dif")

    st.text_area("Queixas", value=st.session_state["queixas"], key="queixas", height=50)
    st.text_area("Comorbidade", value=st.session_state["comorbidade"], key="comorbidade", height=50)
    st.text_area("Alergias", value=st.session_state["alergias"], key="alergias", height=50)
    st.text_area("Observações", value=st.session_state["observacoes"], key="observacoes", height=50)

    # Botões de ação
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<button class="button-blue">Cancelar</button>', unsafe_allow_html=True)
    with col2:
        if st.button("Encaminhar atendimento"):
            navigate("chat")

# Função de navegação (mock)
def navigate(page_name):
    st.write(f"Redirecionando para a página: {page_name}")
