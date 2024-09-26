INSERT INTO countries (name)
SELECT DISTINCT target_country
FROM mission
WHERE target_country IS NOT NULL;

INSERT INTO cities (name)
SELECT DISTINCT target_city
FROM mission
WHERE target_city IS NOT NULL;

INSERT INTO target_types (type)
SELECT DISTINCT target_type
FROM mission
WHERE target_type IS NOT NULL;

INSERT INTO industries (industry)
SELECT DISTINCT target_industry
FROM mission
WHERE target_industry IS NOT NULL;

INSERT INTO coordinates (lat, lon)
SELECT DISTINCT target_latitude, target_longitude
FROM mission
WHERE target_latitude IS NOT NULL AND target_longitude IS NOT NULL;

INSERT INTO target_location (city_id, country_id)
SELECT DISTINCT
    ci.id,
    co.id
FROM mission m
JOIN cities ci ON m.target_city = ci.name
JOIN countries co ON m.target_country = co.name
WHERE m.target_city IS NOT NULL AND m.target_country IS NOT NULL;

INSERT INTO targets (coordinates_id, location_id, type_id, industry_id, priority, mission_id)
SELECT
    c.id AS coordinates_id,
    tl.id AS location_id,
    tt.id AS type_id,
    i.id AS industry_id,
    m.target_priority::INTEGER AS priority,
    m.mission_id
FROM
    mission m
JOIN coordinates c ON m.target_latitude = c.lat AND m.target_longitude = c.lon
JOIN target_location tl ON m.target_city = (SELECT name FROM cities WHERE id = tl.city_id)
                        AND m.target_country = (SELECT name FROM countries WHERE id = tl.country_id)
JOIN target_types tt ON m.target_type = tt.type
JOIN industries i ON m.target_industry = i.industry
WHERE
    m.target_latitude IS NOT NULL AND
    m.target_longitude IS NOT NULL AND
    m.target_city IS NOT NULL AND
    m.target_country IS NOT NULL;

