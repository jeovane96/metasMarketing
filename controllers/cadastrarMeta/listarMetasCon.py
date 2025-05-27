import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarMetas():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            id,     
            nm_meta,       
            empreendimento,        
            mes_ano, 
            tp_meta,
            ROUND(meta::numeric, 2) AS meta,       
            observacao,    
            user_insert,  
            TO_CHAR(dt_insert, 'DD/MM/YYYY') AS dt_insert     
        FROM
            tb_metas
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(
            sistema.metas(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8]
            )
        )
    
    return customerList