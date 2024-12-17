# import streamlit as st
# import openai
# import base64
# from pathlib import Path
# from dotenv import load_dotenv
# import os
# from openai import OpenAI


# def show(navigate):
#     with st.spinner("Carregando informações..."):
#         # Configuração da chave da API da OpenAI
#         load_dotenv()
#         # openai.api_key = os.getenv("OPENAI_KEY")
#         api_key = os.getenv("OPENAI_KEY")

#         def add_bg_from_local(image_file):
#             """
#             Adiciona uma imagem de fundo ao aplicativo Streamlit a partir de um arquivo local.
#             Args:
#             image_file (str): Caminho para o arquivo de imagem local.
#             """
#             with Path(image_file).open("rb") as file:
#                 encoded_string = base64.b64encode(file.read()).decode()
#             st.markdown(
#                 f"""
#                 <style>
#                 .stApp {{
#                     background-image: url(data:image/png;base64,{encoded_string});
#                     background-size: cover;
#                     background-position: center;
#                     background-repeat: no-repeat;
#                 }}
#                 </style>
#                 """,
#                 unsafe_allow_html=True
#             )

#         # Adicionando a imagem de fundo
#         add_bg_from_local("C:/Users/TiagoVettorazzi/Grupo Portfolio/Business Intelligence - Documents/Consulting/01. Projetos Ativos/DS&IA/Health Analyzer/Desenvolvimento/Fundo_Health_Analyzer.png")

#         # Estilos personalizados com CSS para cores e design do layout
#         st.markdown("""
#             <style>
#             /* Estilos do layout */
#             .reportview-container {
#                 width: 90%; 
#                 max-width: 1400px; 
#                 margin: auto; 
#             }
#             .main {
#                 background-color: #FFFFFF;
#                 padding: 5px;
#             }
#             /* Estilo do título */
#             h1 {
#                 font-size: 36px;
#                 color: #0D47A1;
#                 margin-top: -50px;
#             }
#             </style>


#         """, unsafe_allow_html=True)


#         # Título da Aplicação
#         st.title("Health Analyzer")

#         # Recuperar dados da página anterior
#         nome = st.session_state.get("nome", "Informação não registrada")
#         sobrenome = st.session_state.get("sobrenome", "Informação não registrada")
#         alergias = st.session_state.get("alergias", "Nenhuma queixa registrada.")
#         peso = st.session_state.get("peso", "informação não registrada")
#         altura = st.session_state.get("altura", "informação não registrada")
#         sexo = st.session_state.get("sexo", "informação não registrada")
#         temperatura = st.session_state.get("temperatura", "informação não registrada")
#         comorbidade = st.session_state.get("comorbidade", "informação não registrada")
#         sintomas = st.session_state.get("sintomas", "informação não registrada")

#         # Inicializar variáveis de estado da sessão
#         if "openai_model" not in st.session_state:
#             st.session_state["openai_model"] = "gpt-4"

#         if "messages" not in st.session_state:
#             st.session_state.messages = []

#         prompt_posterior = f"""
#                 Com base nas informações coletadas sobre o paciente:
#                 - Nome: {nome}
#                 - Peso: {peso} kg
#                 - Altura: {altura} m
#                 - Idade: {temperatura}
#                 - Comorbidades: {comorbidade}
#                 - Alergias: {alergias}
#                 - Sintomas relatados: {sintomas}

#                 Analise o quadro do paciente com base nas informações fornecidas e determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
#                 1. NÃO informe o nível de gravidade ao paciente, em hipótese nenhuma.
#                 2. A resposta deve ser direcionada exclusivamente ao paciente, utilizando uma linguagem acolhedora e empática.
#                 3. Não inclua perguntas desnecessárias, como se o paciente está bem, pois presume-se que ele está buscando atendimento médico.
#                 4. Oriente o paciente de forma adequada conforme o seguinte:
#                 - Se o quadro for grave: informe que as informações foram recebidas e que ele terá atendimento prioritário em breve.
#                 - Se o quadro for leve ou moderado: informe que as informações foram recebidas e que ele será atendido em breve, com toda a atenção necessária.
#                 5. Mantenha o foco no acolhimento e suporte inicial, ressaltando que ele será avaliado por um profissional de saúde em breve.
#             """
#         load_dotenv()
#         # client = OpenAI(api_key = os.environ.get("OPENAI_KEY"))
#         client = openai.Client(api_key=api_key)
#         response = client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=[ 
#                 {"role": "system", "content": "Você é um assistente médico para triagem hospitalar."},
#                 {"role": "user", "content": prompt_posterior},
#             ],
#             temperature=0.3,
#             max_tokens=400,
#             frequency_penalty=0.5,
#             presence_penalty=0.5
#             )
#         # st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
#         message_content = response.choices[0].message.content
#         st.session_state.messages.append({"role": "assistant", "content": message_content})

#         # Exibir mensagens anteriores
#         for message in st.session_state.messages:
#             avatar = "👤" if message["role"] == "user" else "🩺"
#             with st.chat_message(message["role"], avatar=avatar):
#                 st.markdown(message["content"])

#         prompt_atendimento = f"""
#         Com base nas informações coletadas sobre o paciente:
#         - Nome: {nome}
#         - Peso: {peso} kg
#         - Altura: {altura} m
#         - Idade: {temperatura}
#         - Comorbidades: {comorbidade}
#         - Alergias: {alergias}
#         - Sintomas relatados: {sintomas}

#         O paciente está em busca de atendimento médico e relatou os tais sintomas, analise-os levando em conta as demais informações paciente
#         determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
#         1. Inicie informando a gravidade do caso, em caso de quadro grave inicie com "ATENÇÃO QUADRO GRAVE" em caso de moderado ou leve 
#         utilize "Quadro leve" ou "Quadro moderado".
#         2. Faça um quadrante utilizando tópicos para por as informações de cadastro do paciente e outro para os sintomas relatados.
#         3. Levando em conta as informações que se tem sobre o paciente e seu quadro clínico dê sugestões breves e gerais a equipe médica que irá atendê-lo.
#         """

#         with st.expander("Informações sobre seu quadro clínico e recomendações:"):
#             response = client.chat.completions.create(
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
#             # st.markdown(response["choices"][0]["message"]["content"])
#             message_content = response.choices[0].message.content
#             st.markdown(message_content)




import streamlit as st
import openai
import base64
from pathlib import Path
from dotenv import load_dotenv
import os

def show(navigate):
    with st.spinner("Carregando informações..."):
        # Configuração da chave da API da OpenAI
        load_dotenv()
        api_key = os.getenv("OPENAI_KEY")

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
            .chat-message-assistant {
                background-color:#DDE7F0; 
                color: #333;  /* Cor do texto */
                padding: 10px;  /* Espaçamento interno */
                border-radius: 15px;  /* Bordas arredondadas */
                margin-bottom: 10px;  /* Espaçamento inferior */
                box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1);
            }
            .chat-message-user {
                background-color: rgb(205, 198, 255);  /* Fundo laranja claro */
                color: #333;  /* Cor do texto */
                padding: 10px;  /* Espaçamento interno */
                border-radius: 8px;  /* Bordas arredondadas */
                margin-bottom: 10px;  /* Espaçamento inferior */
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
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

        client = openai.Client(api_key=api_key)
        response = client.chat.completions.create(
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

        message_content = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": message_content})

        # Exibir mensagens anteriores com estilos personalizados
        for message in st.session_state.messages:
            avatar = "👤" if message["role"] == "user" else "🩺"
            role_class = "chat-message-user" if message["role"] == "user" else "chat-message-assistant"
            st.markdown(
                f"""
                <div class="{role_class}">
                    <div style="display: flex; align-items: center;">
                        <div style="font-size: 24px; margin-right: 10px;">{avatar}</div>
                        <div>{message["content"]}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        prompt_atendimento = f"""
        Com base nas informações coletadas sobre o paciente:
        - Nome: {nome}
        - Peso: {peso} kg
        - Altura: {altura} m
        - Idade: {temperatura}
        - Comorbidades: {comorbidade}
        - Alergias: {alergias}
        - Sintomas relatados: {sintomas}

        O paciente está em busca de atendimento médico e relatou os tais sintomas, analise-os levando em conta as demais informações do paciente
e determine o nível de gravidade entre "leve", "moderado" e "grave". **IMPORTANTE**:
        1. Inicie informando a gravidade do caso, em caso de quadro grave inicie com "ATENÇÃO QUADRO GRAVE" em caso de moderado ou leve 
        utilize "Quadro leve" ou "Quadro moderado".
        2. Faça um quadrante utilizando tópicos para pôr as informações de cadastro do paciente e outro para os sintomas relatados.
        3. Levando em conta as informações que se tem sobre o paciente e seu quadro clínico dê sugestões breves e gerais à equipe médica que irá atendê-lo.
        """

        with st.expander("Informações sobre seu quadro clínico e recomendações:"):
            response = client.chat.completions.create(
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

            message_content = response.choices[0].message.content
            st.markdown(
                f"""
                <div class="chat-message-assistant">
                    {message_content}
                </div>
                """,
                unsafe_allow_html=True
            )



