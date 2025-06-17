import streamlit as st
import controllers.database as db

def deleteEventos(id):
    conn = db.connect_integracoes()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            DELETE FROM
                tb_eventos_auten 
            WHERE
                id = %s
        """, (id,))
        conn.commit()

    except Exception as e:
        st.error(f"Erro ao inserir evento: {e}")

    finally:
        cursor.close()
        conn.close()
