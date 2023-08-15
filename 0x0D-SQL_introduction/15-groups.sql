-- script that lists the number of records with the same score in the table
-- The result set should display the score and the number of records same score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
