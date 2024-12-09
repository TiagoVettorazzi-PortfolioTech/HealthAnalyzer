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
                
        # Botão de voltar ao final da página
        .back-button {
            background-color: #007199;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            text-align: center;
            display: inline-block;
            cursor: pointer;
            font-size: 16px;
            text-decoration: none;
        }
        .back-button:hover {
            background-color: #005f73;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título da Aplicação
    st.title("Health Analyzer")

    # Recuperar dados da página anterior
    data_nascimento = st.session_state.get("data_nascimento", "Informação não registrada")
    nome = st.session_state.get("nome", "Informação não registrada")
    sobrenome = st.session_state.get("sobrenome", "Informação não registrada")
    alergias = st.session_state.get("alergias", "Nenhuma queixa registrada.")
    peso = st.session_state.get("peso", "informação não registrada")
    altura = st.session_state.get("altura", "informação não registrada")
    sexo = st.session_state.get("sexo", "informação não registrada")
    temperatura = st.session_state.get("temperatura", "informação não registrada")
    comorbidade = st.session_state.get("comorbidade", "informação não registrada")

    # Inicializar variáveis de estado da sessão
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4"

    if "messages" not in st.session_state:
        st.session_state.messages = []

        prompt_inicial = (
            "Você é um assistente médico que tem como objetivo auxiliar e agilizar a triagem de pacientes.\n"
            f"Cumprimente brevemente o paciente chamando-o pelo nome '{nome}' e peça para ele descrever os sintomas que está sentindo."
        )

        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[{"role": "system", "content": prompt_inicial}],
            temperature=0.2,
            max_tokens=300,
            top_p=0.2,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

    # Exibir mensagens anteriores
    for message in st.session_state.messages:
        avatar = "👤" if message["role"] == "user" else "🩺"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Entrada do usuário
    if user_input := st.chat_input("Descreva seus sintomas:"):
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Armazenar os sintomas relatados pelo paciente
        sintomas_relatados = user_input

        # Criar o prompt posterior com informações do JSON e sintomas relatados
        prompt_posterior = (
            f"Com base nas informações coletadas sobre o paciente:\n"
            f"Nome: {nome}\n"
            # f"Idade: {idade}\n"
            f"Peso: {peso} kg\n"
            f"Altura: {altura} m\n"
            f"Temperatura corporal: {temperatura}°C\n"
            f"Comorbidades: {comorbidade}\n"
            f"Alergias: {alergias}\n\n"
            f"Sintomas relatados: {sintomas_relatados}\n\n"
            f"1. Analise o quadro com base nas informações fornecidas.\n"
            f"2. Determine o nível de gravidade, se aplicável.\n"
            f"3. Apresente uma suspeita inicial com base nos sintomas relatados.\n"
        )

        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": "Você é um assistente médico para triagem hospitalar."},
                {"role": "user", "content": prompt_posterior},
            ],
            temperature=0.3,
            max_tokens=500,
            top_p=0.9,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})















