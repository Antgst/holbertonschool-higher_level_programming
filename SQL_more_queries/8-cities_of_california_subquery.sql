-- Task 8: List all cities of California without using JOIN

-- Select cities linked to the state named California, ordered by cities.id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
