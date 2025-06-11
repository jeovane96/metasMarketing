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
            TO_CHAR(periodo, 'DD/MM/YYYY') AS periodo,    
            mes_ano, 
            CASE
                WHEN in_ativo = 'S' THEN 'Sim'
                WHEN in_ativo = 'N' THEN 'Não'
            END AS in_ativo,   
            observacao,
            user_insert,
            TO_CHAR(dt_insert, 'DD/MM/YYYY') AS dt_insert     
        FROM
            tb_bi_periodo
        ORDER BY
            periodo ASC
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
                row[5],
                row[6]
            )
        )
    
    return customerList