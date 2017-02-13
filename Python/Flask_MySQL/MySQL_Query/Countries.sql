-- 1
SELECT countries.name as "Country Name", languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY  languages.percentage DESC

-- 2
SELECT countries.name as "Country Name", COUNT(cities.name) as "City Amount"
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.name) DESC

-- 3
SELECT countries.name as "Country Name", cities.name as "City Name", cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC

-- 4
SELECT countries.name as "Country Name", languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC

-- 5
SELECT countries.name as "Country Name", countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000
ORDER BY countries.surface_area DESC

-- 6
SELECT countries.name as "Country Name", countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75
ORDER BY countries.name DESC

-- 7 
SELECT countries.name as "Country Name", cities.name as "City Name", cities.district, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000
ORDER BY cities.population DESC

-- 8
SELECT countries.region, COUNT(countries.name) as "Number of Countries"
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.name) DESC