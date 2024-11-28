# import streamlit as st
# import base64
# from pathlib import Path

# def show(navigate):
#     # Função para adicionar uma imagem de fundo a partir de um arquivo local
#     def add_bg_from_local(image_file):
#         """
#         Adiciona uma imagem de fundo ao aplicativo Streamlit a partir de um arquivo local.
#         Args:
#         image_file (str): Caminho para o arquivo de imagem local.
#         """
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

#     # Chamando a função para adicionar o fundo
#     add_bg_from_local("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/Fundo_Health_Analyzer.png")

#     # Estilos personalizados com CSS para cores e design do layout
#     st.markdown("""
#         <style>
#         .reportview-container {
#             width: 90%; 
#             max-width: 1400px; 
#             margin: auto; 
#         }
#         h1 {
#             font-size: 36px;
#             color: #0D47A1; /* Azul escuro para o título */
#             margin-top: -70px; /* Ajustei a margem para puxar mais para cima */
#         }
#         h2 {
#             font-size: 28px;
#             color: #000000; /* Preto para o texto principal */
#             margin-bottom: 30px;
#         }
#         p {
#             font-size: 18px;
#             color: #606060; /* Cinza para o subtítulo */
#             margin-bottom: 40px;
#         }
#         .login-button {
#             background-color: #01579B; /* Azul escuro para o botão */
#             color: white;
#             padding: 15px 30px;
#             font-size: 18px;
#             border-radius: 5px;
#             border: none;
#             cursor: pointer;
#             margin-top: 20px;
#             width: 100%;
#         }
#         .login-button:hover {
#             background-color: #0277BD;
#         }
#         input[type="text"], textarea, .stTextArea textarea {
#             border: 1px solid #03738C;
#             border-radius: 8px;
#             padding: 8px;
#             box-sizing: border-box;
#         }
#         .form-container {
#             max-width: 400px;
#             margin: auto;
#             padding: 20px;
#         }
#         .image-container {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             margin-top: 50px;
#         }
#         .link {
#             font-size: 14px;
#             color: #01579B;
#             text-align: left;
#         }
#         .link:hover {
#             text-decoration: underline;
#         }
#         }
#         /* Estiliza botões do Streamlit */
#         div.stButton > button {
#             background-color: #007199; /* Fundo azul */
#             color: white; /* Texto branco */
#             border: none; /* Remover borda */
#             border-radius: 15px; /* Bordas arredondadas */
#             padding: 10px 20px; /* Espaçamento interno */
#             font-size: 16px; /* Tamanho do texto */
#             font-weight: bold; /* Texto em negrito */
#             cursor: pointer; /* Alterar cursor para ponteiro */
#             width: 200px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Título da página e menu superior
#     st.markdown("<h1>Health Analyzer</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align:right;margin-top: -70px;'>Contatos</p>", unsafe_allow_html=True)

#     # Dividindo a página em duas colunas
#     col1, col2, col3 = st.columns([3, 1, 3])

#     # Coluna da esquerda: Formulário de login
#     with col1:
#         st.markdown("<h2>Bem-vindo ao seu <span style='color:#0D47A1;'>Health Analyzer</span></h2>", unsafe_allow_html=True)
#         st.text_input("Matrícula ou CPF", value="0000000", key="cpf", max_chars=11, help="Insira sua matrícula ou CPF")
#         st.text_input("Senha", value="******",type="password", key="senha")
#         # st.markdown('<a href="#" class="link">Esqueceu sua senha?</a>', unsafe_allow_html=True)

#         if st.button("Entrar"):
#             navigate("Info")  # Navegar para a página 'info'

#     # Coluna da direita: Imagem ilustrativa
#     with col3:
#         st.image('C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/Figura_tela_inicial.png')
import streamlit as st
import base64
from pathlib import Path

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

    # Chamando a função para adicionar o fundo
    add_bg_from_local("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/Fundo_Health_Analyzer.png")

    # Estilos personalizados com CSS para cores e design do layout
    st.markdown("""
        <style>
        .reportview-container {
            width: 90%; 
            max-width: 1400px; 
            margin: auto; 
        }
        h1 {
            font-size: 36px;
            color: #0D47A1; /* Azul escuro para o título */
            margin-top: -70px; /* Ajustei a margem para puxar mais para cima */
        }
        h2 {
            font-size: 28px;
            color: #000000; /* Preto para o texto principal */
            margin-bottom: 30px;
        }
        p {
            font-size: 18px;
            color: #606060; /* Cinza para o subtítulo */
            margin-bottom: 40px;
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
            width: 100%;
        }
        .login-button:hover {
            background-color: #0277BD;
        }
        input[type="text"], textarea, .stTextArea textarea {
            border: 1px solid #03738C;
            border-radius: 8px;
            padding: 8px;
            box-sizing: border-box;
        }
        .form-container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 50px;
        }
        .link {
            font-size: 14px;
            color: #01579B;
            text-align: left;
        }
        .link:hover {
            text-decoration: underline;
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

        /* Garantir que o texto dentro do botão é branco */
        div.stButton > button > span {
            color: white !important; /* Texto branco no botão */
        }

        div.stButton > button:hover {
            background-color: #005f73; /* Fundo mais escuro ao passar o mouse */
        }
        </style>
    """, unsafe_allow_html=True)

    # Título da página e menu superior
    st.markdown("<h1>Health Analyzer</h1>", unsafe_allow_html=True)

    # Dividindo a página em duas colunas
    col1, col2, col3 = st.columns([3, 1, 3])

    # Coluna da esquerda: Formulário de login
    with col1:
        st.markdown("<h2>Bem-vindo ao seu <span style='color:#0D47A1;'>Health Analyzer</span></h2>", unsafe_allow_html=True)
        st.text_input("Matrícula ou CPF", value="0000000", key="cpf", max_chars=11, help="Insira sua matrícula ou CPF")
        st.text_input("Senha", value="******", type="password", key="senha")
        # st.markdown('<a href="#" class="link">Esqueceu sua senha?</a>', unsafe_allow_html=True)

        if st.button("Entrar"):
            navigate("Info")  # Navegar para a página 'info'

    # Coluna da direita: Imagem ilustrativa
    with col3:
        st.image('C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/Figura_tela_inicial.png')
