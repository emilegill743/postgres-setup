DROP TABLE IF EXISTS worldwide_cases;
CREATE TABLE worldwide_cases (
    date_rep TEXT,
    day TEXT,
    month TEXT,
    year TEXT,
    cases INTEGER,
    deaths INTEGER,
    countries_and_territories TEXT,
    geo_id TEXT,
    country_territory_code TEXT,
    pop_data_2018 BIGINT,
    continent TEXT
);