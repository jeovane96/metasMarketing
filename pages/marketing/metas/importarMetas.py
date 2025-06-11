import streamlit as st
import models.sistema as sistema
import time
from datetime import datetime
import pandas as pd
import controllers.database as db

def importMeta():
    uploaded_file = st.file_uploader("**Selecione o arquivo .xlsx**", type=["xlsx"])

    if uploaded_file:
        df = pd.read_excel(uploaded_file)

        if st.button("Inserir no DW"):
            try:
                df.to_sql("tb_bi_marketing_metas", db.engine, if_exists='append', index=False)
                success_container = st.empty()
                success_container.success("Metas lançada!")
                time.sleep(3)
                success_container.empty()
            except Exception as e:
                st.error(f"Erro ao inserir no banco de dados, reveja o arquivo Excel!")