import streamlit                              as st
import controllers.user.usuarioCon            as usuarioCon
import pages.user.createUserArea              as createUserArea

import pages.suprimentos.contratos.createContratos as createContratos
import pages.suprimentos.contratos.listContratos   as listContratos

def acesso_tela_suprimentos():

    user             = st.session_state.get("user", "")
    area_selecionada = st.session_state.get("area_acesso", "")
    perfil           = usuarioCon.selecionar_perfil_usuario_area(user, area_selecionada)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    st.sidebar.markdown('<div class="sidebar-title">SUPRIMENTOS</div>', unsafe_allow_html=True)

    contratos_button = st.sidebar.button("**📃 Contratos**",   use_container_width=True)
    acesso_button    = st.sidebar.button("**🗝️ Acessos**", use_container_width=True)

    placeholder = st.empty()

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = ""

    if contratos_button:
        st.session_state["active_page"] = "telaContratos"
        st.rerun()

    if acesso_button:
        st.session_state["active_page"] = "telaAcessos"
        st.rerun()

    # Renderiza a tela atual dentro do placeholder
    with placeholder:
        if st.session_state["active_page"] == "telaContratos":
            inserir, excluir, consultar = st.tabs(["Inserir", "Excluir", "Consultar"])
            with inserir:
                createContratos.createContratos()
            with excluir:
                pass
            with consultar:
                listContratos.ListContratos()

        elif st.session_state["active_page"] == "telaAcessos" and perfil == "Admin":
            inserir, = st.tabs(["Inserir"])
            with inserir:
                createUserArea.Incluir_usuario()
        elif perfil == "Operador":
            pass