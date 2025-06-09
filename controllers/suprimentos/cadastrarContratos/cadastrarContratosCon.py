import streamlit as st
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertContratos(insert_contratos):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_bi_suprimentos_contratos(
                cd_empresa,
                nu_contrato,         
                vl_orcamento,        
                vl_primeira_proposta,    
                user_insert                      
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s,
                %s
            )""",
            (   
                insert_contratos.cd_empresa,
                insert_contratos.nu_contrato,         
                insert_contratos.vl_orcamento,        
                insert_contratos.vl_primeira_proposta,    
                insert_contratos.user_insert 
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()