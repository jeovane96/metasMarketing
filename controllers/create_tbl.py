import streamlit as st
import psycopg2
import controllers.database as db

def criar_tabelas_db():
    conn = psycopg2.connect(db.db_url)
    cursor = conn.cursor()

    try:
        # cursor.execute('''drop TABLE tb_bi_periodo''')
        # cursor.execute('''drop TABLE tb_bi_metas''')
        # cursor.execute('''drop TABLE tb_bi_empreendimento''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_bi_periodo (
                id          SERIAL PRIMARY KEY,
                periodo     TIMESTAMP NOT NULL,
                mes_ano          TEXT     NULL,
                in_ativo    TEXT NOT NULL DEFAULT 'S',
                observacao  TEXT     NULL,
                user_insert TEXT NOT NULL,
                dt_insert   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_periodo' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_bi_metas (
                id               SERIAL PRIMARY KEY,
                nm_meta          TEXT     NULL, 
                empreendimento   TEXT     NULL,
                tp_meta          TEXT     NULL,
                meta             NUMERIC(10,2) NOT NULL,
                mes_ano          TEXT     NULL,
                observacao       TEXT     NULL,
                user_insert      TEXT NOT NULL,
                dt_insert        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_metas' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_bi_usuario_area (
                id            SERIAL PRIMARY KEY,
                email         TEXT NOT  NULL, 
                area_acesso   TEXT NOT NULL,
                perfil        TEXT NOT  NULL,
                user_insert   TEXT NOT NULL,
                dt_insert     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_bi_usuario_area' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_bi_empreendimento (
                id              SERIAL PRIMARY KEY,
                empreendimento  TEXT NOT NULL
            )''')
        print("Tabela 'empreendimento' criada com sucesso.")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_bi_suprimentos_contratos (
                id                    SERIAL PRIMARY KEY,
                cd_empresa            TEXT NOT  NULL, 
                nu_contrato           TEXT NOT  NULL, 
                vl_orcamento          NUMERIC(10,2) NOT NULL,
                vl_primeira_proposta  NUMERIC(10,2) NOT NULL,
                user_insert           TEXT NOT NULL,
                dt_insert             TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours'
            )''')
        print("Tabela 'tb_bi_suprimentos_contratos' criada com sucesso.")

    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_bi_comercial_metas (
                id                          SERIAL PRIMARY KEY,
                periodo                     TEXT NOT NULL,
                empreendimento              TEXT NOT NULL,
                agrupamento_empreendimento  TEXT NOT NULL,
                meta                        INT NOT NULL,
                considera_bi                TEXT NOT NULL,
                dt_insert                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP - INTERVAL '3 hours',
                user_insert                 TEXT NOT NULL
            )''')
        print("Tabela 'tb_bi_comercial_metas' criada com sucesso.")


    except psycopg2.Error as e:
        print(f"Erro ao criar tabelas: {e}")

    conn.commit()
    conn.close()