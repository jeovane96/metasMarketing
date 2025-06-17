import streamlit as st
import models.sistema as sistema
from models.sistema import eventos_auten
import controllers.marketing.cadastrarEventos.cadastrarEventosCon as cadastrarEventosCon
import time

def createEventos():
       
    col1, col2 = st.columns(2)

    with col1:
        input_nm_evento  = st.text_input("**Evento**", key="evento")
        input_id_fila    = st.text_input("**ID Fila**", key="id_fila")  
        
    with col2:
        input_nm_projeto        = st.text_input("**Projeto**", key="projeto")  
        input_id_empreendimento = st.text_input("**ID Empreendimento**", key="empreendimento")   
         
    input_button_submit = st.button("**Enviar**", key="button_create")
        
    if input_button_submit:

        if input_nm_evento==None or input_id_fila==None or input_nm_projeto==None or input_id_empreendimento==None:
            return st.error("Não é possível lançar campo **NULO**")

        with st.spinner("Atualizando..."):   
            evento = eventos_auten(
                id                = None,
                nm_evento         = input_nm_evento,
                nm_projeto        = input_nm_projeto,
                id_fila           = int(input_id_fila),
                id_empreendimento = int(input_id_empreendimento)
            )
            cadastrarEventosCon.insertEventos(evento) 
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Evento **{input_nm_evento}** lançado!") 
        time.sleep(2)
        success_container.empty()