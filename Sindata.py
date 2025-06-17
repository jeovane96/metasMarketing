import streamlit                            as st
import pages.user.acesso                    as ValidacaoUsuario

import pages.marketing.modulo_marketing     as modulo_marketing
import pages.suprimentos.modulo_suprimentos as modulo_suprimentos
import pages.comercial.modulo_comercial     as modulo_comercial

# create_tbl.criar_tabelas_db()

# --- Define layout baseado no login ---
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon=".streamlit/alvo.png")

# Exibir a logo
st.markdown("""
    <div style="
        background-color: #F2F2F2;
        display: flex; 
        align-items: center; 
        justify-content: center;
        gap: 15px; 
        margin-top: -90px; /* Ajuste para subir mais */
        margin-bottom: 10px;
    ">
        <img src="https://i0.wp.com/catagua.com.br/wp-content/uploads/2019/12/catagua-solucoes-imobiliarias.png?w=1280&ssl=1" 
             alt="Logo Catagua" style="width: 180px; height: auto;">
        <h1 style="margin: 0; ; color: black;"">| SINDATA</h1>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Esconder a barra branca do Streamlit */
    header { visibility: hidden; }

    /* Animação de brilho do título */
    @keyframes glow {
        0% { text-shadow: 0 0 5px #fff, 0 0 10px #CCCCCC, 0 0 15px #D2FED8; }
        50% { text-shadow: 0 0 10px #fff, 0 0 20px #CCCCCC, 0 0 30px #D2FED8; }
        100% { text-shadow: 0 0 5px #fff, 0 0 10px #CCCCCC, 0 0 15px #D2FED8; }
    }

    /* Estilizar o título */
    .glowing-text {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: white;
        animation: glow 5s infinite alternate;
        margin: -30px 0 -50px 0 !important;
        line-height: 1;
    }

    /* Cor de fundo da aplicação */
    .stApp { 
        background: linear-gradient(135deg, #F2F2F2, #F2F2F2, #F2F2F2); 
    }

    /* Estilizar os botões */
    .stButton button {
        border: 2px solid white;
        background-color: #DDEBF7;
        color: black;
        padding: 5px 12px;
        border-radius: 15px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.3s ease;
        width: 180px !important;
        height: 35px !important;
    }

    .stButton button:hover {
        background-color: black;
        border-color: #D9D9D9;
        color: white;
    }

    /* Remover efeito vermelho ao clicar */
    .stButton button:focus, .stButton button:active {
        outline: none !important;
        box-shadow: none !important;
        background-color: black !important;
        border-color: black !important;
        color: white !important;
    }

    /* Ajuste do layout das abas */
    div[data-testid="stTab"] { background-color: transparent; }

    button[data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px 10px 0 0;
        background-color: #D9D9D9;
        color: black;
        padding: 10px 20px;
        transition: 0.3s;
    }

    /* Aba ativa */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: black;
        color: white;
        border-bottom: 2px solid white;
    }

    /* Hover nas abas */
    button[data-baseweb="tab"]:hover { background-color: #B0B0B0; }

    /* Rodapé fixo */
    .fixed-footer {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 5px 10px;
        border-radius: 5px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        font-size: 14px;
        z-index: 1000;
    }

    /* Nome do usuário no canto direito */
    .header-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 10px 10px;
    }

    .user-info {
        font-size: 14px;
        font-weight: normal;
        color: #CBCBCB;
    }
            
    /* Estilizando SOMENTE o campo de input */
    div.stTextInput input {
        background-color: white !important; /* Fundo branco */
        color: black !important; /* Texto preto */
    }

    /* Estilizando SOMENTE o selectbox */
    div[data-baseweb="select"] div {
        background-color: white !important; /* Fundo branco */
        color: black !important;
    }
            
                       
    /* Estilizando SOMENTE o number_input (st.number_input) */
    div.stNumberInput input[type="number"] {
        background-color: white !important;
        color: black !important;
    }
            
    /* Estiliza o campo de data para ficar igual aos outros inputs */
    div[data-baseweb="input"] input[type="text"] {
        background-color: white !important;
        color: black !important;
        border-radius: 10px !important;  /* ajuste conforme o raio dos outros campos */
        padding: 0.5rem !important;
        border: none !important;
        box-shadow: none !important;
    }
        
    /* Fundo da sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, #203764, #203764, #203764);
        width: 212px !important;
        min-width: 270px !important;
        max-width: 212px !important;
        resize: none !important;
        overflow: hidden !important;
    }
        
    /* Título da sidebar */
    .sidebar-title {
        color: white;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
    }
            
    /* Somente os botões da sidebar */
    section[data-testid="stSidebar"] button {
        font-size: 12px !important;
        padding: 8px 15px !important;
        width: 100% !important;
        height: auto !important;
    }      
            
    </style>

""", unsafe_allow_html=True)

if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.sidebar.markdown(f"""
        <style>
            .sidebar-footer {{
                position: fixed;
                bottom: 15px;
                left: 15px;
                color: #CCCCCC;
                font-size: 13px;
                z-index: 100;
            }}

            /* Garante que o footer fique dentro da sidebar */
            section[data-testid="stSidebar"] > div:after {{
                content: "";
                display: block;
                height: 60px; /* espaço reservado para o footer */
            }}
        </style>

        <div class="sidebar-footer">
            🔑 {st.session_state.get("user", "")}
        </div>
        """, unsafe_allow_html=True
    )

# Pequeno espaço para ajuste
st.write("")

user             = st.session_state.get("user", "")
area_selecionada = st.session_state.get("area_acesso", "")

if ValidacaoUsuario.authenticate_user():
    if "just_logged_in" not in st.session_state:
        st.session_state["just_logged_in"] = True
        st.rerun()

    if area_selecionada == "Marketing":
        modulo_marketing.acesso_tela_mkt()

    elif area_selecionada == "Suprimentos":
        modulo_suprimentos.acesso_tela_suprimentos()

    elif area_selecionada == "Comercial":
        modulo_comercial.acesso_tela_comercial()
        
    elif area_selecionada == "Relatório":
        pass
    
    else:
        st.error(f"Módulo do **{area_selecionada}** em manutenção")
        st.stop()