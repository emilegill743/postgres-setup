from sqlalchemy import create_engine
import os

# Connecting to Postgres
connection_uri = 'postgresql://postgres:test@localhost:5432/covid-19'
engine = create_engine(connection_uri)

# Reading our SQL script
script_name = 'create_table.sql'
dirname = os.path.dirname(__file__)
sql_file = os.path.join(dirname, script_name)

sql = open(sql_file, 'r').read()

try:
    # Executing SQL commands
    with engine.connect() as con:
        con.execute(sql)
    print(f'Successfully executed {script_name}')

except Exception as err:
    print(f'Failed to execute {script_name}')
    print(f'Error:\n{err}')


    


