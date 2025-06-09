import streamlit as st
import models.sistema as sistema
import time
from datetime import datetime

import controllers.suprimentos.cadastrarContratos.cadastrarContratosCon as cadastrarContratosCon
import controllers.suprimentos.cadastrarContratos.listarContratosCon as listarContratosCon


def createContratos():

    user = st.session_state.get("user", "")

    def ListContratosFiltro():
        customerList = []

        for item in listarContratosCon.selecionarTodosContratosFiltro():
            customerList.append((item.cd_empresa, item.nu_contrato))
            
        return customerList

    empresa_contratos = ListContratosFiltro() 
        
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        input_empresa = st.selectbox("**Empresa**", options=sorted(set([empresa[0] for empresa in empresa_contratos])), index=0, placeholder="Escolha a Empresa")

    with col2:
        input_contratos = st.selectbox("**Contrato**", options=sorted(set([contratos[1] for contratos in empresa_contratos])), index=0, placeholder="Escolha o Contrato") 

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
            sistema.cd_empresa           = input_empresa
            sistema.nu_contrato          = input_contratos
            sistema.vl_orcamento         = input_vl_orcamento 
            sistema.vl_primeira_proposta = input_vl_primeira_proposta
            sistema.user_insert          = user
            cadastrarContratosCon.insertContratos(sistema)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Contrato nº **{input_contratos}** lançado!") 
        time.sleep(2)
        success_container.empty()