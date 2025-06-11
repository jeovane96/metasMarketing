from sqlalchemy import create_engine

db_url = "postgresql://postgres:postgres@192.168.125.36:5432/DW_HUB"

engine = create_engine('postgresql://postgres:postgres@192.168.125.36:5432/DW_HUB')