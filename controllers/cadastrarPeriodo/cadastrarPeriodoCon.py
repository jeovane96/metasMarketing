import streamlit as st
# import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertPeriodo(insert_periodo):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_periodo (
                periodo,         
                mes_ano,    
                observacao,    
                user_insert                      
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s
            )""",
            (
                insert_periodo.periodo_mkt,        
                insert_periodo.mes_ano,       
                insert_periodo.observacao,    
                insert_periodo.user  
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()