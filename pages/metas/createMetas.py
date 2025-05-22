import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.cadastrarMeta.cadastrarMetaCon as cadastrarMetaCon
import controllers.cadastrarMeta.listarMetasCon as listarMetasCon
import time
import streamlit as st
from datetime import datetime

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

def createMeta():

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
        input_empreendimento = st.selectbox("**Empreendimento**", options=['x', 'y'], key="selectbox_empreendimento_create")
        
    with col2:
        input_periodo = st.selectbox("**Período**", options=lista_meses_ano, key="selectbox_periodo_create") #produto

    with col3:
        input_meta = st.text_input("**Meta**", value="")

    input_observacao = st.text_input("**Observação**", key="obs_create_meta")

    input_button_submit = st.button("**Enviar**", key="button_create")
        
    if input_button_submit:

        if cadastrarMetaCon.validacaoInsertMetaEmpreendimento(input_empreendimento, input_periodo):
            return st.error(f"Meta do empreendimento **{input_empreendimento}** no período de **{input_periodo}** já lançado!")
        
        if input_meta == "":
            return st.error("O campo da meta está sem valor")

        with st.spinner("Atualizando..."):   
            sistema.empreendimento  = input_empreendimento 
            sistema.mes_ano         = input_periodo
            sistema.meta            = int(input_meta) 
            sistema.observacao      = input_observacao
            sistema.user            = user
            cadastrarMetaCon.insertMetas(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Meta do empreendimento **{input_empreendimento}** lançada!")  
        time.sleep(2)
        success_container.empty()