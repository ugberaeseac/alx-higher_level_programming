-- script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa
-- The states table contains only one record where name = California
-- (but the id can be different)
-- results must be sorted in ascending order by cities.id

SELECT id, name
FROM cities
WHERE state_id = (SELECT id
	FROM states
	WHERE name = 'california')
GROUP BY cities.id
ORDER BY cities.id ASC;
