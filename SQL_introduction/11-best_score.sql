-- Task 11: List all records with score >= 10 ordered by score (top first)

-- Display score and name where score is at least 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
