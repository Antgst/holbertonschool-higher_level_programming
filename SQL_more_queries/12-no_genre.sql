-- Task 12: List all shows in hbtn_0d_tvshows without a genre linked.

-- Lists tv_shows.title and tv_show_genres.genre_id for shows with no genre (NULL), sorted by title and genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
