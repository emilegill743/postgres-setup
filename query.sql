SELECT
    countries_and_territories,
    SUM(cases) AS cases,
    SUM(deaths) AS deaths
FROM worldwide_cases
GROUP BY countries_and_territories
ORDER BY cases DESC