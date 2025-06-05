import psycopg2
import streamlit as st
import controllers.database as db

def insertMetas(mes_ano):
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            DELETE FROM 
                tb_bi_metas
            WHERE           
                mes_ano = %s
        """, (mes_ano,))
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()
