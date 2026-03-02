-- Task 15: List the number of records with the same score

-- Count records grouped by score and order by number descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
