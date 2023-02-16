-- list all genres of the show Dexter
SELECT
	g.name
FROM
	tv_genres g
JOIN
	tv_show_genres sg
JOIN
	tv_shows s
ON
	g.id = sg.genre_id AND s.id = show_id
WHERE
	s.title = 'Dexter'
ORDER BY
	g.name ASC;
