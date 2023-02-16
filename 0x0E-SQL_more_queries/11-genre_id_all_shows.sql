-- lists all show in database
-- show NULL for show with no genre
SELECT
	s.title,
	g.genre_id
FROM
	tv_shows s
LEFT JOIN
	tv_show_genres g
ON
	s.id = g.show_id
ORDER BY
	s.title ASC,
	g.genre_id ASC;
