-- script that displays the top 3 of cities temperature
-- during JUly and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE `month` = 7 OR `month` = 8
GROUP BY city
ORDER by avg_temp DESC
LIMIT 3;
