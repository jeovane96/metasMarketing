import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2

def selecionarContratos():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            id, 
            cd_empresa,    
            nu_contrato,         
            vl_orcamento,        
            vl_primeira_proposta,      
            user_insert,  
            TO_CHAR(dt_insert, 'DD/MM/YYYY') AS dt_insert     
        FROM
            tb_bi_suprimentos_contratos
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(
            sistema.suprimentos_contratos(
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


def selecionarTodosContratosFiltro():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT cd_empresa, nu_contrato FROM tb_bi_suprimentos_contratos_sienge")
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.suprimentos_contratos(row[0], row[1], "", "", "", ""))

    return customerList