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

    # Inicializar valores de sessão
    session_vars = [
        "nome", "sobrenome", "data_nascimento","peso", "altura", "sexo", "cpf", 
        "temperatura", "rg", "matricula", "sintomas", 
        "comorbidade", "alergias", "observacoes"
    ]
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = ""

    # Layout dos campos
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Avatar.png", width=100, caption="Paciente")
    with col2:
        st.text_input("Nome", value=st.session_state["nome"], key="nome")
        st.text_input("Sobrenome", value=st.session_state["sobrenome"], key="sobrenome")

    st.write("### Informações de Saúde")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text_input("Data de Nascimento", value=st.session_state["data_nascimento"], key="data_nascimento")
        st.text_input("Sexo", value=st.session_state["sexo"], key="sexo")
    with col2:
        st.text_input("Idade", value=st.session_state["altura"], key="altura")
        st.text_input("CPF", value=st.session_state["cpf"], key="cpf")
    with col3:
        st.text_input("Peso (Kg)", value=st.session_state["peso"], key="peso")
        st.text_input("RG", value=st.session_state["rg"], key="rg")
    with col4:
        st.text_input("Temperatura (°C)", value=st.session_state["temperatura"], key="temperatura")
        st.text_input("Matrícula", value=st.session_state["matricula"], key="matricula")

    # st.text_area("Descreva o que está sentindo", value=st.session_state["queixas"], key="queixas", height=50)
    st.text_area("Comorbidade", value=st.session_state["comorbidade"], key="comorbidade", height=88)
    st.text_area("Alergias", value=st.session_state["alergias"], key="alergias", height=88)
    st.text_area("Observações", value=st.session_state["observacoes"], key="observacoes", height=88)

    # Botões de ação com navegação
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Voltar"):
            navigate("Welcome")
    # with col3:
    #     if st.button("Versão Atendimento"):
    #         navigate("chat_atendimento")
    with col3:
        if st.button("Prosseguir"):
            navigate("Sintomas")
# # # Função de navegação (mock)
# # def navigate(page_name):
# #     st.write(f"Redirecionando para a página: {page_name}")


# import streamlit as st
# from pathlib import Path
# import base64
# import json

# def show(navigate):
#     def add_bg_from_local(image_file):
#         with Path(image_file).open("rb") as file:
#             encoded_string = base64.b64encode(file.read()).decode()
#         st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background-image: url(data:image/png;base64,{encoded_string});
#                 background-size: cover;
#                 background-position: center;
#                 background-repeat: no-repeat;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )

#     add_bg_from_local("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Fundo_Health_Analyzer.png")

#     st.markdown("""
#         <style>
#         section[data-testid="stSidebar"] {
#             background-color: #007199;
#             padding: 20px;
#             border-right: 1px solid #DDD;
#         }
#         section[data-testid="stSidebar"] div.stButton > button {
#             background-color: white;
#             color: #007199;
#             border: 1px solid #007199;
#             border-radius: 20px;
#             padding: 10px;
#             font-size: 16px;
#             font-weight: bold;
#             cursor: pointer;
#             width: 100%;
#             margin-top: 25px;
#         }
#         section[data-testid="stSidebar"] div.stButton > button:hover {
#             background-color: #D0E8FF;
#             color: #005f73;
#         }
#         div.stButton > button {
#             background-color: #007199;
#             color: white;
#             border: none;
#             border-radius: 15px;
#             padding: 10px 20px;
#             font-size: 16px;
#             font-weight: bold;
#             cursor: pointer;
#             width: 200px;
#         }
#         div.stButton > button:hover {
#             background-color: #005f73;
#         }
#         h1 {
#             font-size: 36px;
#             color: #007199;
#             margin-top: -50px;
#         }
#         input[type="text"], textarea, .stTextArea textarea {
#             border: 1px solid #007199;
#             border-radius: 8px;
#             padding: 8px;
#             box-sizing: border-box;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     with st.sidebar:
#         st.image(
#             "C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/MARCA-PORTFOLIO-TECH-MONO.png",
#             width=150,
#         )
#         if st.button("Cadastro"):
#             navigate("Cadastro")
#         if st.button("Histórico", key="sidebar-historico"):
#             navigate("chat_historico")

#     st.title("Health Analyzer")

#     session_vars = [
#         "nome", "sobrenome", "data_nascimento", "peso", "altura", "sexo", "cpf",
#         "temperatura", "rg", "matricula", "queixas",
#         "comorbidade", "alergias", "observacoes"
#     ]
#     for var in session_vars:
#         if var not in st.session_state:
#             st.session_state[var] = ""

#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Avatar.png", width=100, caption="Paciente")
#     with col2:
#         st.session_state["nome"] = st.text_input("Nome", value=st.session_state["nome"])
#         st.session_state["sobrenome"] = st.text_input("Sobrenome", value=st.session_state["sobrenome"])

#     st.write("### Informações de Saúde")
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.session_state["data_nascimento"] = st.text_input("Data de Nascimento", value=st.session_state["data_nascimento"])
#         st.session_state["sexo"] = st.text_input("Sexo", value=st.session_state["sexo"])
#     with col2:
#         st.session_state["altura"] = st.text_input("Altura", value=st.session_state["altura"])
#         st.session_state["cpf"] = st.text_input("CPF", value=st.session_state["cpf"])
#     with col3:
#         st.session_state["peso"] = st.text_input("Peso (Kg)", value=st.session_state["peso"])
#         st.session_state["rg"] = st.text_input("RG", value=st.session_state["rg"])
#     with col4:
#         st.session_state["temperatura"] = st.text_input("Temperatura (°C)", value=st.session_state["temperatura"])
#         st.session_state["matricula"] = st.text_input("Matrícula", value=st.session_state["matricula"])

#     st.session_state["comorbidade"] = st.text_area("Comorbidade", value=st.session_state["comorbidade"], height=88)
#     st.session_state["alergias"] = st.text_area("Alergias", value=st.session_state["alergias"], height=88)
#     st.session_state["observacoes"] = st.text_area("Observações", value=st.session_state["observacoes"], height=88)

#     col1, col2, col3 = st.columns(3)
#     with col2:
#         if st.button("Prosseguir"):
#             # Salvar os dados no JSON
#             data = {key: st.session_state[key] for key in session_vars}
#             with open("user_data.json", "w", encoding="utf-8") as json_file:
#                 json.dump(data, json_file, ensure_ascii=False, indent=4)
#             navigate("Sintomas")


