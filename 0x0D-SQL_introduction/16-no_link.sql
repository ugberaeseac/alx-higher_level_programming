-- script that lists all records of the table
-- lists only rows with name value
-- result set displays score and the name in this order
-- and in descending order of the score
SELECT score, name
FROM second_table
WHERE `name` IS NOT NULL AND `name` != ""
GROUP BY score, name
ORDER BY score DESC;
