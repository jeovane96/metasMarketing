import streamlit as st
import models.sistema as sistema
from datetime import timedelta
import controllers.database as db
import psycopg2
import pandas as pd

def selecionarTodosUsuarios():
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM tb_bi_usuario ORDER BY email ASC")
    customerList = []

    for row in cursor.fetchall():
        customerList.append(sistema.user(row[0], "", "", "", ""))

    return customerList

def verificar_usuario(email, senha):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    cursor.execute("SELECT senha FROM tb_bi_usuario WHERE email = %s AND senha = %s", (email, senha))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    return resultado is not None

def verificar_usuario_area(email, area):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM tb_bi_usuario_area WHERE email = %s AND area_acesso = %s", (email, area))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    return resultado is not None

def selecionar_usuario_area_acesso(email):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    cursor.execute("SELECT area_acesso FROM tb_bi_usuario_area WHERE email = %s", (email,))
    resultado = cursor.fetchall()

    # Dê nome à coluna ao criar o DataFrame
    df = pd.DataFrame(resultado, columns=["area_acesso"])

    cursor.close()
    conn.close()

    return df["area_acesso"]


def selecionar_perfil_usuario_area(email, area_acesso):
    conn   = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    cursor.execute("SELECT perfil FROM tb_bi_usuario_area WHERE email = %s and area_acesso = %s", (email, area_acesso))
    resultado = cursor.fetchone()

    # Dê nome à coluna ao criar o DataFrame
    df = pd.DataFrame(resultado, columns=["perfil"])

    cursor.close()
    conn.close()

    return resultado[0] if resultado else None