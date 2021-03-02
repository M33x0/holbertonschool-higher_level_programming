-- 9. Cities by States
-- List cities containing in the db hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;