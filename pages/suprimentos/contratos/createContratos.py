import streamlit as st
import models.sistema as sistema
import controllers.suprimentos.cadastrarContratosCon as cadastrarContratosCon
import controllers.suprimentos.cadastrarContratosCon.listarContratos as listarContratos
import time
from datetime import datetime

def createContratos():

    user = st.session_state.get("user", "")

    def ListContratosFiltro():
        customerList = []

        for item in listarContratos.selecionarTodosContratosFiltro():
            customerList.append((item.cd_empresa, item.nu_contrato))
            
        return customerList

    empresa_contratos = ListContratosFiltro() 
        
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        input_empresa = st.selectbox("**Empresa**", options=list(set([empresa[0] for empresa in empresa_contratos])), index=0, placeholder="Escolha a Empresa")

    with col2:
        input_contratos = st.selectbox("**Contrato**", options=list(set([contratos[1] for contratos in empresa_contratos])), index=0, placeholder="Escolha o Contrato") 

    with col3:
        input_vl_orcamento = st.number_input("**Orçamento**", step=0.01, format="%.2f")

    with col4:
        input_vl_primeira_proposta  = st.number_input("**Primeira Proposta**", step=0.01, format="%.2f")

    input_button_submit = st.button("**Enviar**", key="button_create_contratos")
        
    if input_button_submit:

        if input_contratos == None:
            return st.error(f'Contrato sem ID**')

        if input_vl_orcamento == None:
            return st.error("Não é possível lançar sem valor de Orçamento")
        
        if input_vl_primeira_proposta == None:
            return st.error("O campo da primeira proposta está sem valor")

        with st.spinner("Atualizando..."):   
            sistema.cd_empresa      = input_empresa
            sistema.nu_contrato     = input_contratos
            sistema.empreendimento  = input_vl_orcamento 
            sistema.tp_meta         = input_vl_primeira_proposta
            sistema.user            = user
            cadastrarContratosCon.insertContratos(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Contrato nº **{input_contratos}** lançado!") 
        time.sleep(2)
        success_container.empty()