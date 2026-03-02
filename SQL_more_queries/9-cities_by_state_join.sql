-- Task 9: List all cities with their state names

-- Display cities.id, cities.name, and states.name ordered by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;
