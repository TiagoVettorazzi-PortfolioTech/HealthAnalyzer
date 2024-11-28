import openai
import streamlit as st

openai.api_key = "key"

data_nascimento = st.session_state.get("data_nascimento", "Informação não registrada")
nome_paciente = st.session_state.get("paciente", "Paciente")
queixas = st.session_state.get("queixas", "Nenhuma queixa registrada.")
peso = st.session_state.get("peso", "informação não registrada")
altura = st.session_state.get("altura", "informação não registrada")
pressao_s = st.session_state.get("pressao_s", "informação não registrada")
pressao_d = st.session_state.get("pressao_d", "informação não registrada")
pressao_dif = st.session_state.get("pressao_dif", "informação não registrada")
temperatura = st.session_state.get("temperatura", "informação não registrada")
oxigenacao = st.session_state.get("oxigenacao", "informação não registrada")
comorbidade = st.session_state.get("comorbidade", "informação não registrada")

def identificar_caso_grave(temperatura, oxigenacao, pressao_s, pressao_d, queixas, comorbidades):
    criterios_graves = []

    # Verificar temperatura
    if temperatura <= 35:
        criterios_graves.append("Hipotermia grave (≤ 35°C).")
    elif temperatura >= 39:
        criterios_graves.append("Febre alta (≥ 39°C).")

    # Verificar oxigenação
    if oxigenacao <= 90:
        criterios_graves.append("Oxigenação crítica (≤ 90%).")

    # Verificar pressão arterial
    if pressao_s >= 180:
        criterios_graves.append("Crise hipertensiva (sistólica ≥ 180 mmHg).")
    elif pressao_s <= 90:
        criterios_graves.append("Hipotensão severa (sistólica ≤ 90 mmHg).")

    if pressao_d >= 120:
        criterios_graves.append("Crise hipertensiva (diastólica ≥ 120 mmHg).")
    elif pressao_d <= 60:
        criterios_graves.append("Hipotensão grave (diastólica ≤ 60 mmHg).")

    # Verificar sintomas usando OpenAI
    sintomas_graves_prompt = (
        "Baseado no seguinte texto, identifique se há sintomas graves que possam incluir:"
        " dor no peito, falta de ar severa, desmaio, confusão mental, sangramento, ou qualquer outro sintoma crítico relacionado."
        " Retorne uma lista dos sintomas críticos identificados:\n"
        f"Queixas do paciente: {queixas}\n"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente médico virtual."},
            {"role": "user", "content": sintomas_graves_prompt}
        ]
    )

    sintomas_criticos = response['choices'][0]['message']['content'].strip()
    if sintomas_criticos and sintomas_criticos.lower() != "nenhum sintoma crítico identificado":
        criterios_graves.append(f"Sintomas graves relatados: {sintomas_criticos}.")

    # Verificar comorbidades
    comorbidades_graves = ["doença cardíaca", "diabetes", "hipertensão", "câncer", "doença pulmonar"]
    for comorbidade in comorbidades_graves:
        if comorbidade in comorbidades.lower():
            criterios_graves.append(f"Comorbidade relevante identificada: {comorbidade.capitalize()}.")

    # Determinar gravidade
    is_grave = len(criterios_graves) > 0

    detalhes = {
        "grave": is_grave,
        "criterios_graves": criterios_graves
    }
    return detalhes


# Exemplo de uso
resultado = identificar_caso_grave(
    temperatura=40,
    oxigenacao=85,
    pressao_s=190,
    pressao_d=125,
    queixas="Paciente sente dores intensas no peito e dificuldade em respirar.",
    comorbidades="Diabetes e hipertensão."
)

if resultado["grave"]:
    print("Caso grave")
    print("Critérios identificados:")
    for criterio in resultado["criterios_graves"]:
        print(f"- {criterio}")
else:
    print("Caso não identificado como grave.")

print(resultado)