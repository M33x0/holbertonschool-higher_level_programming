-- 16. List shows and genres
-- list all shows and all genres linked to that show from db hbtn_od_tvshows
SELECT		s.title, g.name
FROM		tv_shows AS s
			LEFT JOIN tv_show_genres AS sg
			ON s.id = sg.show_id
			LEFT JOIN tv_genres AS g
			ON sg.genre_id =  g.id
ORDER BY	s.title ASC,
			g.name ASC;