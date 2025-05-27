import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarPeriodo():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            id,         
            periodo,    
            mes_ano,    
            observacao,
            user_insert,
            TO_CHAR(dt_insert, 'DD/MM/YYYY') AS dt_insert     
        FROM
            tb_periodo
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(
            sistema.periodo(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )
        )
    
    return customerList