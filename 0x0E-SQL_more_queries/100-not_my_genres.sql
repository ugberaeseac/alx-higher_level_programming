-- script that uses the hbtn_0d_tvshows database to list
-- all genres not linked to the show Dexter
-- the tv_shows table contains only one record where title = Dexter
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- use a maximum of two SELECT statement

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name ASC;
