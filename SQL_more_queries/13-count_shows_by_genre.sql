-- Task 13: List all genres and the number of shows linked to each (only genres with at least one show), sorted by number_of_shows DESC.

-- Displays: genre - number_of_shows
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
