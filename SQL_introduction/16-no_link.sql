-- Task 16: List records with a non-empty name, ordered by score descending

-- Display score and name for rows where name is not NULL and not empty
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
