-- lists all genres with number of shows
SELECT
	g.name as genre,
	COUNT(g.name) AS 'number_of_shows'
FROM
	tv_genres g
JOIN
	tv_show_genres sg
ON
	g.id = sg.genre_id
GROUP BY
	g.name
ORDER BY
	`number_of_shows` DESC;
