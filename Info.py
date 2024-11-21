# import streamlit as st

# def show(navigate):
#     # Estilos personalizados com CSS para cores e design do layout
#     st.markdown("""
#         <style>
#         .reportview-container {
#             width: 90%; 
#             max-width: 1400px; 
#             margin: auto; 
#         }
#         .main {
#             background-color: #FFFFFF; /* fundo da área principal */
#             padding: 5px;
#         }
#         h1 {
#             font-size: 36px;
#             color: #007199; /* Azul escuro para o título */
#             margin-top: -50px; /* Ajustei a margem para puxar mais para cima */
#         }
#         .button-blue { /* Botão de encaminhar atendimento */ 
#             background-color: #007199;
#             color: white;
#             padding: 10px;
#             border-radius: 15px;
#             width: 200px;
#             border: 1px solid #0D47A1;
#             cursor: pointer;
#             margin: 10px;
#             text-align: center; /* Centraliza o texto */
#             display: inline-block; /* Permite o alinhamento correto */
#         }
#         .button-blue:hover {
#             background-color: #0277BD;
#         }
#         .button-white {
#             background-color: #007199;
#             color: white;
#             padding: 10px;
#             border-radius: 15px;
#             width: 200px;
#             border: 1px solid #0D47A1;
#             cursor: pointer;
#             margin: 10px auto;
#             text-align: center;
#             display: block;
#             text-decoration: none;
#         }
#         .button-white:hover {
#             background-color: #0277BD;
#             color: white;
#         }
        
#         .profile-img {
#             border-radius: 50%;
#             width: 100px;
#             height: 100px;
#             display: block;
#             margin: 0 auto; /* Centraliza a imagem */
#         }
#         .sidebar {
#             display: flex;
#             flex-direction: column;
#             align-items: center;  /* Centraliza o conteúdo da sidebar */
#         }
#         .main-content {
#             margin-left: 150px; /* Largura da sidebar para ajustar o conteúdo */
#             padding: 0px;
#             background-color: #FFFFFF; /* Fundo branco para o resto da tela */
#         }
        
#         /* Estilo para os campos de entrada de texto e área de texto */
#         input[type="text"], textarea, .stTextArea textarea {
#             border: 1px solid #007199; /* Borda azul */
#             border-radius: 8px;
#             padding: 8px;
#             box-sizing: border-box; /* Para ajustar o preenchimento */
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Sidebar
#     with st.sidebar:
#         st.image(
#             "C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/MARCA-PORTFOLIO-TECH.png", 
#             width=150
#         )
        
#         # Botões formatados na sidebar
#         st.markdown('<div class="sidebar"><button class="button-white">Atendimentos</button><button class="button-white">Histórico</button></div>', unsafe_allow_html=True)

#     # Título da Página
#     st.title("Health Analyzer")

#    # Configurar o valor inicial no st.session_state apenas se ainda não existir
#     if "paciente" not in st.session_state:
#         st.session_state["paciente"] = ""
#     if "data_nascimento" not in st.session_state:
#         st.session_state["data_nascimento"] = ""
#     if "peso" not in st.session_state:
#         st.session_state["peso"] = ""
#     if "altura" not in st.session_state:
#         st.session_state["altura"] = ""
#     if "pressao_s" not in st.session_state:
#         st.session_state["pressao_s"] = ""
#     if "pressao_d" not in st.session_state:
#         st.session_state["pressao_d"] = ""
#     if "temperatura" not in st.session_state:
#         st.session_state["temperatura"] = ""
#     if "local_medicao" not in st.session_state:
#         st.session_state["local_medicao"] = ""
#     if "oxigenacao" not in st.session_state:
#         st.session_state["oxigenacao"] = ""
#     if "pressao_dif" not in st.session_state:
#         st.session_state["pressao_dif"] = ""
#     if "queixas" not in st.session_state:
#         st.session_state["queixas"] = ""
#     if "comorbidade" not in st.session_state:
#         st.session_state["comorbidade"] = ""
#     if "alergias" not in st.session_state:
#         st.session_state["alergias"] = ""
#     if "observacoes" not in st.session_state:
#         st.session_state["observacoes"] = ""

#     # Layout dos campos
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/Grupo Portfolio/Kanban - Planner/Imagens/TIAGOVETTORAZZI.jpg", 
#                 use_column_width=False, 
#                 width=100, 
#                 caption="Paciente")
#     with col2:
#         st.text_input("Paciente", value=st.session_state["paciente"], key="paciente", disabled=False)
#         st.text_input("Data de Nascimento", value=st.session_state["data_nascimento"], key="data_nascimento", disabled=False)

#     st.write("### Informações de Saúde")

#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.text_input("Peso", value=st.session_state["peso"], key="peso", disabled=False)
#         st.text_input("Pressão Arterial Sistólica", value=st.session_state["pressao_s"], key="pressao_s")
#     with col2:
#         st.text_input("Altura (m)", value=st.session_state["altura"], key="altura", disabled=False)
#         st.text_input("Pressão Arterial Diastólica", value=st.session_state["pressao_d"], key="pressao_d")
#     with col3:
#         st.text_input("Temperatura", value=st.session_state["temperatura"], key="temperatura")
#         st.text_input("Local de Medição", value=st.session_state["local_medicao"], key="local_medicao")
#     with col4:
#         st.text_input("Oxigenação", value=st.session_state["oxigenacao"], key="oxigenacao")
#         st.text_input("Pressão Arterial Diferencial", value=st.session_state["pressao_dif"], key="pressao_dif")

#     st.text_area("Queixas", value=st.session_state["queixas"], key="queixas", height=50, disabled=False)
#     st.text_area("Comorbidade", value=st.session_state["comorbidade"], key="comorbidade", height=50, disabled=False)
#     st.text_area("Alergias", value=st.session_state["alergias"], key="alergias", height=50, disabled=False)

#     st.text_area("Observações", value=st.session_state["observacoes"], key="observacoes", 
#                 height=50, disabled=False)

#     # Botões de ação
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         st.markdown('<button class="button-custom">Cancelar</button>', unsafe_allow_html=True)

#     with col2:
#         if st.button("Encaminhar atendimento", key="encaminhar"):
#             navigate("chat")

#     # Função para navegação (mock)
# def navigate(page_name):
#         st.write(f"Redirecionando para a página: {page_name}")

import streamlit as st

def show(navigate):
    # Estilos personalizados com CSS
    st.markdown("""
        <style>
        .reportview-container {
            width: 90%; 
            max-width: 1400px; 
            margin: auto; 
        }
        .main {
            background-color: #FFFFFF; 
            padding: 5px;
        }
        h1 {
            font-size: 36px;
            color: #007199;
            margin-top: -50px;
        }
        .button-blue, .button-white {
            background-color: #007199;
            color: white;
            padding: 10px;
            border-radius: 15px;
            width: 200px;
            border: 1px solid #0D47A1;
            cursor: pointer;
            text-align: center;
            display: inline-block;
        }
        .button-blue:hover, .button-white:hover {
            background-color: #0277BD;
        }
        .profile-img {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            display: block;
            margin: 0 auto;
        }
        .sidebar {
            display: flex;
            flex-direction: column;
            align-items: center;
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
        st.image("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/MARCA-PORTFOLIO-TECH.png", width=150)
        st.markdown('<div class="sidebar"><button class="button-white">Atendimentos</button><button class="button-white">Histórico</button></div>', unsafe_allow_html=True)

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























