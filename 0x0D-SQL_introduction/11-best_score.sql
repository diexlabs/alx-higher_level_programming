-- displays records where score >= 10
-- ordered by score DESC
-- selects score, name
SELECT
	score, name
FROM 
	second_table 
WHERE 
	score >= 10
ORDER BY
	score DESC;
