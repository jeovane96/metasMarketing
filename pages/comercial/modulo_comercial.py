import pages.comercial.cadastroMetas.createMetas    as createMetas
import pages.comercial.cadastroMetas.listMetas      as listMetas
import streamlit                                    as st
import pages.user.createUserArea                    as createUserArea
import controllers.user.usuarioCon                  as usuarioCon

def acesso_tela_comercial():

    user             = st.session_state.get("user", "")
    area_selecionada = st.session_state.get("area_acesso", "")
    perfil           = usuarioCon.selecionar_perfil_usuario_area(user, area_selecionada)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    st.sidebar.markdown('<div class="sidebar-title">COMERCIAL</div>', unsafe_allow_html=True)

    metas_button   = st.sidebar.button("📊 Metas",   use_container_width=True)
    acesso_button  = st.sidebar.button("**🗝️ Acessos**", use_container_width=True)

    placeholder = st.empty()

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = ""

    if metas_button:
        st.session_state["active_page"] = "telaMetas"
        st.rerun()

    if acesso_button:
        st.session_state["active_page"] = "telaAcessos"
        st.rerun()

    # Renderiza a tela atual dentro do placeholder
    with placeholder:
        if st.session_state["active_page"] == "telaMetas":
            inserir, consultar = st.tabs(["Inserir", "Consultar"])
            with inserir:
                createMetas.createMeta()
            with consultar:
                listMetas.ListMetas()

        elif st.session_state["active_page"] == "telaAcessos" and perfil == "Admin":
            inserir, = st.tabs(["Inserir"])
            with inserir:
                createUserArea.Incluir_usuario()
        elif perfil != "Admin":
            st.error("Usuário não tem perfil de **Administrador**")