import streamlit as st
import controllers.database as db

def insertEventos(insert_eventos):
    conn = db.connect_integracoes()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO tb_eventos_auten (
                evento, 
                projeto, 
                id_fila, 
                id_empreendimento
            ) 
            VALUES (
                %s,
                %s, 
                %s, 
                %s
            )
        """, (
            insert_eventos.nm_evento,
            insert_eventos.nm_projeto,
            insert_eventos.id_fila,
            insert_eventos.id_empreendimento
        ))
        conn.commit()

    except Exception as e:
        st.error(f"Erro ao inserir evento: {e}")

    finally:
        cursor.close()
        conn.close()
