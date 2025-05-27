import streamlit as st
import models.sistema as sistema
import controllers.cadastrarMeta.cadastrarMetaCon as cadastrarMetaCon
import controllers.cadastrarMeta.listarEmpreendimentoCon as listarEmpreendimentoCon
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

    def ListEmpreendimentoFiltro():
        customerList = []

        for item in listarEmpreendimentoCon.selecionarEmpreendimento():
            customerList.append(item.empreendimento)

        return customerList

    empreendimento_ = ListEmpreendimentoFiltro() 

    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("Você precisa estar autenticado.")
        return
    
    user = st.session_state.get("user", "")
        
    col1, col2 = st.columns(2)

    with col1:
        input_nm_meta = st.selectbox(
            "**Nome da Meta**", 
            options=[
                'Leads por empreendimento', 
                'Participação marketing', 
                'Conversão de Leads x vendas', 
                'Vendas marketing',
                'Vendas comercial',
                'Aproveitamento do Lead',
                'Perdas Automáticas'
            ], 
            index=None,
            placeholder='Selecione a Meta',
            key="selectbox_empreendimento_create_meta"
        )
        input_periodo = st.selectbox("**Período**", options=lista_meses_ano, key="selectbox_periodo_create")
        input_meta    = st.number_input("**Meta**", step=0.01, format="%.2f")

    with col2:
        input_empreendimento = st.selectbox("**Empreendimento**", options=empreendimento_, index=None, placeholder='Selecione o Empreendimento', key="selectbox_empreendimento_create")        
        input_tp_meta        = st.selectbox("**Tipo da Meta**", options=["Quantidade", "Percentual"])
        input_observacao     = st.text_input("**Observação**", key="obs_create_meta")

    input_button_submit = st.button("**Enviar**", key="button_create")
        
    if input_button_submit:

        if input_nm_meta==None or input_empreendimento==None:
            return st.error(f'Não é possível inserir meta sem **Nome da Meta** e/ou **Empreendimento**')

        if cadastrarMetaCon.validacaoInsertMetaEmpreendimento(input_nm_meta, input_empreendimento, input_periodo):
            return st.error(f"Meta do empreendimento **{input_empreendimento}** no período de **{input_periodo}** já lançado!")
        
        if input_meta == "":
            return st.error("O campo da meta está sem valor")

        with st.spinner("Atualizando..."):   
            sistema.nm_meta         = input_nm_meta
            sistema.empreendimento  = input_empreendimento 
            sistema.tp_meta         = input_tp_meta
            sistema.mes_ano         = input_periodo
            sistema.meta            = input_meta
            sistema.observacao      = input_observacao
            sistema.user            = user
            cadastrarMetaCon.insertMetas(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Meta do empreendimento **{input_empreendimento}** no período de **{input_periodo}** lançada!") 
        time.sleep(2)
        success_container.empty()