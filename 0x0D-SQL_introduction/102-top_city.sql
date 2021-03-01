-- Script that displays top 3 of city temp during july and Aug ordered by temp (DESC)
SELECT city, AVG(value)
AS avg_temp FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
