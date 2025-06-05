# database_sqlserver.py

import pyodbc

# Configurações do banco SQL Server
db_config = {
    'DRIVER': '{ODBC Driver 17 for SQL Server}',
    'SERVER': '192.168.145.31',
    'DATABASE': 'CataguaDB',
    'UID': 'AppPowerBI',
    'PWD': 'qD6WJA3Isg31%IN'
}

def connect():
    try:
        conn_str = (
            f"DRIVER={db_config['DRIVER']};"
            f"SERVER={db_config['SERVER']};"
            f"DATABASE={db_config['DATABASE']};"
            f"UID={db_config['UID']};"
            f"PWD={db_config['PWD']}"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print("Erro ao conectar ao SQL Server:", e)
        return None
