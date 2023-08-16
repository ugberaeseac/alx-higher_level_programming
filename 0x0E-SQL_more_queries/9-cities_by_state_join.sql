-- script that lists all cities contained in the database hbtn_0d_usa.
-- each record should display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- you can use only one SELECT statement

SELECT cities.id, cities.name, states.	name
FROM states
JOIN cities
WHERE state_id = states.id
ORDER BY cities.id ASC;
