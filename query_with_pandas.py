from sqlalchemy import create_engine
import pandas as pd
import os

# Connecting to Postgres
connection_uri = 'postgresql://postgres:test@localhost:5432/covid-19'
engine = create_engine(connection_uri)

# Reading our SQL script
script_name = 'query.sql'
dirname = os.path.dirname(__file__)
sql_file = os.path.join(dirname, script_name)
sql = open(sql_file, 'r').read()

# Reading query result into DataFrame
df = pd.read_sql(sql, engine)
print(df.head())