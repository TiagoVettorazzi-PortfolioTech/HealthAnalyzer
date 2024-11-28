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
    add_bg_from_local("C:/Users/TiagoVettorazzi/OneDrive - Grupo Portfolio/Área de Trabalho/Streamlit/Fundo_Health_Analyzer.png")

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
    idade = st.session_state.get("idade", "Informação não registrada")
    nome = st.session_state.get("nome", "Informação não registrada")
    queixas = st.session_state.get("queixas", "Nenhuma queixa registrada.")
    peso = st.session_state.get("peso", "informação não registrada")
    altura = st.session_state.get("altura", "informação não registrada")
    pressao_s = st.session_state.get("pressao_s", "informação não registrada")
    pressao_d = st.session_state.get("pressao_d", "informação não registrada")
    pressao_dif = st.session_state.get("pressao_dif", "informação não registrada")
    temperatura = st.session_state.get("temperatura", "informação não registrada")
    oxigenacao = st.session_state.get("oxigenacao", "informação não registrada")
    comorbidade = st.session_state.get("comorbidade", "informação não registrada")

    # Inicializar variáveis de estado da sessão
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4"

    if "messages" not in st.session_state:
        st.session_state.messages = []

        prompt_inicial = (
            f"O paciente {nome} forneceu as seguintes informações durante a triagem: "
            f"Idade: {idade}, peso: {peso} kg, altura: {altura} m, temperatura corporal: {temperatura}°C, nível de oxigenação: {oxigenacao}%, "
            f"pressão arterial sistólica: {pressao_s} mmHg, pressão arterial diastólica: {pressao_d} mmHg, pressão arterial diferencial: {pressao_dif} mmHg. "
            f"Comorbidades relatadas: {comorbidade}. "
            f"Além disso, o paciente descreveu os seguintes sintomas: {queixas}. "
            "Com base nessas informações de triagem, siga estas instruções:\n"
            "1. Analise o quadro com base nas informações fornecidas e determine o nível de gravidade, se considerado caso grave deixe isso/n"  
            "Explicito de forma enfática no início do texto e utilizando letras maiúsculas para destacar e diga de forma breve o motivo por qual o caso é grave./n"
            "o paciente já será atendido por um médico, dessa forma não faça recomendações. Utilize somente as informações que foram forncecidas, não cite as que não foram \n"
            "2. Apresente em um quadrante dividido em tópicos os sintomas relatados na triagem"
            "3. Diga de forma breve e geral a suspeita que paciente apresenta com base nas informações da triagem"
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
        # Adicionar a resposta inicial ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

    # Exibir mensagens anteriores do chat com avatares personalizados
    for message in st.session_state.messages:
        avatar = "👤" if message["role"] == "user" else "🩺"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
    
    if st.button("Voltar"):
        navigate("Info")


