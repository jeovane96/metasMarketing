import streamlit as st
# import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2


def insertMetas(insert_metas):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    try:
        cursor.execute(""" 
            INSERT INTO tb_metas_(
                nm_meta,
                empreendimento,
                meta,           
                mes_ano,    
                observacao,    
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
                insert_metas.nm_meta,
                insert_metas.empreendimento,
                insert_metas.meta,          
                insert_metas.mes_ano,       
                insert_metas.observacao,    
                insert_metas.user  
            )
        )
        conn.commit()
    
    except psycopg2.OperationalError as e:
        st.error(f"Erro no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()


def validacaoInsertMetaEmpreendimento(nm_meta, empreendimento, mes_ano):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    query  = "SELECT * FROM tb_metas WHERE nm_meta =%s AND empreendimento =%s AND mes_ano =%s"
    cursor.execute(query, (nm_meta, empreendimento, mes_ano))
    validacao = cursor.fetchall()
    conn.commit()
    return validacao