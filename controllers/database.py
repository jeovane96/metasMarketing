import pymysql

db_url = "postgresql://postgres:postgres@192.168.125.36:5432/DW_HUB"

def connect_integracoes():
    return pymysql.connect(
        host='integracoes.catagua.com.br',
        user='catagua',
        password='4W8j~#o&xA',
        db='integracoes',
        port=3306
    )