# import streamlit as st
# import openai
# import base64
# from pathlib import Path

# def show(navigate):
#     # Configuração da chave da API da OpenAI
#     openai.api_key = ""

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

#     # Adicionando a imagem de fundo
#     add_bg_from_local("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Fundo_Health_Analyzer.png")

#     # Estilos personalizados com CSS para cores e design do layout
#     st.markdown("""
#         <style>
#         /* Ajustes para o layout */
#         .reportview-container {
#             width: 90%; 
#             max-width: 1400px; 
#             margin: auto; 
#         }
#         .main {
#             background-color: #FFFFFF;
#             padding: 5px;
#         }
#         /* Estilo do título */
#         h1 {
#             font-size: 36px;
#             color: #0D47A1;
#             margin-top: -50px;
#         }
#         /* Fundo da mensagem do usuário */
#         .st-chat-message-user {
#             background-color: #DCEFFD;
#             color: #333;
#             padding: 10px;
#             border-radius: 8px;
#             text-align: left;
#         }
#         /* Fundo da mensagem do assistente */
#         .st-chat-message-assistant {
#             background-color: #21D498;
#             color: #333;
#             padding: 10px;
#             border-radius: 8px;
#             text-align: left;
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
#         div.stButton > button:hover {
#             background-color: #005f73; /* Fundo mais escuro ao passar o mouse */
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Título da Aplicação
#     st.title("Health Analyzer")

#     # Recuperar dados da página anterior
#     nome = st.session_state.get("nome", "Informação não registrada")
#     sobrenome = st.session_state.get("sobrenome", "Informação não registrada")
#     alergias = st.session_state.get("alergias", "Nenhuma queixa registrada.")
#     peso = st.session_state.get("peso", "informação não registrada")
#     altura = st.session_state.get("altura", "informação não registrada")
#     sexo = st.session_state.get("sexo", "informação não registrada")
#     temperatura = st.session_state.get("temperatura", "informação não registrada")
#     comorbidade = st.session_state.get("comorbidade", "informação não registrada")
#     sintomas = st.session_state.get("sintomas", "informação não registrada")

#     # Inicializar variáveis de estado da sessão
#     if "openai_model" not in st.session_state:
#         st.session_state["openai_model"] = "gpt-4"

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#         prompt_inicial = (
#             "Você é um assistente médico que tem como objetivo auxiliar e agilizar a triagem de pacientes.\n"
#             f"Cumprimente brevemente o paciente chamando-o pelo nome '{nome}' e peça para ele descrever os sintomas que está sentindo."
#         )

#         response = openai.ChatCompletion.create(
#             model=st.session_state["openai_model"],
#             messages=[{"role": "system", "content": prompt_inicial}],
#             temperature=0.2,
#             max_tokens=300,
#             top_p=0.2,
#             frequency_penalty=0.0,
#             presence_penalty=0.0
#         )
#         st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

#     # Exibir mensagens anteriores
#     for message in st.session_state.messages:
#         avatar = "👤" if message["role"] == "user" else "🩺"
#         with st.chat_message(message["role"], avatar=avatar):
#             st.markdown(message["content"])

#     # Entrada do usuário
#     if user_input := st.chat_input("Descreva seus sintomas:"):
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         # Armazenar os sintomas relatados pelo paciente
#         sintomas_relatados = user_input

#         # Criar o prompt posterior com informações do JSON e sintomas relatados
#         prompt_posterior = f"""
#         Com base nas informações coletadas sobre o paciente:
#         - Nome: {nome}
#         - Peso: {peso} kg
#         - Altura: {altura} m
#         - Idade: {temperatura}
#         - Comorbidades: {comorbidade}
#         - Alergias: {alergias}
#         - Sintomas relatados: {sintomas_relatados}

#         Analise o quadro do paciente com base nas informações fornecidas e determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
#         1. NÃO informe o nível de gravidade ao paciente, em hipótese nenhuma.
#         2. A resposta deve ser direcionada exclusivamente ao paciente, utilizando uma linguagem acolhedora e empática.
#         3. Não inclua perguntas desnecessárias, como se o paciente está bem, pois presume-se que ele está buscando atendimento médico.
#         4. Oriente o paciente de forma adequada conforme o seguinte:
#         - Se o quadro for grave: informe que as informações foram recebidas e que ele terá atendimento prioritário em breve.
#         - Se o quadro for leve ou moderado: informe que as informações foram recebidas e que ele será atendido em breve, com toda a atenção necessária.
#         5. Mantenha o foco no acolhimento e suporte inicial, ressaltando que ele será avaliado por um profissional de saúde em breve.
#         """

#         response = openai.ChatCompletion.create(
#             model=st.session_state["openai_model"],
#             messages=[ 
#                 {"role": "system", "content": "Você é um assistente médico para triagem hospitalar."},
#                 {"role": "user", "content": prompt_posterior},
#             ],
#             temperature=0.3,
#             max_tokens=400,
#             frequency_penalty=0.5,
#             presence_penalty=0.5
#         )
#         st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
#         st.session_state["sintomas_relatados"] = sintomas_relatados

#     # Exibir expander apenas se os sintomas já foram relatados
#     if "sintomas_relatados" in st.session_state:
#         prompt_atendimento = f"""
#         Com base nas informações coletadas sobre o paciente:
#         - Nome: {nome}
#         - Peso: {peso} kg
#         - Altura: {altura} m
#         - Idade: {temperatura}
#         - Comorbidades: {comorbidade}
#         - Alergias: {alergias}
#         - Sintomas relatados: {st.session_state["sintomas_relatados"]}

#         O paciente está em busca de atendimento médico e relatou os tais sintomas, analise-os levando em conta as demais informações paciente
#         determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
#         1. Inicie informando a gravidade do caso, em caso de quadro grave inicie com "ATENÇÃO QUADRO GRAVE" em caso de moderado ou leve 
#         utilize "Quadro leve" ou "Quadro moderado".
#         2. Faça um quadrante utilizando tópicos para por as informações de cadastro do paciente e outro para os sintomas relatados.
#         3. Levando em conta as informações que se tem sobre o paciente e seu quadro clínico dê sugestões breves e gerais a equipe médica que irá atendê-lo.
#         """

#         with st.expander("Informações sobre seu quadro clínico e recomendações:"):
#             response = openai.ChatCompletion.create(
#                 model=st.session_state["openai_model"],
#                 messages=[ 
#                     {"role": "system", "content": "Você é um assistente médico para triagem hospitalar."},
#                     {"role": "user", "content": prompt_atendimento},
#                 ],
#                 temperature=0.4,
#                 max_tokens=500,
#                 frequency_penalty=0.0,
#                 presence_penalty=0.0
#             )
#             st.markdown(response["choices"][0]["message"]["content"])


import streamlit as st
import openai
import base64
from pathlib import Path

def show(navigate):
    # Configuração da chave da API da OpenAI
    openai.api_key = "sk-rUSqK2zQX7STu1sWSPOq01zpo63VD8we9ooEc2SYAjT3BlbkFJVzrrxq_tfSn9jCL4Drh0eZuNpepNij5vD9si5gjBwA"

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

    # Estilos personalizados com CSS para cores e design do layout
    st.markdown("""
        <style>
        /* Ajustes para o layout */
        .reportview-container {
            width: 90%; 
            max-width: 1400px; 
            margin: auto; 
        }
        .main {
            background-color: #FFFFFF;
            padding: 5px;
        }
        /* Estilo do título */
        h1 {
            font-size: 36px;
            color: #0D47A1;
            margin-top: -50px;
        }
        /* Fundo da mensagem do usuário */
        .st-chat-message-user {
            background-color: #DCEFFD;
            color: #333;
            padding: 10px;
            border-radius: 8px;
            text-align: left;
        }
        /* Fundo da mensagem do assistente */
        .st-chat-message-assistant {
            background-color: #21D498;
            color: #333;
            padding: 10px;
            border-radius: 8px;
            text-align: left;
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
        </style>
    """, unsafe_allow_html=True)

    # Título da Aplicação
    st.title("Health Analyzer")

    # Recuperar dados da página anterior
    nome = st.session_state.get("nome", "Informação não registrada")
    sobrenome = st.session_state.get("sobrenome", "Informação não registrada")
    alergias = st.session_state.get("alergias", "Nenhuma queixa registrada.")
    peso = st.session_state.get("peso", "informação não registrada")
    altura = st.session_state.get("altura", "informação não registrada")
    sexo = st.session_state.get("sexo", "informação não registrada")
    temperatura = st.session_state.get("temperatura", "informação não registrada")
    comorbidade = st.session_state.get("comorbidade", "informação não registrada")
    sintomas = st.session_state.get("sintomas", "informação não registrada")

    # Inicializar variáveis de estado da sessão
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt_posterior = f"""
            Com base nas informações coletadas sobre o paciente:
            - Nome: {nome}
            - Peso: {peso} kg
            - Altura: {altura} m
            - Idade: {temperatura}
            - Comorbidades: {comorbidade}
            - Alergias: {alergias}
            - Sintomas relatados: {sintomas}

            Analise o quadro do paciente com base nas informações fornecidas e determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
            1. NÃO informe o nível de gravidade ao paciente, em hipótese nenhuma.
            2. A resposta deve ser direcionada exclusivamente ao paciente, utilizando uma linguagem acolhedora e empática.
            3. Não inclua perguntas desnecessárias, como se o paciente está bem, pois presume-se que ele está buscando atendimento médico.
            4. Oriente o paciente de forma adequada conforme o seguinte:
            - Se o quadro for grave: informe que as informações foram recebidas e que ele terá atendimento prioritário em breve.
            - Se o quadro for leve ou moderado: informe que as informações foram recebidas e que ele será atendido em breve, com toda a atenção necessária.
            5. Mantenha o foco no acolhimento e suporte inicial, ressaltando que ele será avaliado por um profissional de saúde em breve.
            """

    response = openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=[ 
            {"role": "system", "content": "Você é um assistente médico para triagem hospitalar."},
            {"role": "user", "content": prompt_posterior},
        ],
        temperature=0.3,
        max_tokens=400,
        frequency_penalty=0.5,
        presence_penalty=0.5
        )
    st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    # st.session_state["sintomas_relatados"] = sintomas_relatados

    # Exibir mensagens anteriores
    for message in st.session_state.messages:
        avatar = "👤" if message["role"] == "user" else "🩺"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    prompt_atendimento = f"""
    Com base nas informações coletadas sobre o paciente:
    - Nome: {nome}
    - Peso: {peso} kg
    - Altura: {altura} m
    - Idade: {temperatura}
    - Comorbidades: {comorbidade}
    - Alergias: {alergias}
    - Sintomas relatados: {sintomas}

    O paciente está em busca de atendimento médico e relatou os tais sintomas, analise-os levando em conta as demais informações paciente
    determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
    1. Inicie informando a gravidade do caso, em caso de quadro grave inicie com "ATENÇÃO QUADRO GRAVE" em caso de moderado ou leve 
    utilize "Quadro leve" ou "Quadro moderado".
    2. Faça um quadrante utilizando tópicos para por as informações de cadastro do paciente e outro para os sintomas relatados.
    3. Levando em conta as informações que se tem sobre o paciente e seu quadro clínico dê sugestões breves e gerais a equipe médica que irá atendê-lo.
    """

    with st.expander("Informações sobre seu quadro clínico e recomendações:"):
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[ 
                {"role": "system", "content": "Você é um assistente médico para triagem hospitalar."},
                {"role": "user", "content": prompt_atendimento},
            ],
            temperature=0.4,
            max_tokens=500,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        st.markdown(response["choices"][0]["message"]["content"])