-- Task 16: List all shows and all genres linked to each show (NULL if no genre).

-- Displays tv_shows.title and tv_genres.name sorted by title ASC, name ASC.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
