from sqlalchemy import engine, URL
import json
import duckdb

# with open('credentials.json') as f:
#     credentials = json.load(f)

# connection_url = URL.create(
#         drivername="postgresql+psycopg2",
#         username = credentials['username'],
#         password = credentials['password'],
#         host = credentials['host'],
#         port = credentials['port']
#     )

# def set_connection(): 
#     from sqlalchemy import engine
#     engine =  engine.create_engine(connection_url)
#     pg = engine.connect()

#     return pg

db_file = 'my.db'

def set_connection():
    with duckdb.connect(database=db_file) as duck:
        return duck

