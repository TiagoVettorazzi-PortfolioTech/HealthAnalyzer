import streamlit as st

# Forçar fundo claro e aplicar estilos personalizados
st.markdown("""
    <style>
    /* Sobrescreve qualquer estilo de tema escuro */
    .reportview-container, .main {
        background-color: #F2F0F2 !important; /* Força fundo claro */
        color: #000000; /* Força texto escuro */
    }
    
    .chat-bubble {
        background-color: #007199; /* cor azul clara para as mensagens do bot */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word;
        font-size: 16px;
        color: #FFFFFF;
    }
    
    .chat-bubble-user {
        background-color: #23B0D9; /* cor verde clara para as mensagens do usuário */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word;
        font-size: 16px;
        color: #FFFFFF;
    }
    
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 20px;
    }
    
    .chat-container-user {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        padding: 20px;
    }
    
    h1 {
        color: #202020; /* título escuro */
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho do chatbot
st.title("Health Analyzer")
st.write("Olá, *nome do paciente*! Estou aqui para te ajudar a ter um acesso mais rápido à tua consulta.")
st.write("Caso precise encerrar essa conversa, é só enviar 'encerrar' no chat.")
st.write("Agora, me conta como você está se sentindo.")

# Chatbot com exemplo de conversa
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Mensagem do bot
st.markdown('<div class="chat-bubble">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque felis aliquam facilisis scelerisque ullamcorper molestie habitant morbi.</div>', unsafe_allow_html=True)

# Entrada do usuário (simulando resposta)
st.markdown('<div class="chat-container-user"><div class="chat-bubble-user">Estou com dor de cabeça há 3 dias.</div></div>', unsafe_allow_html=True)

# Mais mensagens do bot
st.markdown('<div class="chat-bubble">Entendi! Há quantos dias você está com esses sintomas?</div>', unsafe_allow_html=True)

st.markdown('<div class="chat-container-user"><div class="chat-bubble-user">Há 3 dias</div></div>', unsafe_allow_html=True)

st.markdown('<div class="chat-bubble">Você convive com alguma comorbidade?</div>', unsafe_allow_html=True)

# Entrada do usuário
st.markdown('<div class="chat-container-user"><div class="chat-bubble-user">Sim, tenho diabetes.</div></div>', unsafe_allow_html=True)

st.markdown('<div class="chat-bubble">Você é alérgico a algum medicamento?</div>', unsafe_allow_html=True)

# Entrada do usuário
st.markdown('<div class="chat-container-user"><div class="chat-bubble-user">Sim, sou alérgico a amoxicilina.</div></div>', unsafe_allow_html=True)

st.markdown('<div class="chat-bubble">Informações recebidas! Agora vamos confirmar o local de atendimento mais próximo.</div></div>', unsafe_allow_html=True)

st.markdown('<div class="chat-container-user"><div class="chat-bubble-user">Obrigado!</div></div>', unsafe_allow_html=True)

# Finalizando o chat
st.markdown('</div>', unsafe_allow_html=True)

# Botões de interação
st.button("Confirmar chegada")
st.button("Abrir no mapa")
