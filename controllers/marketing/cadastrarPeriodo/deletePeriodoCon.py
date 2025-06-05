import streamlit as st
from datetime import timedelta
import controllers.database as db
import psycopg2


def deletePeriodo(user, mes_ano):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            UPDATE 
                tb_bi_periodo
            SET
                in_ativo  = 'N',
                user_insert      = %s,
                dt_insert = CURRENT_TIMESTAMP
            WHERE           
                mes_ano = %s
            """, (user, mes_ano)
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()