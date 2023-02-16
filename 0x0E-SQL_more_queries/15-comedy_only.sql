-- lists all the Comedy show
SELECT
	s.title
FROM
	tv_shows s
JOIN
	tv_show_genres sg
JOIN
	tv_genres g
ON
	s.id = sg.show_id AND g.id = sg.genre_id
WHERE
	g.name = 'Comedy'
ORDER BY
	s.title ASC;
