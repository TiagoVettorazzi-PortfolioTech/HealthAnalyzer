# import streamlit as st
# import openai

# def show(navigate):
#     # Configuração da chave da API da OpenAI
#     openai.api_key = "key"

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
#             background-color: #E5F7E7;
#             color: #333;
#             padding: 10px;
#             border-radius: 8px;
#             text-align: left;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Título da Aplicação
#     st.title("Health Analyzer")

#     # Recuperar dados da página anterior
#     nome_paciente = st.session_state.get("paciente", "Paciente")
#     queixas = st.session_state.get("queixas", "Nenhuma queixa registrada.")
#     peso = st.session_state.get("peso", "informação não registrada")
#     altura = st.session_state.get("altura", "informação não registrada")
#     pressao_s = st.session_state.get("pressao_s", "informação não registrada")
#     pressa_d = st.session_state.get("pressao_d", "informação não registrada")
#     pressao_dif = st.session_state.get("pressao_dif", "informação não registrada")
#     temperatura = st.session_state.get("temperatura", "informação não registrada")
#     oxigenacao = st.session_state.get("oxigenacao", "informação não registrada")
#     comorbidade = st.session_state.get("comorbidade","informação não registrada")

#     # Inicializar variáveis de estado da sessão
#     if "openai_model" not in st.session_state:
#         st.session_state["openai_model"] = "gpt-4o-mini"

#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#         prompt_inicial = (
#             f"Você é um assistente médico virtual. O paciente {nome_paciente} tem as seguintes medidas peso:{peso}, altura:{altura},\
#             temperatura:{temperatura}, oxigenação{oxigenacao}, pressão arterial sistólica {pressao_s}, pressão arterial diastólica: {pressa_d},\
#             pressão arterial diferencial: {pressao_dif} comorbidade: {comorbidade}, e  relatou os seguintes sintomas: {queixas}. "\
#             "Com base nisso, indique o médico especialista que o paciente deve procurar e forneça\
#             uma recomendação inicial clara e simples sobre ações que o paciente deve tomar."
#         )
#         # prompt_inicial = (
#         #     f"Você é um assistente médico virtual. O paciente {nome_paciente} com base nos dados da triagem tem as seguintes medidas peso:{peso}, altura:{altura},\
#         #     temperatura:{temperatura}, oxigenação{oxigenacao}, pressão arterial sistólica {pressao_s}, pressão arterial diastólica: {pressa_d},\
#         #     pressão arterial diferencial: {pressao_dif} comorbidade: {comorbidade}, e  relatou os seguintes sintomas: {queixas}. "\
#         #     "Com base nisso, indique o médico especialista mais adquado para atender o paciente e forneça para o médico um resumo\
#         #     do quadro do paciente para que ele possa se preparar para "
#         # )

#         response = openai.ChatCompletion.create(
#             model=st.session_state["openai_model"],
#             messages=[{"role": "system", "content": prompt_inicial}]
#         )["choices"][0]["message"]["content"]

#         # Adicionar a resposta inicial ao histórico
#         st.session_state.messages.append({"role": "assistant", "content": response})

#     # Exibir mensagens anteriores do chat com avatares personalizados
#     for message in st.session_state.messages:
#         avatar = "👤" if message["role"] == "user" else "🩺"  # Ícone de avatar para usuário e assistente
#         with st.chat_message(message["role"], avatar=avatar):
#             st.markdown(message["content"])

#     # Entrada do usuário no chat
#     if prompt := st.chat_input("Deseja compartilhar mais detalhes ou outros sintomas?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user", avatar="👤"):
#             st.markdown(prompt)

#         # Preparar o prompt para o modelo
#         mensagem_do_modelo = (
#             f"Paciente: {nome_paciente}, "
#             f"Queixas iniciais: {queixas}. "
#             f"Peso: {peso}. "
#             f"Altura: {altura}. "
#             f"Oxigenacao: {oxigenacao}. "
#             f"Temperatura: {temperatura}. "
#             f"Pressão Arterial Diastólica: {pressa_d}. "
#             f"Pressão Arterial Sistólica: {pressao_s}. "
#             f"Pressão Arterial Diferencial: {pressao_dif}. "
#             f"Comorbidade: {comorbidade}. "
#             f"Informações adicionais: {prompt}. "
#             f"Baseado nisso, qual orientação você daria?"
#         )
        
#         # Gerar resposta da IA com a informação adicional dos sintomas
#         with st.chat_message("assistant", avatar="🩺"):
#             response = ""
#             # Adicione o contexto inicial, se for a primeira interação
#             if len(st.session_state.messages) == 1:  # Apenas a mensagem inicial existe
#                 st.session_state.messages.insert(0, {
#                 "role": "system", 
#                 "content": prompt_inicial
#             })

#         # Geração da resposta com histórico completo
#             stream = openai.ChatCompletion.create(
#                 model=st.session_state["openai_model"],
#                 messages=st.session_state.messages,  # Envia o histórico completo
#                 stream=True,
#             )

            
#             # Coletar o conteúdo da resposta de forma incremental
#             for chunk in stream:
#                 content = chunk.choices[0].delta.get("content", "")
#                 response += content

#             # Exibir a resposta completa da IA
#             st.markdown(response)

#         # Adicionar a resposta ao histórico de mensagens
#         st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st
import openai

def show(navigate):
    # Configuração da chave da API da OpenAI
    openai.api_key = "sk-rUSqK2zQX7STu1sWSPOq01zpo63VD8we9ooEc2SYAjT3BlbkFJVzrrxq_tfSn9jCL4Drh0eZuNpepNij5vD9si5gjBwA"

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
            background-color: #E5F7E7;
            color: #333;
            padding: 10px;
            border-radius: 8px;
            text-align: left;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título da Aplicação
    st.title("Health Analyzer")

    # Recuperar dados da página anterior
    nome_paciente = st.session_state.get("paciente", "Paciente")
    queixas = st.session_state.get("queixas", "Nenhuma queixa registrada.")
    peso = st.session_state.get("peso", "informação não registrada")
    altura = st.session_state.get("altura", "informação não registrada")
    pressao_s = st.session_state.get("pressao_s", "informação não registrada")
    pressa_d = st.session_state.get("pressao_d", "informação não registrada")
    pressao_dif = st.session_state.get("pressao_dif", "informação não registrada")
    temperatura = st.session_state.get("temperatura", "informação não registrada")
    oxigenacao = st.session_state.get("oxigenacao", "informação não registrada")
    comorbidade = st.session_state.get("comorbidade","informação não registrada")

    # Inicializar variáveis de estado da sessão
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4"

    if "messages" not in st.session_state:
        st.session_state.messages = []
        
        # Adicionar mensagem inicial com recomendação baseada nas queixas
        # prompt_inicial = (
        #     f"Você é um assistente médico virtual. O paciente {nome_paciente} relatou os seguintes sintomas: {queixas}. "
        #     "Com base nisso, forneça uma recomendação inicial clara e simples sobre o qual o paciente deve fazer e indique um médico especialista em que o paciente deve procurar."
        # )
        prompt_inicial = (
            f"Você é um assistente médico virtual. O paciente {nome_paciente} tem as seguintes medidas peso:{peso}, altura:{altura},\
            temperatura:{temperatura}, oxigenação{oxigenacao}, pressão arterial sistólica {pressao_s}, pressão arterial diastólica: {pressa_d},\
            pressão arterial diferencial: {pressao_dif} comorbidade: {comorbidade}, e  relatou os seguintes sintomas: {queixas}. "\
            "Com base nas informações vindas da triagem, incialmente cumprimente o paciente e dê um panorama (de forma bem resumida) acerca da gravidade do quadro, em seguida fale que ele logo será atendido e pergunte se há algo que precisa complementar"
        )
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[{"role": "system", "content": prompt_inicial}]
        )["choices"][0]["message"]["content"]

        # Adicionar a resposta inicial ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Exibir mensagens anteriores do chat com avatares personalizados
    for message in st.session_state.messages:
        avatar = "👤" if message["role"] == "user" else "🩺"  # Ícone de avatar para usuário e assistente
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Entrada do usuário no chat
    if prompt := st.chat_input("Deseja compartilhar mais detalhes ou outros sintomas?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Preparar o prompt para o modelo
        mensagem_do_modelo = (
            f"Paciente: {nome_paciente}, "
            f"Queixas iniciais: {queixas}. "
            f"Peso: {peso}. "
            f"Altura: {altura}. "
            f"Oxigenacao: {oxigenacao}. "
            f"Temperatura: {temperatura}. "
            f"Pressão Arterial Diastólica: {pressa_d}. "
            f"Pressão Arterial Sistólica: {pressao_s}. "
            f"Pressão Arterial Diferencial: {pressao_dif}. "
            f"Comorbidade: {comorbidade}. "
            f"Informações adicionais: {prompt}. "
            f"Baseado nisso, qual orientação você daria?"
        )
        
        # Gerar resposta da IA com a informação adicional dos sintomas
        with st.chat_message("assistant", avatar="🩺"):
            response = ""
            stream = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": "system", "content": "Você é um assistente médico virtual que deve fornecer recomendações inciais simples e claras com base nas informações disponibilizadas sobre a condição de saúde do paciente, por último também deve recomendar um médido especialista."},
                    {"role": "user", "content": mensagem_do_modelo}
                ],
                stream=True,
            )
            
            # Coletar o conteúdo da resposta de forma incremental
            for chunk in stream:
                content = chunk.choices[0].delta.get("content", "")
                response += content

            # Exibir a resposta completa da IA
            st.markdown(response)

        # Adicionar a resposta ao histórico de mensagens
        st.session_state.messages.append({"role": "assistant", "content": response})