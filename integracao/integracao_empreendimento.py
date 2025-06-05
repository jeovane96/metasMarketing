import database_dw_cv   as dw_cv
import database_sistema as sistema
import pandas as pd
import psycopg2


def consultaEmpreendimento():
    conn   = psycopg2.connect(**dw_cv.db_config)
    cursor = conn.cursor()
    cursor.execute("select distinct(empreendimento_ultimo) AS empreendimento from leads where empreendimento_ultimo <> ''  order by empreendimento_ultimo asc;")
    consulta = cursor.fetchall()

    # Pegando os nomes reais das colunas
    colunas = [desc.name for desc in cursor.description]

    # Criando o DataFrame corretamente
    df = pd.DataFrame(consulta, columns=colunas)

    cursor.close()
    conn.close()

    return df

empreendimento_sienge = consultaEmpreendimento()

def integracaoEmpreendimento():
    conn   = psycopg2.connect(**sistema.db_config)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tb_bi_empreendimento")

    for index, row in empreendimento_sienge.iterrows():
        cursor.execute("INSERT INTO tb_bi_empreendimento (empreendimento) VALUES (%s)", (row["empreendimento"],))
        print(f"Inserido: {row['empreendimento']}")

    conn.commit()

    cursor.close()
    conn.close()

integracaoEmpreendimento()