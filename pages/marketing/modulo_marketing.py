import pages.marketing.metas.createMetas      as createMetas
import pages.marketing.metas.importarMetas    as importarMetas
import pages.marketing.metas.listMetas        as listMetas
import pages.marketing.periodo.createPeriodo  as createPeriodo
import pages.marketing.periodo.listPeriodo    as listPeriodo
import pages.marketing.periodo.deletePeriodo  as deletePeriodo
import streamlit                              as st
import pages.user.createUserArea              as createUserArea
import controllers.user.usuarioCon            as usuarioCon


def acesso_tela_mkt():

    user             = st.session_state.get("user", "")
    area_selecionada = st.session_state.get("area_acesso", "")
    perfil           = usuarioCon.selecionar_perfil_usuario_area(user, area_selecionada)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    st.sidebar.markdown('<div class="sidebar-title">MARKETING</div>', unsafe_allow_html=True)

    metas_button   = st.sidebar.button("**🎯 Metas**",   use_container_width=True)
    periodo_button = st.sidebar.button("**📆 Período**", use_container_width=True)
    acesso_button  = st.sidebar.button("**🗝️ Acessos**", use_container_width=True)

    placeholder = st.empty()

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = ""

    if metas_button:
        st.session_state["active_page"] = "telaMetas"
        st.rerun()

    if periodo_button:
        st.session_state["active_page"] = "telaPeriodo"
        st.rerun()

    if acesso_button:
        st.session_state["active_page"] = "telaAcessos"
        st.rerun()

    # Renderiza a tela atual dentro do placeholder
    with placeholder:
        if st.session_state["active_page"] == "telaMetas":
            inserir, excluir, consultar = st.tabs(["Inserir", "Excluir", "Consultar"])
            with inserir:
                # createMetas.createMeta()
                importarMetas.importMeta()
            with excluir:
                pass
            with consultar:
                listMetas.ListMetas()

        elif st.session_state["active_page"] == "telaPeriodo":
            inserir, excluir, consultar = st.tabs(["Inserir", "Excluir", "Consultar"])
            with inserir:
                createPeriodo.createPeriodo()
            with excluir:
                deletePeriodo.deletePeriodo()
            with consultar:
                listPeriodo.ListPeriodo()

        elif st.session_state["active_page"] == "telaAcessos" and perfil == "Admin":
            inserir, = st.tabs(["Inserir"])
            with inserir:
                createUserArea.Incluir_usuario()
        elif perfil != "Admin":
            st.error("Usuário não tem perfil de **Administrador**")