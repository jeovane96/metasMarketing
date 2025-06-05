import pandas as pd
import psycopg2
import database_sid as sid
import database_sistema as sistema

def consultaUsuario():
    conn = sid.connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT LTRIM(RTRIM(nm_email)) AS nm_email, LTRIM(RTRIM(pw_senha)) AS pw_senha FROM Sistema_usuario WHERE nm_email <> '' AND sn_ativo = '1'")
    consulta = cursor.fetchall()

    consulta_tuplas = [tuple(row) for row in consulta]
    colunas         = [desc[0] for desc in cursor.description]
    df              = pd.DataFrame(consulta_tuplas, columns=colunas)
    
    cursor.close()
    conn.close()

    return df

usuario_sid = consultaUsuario()

def integracaoUsuario():
    conn   = psycopg2.connect(**sistema.db_config)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tb_bi_usuario")

    for index, row in usuario_sid.iterrows():
        cursor.execute(
            "INSERT INTO tb_bi_usuario (email, senha) VALUES (%s, %s)",
            (row["nm_email"], row["pw_senha"])
        )
        print(f"Inserido: {row['nm_email']}")

    conn.commit()
    cursor.close()
    conn.close()

integracaoUsuario()
