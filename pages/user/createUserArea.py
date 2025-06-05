import streamlit as st
import models.sistema as sistema
import pages.user.acesso as acesso
import controllers.user.usuarioCon as UsuarioCon
import controllers.user.cadastrarUsuarioArea as cadastrarUsuarioArea
import controllers.user.usuarioCon as usuarioCon
import time

def Incluir_usuario():  
    
    user = st.session_state.get("user", "")

    area_selecionada = st.session_state.get("area_acesso", "")

    def ListUsuarioFiltro():
        customerList = []

        for item in UsuarioCon.selecionarTodosUsuarios():
            customerList.append(item.email)

        return customerList

    user_ = ListUsuarioFiltro() 

    col1, col2, col3 = st.columns(3)

    with col1:
        input_email  = st.selectbox("**E-mail**", options=user_)

    with col2:
        input_area = st.selectbox("**Área**", options=["Financeiro", "Recursos Humanos", "Suprimentos", "Engenharia", "Marketing", "Comercial", "Assistência Técnica"])    
    
    with col3:
        input_perfil = st.selectbox("**Perfil**", options=["Admin", "Operador"])

    input_button_submit = st.button("**Enviar**", key="button_user")

    usuario_area = usuarioCon.verificar_usuario_area(input_email, input_area)

    if input_button_submit:  

        if usuario_area:
            return st.error("Usuário já atrelado nessa área")
        
        if input_area != area_selecionada:
            return st.error("Você não tem permissão para liberar usuário nesta área")
        
        with st.spinner("Cadastrando usuário..."):
            sistema.email        = input_email 
            sistema.area_acesso  = input_area
            sistema.perfil       = input_perfil
            sistema.user_insert  = user
            cadastrarUsuarioArea.insertUsuarioArea(sistema)
            time.sleep(3)

        success_container = st.empty()
        st.success(f"Usuário **{input_email}** atrelado a área **{input_area.upper()}** com sucesso!" )
        time.sleep(3)
        success_container.empty()