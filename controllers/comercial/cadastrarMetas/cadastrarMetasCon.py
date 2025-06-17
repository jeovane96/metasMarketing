import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertMetas(insert_metas):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_bi_comercial_metas (
                periodo,                   
                empreendimento,            
                agrupamento_empreendimento,
                meta,
                considera_bi,
                user_insert                      
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )""",
            (
                insert_metas.periodo, 
                insert_metas.empreendimento,
                insert_metas.agrupamento_empreendimento,
                insert_metas.meta,
                insert_metas.considera_bi,
                insert_metas.user
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()


def validacaoInsertEmpreendimento(empreendimento, periodo):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    query  = "SELECT * FROM comercial_metas WHERE empreendimento =%s AND periodo =%s"
    cursor.execute(query, (empreendimento, periodo))
    validacao = cursor.fetchall()
    conn.commit()
    return validacao