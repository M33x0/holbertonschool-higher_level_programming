-- 8. Cities of California
-- List all cities of Cali that can be found in db hbtn_0d_usa
SELECT DISTINCT cities.id, cities.name,
FROM cities, states,
WHERE cities.state_id =
(
	SELECT states.id,
	FROM states
	WHERE states.name = "California"
)
ORDER BY cities.id ASC;