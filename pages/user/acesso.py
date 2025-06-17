import streamlit as st
import time
import controllers.user.usuarioCon as usuarioCon

# Função para autenticação no Streamlit
def authenticate_user():

    if st.session_state.get("authenticated", False):  
        return True

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    login_placeholder   = st.empty()  
    success_placeholder = st.empty()  

    with login_placeholder.container():
        st.markdown(""" 
            <style>
            .title-container { display: flex; justify-content: center; text-align: center; height: 10vh; }
            .title-container h1 { font-size: 2em; }
            body {
                background: linear-gradient(180deg, #002f6c, #001b3a);
                height: 100vh;
            }
            </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="title-container"><h1>''</h1></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 4, 3])
        with col1:
            None

        with col2:
            email        = st.text_input("**E-mail**", key="login_email").lower()
            password     = st.text_input("**Senha**", type="password", key="login_password")
            area_acesso  = st.selectbox("**Área**", options=["Financeiro", "Recursos Humanos", "Suprimentos", "Engenharia", "Marketing", "Comercial", "Assistência Técnica"])
            login_button = st.button("Entrar")

            if login_button:
                with st.spinner("Autenticando..."):
                    autenticado_usuario      = usuarioCon.verificar_usuario(email, password)
                    autenticado_usuario_area = usuarioCon.verificar_usuario_area(email, area_acesso)
                    time.sleep(3)

                if not autenticado_usuario_area:
                    st.error('Usuário não tem acesso a área selecionada')
                    st.stop()

                if autenticado_usuario:
                    st.session_state["authenticated"] = True
                    st.session_state["user"]          = email
                    st.session_state["area_acesso"]   = area_acesso

                    email = email.upper()
                    success_placeholder.success(f"Bem-vindo, **{email.upper()}** !")
                    time.sleep(3)
                    success_placeholder.empty()  
                    login_placeholder.empty()  
                
                    return True  
                else:
                    st.error("E-mail ou senha inválidos.")

            return False
        
        with col3:
            None
