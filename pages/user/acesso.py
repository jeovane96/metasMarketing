import streamlit as st
import time
import psycopg2
import controllers.database as db


def verificar_usuario(email, senha):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    cursor.execute("SELECT senha FROM tb_usuario WHERE email = %s AND senha = %s", (email, senha))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    # Se encontrou o usuário com e-mail e senha corretos, retorna True
    return resultado is not None




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
            </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="title-container"><h1>''</h1></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 4, 3])
        with col1:
            None

        with col2:
            email        = st.text_input("**E-mail**", key="login_email")
            password     = st.text_input("**Senha**", type="password", key="login_password")
            login_button = st.button("Entrar")

            if login_button:
                with st.spinner("Autenticando..."):
                    autenticado = verificar_usuario(email, password)
                    time.sleep(3)

                if autenticado:
                    st.session_state["authenticated"] = True
                    st.session_state["user"] = email

                    email = email.upper()
                    success_placeholder.success(f"Bem-vindo, **{email.upper()}** !")
                    # success_placeholder.markdown(
                    #     f"""
                    #     <div style="
                    #         padding: 10px;
                    #         border-radius: 5px;
                    #         --background-color: #F6FFD5; /* Cor verde personalizada */
                    #         color: black; /* Texto branco */
                    #         text-align: center;
                    #         font-weight: bold;">
                    #         <span style="color: black;">Bem-vindo, {email} !</span>
                    #     </div>
                    #     """,
                    #     unsafe_allow_html=True
                    # )
                    time.sleep(3)
                    success_placeholder.empty()  
                    login_placeholder.empty()  

                    return True  
                else:
                    st.error("E-mail ou senha inválidos.")

            return False
        
        with col3:
            None
