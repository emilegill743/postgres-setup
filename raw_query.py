from sqlalchemy import create_engine

# Connecting to Postgres
connection_uri = 'postgresql://postgres:test@localhost:5432/covid-19'
engine = create_engine(connection_uri)

with engine.connect() as con:
    result = con.execute(
                """
                SELECT
                    countries_and_territories,
                    SUM(cases) AS cases,
                    SUM(deaths) AS deaths
                FROM worldwide_cases
                GROUP BY countries_and_territories
                ORDER BY cases DESC
                """
                )
    
for row in result.fetchall():
    print(row)
    