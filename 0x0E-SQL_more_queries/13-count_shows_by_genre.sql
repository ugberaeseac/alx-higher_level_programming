-- script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
-- each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- first column must be called genre and second column must be called number_of_shows
-- don’t display a genre that doesn’t have any shows linked
-- results must be sorted in descending order by the number of shows linked
-- use only one SELECT statement

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
	FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
