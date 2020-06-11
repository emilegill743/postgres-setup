from sqlalchemy import create_engine, MetaData, Table
import pandas as pd
import os

# Connecting to Postgres
connection_uri = 'postgresql://postgres:test@localhost:5432/covid-19'
engine = create_engine(connection_uri)

# Reading CSV dataset into pandas DataFrame
dirname = os.path.dirname(__file__)
csv_path = os.path.join(dirname, 'data.csv')

df = pd.read_csv(csv_path)

# Rename columns
metadata = MetaData()
table_obj = Table('worldwide_cases', metadata, autoload=True, autoload_with=engine)
columns = [col.name for col in table_obj.columns]
df.columns = columns

# Load DataFrame into Postgres database
df.to_sql(
    name='worldwide_cases',
    con=engine,
    if_exists='append',
    index=False)