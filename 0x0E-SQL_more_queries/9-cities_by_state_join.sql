-- list all cities contained in database
-- join cities with states table
SELECT
	c.id, c.name, s.name
FROM
	cities c
INNER JOIN
	states s
ON
	c.state_id = s.id;
