-- script that lists the score and the name records of the table second_table
-- if score >=10 in descending order
SELECT score, name
FROM second_table
ORDER BY score DESC
WHERE score >= 10;
