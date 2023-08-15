-- script that lists the score and the name records of the table second_table
-- if score >=10 in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
