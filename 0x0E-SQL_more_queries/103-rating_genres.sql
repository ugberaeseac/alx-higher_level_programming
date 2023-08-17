-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- each record should display: tv_genres.name - rating sum
-- results must be sorted in descending order by the rating
-- use only one SELECT statement

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_genres
INNER JOIN tv_show_ratings
ON tv_genres.id = tv_show_ratings.genre_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
