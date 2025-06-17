import streamlit as st
import models.sistema as sistema
import controllers.marketing.cadastrarEventos.deletarEventoCon as deletarEventoCon
import time

def deleteEventos():
       
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        input_id  = st.text_input("**ID Evento**", key="id_evento")
        
    with col2:
        pass

    with col3:
        pass

    with col4:
        pass

    with col5:
        pass
         
    input_button_submit = st.button("**Enviar**", key="button_delete")
        
    if input_button_submit:

        if input_id==None:
            return st.error("Não é possível deletar com campo **NULO**")

        with st.spinner("Atualizando..."):   
            sistema.id = input_id
            deletarEventoCon.deleteEventos(input_id)
            time.sleep(2) 

        success_container = st.empty()
        st.success(f"Evento **{input_id}** deletado!") 
        time.sleep(2)
        success_container.empty()