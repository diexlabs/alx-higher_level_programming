-- selects all tv shows with at least one genre linked
-- record is sorted on ascending order
-- joins tv_show_genres with tv_shows
SELECT
	s.title,
	g.genre_id
FROM
	tv_shows s
LEFT JOIN
	tv_show_genres g
ON
	s.id = g.show_id
WHERE
	g.genre_id IS NOT NULL
ORDER BY
	s.title ASC,
	g.genre_id ASC;
