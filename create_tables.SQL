
CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS industries (
    id SERIAL PRIMARY KEY,
    industry VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS target_types (
    id SERIAL PRIMARY KEY,
    type VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS target_location (
    id SERIAL PRIMARY KEY,
    city_id INTEGER REFERENCES cities(id),
    country_id INTEGER REFERENCES countries(id)
);


CREATE TABLE IF NOT EXISTS coordinates (
    id SERIAL PRIMARY KEY,
    lat FLOAT,
    lon FLOAT
);


CREATE TABLE IF NOT EXISTS targets (
    id SERIAL PRIMARY KEY,
    coordinates_id INTEGER REFERENCES coordinates(id),
    location_id INTEGER REFERENCES target_location(id),
    type_id INTEGER REFERENCES target_types(id),
    industry_id INTEGER REFERENCES industries(id),
    priority INTEGER
);
