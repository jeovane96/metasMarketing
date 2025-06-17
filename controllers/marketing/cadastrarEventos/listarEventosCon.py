import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db

def selecionarEventos():
    conn = db.connect_integracoes()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            CAST(id AS UNSIGNED)                AS id,
            IFNULL(evento, '')                  AS evento,
            IFNULL(projeto, '')                 AS projeto,
            CASE 
                WHEN id_fila IS NULL THEN ''
                WHEN id_fila = 0 THEN ''
                ELSE CAST(id_fila AS CHAR)
            END AS id_fila,
            CASE 
                WHEN id_empreendimento IS NULL THEN ''
                WHEN id_empreendimento = 0 THEN ''
                ELSE CAST(id_empreendimento AS CHAR)
            END AS id_empreendimento
        FROM
            tb_eventos_auten
        ORDER BY
            id DESC;
    """)
    customerList = []

    for row in cursor.fetchall():
        customerList.append(
            sistema.eventos_auten(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )
        )
    
    return customerList