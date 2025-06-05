import database_sienge   as sienge
import database_sistema as sistema
import pandas as pd
import psycopg2


def consultaContratosSuprimentos():
    conn   = psycopg2.connect(**sienge.db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT cdempresa, nucontrato FROM emedcontrato GROUP BY cdempresa, nucontrato ORDER BY nucontrato;")
    consulta = cursor.fetchall()

    # Pegando os nomes reais das colunas
    colunas = [desc.name for desc in cursor.description]

    # Criando o DataFrame corretamente
    df = pd.DataFrame(consulta, columns=colunas)

    cursor.close()
    conn.close()

    return df

contratos_suprimentos_sienge = consultaContratosSuprimentos()

def integracaoContratosSuprimentos():
    conn   = psycopg2.connect(**sistema.db_config)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tb_bi_suprimentos_contratos_sienge")

    for index, row in contratos_suprimentos_sienge.iterrows():
        cursor.execute("INSERT INTO tb_bi_suprimentos_contratos_sienge (cd_empresa, nu_contrato) VALUES (%s, %s)", (row["cdempresa"], row["nucontrato"]))
        print(f"Inserido: {row['nucontrato']}")

    conn.commit()

    cursor.close()
    conn.close()

integracaoContratosSuprimentos()