import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.marketing.cadastrarPeriodo.cadastrarPeriodoCon as cadastrarPeriodoCon
import time
import streamlit as st
from datetime import datetime, timedelta

ano_atual = datetime.now().year
meses = [
    "Janeiro", 
    "Fevereiro", 
    "Março", 
    "Abril", 
    "Maio", 
    "Junho",
    "Julho", 
    "Agosto", 
    "Setembro", 
    "Outubro", 
    "Novembro", 
    "Dezembro"
]
lista_meses_ano = [f"{mes}/{ano_atual}" for mes in meses]

def createPeriodo():

    # def ListEmpreendimentoFiltro():
    #     customerList = []

    #     for item in listEmpreendimentoCon.selecionarEmpreendimento():
    #         customerList.append(item.empreendimento)

    #     return customerList

    # empreendimento_ = ListEmpreendimentoFiltro() 

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        input_dt_inicio = st.date_input("**Data de Início**", format="DD/MM/YYYY", key="dt_inicio_input")
        
    with col2:
        input_dt_fim = st.date_input("**Data de Fim**", format="DD/MM/YYYY", key="dt_fim_input")

    with col3:
        input_mes_ano = st.selectbox("**Período**", options=lista_meses_ano, key="selectbox_periodo_create") #produto

    input_observacao = st.text_input("**Observação**", key="obs_create_meta")

    input_button_submit = st.button("**Enviar**", key="button_create_periodo")
        
    if input_button_submit:
        with st.spinner("Atualizando..."):   

            data_atual = input_dt_inicio
            while data_atual <= input_dt_fim:
                sistema.periodo_mkt = data_atual 
                sistema.mes_ano     = input_mes_ano
                sistema.observacao  = input_observacao
                sistema.user        = user
                cadastrarPeriodoCon.insertPeriodo(sistema)
                data_atual += timedelta(days=1)  # Avança para o próximo dia
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Período de **{input_mes_ano}** cadastrado com sucesso!")  
        time.sleep(2)
        success_container.empty()