import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.marketing.cadastrarPeriodo.deletePeriodoCon as deletePeriodoCon
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

def deletePeriodo():

    # Verifica se o usuário está autenticado
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    # Garante que o usuário autenticado está disponível no session_state
    user = st.session_state.get("user", "")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        input_mes_ano = st.selectbox("**Deletar Período**", options=lista_meses_ano, key="selectbox_periodo_delete") #produto
        
    with col2:
        None

    with col3:
        None

    input_button_submit = st.button("**Enviar**", key="button_delete")

    if input_button_submit:
        with st.spinner("Atualizando..."):  
            sistema.user    = user  
            sistema.mes_ano = input_mes_ano
            deletePeriodoCon.deletePeriodo(sistema.user, sistema.mes_ano)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Período de **{input_mes_ano}** deletado com sucesso!")  
        time.sleep(2)
        success_container.empty()