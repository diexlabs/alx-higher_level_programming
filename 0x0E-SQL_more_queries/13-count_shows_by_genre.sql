-- lists all genres with number of shows
SELECT
	g.name as genre,
	COUNT(g.name) AS 'number_of_shows'
FROM
	tv_show_genres sg
JOIN
	tv_shows s
JOIN
	tv_genres g
ON
	sg.show_id = s.id AND sg.genre_id = g.id
GROUP BY
	g.name
ORDER BY
	`number_of_shows` DESC;
