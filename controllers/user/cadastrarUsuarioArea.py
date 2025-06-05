import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def insertUsuarioArea(insert_usuario_area):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_bi_usuario_area(
                email,
                area_acesso,
                perfil,
                user_insert                  
            ) 
            VALUES(
                %s,
                %s,
                %s,
                %s
            )""",
            (   
                insert_usuario_area.email,
                insert_usuario_area.area_acesso,
                insert_usuario_area.perfil,
                insert_usuario_area.user_insert
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()